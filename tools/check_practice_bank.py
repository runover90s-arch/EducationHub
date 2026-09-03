#!/usr/bin/env python3
"""Kiểm tra cấu trúc ngân hàng bài tập Vật lí 11.

Không thay thế thẩm định học thuật thủ công, nhưng bắt các lỗi xuất bản thường gặp:
- thiếu cặp Bài tập / Đáp án;
- số câu giữa đề và lời giải không khớp;
- trắc nghiệm thiếu A–D;
- câu trùng nguyên văn;
- bài học thiếu liên kết sang luyện tập;
- thuật ngữ mức độ còn để tiếng Anh;
- ngân hàng bị giảm số lượng ngoài ý muốn.
"""
from __future__ import annotations
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
GRADE=ROOT/'docs/physics/high-school/grade-11'
MIN_TOTAL=500

errors=[]
questions_seen={}
total=0
pairs=0

for ex in sorted(GRADE.glob('[0-9][0-9]-*/practice/*/exercises.md')):
    sol=ex.with_name('solutions.md')
    if not sol.exists():
        errors.append(f'Thiếu lời giải: {sol.relative_to(ROOT)}')
        continue
    et=ex.read_text(encoding='utf-8')
    st=sol.read_text(encoding='utf-8')
    qheads=list(re.finditer(r'^### Câu (\d+)\b.*$',et,re.M))
    sheads=list(re.finditer(r'^## Câu (\d+)\b.*$',st,re.M))
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

    # Multiple choice section must have 4 options per question in that section.
    mA=re.search(r'^## Phần A .*?$(.*?)(?=^## Phần B|^## Phần C|^## Phần D|\Z)',et,re.M|re.S)
    if mA:
        block=mA.group(1)
        hs=list(re.finditer(r'^### Câu \d+.*$',block,re.M))
        for i,h in enumerate(hs):
            body=block[h.end(): hs[i+1].start() if i+1<len(hs) else len(block)]
            for opt in 'ABCD':
                if not re.search(rf'(^|\n){opt}\.\s',body):
                    errors.append(f'Trắc nghiệm thiếu phương án {opt}: {ex.relative_to(ROOT)}')
                    break

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

print(f'[practice] {pairs} bộ bài tập theo bài, {total} câu/bài mới.')
if errors:
    for e in errors: print('ERROR PRACTICE001:',e)
    print(f'[practice] {len(errors)} lỗi.')
    raise SystemExit(1)
print('[practice] 0 lỗi cấu trúc. OK.')
