# 视觉顶会 Oral：方法论首轮证据库（2022–2026）

核查日期：2026-10-27。共16篇；全部逐篇具有官方 Oral 依据。此为有目的的代表性样本，不是全量目录或频率统计。其中2篇已实际读取方法段并标记 `method_section`（拓扑分割、凸松弛）；其余14篇为 `abstract`。下列公式是用于迁移研究问题的数学框架示意，除明确说明外不声称逐字复刻论文公式。`new_family` 是相对于常见 Bayes/熵/minmax 等入口的扩展候选；原30类完整原表尚未在本子任务获得，因此最终新增/合并由总表对齐后决定。

## 覆盖与缺口

|年份|CVPR|ICCV|ECCV|
|---|---|---|---|
|2022|1篇|非举办年|3篇|
|2023|1篇 Oral-Award|1篇|非举办年|
|2024|1篇|非举办年|1篇|
|2025|2篇|2篇|非举办年|
|2026|2篇|非举办年|2篇|

2026记录均来自已经公开的官方 oral event 和其摘要，不以年份推断接收状态。未覆盖年份不代表没有相关论文。没有根据本样本估计任何方法的占比或近年趋势。

## 如何变成研究设计

1. **观察的是无效结构**：考虑流形、拓扑、包含/排斥关系；比较同等容量下约束是否提高结构正确率，同时报告像素或任务误差。
2. **观察的是上游误差累积**：传递后验或不确定性；设计校准、错配和分布偏移实验，比较点估计与分布传递。
3. **观察的是优化太难或规模太大**：考虑凸松弛、算法展开、区域分解；分别检查松弛间隙、近似误差、真实内存和任务效果。
4. **观察的是生成路径或表征不合适**：考虑连续输运、热核内蕴几何、潜变量分解；比较表示与路径本身，不只换更大模型。
5. **观察的是评估过于乐观**：把被评估管线写进攻击目标，检验梯度、随机性与预算；不要把攻击失败误当成证明。

## 逐篇提炼

### SNUG: Self-Supervised Neural Dynamic Garments（CVPR 2022）

