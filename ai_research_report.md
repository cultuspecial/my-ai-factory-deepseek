# AI 简报 (2026-10-31)

### Rethinking Neural Thickets Without Weight Perturbations
📄 论文表明神经网络“厚块”假设所依赖的随机权重扰动所带来的性能提升，其实无需该几何解释——仅扰动单个解码块、甚至完全冻结模型并给输出logits加随机偏置即可达到相当甚至更好效果，从而提出基于输出多样性、验证集选择和投票的“扰动-选择-投票”（PSV）替代解释。
🔗 http://arxiv.org/abs/2610.40649v1

### Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers
📄 SpecSlot 通过将每个空间锚点扩展为多个分别承载不重叠 DCT 频带的槽位，并仅让最低频槽位参与全局注意力、其余槽位局部建模，从而在像素空间生成 Transformer 中实现输出细节与全局注意力序列长度的解耦。
🔗 http://arxiv.org/abs/2610.40647v1

### Luggage re-identification: A study of strategies towards a real-world application
📄 论文研究了行李重识别在真实应用场景中的策略，重点利用多镜头和多视角视频信息的互补性来应对遮挡、背景杂乱和拥挤等挑战。
🔗 http://arxiv.org/abs/2610.40643v1
