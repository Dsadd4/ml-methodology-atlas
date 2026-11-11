# 方法论详细卡

每项独立说明适用条件；参考文献为框架入口，Oral为本轮实例。`related`只表示关联，不作为该框架直接实例。

## M01 贝叶斯推断与模型平均

**直觉：** 有限证据支持多个解释，应保留不确定性并随证据更新。

**数学模板：** p(θ|D)∝p(D|θ)p(θ)

**适用问题：** 小样本、先验融合、预测分布

**成立条件：** 先验和似然能表达任务；近似后验需检查。

**失效边界：** softmax置信度不等于参数后验；贝叶斯也不自动校准。

**与相邻方法的区别：** 推断相信什么，与M06如何行动不同。

**框架文献：** [Weight Uncertainty in Neural Networks](https://proceedings.mlr.press/v37/blundell15.html)

**本轮论文联系：**

- ICML 2022 [Bayesian Model Selection, the Marginal Likelihood, and Generalization](https://icml.cc/media/icml-2022/Slides/17992.pdf)；主要联系；阅读层级 `abstract`。
- CVPR 2024 [Producing and Leveraging Online Map Uncertainty in Trajectory Prediction](https://cvpr.thecvf.com/Conferences/2024/News/Oral_Papers)；主要联系；阅读层级 `abstract`。

## M02 潜变量建模与变分推断

**直觉：** 用隐藏状态解释观测，再用可计算分布近似复杂后验。

**数学模板：** ELBO=E_q[log p(x,z)−log q(z|x)]

**适用问题：** 生成、缺失数据、多机制混合

**成立条件：** 近似族与潜变量结构要适合数据。

**失效边界：** 潜变量命名不保证可识别或可解释。

**与相邻方法的区别：** 潜变量是模型结构，变分推断是求解工具；本版保留原合并条目并明确两层。

**框架文献：** [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M03 最大熵原理与熵正则

**直觉：** 满足已知信息后尽量不作额外确定性假设。

**数学模板：** max_p H(p), s.t. E_p[f]=c

**适用问题：** 探索、概率分布构造、多解保留

**成立条件：** 约束、样本空间与参考测度明确。

**失效边界：** 最大随机性并非任务效用最大。

**与相邻方法的区别：** 关注分布选择，与M04任务信息压缩不同。

**框架文献：** [Information Theory and Statistical Mechanics](https://journals.aps.org/pr/abstract/10.1103/PhysRev.106.620)

**本轮论文联系：**

- NeurIPS 2023 [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://neurips.cc/virtual/2023/oral/73865)；辅助联系；阅读层级 `abstract`。

## M04 信息瓶颈与率失真思想

**直觉：** 压缩输入细节，同时保留预测任务所需的信息。

**数学模板：** min I(X;Z)−βI(Z;Y)

**适用问题：** 表征压缩、抗干扰、多视图

**成立条件：** 明确保留目标及可计算的互信息估计/变分界。

**失效边界：** 估计偏差、连续确定性编码等会使理想目标难以直接优化。

**与相邻方法的区别：** 信息瓶颈是任务相关的率失真视角，不是任意减小熵。

**框架文献：** [Deep Variational Information Bottleneck](https://arxiv.org/abs/1612.00410)

**本轮论文联系：**

- CVPR 2026 [Differentiable Vector Quantization for Rate-Distortion Optimization of Generative Image Compression](https://cvpr.thecvf.com/virtual/2026/oral/40298)；主要联系；阅读层级 `abstract`。

## M05 最小描述长度 MDL

**直觉：** 简洁的模型与短的残差描述共同构成好解释。

**数学模板：** min_M L(M)+L(D|M)

**适用问题：** 模型选择、规则和技能压缩

**成立条件：** 编码方案、数据精度与复杂度口径明确。

**失效边界：** 参数少不必然描述短；压缩会丢失任务信息。

**与相邻方法的区别：** 总编码长度，不等于M22非零数或M23方向数。

**框架文献：** [A Tutorial Introduction to MDL](https://arxiv.org/abs/math/0406077)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M06 决策论与期望效用

**直觉：** 行动价值由结果概率、收益和成本共同决定。

**数学模板：** a*=argmax_a E[U(a,Y)|D]−C(a)

**适用问题：** 工具、拒答、专家调用、资源分配

**成立条件：** 效用与概率可估计，成本口径一致。

**失效边界：** 置信度提高不等于决策价值提高。

**与相邻方法的区别：** 单个决策者面对不确定性；M31处理策略性他人。

**框架文献：** [Principles of Metareasoning](https://www.sciencedirect.com/science/article/pii/000437029190015C)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M07 主动学习与最优实验设计

**直觉：** 选择最能减少目标未知程度的观测。

**数学模板：** a*=argmax_a I(Θ;O_a|D)

**适用问题：** 标注、传感、实验选择

**成立条件：** 区分可约模型未知与不可约噪声。

**失效边界：** 最高预测熵可能只选到噪声；信息增益不保证任务收益。

**与相邻方法的区别：** 以辨识或信息为目标；M08以决策收益为目标。

**框架文献：** [Deep Bayesian Active Learning](https://proceedings.mlr.press/v70/gal17a.html)

**本轮论文联系：**

- ICML 2024 [Privacy Preserving Adaptive Experiment Design](https://icml.cc/virtual/2024/oral/35582)；辅助联系；阅读层级 `abstract`。

## M08 信息价值与计算价值

**直觉：** 新证据或计算只有改善最终决策才值得花费。

**数学模板：** VOI(a)=E_o[V(D,o,a)]−V(D)

**适用问题：** 看哪里、查什么、追加推理

**成立条件：** V为最优条件期望效用，观测模型可估计。

**失效边界：** 用事后正确答案估计动作价值会泄漏；模型误差会误选。

**与相邻方法的区别：** 信息价值不等于熵下降；与M09多步停止互补。

**框架文献：** [Principles of Metareasoning](https://www.sciencedirect.com/science/article/pii/000437029190015C)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M09 最优停止

**直觉：** 比较现在交付与继续计算后的预期净收益。

**数学模板：** V(s)=max{R_stop(s),−c(s)+E[V(S')|s]}

**适用问题：** 早退、推理深度、检测终止

**成立条件：** 状态、转移及成本可建模；停止规则不看未来。

**失效边界：** 任意置信度阈值不是最优停止的证明。

**与相邻方法的区别：** 优化停止时机；M35保证自适应停止下统计有效性。

**框架文献：** [Deep Optimal Stopping](https://jmlr.csail.mit.edu/papers/volume20/18-232/18-232.pdf)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M10 最优控制与MPC

**直觉：** 行动改变未来状态，规划后根据反馈重算。

**数学模板：** min Σ_k c(s_k,a_k)+V_f(s_H), s_{k+1}=F(s_k,a_k)

**适用问题：** 闭环Agent、机器人、动态调度

**成立条件：** 动力学、观测与约束可信。

**失效边界：** 误差累积；有反馈不代表稳定。

**与相邻方法的区别：** 显式优化轨迹；不同于只对当前动作评分。

**框架文献：** [Differentiable MPC](https://proceedings.neurips.cc/paper/2018/hash/ba6d843eb4251a4526ce65d1807a9309-Abstract.html)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M11 约束优化与拉格朗日对偶

**直觉：** 区分希望优化的性能与必须满足的限制。

**数学模板：** min_θ L(θ), C_j(θ)≤b_j

**适用问题：** 预算、风险、延迟、受约束策略

**成立条件：** 约束可测；区分平均约束与逐样本约束。

**失效边界：** 固定罚项不保证硬约束；非凸情形不自动强对偶。

**与相邻方法的区别：** 对偶变量是限制的价格，不是随意loss权重。

**框架文献：** [Convex Optimization](https://stanford.edu/~boyd/cvxbook/)

**本轮论文联系：**

- NeurIPS 2026 [Follow the Regularized Leader Does Not Converge in Constrained Optimization](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)；辅助联系；阅读层级 `abstract`。

## M12 多目标与Pareto优化

**直觉：** 不同目标未必有统一兑换比例，应分析不可支配解。

**数学模板：** min_θ (L_1(θ),…,L_m(θ))

**适用问题：** 多任务、准确率成本权衡

**成立条件：** 明确偏好和各目标可比性。

**失效边界：** 驻点不等于全局Pareto最优；加权和会漏非凸前沿。

**与相邻方法的区别：** 多个系统目标，不要求M31中的多个战略参与者。

**框架文献：** [Multi-Task Learning as Multi-Objective Optimization](https://papers.nips.cc/paper_files/paper/2018/hash/432aca3a1e345e339f35a30c8f65edce-Abstract.html)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M13 鲁棒优化、对抗训练与DRO

**直觉：** 在明确的不利变化范围内控制最坏损失。

**数学模板：** min_θ sup_{Q∈U(P)} E_Q[ℓ_θ]

**适用问题：** 分布偏移、攻击、尾部与群体风险

**成立条件：** 不确定集合对应真实变化，内层求解足够强。

**失效边界：** 像素范数鲁棒不等于语义鲁棒；集合过宽会保守。

**与相邻方法的区别：** min–max是形式；这里max对象是允许的环境/分布。

**框架文献：** [Learning Models with Uniform Performance via DRO](https://arxiv.org/abs/1810.08750)

**本轮论文联系：**

- ICLR 2024 [Robust agents learn causal world models](https://blog.iclr.cc/category/iclr-2024/)；辅助联系；阅读层级 `abstract`。
- ICCV 2023 [Robust Evaluation of Diffusion-Based Adversarial Purification](https://iccv2023.thecvf.com/main.conference.program-107.php)；主要联系；阅读层级 `abstract`。
- ECCV 2024 [RACE: Robust Adversarial Concept Erasure for Secure Text-to-Image Diffusion Model](https://eccv.ecva.net/virtual/2024/oral/2342)；主要联系；阅读层级 `abstract`。

## M14 双层优化与元学习

**直觉：** 学习使模型学得更好的初始化、规则或数据权重。

**数学模板：** min_φ L_val(θ*(φ),φ), θ*(φ)∈argmin_θ L_train(θ,φ)

**适用问题：** 学loss、超参数、快速适应

**成立条件：** 外层数据独立性、内层求解精度明确。

**失效边界：** 验证集会被外层过拟合；截断梯度改变目标。

**与相邻方法的区别：** 嵌套优化；M39提供求导方式但不是同一科学目标。

**框架文献：** [Bilevel Programming for Hyperparameter Optimization and Meta-Learning](https://proceedings.mlr.press/v80/franceschi18a.html)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M15 子模优化与覆盖

**直觉：** 已有覆盖越多，相似新增元素的边际收益越小。

**数学模板：** Δ(e|A)≥Δ(e|B), A⊆B

**适用问题：** 样本、工具、专家子集选择

**成立条件：** 目标确有收益递减，近似保证依单调性及预算形式。

**失效边界：** 强互补证据不满足子模性。

**与相邻方法的区别：** 组合选择中的结构假设，不是任意贪心算法。

**框架文献：** [Adaptive Submodularity](https://ed.aaai.org/Papers/JAIR/Vol42/JAIR4212.pdf)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M16 对称性、不变性与等变性

**直觉：** 输入按某种规律变化，输出也应保持或按规律变化。

**数学模板：** f(ρ_X(g)x)=ρ_Y(g)f(x)

**适用问题：** 分子、点云、集合、视觉

**成立条件：** 真实任务遵守相应群作用。

**失效边界：** 会改变标签的变换不应强制不变；增强不等于严格等变。

**与相邻方法的区别：** 变换结构；M18关注环境变化而不是群变换。

**框架文献：** [Group Equivariant CNNs](https://proceedings.mlr.press/v48/cohenc16.html)

**本轮论文联系：**

- ICLR 2022 [Frame Averaging for Invariant and Equivariant Network Design](https://iclr.cc/virtual/2022/oral/6190)；主要联系；阅读层级 `abstract`。
- ICLR 2023 [Sign and Basis Invariant Networks for Spectral Graph Representation Learning](https://iclr.cc/virtual/2023/events/oral)；主要联系；阅读层级 `abstract`。
- ICML 2024 [Emergent Equivariance in Deep Ensembles](https://icml.cc/virtual/2024/events/oral)；主要联系；阅读层级 `abstract`。

## M17 结构因果模型与干预

**直觉：** 研究改变某因素的后果，而不只拟合相关。

**数学模板：** X_i=f_i(Pa_i,U_i); P(Y|do(X=x))

**适用问题：** 去混杂、机制、反事实

**成立条件：** 识别假设、干预或环境信息足够。

**失效边界：** attention或普通消融不能自动识别因果效应。

**与相邻方法的区别：** 因果识别先于M50统计估计。

**框架文献：** [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107)

**本轮论文联系：**

- ICLR 2024 [Robust agents learn causal world models](https://blog.iclr.cc/category/iclr-2024/)；主要联系；阅读层级 `abstract`。

## M18 跨环境不变学习

**直觉：** 跨环境稳定的预测机制有望迁移。

**数学模板：** min_Φ,w Σ_e R^e(w∘Φ), w∈argmin_v R^e(v∘Φ) ∀e

**适用问题：** 域泛化、抗伪相关

**成立条件：** 训练环境有足够变化且目标机制确实稳定。

**失效边界：** 训练环境不变不自动意味着因果或任意OOD保证。

**与相邻方法的区别：** 稳定预测机制不是M16的输入对称性。

**框架文献：** [Invariant Risk Minimization](https://arxiv.org/abs/1907.02893)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M19 图模型、因子分解与消息传递

**直觉：** 把局部依赖组合为整体判断。

**数学模板：** p(y|x)∝∏_a ψ_a(y_a,x); h'_v=U(h_v,Σ_u M(h_v,h_u,e_uv))

**适用问题：** 分子、关系、序列、联合输出

**成立条件：** 边、因子及条件独立性有意义。

**失效边界：** 神经消息传递不自动有概率推断语义。

**与相邻方法的区别：** 保留原合并条目；概率因子与神经聚合是两个层级。

**框架文献：** [Neural Message Passing for Quantum Chemistry](https://proceedings.mlr.press/v70/gilmer17a.html)

**本轮论文联系：**

- ECCV 2022 [Learning Topological Interactions for Multi-Class Medical Image Segmentation](https://eccv2022.ecva.net/program/accepted-papers/)；相关联系；阅读层级 `method_section`。

## M20 最优传输

**直觉：** 匹配两组分布时同时遵守质量约束并最小化移动代价。

**数学模板：** min_{π∈Π(P,Q)} E_π[c(x,y)]

**适用问题：** 无配对匹配、跨模态、空间映射

**成立条件：** 代价、质量与边缘约束有领域意义。

**失效边界：** 边缘对齐不保证语义或条件分布对齐。

**与相邻方法的区别：** 主要约束端点耦合；M46约束随机路径分布。

**框架文献：** [Sinkhorn Distances](https://papers.nips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html)

**本轮论文联系：**

- ICLR 2023 [Neural Optimal Transport](https://iclr.cc/virtual/2023/events/oral)；主要联系；阅读层级 `abstract`。
- NeurIPS 2024 [Learning diffusion at lightspeed](https://neurips.cc/media/neurips-2024/Slides/93047.pdf)；辅助联系；阅读层级 `method_section`。
- ICML 2025 [Hierarchical Refinement: Optimal Transport to Infinity and Beyond](https://icml.cc/virtual/2025/oral/47248)；主要联系；阅读层级 `abstract`。
- ICML 2025 [Flowing Datasets with Wasserstein over Wasserstein Gradient Flows](https://icml.cc/virtual/2025/events/oral)；辅助联系；阅读层级 `abstract`。

## M21 核方法与分布嵌入

**直觉：** 用丰富特征空间中的均值表示与比较分布。

**数学模板：** MMD(P,Q)=‖μ_P−μ_Q‖_H

**适用问题：** 漂移检测、分布匹配、非参数检验

**成立条件：** 核与带宽适合差异尺度；辨识需相应核条件。

**失效边界：** 有限样本功效不足不能证明分布相同。

**与相邻方法的区别：** 核空间比较，不需要M20的运输计划。

**框架文献：** [A Kernel Two-Sample Test](https://www.jmlr.org/beta/papers/v13/gretton12a.html)

**本轮论文联系：**

- ICML 2025 [Inductive Moment Matching](https://icml.cc/virtual/2025/events/oral)；主要联系；阅读层级 `abstract`。
- NeurIPS 2026 [Generative Modeling via Drifting](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)；相关联系；阅读层级 `abstract`。

## M22 稀疏建模

**直觉：** 少数变量、连接或模块足以解释目标。

**数学模板：** min_θ L(θ)+λ‖θ‖_1

**适用问题：** 特征选择、稀疏图、模块选择

**成立条件：** 信号可被稀疏结构近似。

**失效边界：** 相关变量选择不稳定；稀疏不等于因果或硬件加速。

**与相邻方法的区别：** 限制非零数，不是限制独立方向数。

**框架文献：** [Lasso](https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/j.2517-6161.1996.tb02080.x)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M23 低秩与子空间学习

**直觉：** 高维变化主要沿少量共享方向发生。

**数学模板：** ΔW=BA, rank(BA)≤r

**适用问题：** 参数适配、多任务共享、矩阵恢复

**成立条件：** 目标变化具有低维近似。

**失效边界：** 低秩更新不证明原权重低秩。

**与相邻方法的区别：** 线性子空间；M42可处理弯曲的非线性几何。

**框架文献：** [LoRA](https://arxiv.org/abs/2106.09685)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M24 能量模型

**直觉：** 给候选输出定义兼容程度，再寻找低能量解。

**数学模板：** ŷ=argmin_y E_θ(x,y)

**适用问题：** 结构化预测、生成、约束满足

**成立条件：** 能量可学习，搜索和可能的归一化可处理。

**失效边界：** 只降低正例能量会塌缩；改名score不是新机制。

**与相邻方法的区别：** 能量只定义评分结构，需另给训练与推断算法。

**框架文献：** [A Tutorial on Energy-Based Learning](https://yann.lecun.org/exdb/publis/pdf/lecun-06.pdf)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M25 对比学习与度量学习

**直觉：** 通过哪些样本应相近或区分学习表征。

**数学模板：** −log exp(s(z,z+)/τ)/Σ_j exp(s(z,z_j)/τ)

**适用问题：** 检索、自监督、跨模态

**成立条件：** 正负样本与增强符合任务语义。

**失效边界：** 伪负样本与错误增强会丢失关键信息。

**与相邻方法的区别：** 学习相对关系，与完整生成密度不同。

**框架文献：** [SimCLR](https://proceedings.mlr.press/v119/chen20j.html)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M26 得分匹配、去噪与扩散

**直觉：** 学习概率密度的局部方向或噪声逆过程。

**数学模板：** s_θ(x,t)≈∇_x log p_t(x)

**适用问题：** 生成、补全、逆问题

**成立条件：** 噪声过程、学习目标及采样器一致。

**失效边界：** 此score不是一般分数；普通去噪不自动定义正确生成。

**与相邻方法的区别：** M45学概率流速度，M26典型学密度梯度。

**框架文献：** [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

**本轮论文联系：**

- ICLR 2023 [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://iclr.cc/virtual/2023/events/oral)；辅助联系；阅读层级 `abstract`。
- ICCV 2023 [Robust Evaluation of Diffusion-Based Adversarial Purification](https://iccv2023.thecvf.com/main.conference.program-107.php)；辅助联系；阅读层级 `abstract`。
- CVPR 2025 [TopoCellGen: Generating Histopathology Cell Topology with a Diffusion Model](https://cvpr.thecvf.com/virtual/2025/oral/35356)；辅助联系；阅读层级 `abstract`。

## M27 物理约束与科学机器学习

**直觉：** 数据之外，方程和守恒关系也能提供监督。

**数学模板：** L=L_data+λL_PDE+μL_boundary

**适用问题：** 科学预测、参数反演、稀疏观测

**成立条件：** 方程、边界、量纲与适用域正确。

**失效边界：** 残差小不保证解准确；损失尺度与梯度冲突。

**与相邻方法的区别：** 物理约束可与M40算子映射同时使用。

**框架文献：** [Physics-informed neural networks](https://www.sciencedirect.com/science/article/pii/S0021999118307125)

**本轮论文联系：**

- CVPR 2022 [SNUG: Self-Supervised Neural Dynamic Garments](https://cvpr2022.thecvf.com/orals-622-pm)；主要联系；阅读层级 `abstract`。

## M28 PAC-Bayes泛化分析

**直觉：** 用训练误差与预测器分布相对先验的复杂度控制风险。

**数学模板：** R(Q)≲R̂(Q)+√((KL(Q‖P)+log(1/δ))/n) [量级示意]

**适用问题：** 泛化界、随机化模型、复杂度正则

**成立条件：** 先验数据依赖须符合所用定理，损失条件成立。

**失效边界：** 界可能空泛；Q不必是真贝叶斯后验。

**与相邻方法的区别：** 控制泛化风险，与M29预测集合覆盖不同。

**框架文献：** [Computing Nonvacuous Generalization Bounds](https://arxiv.org/abs/1703.11008)

**本轮论文联系：**

- ECCV 2022 [PACTran: PAC-Bayesian Metrics for Estimating the Transferability of Pretrained Models to Classification Tasks](https://eccv2022.ecva.net/program/accepted-papers/)；主要联系；阅读层级 `abstract`。

## M29 共形预测

**直觉：** 用校准数据为预测集合提供覆盖保证。

**数学模板：** P(Y_new∈C_α(X_new))≥1−α

**适用问题：** 区间、候选集合、可靠输出

**成立条件：** 标准形式要求交换性和正确校准程序。

**失效边界：** 边际覆盖不保证每个样本或子群覆盖；漂移需额外处理。

**与相邻方法的区别：** 不需要完整概率模型，但不能自动决定是否调用专家。

**框架文献：** [A Gentle Introduction to Conformal Prediction](https://arxiv.org/abs/2107.07511)

**本轮论文联系：**

- ICML 2023 [JAWS-X: Addressing Efficiency Bottlenecks of Conformal Prediction Under Standard and Feedback Covariate Shift](https://icml.cc/static/virtual/data/icml-2023-orals-posters.json)；主要联系；阅读层级 `abstract`。

## M30 选择性预测与学习转交

**直觉：** 比较模型与专家在当前样本上的风险，选择谁回答。

**数学模板：** min_{f,g} E[g(X)ℓ_f+(1−g(X))ℓ_expert]

**适用问题：** 拒答、路由、人机协作

**成立条件：** 专家表现及转交成本可估计。

**失效边界：** 模型不确定不意味着专家更强。

**与相邻方法的区别：** M06的具体风险建模，不以置信度阈值替代协作效用。

**框架文献：** [Consistent Estimators for Learning to Defer](https://proceedings.mlr.press/v119/mozannar20b.html)

**本轮论文联系：**

- ICML 2026 [Information Flow Reveals When to Trust Language Models](https://icml.cc/static/virtual/data/icml-2026-orals-posters.json)；相关联系；阅读层级 `abstract`。

## M31 博弈论与均衡

**直觉：** 多个会反应的决策者互相影响，寻找互为最佳反应的策略。

**数学模板：** u_i(π_i*,π_-i*)≥u_i(π_i,π_-i*) ∀i,π_i

**适用问题：** 多Agent竞争合作、均衡学习

**成立条件：** 参与者、收益、信息与策略空间明确。

**失效边界：** 纳什不等于社会最优；梯度迭代不自动收敛均衡。

**与相邻方法的区别：** 比M13零和最坏情况更一般，可处理非零和互动。

**框架文献：** [Twenty Lectures on Algorithmic Game Theory](https://timroughgarden.org/notes.html)

**本轮论文联系：**

- ICLR 2024 [Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization](https://iclr.cc/virtual/2024/oral/19744)；主要联系；阅读层级 `abstract`。

## M32 机制设计与激励相容

**直觉：** 设计规则和奖励，使个体自利行为产生希望的系统结果。

**数学模板：** max_M E[W(M)]; u_i(truth)≥u_i(report) [IC模板]

**适用问题：** 资源分配、拍卖、奖励设计、信息报告

**成立条件：** 明确私有信息、效用及激励相容种类。 明确真实类型、配置、支付；DSIC对任意他人报告成立，BIC按信念取条件期望。

**失效边界：** 训练奖励高不保证部署激励相容；共享Agent不一定需要经济机制。

**与相邻方法的区别：** M31给定规则求行为，M32反过来设计规则。

**框架文献：** [Algorithmic Mechanism Design lectures](https://timroughgarden.org/f13/f13.html)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M33 在线学习与遗憾最小化

**直觉：** 环境逐步揭示结果，希望长期不输给合适的比较策略。

**数学模板：** R_T=Σ_t ℓ_t(a_t)−min_a Σ_t ℓ_t(a)

**适用问题：** 持续决策、在线路由、自适应优化

**成立条件：** 反馈、对手能力、比较类及静态/动态regret明确。

**失效边界：** 静态低遗憾不保证非平稳动态最优或最后一步均衡。

**与相邻方法的区别：** 分析在线学习代价；不等于普通增量训练。

**框架文献：** [Online Learning and Online Convex Optimization](https://courses.cs.washington.edu/courses/cse522/17sp/papers/Shalev-SchwartzOnlineOptimization.pdf)

**本轮论文联系：**

- ICML 2024 [Rate-Optimal Policy Optimization for Linear Markov Decision Processes](https://icml.cc/virtual/2024/events/oral)；主要联系；阅读层级 `abstract`。
- NeurIPS 2026 [Follow the Regularized Leader Does Not Converge in Constrained Optimization](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json)；主要联系；阅读层级 `abstract`。

## M34 Bandit与探索利用

**直觉：** 只看到选中行动的结果，必须主动探索以免长期选错。

**数学模板：** a_t=argmax_a [μ̂_t(a)+b_t(a)] [UCB模板]

**适用问题：** 工具选择、推荐、实验分配、模型路由

**成立条件：** 奖励反馈和随机/对抗设定明确；处理延迟与漂移。

**失效边界：** 只比较已选动作的平均分会产生选择偏差。

**与相邻方法的区别：** M33的一类部分反馈问题；与M07纯信息获取目标不同。

**框架文献：** [Bandit Algorithms](https://tor-lattimore.com/)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M35 序贯检验与随时有效推断

**直觉：** 观察过程中可随时停止，但错误控制仍应成立。

**数学模板：** P(∀t: μ∈C_t)≥1−α

**适用问题：** 自适应评测、早停实验、持续监测

**成立条件：** 条件矩、鞅或所用定理的采样条件成立。

**失效边界：** 反复查看普通置信区间不能自动保持显著性。

**与相邻方法的区别：** M09优化停止收益，M35控制停止后的推断错误。

**框架文献：** [Time-uniform nonparametric nonasymptotic confidence sequences](https://arxiv.org/abs/1810.08240)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M36 信息几何与自然梯度

**直觉：** 参数距离应衡量分布变化，而非仅欧氏坐标变化。

**数学模板：** θ'=θ−ηF(θ)^{-1}∇L(θ)

**适用问题：** 概率模型优化、策略更新、曲率预条件

**成立条件：** Fisher或近似度量有效；奇异时要正则或广义逆。

**失效边界：** 近似自然梯度不保证坐标不变或总更快。

**与相邻方法的区别：** 概率分布的几何；M42涵盖更一般流形。

**框架文献：** [Natural Gradient Works Efficiently in Learning](https://doi.org/10.1162/089976698300017746)

**本轮论文联系：**

- ICML 2024 [Rate-Optimal Policy Optimization for Linear Markov Decision Processes](https://icml.cc/virtual/2024/events/oral)；辅助联系；阅读层级 `abstract`。

## M37 镜像下降与Bregman几何

**直觉：** 更新应尊重变量的几何，例如概率单纯形。

**数学模板：** x'=argmin_x {η⟨g,x⟩+D_ψ(x,x_t)}

**适用问题：** 概率权重、在线学习、非欧氏优化

**成立条件：** 势函数凸性、定义域与步长条件明确。

**失效边界：** Bregman散度一般非对称，也不一定是距离。

**与相邻方法的区别：** 与自然梯度相关但有限步离散化不同；不混为同一算法。

**框架文献：** [Mirrorless Mirror Descent](https://proceedings.mlr.press/v130/gunasekar21a.html)

**本轮论文联系：**

- ICML 2024 [Rate-Optimal Policy Optimization for Linear Markov Decision Processes](https://icml.cc/virtual/2024/events/oral)；辅助联系；阅读层级 `abstract`。

## M38 近端方法与算子分裂

**直觉：** 把复杂目标拆成容易处理的数据项、先验与约束模块。

**数学模板：** prox_{λg}(v)=argmin_x g(x)+‖x−v‖²/(2λ)

**适用问题：** 非光滑正则、ADMM、展开网络、成像

**成立条件：** 各模块可解；收敛需凸性或另有非凸条件。

**失效边界：** 学到的去噪器不自动是某凸函数的近端映射。

**与相邻方法的区别：** 提供组合求解方式，与M11单纯写约束不同。

**框架文献：** [Proximal Algorithms](https://stanford.edu/~boyd/papers/prox_algs.html)

**本轮论文联系：**

- CVPR 2026 [Efficient Unrolled Networks for Large-Scale 3D Inverse Problems](https://cvpr.thecvf.com/virtual/2026/oral/40269)；主要联系；阅读层级 `abstract`。

## M39 不动点、隐式层与隐式微分

**直觉：** 直接定义收敛状态或优化解，而不固定展开层数。

**数学模板：** z*=f_θ(z*,x); dz*/dθ=(I−∂_z f)^{-1}∂_θf

**适用问题：** 隐式网络、可微求解器、双层优化

**成立条件：** 局部解存在，相关Jacobian可逆，数值求解精度足够。 f局部连续可微，选定解分支满足隐函数条件。

**失效边界：** 不动点不等于博弈纳什；常数激活存储不代表低总计算。

**与相邻方法的区别：** 数学固定点与M31策略均衡概念不同。

**框架文献：** [Deep Equilibrium Models](https://arxiv.org/abs/1909.01377)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M40 算子学习与函数空间建模

**直觉：** 学习从一个函数或场到另一个函数或场的映射。

**数学模板：** G_θ:a(·)↦u(·)

**适用问题：** PDE代理、跨网格场预测、科学模型

**成立条件：** 离散化与函数空间结构合理；训练分布覆盖目标函数。

**失效边界：** 共享参数跨网格不代表任意分辨率无误差。

**与相邻方法的区别：** 学一族问题的解映射，不是M27单个方程残差训练。

**框架文献：** [Neural Operator: Learning Maps Between Function Spaces](https://www.jmlr.org/beta/papers/v24/21-1524.html)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M41 谱方法与调和分析

**直觉：** 特征向量和频率分量揭示平滑结构、分区与多尺度变化。

**数学模板：** L=UΛUᵀ; g(L)x=Ug(Λ)Uᵀx

**适用问题：** 图聚类、滤波、分割、频率分析

**成立条件：** 图/算子反映有意义关系，注意谱间隙与重根。

**失效边界：** 特征向量符号和重根基不唯一；低频未必是语义。

**与相邻方法的区别：** 不是任意PCA降维；可与M16处理谱基对称性。

**框架文献：** [A Tutorial on Spectral Clustering](https://arxiv.org/abs/0711.0189)

**本轮论文联系：**

- ICLR 2023 [Sign and Basis Invariant Networks for Spectral Graph Representation Learning](https://iclr.cc/virtual/2023/events/oral)；辅助联系；阅读层级 `abstract`。
- ECCV 2026 [Heat Kernel Textures -- the Geodesic Gaussians That Do Not Splat](https://eccv.ecva.net/virtual/2026/oral/6124)；主要联系；阅读层级 `abstract`。

## M42 流形与黎曼几何

**直觉：** 状态生活在弯曲空间，距离和更新应沿该空间定义。

**数学模板：** x'=Retr_x(−η grad_M f(x))

**适用问题：** 旋转、正交矩阵、双曲嵌入、非线性几何

**成立条件：** 流形、度量与约束正确，注意全局拓扑与奇点。

**失效边界：** 投影可视化看着分开不证明真实几何；局部优化非全局最优。

**与相邻方法的区别：** 非线性几何区别于M23线性低秩，M36是统计流形特例。

**框架文献：** [Riemannian adaptive stochastic gradient algorithms](https://proceedings.mlr.press/v97/kasai19a.html)

**本轮论文联系：**

- ICLR 2024 [Flow Matching on General Geometries](https://iclr.cc/virtual/2024/oral/19740)；辅助联系；阅读层级 `abstract`。
- ICML 2024 [LSEnet: Lorentz Structural Entropy Neural Network for Deep Graph Clustering](https://icml.cc/virtual/2024/events/oral)；主要联系；阅读层级 `abstract`。
- ECCV 2022 [Pose-NDF: Modelling Human Pose Manifolds with Neural Distance Fields](https://eccv2022.ecva.net/program/accepted-papers/)；主要联系；阅读层级 `abstract`。
- ECCV 2026 [Heat Kernel Textures -- the Geodesic Gaussians That Do Not Splat](https://eccv.ecva.net/virtual/2026/oral/6124)；辅助联系；阅读层级 `abstract`。

## M43 拓扑数据分析与持久同调

**直觉：** 连接、环和孔洞等多尺度结构可补充点距离。

**数学模板：** L_top=d(Dgm(X),Dgm(Z)) [模板]

**适用问题：** 结构保持、形状、分割、表征

**成立条件：** 过滤函数、尺度及拓扑特征与任务相关。

**失效边界：** 持久特征不自动是语义；批内拓扑不代表总体拓扑。

**与相邻方法的区别：** 关注连通和洞，不等于M42的局部度量几何。

**框架文献：** [Topological Autoencoders](https://arxiv.org/abs/1906.00722)

**本轮论文联系：**

- CVPR 2025 [TopoCellGen: Generating Histopathology Cell Topology with a Diffusion Model](https://cvpr.thecvf.com/virtual/2025/oral/35356)；主要联系；阅读层级 `abstract`。

## M44 逆问题、正则化与数据一致性

**直觉：** 从不完整观测恢复潜在对象，需要测量模型与先验共同约束。

**数学模板：** min_x −log p(y|x)+λR(x)；白高斯噪声下对应平方残差

**适用问题：** 重建、去模糊、科学反演、扩散后验采样

**成立条件：** 测量过程、噪声和可识别性明确。

**失效边界：** 生成得真实不等于符合观测；病态问题通常不唯一。

**与相邻方法的区别：** 明确观测算子与恢复目标；M38可作为求解器。

**框架文献：** [Regularization of Inverse Problems by Neural Networks](https://arxiv.org/abs/2006.03972)

**本轮论文联系：**

- ICLR 2023 [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://iclr.cc/virtual/2023/events/oral)；主要联系；阅读层级 `abstract`。
- ICCV 2025 [Diffusion Image Prior](https://iccv.thecvf.com/virtual/2025/oral/2934)；辅助联系；阅读层级 `abstract`。
- CVPR 2026 [Efficient Unrolled Networks for Large-Scale 3D Inverse Problems](https://cvpr.thecvf.com/virtual/2026/oral/40269)；辅助联系；阅读层级 `abstract`。

## M45 连续概率流与流匹配

**直觉：** 学习把简单分布搬到数据分布的时间依赖速度场。

**数学模板：** dx_t/dt=v_θ(x_t,t); L=E‖v_θ(x_t,t)−u_t‖²

**适用问题：** 生成、分布转换、编辑

**成立条件：** 路径构造、端点分布和目标向量场一致。

**失效边界：** 逐点条件直线路径不自动等于边缘分布的最优传输。

**与相邻方法的区别：** 概率流速度不同于M26的score；基础论文身份不在此假定Oral。

**框架文献：** [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)

**本轮论文联系：**

- ICLR 2024 [Flow Matching on General Geometries](https://iclr.cc/virtual/2024/oral/19740)；主要联系；阅读层级 `abstract`。
- ICLR 2026 [GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models](https://iclr.cc/virtual/2026/oral/10006825)；主要联系；阅读层级 `abstract`。
- ICML 2025 [Temporal Difference Flows](https://icml.cc/virtual/2025/oral/47200)；主要联系；阅读层级 `abstract`。
- ICCV 2025 [FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](https://iccv.thecvf.com/virtual/2025/oral/2925)；主要联系；阅读层级 `abstract`。

## M46 Schrödinger桥与随机路径控制

**直觉：** 在匹配起终点分布时，让随机过程尽量接近参考动力学。

**数学模板：** min_Q KL(Q‖R), Q_0=μ, Q_T=ν

**适用问题：** 分布桥接、随机控制、条件生成

**成立条件：** 参考过程与端点约束可实现；路径KL良定义。

**失效边界：** 端点匹配不保证路径语义；有限迭代存在近似误差。

**与相邻方法的区别：** 在路径空间优化，相比M20静态耦合多了动力学。

**框架文献：** [Diffusion Schrödinger Bridge](https://arxiv.org/abs/2106.01357)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M47 GFlowNet与流守恒采样

**直觉：** 按奖励比例采样多样解，而非只追求单个最大值。

**数学模板：** 中间节点 Σin F=Σout F；源流量Z；终端流入R(x)；P(x)=R(x)/Z

**适用问题：** 分子、组合对象、探索、多模态候选

**成立条件：** 终态奖励非负、可达性与流平衡条件明确。 终端奖励可归一化：0<Z=Σ_xR(x)<∞。

**失效边界：** GFlowNet流守恒不等于M45连续速度流匹配；好奖励不等于科学有效。

**与相邻方法的区别：** 目标分布采样不同于标准最大期望奖励控制。

**框架文献：** [GFlowNet Foundations](https://arxiv.org/abs/2111.09266)

**本轮论文联系：**

- ICLR 2024 [Amortizing intractable inference in large language models](https://blog.iclr.cc/category/iclr-2024/)；主要联系；阅读层级 `abstract`。
- ICML 2023 [Learning GFlowNets From Partial Episodes For Improved Convergence And Stability](https://icml.cc/media/icml-2023/Slides/25580_Op4JkaX.pdf)；主要联系；阅读层级 `abstract`。

## M48 重要性采样与Monte Carlo方差控制

**直觉：** 改变抽样分布，把计算放到重要区域，同时用权重校正。

**数学模板：** E_p[f]=E_q[(p/q)f]

**适用问题：** 稀有事件、积分、训练抽样、离策略估计

**成立条件：** q覆盖目标支持，权重可计算并控制方差。

**失效边界：** 权重尾部大可能更差；裁剪和自归一化引入偏差。

**与相邻方法的区别：** M07改变获得的数据；这里校正抽样分布估计原目标。

**框架文献：** [Neural Importance Sampling](https://arxiv.org/abs/1808.03856)

**本轮论文联系：**

- ICLR 2023 [Flow Annealed Importance Sampling Bootstrap](https://iclr.cc/virtual/2023/events/oral)；主要联系；阅读层级 `abstract`。

## M49 知识蒸馏与特权信息迁移

**直觉：** 把昂贵或训练时可见的知识转成部署可用模型。

**数学模板：** min_θ E[KL(p_teacher(·|x)‖p_θ(·|x))]

**适用问题：** 压缩、跨模态监督、集成到单模型

**成立条件：** 教师信息可靠，学生输入足以支持目标。

**失效边界：** 教师错误会继承；训练时特权信息不能偷渡到测试。

**与相邻方法的区别：** 优化预测行为迁移，不等于M05描述长度；自蒸馏需说明信号来源。

**框架文献：** [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M50 正交估计、双重稳健与交叉拟合

**直觉：** 用机器学习估计辅助函数时，降低其误差对目标参数的一阶影响。

**数学模板：** E[ψ(W;θ₀,η₀)]=0；D_η E[ψ(W;θ₀,η₀)][h]=0 ∀h

**适用问题：** 处理效应、离策略评估、半参数推断

**成立条件：** 识别假设、重叠性、辅助估计速率与样本划分成立。

**失效边界：** 正交不自动双重稳健；交叉拟合不解决未测混杂。

**与相邻方法的区别：** M17负责识别，这里负责稳健统计估计；两者不可替代。

**框架文献：** [Double/debiased machine learning](https://academic.oup.com/ectj/article/21/1/C1/5056401)

本轮暂无对应的已核Oral实例；本条来自经典框架扩充。

## M51 进化搜索与质量多样性

**直觉：** 不仅找一个最高分解，还保留行为不同且各自优秀的一组解。

**数学模板：** A[b]←argmax_{θ:descriptor(θ)∈b} fitness(θ)

**适用问题：** 技能发现、黑箱优化、多样解生成

**成立条件：** 行为描述符和质量函数应对应实际需要。

**失效边界：** 行为格覆盖不等于语义多样性；探索成本需公平比较。

**与相邻方法的区别：** 区别于M12：多样性通常通过行为描述符分区，不一定是多目标Pareto前沿。

**框架文献：** [Neuroevolution is a Competitive Alternative to Reinforcement Learning for Skill Discovery](https://arxiv.org/abs/2210.03516)

**本轮论文联系：**

- ICLR 2023 [Neuroevolution is a Competitive Alternative to Reinforcement Learning for Skill Discovery](https://iclr.cc/virtual/2023/events/oral)；主要联系；阅读层级 `abstract`。

## M52 Markov生成元与概率演化

**直觉：** 直接描述分布怎样随时间演化，统一连续运动、扩散和离散跳跃。

**数学模板：** dE[f(X_t)]/dt=E[(L_t f)(X_t)]

**适用问题：** 离散与连续生成、混合状态空间

**成立条件：** 生成元定义合法过程；域、边界与非爆炸条件成立。

**失效边界：** 形式上的统一不保证数值求解稳定；不同过程不能共享所有路径假设。

**与相邻方法的区别：** M45是确定性流；M52允许扩散和跳跃等更一般过程。

**框架文献：** [Generator Matching: Generative modeling with arbitrary Markov processes](https://openreview.net/forum?id=RuP17cJtZo)

**本轮论文联系：**

- ICLR 2025 [Generator Matching: Generative modeling with arbitrary Markov processes](https://iclr.cc/virtual/2025/oral/31846)；主要联系；阅读层级 `abstract`。
- ICML 2025 [DeFoG: Discrete Flow Matching for Graph Generation](https://icml.cc/virtual/2025/events/oral)；主要联系；阅读层级 `abstract`。

## M53 凸松弛与半定规划提升

**直觉：** 先在包含原可行域的易解集合中求界，再恢复原问题候选解。

**数学模板：** min tr(CX), s.t. tr(A_iX)=b_i, X⪰0；松弛rank(X)=1

**适用问题：** 几何估计、离散优化、全局证书

**成立条件：** 松弛方向与原目标一致；紧性需单独证明。

**失效边界：** 有最优松弛解不等于原问题全局解；噪声和离群点可能破坏紧性。

**与相邻方法的区别：** M11处理约束及对偶；M53改变可行域取得可解近似和界。

**框架文献：** [Convex Relaxation for Robust Vanishing Point Estimation in Manhattan World](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_Convex_Relaxation_for_Robust_Vanishing_Point_Estimation_in_Manhattan_World_CVPR_2025_paper.html)

**本轮论文联系：**

- CVPR 2025 [Convex Relaxation for Robust Vanishing Point Estimation in Manhattan World](https://cvpr.thecvf.com/virtual/2025/oral/35342)；主要联系；阅读层级 `method_section`。

## M54 隐式正则与优化归纳偏置

**直觉：** 即使不显式加罚项，架构、初始化和优化轨迹也会偏向某些解。

**数学模板：** θ_{t+1}=θ_t−η∇L(θ_t), x̂=g_{θ_T}(z)

**适用问题：** 逆问题、过参数化学习、少样本拟合

**成立条件：** 比较时需固定数据、停止规则和优化配置。

**失效边界：** 早停可能利用验证信息；某结构有效不代表存在普适的显式正则等价。

**与相邻方法的区别：** M44定义逆问题；M54解释算法如何在多个拟合解中作选择，亦不同于M09序贯决策。

**框架文献：** [Diffusion Image Prior](https://iccv.thecvf.com/virtual/2025/oral/2934)

**本轮论文联系：**

- ICCV 2025 [Diffusion Image Prior](https://iccv.thecvf.com/virtual/2025/oral/2934)；主要联系；阅读层级 `abstract`。

## M55 可逆变换与归一化流

**直觉：** 把简单密度通过可逆映射变成复杂密度，同时追踪体积变化。

**数学模板：** log p_X(x)=log p_Z(f⁻¹(x))+log|det Df⁻¹(x)|

**适用问题：** 精确似然、可逆生成、密度估计

**成立条件：** 双射、维度和Jacobian可计算性符合模型设定。

**失效边界：** 可逆结构限制表达与计算；高似然不必然等于感知质量。

**与相邻方法的区别：** M45侧重学习连续速度场；M55侧重变量变换和密度可计算性，两者有交集。

**框架文献：** [MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2272.pdf)

**本轮论文联系：**

- ICLR 2023 [Flow Annealed Importance Sampling Bootstrap](https://iclr.cc/virtual/2023/events/oral)；辅助联系；阅读层级 `abstract`。
- ECCV 2026 [MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation](https://eccv.ecva.net/virtual/2026/oral/6128)；主要联系；阅读层级 `abstract`。

## M56 偏好学习与随机效用模型

**直觉：** 不用绝对分数，利用成对选择推断相对效用或直接学习策略。

**数学模板：** P(y_a≻y_b|x)=σ(r(x,y_a)−r(x,y_b))

**适用问题：** 人类偏好对齐、排序、相对评价

**成立条件：** 偏好模型、参考分布和数据覆盖需说明。

**失效边界：** 循环偏好、标注异质性和分布外数据可能违背单一效用模型。

**与相邻方法的区别：** M06使用效用决策；M56研究如何从比较中学习效用或其策略参数化。

**框架文献：** [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)

**本轮论文联系：**

- NeurIPS 2023 [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://neurips.cc/virtual/2023/oral/73865)；主要联系；阅读层级 `abstract`。

## M57 差分隐私与稳定随机机制

**直觉：** 限制单个样本参与与否对输出分布的影响。

**数学模板：** P[M(D)∈S]≤e^ε P[M(D′)∈S]+δ

**适用问题：** 隐私训练、自适应实验设计、敏感数据分析

**成立条件：** 相邻数据集、隐私预算和组合会计需明确。

**失效边界：** 加噪声不自动构成DP；隐私保证不等于数据安全或模型公平的全部。

**与相邻方法的区别：** 与M28泛化和M29覆盖保证针对不同对象。

**框架文献：** [Privacy Preserving Adaptive Experiment Design](https://arxiv.org/abs/2401.08224)

**本轮论文联系：**

- ICML 2024 [Privacy Preserving Adaptive Experiment Design](https://icml.cc/virtual/2024/oral/35582)；主要联系；阅读层级 `abstract`。

## M58 组合一致性与图团搜索

**直觉：** 把两两相容的候选建立图，通过组合结构挑出一致集合。

**数学模板：** 枚举C：C中节点两两相连，且不存在v∉C可加入后仍成团（极大团）；最大团另需max|C|

**适用问题：** 几何配准、匹配、离散结构选择

**成立条件：** 边的相容性应有实际几何或逻辑意义。

**失效边界：** 极大团不等于最大团；两两相容不总能保证全局正确。

**与相邻方法的区别：** 与M19消息传递不同；这里显式搜索离散组合结构。论文MAC枚举极大团，不应写成已求最大团。

**框架文献：** [3D Registration With Maximal Cliques](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_3D_Registration_With_Maximal_Cliques_CVPR_2023_paper.html)

**本轮论文联系：**

- CVPR 2023 [3D Registration With Maximal Cliques](https://media.icml.cc/Conferences/CVPR2023/CVPR_2023_MainConference_ProgramGuide.pdf)；主要联系；阅读层级 `abstract`。

## M59 Wasserstein梯度流与分布优化

**直觉：** 把整个概率分布视为优化变量，在能量下降与分布移动成本之间平衡。

**数学模板：** μ_{k+1}=argmin_μ F(μ)+W₂²(μ,μ_k)/(2τ)

**适用问题：** 分布动力学、数据集优化、能量反推

**成立条件：** 能量泛函、分布空间、边界与离散近似需明确。

**失效边界：** 分布轨迹不必唯一识别能量；数值近似不自动继承连续流性质。

**与相邻方法的区别：** M20求两个分布间的运输；M59定义沿时间下降能量的分布轨迹。

**框架文献：** [Learning diffusion at lightspeed](https://arxiv.org/abs/2406.12616)

**本轮论文联系：**

- NeurIPS 2024 [Learning diffusion at lightspeed](https://neurips.cc/media/neurips-2024/Slides/93047.pdf)；主要联系；阅读层级 `method_section`。
- ICML 2025 [Flowing Datasets with Wasserstein over Wasserstein Gradient Flows](https://icml.cc/virtual/2025/events/oral)；主要联系；阅读层级 `abstract`。

