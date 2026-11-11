# ICLR 2022–2026：Oral 方法论首轮精选

核查日期：2026-10-27。共 12 篇已核验 Oral，按会议年份为 2022:1、2023:5、2024:4、2025:1、2026:1。这是目的性精选，不是五年完整 Oral 普查，不能用于年度主题比例或趋势推断。论文内容主要读取摘要，全部标为 abstract；数学式为可迁移的方法论模板，除特别说明外不当作论文逐字公式。

## 检索与证据范围

- 先查官方会议 Oral 总表/单篇页面；2023 总表可直接读，2024 单篇页面及官方博客可交叉核对。
- OpenReview forum 部分页呈浏览器挑战，因此 2022 Frame Averaging、2026 GLASS 采用 OpenReview 官方搜索或作者 profile 的接受类型字段。
- 2025 Generator Matching 的网页检索工具受限；采用轻量 requests 直接读取同一官方 URL，HTTP 200，正文包含题名及 2025 Oral。没有把第三方声称当最终证据。
- 论文方法来源使用官方 proceedings、OpenReview 或作者 arXiv 原稿；无下载全量 PDF、无复现实验。
- 年份均有实质实例，但 2022/2025/2026 各仅 1 篇，覆盖明显不均衡。需要扩展这些年份的全部 Oral 名单与方法章节阅读。

## 方法论扩充建议

优先新增：谱方法与商对称性、重要性采样/退火蒙特卡洛、进化搜索/质量多样性、博弈均衡、黎曼几何、GFlowNet、马尔可夫生成元、充分统计量。群平均、最优传输、贝叶斯逆问题和鲁棒因果关系适合补充已有分类，不应为增加类别数重复拆分。

## 2022 · Frame Averaging for Invariant and Equivariant Network Design

