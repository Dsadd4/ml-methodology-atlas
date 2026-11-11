# 论文方法卡与取证记录

模板是本项目提炼；实验建议不代表已经执行。abstract含摘要/介绍/讲者材料层筛选；method_section代表定位阅读过部分方法段，均不等同完整复现。

## SNUG: Self-Supervised Neural Dynamic Garments

CVPR 2022 · `vision-cvpr22-snug` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 Orals 6/22 PM 页面，2022-06-22 13:30–15:00，21b列名。

**方法族：** 变分力学与物理自监督

**直觉：** 将逐时刻隐式积分重写为优化问题，让物理能量承担监督信号，减少预先生成真值轨迹的需求。

**模板：** 框架示意：x_{t+1}=argmin_x [惯性能量(x,x_t,v_t)+势能(x)]，以该目标训练预测网络。

**前提：** 材料模型、边界条件和人体运动输入足够可信；训练状态覆盖测试动态。

**限制：** 物理先验有模型误差；低损失不等同真实服装材料准确。作者项目页有Eq9材料系数和Eq10弯曲能缩放勘误，复现须核对：https://mslab.es/projects/SNUG/

**方法段证据：** 已读官方摘要；未升级为方法节精读。

**映射：** M27。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://cvpr2022.thecvf.com/orals-622-pm) · [论文](https://openaccess.thecvf.com/content/CVPR2022/html/Santesteban_SNUG_Self-Supervised_Neural_Dynamic_Garments_CVPR_2022_paper.html)

