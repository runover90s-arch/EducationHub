#!/usr/bin/env python3
"""Quality gate for Physics 11 answers and worked solutions.

The checker covers both layers of the Grade 11 bank:
- authored practice questions, whose solutions exist inline and in solutions.md;
- PDF-imported source questions, whose solutions are kept inline with source ids.

It is a structural/pedagogical gate, not a substitute for independent physics review.
It catches recurring failures such as missing/mismatched solutions, placeholder prose,
empty T/F explanations, under-explained advanced questions and truncated imports.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]
GRADE11 = ROOT / "docs/physics/high-school/grade-11"
PRACTICE_FILES = sorted(GRADE11.glob("[0-9][0-9]-*/practice/*/exercises.md"))
SOURCE_FILES = sorted(GRADE11.rglob("exercises.md"))

SOURCE_RE = re.compile(r"<!-- source-id: ([^ ]+) -->")
NEXT_SOURCE_BAI_RE = re.compile(r"(?m)^#### Bài \d+\s*$")
AUTHORED_HEAD_RE = re.compile(r"(?m)^### (?:Câu|Bài) (\d+)\b([^\n]*)$")
SOLUTION_HEAD_RE = re.compile(r"(?m)^## (?:Câu|Bài) (\d+)\s*$")
SOLUTION_MARK = '??? success "Đáp án và lời giải"'
PLACEHOLDERS = re.compile(
    r"Đối chiếu trực tiếp|Đối chiếu phát biểu|không có lời giải dài|"
    r"các phần còn lại tương tự|TODO:.*(?:đáp án|lời giải)|"
    r"(?:đáp án|lời giải)\s*:\s*\.\.\.",
    re.I,
)
BARE_ITEM = re.compile(r"(?m)^\s{4,}[a-d][.)]\s*$")

errors: list[str] = []
warnings: list[str] = []


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def canonical_solution(text: str) -> str:
    """Normalize presentation-only differences for inline-vs-solutions comparison."""
    text = textwrap.dedent(text).strip()
    text = re.sub(r"\$\$\s*(.*?)\s*\$\$", lambda m: f"${flat(m.group(1))}$", text, flags=re.S)
    text = text.replace("  \n", "\n")
    return flat(text)


def tf_item_count(question: str) -> int:
    return sum(bool(re.search(rf"(?m)^\s*{x}[.)]\s+", question)) for x in "abcd")


def labelled_tf_count(solution: str) -> int:
    return sum(
        bool(re.search(rf"(?m)^\s*{x}[.)]\s*", solution))
        or bool(re.search(rf"\b{x}\)\s*\*\*", solution))
        for x in "abcd"
    )


# ---------------------------------------------------------------------------
# 1) Authored bank: every answer must exist inline AND in solutions.md, agree,
#    and use detail proportional to the declared difficulty.
# ---------------------------------------------------------------------------
authored_blocks = 0
authored_tf = 0
advanced_blocks = 0

for ex in PRACTICE_FILES:
    sol_path = ex.with_name("solutions.md")
    if not sol_path.exists():
        errors.append(f"AUTHORED_MISSING_SOLUTIONS_FILE {sol_path.relative_to(ROOT)}")
        continue

    et = ex.read_text(encoding="utf-8")
    st = sol_path.read_text(encoding="utf-8")
    qheads = list(AUTHORED_HEAD_RE.finditer(et))
    sheads = list(SOLUTION_HEAD_RE.finditer(st))

    separate: dict[int, str] = {}
    for i, h in enumerate(sheads):
        end = sheads[i + 1].start() if i + 1 < len(sheads) else len(st)
        body = st[h.end():end]
        body = re.split(r"(?m)^---\s*$", body)[0]
        separate[int(h.group(1))] = body.strip()

    for i, h in enumerate(qheads):
        n = int(h.group(1))
        meta = h.group(2)
        end = qheads[i + 1].start() if i + 1 < len(qheads) else len(et)
        # The last authored question is followed by the imported source bank. Do not
        # let its many inline solution blocks bleed into the authored question.
        source_section = et.find("\n## Ngân hàng bài tập mở rộng", h.end(), end)
        if source_section >= 0:
            end = source_section
        first_source = et.find("<!-- source-id:", h.end(), end)
        if first_source >= 0:
            end = first_source
        block = et[h.end():end]
        # Source imports are level-4 headings, so ### questions are authored only.
        if block.count(SOLUTION_MARK) != 1:
            errors.append(
                f"AUTHORED_SOLUTION_COUNT {ex.relative_to(ROOT)} Bài {n}: cần đúng 1 khối '{SOLUTION_MARK}'"
            )
            continue

        question, inline = block.split(SOLUTION_MARK, 1)
        inline = re.split(r"(?m)^## ", inline)[0]
        inline_dedented = textwrap.dedent(inline).strip()
        inline_flat = flat(inline_dedented)
        authored_blocks += 1

        if len(inline_flat) < 8:
            errors.append(f"AUTHORED_TOO_SHORT {ex.relative_to(ROOT)} Bài {n}: lời giải gần như trống")
        if PLACEHOLDERS.search(inline_dedented):
            errors.append(f"AUTHORED_PLACEHOLDER {ex.relative_to(ROOT)} Bài {n}")
        if BARE_ITEM.search(inline):
            errors.append(f"AUTHORED_BARE_TF_ITEM {ex.relative_to(ROOT)} Bài {n}")

        sep = separate.get(n)
        if sep is None:
            errors.append(f"AUTHORED_MISSING_SEPARATE {sol_path.relative_to(ROOT)} Bài {n}")
        elif canonical_solution(inline) != canonical_solution(sep):
            errors.append(
                f"AUTHORED_MISMATCH {ex.relative_to(ROOT)} Bài {n}: lời giải inline và solutions.md không đồng nhất"
            )

        mlev = re.search(r"Mức\s*(\d)", meta)
        level = int(mlev.group(1)) if mlev else None
        if level == 4:
            advanced_blocks += 1
            # Advanced questions must show an actual reasoning path, not just an answer key.
            if len(inline_flat) < 100:
                errors.append(
                    f"AUTHORED_ADVANCED_TOO_SHORT {ex.relative_to(ROOT)} Bài {n}: "
                    f"Mức 4 chỉ có {len(inline_flat)} ký tự"
                )
        elif level == 3:
            # A computation may be concise, but must expose at least a formula/equality or reasoning cue.
            if len(inline_flat) < 20 and not any(tok in inline_dedented for tok in ("=", "Suy ra", "Ta có", "Vậy")):
                errors.append(
                    f"AUTHORED_APPLIED_BARE {ex.relative_to(ROOT)} Bài {n}: Mức 3 thiếu bước tính/suy luận"
                )

        items = tf_item_count(question)
        if items >= 3:
            authored_tf += 1
            if labelled_tf_count(inline_dedented) < 3:
                errors.append(
                    f"AUTHORED_TF_INCOMPLETE {ex.relative_to(ROOT)} Bài {n}: thiếu giải thích theo từng ý"
                )
            if len(inline_flat) < 45:
                errors.append(
                    f"AUTHORED_TF_TOO_SHORT {ex.relative_to(ROOT)} Bài {n}: lời giải Đúng/Sai quá ngắn"
                )


# ---------------------------------------------------------------------------
# 2) PDF-source bank: keep the source style but require complete learner-facing
#    explanations and explicit T/F reasoning.
# ---------------------------------------------------------------------------
seen: dict[str, Path] = {}
source_blocks = 0
source_tf = 0

for path in SOURCE_FILES:
    text = path.read_text(encoding="utf-8")
    matches = list(SOURCE_RE.finditer(text))
    for i, m in enumerate(matches):
        source_id = m.group(1)
        source_blocks += 1
        if source_id in seen:
            errors.append(f"SOURCE_DUPLICATE {source_id}: {seen[source_id]} và {path}")
        else:
            seen[source_id] = path

        upper = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        nb = NEXT_SOURCE_BAI_RE.search(text, m.end(), upper)
        end = nb.start() if nb else upper
        block = text[m.start():end]

        if block.count(SOLUTION_MARK) != 1:
            errors.append(f"SOURCE_SOLUTION_COUNT {source_id}: cần đúng 1 khối '{SOLUTION_MARK}'")
            continue

        question, solution = block.split(SOLUTION_MARK, 1)
        solution_flat = flat(solution)

        if "**Hướng dẫn giải:**" not in solution:
            errors.append(f"SOURCE_MISSING_GUIDE {source_id}: thiếu nhãn '**Hướng dẫn giải:**'")
        if len(solution_flat) < 30:
            errors.append(f"SOURCE_TOO_SHORT {source_id}: lời giải chỉ có {len(solution_flat)} ký tự")
        if PLACEHOLDERS.search(solution):
            errors.append(f"SOURCE_PLACEHOLDER {source_id}: còn câu mẫu/placeholder trong lời giải")
        if BARE_ITEM.search(solution):
            errors.append(f"SOURCE_BARE_TF_ITEM {source_id}: còn mục a/b/c/d trống trong lời giải")

        items = tf_item_count(question)
        if items >= 3:
            source_tf += 1
            explicit = bool(re.search(r"\*\*(?:Đáp án|Kết luận)", solution))
            labelled = labelled_tf_count(solution)
            if not explicit and labelled < 3:
                errors.append(f"SOURCE_TF_INCOMPLETE {source_id}: chưa tách kết luận/giải thích đủ các ý Đúng-Sai")
            if len(solution_flat) < 150:
                errors.append(f"SOURCE_TF_TOO_SHORT {source_id}: lời giải Đúng-Sai quá ngắn ({len(solution_flat)} ký tự)")


print(
    f"[solution-quality] Authored: {authored_blocks} bài / {len(PRACTICE_FILES)} bộ, "
    f"{authored_tf} bài Đúng/Sai, {advanced_blocks} bài Mức 4."
)
print(
    f"[solution-quality] PDF source: {source_blocks} khối nguồn, "
    f"{source_tf} bài có cấu trúc Đúng/Sai."
)
print(f"[solution-quality] Tổng phạm vi kiểm tra: {authored_blocks + source_blocks} bài.")
if warnings:
    for w in warnings:
        print("WARNING", w)
if errors:
    for e in errors:
        print("ERROR", e)
    print(f"[solution-quality] {len(errors)} lỗi.")
    sys.exit(1)
print("[solution-quality] 0 lỗi.")
