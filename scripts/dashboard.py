import os, json

def main():
    history_file = "run_history.jsonl"
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file: return

    content = ["### 🏭 工厂运行看板 (L4+ 监控版)"]
    if not os.path.exists(history_file):
        with open(summary_file, "a") as f: f.write("等待首次运行...") 
        return

    lines = []
    with open(history_file, "r") as f:
        for l in f:
            try: lines.append(json.loads(l))
            except: continue

    recent_7 = lines[-7:]
    # 核心指标计算
    total_tokens = sum(r.get("total_tokens", 0) for r in recent_7)
    retry_count = sum(r.get("retry_count", 0) for r in recent_7)
    est_cost = (total_tokens / 1_000_000) * 2.0

    # 重试趋势判断
    retry_trend = "➖"
    if len(recent_7) >= 6:
        new_3 = sum(r.get("retry_count", 0) for r in recent_7[-3:])
        old_3 = sum(r.get("retry_count", 0) for r in recent_7[-6:-3])
        if new_3 > old_3: retry_trend = "📈 压力上升"
        elif new_3 < old_3: retry_trend = "📉 趋于稳定"

    content.append("| 维度 | 统计 (7日) | 状态/趋势 |")
    content.append("| :--- | :--- | :--- |")
    content.append(f"| **Token 消耗** | {total_tokens} | 💰 ¥{est_cost:.4f} |")
    content.append(f"| **重试压力** | {retry_count} | {retry_trend} |")
    content.append(f"| **运行记录** | {len(lines)} 次 | 🟢 持续生产中 |")
    
    with open(summary_file, "a") as f: f.write("\n".join(content) + "\n")

if __name__ == "__main__": main()

    main()
