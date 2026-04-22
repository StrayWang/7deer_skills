# 上下文管理器：防止 Agent 在长对话中「失忆」
# 文件路径：liuxiaopai-claude-workflow/scripts/context_manager.py

import json
from pathlib import Path
from datetime import datetime

class AgentContextManager:
    """
    刘小排「代码屎山预防」上下文管理器
    
    核心思路：
    - 每个功能模块独立的上下文文件
    - 定期生成「当前状态摘要」供 Agent 快速恢复上下文
    - 关键决策记录存档，避免 Agent 反复询问同一问题
    """
    
    def __init__(self, project_name: str, context_dir: str = ".agent/context"):
        self.project_name = project_name
        self.context_dir = Path(context_dir)
        self.context_dir.mkdir(parents=True, exist_ok=True)
        
    def save_decision(self, decision_type: str, content: dict):
        """记录关键决策（技术选型、架构决定等）"""
        decisions_file = self.context_dir / "decisions.json"
        
        decisions = []
        if decisions_file.exists():
            try:
                with open(decisions_file, 'r', encoding='utf-8') as f:
                    decisions = json.load(f)
            except json.JSONDecodeError:
                decisions = []
        
        decisions.append({
            "timestamp": datetime.now().isoformat(),
            "type": decision_type,
            "content": content
        })
        
        with open(decisions_file, 'w', encoding='utf-8') as f:
            json.dump(decisions, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 决策已记录：{decision_type}")
    
    def generate_status_summary(self, completed_tasks: list, current_task: str, blockers: list = None) -> str:
        """
        生成当前项目状态摘要
        在每次新开对话时，将此摘要粘贴给 Agent，快速恢复上下文
        """
        summary = f"""
# {self.project_name} — 当前状态摘要
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}

## 已完成
{chr(10).join(f'- ✅ {task}' for task in completed_tasks)}

## 当前任务
- 🔄 {current_task}

## 阻塞项
{chr(10).join(f'- ⚠️  {b}' for b in (blockers or [])) or '- 无'}

## 关键决策记录
"""
        decisions_file = self.context_dir / "decisions.json"
        if decisions_file.exists():
            try:
                with open(decisions_file, 'r', encoding='utf-8') as f:
                    decisions = json.load(f)
                for d in decisions[-5:]:  # 只显示最近5条
                    summary += f"- [{d['type']}] {json.dumps(d['content'], ensure_ascii=False)}\n"
            except:
                summary += "- (无法加载决策记录)\n"
        
        # 保存摘要文件
        summary_file = self.context_dir / "latest_summary.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        return summary


if __name__ == "__main__":
    # 使用示例
    ctx = AgentContextManager("AI Logo Generator")
    
    # 记录技术选型决策
    ctx.save_decision("tech_stack", {
        "frontend": "Next.js 14",
        "reason": "团队熟悉，Vercel 部署方便"
    })
    
    # 生成状态摘要（每次开新对话前执行）
    summary = ctx.generate_status_summary(
        completed_tasks=["项目初始化", "用户登录功能", "图片上传功能"],
        current_task="接入 DALL-E API 生成图片",
        blockers=["DALL-E API Key 还未申请"]
    )
    
    print("📋 状态摘要已生成，请在新对话开始时粘贴给 Agent：")
    print(summary)
