import json
import requests
import re

def crawl_arxiv():
    print("🔍 [Crawler] 正在连接 arXiv API...")
    # 抓取 AI 领域最新 5 篇论文
    url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=5&sortBy=submittedDate&sortOrder=descending"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # 使用正则提取，比 XML 库更轻量、更适合 CI 环境
        entries = re.findall(r'<entry>(.*?)</entry>', response.text, re.DOTALL)
        
        papers = []
        for entry in entries:
            title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
            summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
            link = re.search(r'<id>(.*?)</id>', entry, re.DOTALL)
            
            if title and summary:
                papers.append({
                    "title": title.group(1).strip().replace('\n', ' '),
                    "summary": summary.group(1).strip().replace('\n', ' ')[:800],
                    "link": link.group(1).strip() if link else "N/A"
                })
        
        print(f"✅ [Crawler] 成功抓取 {len(papers)} 篇论文")
        return papers

    except Exception as e:
        print(f"⚠️ [Crawler] 抓取失败: {e}")
        # 降级数据，保证 pipeline 不断
        return [{"title": "API Error Fallback", "summary": "Simulation data.", "link": "https://arxiv.org"}]

if __name__ == "__main__":
    data = crawl_arxiv()
    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
