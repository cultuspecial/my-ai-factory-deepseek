# AI 简报 (2026-11-14)

### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
📄 论文提出AgentSSL，将半监督学习形式化为程序搜索问题，发现即使反馈微弱且计算量匹配，MLE智能体也能合成结合并适配已有SSL技术的代码，在12个设置中的8个上超越最强人工基线，最高提升+21.8%。
🔗 http://arxiv.org/abs/2611.17323v1

### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
📄 CoReMem提出了一种将记忆写入与读取成本内化的框架，通过前瞻性片段估值（对比有无继承轨迹片段时下一任务的表现）来指导围绕锚点（仓库位置和可执行检查）构建紧凑记忆，并适配执行者决策，从而在未知后续任务的连续编码场景中平衡记忆的未来效用与成本。
🔗 http://arxiv.org/abs/2611.17316v1

### Sketching Language Models for Context Attribution
📄 论文提出一种基于草图（sketching）的算法，在稳定性假设下用 \(O(\sqrt{\log(1/\varepsilon)}/\varepsilon)\) 次模型评估即可估计所有留一法上下文归因值，并证明匹配的下界，从而显著优于直接计算的 \(n\) 次评估。
🔗 http://arxiv.org/abs/2611.17313v1
