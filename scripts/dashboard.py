import os
import json
import sys

def main():
    # 1. 环境与文件准备
    history_file = "run_history.jsonl"
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    
    if not summary_file:
        print("非 GitHub Actions 环境，跳过看板生成。")
        return

    content = ["### 🏭 工厂运行看板 (L4 Frozen)"]
    
    if not os.path.exists(history_file):
        content.append("> ⚠️ 暂无历史数据，等待首次运行...")
        write_summary(summary_file, content)
        return

    # 2. 读取数据 (带容错)
    lines = []
    try:
        with open(history_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        lines.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue 
    except Exception as e:
        content.append(f"> ❌ 读取失败: {e}")
        write_summary(summary_file, content)
        return

    if not lines:
        content.append("> ⚠️ 历史记录为空。")
        write_summary(summary_file, content)
        return

    # 3. 计算核心指标 (Python 原生计算，精准且不报错)
    recent_7 = lines[-7:]
    run_count = len(recent_7)
    fallback_count = sum(1 for r in recent_7 if r.get("fallback_used", False))
    total_tokens = sum(r.get("total_tokens", 0) for r in recent_7)
    est_cost = (total_tokens / 1_000_000) * 2.0  # 假设 ¥2.00 / 1M tokens
    
    # 4. 生成趋势表格
    content.append("| 维度 | 统计 (近7次) | 状态 |")
    content.append("| :--- | :--- | :--- |")
    content.append(f"| **总运行** | {run_count} 次 | 🟢 Active |")
    content.append(f"| **降级率** | {fallback_count} 次 | {'🟢 0%' if fallback_count == 0 else '🟡 波动'} |")
    content.append(f"| **总消耗** | {total_tokens} Tokens | 💰 ¥{est_cost:.4f} |")
    
    content.append(f"\n> 📝 最近一次运行时间: {lines[-1].get('timestamp', 'N/A')[:16]}")

    # 5. 输出
    write_summary(summary_file, content)

def write_summary(filepath, lines):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
