# AI 简报 (2026-08-25)

### How to Train a Critic Stably and Efficiently
📄 BPCO提出了一种结合DPPO、奖励范围限定的值预测、蒙特卡洛价值目标、未归一化策略优势及长度自适应GAE的稳定高效评论家训练方案，使基于评论家（critic）的方法在单响应下也能达到与群体采样方法（如GRPO）相当的性能，并允许在训练时利用隐藏于策略的奖励定义信息（如参考答案或评分标准）进一步提升优势估计的准确性。
🔗 http://arxiv.org/abs/2608.23566v1

### ReWorld: An Interactive World Model with Long-Horizon Memory
📄 ReWorld 通过混合注意力窗口与随机头路由解耦“控制”和“记忆”的冲突，并借助位姿索引地标库与有界KV缓存实现长时记忆下的实时交互世界建模，突破了结构上短时控制与无限记忆之间的固有矛盾。
🔗 http://arxiv.org/abs/2608.23565v1

### SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?
📄 该论文提出了SWE Refactor Bench基准，通过三阶段评估协议（迁移审计、行为正确性和防“盲目复制”机制）首次系统评测编码智能体在整仓库长周期技术栈迁移任务中的真实完成度，解决了现有基准仅验证行为正确性而无法检测“复制原实现骗过测试”的根本缺陷。
🔗 http://arxiv.org/abs/2608.23564v1
