# AI 简报 (2026-11-02)

### Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention
📄 提出Latent Sparse Attention（LSA），通过在学习的潜在空间中对键进行层次聚类、让查询对聚类层次而非每个键打分，从而在超长上下文（超100万token）下实现亚二次复杂度且保持精度的稀疏注意力方法。
🔗 http://arxiv.org/abs/2610.42147v1

### Hierarchical World Models with Implicit Dynamics
📄 ID-WM提出一种分层世界模型，将状态空间可达性与局部控制解耦，高层模型采样可行状态转移、低层世界模型作为逆动力学求解器将其落地为精确动作，从而在长程任务中实现更灵活、精细的规划与控制。
🔗 http://arxiv.org/abs/2610.42146v1

### RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory
📄 RoboArchitect 提出用编码模型自动迭代设计冻结机器人策略外围的智能体框架（harness），无需微调模型权重即可将未见场景和任务上的平均成功率分别提升至43.3%和40.2%（提升约4.5倍和3.2倍）。
🔗 http://arxiv.org/abs/2610.42141v1