- **方法族**：变分力学与物理自监督
- **研究现象 → 框架**：将逐时刻隐式积分重写为优化问题，让物理能量承担监督信号，减少预先生成真值轨迹的需求。
- **数学入口**：框架示意：x_{t+1}=argmin_x [惯性能量(x,x_t,v_t)+势能(x)]，以该目标训练预测网络。
- **需验证假设**：材料模型、边界条件和人体运动输入足够可信；训练状态覆盖测试动态。
- **失效边界**：物理先验有模型误差；低损失不等同真实服装材料准确。作者项目页有Eq9材料系数和Eq10弯曲能缩放勘误，复现须核对：https://mslab.es/projects/SNUG/
- **Oral证据**：[官方来源](https://cvpr2022.thecvf.com/orals-622-pm)；官方 Orals 6/22 PM 页面，2022-06-22 13:30–15:00，21b列名。
- **阅读证据**：[abstract](https://openaccess.thecvf.com/content/CVPR2022/html/Santesteban_SNUG_Self-Supervised_Neural_Dynamic_Garments_CVPR_2022_paper.html)；已读官方摘要；未升级为方法节精读。

### PACTran: PAC-Bayesian Metrics for Estimating the Transferability of Pretrained Models to Classification Tasks（ECCV 2022）

- **方法族**：PAC-Bayes泛化界与模型选择
- **研究现象 → 框架**：预训练模型选择可用风险与后验复杂度折中，不必为每个候选完整微调。
- **数学入口**：框架示意：min_Q Rhat(Q)+Complexity(KL(Q||P),n,δ)；具体界及常数需按原文实例。
- **需验证假设**：界所需采样、先验和后验条件成立；代理任务与实际微调目标相符。
- **失效边界**：代理得分排名不保证任意微调方案的排序；界有时宽松。
- **Oral证据**：[官方来源](https://eccv2022.ecva.net/program/accepted-papers/)；官方 Oral papers 表，ID 6568。
- **阅读证据**：[abstract](https://arxiv.org/abs/2203.05126)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Pose-NDF: Modelling Human Pose Manifolds with Neural Distance Fields（ECCV 2022）

- **方法族**：流形约束与隐式距离场
- **研究现象 → 框架**：先学习有效解集合的几何，再把不合理预测投影回集合；可迁移到满足结构约束的连续预测。
- **数学入口**：框架示意：M={q∈SO(3)^K:fθ(q)=0}；沿流形梯度降低 fθ 并保持旋转约束。
- **需验证假设**：训练姿态覆盖目标有效姿态；学习的距离能反映几何邻近。
- **失效边界**：分布外姿态可能被错误投影；非凸投影不保证全局最近解。
- **Oral证据**：[官方来源](https://eccv2022.ecva.net/program/accepted-papers/)；官方 accepted-papers 第一张表 Oral papers，ID 1413；第二张表是 Poster，不混入。
- **阅读证据**：[abstract](https://arxiv.org/abs/2207.13807)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Learning Topological Interactions for Multi-Class Medical Image Segmentation（ECCV 2022）

- **方法族**：拓扑与多对象关系约束
- **研究现象 → 框架**：像素预测正确率不等于结构正确；把类别之间包含、排斥等关系变成训练约束。
- **数学入口**：原文§3.2 Eq(3)–(4)：Lti=Lpixel(f⊙V,g⊙V)，Ltotal=Lce+λdice Ldice+λti Lti；V由§3.1的邻域卷积与禁止标签对生成。
- **需验证假设**：解剖类别关系可可靠定义，标签与关系先验一致。
- **失效边界**：约束依赖离散邻域定义、类别关系和标注；损失惩罚不是推理时硬可行性保证，也不保证所有连通性/洞数量正确。
- **Oral证据**：[官方来源](https://eccv2022.ecva.net/program/accepted-papers/)；官方 Oral papers 表，ID 6180；arXiv comment 亦注明 Oral。
- **阅读证据**：[method_section](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136890691.pdf)；§3.1，pp6–8：Eq(1)卷积求邻域，Eq(2)找违反禁止邻接的critical pixel集合；§3.2，p9：Eq(3) Lti=Lpixel(f⊙V,g⊙V)，Eq(4) Ltotal=Lce+λdice Ldice+λti Lti。包含关系通过禁止内部类接触包围类之外的标签编码；邻域由数字拓扑connectivity kernel决定。这里约束的是特定包含/排斥关系，非一般持久同调或所有Betti数。

### 3D Registration With Maximal Cliques（CVPR 2023）

- **方法族**：相容图、极大团与多假设共识
- **研究现象 → 框架**：最大团未必对应正确几何；枚举多个不可继续扩大的局部一致集合，从它们生成候选变换并验证。
- **数学入口**：框架示意：G=(V,E)，相容匹配为边；每个极大团C产生 SVD刚体解(R_C,t_C)，再按全局对应一致性选解。
- **需验证假设**：匹配的几何相容性能有效区别内外点；候选团中存在正确共识。
- **失效边界**：极大团≠最大团；枚举数量最坏可指数增长；错误相容关系仍可组成团。
- **Oral证据**：[官方来源](https://media.icml.cc/Conferences/CVPR2023/CVPR_2023_MainConference_ProgramGuide.pdf)；官方 Program Guide 印刷p14/PDF第18页：2023-06-20 Oral-Award-Tue 15:10列名，Award candidate paper presentations。
- **阅读证据**：[abstract](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_3D_Registration_With_Maximal_Cliques_CVPR_2023_paper.html)；已读官方摘要；未升级为方法节精读。

### Robust Evaluation of Diffusion-Based Adversarial Purification（ICCV 2023）

- **方法族**：随机系统的自适应鲁棒评估
- **研究现象 → 框架**：防御内部有随机性和迭代求解时，攻击必须穿过实际管线；梯度难求不能当成鲁棒性。
- **数学入口**：框架示意：max_{δ∈Δ} Eξ[ℓ(f(Pξ(x+δ)),y)]；用可用的代理梯度逼近迭代净化过程。
- **需验证假设**：威胁集明确；攻击能近似随机净化管线，采样与迭代预算足够。
- **失效边界**：有限攻击只给风险下界，不是鲁棒性认证；代理梯度仍可能漏攻。
- **Oral证据**：[官方来源](https://iccv2023.thecvf.com/telechargements/fichiers/1696406666.iccv2023.opening.slides.pdf)；官方开幕 slides 的 Orals 表：2023-10-04 09:30–10:30 Adversarial attack and defense，paper 11381。
- **阅读证据**：[abstract](https://arxiv.org/abs/2303.09051)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Producing and Leveraging Online Map Uncertainty in Trajectory Prediction（CVPR 2024）

- **方法族**：层级概率建模与不确定性传播
- **研究现象 → 框架**：上游地图不确定时，把分布而非单点估计传给下游轨迹预测。
- **数学入口**：框架示意：p(τ|x)=∫p(τ|m,x)p(m|x)dm；积分可近似，非原文公式复刻。
- **需验证假设**：地图不确定性表征可靠；下游会利用其信息而非忽略。
- **失效边界**：校准误差会传播；平均预测质量不构成自动驾驶安全保证。
- **Oral证据**：[官方来源](https://cvpr.thecvf.com/Conferences/2024/News/Oral_Papers)；CVPR 2024 官方 Oral Papers 新闻页明确列名。
- **阅读证据**：[abstract](https://arxiv.org/abs/2403.16439)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### RACE: Robust Adversarial Concept Erasure for Secure Text-to-Image Diffusion Model（ECCV 2024）

- **方法族**：对抗鲁棒优化与知识移除
- **研究现象 → 框架**：移除概念不能只看常规提示；主动寻找仍触发该概念的输入，再训练抵御。
- **数学入口**：框架示意：minθ max_{δ∈Δ} Lerase(θ,e+δ)+λLretain(θ)；精确损失需查原文。
- **需验证假设**：文本嵌入攻击集合代表真实风险；保留概念集合定义清楚。
- **失效边界**：有限嵌入攻击不等于全提示空间的彻底移除；保留能力存在权衡。
- **Oral证据**：[官方来源](https://eccv.ecva.net/media/eccv-2024/Slides/2341_x8MzD3f.pdf)；官方托管 slides 标题页明示 ECCV 2024 (Oral)。
- **阅读证据**：[abstract](https://arxiv.org/abs/2405.16341)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Convex Relaxation for Robust Vanishing Point Estimation in Manhattan World（CVPR 2025）

- **方法族**：凸松弛与半正定提升
- **研究现象 → 框架**：把离散关联与几何求解难题转成QCQP，再放松为可解的凸问题。
- **数学入口**：§3.3 Eq(4)–(7)：min xᵀCx s.t. xᵀA_i x=b_i；令X=xxᵀ，保留tr(A_i X)=b_i、X≽0，删除rank(X)=1。论文§4.2将VP联合关联提升为具体Full SDP，§4.3使用逐方向Single Block SDP。
- **需验证假设**：Manhattan三方向与相机内参条件适用；逐方向最大内点识别依赖论文的distinguishability假设，单块紧性证明采用无噪声无离群条件。
- **失效边界**：不能把理想条件下紧性证明外推为任意噪声/离群的保证；随机采样和顺序去除内点影响实际全局行为；SDP规模成本仍存在。
- **Oral证据**：[官方来源](https://cvpr.thecvf.com/virtual/2025/oral/35342)；官方 /virtual/2025/events/oral 列表的同名 oral event。
- **阅读证据**：[method_section](https://arxiv.org/html/2505.04788v1)；§3.3 Eq(4)–(7)：QCQP经X=xxᵀ提升并去掉rank=1为SDP。§4.1 Primal Problem：Q为每列one-hot，三方向单位正交，外点截断c²。§4.2 Eq(8)–(12)给Full QCQP/SDP；§4.3.1 Eq(13)–(14)与Single Block SDP逐方向求解。§4.3.1 Remark明确需distinguishability，且单块紧性证明限noise-free/outlier-free；§4.3.2再正交精化，规模大时随机采样线。

### TopoCellGen: Generating Histopathology Cell Topology with a Diffusion Model（CVPR 2025）

- **方法族**：拓扑约束与结构感知生成评估
- **研究现象 → 框架**：生成细胞布局时约束空间结构，并用 TopoFD 评估结构差异，弥补仅看外观的不足。
- **数学入口**：框架示意：L=Ldiff+λLtopology；通过拓扑特征分布比较生成布局与真实布局。
- **需验证假设**：拓扑特征捕捉任务相关结构，细胞类型及布局标注可信。
- **失效边界**：结构相似不是生物机制证明；Topological FID 也受样本量和特征选择影响。
- **Oral证据**：[官方来源](https://cvpr.thecvf.com/virtual/2025/oral/35356)；官方同名oral event 35356；官方slides另明确标注Oral Presentation。
- **阅读证据**：[abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_TopoCellGen_Generating_Histopathology_Cell_Topology_with_a_Diffusion_Model_CVPR_2025_paper.html)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Diffusion Image Prior（ICCV 2025）

- **方法族**：隐式正则化与早停
- **研究现象 → 框架**：优化过程可能先拟合真实结构、后拟合退化伪影；利用时间顺序作为先验。
- **数学入口**：框架示意：x_t=Optimize_t(prior,y)，在拟合噪声前选择 t_stop；不是决策论最优停止定理。
- **需验证假设**：拟合结构与伪影的时间可分；有实际可用的停止准则。
- **失效边界**：未知退化与停止选择影响可信度；生成先验可能引入不真实细节。
- **Oral证据**：[官方来源](https://iccv.thecvf.com/virtual/2025/oral/2934)；官方 oral event 2934，含同名摘要。
- **阅读证据**：[abstract](https://iccv.thecvf.com/virtual/2025/oral/2934)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models（ICCV 2025）

- **方法族**：连续流与分布间输运
- **研究现象 → 框架**：直接构造连接源提示与目标提示分布的ODE，用路径设计控制编辑，不必先反演为噪声。
- **数学入口**：框架示意：dx/dt=v(x,t;csrc,ctgt)；具体 FlowEdit 速度构造需读方法节，不等同一般条件流。
- **需验证假设**：预训练流模型准确表达目标条件分布；源图与条件有合理对应。
- **失效边界**：较低输运成本不等于严格最优输运；内容保留和复杂编辑仍需实验检查。
- **Oral证据**：[官方来源](https://iccv.thecvf.com/virtual/2025/oral/2925)；官方 oral event 2925，含同名摘要。
- **阅读证据**：[abstract](https://iccv.thecvf.com/virtual/2025/oral/2925)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Differentiable Vector Quantization for Rate-Distortion Optimization of Generative Image Compression（CVPR 2026）

- **方法族**：率失真理论与离散变量软松弛
- **研究现象 → 框架**：用距离相关软码字后验连接离散量化与熵模型，让编码器能收到码率目标的梯度。
- **数学入口**：摘要机制示意：q(k|z)∝exp(−d(z,c_k)/T)，R≈−Σ_k q(k|z)log pφ(k|context)，L=R+λD；核函数形式为示意。
- **需验证假设**：软后验能近似实际码字选择；熵模型与传输协议一致。
- **失效边界**：可微率代理不自动等于真实比特数；感知质量与像素保真存在权衡。
- **Oral证据**：[官方来源](https://cvpr.thecvf.com/virtual/2026/oral/40298)；官方 oral event 40298，含摘要和 CVF Paper PDF 链接。
- **阅读证据**：[abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Differentiable_Vector_Quantization_for_Rate-Distortion_Optimization_of_Generative_Image_Compression_CVPR_2026_paper.html)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Efficient Unrolled Networks for Large-Scale 3D Inverse Problems（CVPR 2026）

- **方法族**：算法展开、算子近似与区域分解
- **研究现象 → 框架**：把物理成像算子嵌入网络，用区域划分和正规算子近似缓解3D问题的显存瓶颈。
- **数学入口**：通用展开示意：x_{k+1}=Dθk(x_k−η_k A* (Ax_k−y))；论文关键是域划分和 A*A 近似，非该式本身。
- **需验证假设**：前向算子已知且近似误差可控；分区能保持全局物理耦合的重要部分。
- **失效边界**：近似引入偏差；可扩展性与重建保真度需逐算子验证。
- **Oral证据**：[官方来源](https://cvpr.thecvf.com/virtual/2026/oral/40269)；官方 oral event 40269，含摘要和 CVF Paper PDF 链接。
- **阅读证据**：[abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### Heat Kernel Textures -- the Geodesic Gaussians That Do Not Splat（ECCV 2026）

- **方法族**：黎曼几何、热核与内蕴表示
- **研究现象 → 框架**：在物体表面直接定义各向异性热核，避免将曲面纹理强行展开到二维UV坐标。
- **数学入口**：基础框架：∂t u=−Δ_M u，H_t=exp(−tΔ_M)；论文使用离散曲面上的各向异性核。
- **需验证假设**：三角网格合理表示流形表面；离散几何算子稳定。
- **失效边界**：网格质量和离散近似影响纹理；方法针对表面表示，不是通用生成保证。
- **Oral证据**：[官方来源](https://eccv.ecva.net/virtual/2026/oral/6124)；官方 oral event 6124，含摘要和官方论文 PDF 链接。
- **阅读证据**：[abstract](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2392.pdf)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

### MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation（ECCV 2026）

- **方法族**：变量变换、可逆模型与语义分解
- **研究现象 → 框架**：让流模型集中拟合语义潜变量，解码器负责高频细节，减少可逆建模在像素细节上的容量消耗。
- **数学入口**：NF基础：log p_X(x)=log p_Z(f(x))+log|det J_f(x)|；VAE/解码器组成的完整混合模型不因此自动具有精确边缘似然。
- **需验证假设**：NF部分可逆且Jacobian可计算；语义与细节分工能够学习。
- **失效边界**：潜变量信息丢失和重建目标会影响生成；NF精确密度属性不能直接推广到整体。
- **Oral证据**：[官方来源](https://eccv.ecva.net/virtual/2026/oral/6128)；官方 oral event 6128，含摘要和官方论文 PDF 链接。
- **阅读证据**：[abstract](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2272.pdf)；已读论文或官方事件摘要；公式为框架示意，未核对方法节式号。

## 检索与核验记录

- 从 ECCV2022 官方 accepted-papers 页检查表格边界：第一表 Oral，第二表 Poster。直接在整页搜索标题会误混Poster，已排除这种命中；例如 Subspace Diffusion 不能因全页命中而记为Oral。
- ICCV2023 使用官方开幕slides中的逐场次Orals表，锁定论文ID与会话；不以获奖或标题热度推断Oral。
- CVPR2024 使用官方 Oral Papers 新闻条目；ECCV2024、CVPR2025个别记录使用官方托管slides明确写出的Oral标签。
- CVPR2025、ICCV2025、CVPR2026、ECCV2026 读取官方 `/virtual/YYYY/events/oral` 与对应 `/oral/ID`；后者同时提供题名、摘要及部分论文链接。
- 搜索工具对若干 `/virtual` 页返回robots限制；以Python requests对相同官方公开HTML做有界读取后核对，不用搜索摘要替代页面。个别PDF超大小限制或超时，改用官方HTML证据。
- 内容来源为CVF、ECVA、会议官网、作者arXiv；未将博客二手陈述作为Oral证据。未下载全量PDF、未复现实验，未引用未核对的性能百分比。

## 后续精读优先序

优先核查 FlowEdit 的速度场与输运成本论证、凸松弛的紧性条件、TopoCellGen 的拓扑特征和Topological FID定义、DIIP可操作早停准则、2026域分解的正规算子近似误差。精读后再补精确式号、消融、反例与可复现实验设计。CVPR2022/2023已各补1篇，视觉会议10个实际举办年份单元均有代表样本。

## 第二轮补核（2026-10-27）

CVPR2022 SNUG由官方6/22 PM Orals表核实。CVPR2023 MAC由官方Program Guide PDF第18页的Oral-Award-Tue核实，保留Award candidate session原始类型，不将普通Highlight转换为Oral。两篇方法精读分别使用ECVA正式PDF与作者arXiv HTML；记录章节、式号及紧性条件。16个唯一ID及新增content_source_url/method_evidence字段已核对。
