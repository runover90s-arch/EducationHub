from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import math
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]
GRADE = ROOT / 'docs/physics/high-school/grade-11'

@dataclass
class Problem:
    kind: str  # mcq, tf, short, applied
    question: str
    solution: str
    level: str


def vn(x: float, digits: int = 3) -> str:
    if abs(x - round(x)) < 10**(-(digits+1)):
        s = str(int(round(x)))
    else:
        s = f"{x:.{digits}f}".rstrip('0').rstrip('.')
    return s.replace('.', ',')


def slug_title(md_path: Path) -> str:
    text = md_path.read_text(encoding='utf-8')
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.M)
    return m.group(1) if m else md_path.stem


def normalize_choice_blocks(markdown: str) -> str:
    """Render MCQ and true/false choices as stable Markdown blocks.

    Blank lines are used instead of trailing-space hard breaks so formatters
    cannot silently collapse A-D or a-d statements back into one paragraph.
    """
    marker = re.compile(r'^(?:[A-D]\.|[a-d]\))\s+')
    out: list[str] = []
    for raw_line in markdown.strip().splitlines():
        line = raw_line
        if marker.match(raw_line.rstrip()):
            line = raw_line.rstrip()
            if out and out[-1] != '':
                out[-1] = out[-1].rstrip()
                out.append('')
        out.append(line)
    return '\n'.join(out)


def render_exercises(title: str, theory_rel: str, problems: list[Problem]) -> str:
    groups = [
        ('mcq', 'Phần A — Trắc nghiệm 4 lựa chọn'),
        ('tf', 'Phần B — Đúng/Sai'),
        ('short', 'Phần C — Trả lời ngắn'),
        ('applied', 'Phần D — Vận dụng và vận dụng cao'),
    ]
    out = [
        '---',
        f'title: "Bài tập — {title}"',
        'description: "Bài tập luyện tập theo đúng nội dung bài học, phân hóa từ nền tảng đến vận dụng cao."',
        'tags:',
        '  - physics',
        '  - grade-11',
        '  - exercises',
        '---',
        '',
        f'# Bài tập — {title}',
        '',
        f'[← Trở lại bài học]({theory_rel})',
        '',
    ]
    n = 0
    for kind, heading in groups:
        ps = [p for p in problems if p.kind == kind]
        if not ps:
            continue
        out += [f'## {heading}', '']
        for p in ps:
            n += 1
            out += [f'### Câu {n} — {p.level}', '', normalize_choice_blocks(p.question), '']
    out += ['---', '', '[Đáp án và lời giải →](solutions.md)', '']
    return '\n'.join(out)


def render_solutions(title: str, problems: list[Problem]) -> str:
    out = [
        '---',
        f'title: "Đáp án và lời giải — {title}"',
        'description: "Đáp án được kiểm tra lại; câu khó có lời giải chi tiết và nêu rõ lựa chọn phương pháp."',
        'tags:',
        '  - physics',
        '  - grade-11',
        '  - solutions',
        '---',
        '',
        f'# Đáp án và lời giải — {title}',
        '',
        '> Câu nền tảng được giải vừa đủ để kiểm tra cách làm. Câu vận dụng được trình bày chi tiết hơn để người học thấy được đường suy luận, điều kiện dùng công thức và bước kiểm tra kết quả.',
        '',
        '[← Bài tập](exercises.md)',
        '',
    ]
    for i, p in enumerate(problems, 1):
        out += [f'## Câu {i}', '', p.solution.strip(), '']
    out += ['---', '', '[← Bài tập](exercises.md)', '']
    return '\n'.join(out)


def write_lesson_practice(chapter: str, lesson_file: str, problems: list[Problem]) -> tuple[Path, Path]:
    chdir = GRADE / chapter
    theory = chdir / lesson_file
    title = slug_title(theory)
    stem = lesson_file[:-3]
    pdir = chdir / 'practice' / stem
    pdir.mkdir(parents=True, exist_ok=True)
    ex = pdir / 'exercises.md'
    sol = pdir / 'solutions.md'
    theory_rel = f'../../{lesson_file}'
    ex.write_text(render_exercises(title, theory_rel, problems), encoding='utf-8')
    sol.write_text(render_solutions(title, problems), encoding='utf-8')
    return ex, sol


def add_practice_links(chapter: str, lesson_file: str) -> None:
    path = GRADE / chapter / lesson_file
    text = path.read_text(encoding='utf-8')
    stem = lesson_file[:-3]
    marker = '<!-- LESSON_PRACTICE_LINKS -->'
    block = f'''\n\n{marker}\n## Luyện tập sau bài\n\n- [Bài tập theo bài](practice/{stem}/exercises.md)\n- [Đáp án và lời giải](practice/{stem}/solutions.md)\n'''
    if marker in text:
        text = re.sub(r'\n*<!-- LESSON_PRACTICE_LINKS -->.*?(?=\n---\n|\Z)', block.rstrip(), text, flags=re.S)
    else:
        # insert before final navigation separator when present
        pos = text.rfind('\n---\n')
        if pos >= 0:
            text = text[:pos] + block + text[pos:]
        else:
            text += block
    path.write_text(text, encoding='utf-8')


