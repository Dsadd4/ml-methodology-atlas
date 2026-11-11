import json,html,textwrap
from pathlib import Path
from playwright.sync_api import sync_playwright
r=Path(__file__).resolve().parents[1];ms=json.loads((r/'data/methods.json').read_text());groups=list(dict.fromkeys(m['group'] for m in ms));cols=['#3965bb','#5aa69a','#b0a0d2','#da7c38','#cf8393','#7b387e'];out=r/'frontend/exports';out.mkdir(exist_ok=True)
s=['<svg xmlns="http://www.w3.org/2000/svg" width="1680" height="1130" viewBox="0 0 1680 1130"><rect width="1680" height="1130" fill="#f6f8fb"/><g font-family="Arial, PingFang SC, sans-serif" fill="#182d3b"><text x="35" y="52" font-size="29">机器学习方法论图谱 · 59类框架</text><text x="35" y="88" font-size="15">分类导航 · 类别可组合且存在包含关系 · 2026-10-27</text>']
for i,g in enumerate(groups):
 x=30+i*275;s.append(f'<rect x="{x}" y="120" width="260" height="50" rx="8" fill="{cols[i]}"/><text x="{x+14}" y="152" fill="white" font-size="20">{g}</text>')
 for j,m in enumerate([m for m in ms if m['group']==g]):
  y=185+j*63;s.append(f'<rect x="{x}" y="{y}" width="260" height="55" rx="7" fill="white" stroke="#dce3e9"/><text x="{x+12}" y="{y+22}" font-size="12">{m["id"]}</text>')
  lines=textwrap.wrap(m['name'],15)
  for k,line in enumerate(lines):s.append(f'<text x="{x+49}" y="{y+22+k*20}" font-size="14">{html.escape(line)}</text>')
s.append('</g></svg>');(out/'overview.svg').write_text(''.join(s));(out/'diagram_data.json').write_text(json.dumps(ms,ensure_ascii=False,indent=2));(out/'gallery.json').write_text(json.dumps({'pages':[{'id':'overview','file':'overview.svg','title':'59类方法论导航'}]},ensure_ascii=False,indent=2))
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={'width':1680,'height':1130},device_scale_factor=2);page.set_content('<style>@page{size:1680px 1130px;margin:0}body{margin:0}</style>'+''.join(s));page.screenshot(path=str(out/'overview.png'));page.pdf(path=str(out/'overview.pdf'),width='1680px',height='1130px',print_background=True);b.close()
