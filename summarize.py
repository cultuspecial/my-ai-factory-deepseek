# summarize.py - 增强版：真实调用 DeepSeek API 总结论文
import datetime
import json
import os
import sys
import time

def call_deepseek_api(prompt, api_key, base_url="https://api.deepseek.com"):
    """
    调用 DeepSeek API（兼容 Chat Completions 格式）
    返回 (response_text, total_tokens, success)
    """
    import requests
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一位AI研究助理，负责从论文摘要中提取核心信息。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        response.raise_for_status()
        result = response.json()
        
        # 提取回复内容和 token 使用量
        reply = result["choices"][0]["message"]["content"]
        total_tokens = result.get("usage", {}).get("total_tokens", 0)
        
        return reply, total_tokens, True
        
    except Exception as e:
        print(f"❌ DeepSeek API 调用失败: {e}")
        return f"API调用失败: {e}", 0, False

def record_meta(topic, success, fallback, retries, content, tokens=0):
    """
    保持与你原版完全相同的元数据记录函数
    """
    meta = {
        "timestamp": datetime.datetime.now().isoformat(),
        "topic": topic,
        "llm_success": success,
        "fallback_used": fallback,
        "retry_count": retries,
        "content_length": len(content),
        "total_tokens": tokens, 
        "status": "HEALTHY" if success and not fallback else "DEGRADED"
    }
    
    with open("run_history.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    
    return meta

def generate_report():
    """
    核心业务逻辑：读取抓取的论文，调用 API 总结，记录元数据
    """
    # 1. 读取 crawler.py 生成的数据
    try:
        with open("raw_data.json", "r", encoding="utf-8") as f:
            papers = json.load(f)
    except FileNotFoundError:
        print("❌ 未找到 raw_data.json，请先运行 crawler.py")
        record_meta("Error", False, False, 0, "raw_data.json not found", 0)
        return
    
    if not papers:
        print("⚠️ raw_data.json 为空，使用模拟数据")
        papers = [{"title": "AI Trends", "summary": "No data available."}]
    
    # 2. 从环境变量获取 API 配置（与你的 workflow.yml 完全一致）
    api_key = os.environ.get("LLM_API_KEY")
    base_url = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com")
    
    if not api_key:
        print("❌ 未设置 LLM_API_KEY 环境变量")
        record_meta("Config Error", False, False, 0, "API key not configured", 0)
        return
    
    # 3. 处理每一篇论文（示例：处理前2篇）
    all_summaries = []
    total_tokens_used = 0
    success_count = 0
    
    for i, paper in enumerate(papers[:2]):  # 先处理2篇，控制成本
        print(f"📝 处理论文 {i+1}/{min(2, len(papers))}: {paper['title'][:50]}...")
        
        # 构建提示词
        prompt = f"""请总结以下学术论文的核心贡献：

标题：{paper.get('title', 'N/A')}
摘要：{paper.get('summary', 'N/A')}

请用中文提供：
1. 研究目标（1句话）
2. 核心方法（1-2句话）
3. 主要发现（1-2句话）
4. 潜在影响（1句话）"""
        
        # 调用 API
        summary, tokens, success = call_deepseek_api(prompt, api_key, base_url)
        
        if success:
            success_count += 1
            total_tokens_used += tokens
            all_summaries.append({
                "title": paper.get("title", "Untitled"),
                "summary": summary,
                "tokens": tokens
            })
            print(f"   ✅ 总结成功，消耗 {tokens} tokens")
        else:
            print(f"   ❌ 总结失败，使用备用摘要")
            # 降级：使用简单摘要
            all_summaries.append({
                "title": paper.get("title", "Untitled"),
                "summary": f"论文摘要：{paper.get('summary', '')[:100]}...",
                "tokens": 0
            })
    
    # 4. 生成最终报告内容
    if all_summaries:
        report_content = "# AI 论文研究简报\n\n"
        report_content += f"*生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
        report_content += f"*分析论文数：{len(all_summaries)}*\n"
        report_content += f"*成功总结：{success_count}篇*\n"
        report_content += f"*总 Token 消耗：{total_tokens_used}*\n\n"
        
        for item in all_summaries:
            report_content += f"## {item['title']}\n"
            report_content += f"{item['summary']}\n\n"
            report_content += f"*Tokens: {item['tokens']}*\n\n---\n\n"
        
        # 5. 保存报告文件
        with open("ai_research_report.md", "w", encoding="utf-8") as f:
            f.write(report_content)
        
        print(f"📄 报告已保存至 ai_research_report.md")
        
        # 6. 记录元数据（与你的历史记录格式完全兼容）
        meta = record_meta(
            topic="AI Research Papers",
            success=success_count > 0,
            fallback=success_count < len(all_summaries),
            retries=0,
            content=report_content[:100] + "...",  # 只存开头部分
            tokens=total_tokens_used
        )
        
        print(f"✅ 成功记录元数据，本次消耗 {total_tokens_used} tokens")
    else:
        print("❌ 未生成任何总结")
        record_meta("AI Research Papers", False, True, 0, "No summaries generated", 0)

if __name__ == "__main__":
    generate_report()
