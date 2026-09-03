#!/usr/bin/env python3
"""QA cho ngân hàng bài tập nhập từ các PDF Vật lí 11.

Mục tiêu:
- không thất lạc cặp đề/đáp án;
- không lặp source-id;
- không sao chép lặp lại cùng một câu vào nhiều bài học;
- mọi ảnh cần để giữ nguyên công thức/hình vẽ phải tồn tại;
- câu Vận dụng cao phải có lời giải đủ dài hoặc ảnh lời giải;
- bảo vệ quy mô ngân hàng khỏi bị giảm ngoài ý muốn.

Checker này kiểm tra tính toàn vẹn xuất bản. Nó không thay thế việc thẩm định học thuật thủ công.
"""
from pathlib import Path
import re, sys, json, unicodedata, hashlib
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
GRADE=ROOT/'docs/physics/high-school/grade-11'
REPORT=ROOT/'tools/v9_import_report.json'
MIN_IMPORTED=1600
errors=[]; warnings=[]
source_seen={}; body_seen={}; imported=0; image_q=0; solution_img=0
by_chapter=Counter(); by_level=Counter(); by_format=Counter(); files=0

def norm_text(s:str)->str:
    s=re.sub(r'<!--.*?-->',' ',s,flags=re.S)
    s=re.sub(r'!\[[^]]*\]\([^)]*\)(?:\{[^}]*\})?',' ',s)
    s=re.sub(r'[`*_#>]',' ',s)
    s=unicodedata.normalize('NFKC',s).lower()
    s=re.sub(r'\s+',' ',s).strip()
    return s

def split_imported(s:str,marker:str):
    return s.split(marker,1)[1] if marker in s else ''

for ex in sorted(GRADE.glob('0[1-4]-*/practice/*/exercises.md')):
    et=ex.read_text(encoding='utf-8')
    sol=ex.with_name('solutions.md')
    old_marker='## Ngân hàng bài tập PDF mở rộng'
    new_marker='## Ngân hàng bài tập mở rộng'
    if old_marker in et:
        marker=old_marker; inline_answers=False
    elif new_marker in et:
        marker=new_marker; inline_answers=True
    else:
        continue
    files+=1
    if not sol.exists():
        errors.append(f'Thiếu file lời giải: {sol.relative_to(ROOT)}')
        continue
    st=sol.read_text(encoding='utf-8')
    es=split_imported(et,marker)

    # Legacy pages keep a separate imported-solution bank. New-format pages keep
    # each answer immediately below the exercise inside a pymdownx.details block.
    if inline_answers:
        ss=''
    else:
        sol_marker='## Đáp án và lời giải — Ngân hàng PDF mở rộng'
        if sol_marker not in st:
            errors.append(f'Thiếu phần lời giải PDF: {sol.relative_to(ROOT)}')
            continue
        ss=split_imported(st,sol_marker)

    em=list(re.finditer(r'^#### Bài(?: PDF)? (\d+)\s*\n\n<!-- source-id: ([^>]+) -->\n\n',es,re.M))
    en=[int(m.group(1)) for m in em]
    if en:
        expected=list(range(en[0],en[0]+len(en)))
        if en != expected:
            errors.append(f'Số bài nhập không liên tục: {ex.relative_to(ROOT)}')
    else:
        errors.append(f'Không tìm thấy bài nhập: {ex.relative_to(ROOT)}')
        continue

    sm=[]
    if not inline_answers:
        sm=list(re.finditer(r'^#### Bài PDF (\d+)\s*$',ss,re.M))
        sn=[int(m.group(1)) for m in sm]
        if en != list(range(1,len(en)+1)):
            errors.append(f'Số Bài PDF legacy không liên tục từ 1: {ex.relative_to(ROOT)}')
        if sn != en:
            errors.append(f'Đề/lời giải PDF lệch số lượng: {ex.relative_to(ROOT)} -> đề {len(en)}, giải {len(sn)}')

    # group-level metadata for level/format
    headings=[]
    for m in re.finditer(r'^### (.+?) — (.+?)\s*$',es,re.M):
        headings.append((m.start(),m.group(1).strip(),m.group(2).strip()))

    # map separate solution blocks for legacy pages
    solblocks={}
    if not inline_answers:
        for i,m in enumerate(sm):
            end=sm[i+1].start() if i+1<len(sm) else len(ss)
            solblocks[int(m.group(1))]=ss[m.end():end]

    for i,m in enumerate(em):
        end=em[i+1].start() if i+1<len(em) else len(es)
        block=es[m.end():end]
        seq=int(m.group(1)); sid=m.group(2).strip(); imported+=1
        mm=re.match(r'BT-Chuong-(I|II|III|IV)-p\d+-q\d+-\d+$',sid)
        if not mm:
            errors.append(f'source-id sai định dạng: {sid}')
            ch='?'
        else:
            ch=mm.group(1); by_chapter[ch]+=1
        if sid in source_seen:
            errors.append(f'source-id lặp: {sid} ở {ex.relative_to(ROOT)} và {source_seen[sid]}')
        else:
            source_seen[sid]=str(ex.relative_to(ROOT))

        # Determine active group heading before block.
        active=[h for h in headings if h[0] < m.start()]
        if active:
            level,fmt=active[-1][1],active[-1][2]
            by_level[level]+=1; by_format[fmt]+=1
        else:
            level=fmt='Không rõ'
            warnings.append(f'Không xác định nhóm mức độ: {ex.relative_to(ROOT)} Bài {seq}')

        # In inline-answer pages only the part before the details block is the question.
        question_block=block.split('??? success "Đáp án và lời giải"',1)[0] if inline_answers else block
        nb=norm_text(question_block)
        if len(nb)>150 and 'công thức/kí hiệu của câu này được giữ nguyên bằng ảnh' not in nb:
            key=hashlib.sha1(nb.encode()).hexdigest()
            if key in body_seen:
                errors.append(f'Câu nhập trùng nguyên văn: {ex.relative_to(ROOT)} Bài {seq} và {body_seen[key]}')
            else:
                body_seen[key]=f'{ex.relative_to(ROOT)} Bài {seq}'

        # image references must resolve relative to file
        for ref in re.findall(r'!\[[^]]*\]\(([^)]+\.webp)\)',question_block):
            target=(ex.parent/ref).resolve()
            if not target.exists():
                errors.append(f'Ảnh bài tập không tồn tại: {ex.relative_to(ROOT)} -> {ref}')
            else:
                image_q+=1

        if inline_answers:
            dm=re.search(r'\?\?\? success "Đáp án và lời giải"\s*\n(.*)',block,re.S)
            if not dm:
                errors.append(f'Thiếu nút đáp án/lời giải: {ex.relative_to(ROOT)} Bài {seq}')
                sb=''
            else:
                sb=dm.group(1)
        else:
            sb=solblocks.get(seq,'')
            for ref in re.findall(r'!\[[^]]*\]\(([^)]+\.webp)\)',sb):
                target=(sol.parent/ref).resolve()
                if not target.exists():
                    errors.append(f'Ảnh lời giải không tồn tại: {sol.relative_to(ROOT)} -> {ref}')
                else:
                    solution_img+=1

        # Vận dụng cao must have an actual explanation.
        if level.startswith('Vận dụng cao'):
            plain=re.sub(r'\*\*Đáp án:\*\*[^\n]*','',sb)
            plain=norm_text(plain)
            if len(plain)<80 and 'source-faithful/' not in sb:
                errors.append(f'Vận dụng cao thiếu lời giải chi tiết: {ex.relative_to(ROOT)} Bài {seq}')

