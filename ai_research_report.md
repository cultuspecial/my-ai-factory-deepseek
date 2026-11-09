# AI 简报 (2026-11-09)

### On Agentic Manipulation Policies
📄 论文提出并验证了“智能体操作策略”（AMP）——让通用AI模型直接控制机械臂并随任务进展自适应调整动作，无需演示数据或任务专项训练，其参考实现AMP1在单臂、双臂和移动操作上通用，并在RoboLab-120和CaP-Gym基准上零样本达到最先进水平（如RoboLab-120成功率85.6%，远超领先VLA和WAM的49.2%和42.9%）。
🔗 http://arxiv.org/abs/2611.09892v1

### CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse
📄 论文提出“智能体推理缓存”（ARCs），将大模型推理过程转化为可CPU执行、可解释且可持续训练的缓存方案，在新问题上复用已有推理，性能媲美前沿大模型，调用成本降低16–291倍。
🔗 http://arxiv.org/abs/2611.09891v1

### On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning
📄 论文分析了测试时强化学习中多数投票伪标签的可靠性，将误差分解为群体多数偏差与提示相关的有限采样波动，并提出提示条件分布鲁棒DPO（PC-Dr.DPO），依据观测到的投票可靠性对提示内样本进行鲁棒重加权，使采样敏感提示的更新更保守，从而缓解有限采样波动的下游影响。
🔗 http://arxiv.org/abs/2611.09872v1
