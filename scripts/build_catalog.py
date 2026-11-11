#!/usr/bin/env python3
"""Build inspectable Markdown and CSV views from curated JSON. Standard library only."""
import csv,json
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]; D=R/'data'
load=lambda f:json.loads((D/f).read_text())
methods=load('methods.json'); mapping=load('paper_method_map.json')
papers=[x for f in ['iclr.json','neurips_icml.json','vision.json'] for x in load(f)]
ids={m['id'] for m in methods}
assert len(ids)==len(methods)
assert len({p['id'] for p in papers})==len(papers)
assert len({(p['title'].lower(),p['year'],p['venue']) for p in papers})==len(papers)
assert set(mapping)=={p['id'] for p in papers}
for p in papers:
 assert 2022<=int(p['year'])<=2026
 for f in ['title','oral_url','paper_url','intuition','formulation','assumptions','limitations','reading_depth']:assert p.get(f),(p['id'],f)
 p['method_mapping']=mapping[p['id']]
 assert set(mapping[p['id']]['primary']+mapping[p['id']]['secondary'])<=ids
verified=[p for p in papers if p['oral_status']=='verified']; pending=[p for p in papers if p['oral_status']!='verified']
by={m['id']:[] for m in methods}
for p in verified:
 for mid in mapping[p['id']]['primary']+mapping[p['id']]['secondary']:by[mid].append(p)
