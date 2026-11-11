# 独立复核：视觉 Oral 身份与 M31–M50 数学框架

核查时间：2026-10-27。只读 data/vision.json、data/methods.json；初始审阅未修改主数据；随后按主 agent 明确授权，仅将自己 iclr.json 的两条身份来源升级为官方单篇 event。视觉和 methods 主数据未改。复核者为 ICLR 子任务 agent，视觉条目由另一 agent 整理。方法：直接请求官方站点并检查 HTML 标题、正文、表格所属标题；两份作者 slides 另作 PDF 文本提取；核对新增 20 类公式、条件、边界与分类关系。未重新阅读全部论文方法节，亦未复现实验。

**结论：14/14 视觉论文的 Oral 身份获得独立官方来源支持。P0=0；当前未发现阻止首轮发布的 P1。存在 6 组 P2 修订建议。** 原来仅 slides 支持的 TopoCellGen 和 RACE 均找到更强的官方 Oral 页面/总表。四篇 2026 论文均成功读取官方 event，非仅依据未来会议名称推断。ICLR 两篇原先的索引证据也已找到官方单篇 event。

## 视觉 14 篇核查

以下页面均本轮实际请求成功（HTTP 200）。表中的“全文”指 Oral 身份页面全文，**不指研究论文全文精读**。