- 方法族：**群平均与等变性**；图谱动作：`enrich_existing`。
- 直觉：同一对象换坐标后含义不变；把少量合法参考系下的预测合并，获得结构性不变或等变。
- 数学模板：`方法论模板：F(x)=|G|^{-1}∑_{g∈G}g·f(g^{-1}·x)；论文用等变有限 frame 替代全群。`
- 前提：群作用已知；frame 的选择本身满足等变性。
- 边界：连续群不能直接有限求和；退化结构与 frame 稳定性需要专门处理。
- Oral 证据：[OpenReview 官方搜索页面在同名论文下标注 ICLR 2022 Oral。](https://openreview.net/search?content=authors&group=all&sort=cdate%3Adesc&source=forum&term=~Ishan_Misra2)
- [论文原始来源](https://arxiv.org/abs/2110.03336)；阅读深度：摘要。

## 2023 · Sign and Basis Invariant Networks for Spectral Graph Representation Learning

- 方法族：**谱方法与特征空间商对称性**；图谱动作：`new_family`。
- 直觉：特征向量是坐标选择，不是唯一物理对象；学习应忽略正负号和重根子空间的基变换。
- 数学模板：`方法论模板：L=UΛUᵀ；同一特征子空间内 f(UQ)=f(U), QᵀQ=I。`
- 前提：已知谱算子和等价变换群；区分单根与重根。
- 边界：只处理符号不足以处理重根；计算特征分解及谱扰动稳定性另需评估。
- Oral 证据：[官方 2023 Oral 总表的同名条目直接标注 Oral。](https://iclr.cc/virtual/2023/events/oral)
- [论文原始来源](https://arxiv.org/abs/2202.13013)；阅读深度：摘要。

## 2023 · Flow Annealed Importance Sampling Bootstrap

- 方法族：**重要性采样与退火蒙特卡洛**；图谱动作：`new_family`。
- 直觉：没有真实样本但能算未归一化密度时，用可学习提议分布加退火链寻找被遗漏的概率质量。
- 数学模板：`方法论模板：w(x)=p̃(x)/qθ(x)；以 α=2 散度降低重要性权重方差。`
- 前提：目标密度可计算；提议分布覆盖目标支撑；相关矩存在。
- 边界：覆盖不足会导致极端权重；自归一化比率估计一般不能直接称有限样本无偏。
- Oral 证据：[官方 2023 Oral 总表的同名条目直接标注 Oral。](https://iclr.cc/virtual/2023/events/oral)
- [论文原始来源](https://arxiv.org/abs/2208.01893)；阅读深度：摘要。

## 2023 · Neural Optimal Transport

- 方法族：**最优传输的随机计划**；图谱动作：`enrich_existing`。
- 直觉：无配对两域数据的对应关系可作为耦合分布求解，而非强迫每个输入只有一个输出。
- 数学模板：`通用 OT 模板：min_{π∈Π(μ,ν)} Eπ[c(x,y)]；论文还研究 weak transport costs。`
- 前提：代价应对应任务语义；边缘分布约束合理。
- 边界：匹配分布不自动保证语义或因果对应；上述简单公式不等同论文全部弱代价形式。
- Oral 证据：[官方 2023 Oral 总表的同名条目直接标注 Oral。](https://iclr.cc/virtual/2023/events/oral)
- [论文原始来源](https://arxiv.org/abs/2201.12220)；阅读深度：摘要。

## 2023 · Diffusion Posterior Sampling for General Noisy Inverse Problems

- 方法族：**贝叶斯逆问题与软数据一致性**；图谱动作：`enrich_existing`。
- 直觉：观测含噪时，不能把输出强行投影到观测；用生成先验与噪声似然共同解释数据。
- 数学模板：`方法论模板：p(x|y)∝p(y|x)p(x)，y=A(x)+ε；后验 score=先验 score+似然 score。`
- 前提：前向模型及噪声似然足够准确；已有适合目标分布的生成先验。
- 边界：DPS 使用后验近似，不能声称精确后验采样；错误先验可能产生可信但错误结构。
- Oral 证据：[官方 2023 Oral 总表的同名条目直接标注 Oral。](https://iclr.cc/virtual/2023/events/oral)
- [论文原始来源](https://arxiv.org/abs/2209.14687)；阅读深度：摘要。

## 2023 · Neuroevolution is a Competitive Alternative to Reinforcement Learning for Skill Discovery

- 方法族：**进化搜索与质量多样性**；图谱动作：`new_family`。
- 直觉：保留每类行为中表现好的解，形成可组合技能库；单个最大回报解并不代表可迁移能力。
- 数学模板：`方法论模板：archive[b]←argmax_{θ:descriptor(θ)∈b} R(θ)。`
- 前提：行为描述符与分桶能表达有用差异；环境可重复评价。
- 边界：质量与覆盖依赖描述符；论文比较多算法而非证明 QD 在所有任务优于 RL。
- Oral 证据：[官方 2023 Oral 总表的同名条目直接标注 Oral。](https://iclr.cc/virtual/2023/events/oral)
- [论文原始来源](https://arxiv.org/abs/2210.03516)；阅读深度：摘要。

## 2024 · Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization

- 方法族：**博弈论与近似均衡**；图谱动作：`new_family`。
- 直觉：多个决策者互相影响时，稳定解要求任何一方单独改变策略都无法明显获益。
- 数学模板：`通用定义：ε(π)=max_i[max_{π′ᵢ}uᵢ(π′ᵢ,π₋ᵢ)−uᵢ(π)]；求 ε≤δ。论文另外构造可无偏 Monte Carlo 估计的损失。`
- 前提：有限标准式博弈；效用估计与策略空间可访问。
- 边界：非凸局部驻点不能自动当全局均衡；本模板不是论文无偏损失的原式。
- Oral 证据：[官方会议 Oral 页面列出同名论文并标注 2024 Oral。](https://iclr.cc/virtual/2024/oral/19744)
- [论文原始来源](https://openreview.net/forum?id=cc8h3I3V4E)；阅读深度：摘要。

## 2024 · Flow Matching on General Geometries

- 方法族：**黎曼几何与流形上的流匹配**；图谱动作：`new_family`。
- 直觉：数据受曲面或几何约束时，速度、距离和移动方向都应在对应流形上定义。
- 数学模板：`方法论模板：minθ E||vθ(x,t)−u_t(x|x₁)||²_g；dx/dt=vθ(x,t)∈T_xM。`
- 前提：流形、度量或 premetric 可获得；目标向量场可构造。
- 边界：简单几何可免模拟不代表任意网格都无计算开销；几何设错会造成偏差。
- Oral 证据：[官方会议 Oral 页面列出同名论文并标注 2024 Oral。](https://iclr.cc/virtual/2024/oral/19740)
- [论文原始来源](https://openreview.net/forum?id=g7ohDlTITL)；阅读深度：摘要。

## 2024 · Robust agents learn causal world models

- 方法族：**鲁棒决策与因果模型可识别性**；图谱动作：`enrich_existing`。
- 直觉：若要求策略在足够丰富的环境变化下仍近似最优，策略必须携带足够因果信息。
- 数学模板：`概念模板：sup_{e∈E}Regret_e(π)≤δ ⇒ 在论文条件下可从策略恢复近似因果模型。`
- 前提：环境变化族足够丰富；满足论文决策和因果模型假设。
- 边界：不能从普通 OOD 得分直接推出模型已学到可解释因果图。
- Oral 证据：[ICLR 官方 2024 博客将同名论文链接至 /virtual/2024/oral/19724。](https://blog.iclr.cc/category/iclr-2024/)
- [论文原始来源](https://arxiv.org/abs/2402.10877)；阅读深度：摘要。

## 2024 · Amortizing intractable inference in large language models

- 方法族：**GFlowNet与流守恒采样**；图谱动作：`new_family`。
- 直觉：有多个好解释或推理路径时，学习按奖励成比例抽样，比只寻找单个最高奖励解更能保留多样性。
- 数学模板：`通用 GFlowNet 模板：终端 Pθ(z)=R(z)/Z；中间状态流入总量=流出总量。`
- 前提：非负可评估奖励；生成轨迹的状态结构可定义。
- 边界：奖励错设会采到错误解释；训练近似不保证精确贝叶斯后验。
- Oral 证据：[ICLR 官方 2024 博客将同名论文链接至 /virtual/2024/oral/19763。](https://blog.iclr.cc/category/iclr-2024/)
- [论文原始来源](https://arxiv.org/abs/2310.04363)；阅读深度：摘要。

## 2025 · Generator Matching: Generative modeling with arbitrary Markov processes

- 方法族：**马尔可夫生成元与算子建模**；图谱动作：`new_family`。
- 直觉：将连续运动、扩散、离散跳转都视为无穷小演化算子，便可在同一框架设计生成过程。
- 数学模板：`通用定义：L_t f(x)=lim_{h→0}(E[f(X_{t+h})|X_t=x]−f(x))/h；∂_t p=L_t* p。`
- 前提：过程、定义域及生成元满足相应正则条件；条件生成元可构造。
- 边界：统一表达不代表任意生成元容易训练或模拟；数值误差需单独验证。
- Oral 证据：[官方页面经 requests HTTP 200 读取，正文明确标注 2025 Oral 并列出同名论文。](https://iclr.cc/virtual/2025/oral/31846)
- [论文原始来源](https://openreview.net/forum?id=RuP17cJtZo)；阅读深度：摘要。

## 2026 · GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models

- 方法族：**充分统计量与随机转移重参数化**；图谱动作：`new_family`。
- 直觉：把采样的随机性压缩为高斯潜在统计量，通过已有流模型的确定性演化实现可分支采样与奖励引导。
- 数学模板：`概念模板：ε∼N(0,I)，x′=Φ_{x,t,t′}(ε)；具体充分性由论文构造保证。`
- 前提：采用论文规定的预训练流及路径构造；数值积分和向量场精度足够。
- 边界：并非任意转移核都可直接套同一构造；奖励偏差仍会影响对齐结果。
- Oral 证据：[OpenReview 官方作者 profile 在同名论文条目下显示 ICLR 2026 Oral。](https://openreview.net/profile?id=~Ricky_T._Q._Chen2)
- [论文原始来源](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ad6ac52e02e14e0f2ddc0d4587ab47f1-Abstract-Conference.html)；阅读深度：摘要。

## 从论文到可证伪实验

以下为本项目提出的实验建议，不是原论文已完成实验的转述：

| 方法族 | 应检查的现象 | 关键对照/证伪方式 |
|---|---|---|
| 群平均/谱对称 | 同一对象换坐标或谱基后预测改变 | 固定对象随机旋转/换基，比较任务精度与不变误差 |
| 重要性采样 | 模型漏掉少数模式 | 在可积分低维目标上比较 ESS、模式覆盖与目标期望误差 |
| 均衡 | 策略能被其他玩家单边利用 | 用独立更强 best-response 搜索测 exploitability；损失小不足以验收 |
| 黎曼流/生成元 | 数据存在拓扑约束或连续离散混合 | 比较约束违例、分布误差、同预算采样开销 |
| GFlowNet/QD | 单一最优解不利于后续任务 | 同预算比较覆盖、质量及迁移任务表现；去掉无效多样性 |
| 充分统计量 | 推理内循环成本高 | 检验转移分布误差与收益-成本曲线，不仅吞吐量 |