def write_practice_index(chapter: str, lesson_files: list[str]) -> None:
    chdir = GRADE / chapter
    ctitle = slug_title(chdir / 'index.md')
    out = [
        '---',
        f'title: "Bài tập theo từng bài — {ctitle}"',
        'description: "Cổng luyện tập theo từng bài, kèm đáp án và lời giải."',
        '---',
        '',
        f'# Bài tập theo từng bài — {ctitle}',
        '',
        'Mỗi bài có **một trang bài tập riêng** và **một trang đáp án/lời giải riêng**. Nên làm bài tập trước, sau đó mới mở lời giải.',
        '',
    ]
    for i, lf in enumerate(lesson_files, 1):
        title = slug_title(chdir / lf)
        stem = lf[:-3]
        out += [
            f'## {title}',
            '',
            f'- [Bài tập](./{stem}/exercises.md)',
            f'- [Đáp án và lời giải](./{stem}/solutions.md)',
            '',
        ]
    (chdir / 'practice').mkdir(exist_ok=True)
    (chdir / 'practice' / 'index.md').write_text('\n'.join(out), encoding='utf-8')


def mcq(q: str, sol: str, level='Mức 1 — Nhận biết') -> Problem:
    return Problem('mcq', q, sol, level)

def tf(q: str, sol: str, level='Mức 2 — Thông hiểu') -> Problem:
    return Problem('tf', q, sol, level)

def short(q: str, sol: str, level='Mức 3 — Vận dụng') -> Problem:
    return Problem('short', q, sol, level)

def applied(q: str, sol: str, level='Mức 4 — Vận dụng cao') -> Problem:
    return Problem('applied', q, sol, level)

# ---------------------------------------------------------------------------
# Deterministic QA helpers shared by the Physics 11 practice-bank checkers.
# Keep these presentation checks syntax-based: semantic suspicions belong in
# warnings so they do not create brittle build failures.
# ---------------------------------------------------------------------------
LOCAL_IMAGE_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)(?:\{[^}]*\})?')
MCQ_LINE_RE = re.compile(r'(?m)^[ \t]*([A-D])\.[ \t]+')
TF_LINE_RE = re.compile(r'(?m)^[ \t]*([a-d])[.)][ \t]+')
MCQ_INLINE_RE = re.compile(r'(?<![\w/])([A-D])\.[ \t]+')
TF_INLINE_RE = re.compile(r'(?<![\w/])([a-d])[.)][ \t]+')


def question_before_solution(block: str) -> str:
    """Return learner-facing question text before the inline solution details."""
    return block.split('??? success "Đáp án và lời giải"', 1)[0]


def markdown_paragraphs(text: str) -> list[str]:
    """Split Markdown into paragraphs using real blank lines."""
    return [p for p in re.split(r'\n[ \t]*\n+', text.strip()) if p.strip()]


def infer_marker_kind(text: str) -> str | None:
    """Infer MCQ/T-F only from visible option markers, not section metadata."""
    mcq = {m.group(1) for m in MCQ_LINE_RE.finditer(text)}
    tf = {m.group(1) for m in TF_LINE_RE.finditer(text)}
    # Complete uppercase answer choices take precedence over lowercase labels
    # used inside matching-column content. Otherwise infer from whichever marker
    # family is actually present.
    if len(mcq) >= 3:
        return 'mcq'
    if len(tf) >= 2 and len(mcq) < 2:
        return 'tf'
    if len(mcq) >= 2 and len(tf) < 2:
        return 'mcq'
    return None