write=lambda f,s:(R/f).write_text(s,encoding='utf-8')
def cell(s):return str(s).replace('|','\\|').replace('\n',' ')
def table(head,rows):return '| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+''.join('| '+' | '.join(cell(x) for x in row)+' |\n' for row in rows)
(D/'papers.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2)+'\n')
for name,records,fields in [('methods',methods,list(methods[0])),('papers',papers,['id','title','venue','year','presentation','oral_status','oral_url','paper_url','method_family','reading_depth'])]:
 with (D/(name+'.csv')).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(records)
text='# 59类机器学习与数学方法论总表\n\n更新：2026-10-27。原M01–M30编号保留；M31–M50为经典框架扩充；M51–M59由本轮论文机制进一步拆分。类别是可组合的导航标签，包含父子层级，并非59个互斥理论。公式是教学模板，不是逐篇算法的逐字转录。\n\n完整条件、失效边界及论文映射见 [方法卡](METHOD_CARDS.md)。\n\n'
for group in dict.fromkeys(m['group'] for m in methods):
 text+='## '+group+'\n\n'+table(['编号 / 方法','核心直觉','数学模板','适用问题','本轮关联Oral'],[(m['id']+' '+m['name'],m['intuition'],m['formulation'],m['applications'],len(by[m['id']])) for m in methods if m['group']==group])+'\n'
text+='“关联Oral”包括主要、辅助和相关联系，数量不是对理论正确性或方法优劣的投票；0表示本轮未收录对应Oral。\n'
write('METHODS.md',text)
text='# 方法论详细卡\n\n每项独立说明适用条件；参考文献为框架入口，Oral为本轮实例。`related`只表示关联，不作为该框架直接实例。\n\n'
for m in methods:
 text+=f"## {m['id']} {m['name']}\n\n**直觉：** {m['intuition']}\n\n**数学模板：** {m['formulation']}\n\n**适用问题：** {m['applications']}\n\n**成立条件：** {m['assumptions']}\n\n**失效边界：** {m['limitations']}\n\n**与相邻方法的区别：** {m['distinction']}\n\n**框架文献：** [{m['reference_title']}]({m['reference_url']})\n\n"
 if by[m['id']]:
  text+='**本轮论文联系：**\n\n'
  for p in by[m['id']]:
   mp=mapping[p['id']];role='相关' if mp.get('relation')=='related' else ('主要' if m['id'] in mp['primary'] else '辅助')
   text+=f"- {p['venue']} {p['year']} [{p['title']}]({p['oral_url']})；{role}联系；阅读层级 `{p['reading_depth']}`。\n"
 else:text+='本轮暂无对应的已核Oral实例；本条来自经典框架扩充。\n'
 text+='\n'
write('METHOD_CARDS.md',text)
text='# Oral论文索引\n\n官方身份核实与论文阅读深度分开记录；Oral指官方展示类别，不保证录用字段也写作Oral。这里只是方法导向精选，不是全部Oral清单。\n\n'+table(['会议','年份','论文 / 官方身份来源','方法标签','阅读深度'],[(p['venue'],p['year'],f"[{p['title']}]({p['oral_url']})",', '.join(mapping[p['id']]['primary']+mapping[p['id']]['secondary']),p['reading_depth']) for p in sorted(verified,key=lambda p:(p['year'],p['venue'],p['title']))])
text+='\n## 未计入已核Oral\n\n'+table(['论文','状态','说明'],[(p['title'],p['oral_status'],p['oral_evidence']) for p in pending])
text+='\nICML2026 Information Flow 官方事件为Oral，但decision为Accept (spotlight)；保留两字段差异，未改写录用等级。完整证据与机制见 [论文卡](PAPER_CARDS.md)。\n'
write('ORAL_PAPERS.md',text)
text='# 论文方法卡与取证记录\n\n模板是本项目提炼；实验建议不代表已经执行。abstract含摘要/介绍/讲者材料层筛选；method_section代表定位阅读过部分方法段，均不等同完整复现。\n\n'
for p in sorted(papers,key=lambda p:(p['venue'],p['year'],p['id'])):
 text+=f"## {p['title']}\n\n{p['venue']} {p['year']} · `{p['id']}` · `{p['oral_status']}` · 阅读 `{p['reading_depth']}`\n\n"
 for label,key in [('原展示类型','presentation'),('录用字段','acceptance_label'),('身份依据','oral_evidence'),('身份补充','oral_status_note'),('方法族','method_family'),('直觉','intuition'),('模板','formulation'),('前提','assumptions'),('限制','limitations'),('方法段证据','method_evidence'),('可证伪实验建议','falsification_experiment')]:
  if p.get(key):text+=f"**{label}：** {p[key]}\n\n"
 text+=f"**映射：** {', '.join(mapping[p['id']]['primary']+mapping[p['id']]['secondary'])}。{mapping[p['id']]['note']}\n\n[官方身份来源]({p['oral_url']}) · [论文]({p['paper_url']})\n\n"
 if p.get('content_source_url'):text+=f"[实际内容入口]({p['content_source_url']})\n\n"
write('PAPER_CARDS.md',text)
counts=Counter((p['venue'],p['year']) for p in verified)
venues=['NeurIPS','ICML','ICLR','CVPR','ICCV','ECCV'];years=list(range(2022,2027))
def scheduled(v,y):return not(v=='ICCV' and y%2==0 or v=='ECCV' and y%2==1)
cells=[(v,y) for v in venues for y in years if scheduled(v,y)]
covered=sum(counts[c]>0 for c in cells)
text='# 年份覆盖与证据边界\n\n数字为本项目已核官方Oral展示的精选论文数，不是大会Oral总数。—表示非该会举办年份；0表示当前未覆盖。\n\n'+table(['会议']+list(map(str,years)),[[v]+[counts[v,y] if scheduled(v,y) else '—' for y in years] for v in venues])
text+=f'\n覆盖 {covered}/{len(cells)} 个会议年份单元；共 {len(verified)} 篇已核，{len(pending)} 篇待核，不计入已核分母。\n\nNeurIPS2022官方JSON当前快照有Poster与Spotlight但无Oral标签；不能据此断言该会没有口头报告，也不将Spotlight自动转换为Oral。详情与计数口径见 research/neurips_icml.md。\n\n2026按截至2026-10-27已公开的官方记录收录，会议展示记录不等于报告已举行。ICML2026 Information Flow存在Oral事件与spotlight录用字段差异。\n\n阅读深度分布：'+str(dict(Counter(p['reading_depth'] for p in verified)))+'。部分方法段阅读不等于全文精读；暂无实验复现。\n\n选择偏差：主动寻找可提炼数学框架的论文；未按热度、引用量或性能排序，不能用本库频数推断顶会方法趋势。\n'
write('COVERAGE.md',text)
write('README.md',f'''# ML Methodology Atlas · 机器学习方法论图谱

**原30类扩充到{len(methods)}类；收录{len(verified)}篇已核官方Oral展示论文及{len(pending)}篇待核候选，覆盖2022–2026六个顶会的{covered}/{len(cells)}个举办年份单元。** 第一版，更新2026-10-27。

核心产物是方法论表：数学框架、直觉、适用问题、成立条件、失效边界和实际论文中的用法。保留原30类稳定编号；补充20类基础框架，并从本轮论文中拆出9类独立有用的框架。

## 阅读入口

- [59类总表](METHODS.md)：先看全貌。
- [59张详细方法卡](METHOD_CARDS.md)：条件、区别、基础文献与Oral实例。
- [Oral论文索引](ORAL_PAPERS.md)：会议、年份、官方来源和阅读深度。
- [论文方法卡](PAPER_CARDS.md)：逐篇机制、假设、失效条件与部分实验建议。
- [年份覆盖](COVERAGE.md)：哪些年份已经取样、哪些仍有缺口。
- [独立复核](research/independent_review.md)及[数据验收](VALIDATION.md)。

## 本版新增方向

M31–M50涵盖博弈均衡、机制设计、在线学习、Bandit、序贯检验、信息几何、镜像下降、近端方法、不动点、算子学习、谱方法、流形、拓扑、逆问题、流匹配、Schrödinger桥、GFlowNet、重要性采样、蒸馏、正交估计。

M51–M59进一步加入进化搜索与质量多样性、Markov生成元、凸松弛、隐式正则、归一化流、偏好学习、差分隐私、图团搜索、Wasserstein梯度流。

这些是可组合且有层级关系的建模标签，并非互斥理论。不是每类都有本轮Oral实例。官方身份已核实与正文方法已精读也分开记录；目前主要完成摘要层筛选，3篇定位阅读方法段。这里没有宣称完成五年所有Oral普查。

## 下载与启动

```bash
git clone https://github.com/Dsadd4/ml-methodology-atlas.git
cd ml-methodology-atlas
python3 -m http.server 8768 --bind 127.0.0.1
```

在浏览器打开 http://127.0.0.1:8768/frontend/index.html 。也可以直接打开下载后的 `frontend/index.html`，页面自带数据，无需安装依赖。

![前端预览](frontend/output/playwright/desktop.png)

修改数据后，依次运行：

```bash
python3 scripts/build_catalog.py
python3 scripts/build_frontend.py
```

可选的浏览器交互检查与图片导出使用 Playwright：

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 scripts/check_frontend.py
python3 scripts/export_overview.py
```

## 数据与维护

主数据：[methods.json](data/methods.json)、三个会议分组JSON、[映射表](data/paper_method_map.json)。导出：[methods.csv](data/methods.csv)、[papers.csv](data/papers.csv)、[papers.json](data/papers.json)。CSV使用UTF-8 BOM便于表格软件读取。

运行 `python scripts/build_catalog.py` 重建所有目录与卡片。只用Python标准库；构建同时检查唯一ID、必填字段、年份和映射引用。`methods_seed.tsv`是原50类输入快照（使用¦分隔），不是维护入口。

三路并行调研：ICLR、NeurIPS/ICML、CVPR/ICCV/ECCV；另由ICLR调研者对视觉初始14篇身份及M31–M50作交叉复核。详见research下分工报告。论文发现脚本原始结果保留，但其命中不是Oral身份依据。

下一版最有价值的工作是对现有卡逐步补全文方法依据、反例与最小可运行示例，再扩大尚无实例的方法覆盖。项目未进行模型实验。
''')
write('VALIDATION.md',f'''# 构建与数据验收

更新2026-10-27；运行 scripts/build_catalog.py 成功。

- 方法ID唯一：{len(methods)}；原M01–M30保留。
- 论文ID及标题/会议/年份组合唯一：{len(papers)}。
- 官方Oral展示已核：{len(verified)}；未核：{len(pending)}，未混入已核计数。
- 全部论文的字段、年份范围及方法标签外键通过检查。
- 会议年份覆盖：{covered}/{len(cells)}；不是Oral论文总体覆盖率。
- 阅读深度计数：{dict(Counter(p['reading_depth'] for p in verified))}。
- 独立审阅范围：视觉最初14条身份、M31–M50；不是所有条目逐项双人全文审稿。
- 已采纳复核：M32量词/IC类型，M39局部可微，M44一般似然，M47流边界，M50正交方向；拓扑交互未映射成持久同调。
- 独立审阅结果与其余细节见 research/independent_review.md。

上述是数据完整性与文献整理检查，不能作为实验复现或科学效果验证。
''')
print(json.dumps(dict(methods=len(methods),papers=len(papers),verified=len(verified),pending=len(pending),covered=covered,reading=dict(Counter(p['reading_depth'] for p in verified))),ensure_ascii=False))
