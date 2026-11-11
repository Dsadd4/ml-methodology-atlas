# ML Methodology Atlas

用户授权：2026-10-27，独立整理机器学习/数学方法论，以原有30类为主体，调研2022—2026年NeurIPS、ICML、ICLR、CVPR、ICCV、ECCV官方Oral并扩充。

- 主体是方法论总表，不转移成单独的科研流程教程；不为了数量把算法品牌当独立数学框架。
- 原30类ID M01—M30固定保留。新增类别需说明与已有类别区别；同一论文可映射多个类别。
- Oral必须有官方逐篇身份或官方session证据；Spotlight、Highlight、Workshop Oral不自动算主会Oral。获奖也不自动算Oral。
- 官方身份与论文内容阅读深度分开记录。摘要筛读不能写成方法全文精读；公式模板不是原文定理。
- 2022—2026按会议年份，不按arXiv首发年。ICCV/ECCV非举办年份记not_scheduled，不记遗漏。2026未核实的身份记待核验，不猜。
- 当前是面向方法覆盖的精选调研，不称全部Oral穷尽综述，不据样本频次推断全会议趋势。
- `data/methods.json`为方法论主数据；各分组论文JSON保留来源，汇总由`scripts/build_catalog.py`生成。
- 每次更新保留出处、检查日期、局限和读到的层级；优先官方program、OpenReview最终decision、proceedings与作者正文。
- 文献整理仅轻量编辑与网页核验；不启动模型实验、GPU任务或自动监控；不改其他项目。

入口：README.md；方法总表METHODS.md；论文索引ORAL_PAPERS.md；覆盖COVERAGE.md。
