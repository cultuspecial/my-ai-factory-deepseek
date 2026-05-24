# AI 简报 (2026-05-24)

### Vector Policy Optimization: Training for Diversity Improves Test-Time Search
📄 VPO提出了一种强化学习算法，通过显式训练策略生成多样化解以应对下游任务中多种未知的向量奖励函数，从而显著提升模型在推理时搜索（如AlphaEvolve）中的泛化性能。
🔗 http://arxiv.org/abs/2605.22817v1

### The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning
📄 该论文提出**匹配原则**，将鲁棒性、领域自适应、遮挡不变性等一系列看似独立的问题统一为“估计标签保持扰动的协方差并沿其范围正则化编码器雅可比矩阵”的几何框架，并在线性高斯模型中证明了闭式最优性。
🔗 http://arxiv.org/abs/2605.22800v1

### Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models
📄 这篇论文提出了一种**保守式漂移方法**用于单步生成建模，通过将原位移驱动速度替换为核密度估计（KDE）梯度速度（即核平滑后的数据得分与模型得分之差），解决了传统位移驱动方法中**非保守性**的问题，并在连续时间下证明了有限粒子的收敛速率，揭示了关键修正项为**递归KDE自相互作用项**。
🔗 http://arxiv.org/abs/2605.22795v1
