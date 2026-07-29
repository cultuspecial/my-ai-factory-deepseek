# AI 简报 (2026-07-29)

### Pass the Baton: Trajectory-Relayed On-Policy Distillation
📄 该论文提出**Relay-OPD方法**，通过检测学生模型推理失败前缀并让教师模型短暂接管生成“教师腿”来构建接力轨迹，从而缓解在线策略蒸馏中因持续错误方向导致的监督失效与计算浪费问题。
🔗 http://arxiv.org/abs/2607.26057v1

### $π\mathbf{R}^2$: Reactive Real-time Flow Policies
📄 论文贡献：提出 $\pi\mathbf{R}^2$ 框架，通过扩散强制的位置噪声调度机制，使基于大模型的动作分块流策略兼具实时反应能力与高表达力，解决了开环控制中感知延迟导致的动作过时问题，实现动态环境下的闭环控制。
🔗 http://arxiv.org/abs/2607.26055v1

### Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?
📄 论文贡献：提出**Desktop-Delta Bench (DDB)**，首个面向桌面GUI操作代理（CUA）的**离线、步骤级基准**，通过2013个人工验证的多应用Linux轨迹实例，系统性评估模型能否**正确识别动作引发的因果性GUI状态变化**（而非简单任务成功率或单帧定位），以解决异步环境中的状态误判与恢复失败问题。
🔗 http://arxiv.org/abs/2607.26041v1
