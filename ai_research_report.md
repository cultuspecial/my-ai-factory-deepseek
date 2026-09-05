# AI 简报 (2026-09-05)

### Compile by Training: Turning Natural-Language Specifications into Local Neural Functions
📄 这篇论文提出“编译即训练”方法，将自然语言描述自动转化为可复用的小型本地神经函数，在编译阶段借助教师模型生成训练样本，从而无需远程大模型推理，在FuzzyBench-Hard上达到83.6%的语义准确率，并支持像软件一样存储、版本化和组合。
🔗 http://arxiv.org/abs/2609.04199v1

### Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints
📄 这篇论文的核心贡献在于，通过两项预注册的严格审计，实证揭示了基于黑盒大语言模型的评判系统在共享端点上的测量不可靠性：即便请求完全一致、模型名称相同，其重复评估结果的一致性远低于可接受阈值（如Spearman相关系数仅0.400对要求的0.90），从而系统性地质疑了此类“LLM裁判”作为稳定测量工具的适用性。
🔗 http://arxiv.org/abs/2609.04198v1

### ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize
📄 ESPO提出了一种基于错误结构化诊断、多样化生成和自举稳定选择的提示词优化方法，有效解决了进化式优化器（如GEPA）的提示词膨胀问题，并在七个公开NLP基准上将平均准确率提升了3.76个百分点（达74.67%）。
🔗 http://arxiv.org/abs/2609.04197v1
