# AI 简报 (2026-06-25)

### Learning Action Priors for Cross-embodiment Robot Manipulation
📄 本文提出一种两阶段训练框架，通过先预训练动作模块获取跨本体时间运动先验，再对齐视觉-语言-动作（VLA）模型，有效解决了现有VLA模型缺乏运动先验导致跨本体操控学习困难的问题。
🔗 http://arxiv.org/abs/2606.26095v1

### On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
📄 该论文揭示了同策略自蒸馏方法（通过正确演示提供密集token级反馈）虽能提升pass@1准确率，但会导致模型生成多样性下降及pass@k曲线趋于平缓（即增加采样次数无法持续提升准确率），并从理论上证明该偏差源于教师模型在自身偏误下根据条件互信息评分扭曲学生输出的基础分布。
🔗 http://arxiv.org/abs/2606.26091v1

### Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
📄 这篇论文发现，强化学习后训练中策略模型与参考模型的对数概率比可以直接作为最优优势函数，从而免去了为智能体任务单独训练过程奖励模型的需求。
🔗 http://arxiv.org/abs/2606.26080v1
