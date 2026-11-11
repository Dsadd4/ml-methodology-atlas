# NeurIPS / ICML 2022–2026：首轮 Oral 方法论抽样

核查日期：2026-10-27。19篇精选方法卡，18篇具有官方 Oral 页面、Oral 列表或会议托管且明确写出 Oral 的讲者幻灯片，1篇目前只有作者 Oral 声明，单列待核。该集合是面向数学方法多样性的目的性抽样，**不是五年全部 Oral 普查**；不能据此估计各方法流行程度。

阅读深度 `abstract` 表示摘要/介绍或讲者材料层面的提炼，`method_section` 表示实际读到方法定义；这里仅 Learning diffusion at lightspeed 标为后者。卡中的“框架/概念模板”是研究迁移用的统一表达，并非声称逐字抄录论文公式。假设和证伪实验中有研究者判断，不能替代论文定理逐条核验。所有性能数字只作为作者论文主张，本轮未重现实验，故卡片不堆叠排行榜数字。

## 方法论增量

建议新增独立族：①在线学习与regret；②博弈与均衡（待官方Oral标签核验的代表文献不计入已核Oral）；③差分隐私；④双曲/非欧几何；⑤变分梯度流与逆最优性；⑥Bellman固定点与分布算子；⑦离散流匹配/连续时间Markov链；⑧局部敏感度与数据影响归因；⑨偏好学习与奖励重参数化。

群平均/NTK、层次OT、条件边际似然、WoW、矩匹配优先丰富已有族，避免把每个论文名字都新建一类。训练算法工具如镜像下降可作为跨族算子，和任务框架分层记录。

## 年份覆盖和明确缺口

| 年份 | ICML 已核Oral | NeurIPS 已核Oral | 本轮缺口 |
|---|---:|---:|---|
|2022|1|0|NeurIPS swap-regret有发表和作者Oral声明，官方标签未核|
|2023|2|1|JAWS-X已补官方JSON的Accept (Oral & Poster)|
|2024|4|1|仅方法多样性抽样，没有完整名单分母|
|2025|5|1|仅方法多样性抽样，没有完整名单分母|
|2026|1|2|ICML一篇展示类型Oral、录用标签spotlight，已显式保留两字段；NeurIPS两篇Accept(oral)|

