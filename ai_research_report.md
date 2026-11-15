# AI 简报 (2026-11-15)

### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
📄 论文提出AgentSSL框架，将半监督学习形式化为程序搜索问题，发现即使反馈有限且计算资源相当，MLE智能体也能合成结合并适配既有SSL技术的代码，在12个设定中的8个上超越最强人工基线最多+21.8%。
🔗 http://arxiv.org/abs/2611.17323v1

### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
📄 CoReMem提出了一种将记忆写入/读取成本内化的框架，通过前瞻性片段估值（对比有无特定轨迹片段时下一任务的表现）来指导面向未知后续编码任务的紧凑记忆设计（围绕仓库位置与可执行检查等锚点构建），并适配执行者策略，从而在连续编码任务中平衡记忆的未来效用与成本。
🔗 http://arxiv.org/abs/2611.17316v1

### Sketching Language Models for Context Attribution
📄 该论文提出了一种基于稳定性假设的草图算法，仅需 \(O(\sqrt{\log(1/\varepsilon)}/\varepsilon)\) 次模型评估即可将所有留一法上下文归因值估计到误差 \(\varepsilon\)，并证明了匹配的下界，且在检索任务上验证了有效性。
🔗 http://arxiv.org/abs/2611.17313v1
