# AI 简报 (2026-11-13)

### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
📄 论文提出AgentSSL，将半监督学习形式化为程序搜索问题，发现MLE智能体在弱反馈和同等算力下能合成结合并适配已有SSL技术的代码，在12个设置中的8个超越最强人工基线（最高提升21.8%）。
🔗 http://arxiv.org/abs/2611.17323v1

### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
📄 CoReMem提出了一种将写入/读取成本内化的记忆框架，通过前瞻性片段估值（对比有无某段记忆时下一任务的表现）来指导围绕仓库锚点（位置与可执行检查）构建紧凑记忆，并让智能体自适应地决定何时依赖记忆以节省任务执行开销。
🔗 http://arxiv.org/abs/2611.17316v1

### Sketching Language Models for Context Attribution
📄 该论文提出用草图（sketching）算法在稳定性假设下以 \(O(\sqrt{\log(1/\varepsilon)}/\varepsilon)\) 次模型评估高效估计所有留一法上下文归因值，并证明了匹配的下界。
🔗 http://arxiv.org/abs/2611.17313v1
