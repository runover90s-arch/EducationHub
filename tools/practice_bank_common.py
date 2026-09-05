from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import math
import re

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
        '> Hệ bài tập được biên soạn theo các dạng xuất hiện trong bộ tài liệu Vật lí 11 của dự án. Câu hỏi được giữ ngắn, trực tiếp; độ khó tăng dần và không cố tình thêm dữ kiện gây nhiễu.',
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
