# AI 简报 (2026-09-06)

### Compile by Training: Turning Natural-Language Specifications into Local Neural Functions
📄 该论文提出“编译即训练”方法，将自然语言规范自动转化为可复用的小型本地神经函数，无需调用远程模型，在FuzzyBench-Hard上达到83.6%的语义准确率，虽编译耗时约一分钟但显著提升了精度与可部署性。
🔗 http://arxiv.org/abs/2609.04199v1

### Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints
📄 这篇论文的核心贡献在于：通过两项预注册的严格审计实验（共52,988次请求），实证揭示了“黑箱LLM裁判”在同一模型端点上的测量结果极不稳定——同日重复与隔日逐字节重放的相关性均远低于预注册阈值（0.400 vs 0.90；0.78 vs 0.99），并识别出标签映射偏差与候选间微小差异是导致失效的机制，从而质疑了依赖LLM作为可靠测量工具的基础假设。
🔗 http://arxiv.org/abs/2609.04198v1

### ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize
📄 ESPO提出了一种通过“诊断-生成-稳定选择”三阶段框架的错误结构化提示优化方法，有效缓解了进化式提示优化中的提示膨胀问题，在七个NLP基准上平均准确率较现有最优方法提升3.76个百分点。
🔗 http://arxiv.org/abs/2609.04197v1