| 数据 ID | 结论与实际证据 | 建议 |
|---|---|---|
| vision-eccv22-pose | [ECCV2022 accepted papers](https://eccv2022.ecva.net/program/accepted-papers/) 第一张 table 的前置标题为 Oral papers；Pose-NDF 位于该表、ID1413 | 保留 |
| vision-eccv22-topology | 同一官方 Oral papers 表含完整题名，ID6180；不是第二张 Poster 表 | 保留 |
| vision-eccv22-pactran | 同一官方 Oral papers 表含完整题名，ID6568 | 保留 |
| vision-iccv23-purification | [官方 HTML program](https://iccv2023.thecvf.com/main.conference.program-107.php) 同名题目 ID11381 的所属标题为 Wednesday 4th 09:30 AM–10:30 AM - Orals，Room Paris Nord | 建议替代开幕 slides 链接。相同论文也在随后 Poster 表出现，不影响 Oral 身份 |
| vision-cvpr24-map | [CVPR2024 官方 Oral Papers 新闻](https://cvpr.thecvf.com/Conferences/2024/News/Oral_Papers) 将同名论文列在 Oral 介绍中 | 保留，新闻证据与具体名单不同层级但此处同名明确 |
| vision-eccv24-race | [ECCV2024 官方 Oral 总表](https://eccv.ecva.net/virtual/2024/events/oral) 条目标题为 R.A.C.E.: Robust Adversarial Concept Erasure for Secure Text-to-Image Diffusion Model，前置 Oral，时间 Oct4 9:20–9:30，链接 [oral/2342](https://eccv.ecva.net/virtual/2024/oral/2342) | 用总表或单篇 event 替代作者 slides；注意题名前缀有句点 |
| vision-cvpr25-topocell | [官方单篇 event](https://cvpr.thecvf.com/virtual/2025/oral/35356) 全文 HTML 标题含 CVPR Oral 与完整题名，正文 2025 Oral；官方 Oral 总表链接至该 event | 替代 slides 链接 |
| vision-cvpr25-convex | [官方单篇 event](https://cvpr.thecvf.com/virtual/2025/oral/35342) 全文 HTML 标题含 CVPR Oral 与完整题名 | 保留 |
| vision-iccv25-flowedit | [官方单篇 event](https://iccv.thecvf.com/virtual/2025/oral/2925) 全文 HTML 标题含 ICCV Oral 与完整题名 | 保留 |
| vision-iccv25-diip | [官方单篇 event](https://iccv.thecvf.com/virtual/2025/oral/2934) 全文 HTML 标题含 ICCV Oral Diffusion Image Prior | 保留 |
| vision-cvpr26-unroll | [官方单篇 event](https://cvpr.thecvf.com/virtual/2026/oral/40269) HTTP200，同名 HTML 标题明确 CVPR Oral，会议为 CVPR2026 | 保留 |
| vision-cvpr26-rdvq | [官方单篇 event](https://cvpr.thecvf.com/virtual/2026/oral/40298) HTTP200，同名 HTML 标题明确 CVPR Oral，会议为 CVPR2026 | 保留 |
| vision-eccv26-heat | [官方单篇 event](https://eccv.ecva.net/virtual/2026/oral/6124) HTTP200，同名 HTML 标题明确 ECCV Oral，会议为 ECCV2026 | 保留 |
| vision-eccv26-mimflow | [官方单篇 event](https://eccv.ecva.net/virtual/2026/oral/6128) HTTP200，同名 HTML 标题明确 ECCV Oral，会议为 ECCV2026 | 保留 |

RACE slides 的第一页确实提取到 ECCV 2024 (Oral)；TopoCellGen slides 的第一页确实提取到 Oral Presentation。它们并非错误证据，但属“会议官方托管的作者自述”，优先用本轮发现的会议 program 分类。ICCV2023 开幕 slides 的表格文字提取不完整，本轮未将“未提取到题名”当否定证据；改由官方 HTML program 解决。

## ICLR 2022/2026 原索引证据升级

| 论文 | 旧证据的准确等级 | 本轮更强来源 |
|---|---|---|
| Frame Averaging for Invariant and Equivariant Network Design | OpenReview 官方搜索页面被搜索引擎收录的题名+ICLR2022 Oral 字段；不是成功读取 forum decision | [ICLR2022 Oral 总表](https://iclr.cc/virtual/2022/events/oral) 找到题名链接，再读取 [单篇 Oral6190](https://iclr.cc/virtual/2022/oral/6190)，HTTP200，标题明确 ICLR Oral，正文 2022 Oral |
| GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models | OpenReview 官方作者 profile 的搜索索引内容，同一题名下 ICLR2026 Oral；直接打开 profile 曾遇到 browser challenge。不能描述成 forum/full decision 已读 | [ICLR2026 Oral 总表](https://iclr.cc/virtual/2026/events/oral) 找到题名链接，再读取 [单篇 Oral10006825](https://iclr.cc/virtual/2026/oral/10006825)，HTTP200，标题明确 ICLR Oral 与完整题名 |

已按主 agent 后续授权更新 iclr.json 两条 oral_url/oral_evidence；本文保留从索引升级到 program 的事实。无需把论文 reading_depth 从 abstract 升级；身份取证和方法精读是两个维度。

## M31–M50 数学与重复检查

20 条均作为教学模板而非严格完整定理理解，未发现方向颠倒、错误目标或把不同概念直接等同的 P1。关键区分已有正确说明：纳什与社会最优、固定点与纳什、静态遗憾与动态/末迭代结果、自然梯度与镜像下降、OT与路径空间桥、GFlowNet与连续流、正交性与双重稳健。

建议修订以下 P2，防止读者直接复制成实施公式：

1. **M47：注明流守恒的节点范围和边界条件。** 当前 `Σ_parent F=Σ_child F; P(x)∝R(x)` 对中间节点成立；若对所有节点机械套用会与源/终点冲突。改为“中间节点 Σin F=Σout F；源流量 Z；终端流入=R(x)；Z=Σ_xR(x)>0”。明确奖励可归一化，只有非负不足以得到有效概率分布。
2. **M39：补局部可微分分支条件。** 当前逆 Jacobian 公式正确，但除可逆外还需 f 可微以及选定解分支的适当局部条件；不需用压缩映射条件冒充必要条件。可在 assumptions 添加“f 局部连续可微”。
3. **M32：写清 IC 的类型和条件变量。** `u_i(truth)≥u_i(report)` 可作口语模板，落地需定义对其他报告取任意值的 DSIC，还是条件期望的 BIC，并注明支付/配置及真实类型。避免一条不带量词的不等式混用两类机制。
4. **M44：平方残差是高斯/二次损失示例。** 建议通用式改 `min_x −log p(y|x)+λR(x)`，平方残差作为白高斯噪声实例。已有 assumptions 说噪声明确，但主公式若只写 L2 易诱导 Poisson 数据误用。
5. **M50：明确正交导数是 nuisance 方向导数。** 可写 `D_η E[ψ(W;θ₀,η₀)][h]=0 ∀h`。双重稳健是至少一个 nuisance 正确时的结构性质，当前 limitations 已正确提醒；若保持合并类名，最好补一个 AIPW 示例后再扩写。
6. **分类为多层级标签而非 50 个互斥原子。** M34 是 M33 的部分反馈子类；M36 是 M42 的统计流形特例；M38/M39 是可用于 M44 的算法工具；M43 不涵盖所有简单类别包含/排斥关系损失；M49 把蒸馏与特权信息迁移合为一类需保留可分离子标签。当前“50类”可作为导航，但不得据此宣称有50个独立且互不重叠理论。视觉 Learning Topological Interactions 的关系约束不能仅凭名称作为持久同调证据。

参考链接抽查：[M44 原文标题](https://arxiv.org/abs/2006.03972)、[M48 原文标题](https://arxiv.org/abs/1808.03856)匹配；[M42 原文](https://proceedings.mlr.press/v97/kasai19a.html)完整标题末尾是 “on matrix manifolds”，当前 reference_title 省略该后缀，属书目精度 P2。

## 本轮验收范围

本轮确认“论文确为 Oral”及“数学导航模板没有发现重大错误”。不确认论文效果可复现，不确认抽象分类已经全面覆盖顶会，不将摘要式提炼提升为方法节审查。建议将 `oral_evidence_level` 与 `reading_depth` 分开维护：program全文 / 官方托管slides / 官方索引片段 / 作者声明，应可区分。

## 第二轮：M51–M59及映射复核

新增9类未发现重大数学错误。发布前已采纳：rate-policy改主M33、次M36/M37；influence撤去M39并标未映射；拓扑交互仅related；LSEnet移除M03；M58明确极大团枚举；MIMFlow注明组件似然与整体边缘似然之别；FlowEdit不作严格OT实例。第二轮按已存论文卡交叉核对，没有把阅读深度升级为全文审阅。
