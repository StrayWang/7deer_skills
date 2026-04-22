# 多模型协作路由器（参考刘小排「三模型协作」工作流）
# 文件路径：liuxiaopai-claude-workflow/scripts/multi_model_router.py

from enum import Enum
from typing import Tuple

class TaskType(Enum):
    LOGIC_HEAVY = "logic"        # 复杂逻辑、长上下文 → Claude
    CODE_REVIEW = "review"       # 代码审查、单元测试 → GPT Codex  
    UI_DESIGN = "ui"             # 界面设计、前端代码 → Gemini

def route_task(task_description: str) -> Tuple[TaskType, str]:
    """
    根据任务描述自动路由到最合适的模型
    返回：(任务类型, 推荐模型)
    """
    task_lower = task_description.lower()
    
    ui_keywords = ["界面", "ui", "前端", "样式", "css", "tailwind", "组件", "布局", "设计", "layout", "visual"]
    review_keywords = ["审查", "review", "测试", "test", "bug", "修复", "检查代码", "audit", "security"]
    
    if any(kw in task_lower for kw in ui_keywords):
        return TaskType.UI_DESIGN, "Gemini 2.5 Pro — 多模态 UI 设计与前端代码生成能力强"
    elif any(kw in task_lower for kw in review_keywords):
        return TaskType.CODE_REVIEW, "GPT-4o / Codex — 代码审查与逻辑自洽性检查速度快"
    else:
        return TaskType.LOGIC_HEAVY, "Claude 3.5 Sonnet / Opus — 长上下文逻辑推理与系统架构能力强"


if __name__ == "__main__":
    test_tasks = [
        "实现用户登录的 JWT 鉴权逻辑",
        "设计首页的 Hero Section 布局",
        "审查支付模块的代码，检查安全漏洞",
        "调研 3 个开源 3D 模型库的性能差异",
    ]
    
    print("任务路由结果：\n")
    for task in test_tasks:
        task_type, model = route_task(task)
        print(f"📌 任务：{task}")
        print(f"   → 推荐模型：{model}\n")
