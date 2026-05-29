# AI 简报 (2026-05-29)

### Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
📄 该论文通过一个受物理学家监督的AI编程智能体（Claude Code）开发科学软件（CLAX-PT）的量化案例研究，揭示了当前AI智能体在科学计算中的根本局限：其倾向于通过“症状缓解”而非“根因分析”修正代码错误，即使面对无法表征目标物理现象的代码架构，也无法自主跳出局部修正循环，从而论证了物理学家领域知识在AI辅助科研中的不可替代性。
🔗 http://arxiv.org/abs/2605.30353v1

### VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
📄 **论文贡献**：首次将多头潜在注意力（MLA）机制引入视频扩散模型，通过共享低秩内容潜变量和分离式3D-RoPE位置键，将每层缓存的KV内存减少92.7%，并揭示了其在视频扩散中成功的原因（即使语言模型中常用的频谱假设不成立）。
🔗 http://arxiv.org/abs/2605.30351v1

### LLMSurgeon: Diagnosing Data Mixture of Large Language Models
📄 LLMSurgeon提出了一种基于软混淆矩阵和逆问题求解的新框架，能够仅从目标大模型的生成文本中，有效反推其预训练数据的领域分布，解决了数据混合可审计性难题。
🔗 http://arxiv.org/abs/2605.30348v1
