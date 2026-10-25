# AI 简报 (2026-10-25)

### Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning
📄 论文提出Direct Pass@$k$优化方法，通过在生成短前缀后对候选推理路径进行剪枝，在质量（预测正确性）与多样性（覆盖不同推理轨迹）之间取得平衡，从而在测试时推理中以更低计算成本提升找到正确答案的概率。
🔗 http://arxiv.org/abs/2610.31667v1

### Cost-Aware Abstention for LLM-Based IT Ticket Classification
📄 论文提出并验证了一种基于成本感知弃权的LLM工单分类评估框架：在校准集上按显式成本选择路由策略并在测试集上冻结评估，实验表明TF-IDF+逻辑回归配合0.60阈值可将测试成本相对降低38.1%，同时将错误路由率从15.3%降至3.5%。
🔗 http://arxiv.org/abs/2610.31657v1

### METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning
📄 METTA通过将快速适应分解为线性复杂度的因果神经记忆（负责幕内细粒度适应）和紧凑的幕级摘要（支持跨幕长程任务推断），在避免二次方计算与内存开销的同时实现了元强化学习的高效测试时适应。
🔗 http://arxiv.org/abs/2610.31656v1
