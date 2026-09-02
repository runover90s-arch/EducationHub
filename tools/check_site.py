#!/usr/bin/env python3
"""Quality gate for Education Hub Markdown and MkDocs.

Checks source Markdown for common MathJax/Arithmatex mistakes, suspicious
layout-only display math, and broken internal .md links. By default it also
runs `mkdocs build --strict` in a temporary directory.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile

import yaml
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

LATEX_COMMAND = re.compile(
    r"\\(?:alpha|beta|gamma|delta|Delta|theta|lambda|mu|pi|rho|sigma|"
    r"omega|Omega|varphi|phi|Phi|frac|dfrac|tfrac|sqrt|sin|cos|tan|cot|"
    r"le|leq|ge|geq|neq|approx|cdot|times|vec|overrightarrow|boxed|text|"
    r"mathrm|left|right|quad|qquad|begin|end)\b"
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
SINGLE_SYMBOL_RE = re.compile(r"^[A-Za-z](?:_[A-Za-z0-9{}]+)?$")


@dataclass
class Issue:
    path: Path
    line: int
    code: str
    message: str
    severity: str = "ERROR"

    def render(self) -> str:
        rel = self.path.relative_to(ROOT)
        return f"{self.severity} {self.code} {rel}:{self.line}: {self.message}"


def strip_inline_code(line: str) -> str:
    """Blank inline-code spans while preserving approximate positions."""
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)


def outside_math_segments(line: str, in_display: bool) -> tuple[list[str], bool, bool]:
    """Return text outside math plus updated display state and inline balance."""
    segments: list[str] = []
    current: list[str] = []
    i = 0
    in_inline = False
    inline_unbalanced = False

    while i < len(line):
        if line.startswith("$$", i):
            if not in_inline:
                if not in_display:
                    segments.append("".join(current))
                    current = []
                    in_display = True
                else:
                    in_display = False
                i += 2
                continue
        ch = line[i]
        if ch == "$" and (i == 0 or line[i - 1] != "\\") and not in_display:
            if not in_inline:
                segments.append("".join(current))
                current = []
                in_inline = True
            else:
                in_inline = False
            i += 1
            continue
        if not in_display and not in_inline:
            current.append(ch)
        i += 1

    if not in_display and not in_inline:
        segments.append("".join(current))
    if in_inline:
        inline_unbalanced = True
    return segments, in_display, inline_unbalanced


def lint_markdown(path: Path) -> list[Issue]:
    issues: list[Issue] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    fence = ""
    in_display = False
    command_display = False
    display_start = 0
    display_body: list[str] = []

    for lineno, original in enumerate(lines, 1):
        m = FENCE_RE.match(original)
        if m:
            marker = m.group(1)
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = ""
            continue
        if in_fence:
            continue

        line = strip_inline_code(original)

        for token in (r"\(", r"\)", r"\[", r"\]"):
            if token in line:
                issues.append(
                    Issue(path, lineno, "MATH001", f"Không dùng delimiter thô {token}; dùng $...$ hoặc $$...$$.")
                )

        # Capture display blocks for layout linting.
        count_display = line.count("$$")
        if in_display and count_display == 0:
            display_body.append(line)
        if count_display:
            parts = line.split("$$")
            for idx, part in enumerate(parts):
                if in_display:
                    display_body.append(part)
                if idx < len(parts) - 1:
                    if not in_display:
                        in_display = True
                        display_start = lineno
                        display_body = []
                    else:
                        body = " ".join(display_body).strip()
                        compact = re.sub(r"\s+", "", body)
                        if SINGLE_SYMBOL_RE.fullmatch(compact):
                            issues.append(
                                Issue(
                                    path,
                                    display_start,
                                    "LAYOUT001",
                                    "Khối công thức chỉ có một kí hiệu; nên viết inline để tránh khoảng trắng lớn.",
                                    "WARNING",
                                )
                            )
                        in_display = False
                        display_body = []

        # Analyze commands outside math independently.
        segments, command_display, inline_unbalanced = outside_math_segments(line, command_display)
        if inline_unbalanced:
            issues.append(Issue(path, lineno, "MATH002", "Dấu $ inline không cân bằng trên cùng một dòng."))
        for segment in segments:
            match = LATEX_COMMAND.search(segment)
            if match:
                issues.append(
                    Issue(
                        path,
                        lineno,
                        "MATH003",
                        f"Lệnh LaTeX {match.group(0)} đang nằm ngoài vùng toán.",
                    )
                )
                break

    if in_display:
        issues.append(Issue(path, display_start or len(lines), "MATH004", "Khối $$ chưa được đóng."))

    issues.extend(check_links(path, lines))
    return issues


def check_links(path: Path, lines: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    in_fence = False
    fence = ""
    for lineno, line in enumerate(lines, 1):
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = ""
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(line):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target.endswith(".md"):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            try:
                resolved.relative_to(DOCS.resolve())
            except ValueError:
                issues.append(Issue(path, lineno, "LINK002", f"Liên kết thoát khỏi docs/: {target}"))
                continue
            if not resolved.is_file():
                issues.append(Issue(path, lineno, "LINK001", f"Không tìm thấy file đích: {target}"))
    return issues



def check_mkdocs_config() -> list[Issue]:
    issues: list[Issue] = []
    config_path = ROOT / "mkdocs.yml"
    try:
        data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        return [Issue(config_path, 1, "YAML001", f"mkdocs.yml không hợp lệ: {exc}")]

    def walk_nav(node):
        if isinstance(node, str):
            yield node
        elif isinstance(node, list):
            for item in node:
                yield from walk_nav(item)
        elif isinstance(node, dict):
            for value in node.values():
                yield from walk_nav(value)

    for target in walk_nav(data.get("nav", [])):
        if not isinstance(target, str) or not target.endswith(".md"):
            continue
        resolved = DOCS / target
        if not resolved.is_file():
            issues.append(Issue(config_path, 1, "NAV001", f"Nav trỏ tới file không tồn tại: {target}"))

    for key in ("extra_css", "extra_javascript"):
        for target in data.get(key, []) or []:
            if not isinstance(target, str) or target.startswith(("http://", "https://")):
                continue
            resolved = DOCS / target
            if not resolved.is_file():
                issues.append(Issue(config_path, 1, "ASSET001", f"{key} trỏ tới file không tồn tại: {target}"))
    return issues

def run_mkdocs_build() -> int:
    if shutil.which("mkdocs") is None:
        print("ERROR BUILD001: Không tìm thấy lệnh mkdocs. Hãy chạy: pip install -r requirements.txt")
        return 1
    with tempfile.TemporaryDirectory(prefix="education-hub-check-") as tmp:
        cmd = ["mkdocs", "build", "--strict", "--clean", "--site-dir", tmp]
        print("\n[build] " + " ".join(cmd))
        result = subprocess.run(cmd, cwd=ROOT)
        return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm tra Markdown, LaTeX, link và MkDocs của Education Hub.")
    parser.add_argument("--lint-only", action="store_true", help="Không chạy mkdocs build --strict.")
    args = parser.parse_args()

    paths = sorted(DOCS.rglob("*.md"))
    issues: list[Issue] = []
    for path in paths:
        issues.extend(lint_markdown(path))
    issues.extend(check_mkdocs_config())

    errors = [i for i in issues if i.severity == "ERROR"]
    warnings = [i for i in issues if i.severity == "WARNING"]

    print(f"[lint] Đã kiểm tra {len(paths)} file Markdown.")
    for issue in issues:
        print(issue.render())
    print(f"[lint] {len(errors)} lỗi, {len(warnings)} cảnh báo.")

    status = 1 if errors else 0
    if not args.lint_only:
        status = max(status, run_mkdocs_build())

    if status == 0:
        print("\nOK: Education Hub vượt qua toàn bộ kiểm tra bắt buộc.")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
