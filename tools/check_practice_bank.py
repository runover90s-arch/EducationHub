#!/usr/bin/env python3
"""Kiểm tra cấu trúc ngân hàng bài tập Vật lí 11.

Không thay thế thẩm định học thuật thủ công, nhưng bắt các lỗi xuất bản thường gặp:
- thiếu cặp Bài tập / Đáp án;
- số câu giữa đề và lời giải không khớp;
- trắc nghiệm thiếu A–D hoặc ghép nhiều lựa chọn trong một paragraph;
- Đúng/Sai thiếu a–d hoặc ghép nhiều mệnh đề trong một paragraph;
- hình dữ kiện đặt sau lựa chọn/mệnh đề;
- ghi chú nội bộ project/import lộ ra ở đầu practice page;
- câu trùng nguyên văn;
- bài học thiếu liên kết sang luyện tập;
- thuật ngữ mức độ còn để tiếng Anh;
- ngân hàng bị giảm số lượng ngoài ý muốn.
"""
from __future__ import annotations
from pathlib import Path
import re, sys

from practice_bank_common import figure_after_choices, image_refs, marker_layout_errors, question_before_solution

ROOT=Path(__file__).resolve().parents[1]
GRADE=ROOT/'docs/physics/high-school/grade-11'
MIN_TOTAL=500
MIN_PDF_TOTAL=1600

errors=[]
questions_seen={}
total=0
pairs=0

INTERNAL_NOTE_RE = re.compile(
    r"\b(?:repository|learner-facing|corpus|pipeline|source-id|import report)\b|"
    r"(?:quy trình|ghi chú|lưu ý)[^\n]{0,80}(?:import|nhập từ PDF)|nhập từ PDF",
    re.I,
)


def authored_section(text: str, label: str) -> str:
    m = re.search(rf"^## {re.escape(label)}.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def check_authored_layout(path: Path, text: str, label: str, kind: str) -> None:
    section = authored_section(text, label)
    if not section:
        return
    heads = list(re.finditer(r"^### (?:Câu|Bài) (\d+)\b.*$", section, re.M))
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(section)
        question = question_before_solution(section[head.end():end])
        number = head.group(1)
        for issue in marker_layout_errors(question, kind):
            errors.append(f"Layout {kind} không hợp lệ: {path.relative_to(ROOT)} Bài {number}: {issue}")
        if figure_after_choices(question, kind):
            errors.append(
                f"Hình nằm sau phương án/mệnh đề: {path.relative_to(ROOT)} Bài {number}; "
                "thứ tự phải là đề dẫn -> hình -> lựa chọn/mệnh đề"
            )
        for ref in image_refs(question):
            if ref.startswith(('http://', 'https://', 'data:')):
                continue
            target=(path.parent/ref.split('#',1)[0].split('?',1)[0]).resolve()
            if not target.exists():
                errors.append(f"Ảnh bài biên soạn không tồn tại: {path.relative_to(ROOT)} Bài {number} -> {ref}")


def check_practice_intro(path: Path, text: str) -> None:
    # Only inspect the learner-facing intro before the first H2 section. Provenance
    # inside source comments/solution blocks is intentionally outside this rule.
    body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    intro = body.split("\n## ", 1)[0]
    intro = re.sub(r"<!--.*?-->", " ", intro, flags=re.S)
    hit = INTERNAL_NOTE_RE.search(intro)
    if hit:
        errors.append(
            f"Ghi chú nội bộ learner-facing ở đầu practice page: {path.relative_to(ROOT)} -> {hit.group(0)!r}"
        )

for ex in sorted(GRADE.glob('[0-9][0-9]-*/practice/*/exercises.md')):
    sol=ex.with_name('solutions.md')
    if not sol.exists():
        errors.append(f'Thiếu lời giải: {sol.relative_to(ROOT)}')
        continue
    et=ex.read_text(encoding='utf-8')
    st=sol.read_text(encoding='utf-8')
    qheads=list(re.finditer(r'^### (?:Câu|Bài) (\d+)\b.*$',et,re.M))
    sheads=list(re.finditer(r'^## (?:Câu|Bài) (\d+)\s*$',st,re.M))
    qnums=[int(m.group(1)) for m in qheads]
    snums=[int(m.group(1)) for m in sheads]
    if qnums != list(range(1,len(qnums)+1)):
        errors.append(f'Số câu không liên tục: {ex.relative_to(ROOT)} -> {qnums}')
    if snums != qnums:
        errors.append(f'Số lời giải không khớp: {sol.relative_to(ROOT)} -> đề {qnums}, giải {snums}')
    total += len(qnums); pairs += 1

    # exact duplicate blocks, normalized whitespace
    for i,m in enumerate(qheads):
        start=m.end(); end=qheads[i+1].start() if i+1<len(qheads) else et.find('\n---',start)
        if end<0: end=len(et)
        body=re.sub(r'\s+',' ',et[start:end]).strip()
        key=re.sub(r'\s+',' ',re.sub(r'\$[^$]+\$','<MATH>',body)).strip().lower()
        # Only flag long exact-ish duplicates; short conceptual stems can legitimately recur.
        if len(key)>180:
            prev=questions_seen.get(key)
            if prev:
                errors.append(f'Câu trùng nguyên văn: {ex.relative_to(ROOT)} và {prev}')
            else:
                questions_seen[key]=str(ex.relative_to(ROOT))

    # Deterministic learner-facing layout checks for authored A/B sections.
    check_authored_layout(ex, et, 'Phần A', 'mcq')
    check_authored_layout(ex, et, 'Phần B', 'tf')
    check_practice_intro(ex, et)

# Every theory lesson must link to its practice pair.
for lesson in sorted(GRADE.glob('[0-9][0-9]-*/[0-9][0-9]-*.md')):
    txt=lesson.read_text(encoding='utf-8')
    stem=lesson.stem
    expected=f'practice/{stem}/exercises.md'
    if expected not in txt:
        errors.append(f'Bài học thiếu liên kết Bài tập: {lesson.relative_to(ROOT)}')
    expected2=f'practice/{stem}/solutions.md'
    if expected2 not in txt:
        errors.append(f'Bài học thiếu liên kết Đáp án: {lesson.relative_to(ROOT)}')

# Learner-facing English level terms should not return.
for p in GRADE.rglob('*.md'):
    txt=p.read_text(encoding='utf-8')
    for term in ('Level 1','Level 2','Level 3','Level 4','Level 5','Foundation','Standard','Applied','Enrichment','Prerequisite'):
        if term in txt:
            errors.append(f'Thuật ngữ chưa Việt hóa {term!r}: {p.relative_to(ROOT)}')

if total < MIN_TOTAL:
    errors.append(f'Ngân hàng theo từng bài chỉ còn {total} câu, thấp hơn ngưỡng bảo vệ {MIN_TOTAL}.')

pdf_total=sum(1 for p in GRADE.glob('[0-9][0-9]-*/practice/*/exercises.md') for _ in re.finditer(r'<!-- source-id:',p.read_text(encoding='utf-8')))
if pdf_total < MIN_PDF_TOTAL:
    errors.append(f'Ngân hàng PDF mở rộng chỉ còn {pdf_total} câu, thấp hơn ngưỡng bảo vệ {MIN_PDF_TOTAL}.')
print(f'[practice] {pairs} bộ bài tập theo bài, {total} câu biên soạn trước + {pdf_total} câu nhập từ PDF.')
if errors:
    for e in errors: print('ERROR PRACTICE001:',e)
    print(f'[practice] {len(errors)} lỗi.')
    raise SystemExit(1)
print('[practice] 0 lỗi cấu trúc. OK.')