if imported < MIN_IMPORTED:
    errors.append(f'Ngân hàng PDF chỉ còn {imported} câu, thấp hơn ngưỡng bảo vệ {MIN_IMPORTED}.')

# Dạng bài: không cho phép lặp nguyên tên trong cùng bài học.
type_count=0
for lesson in sorted(GRADE.glob('0[1-4]-*/[0-9][0-9]-*.md')):
    txt=lesson.read_text(encoding='utf-8')
    heads=re.findall(r'^###\s+Dạng\s+\d+\s*[—:-]\s*(.+?)\s*$',txt,re.M|re.I)
    type_count += len(heads)
    seen={}
    for h in heads:
        key=unicodedata.normalize('NFKC',h).casefold()
        key=re.sub(r'\s+',' ',key).strip()
        if key in seen:
            errors.append(f'Dạng bài trùng tên trong {lesson.relative_to(ROOT)}: {h!r}')
        else:
            seen[key]=1

if REPORT.exists():
    try:
        rep=json.loads(REPORT.read_text(encoding='utf-8'))
        expected=int(rep.get('deduplicated_verified_imported',-1))
        if expected != imported:
            errors.append(f'Report ghi {expected} câu nhưng repository thực tế có {imported}.')
    except Exception as e:
        errors.append(f'Không đọc được {REPORT.relative_to(ROOT)}: {e}')
else:
    errors.append('Thiếu tools/v9_import_report.json')

CROSS=ROOT/'tools/v9_answer_crosscheck.json'
if CROSS.exists():
    try:
        cross=json.loads(CROSS.read_text(encoding='utf-8'))
        conflicts=cross.get('conflicts',[])
        if conflicts:
            errors.append(f'Cross-check đáp án nguồn còn {len(conflicts)} xung đột.')
    except Exception as e:
        errors.append(f'Không đọc được {CROSS.relative_to(ROOT)}: {e}')
else:
    errors.append('Thiếu tools/v9_answer_crosscheck.json')

print(f'[pdf-bank] {files} bài học có ngân hàng PDF; {imported} câu/bài đã nhập.')
print('[pdf-bank] Theo chương:', ', '.join(f'{k}={v}' for k,v in sorted(by_chapter.items())))
print('[pdf-bank] Theo mức độ:', ', '.join(f'{k}={v}' for k,v in by_level.items()))
print(f'[pdf-bank] {image_q} hình/đồ thị bài tập được tham chiếu; {solution_img} lời giải legacy dùng ảnh.')
print(f'[pdf-bank] {type_count} mục dạng bài ở 4 chương lõi; không lặp tên trong cùng bài học.')
if warnings:
    for w in warnings[:20]: print('WARN PDFBANK:',w)
    if len(warnings)>20: print(f'WARN PDFBANK: ... còn {len(warnings)-20} cảnh báo')
if errors:
    for e in errors: print('ERROR PDFBANK001:',e)
    print(f'[pdf-bank] {len(errors)} lỗi.')
    raise SystemExit(1)
print('[pdf-bank] 0 lỗi toàn vẹn. OK.')