def marker_layout_errors(text: str, kind: str) -> list[str]:
    """Validate A-D or a-d options as one marker per Markdown paragraph."""
    if kind == 'mcq':
        labels = 'ABCD'
        line_re = MCQ_LINE_RE
        inline_re = MCQ_INLINE_RE
        start_re = re.compile(r'^[ \t]*([A-D])\.[ \t]+')
    elif kind == 'tf':
        labels = 'abcd'
        line_re = TF_LINE_RE
        inline_re = TF_INLINE_RE
        start_re = re.compile(r'^[ \t]*([a-d])[.)][ \t]+')
    else:
        return []

    found = [m.group(1) for m in line_re.finditer(text)]
    issues: list[str] = []
    missing = [x for x in labels if x not in found]
    if missing:
        issues.append('thiếu ' + ', '.join(missing))
    duplicated = [x for x in labels if found.count(x) > 1]
    if duplicated:
        issues.append('lặp marker ' + ', '.join(duplicated))

    for paragraph in markdown_paragraphs(text):
        # A Markdown paragraph may contain several physical lines. Multiple
        # line-start choice markers inside one paragraph deterministically mean
        # the choices/statements will render as one clustered paragraph.
        paragraph_labels = []
        for line in paragraph.splitlines():
            m = start_re.match(line)
            if m:
                paragraph_labels.append(m.group(1))
        if len(paragraph_labels) > 1:
            issues.append('nhiều marker trong cùng paragraph: ' + ', '.join(paragraph_labels))
            continue

        # If all markers were typed inline after the stem, line-start detection
        # above reports them as missing. This extra diagnostic is only emitted
        # when at least three inline markers are visible, avoiding false positives
        # from prose that merely refers to another item such as "ở b)".
        inline = [m.group(1) for m in inline_re.finditer(paragraph)]
        if not paragraph_labels and len(set(inline)) >= 3:
            issues.append('phương án/mệnh đề bị ghép vào paragraph đề dẫn: ' + ', '.join(inline))
    return issues


def image_refs(text: str) -> list[str]:
    """Return local/remote Markdown image targets without interpreting paths."""
    return [m.group(1).strip() for m in LOCAL_IMAGE_RE.finditer(text)]


def figure_after_choices(text: str, kind: str) -> bool:
    """True when a figure deterministically occurs after answer markers.

    Prefer line-start markers. For a malformed one-line choice cluster, accept
    inline markers only when at least three distinct labels occur in the same
    paragraph; this avoids treating ordinary point labels such as ``B. Chọn``
    in Vietnamese prose as answer choices.
    """
    line_re = MCQ_LINE_RE if kind == 'mcq' else TF_LINE_RE if kind == 'tf' else None
    inline_re = MCQ_INLINE_RE if kind == 'mcq' else TF_INLINE_RE if kind == 'tf' else None
    if line_re is None or inline_re is None:
        return False
    first_choice = line_re.search(text)
    if first_choice is None:
        for paragraph in markdown_paragraphs(text):
            matches = list(inline_re.finditer(paragraph))
            if len({m.group(1) for m in matches}) >= 3:
                offset = text.find(paragraph)
                first_choice_pos = offset + matches[0].start()
                break
        else:
            return False
    else:
        first_choice_pos = first_choice.start()
    return any(img.start() > first_choice_pos for img in LOCAL_IMAGE_RE.finditer(text))


def labels_share_paragraph(text: str, first: str, second: str) -> bool:
    """Check whether two exact labels render in the same Markdown paragraph."""
    for paragraph in markdown_paragraphs(text):
        if first in paragraph and second in paragraph:
            return True
    return False


def tf_solution_item_issues(solution: str) -> list[str]:
    """Require a-d solution spans to contain a clear verdict and explanation."""
    issues: list[str] = []
    paragraphs = markdown_paragraphs(textwrap.dedent(solution))
    start_re = re.compile(r'^\s*([a-d])[.)]\s+(.*)$', re.S)
    starts: list[tuple[int, str, str]] = []
    for idx, paragraph in enumerate(paragraphs):
        m = start_re.match(paragraph)
        if m:
            starts.append((idx, m.group(1), m.group(2).strip()))

    by_label: dict[str, list[tuple[int, str]]] = {x: [] for x in 'abcd'}
    for idx, label, first_body in starts:
        by_label[label].append((idx, first_body))

    verdict_re = re.compile(
        r'^\*\*(Đúng|Sai|Không xác định(?: duy nhất)?|Không đủ dữ kiện)\.?\*\*\.?\s*(.*)$',
        re.S | re.I,
    )
    start_indices = {idx for idx, _label, _body in starts}
    for label in 'abcd':
        entries = by_label[label]
        if len(entries) != 1:
            issues.append(f'{label}) cần đúng 1 paragraph lời giải, hiện có {len(entries)}')
            continue
        idx, first_body = entries[0]
        vm = verdict_re.match(first_body)
        if not vm:
            issues.append(f'{label}) thiếu verdict Đúng/Sai hoặc kết luận không xác định ở đầu paragraph')
            continue
        next_idx = min((j for j in start_indices if j > idx), default=len(paragraphs))
        continuation = paragraphs[idx + 1:next_idx]
        reasoning = ' '.join([vm.group(2), *continuation])
        # A compact equation is a valid explanation; otherwise require some
        # actual prose beyond the verdict itself.
        cleaned = re.sub(r'!!! warning "Đối chiếu nguồn".*', ' ', reasoning, flags=re.S)
        cleaned = re.sub(r'[`*_#$]', ' ', cleaned)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip(' .;:,-')
        if '=' not in reasoning and len(cleaned) < 8:
            issues.append(f'{label}) có verdict nhưng thiếu giải thích')
    return issues

