from pathlib import Path
import re,yaml
ROOT=Path(__file__).resolve().parents[1]
CFG=ROOT/'mkdocs.yml'
DOCS=ROOT/'docs'
GRADE=DOCS/'physics/high-school/grade-11'

chapters={
'Chương 1 — Dao động cơ học':'01-oscillations',
'Chương 2 — Sóng':'02-waves',
'Chương 3 — Điện trường':'03-electric-field',
'Chương 4 — Dòng điện và mạch điện':'04-current-circuits',
'Chương 5 — Dòng điện trong các môi trường':'05-current-media',
'Chương 6 — Từ trường và cảm ứng từ':'06-magnetism',
'Chương 7 — Cảm ứng điện từ':'07-electromagnetic-induction',
'Chương 8 — Khúc xạ ánh sáng và quang hình':'08-geometrical-optics',
}

def title(path):
    t=path.read_text(encoding='utf-8')
    m=re.search(r'^title:\s*["\']?(.+?)["\']?\s*$',t,re.M)
    return m.group(1) if m else path.stem

def strip_bai(t):
    return re.sub(r'^Bài\s+\d+\s+—\s*','',t)

data=yaml.safe_load(CFG.read_text(encoding='utf-8'))
# locate Vật lí 11 list
nav=data['nav']
# recursive find key value
def find_key(node,key):
    if isinstance(node,list):
        for x in node:
            r=find_key(x,key)
            if r is not None:return r
    elif isinstance(node,dict):
        for k,v in node.items():
            if k==key:return v
            r=find_key(v,key)
            if r is not None:return r
    return None
vl11=find_key(nav,'Vật lí 11')
for item in vl11:
    if not isinstance(item,dict):
        continue
    for ch_label,ch_slug in chapters.items():
        if ch_label not in item: continue
        lst=item[ch_label]
        # normalize existing labels
        for ent in lst:
            if isinstance(ent,dict):
                if 'Bài tập' in ent:
                    ent['Bài tập tổng hợp chương']=ent.pop('Bài tập')
                if 'Lời giải' in ent:
                    ent['Đáp án tổng hợp chương']=ent.pop('Lời giải')
                if 'Quiz' in ent:
                    ent['Kiểm tra cuối chương']=ent.pop('Quiz')
        # remove old practice nav if rerun
        lst[:]=[ent for ent in lst if not (isinstance(ent,dict) and 'Luyện tập theo từng bài' in ent)]
        practice=[{'Tổng quan':f'physics/high-school/grade-11/{ch_slug}/practice/index.md'}]
        chdir=GRADE/ch_slug
        for lf in sorted(chdir.glob('[0-9][0-9]-*.md')):
            stem=lf.stem
            disp=title(lf)
            practice.append({disp:[
                {'Bài tập':f'physics/high-school/grade-11/{ch_slug}/practice/{stem}/exercises.md'},
                {'Đáp án và lời giải':f'physics/high-school/grade-11/{ch_slug}/practice/{stem}/solutions.md'},
            ]})
        # insert before total chapter exercises if possible
        idx=next((i for i,e in enumerate(lst) if isinstance(e,dict) and 'Bài tập tổng hợp chương' in e),len(lst))
        lst.insert(idx,{'Luyện tập theo từng bài':practice})

CFG.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False,width=120),encoding='utf-8')
print('updated nav')
