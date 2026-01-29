import json
import os

def generate_summary():
    print("### 🏭 工厂运行简报")
    print("")
    
    history_file = "run_history.jsonl"
    if not os.path.exists(history_file):
        print("**状态**: 🟡 等待首次运行数据积累")
        return

    try:
        with open(history_file, 'r', encoding='utf-8') as f:
            lines = [json.loads(line.strip()) for line in f if line.strip()]
        
        if not lines:
            print("**状态**: 🟡 历史记录为空")
            return

        last_run = lines[-1]
        total_tokens = sum(r.get('total_tokens', 0) for r in lines)
        cost_cny = (total_tokens / 1000000) * 2.0  # 假设 2元/M tokens
        
        status_icon = "🟢 健康" if last_run.get('status') == "HEALTHY" else "🟡 降级"
        
        print(f"**最近运行**: {last_run.get('timestamp', 'N/A')[:19]}")
        print(f"**累计运行**: {len(lines)} 次")
        print(f"**累计消耗**: {total_tokens} Tokens")
        print(f"**预估成本**: ¥{cost_cny:.4f}")
        print(f"**当前状态**: {status_icon}")
        print("\n> 💡 提示：完整报告已生成 `ai_research_report.md`，历史数据见 `run_history.jsonl`。")
        
    except Exception as e:
        print(f"生成看板时出错: {e}")

if __name__ == "__main__":
    generate_summary()
