# scripts/generate_summary.py
import json, os, sys

def main():
    print("### 🏭 工厂运行简报")
    print()
    if not os.path.exists("run_history.jsonl"):
        print("**状态**: 🟡 等待首次运行完成")
        return

    try:
        with open('run_history.jsonl', 'r', encoding='utf-8') as f:
            lines = [json.loads(l.strip()) for l in f if l.strip()]
        if not lines:
            print("**状态**: 🟡 暂无有效数据")
            return
        last_run = lines[-1]
        total_runs = len(lines)
        total_tokens = sum(r.get('total_tokens', 0) for r in lines)
        estimated_cost_cny = (total_tokens / 1_000_000) * 2.0
        status_text = {'HEALTHY':'🟢 健康', 'DEGRADED':'🟡 降级'}.get(last_run.get('status'), '🔴 失败')
        print(f"**最近运行时间**: {last_run.get('timestamp', 'N/A')[:19]}")
        print(f"**累计运行次数**: {total_runs}")
        print(f"**累计Token消耗**: {total_tokens}")
        print(f"**预估总成本**: ¥{estimated_cost_cny:.4f}")
        print(f"**上次状态**: {status_text}")
        print()
        print("> 💡 提示：完整报告已生成 `ai_research_report.md`，历史数据详见 `run_history.jsonl`。")
    except Exception as e:
        print(f"生成看板时出错: {e}")
if __name__ == "__main__":
    main()