[实际内容入口](https://openaccess.thecvf.com/content/CVPR2022/html/Santesteban_SNUG_Self-Supervised_Neural_Dynamic_Garments_CVPR_2022_paper.html)

## 3D Registration With Maximal Cliques

CVPR 2023 · `vision-cvpr23-mac` · `verified` · 阅读 `abstract`

**原展示类型：** Oral (Award candidate session)

**身份依据：** 官方 Program Guide 印刷p14/PDF第18页：2023-06-20 Oral-Award-Tue 15:10列名，Award candidate paper presentations。

**方法族：** 相容图、极大团与多假设共识

**直觉：** 最大团未必对应正确几何；枚举多个不可继续扩大的局部一致集合，从它们生成候选变换并验证。

**模板：** 框架示意：G=(V,E)，相容匹配为边；每个极大团C产生 SVD刚体解(R_C,t_C)，再按全局对应一致性选解。

**前提：** 匹配的几何相容性能有效区别内外点；候选团中存在正确共识。

**限制：** 极大团≠最大团；枚举数量最坏可指数增长；错误相容关系仍可组成团。

**方法段证据：** 已读官方摘要；未升级为方法节精读。

**映射：** M58。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://media.icml.cc/Conferences/CVPR2023/CVPR_2023_MainConference_ProgramGuide.pdf) · [论文](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_3D_Registration_With_Maximal_Cliques_CVPR_2023_paper.html)

[实际内容入口](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_3D_Registration_With_Maximal_Cliques_CVPR_2023_paper.html)

## Producing and Leveraging Online Map Uncertainty in Trajectory Prediction

CVPR 2024 · `vision-cvpr24-map` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** CVPR 2024 官方 Oral Papers 新闻页明确列名。

**方法族：** 层级概率建模与不确定性传播

**直觉：** 上游地图不确定时，把分布而非单点估计传给下游轨迹预测。

**模板：** 框架示意：p(τ|x)=∫p(τ|m,x)p(m|x)dm；积分可近似，非原文公式复刻。

**前提：** 地图不确定性表征可靠；下游会利用其信息而非忽略。

**限制：** 校准误差会传播；平均预测质量不构成自动驾驶安全保证。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M01。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://cvpr.thecvf.com/Conferences/2024/News/Oral_Papers) · [论文](https://arxiv.org/abs/2403.16439)

[实际内容入口](https://arxiv.org/abs/2403.16439)

## Convex Relaxation for Robust Vanishing Point Estimation in Manhattan World

CVPR 2025 · `vision-cvpr25-convex` · `verified` · 阅读 `method_section`

**原展示类型：** Oral

**身份依据：** 官方 /virtual/2025/events/oral 列表的同名 oral event。

**方法族：** 凸松弛与半正定提升

**直觉：** 把离散关联与几何求解难题转成QCQP，再放松为可解的凸问题。

**模板：** §3.3 Eq(4)–(7)：min xᵀCx s.t. xᵀA_i x=b_i；令X=xxᵀ，保留tr(A_i X)=b_i、X≽0，删除rank(X)=1。论文§4.2将VP联合关联提升为具体Full SDP，§4.3使用逐方向Single Block SDP。

**前提：** Manhattan三方向与相机内参条件适用；逐方向最大内点识别依赖论文的distinguishability假设，单块紧性证明采用无噪声无离群条件。

**限制：** 不能把理想条件下紧性证明外推为任意噪声/离群的保证；随机采样和顺序去除内点影响实际全局行为；SDP规模成本仍存在。

**方法段证据：** §3.3 Eq(4)–(7)：QCQP经X=xxᵀ提升并去掉rank=1为SDP。§4.1 Primal Problem：Q为每列one-hot，三方向单位正交，外点截断c²。§4.2 Eq(8)–(12)给Full QCQP/SDP；§4.3.1 Eq(13)–(14)与Single Block SDP逐方向求解。§4.3.1 Remark明确需distinguishability，且单块紧性证明限noise-free/outlier-free；§4.3.2再正交精化，规模大时随机采样线。

**映射：** M53。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://cvpr.thecvf.com/virtual/2025/oral/35342) · [论文](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_Convex_Relaxation_for_Robust_Vanishing_Point_Estimation_in_Manhattan_World_CVPR_2025_paper.html)

[实际内容入口](https://arxiv.org/html/2505.04788v1)

## TopoCellGen: Generating Histopathology Cell Topology with a Diffusion Model

CVPR 2025 · `vision-cvpr25-topocell` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方同名oral event 35356，独立审核HTTP200；官方slides另明确标注Oral Presentation。

**方法族：** 拓扑约束与结构感知生成评估

**直觉：** 生成细胞布局时约束空间结构，并用 TopoFD 评估结构差异，弥补仅看外观的不足。

**模板：** 框架示意：L=Ldiff+λLtopology；通过拓扑特征分布比较生成布局与真实布局。

**前提：** 拓扑特征捕捉任务相关结构，细胞类型及布局标注可信。

**限制：** 结构相似不是生物机制证明；Topological FID 也受样本量和特征选择影响。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M43, M26。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://cvpr.thecvf.com/virtual/2025/oral/35356) · [论文](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_TopoCellGen_Generating_Histopathology_Cell_Topology_with_a_Diffusion_Model_CVPR_2025_paper.html)

[实际内容入口](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_TopoCellGen_Generating_Histopathology_Cell_Topology_with_a_Diffusion_Model_CVPR_2025_paper.html)

## Differentiable Vector Quantization for Rate-Distortion Optimization of Generative Image Compression

CVPR 2026 · `vision-cvpr26-rdvq` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 oral event 40298，含摘要和 CVF Paper PDF 链接。

**方法族：** 率失真理论与离散变量软松弛

**直觉：** 用距离相关软码字后验连接离散量化与熵模型，让编码器能收到码率目标的梯度。

**模板：** 摘要机制示意：q(k|z)∝exp(−d(z,c_k)/T)，R≈−Σ_k q(k|z)log pφ(k|context)，L=R+λD；核函数形式为示意。

**前提：** 软后验能近似实际码字选择；熵模型与传输协议一致。

**限制：** 可微率代理不自动等于真实比特数；感知质量与像素保真存在权衡。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M04。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://cvpr.thecvf.com/virtual/2026/oral/40298) · [论文](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Differentiable_Vector_Quantization_for_Rate-Distortion_Optimization_of_Generative_Image_Compression_CVPR_2026_paper.html)

[实际内容入口](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Differentiable_Vector_Quantization_for_Rate-Distortion_Optimization_of_Generative_Image_Compression_CVPR_2026_paper.html)

## Efficient Unrolled Networks for Large-Scale 3D Inverse Problems

CVPR 2026 · `vision-cvpr26-unroll` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 oral event 40269，含摘要和 CVF Paper PDF 链接。

**方法族：** 算法展开、算子近似与区域分解

**直觉：** 把物理成像算子嵌入网络，用区域划分和正规算子近似缓解3D问题的显存瓶颈。

**模板：** 通用展开示意：x_{k+1}=Dθk(x_k−η_k A* (Ax_k−y))；论文关键是域划分和 A*A 近似，非该式本身。

**前提：** 前向算子已知且近似误差可控；分区能保持全局物理耦合的重要部分。

**限制：** 近似引入偏差；可扩展性与重建保真度需逐算子验证。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M38, M44。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://cvpr.thecvf.com/virtual/2026/oral/40269) · [论文](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html)

[实际内容入口](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html)

## PACTran: PAC-Bayesian Metrics for Estimating the Transferability of Pretrained Models to Classification Tasks

ECCV 2022 · `vision-eccv22-pactran` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 Oral papers 表，ID 6568。

**方法族：** PAC-Bayes泛化界与模型选择

**直觉：** 预训练模型选择可用风险与后验复杂度折中，不必为每个候选完整微调。

**模板：** 框架示意：min_Q Rhat(Q)+Complexity(KL(Q||P),n,δ)；具体界及常数需按原文实例。

**前提：** 界所需采样、先验和后验条件成立；代理任务与实际微调目标相符。

**限制：** 代理得分排名不保证任意微调方案的排序；界有时宽松。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M28。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://eccv2022.ecva.net/program/accepted-papers/) · [论文](https://arxiv.org/abs/2203.05126)

[实际内容入口](https://arxiv.org/abs/2203.05126)

## Pose-NDF: Modelling Human Pose Manifolds with Neural Distance Fields

ECCV 2022 · `vision-eccv22-pose` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 accepted-papers 第一张表 Oral papers，ID 1413；第二张表是 Poster，不混入。

**方法族：** 流形约束与隐式距离场

**直觉：** 先学习有效解集合的几何，再把不合理预测投影回集合；可迁移到满足结构约束的连续预测。

**模板：** 框架示意：M={q∈SO(3)^K:fθ(q)=0}；沿流形梯度降低 fθ 并保持旋转约束。

**前提：** 训练姿态覆盖目标有效姿态；学习的距离能反映几何邻近。

**限制：** 分布外姿态可能被错误投影；非凸投影不保证全局最近解。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M42。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://eccv2022.ecva.net/program/accepted-papers/) · [论文](https://arxiv.org/abs/2207.13807)

[实际内容入口](https://arxiv.org/abs/2207.13807)

## Learning Topological Interactions for Multi-Class Medical Image Segmentation

ECCV 2022 · `vision-eccv22-topology` · `verified` · 阅读 `method_section`

**原展示类型：** Oral

**身份依据：** 官方 Oral papers 表，ID 6180；arXiv comment 亦注明 Oral。

**方法族：** 拓扑与多对象关系约束

**直觉：** 像素预测正确率不等于结构正确；把类别之间包含、排斥等关系变成训练约束。

**模板：** 原文§3.2 Eq(3)–(4)：Lti=Lpixel(f⊙V,g⊙V)，Ltotal=Lce+λdice Ldice+λti Lti；V由§3.1的邻域卷积与禁止标签对生成。

**前提：** 解剖类别关系可可靠定义，标签与关系先验一致。

**限制：** 约束依赖离散邻域定义、类别关系和标注；损失惩罚不是推理时硬可行性保证，也不保证所有连通性/洞数量正确。

**方法段证据：** §3.1，pp6–8：Eq(1)卷积求邻域，Eq(2)找违反禁止邻接的critical pixel集合；§3.2，p9：Eq(3) Lti=Lpixel(f⊙V,g⊙V)，Eq(4) Ltotal=Lce+λdice Ldice+λti Lti。包含关系通过禁止内部类接触包围类之外的标签编码；邻域由数字拓扑connectivity kernel决定。这里约束的是特定包含/排斥关系，非一般持久同调或所有Betti数。

**映射：** M19。局部类别包含/排斥的结构约束，仅与M19相关；不证明采用概率因子图、消息传递或持久同调。

[官方身份来源](https://eccv2022.ecva.net/program/accepted-papers/) · [论文](https://arxiv.org/abs/2207.09654)

[实际内容入口](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136890691.pdf)

## RACE: Robust Adversarial Concept Erasure for Secure Text-to-Image Diffusion Model

ECCV 2024 · `vision-eccv24-race` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 独立复核官方Oral总表，同名R.A.C.E.条目链接至oral/2342。

**方法族：** 对抗鲁棒优化与知识移除

**直觉：** 移除概念不能只看常规提示；主动寻找仍触发该概念的输入，再训练抵御。

**模板：** 框架示意：minθ max_{δ∈Δ} Lerase(θ,e+δ)+λLretain(θ)；精确损失需查原文。

**前提：** 文本嵌入攻击集合代表真实风险；保留概念集合定义清楚。

**限制：** 有限嵌入攻击不等于全提示空间的彻底移除；保留能力存在权衡。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M13。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://eccv.ecva.net/virtual/2024/oral/2342) · [论文](https://arxiv.org/abs/2405.16341)

[实际内容入口](https://arxiv.org/abs/2405.16341)

## Heat Kernel Textures -- the Geodesic Gaussians That Do Not Splat

ECCV 2026 · `vision-eccv26-heat` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 oral event 6124，含摘要和官方论文 PDF 链接。

**方法族：** 黎曼几何、热核与内蕴表示

**直觉：** 在物体表面直接定义各向异性热核，避免将曲面纹理强行展开到二维UV坐标。

**模板：** 基础框架：∂t u=−Δ_M u，H_t=exp(−tΔ_M)；论文使用离散曲面上的各向异性核。

**前提：** 三角网格合理表示流形表面；离散几何算子稳定。

**限制：** 网格质量和离散近似影响纹理；方法针对表面表示，不是通用生成保证。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M41, M42。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://eccv.ecva.net/virtual/2026/oral/6124) · [论文](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2392.pdf)

[实际内容入口](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2392.pdf)

## MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation

ECCV 2026 · `vision-eccv26-mimflow` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 oral event 6128，含摘要和官方论文 PDF 链接。

**方法族：** 变量变换、可逆模型与语义分解

**直觉：** 让流模型集中拟合语义潜变量，解码器负责高频细节，减少可逆建模在像素细节上的容量消耗。

**模板：** NF基础：log p_X(x)=log p_Z(f(x))+log|det J_f(x)|；VAE/解码器组成的完整混合模型不因此自动具有精确边缘似然。

**前提：** NF部分可逆且Jacobian可计算；语义与细节分工能够学习。

**限制：** 潜变量信息丢失和重建目标会影响生成；NF精确密度属性不能直接推广到整体。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M55。归一化流用于模型组件；潜变量与解码器混合结构不自动具有精确整体边缘似然。

[官方身份来源](https://eccv.ecva.net/virtual/2026/oral/6128) · [论文](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2272.pdf)

[实际内容入口](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2272.pdf)

## Robust Evaluation of Diffusion-Based Adversarial Purification

ICCV 2023 · `vision-iccv23-purification` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 独立复核官方program：ID11381在Wednesday 4th 09:30–10:30 Orals。

**方法族：** 随机系统的自适应鲁棒评估

**直觉：** 防御内部有随机性和迭代求解时，攻击必须穿过实际管线；梯度难求不能当成鲁棒性。

**模板：** 框架示意：max_{δ∈Δ} Eξ[ℓ(f(Pξ(x+δ)),y)]；用可用的代理梯度逼近迭代净化过程。

**前提：** 威胁集明确；攻击能近似随机净化管线，采样与迭代预算足够。

**限制：** 有限攻击只给风险下界，不是鲁棒性认证；代理梯度仍可能漏攻。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M13, M26。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iccv2023.thecvf.com/main.conference.program-107.php) · [论文](https://arxiv.org/abs/2303.09051)

[实际内容入口](https://arxiv.org/abs/2303.09051)

## Diffusion Image Prior

ICCV 2025 · `vision-iccv25-diip` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 oral event 2934，含同名摘要。

**方法族：** 隐式正则化与早停

**直觉：** 优化过程可能先拟合真实结构、后拟合退化伪影；利用时间顺序作为先验。

**模板：** 框架示意：x_t=Optimize_t(prior,y)，在拟合噪声前选择 t_stop；不是决策论最优停止定理。

**前提：** 拟合结构与伪影的时间可分；有实际可用的停止准则。

**限制：** 未知退化与停止选择影响可信度；生成先验可能引入不真实细节。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M54, M44。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iccv.thecvf.com/virtual/2025/oral/2934) · [论文](https://iccv.thecvf.com/virtual/2025/oral/2934)

[实际内容入口](https://iccv.thecvf.com/virtual/2025/oral/2934)

## FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models

ICCV 2025 · `vision-iccv25-flowedit` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 oral event 2925，含同名摘要。

**方法族：** 连续流与分布间输运

**直觉：** 直接构造连接源提示与目标提示分布的ODE，用路径设计控制编辑，不必先反演为噪声。

**模板：** 框架示意：dx/dt=v(x,t;csrc,ctgt)；具体 FlowEdit 速度构造需读方法节，不等同一般条件流。

**前提：** 预训练流模型准确表达目标条件分布；源图与条件有合理对应。

**限制：** 较低输运成本不等于严格最优输运；内容保留和复杂编辑仍需实验检查。

**方法段证据：** 已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

**映射：** M45。生成流为主要联系；运输相关目标不自动等于严格最优传输，未作为M20实证。

[官方身份来源](https://iccv.thecvf.com/virtual/2025/oral/2925) · [论文](https://iccv.thecvf.com/virtual/2025/oral/2925)

[实际内容入口](https://iccv.thecvf.com/virtual/2025/oral/2925)

## Frame Averaging for Invariant and Equivariant Network Design

ICLR 2022 · `iclr2022-frame-averaging` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 Oral 总表链接至单篇 event 6190；HTTP200 全文标题含同名论文与 ICLR Oral，正文 2022 Oral。

**方法族：** 群平均与等变性

**直觉：** 同一对象换坐标后含义不变；把少量合法参考系下的预测合并，获得结构性不变或等变。

**模板：** 方法论模板：F(x)=|G|^{-1}∑_{g∈G}g·f(g^{-1}·x)；论文用等变有限 frame 替代全群。

**前提：** 群作用已知；frame 的选择本身满足等变性。

**限制：** 连续群不能直接有限求和；退化结构与 frame 稳定性需要专门处理。

**映射：** M16。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2022/oral/6190) · [论文](https://arxiv.org/abs/2110.03336)

## Diffusion Posterior Sampling for General Noisy Inverse Problems

ICLR 2023 · `iclr2023-dps` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 2023 Oral 总表的同名条目直接标注 Oral。

**方法族：** 贝叶斯逆问题与软数据一致性

**直觉：** 观测含噪时，不能把输出强行投影到观测；用生成先验与噪声似然共同解释数据。

**模板：** 方法论模板：p(x|y)∝p(y|x)p(x)，y=A(x)+ε；后验 score=先验 score+似然 score。

**前提：** 前向模型及噪声似然足够准确；已有适合目标分布的生成先验。

**限制：** DPS 使用后验近似，不能声称精确后验采样；错误先验可能产生可信但错误结构。

**映射：** M44, M26。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2023/events/oral) · [论文](https://arxiv.org/abs/2209.14687)

## Flow Annealed Importance Sampling Bootstrap

ICLR 2023 · `iclr2023-fab` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 2023 Oral 总表的同名条目直接标注 Oral。

**方法族：** 重要性采样与退火蒙特卡洛

**直觉：** 没有真实样本但能算未归一化密度时，用可学习提议分布加退火链寻找被遗漏的概率质量。

**模板：** 方法论模板：w(x)=p̃(x)/qθ(x)；以 α=2 散度降低重要性权重方差。

**前提：** 目标密度可计算；提议分布覆盖目标支撑；相关矩存在。

**限制：** 覆盖不足会导致极端权重；自归一化比率估计一般不能直接称有限样本无偏。

**映射：** M48, M55。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2023/events/oral) · [论文](https://arxiv.org/abs/2208.01893)

## Neural Optimal Transport

ICLR 2023 · `iclr2023-not` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 2023 Oral 总表的同名条目直接标注 Oral。

**方法族：** 最优传输的随机计划

**直觉：** 无配对两域数据的对应关系可作为耦合分布求解，而非强迫每个输入只有一个输出。

**模板：** 通用 OT 模板：min_{π∈Π(μ,ν)} Eπ[c(x,y)]；论文还研究 weak transport costs。

**前提：** 代价应对应任务语义；边缘分布约束合理。

**限制：** 匹配分布不自动保证语义或因果对应；上述简单公式不等同论文全部弱代价形式。

**映射：** M20。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2023/events/oral) · [论文](https://arxiv.org/abs/2201.12220)

## Neuroevolution is a Competitive Alternative to Reinforcement Learning for Skill Discovery

ICLR 2023 · `iclr2023-quality-diversity` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 2023 Oral 总表的同名条目直接标注 Oral。

**方法族：** 进化搜索与质量多样性

**直觉：** 保留每类行为中表现好的解，形成可组合技能库；单个最大回报解并不代表可迁移能力。

**模板：** 方法论模板：archive[b]←argmax_{θ:descriptor(θ)∈b} R(θ)。

**前提：** 行为描述符与分桶能表达有用差异；环境可重复评价。

**限制：** 质量与覆盖依赖描述符；论文比较多算法而非证明 QD 在所有任务优于 RL。

**映射：** M51。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2023/events/oral) · [论文](https://arxiv.org/abs/2210.03516)

## Sign and Basis Invariant Networks for Spectral Graph Representation Learning

ICLR 2023 · `iclr2023-sign-basis` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 2023 Oral 总表的同名条目直接标注 Oral。

**方法族：** 谱方法与特征空间商对称性

**直觉：** 特征向量是坐标选择，不是唯一物理对象；学习应忽略正负号和重根子空间的基变换。

**模板：** 方法论模板：L=UΛUᵀ；同一特征子空间内 f(UQ)=f(U), QᵀQ=I。

**前提：** 已知谱算子和等价变换群；区分单根与重根。

**限制：** 只处理符号不足以处理重根；计算特征分解及谱扰动稳定性另需评估。

**映射：** M16, M41。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2023/events/oral) · [论文](https://arxiv.org/abs/2202.13013)

## Amortizing intractable inference in large language models

ICLR 2024 · `iclr2024-gflownet-inference` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** ICLR 官方 2024 博客将同名论文链接至 /virtual/2024/oral/19763。

**方法族：** GFlowNet与流守恒采样

**直觉：** 有多个好解释或推理路径时，学习按奖励成比例抽样，比只寻找单个最高奖励解更能保留多样性。

**模板：** 通用 GFlowNet 模板：终端 Pθ(z)=R(z)/Z；中间状态流入总量=流出总量。

**前提：** 非负可评估奖励；生成轨迹的状态结构可定义。

**限制：** 奖励错设会采到错误解释；训练近似不保证精确贝叶斯后验。

**映射：** M47。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://blog.iclr.cc/category/iclr-2024/) · [论文](https://arxiv.org/abs/2310.04363)

## Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization

ICLR 2024 · `iclr2024-nash` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方会议 Oral 页面列出同名论文并标注 2024 Oral。

**方法族：** 博弈论与近似均衡

**直觉：** 多个决策者互相影响时，稳定解要求任何一方单独改变策略都无法明显获益。

**模板：** 通用定义：ε(π)=max_i[max_{π′ᵢ}uᵢ(π′ᵢ,π₋ᵢ)−uᵢ(π)]；求 ε≤δ。论文另外构造可无偏 Monte Carlo 估计的损失。

**前提：** 有限标准式博弈；效用估计与策略空间可访问。

**限制：** 非凸局部驻点不能自动当全局均衡；本模板不是论文无偏损失的原式。

**映射：** M31。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2024/oral/19744) · [论文](https://openreview.net/forum?id=cc8h3I3V4E)

## Flow Matching on General Geometries

ICLR 2024 · `iclr2024-riemannian-flow` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方会议 Oral 页面列出同名论文并标注 2024 Oral。

**方法族：** 黎曼几何与流形上的流匹配

**直觉：** 数据受曲面或几何约束时，速度、距离和移动方向都应在对应流形上定义。

**模板：** 方法论模板：minθ E||vθ(x,t)−u_t(x|x₁)||²_g；dx/dt=vθ(x,t)∈T_xM。

**前提：** 流形、度量或 premetric 可获得；目标向量场可构造。

**限制：** 简单几何可免模拟不代表任意网格都无计算开销；几何设错会造成偏差。

**映射：** M45, M42。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2024/oral/19740) · [论文](https://openreview.net/forum?id=g7ohDlTITL)

## Robust agents learn causal world models

ICLR 2024 · `iclr2024-robust-causal` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** ICLR 官方 2024 博客将同名论文链接至 /virtual/2024/oral/19724。

**方法族：** 鲁棒决策与因果模型可识别性

**直觉：** 若要求策略在足够丰富的环境变化下仍近似最优，策略必须携带足够因果信息。

**模板：** 概念模板：sup_{e∈E}Regret_e(π)≤δ ⇒ 在论文条件下可从策略恢复近似因果模型。

**前提：** 环境变化族足够丰富；满足论文决策和因果模型假设。

**限制：** 不能从普通 OOD 得分直接推出模型已学到可解释因果图。

**映射：** M17, M13。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://blog.iclr.cc/category/iclr-2024/) · [论文](https://arxiv.org/abs/2402.10877)

## Generator Matching: Generative modeling with arbitrary Markov processes

ICLR 2025 · `iclr2025-generator-matching` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方页面经 requests HTTP 200 读取，正文明确标注 2025 Oral 并列出同名论文。

**方法族：** 马尔可夫生成元与算子建模

**直觉：** 将连续运动、扩散、离散跳转都视为无穷小演化算子，便可在同一框架设计生成过程。

**模板：** 通用定义：L_t f(x)=lim_{h→0}(E[f(X_{t+h})|X_t=x]−f(x))/h；∂_t p=L_t* p。

**前提：** 过程、定义域及生成元满足相应正则条件；条件生成元可构造。

**限制：** 统一表达不代表任意生成元容易训练或模拟；数值误差需单独验证。

**映射：** M52。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2025/oral/31846) · [论文](https://openreview.net/forum?id=RuP17cJtZo)

## GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models

ICLR 2026 · `iclr2026-glass` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方 2026 Oral 总表链接至单篇 event 10006825；HTTP200 全文标题含同名论文与 ICLR Oral。

**方法族：** 充分统计量与随机转移重参数化

**直觉：** 把采样的随机性压缩为高斯潜在统计量，通过已有流模型的确定性演化实现可分支采样与奖励引导。

**模板：** 概念模板：ε∼N(0,I)，x′=Φ_{x,t,t′}(ε)；具体充分性由论文构造保证。

**前提：** 采用论文规定的预训练流及路径构造；数值积分和向量场精度足够。

**限制：** 并非任意转移核都可直接套同一构造；奖励偏差仍会影响对齐结果。

**映射：** M45。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://iclr.cc/virtual/2026/oral/10006825) · [论文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ad6ac52e02e14e0f2ddc0d4587ab47f1-Abstract-Conference.html)

## Bayesian Model Selection, the Marginal Likelihood, and Generalization

ICML 2022 · `icml2022-bayesian-selection` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 首页：ICML 2022, long oral presentation

**方法族：** 贝叶斯模型选择；条件边际似然

**直觉：** 选先验科学假说和预测训练后模型泛化是两个问题；条件边际似然先用部分数据形成后验，再评价剩余数据。

**模板：** 概念模板：log p(D_rest | D_prefix)=log ∫ p(D_rest|θ)p(θ|D_prefix)dθ

**前提：** 数据拆分与预测目标一致；后验近似质量可接受。

**限制：** 边际似然大不保证训练后泛化好；条件版本也受划分、先验与近似误差影响。

**可证伪实验建议：** 改变先验尺度和训练子集比例，比较边际似然/条件边际似然与独立测试似然的排序一致性。

**映射：** M01。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/media/icml-2022/Slides/17992.pdf) · [论文](https://arxiv.org/abs/2202.11678)

## JAWS-X: Addressing Efficiency Bottlenecks of Conformal Prediction Under Standard and Feedback Covariate Shift

ICML 2023 · `icml2023-jawsx` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方JSON id25430：decision=Accept (Oral & Poster)；virtualsite_url=/virtual/2023/oral/25430

**方法族：** 分布偏移下保形预测；近似影响函数

**直觉：** 把随预测器反馈而变化的数据分布纳入置信区间设计，同时处理重复拟合的计算成本。

**模板：** 框架模板：用目标/训练分布密度比加权校准分数；以近似更新减轻逐样本重拟合。非原文完整算法

**前提：** 密度比、支持集与反馈机制需满足论文保证所用假设；近似误差须另验。

**限制：** 不能把协变量偏移保证推广到任意概念漂移，也不能把近似算法自动视为精确有限样本保证。

**可证伪实验建议：** 并列报告目标域覆盖率、区间宽度、运行时；分别改变密度比误差和反馈强度。

**映射：** M29。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/static/virtual/data/icml-2023-orals-posters.json) · [论文](https://proceedings.mlr.press/v202/prinster23a.html)

## Learning GFlowNets From Partial Episodes For Improved Convergence And Stability

ICML 2023 · `icml2023-subtb` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方托管PDF标题：ICML 2023 ORAL FINAL

**方法族：** 概率流守恒；GFlowNet；偏差方差权衡

**直觉：** 生成候选的目标是按非归一化奖励成比例采样，用不同长度子轨迹的流平衡连接局部与整轨迹训练。

**模板：** 框架模板：P_terminal(x)∝R(x)；SubTB(λ)加权不同长度子轨迹的前后向流平衡残差

**前提：** 有向无环生成过程；足够表达能力、采样支持与优化收敛条件。

**限制：** 目标是多样性采样而非只找最大奖励；低平衡损失的意义依赖覆盖，奖励模型也可能错。

**可证伪实验建议：** 在可枚举空间测总变差和模式覆盖，再增大序列长度/奖励稀疏度；比较梯度方差与收敛。

**映射：** M47。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/media/icml-2023/Slides/25580_Op4JkaX.pdf) · [论文](https://proceedings.mlr.press/v202/madan23a.html)

## Emergent Equivariance in Deep Ensembles

ICML 2024 · `icml2024-emergent-equivariance` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方Oral列表包含该题；对应oral/35462

**方法族：** 对称性；群平均；神经切线核

**直觉：** 即使个体预测器不等变，充分增强后的集成预测也可在理论极限中出现等变性。

**模板：** 框架模板：f̄(x)=E_init[fθ(x)]；检验 f̄(gx)=ρ(g)f̄(x)

**前提：** 无限宽理论、初始化分布与完整数据增强条件；实际集成用有限Monte Carlo近似。

**限制：** 有限宽、有限成员数、连续群有限采样都会破坏精确等变；不等于所有域外预测正确。

**可证伪实验建议：** 扫描宽度、集成规模和群采样密度，测域内/域外等变误差，同时报告任务误差。

**映射：** M16。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2024/events/oral) · [论文](https://arxiv.org/abs/2403.03103)

## LSEnet: Lorentz Structural Entropy Neural Network for Deep Graph Clustering

ICML 2024 · `icml2024-lsenet` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方Oral列表包含该题；对应oral/35538

**方法族：** 双曲几何；结构熵；层次划分

**直觉：** 树状数据的表示空间与层次结构匹配，并以可微结构信息目标学习划分，减少预指定簇数的依赖。

**模板：** 框架模板：min_T DSI(G,T)；表示h_i位于Lorentz双曲流形。具体DSI定义需全文细读

**前提：** 图连边与属性反映待发现层次；曲率和树构造具有合理归纳偏置。

**限制：** 无需输入簇数不代表无需模型选择；噪声图或无层次数据可能不适合双曲结构。

**可证伪实验建议：** 比较树状/平坦/随机图，控制参数和簇数信息，分别消融几何与结构熵。

**映射：** M42。Lorentz几何为主要联系；最小结构熵不等同最大熵，因此不映射M03。

[官方身份来源](https://icml.cc/virtual/2024/events/oral) · [论文](https://arxiv.org/abs/2405.11801)

## Privacy Preserving Adaptive Experiment Design

ICML 2024 · `icml2024-private-design` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 页面标注：2024 Oral

**方法族：** 差分隐私；情境bandit；实验设计

**直觉：** 实验分配同时追求估计精度、累计收益和隐私，用Pareto边界说明不能只看某一个分数。

**模板：** 框架模板：min (Regret_T, Var(τ̂)) subject to (ε,δ)-DP

**前提：** 明确数据邻接、隐私预算、情境和处理效应模型；渐近推断需相应条件。

**限制：** 论文特定条件下隐私代价小，不代表任意样本规模或群体隐私都免费。

**可证伪实验建议：** 同时扫描ε、样本量与稀有子群比例，报告CATE误差/覆盖、regret及隐私会计。

**映射：** M57, M07。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2024/oral/35582) · [论文](https://arxiv.org/abs/2401.08224)

## Rate-Optimal Policy Optimization for Linear Markov Decision Processes

ICML 2024 · `icml2024-rate-policy` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方Oral列表包含该题；对应oral/35519

**方法族：** 在线遗憾；自然梯度与镜像下降

**直觉：** 以乐观价值估计驱动策略更新，配合无奖励预热与bonus更新节奏控制探索代价。

**模板：** 框架：Regret_K=Σ_k V_k(π_k)−min_πΣ_k V_k(π)；论文得到对K的Õ(√K)速率

**前提：** 线性MDP；随机损失+bandit反馈，或对抗损失+全信息反馈，须区分。

**限制：** 理论速率不能直接转给任意神经网络MDP；维数、时域与预热代价也需要计入。

**可证伪实验建议：** 分别比较两种反馈设定，改变线性特征失配，报告累计regret而非只看最终回报。

**映射：** M33, M36, M37。在线遗憾与自然梯度/镜像下降；完整线性MDP不当作简单Bandit。

[官方身份来源](https://icml.cc/virtual/2024/events/oral) · [论文](https://proceedings.mlr.press/v235/sherman24a.html)

## DeFoG: Discrete Flow Matching for Graph Generation

ICML 2025 · `icml2025-defog` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方Oral列表包含该题；官方作者代码链接oral/47238

**方法族：** 离散流匹配；连续时间Markov链

**直觉：** 离散图的概率质量通过跳变率演化，训练路径与采样器设计可以分开，同时尊重节点置换。

**模板：** 框架模板：d p_t/dt=p_t Q_t；Q_t为连续时间Markov跳变生成元

**前提：** 合法速率矩阵、图置换性质和目标概率路径；理论对真实分布复制有模型准确性条件。

**限制：** 有限步采样、速率估计和图有效性约束都可能产生偏差。

**可证伪实验建议：** 固定同一训练模型改采样器，比较分布距离、图有效性、步数/时间；置换输入检验一致性。

**映射：** M52。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2025/events/oral) · [论文](https://arxiv.org/abs/2410.04263)

## Hierarchical Refinement: Optimal Transport to Infinity and Beyond

ICML 2025 · `icml2025-hierarchical-ot` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 页面标注：2025 Oral

**方法族：** 最优传输；层次分治

**直觉：** 先用低秩传输发现应一起匹配的簇，再递归细分至一一指派，把巨型匹配转为分层子问题。

**模板：** 概念模板：low-rank coupling → paired partitions → recursive child assignment

**前提：** 赋值/双射设定；理论所需低秩子问题解与分组性质成立。

**限制：** 近似子问题与错误粗分可能传播误差；不能把赋值保证推广到所有OT变体。

**可证伪实验建议：** 在可精确求解的小规模上核对代价差，再逐步扩大规模，同时测内存、时间和层级误差。

**映射：** M20。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2025/oral/47248) · [论文](https://arxiv.org/abs/2503.03025)

## Inductive Moment Matching

ICML 2025 · `icml2025-imm` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方Oral列表包含该题；对应oral/47188

**方法族：** 分布矩匹配；归纳自蒸馏

**直觉：** 用分布层面的匹配构造少步生成训练，避免把每个样本路径一致性当作唯一目标。

**模板：** 概念模板：minθ D_moment(Pθ,Q_teacher(θ))；原始MMSD构造和梯度需进一步读全文

**前提：** 所选矩/核需足以区分分布；归纳训练和理论收敛要求成立。

**限制：** 分布层面理论不等于有限神经网络的训练必收敛；少步质量须同预算核验。

**可证伪实验建议：** 固定模型与训练预算，扫描采样步数，分别报告分布指标、模式覆盖和训练稳定性。

**映射：** M21。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2025/events/oral) · [论文](https://arxiv.org/abs/2503.07565)

## Temporal Difference Flows

ICML 2025 · `icml2025-td-flow` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 页面标注：2025 Oral

**方法族：** Bellman分布固定点；流匹配

**直觉：** 直接学习随机几何时域的未来状态分布，利用概率路径上的Bellman关系训练，避免预测时逐步展开误差。

**模板：** 概念模板：未来分布M=(1−γ)P+γPM；概率路径的对应Bellman方程连接flow matching。此式是框架示意

**前提：** 固定策略下适用的Markov预测关系、几何时域及可学习概率路径。

**限制：** 直接未来分布预测不能自动提供每一步因果轨迹；训练自举偏差和域外转移仍需检验。

**可证伪实验建议：** 固定训练数据与计算，比较rollout/直接未来分布在不同时域的分布误差、梯度方差和策略评估偏差。

**映射：** M45。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2025/oral/47200) · [论文](https://openreview.net/forum?id=j6H7c3aQyb)

## Flowing Datasets with Wasserstein over Wasserstein Gradient Flows

ICML 2025 · `icml2025-wow` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方Oral列表包含该题；对应oral/47240

**方法族：** 分布之上的分布；Wasserstein梯度流

**直觉：** 每个类别先表示为特征分布，整个数据集再表示为这些类别分布的混合，使数据集本身可被连续优化。

**模板：** 概念模板：ν=Σ_c w_c δ_{μ_c}；WoW²(ν,ν′)=inf_Γ∫W₂²(μ,μ′)dΓ；沿目标泛函梯度移动

**前提：** 类条件经验分布有代表性；底层特征距离和跨类传输结构有语义。

**限制：** 高维距离估计、类缺失和切片近似误差可影响效果；距离小不等于下游预测必提升。

**可证伪实验建议：** 对标签结构错配/缺失类别设计对照，比较普通OT与WoW对齐和真正独立下游任务。

**映射：** M59, M20。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://icml.cc/virtual/2025/events/oral) · [论文](https://arxiv.org/abs/2506.07534)

## Information Flow Reveals When to Trust Language Models

ICML 2026 · `icml2026-information-flow` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**录用字段：** Accept (spotlight)

**身份依据：** 官方JSON id71120：event_type=Oral；但decision=Accept (spotlight)；virtualsite_url=/virtual/2026/oral/71120

**身份补充：** 官方展示类型Oral已核实；录用决定保留spotlight，需与仅按Accept(oral)筛选的分析区分。

**方法族：** 信息流归因；置信度校准

**直觉：** 沿模型层追踪上下文token贡献，把证据相关性匹配程度和贡献集中程度用于判断回答可靠性。

**模板：** 概念模板：confidence=g(simulatability, concentration)；不是仅用输出token熵

**前提：** 能访问内部信息传播；检索证据和问题相关性可评估，校准集有代表性。

**限制：** 内部归因不自动是因果证据；集中于错误证据也可能过度自信。官方展示事件为Oral，但录用标签是spotlight，不能改写成Accept(oral)。

**可证伪实验建议：** 在相关/干扰/错误检索证据下比较AUROC、校准误差与拒答风险；固定模型和推理成本。

**映射：** M30。可靠性诊断，与选择性预测相关；不代表共形覆盖保证。

[官方身份来源](https://icml.cc/static/virtual/data/icml-2026-orals-posters.json) · [论文](https://proceedings.mlr.press/v306/xu26c.html)

## Uncoupled Learning Dynamics with O(log T) Swap Regret in Multiplayer Games

NeurIPS 2022 · `neurips2022-swap-regret` · `unverified` · 阅读 `abstract`

**原展示类型：** Oral candidate

**身份依据：** 作者页面报告oral；官方2022 JSON仅找到Poster55247、decision=Accept，未找到独立Oral事件

**身份补充：** 官方源 https://neurips.cc/static/virtual/data/neurips-2022-orals-posters.json 的当前快照事件类型只有Poster/Spotlight；不能从作者oral说法升级为官方verified。

**方法族：** 无悔学习；博弈均衡；乐观正则化

**直觉：** 每个玩家只需自身反馈；控制换行动规则后的事后收益改进，连接重复博弈与相关均衡。

**模板：** 框架模板：R_swap(T)=max_φ Σ_t[u(φ(a_t),a_-t)−u(a_t,a_-t)]；乐观正则化结合自协调障碍

**前提：** 对数速率要求所有玩家按指定动力学更新；一般对手环境对应不同速率。

**限制：** 低swap regret连接经验分布的相关均衡，不能直接声称最后一次策略达到纳什均衡。

**可证伪实验建议：** 在一般和博弈上同时画swap regret/T、相关均衡缺口与最后迭代震荡，区分平均收敛与逐点收敛。

**映射：** M33, M31。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://www.andrew.cmu.edu/user/ianagnos/) · [论文](https://proceedings.neurips.cc/paper_files/paper/2022/hash/15d45097f9806983f0629a77e93ee60f-Abstract-Conference.html)

## Direct Preference Optimization: Your Language Model is Secretly a Reward Model

NeurIPS 2023 · `neurips2023-dpo` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 页面标注：2023 Oral

**方法族：** 偏好学习；奖励与最优策略的重参数化

**直觉：** 将KL正则化奖励优化的最优策略关系代回偏好模型，使偏好对直接监督策略。

**模板：** 概念模板：rθ(x,y)=β log[πθ(y|x)/πref(y|x)]+c(x)；对偏好奖励差作logistic分类

**前提：** 偏好概率模型、KL正则目标和参考策略支持集需与推导匹配。

**限制：** 离线偏好覆盖不足、偏好噪声与参考策略偏差仍会影响结果；不能据此断言无需任何奖励假设。

**可证伪实验建议：** 固定偏好数据/模型/预算，与显式奖励模型路线比较，并分层改变偏好噪声和分布外提示。

**映射：** M56, M03。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://neurips.cc/virtual/2023/oral/73865) · [论文](https://arxiv.org/abs/2305.18290)

## Learning diffusion at lightspeed

NeurIPS 2024 · `neurips2024-lightspeed` · `verified` · 阅读 `method_section`

**原展示类型：** Oral

**身份依据：** 官方托管幻灯片：NeurIPS 2024, oral

**方法族：** Wasserstein梯度流；逆最优性条件

**直觉：** 观察分布随时间怎样移动，反推驱动能量；用一步变分更新的最优性条件避免反复求解内层问题。

**模板：** 框架：μ_next=argmin_μ {Fθ(μ)+W₂²(μ,μ_now)/(2τ)}；以一阶最优性残差拟合θ

**前提：** 快照动力学可以被设定的梯度流描述；传输与密度估计可信。

**限制：** 最优性残差小不自动代表能量唯一可识别；错误能量族、稀疏快照可造成混淆。

**可证伪实验建议：** 有真值势能/交互/扩散项的合成动力学分别恢复，逐步降低快照密度，再检验未见时间段预测。

**映射：** M59, M20。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://neurips.cc/media/neurips-2024/Slides/93047.pdf) · [论文](https://arxiv.org/abs/2406.12616)

## A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning

NeurIPS 2025 · `neurips2025-influence` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方托管幻灯片首页：NeurIPS 2025 oral

**方法族：** 局部影响归因；梯度相似度

**直觉：** 在线策略会改变后续训练数据，因此先把归因对象限制为检查点附近缓冲区，用样本梯度与动作/回报目标梯度的关系解释更新。

**模板：** 概念模板：influence_i ∝ ⟨∇θℓ_i,∇θJ_target⟩，正负号依损失/收益约定；不是全轨迹因果效应

**前提：** 局部检查点、近期缓冲、可微目标和PPO更新框架。

**限制：** 局部一阶关系不等于移除样本后的全训练因果贡献；筛选也会改变未来采样。

**可证伪实验建议：** 用局部真实移除/重加权更新检验归因排序；对全训练干预另设独立实验，不混同两种证据。

**映射：** 。局部梯度内积归因；目前59类暂无直接匹配，不能据此归入隐式微分。

[官方身份来源](https://neurips.cc/media/neurips-2025/Slides/115685.pdf) · [论文](https://arxiv.org/abs/2505.19281)

## Generative Modeling via Drifting

NeurIPS 2026 · `neurips2026-drifting` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方JSON id154241：event_type=Oral；decision=Accept (oral)；virtualsite_url=/virtual/2026/oral/154241

**方法族：** 分布动力学；推前映射；平衡匹配

**直觉：** 把生成分布的逐步变化放到训练过程，训练一个推前映射实现单步采样。

**模板：** 框架模板：qθ=(fθ)#p_prior；drift V[p,q]在p=q时为零，优化器更新fθ使qθ靠近p

**前提：** 漂移场、数据和生成样本估计有效；网络有足够表示能力。

**限制：** p=q⇒V=0不自动意味着V=0⇒p=q；平衡唯一性、优化收敛和有限样本偏差必须另核。

**可证伪实验建议：** 先在可知分布上检测伪平衡/模式遗漏；固定预算比较单步与多步方法的覆盖和采样代价。

**映射：** M21。核诱导分布比较/粒子漂移；不等同现有流匹配训练。

[官方身份来源](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json) · [论文](https://arxiv.org/abs/2602.04770)

## Follow the Regularized Leader Does Not Converge in Constrained Optimization

NeurIPS 2026 · `neurips2026-ftrl-limits` · `verified` · 阅读 `abstract`

**原展示类型：** Oral

**身份依据：** 官方JSON id150987：event_type=Oral；decision=Accept (oral)；virtualsite_url=/virtual/2026/oral/150987

**方法族：** 在线正则化；变分不等式；收敛反例

**直觉：** 目标单调改善或低regret并不保证约束非凸问题达到一阶稳定点；需要监控KKT条件。

**模板：** 框架模板：x_t=argmin_x{⟨Σ_s<t g_s,x⟩+R(x)/η}；连续时间FTRL反例中KKT gap持续非零

**前提：** 负结论针对无限光滑约束问题的连续时间FTRL；解析函数和Euclidean正则具有不同结果。

**限制：** 不能将一个反例解读为所有FTRL都失败；连续时间和有限步实现须分开。

**可证伪实验建议：** 重建论文反例，同时画目标值、KKT gap、轨迹；与镜像下降比较，并区分光滑/解析目标。

**映射：** M33, M11。首标签为主要数学联系，次标签为辅助联系；是否严格等价须以论文机制为准。

[官方身份来源](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json) · [论文](https://arxiv.org/abs/2610.35004)

