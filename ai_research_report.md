# AI 简报 (2026-08-24)

### Primal Acceleration of Newton's Method
📄 该论文提出一种仅使用原始变量、每次迭代只需一次线性求解的直接加速牛顿法，首次在仅依赖单次线性系统求解（无需辅助非线性正则化子问题、非线性参数搜索或对偶外梯度校正）的条件下，实现对具有Lipschitz连续Hessian的凸函数达到$O(1/k^3)$全局收敛率，并支持Hessian-free的近似求解实现。
🔗 http://arxiv.org/abs/2608.21359v1

### VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences
📄 VIALS benchmark揭示了前沿视觉语言模型在生命科学领域专业视觉符号（如凝胶电泳图、显微图像等）解释任务上的严重不足，并提供了首个涵盖161项真实实验工作流任务的评测基准。
🔗 http://arxiv.org/abs/2608.21357v1

### AI with Authority, from Application to Silicon
📄 这篇论文的核心贡献在于，通过“Salt 方法”证明了生成式 AI 能够以自主、可验证的方式（从应用层到芯片流片）全面驱动机器工作，并首次实现由 AI 编写全部代码、且无需人类审查证明的完整 RISC-V 芯片设计流程，从而将机器验证从昂贵负担转变为支撑单人在大规模自主工作中可信赖的“裁判”，开启了“AI 主导硬件与软件可信生产”的新范式。
🔗 http://arxiv.org/abs/2608.21356v1
