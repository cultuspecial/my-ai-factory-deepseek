import json
import os
import datetime
import requests

def call_llm(prompt):
    api_key = os.environ.get("LLM_API_KEY")
    base_url = os.environ.get("LLM_BASE_URL")
    provider = os.environ.get("LLM_PROVIDER", "openrouter")  # 明确冻结

    if not api_key or not base_url:
        return "Error: Missing LLM config", 0, False

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        if provider == "openrouter":
            model = "google/gemini-2.0-flash-exp:free"
        elif provider == "deepseek":
            model = "deepseek-chat"
        else:
            return "Unknown provider", 0, False

        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }

        resp = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=40
        )
        resp.raise_for_status()

        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        tokens = data.get("usage", {}).get("total_tokens", 0)

        return content, tokens, True

    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return f"生成失败: {e}", 0, False


def main():
    if not os.path.exists("raw_data.json"):
        return

    with open("raw_data.json", "r") as f:
        papers = json.load(f)

    report = [f"# AI 简报 ({datetime.date.today()})\n"]
    total_tokens = 0
    fallback = False

    # 只处理前 3 篇，控制成本
    for paper in papers[:3]:
        prompt = f"一句话中文总结论文贡献：{paper['title']}\n摘要：{paper['summary']}"
        summary, tokens, success = call_llm(prompt)
        
        total_tokens += tokens
        if not success: fallback = True
        
        report.append(f"### {paper['title']}")
        report.append(f"📄 {summary}")
        report.append(f"🔗 {paper['link']}\n")

    # 1. 保存报告
    with open("ai_research_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    # 2. 记录核心资产
    meta = {
        "timestamp": datetime.datetime.now().isoformat(),
        "topic": "ArXiv AI",
        "fallback_used": fallback,
        "total_tokens": total_tokens,
        "status": "DEGRADED" if fallback else "HEALTHY"
    }
    with open("run_history.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(meta) + "\n")

if __name__ == "__main__":
    main()
