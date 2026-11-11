"""Build standalone offline UI from canonical atlas data."""
import json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
data={n:json.loads((r/'data'/f'{n}.json').read_text()) for n in ['methods','papers']}
payload=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
(r/'frontend/index.html').write_text((r/'frontend/template.html').read_text().replace('__ATLAS_DATA__',payload))
(r/'frontend/sources.json').write_text(json.dumps([{'id':p['id'],'title':p['title'],'url':p['oral_url'],'content_url':p['paper_url'],'accessed':'2026-10-27','reading_depth':p['reading_depth'],'supports':p['oral_evidence']} for p in data['papers']],ensure_ascii=False,indent=2))
print('Built offline frontend:',len(data['methods']),'methods,',len(data['papers']),'papers')
