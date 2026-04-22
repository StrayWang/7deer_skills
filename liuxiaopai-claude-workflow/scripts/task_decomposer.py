# 任务分解器：将大需求拆分为可执行的最小单元
# 文件路径：liuxiaopai-claude-workflow/scripts/task_decomposer.py

import anthropic
import json
import os

client = anthropic.Anthropic()

DECOMPOSE_PROMPT = """
你是一位经验丰富的技术项目经理。

请将以下需求拆解为独立的开发任务，每个任务必须满足：
1. 单一职责（只做一件事）
2. 可独立测试（完成后能验证效果）
3. 完成时间 < 2小时（如果超过，继续拆分）
4. 有明确的完成标准

需求：{requirement}
技术栈：{tech_stack}

输出格式（JSON）：
{{
  "tasks": [
    {{
      "id": 1,
      "name": "任务名称",
      "description": "具体做什么",
      "acceptance": "完成标准",
      "estimated_hours": 1,
      "dependencies": []
    }}
  ],
  "total_estimated_hours": 8,
  "critical_path": [1, 2, 3]
}}
"""

def decompose_requirement(requirement: str, tech_stack: str) -> dict:
    """将需求文档拆解为可执行任务列表"""
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": DECOMPOSE_PROMPT.format(
                    requirement=requirement,
                    tech_stack=tech_stack
                )
            }]
        )
        
        response_text = message.content[0].text
        # 尝试提取 JSON 块（以防模型输出额外文本）
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "{" in response_text:
            response_text = response_text[response_text.find("{"):response_text.rfind("}")+1]
            
        return json.loads(response_text)
    except Exception as e:
        return {"error": str(e), "raw_output": locals().get('response_text', '')}


if __name__ == "__main__":
    req = "开发一个 AI 图片生成工具，用户输入文字描述，调用 DALL-E API 生成图片，可以下载"
    stack = "Next.js 14 + Python FastAPI + Supabase"
    
    result = decompose_requirement(req, stack)
    
    if "tasks" in result:
        print(f"✅ 任务拆解完成，共 {len(result['tasks'])} 个任务")
        print(f"预计总工时：{result['total_estimated_hours']} 小时")
        print("\n任务列表：")
        for task in result["tasks"]:
            print(f"  [{task['id']}] {task['name']} ({task['estimated_hours']}h)")
            print(f"       完成标准：{task['acceptance']}")
    else:
        print("❌ 拆解失败：")
        print(json.dumps(result, indent=2, ensure_ascii=False))
