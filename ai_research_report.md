# AI 简报 (2026-08-05)

### TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning
📄 TurnSight提出了一种基于执行结果事后反馈的回合级（turn-level）事后自我蒸馏框架，通过利用状态实际访问情况生成密集监督信号，解决了工具集成推理中轨迹级信用分配粗粒度的问题，并提升了长时程推理任务中模型的细粒度学习效率与性能。
🔗 http://arxiv.org/abs/2608.04007v1

### Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility
📄 该论文系统化梳理了推理大模型中的测试时扩展（test-time scaling）方法，提出按推理机制（单轨迹扩展、采样-聚合、搜索）划分的统一形式化框架，并强调在评估与复现中必须明确推理协议、计算预算与统计结构，以避免不同研究间因方法混用或报告不完整而导致的不可比性。
🔗 http://arxiv.org/abs/2608.04001v1

### Can Large Language Models Recover Semantic Optimization Opportunities That Compilers Miss?
📄 这篇论文首次提出了 **SeGaBench** 基准，系统性地评估大语言模型能否从异构C/C++代码上下文中“挖掘”出编译器因缺失语义信息而错过的优化机会，并将其转化为经过验证的正确且保持语义的优化产物——实验表明最强模型在94.8%的响应中生成正确结果，并实现至少1.05倍的加速。
🔗 http://arxiv.org/abs/2608.03983v1
