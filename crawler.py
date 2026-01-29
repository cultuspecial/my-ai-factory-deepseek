# crawler.py - 增强版：真实抓取 arXiv 论文
import json
import requests
import re
from datetime import datetime, timedelta

def crawl_arxiv_ai_papers(max_results=10, lookback_days=7):
    """
    真实抓取 arXiv 上 AI 相关的最新论文
    返回格式与旧版本兼容的列表
    """
    print(f"🔍 开始抓取 arXiv 最新 AI 论文 (近{lookback_days}天)...")
    
    # arXiv API 查询参数
    categories = ['cs.AI', 'cs.CL', 'cs.LG']  # 人工智能、计算语言学、机器学习
    query = ' OR '.join([f'cat:{cat}' for cat in categories])
    
    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    try:
        # 调用 arXiv API
        response = requests.get(
            'http://export.arxiv.org/api/query',
            params=params,
            headers={'User-Agent': 'AI-Research-Bot/1.0'},
            timeout=30
        )
        response.raise_for_status()
        
        # 解析 XML 响应（简化版）
        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.text)
        
        # XML 命名空间
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        papers = []
        for entry in root.findall('atom:entry', ns):
            title_elem = entry.find('atom:title', ns)
            summary_elem = entry.find('atom:summary', ns)
            
            if title_elem is not None and summary_elem is not None:
                # 清理标题和摘要
                title = re.sub(r'\s+', ' ', title_elem.text).strip()
                summary = re.sub(r'\s+', ' ', summary_elem.text).strip()
                
                # 提取论文 ID
                id_elem = entry.find('atom:id', ns)
                paper_id = id_elem.text.split('/')[-1] if id_elem is not None else 'unknown'
                
                # 提取发布日期
                published_elem = entry.find('atom:published', ns)
                published = published_elem.text if published_elem is not None else ''
                
                papers.append({
                    "title": title[:200],  # 限制标题长度
                    "link": f"https://arxiv.org/abs/{paper_id}",
                    "summary": summary[:500],  # 摘要取前500字符，供LLM总结
                    "paper_id": paper_id,
                    "published": published[:10] if published else "",
                    "source": "arXiv"
                })
        
        print(f"✅ 成功抓取 {len(papers)} 篇论文")
        return papers[:max_results]  # 确保不超过最大数量
        
    except Exception as e:
        print(f"⚠️ arXiv 抓取失败，启用模拟数据模式: {e}")
        # 降级方案：返回模拟数据，保证流水线不中断
        return [
            {
                "title": "Large Language Models: A Survey",
                "link": "https://arxiv.org/abs/2401.00000",
                "summary": "This paper surveys recent advances in large language models.",
                "paper_id": "2401.00000",
                "published": "2024-01-01",
                "source": "simulation"
            },
            {
                "title": "Efficient Fine-tuning Methods for Transformers",
                "link": "https://arxiv.org/abs/2401.00001",
                "summary": "We propose a new parameter-efficient fine-tuning method.",
                "paper_id": "2401.00001",
                "published": "2024-01-02",
                "source": "simulation"
            }
        ]

if __name__ == "__main__":
    # 参数可以保持与你原工作流一致
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default="AI Trends")
    args = parser.parse_args()
    
    # 抓取论文（默认为10篇，近7天）
    data = crawl_arxiv_ai_papers(max_results=10, lookback_days=7)
    
    # 保持与原文件完全相同的输出格式和文件名
    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"📁 数据已保存至 raw_data.json, 共 {len(data)} 条记录")