2026已通过官方静态program JSON逐项核验，见后述补充审计。Downloads不用于判定展示级别。补采入口：[ICML官方Downloads](https://icml.cc/Downloads/2026)、[NeurIPS官方Downloads](https://neurips.cc/Downloads/2026)。Information Flow Reveals When to Trust Language Models 已通过官方JSON核定展示事件为Oral，但录用标签为spotlight；两个含义不得混同。不要把仅仅接受/Spotlight视作Oral。

## 已核实 Oral 方法卡

### icml2022-bayesian-selection · Bayesian Model Selection, the Marginal Likelihood, and Generalization

- **会议**：ICML 2022；verified。[首页：ICML 2022, long oral presentation](https://icml.cc/media/icml-2022/Slides/17992.pdf)；[论文](https://arxiv.org/abs/2202.11678)。
- **可迁移方法**：贝叶斯模型选择；条件边际似然。选先验科学假说和预测训练后模型泛化是两个问题；条件边际似然先用部分数据形成后验，再评价剩余数据。
- **建模表达**：概念模板：log p(D_rest | D_prefix)=log ∫ p(D_rest|θ)p(θ|D_prefix)dθ
- **成立前提**：数据拆分与预测目标一致；后验近似质量可接受。
- **失效边界**：边际似然大不保证训练后泛化好；条件版本也受划分、先验与近似误差影响。
- **证伪实验建议**：改变先验尺度和训练子集比例，比较边际似然/条件边际似然与独立测试似然的排序一致性。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### neurips2023-dpo · Direct Preference Optimization: Your Language Model is Secretly a Reward Model

- **会议**：NeurIPS 2023；verified。[页面标注：2023 Oral](https://neurips.cc/virtual/2023/oral/73865)；[论文](https://arxiv.org/abs/2305.18290)。
- **可迁移方法**：偏好学习；奖励与最优策略的重参数化。将KL正则化奖励优化的最优策略关系代回偏好模型，使偏好对直接监督策略。
- **建模表达**：概念模板：rθ(x,y)=β log[πθ(y|x)/πref(y|x)]+c(x)；对偏好奖励差作logistic分类
- **成立前提**：偏好概率模型、KL正则目标和参考策略支持集需与推导匹配。
- **失效边界**：离线偏好覆盖不足、偏好噪声与参考策略偏差仍会影响结果；不能据此断言无需任何奖励假设。
- **证伪实验建议**：固定偏好数据/模型/预算，与显式奖励模型路线比较，并分层改变偏好噪声和分布外提示。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2023-jawsx · JAWS-X: Addressing Efficiency Bottlenecks of Conformal Prediction Under Standard and Feedback Covariate Shift

- **会议**：ICML 2023；verified。[官方JSON id25430：decision=Accept (Oral & Poster)；virtualsite_url=/virtual/2023/oral/25430](https://icml.cc/static/virtual/data/icml-2023-orals-posters.json)；[论文](https://proceedings.mlr.press/v202/prinster23a.html)。
- **可迁移方法**：分布偏移下保形预测；近似影响函数。把随预测器反馈而变化的数据分布纳入置信区间设计，同时处理重复拟合的计算成本。
- **建模表达**：框架模板：用目标/训练分布密度比加权校准分数；以近似更新减轻逐样本重拟合。非原文完整算法
- **成立前提**：密度比、支持集与反馈机制需满足论文保证所用假设；近似误差须另验。
- **失效边界**：不能把协变量偏移保证推广到任意概念漂移，也不能把近似算法自动视为精确有限样本保证。
- **证伪实验建议**：并列报告目标域覆盖率、区间宽度、运行时；分别改变密度比误差和反馈强度。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### neurips2024-lightspeed · Learning diffusion at lightspeed

- **会议**：NeurIPS 2024；verified。[官方托管幻灯片：NeurIPS 2024, oral](https://neurips.cc/media/neurips-2024/Slides/93047.pdf)；[论文](https://arxiv.org/abs/2406.12616)。
- **可迁移方法**：Wasserstein梯度流；逆最优性条件。观察分布随时间怎样移动，反推驱动能量；用一步变分更新的最优性条件避免反复求解内层问题。
- **建模表达**：框架：μ_next=argmin_μ {Fθ(μ)+W₂²(μ,μ_now)/(2τ)}；以一阶最优性残差拟合θ
- **成立前提**：快照动力学可以被设定的梯度流描述；传输与密度估计可信。
- **失效边界**：最优性残差小不自动代表能量唯一可识别；错误能量族、稀疏快照可造成混淆。
- **证伪实验建议**：有真值势能/交互/扩散项的合成动力学分别恢复，逐步降低快照密度，再检验未见时间段预测。
- **阅读记录**：method_section；扩充类型：new_family。

### icml2024-private-design · Privacy Preserving Adaptive Experiment Design

- **会议**：ICML 2024；verified。[页面标注：2024 Oral](https://icml.cc/virtual/2024/oral/35582)；[论文](https://arxiv.org/abs/2401.08224)。
- **可迁移方法**：差分隐私；情境bandit；实验设计。实验分配同时追求估计精度、累计收益和隐私，用Pareto边界说明不能只看某一个分数。
- **建模表达**：框架模板：min (Regret_T, Var(τ̂)) subject to (ε,δ)-DP
- **成立前提**：明确数据邻接、隐私预算、情境和处理效应模型；渐近推断需相应条件。
- **失效边界**：论文特定条件下隐私代价小，不代表任意样本规模或群体隐私都免费。
- **证伪实验建议**：同时扫描ε、样本量与稀有子群比例，报告CATE误差/覆盖、regret及隐私会计。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2024-rate-policy · Rate-Optimal Policy Optimization for Linear Markov Decision Processes

- **会议**：ICML 2024；verified。[官方Oral列表包含该题；对应oral/35519](https://icml.cc/virtual/2024/events/oral)；[论文](https://proceedings.mlr.press/v235/sherman24a.html)。
- **可迁移方法**：在线遗憾；自然梯度与镜像下降。以乐观价值估计驱动策略更新，配合无奖励预热与bonus更新节奏控制探索代价。
- **建模表达**：框架：Regret_K=Σ_k V_k(π_k)−min_πΣ_k V_k(π)；论文得到对K的Õ(√K)速率
- **成立前提**：线性MDP；随机损失+bandit反馈，或对抗损失+全信息反馈，须区分。
- **失效边界**：理论速率不能直接转给任意神经网络MDP；维数、时域与预热代价也需要计入。
- **证伪实验建议**：分别比较两种反馈设定，改变线性特征失配，报告累计regret而非只看最终回报。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2024-lsenet · LSEnet: Lorentz Structural Entropy Neural Network for Deep Graph Clustering

- **会议**：ICML 2024；verified。[官方Oral列表包含该题；对应oral/35538](https://icml.cc/virtual/2024/events/oral)；[论文](https://arxiv.org/abs/2405.11801)。
- **可迁移方法**：双曲几何；结构熵；层次划分。树状数据的表示空间与层次结构匹配，并以可微结构信息目标学习划分，减少预指定簇数的依赖。
- **建模表达**：框架模板：min_T DSI(G,T)；表示h_i位于Lorentz双曲流形。具体DSI定义需全文细读
- **成立前提**：图连边与属性反映待发现层次；曲率和树构造具有合理归纳偏置。
- **失效边界**：无需输入簇数不代表无需模型选择；噪声图或无层次数据可能不适合双曲结构。
- **证伪实验建议**：比较树状/平坦/随机图，控制参数和簇数信息，分别消融几何与结构熵。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2024-emergent-equivariance · Emergent Equivariance in Deep Ensembles

- **会议**：ICML 2024；verified。[官方Oral列表包含该题；对应oral/35462](https://icml.cc/virtual/2024/events/oral)；[论文](https://arxiv.org/abs/2403.03103)。
- **可迁移方法**：对称性；群平均；神经切线核。即使个体预测器不等变，充分增强后的集成预测也可在理论极限中出现等变性。
- **建模表达**：框架模板：f̄(x)=E_init[fθ(x)]；检验 f̄(gx)=ρ(g)f̄(x)
- **成立前提**：无限宽理论、初始化分布与完整数据增强条件；实际集成用有限Monte Carlo近似。
- **失效边界**：有限宽、有限成员数、连续群有限采样都会破坏精确等变；不等于所有域外预测正确。
- **证伪实验建议**：扫描宽度、集成规模和群采样密度，测域内/域外等变误差，同时报告任务误差。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### neurips2025-influence · A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning

- **会议**：NeurIPS 2025；verified。[官方托管幻灯片首页：NeurIPS 2025 oral](https://neurips.cc/media/neurips-2025/Slides/115685.pdf)；[论文](https://arxiv.org/abs/2505.19281)。
- **可迁移方法**：局部影响归因；梯度相似度。在线策略会改变后续训练数据，因此先把归因对象限制为检查点附近缓冲区，用样本梯度与动作/回报目标梯度的关系解释更新。
- **建模表达**：概念模板：influence_i ∝ ⟨∇θℓ_i,∇θJ_target⟩，正负号依损失/收益约定；不是全轨迹因果效应
- **成立前提**：局部检查点、近期缓冲、可微目标和PPO更新框架。
- **失效边界**：局部一阶关系不等于移除样本后的全训练因果贡献；筛选也会改变未来采样。
- **证伪实验建议**：用局部真实移除/重加权更新检验归因排序；对全训练干预另设独立实验，不混同两种证据。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2025-hierarchical-ot · Hierarchical Refinement: Optimal Transport to Infinity and Beyond

- **会议**：ICML 2025；verified。[页面标注：2025 Oral](https://icml.cc/virtual/2025/oral/47248)；[论文](https://arxiv.org/abs/2503.03025)。
- **可迁移方法**：最优传输；层次分治。先用低秩传输发现应一起匹配的簇，再递归细分至一一指派，把巨型匹配转为分层子问题。
- **建模表达**：概念模板：low-rank coupling → paired partitions → recursive child assignment
- **成立前提**：赋值/双射设定；理论所需低秩子问题解与分组性质成立。
- **失效边界**：近似子问题与错误粗分可能传播误差；不能把赋值保证推广到所有OT变体。
- **证伪实验建议**：在可精确求解的小规模上核对代价差，再逐步扩大规模，同时测内存、时间和层级误差。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### icml2025-td-flow · Temporal Difference Flows

- **会议**：ICML 2025；verified。[页面标注：2025 Oral](https://icml.cc/virtual/2025/oral/47200)；[论文](https://openreview.net/forum?id=j6H7c3aQyb)。
- **可迁移方法**：Bellman分布固定点；流匹配。直接学习随机几何时域的未来状态分布，利用概率路径上的Bellman关系训练，避免预测时逐步展开误差。
- **建模表达**：概念模板：未来分布M=(1−γ)P+γPM；概率路径的对应Bellman方程连接flow matching。此式是框架示意
- **成立前提**：固定策略下适用的Markov预测关系、几何时域及可学习概率路径。
- **失效边界**：直接未来分布预测不能自动提供每一步因果轨迹；训练自举偏差和域外转移仍需检验。
- **证伪实验建议**：固定训练数据与计算，比较rollout/直接未来分布在不同时域的分布误差、梯度方差和策略评估偏差。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2025-imm · Inductive Moment Matching

- **会议**：ICML 2025；verified。[官方Oral列表包含该题；对应oral/47188](https://icml.cc/virtual/2025/events/oral)；[论文](https://arxiv.org/abs/2503.07565)。
- **可迁移方法**：分布矩匹配；归纳自蒸馏。用分布层面的匹配构造少步生成训练，避免把每个样本路径一致性当作唯一目标。
- **建模表达**：概念模板：minθ D_moment(Pθ,Q_teacher(θ))；原始MMSD构造和梯度需进一步读全文
- **成立前提**：所选矩/核需足以区分分布；归纳训练和理论收敛要求成立。
- **失效边界**：分布层面理论不等于有限神经网络的训练必收敛；少步质量须同预算核验。
- **证伪实验建议**：固定模型与训练预算，扫描采样步数，分别报告分布指标、模式覆盖和训练稳定性。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### icml2025-defog · DeFoG: Discrete Flow Matching for Graph Generation

- **会议**：ICML 2025；verified。[官方Oral列表包含该题；官方作者代码链接oral/47238](https://icml.cc/virtual/2025/events/oral)；[论文](https://arxiv.org/abs/2410.04263)。
- **可迁移方法**：离散流匹配；连续时间Markov链。离散图的概率质量通过跳变率演化，训练路径与采样器设计可以分开，同时尊重节点置换。
- **建模表达**：框架模板：d p_t/dt=p_t Q_t；Q_t为连续时间Markov跳变生成元
- **成立前提**：合法速率矩阵、图置换性质和目标概率路径；理论对真实分布复制有模型准确性条件。
- **失效边界**：有限步采样、速率估计和图有效性约束都可能产生偏差。
- **证伪实验建议**：固定同一训练模型改采样器，比较分布距离、图有效性、步数/时间；置换输入检验一致性。
- **阅读记录**：abstract；扩充类型：new_family。

### icml2025-wow · Flowing Datasets with Wasserstein over Wasserstein Gradient Flows

- **会议**：ICML 2025；verified。[官方Oral列表包含该题；对应oral/47240](https://icml.cc/virtual/2025/events/oral)；[论文](https://arxiv.org/abs/2506.07534)。
- **可迁移方法**：分布之上的分布；Wasserstein梯度流。每个类别先表示为特征分布，整个数据集再表示为这些类别分布的混合，使数据集本身可被连续优化。
- **建模表达**：概念模板：ν=Σ_c w_c δ_{μ_c}；WoW²(ν,ν′)=inf_Γ∫W₂²(μ,μ′)dΓ；沿目标泛函梯度移动
- **成立前提**：类条件经验分布有代表性；底层特征距离和跨类传输结构有语义。
- **失效边界**：高维距离估计、类缺失和切片近似误差可影响效果；距离小不等于下游预测必提升。
- **证伪实验建议**：对标签结构错配/缺失类别设计对照，比较普通OT与WoW对齐和真正独立下游任务。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### icml2023-subtb · Learning GFlowNets From Partial Episodes For Improved Convergence And Stability

- **会议**：ICML 2023；verified。[官方托管PDF标题：ICML 2023 ORAL FINAL](https://icml.cc/media/icml-2023/Slides/25580_Op4JkaX.pdf)；[论文](https://proceedings.mlr.press/v202/madan23a.html)。
- **可迁移方法**：概率流守恒；GFlowNet；偏差方差权衡。生成候选的目标是按非归一化奖励成比例采样，用不同长度子轨迹的流平衡连接局部与整轨迹训练。
- **建模表达**：框架模板：P_terminal(x)∝R(x)；SubTB(λ)加权不同长度子轨迹的前后向流平衡残差
- **成立前提**：有向无环生成过程；足够表达能力、采样支持与优化收敛条件。
- **失效边界**：目标是多样性采样而非只找最大奖励；低平衡损失的意义依赖覆盖，奖励模型也可能错。
- **证伪实验建议**：在可枚举空间测总变差和模式覆盖，再增大序列长度/奖励稀疏度；比较梯度方差与收敛。
- **阅读记录**：abstract；扩充类型：new_family。

### neurips2026-drifting · Generative Modeling via Drifting

- **会议**：NeurIPS 2026；verified。[官方JSON id154241：event_type=Oral；decision=Accept (oral)；virtualsite_url=/virtual/2026/oral/154241](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)；[论文](https://arxiv.org/abs/2602.04770)。
- **可迁移方法**：分布动力学；推前映射；平衡匹配。把生成分布的逐步变化放到训练过程，训练一个推前映射实现单步采样。
- **建模表达**：框架模板：qθ=(fθ)#p_prior；drift V[p,q]在p=q时为零，优化器更新fθ使qθ靠近p
- **成立前提**：漂移场、数据和生成样本估计有效；网络有足够表示能力。
- **失效边界**：p=q⇒V=0不自动意味着V=0⇒p=q；平衡唯一性、优化收敛和有限样本偏差必须另核。
- **证伪实验建议**：先在可知分布上检测伪平衡/模式遗漏；固定预算比较单步与多步方法的覆盖和采样代价。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### neurips2026-ftrl-limits · Follow the Regularized Leader Does Not Converge in Constrained Optimization

- **会议**：NeurIPS 2026；verified。[官方JSON id150987：event_type=Oral；decision=Accept (oral)；virtualsite_url=/virtual/2026/oral/150987](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)；[论文](https://arxiv.org/abs/2610.35004)。
- **可迁移方法**：在线正则化；变分不等式；收敛反例。目标单调改善或低regret并不保证约束非凸问题达到一阶稳定点；需要监控KKT条件。
- **建模表达**：框架模板：x_t=argmin_x{⟨Σ_s<t g_s,x⟩+R(x)/η}；连续时间FTRL反例中KKT gap持续非零
- **成立前提**：负结论针对无限光滑约束问题的连续时间FTRL；解析函数和Euclidean正则具有不同结果。
- **失效边界**：不能将一个反例解读为所有FTRL都失败；连续时间和有限步实现须分开。
- **证伪实验建议**：重建论文反例，同时画目标值、KKT gap、轨迹；与镜像下降比较，并区分光滑/解析目标。
- **阅读记录**：abstract；扩充类型：enrich_existing。

### icml2026-information-flow · Information Flow Reveals When to Trust Language Models

- **会议**：ICML 2026；verified。[官方JSON id71120：event_type=Oral；但decision=Accept (spotlight)；virtualsite_url=/virtual/2026/oral/71120](https://icml.cc/static/virtual/data/icml-2026-orals-posters.json)；[论文](https://proceedings.mlr.press/v306/xu26c.html)。
- **可迁移方法**：信息流归因；置信度校准。沿模型层追踪上下文token贡献，把证据相关性匹配程度和贡献集中程度用于判断回答可靠性。
- **建模表达**：概念模板：confidence=g(simulatability, concentration)；不是仅用输出token熵
- **成立前提**：能访问内部信息传播；检索证据和问题相关性可评估，校准集有代表性。
- **失效边界**：内部归因不自动是因果证据；集中于错误证据也可能过度自信。官方展示事件为Oral，但录用标签是spotlight，不能改写成Accept(oral)。
- **证伪实验建议**：在相关/干扰/错误检索证据下比较AUROC、校准误差与拒答风险；固定模型和推理成本。
- **阅读记录**：abstract；扩充类型：enrich_existing。

## 待核官方 Oral 标签的候选（不计已核Oral）

### neurips2022-swap-regret · Uncoupled Learning Dynamics with O(log T) Swap Regret in Multiplayer Games

- **会议**：NeurIPS 2022；unverified。[作者页面报告oral；本轮未取得官方program的oral标签](https://www.andrew.cmu.edu/user/ianagnos/)；[论文](https://proceedings.neurips.cc/paper_files/paper/2022/hash/15d45097f9806983f0629a77e93ee60f-Abstract-Conference.html)。
- **可迁移方法**：无悔学习；博弈均衡；乐观正则化。每个玩家只需自身反馈；控制换行动规则后的事后收益改进，连接重复博弈与相关均衡。
- **建模表达**：框架模板：R_swap(T)=max_φ Σ_t[u(φ(a_t),a_-t)−u(a_t,a_-t)]；乐观正则化结合自协调障碍
- **成立前提**：对数速率要求所有玩家按指定动力学更新；一般对手环境对应不同速率。
- **失效边界**：低swap regret连接经验分布的相关均衡，不能直接声称最后一次策略达到纳什均衡。
- **证伪实验建议**：在一般和博弈上同时画swap regret/T、相关均衡缺口与最后迭代震荡，区分平均收敛与逐点收敛。
- **阅读记录**：abstract；扩充类型：new_family。

## 检索与审计记录

1. 先检索标题+会议+oral，再回到官方virtual页面/Oral列表/会议托管Slides核标签；作者首页仅作候选线索。
2. ICML2024和2025官方Oral列表成功读取；部分单篇页浏览工具返回restricted URL，列表仍有题目与Oral标签。保留列表作为证据，不能把单页读取失败解释成论文不存在。
3. NeurIPS2023 DPO官方单篇页标2023 Oral；2024 Learning diffusion at lightspeed与2025 Snapshot of Influence的官方托管Slides首页显式标oral。
4. OpenReview部分页面触发browser challenge，因此论文内容交叉使用PMLR、NeurIPS proceedings和作者arXiv。仅有OpenReview URL不表示本轮全文读过。
5. 2022的一张待核卡保留明确标记；2023 JAWS-X已通过官方JSON补核。2026官方静态program JSON通过urllib轻量读取成功，按标题、事件ID、event_type、decision和paper_url交叉核验。相同论文Poster/Oral事件不重复计篇。
6. 搜索词包括：NeurIPS 2022 uncoupled swap regret oral；ICML 2022 Bayesian Model Selection oral；ICML2023 JAWS-X oral；NeurIPS2024 diffusion lightspeed oral；NeurIPS2025 Snapshot Influence oral；ICML2024/2025 events/oral；ICML2026 Information Flow Reveals oral。
7. 后继最有价值工作：补齐年份缺口的官方标签，再选每个新增族至少一篇完整方法/定理精读；全文精读前不得将模板当作论文可运行算法。

### NeurIPS2022展示分类的补充核查

官方静态数据 [neurips-2022-orals-posters.json](https://neurips.cc/static/virtual/data/neurips-2022-orals-posters.json) 于2026-10-27有界读取成功：该文件的事件记录为Poster 2,905条、Spotlight 585条，没有eventtype=Oral。这里是**该端点当前快照的事件计数**，不是论文去重数，也不能单独证明整个会议从未有口头报告。

- Swap regret只找到Poster55247、decision=Accept；作者报告oral与官方当前分类不一致，继续unverified。
- Trajectory balance只找到Poster53114。
- Elucidating the Design Space of Diffusion-Based Generative Models另有Spotlight64974；不能为补齐年度覆盖把它改写为Oral。
- 因此NeurIPS2022的空缺是展示口径需进一步核定的真实缺口，后继可单独建Spotlight补充层，但不混入本轮严格Oral集合。
