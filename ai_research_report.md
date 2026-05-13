# AI 简报 (2026-05-13)

### AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward
📄 AlphaGRPO通过分解可验证奖励（DVReward）将GRPO应用于统一多模态模型，无需冷启动即实现自我反思式多模态生成，并能推理用户隐含意图并自主诊断修正生成偏差。
🔗 http://arxiv.org/abs/2605.12495v1

### Learning, Fast and Slow: Towards LLMs That Adapt Continually
📄 该论文提出了一种针对大语言模型的“快慢学习”框架，通过结合参数更新（慢权重）与上下文优化（快适应），在避免灾难性遗忘和保持可塑性的同时，实现更高效且持续的任务适应。
🔗 http://arxiv.org/abs/2605.12484v1

### Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training
📄 该论文提出了一种“从稀疏到密集的奖励分配原则”，主张在语言模型后训练中，应将稀缺的可验证标注数据优先用于生成能力强、探索性高的模型（如通过GRPO进行稀疏奖励强化学习），而将密集的教师监督（如通过OPD）用于将行为压缩到较小模型，从而更高效地分配标注资源。
🔗 http://arxiv.org/abs/2605.12483v1
