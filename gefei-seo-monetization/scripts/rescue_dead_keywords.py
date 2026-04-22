# 哑炮词标题优化脚本
# 文件路径：gefei-seo-monetization/scripts/rescue_dead_keywords.py

import anthropic
import csv
import json
import os

client = anthropic.Anthropic()

TITLE_REWRITE_PROMPT = """
你是一位 SEO 专家，擅长撰写高点击率的页面标题。

当前页面信息：
- 原标题：{original_title}
- 目标关键词：{keyword}
- 当前展示次数：{impressions}
- 当前点击率：{ctr}%
- 竞争对手标题（SERP Top 3）：{competitor_titles}

请生成 3 个优化版标题，要求：
1. 关键词放在标题前半段
2. 包含数字或具体利益点
3. 长度 50~60 字符（英文）
4. 避免标题党，保持真实性

输出 JSON 格式：
{{"titles": ["标题1", "标题2", "标题3"], "reasoning": "优化逻辑说明"}}
"""

def rescue_dead_keywords(input_csv: str, output_json: str):
    """
    输入：从 GSC 导出的哑炮词 CSV
    输出：优化后的标题建议 JSON
    """
    results = []
    
    if not os.path.exists(input_csv):
        print(f"错误：找不到文件 {input_csv}")
        return []

    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 筛选条件：展示次数 > 100，CTR < 5%
            # 注意：CSV 里的列名可能因导出语言不同而异，这里按常见英文列名处理
            impressions = float(row.get('Impressions', 0))
            ctr_str = row.get('CTR', '0%').replace('%', '')
            ctr = float(ctr_str) if ctr_str else 0
            
            if impressions > 100 and ctr < 5:
                prompt = TITLE_REWRITE_PROMPT.format(
                    original_title=row.get('Page Title', ''),
                    keyword=row.get('Query', ''),
                    impressions=impressions,
                    ctr=ctr,
                    competitor_titles="（请手动填入 SERP 前3标题）"
                )
                
                try:
                    message = client.messages.create(
                        model="claude-3-5-sonnet-20241022", # 更新为可用模型
                        max_tokens=500,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    
                    response_text = message.content[0].text
                    try:
                        suggestion = json.loads(response_text)
                    except json.JSONDecodeError:
                        suggestion = {"titles": [response_text], "reasoning": "解析失败，请手动处理"}
                except Exception as e:
                    suggestion = {"titles": [], "reasoning": f"调用 API 失败: {str(e)}"}
                
                results.append({
                    "keyword": row.get('Query', ''),
                    "original_title": row.get('Page Title', ''),
                    "impressions": impressions,
                    "current_ctr": f"{ctr}%",
                    "suggested_titles": suggestion.get('titles', []),
                    "reasoning": suggestion.get('reasoning', '')
                })
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 处理完成，共 {len(results)} 个哑炮词，结果已保存到 {output_json}")
    return results


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("用法：python rescue_dead_keywords.py input.csv output.json")
    else:
        rescue_dead_keywords(sys.argv[1], sys.argv[2])
