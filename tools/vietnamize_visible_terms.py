from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
repls=[
('Research / Enrichment','Nghiên cứu / Mở rộng'),
('Advanced / Enrichment','Nâng cao / Mở rộng'),
('Level 1','Mức 1'),('Level 2','Mức 2'),('Level 3','Mức 3'),('Level 4','Mức 4'),('Level 5','Mức 5'),
('Foundation','Nền tảng'),('Standard','Chuẩn'),('Applied','Vận dụng'),('Advanced','Nâng cao'),('Enrichment','Mở rộng'),
('Prerequisite chính','Kiến thức tiên quyết chính'),('Prerequisite','Kiến thức tiên quyết'),
('Quiz cuối chương','Kiểm tra cuối chương'),('Quiz Chương','Kiểm tra Chương'),('[Quiz →]','[Kiểm tra cuối chương →]'),('[Quiz](quiz.md)','[Kiểm tra cuối chương](quiz.md)'),
('Quiz kiểm tra','Bài kiểm tra'),
]
for p in DOCS.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    old=text
    for a,b in repls:text=text.replace(a,b)
    if text!=old:p.write_text(text,encoding='utf-8')
print('done')
