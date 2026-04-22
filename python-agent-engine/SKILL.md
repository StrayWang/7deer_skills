---
name: python-agent-engine
version: 1.1.0
description: A production-ready Python AI Agent engine using LangChain. Supports ReAct pattern, tool calling, and thinking process tracking.
---

# Python Agent Engine

A plug-and-play AI Agent core for Python applications. It handles the complexity of LLM interaction, tool calling loops, and context management.

## Features
- **ReAct Loop**: Automatically handles "Reasoning -> Tool Call -> Result -> Answer" process.
- **Thinking Process**: Returns structured "Thinking Steps" for UI visualization.
- **Model Agnostic**: Works with OpenAI, DeepSeek, or any OpenAI-compatible API.

## Installation

1. Copy `resources/agent_engine.py` to your project (e.g., `src/core/agent_engine.py`).
2. Install dependencies:
   ```bash
   pip install langchain-core langchain-openai python-dotenv
   ```
3. Set Environment Variables in your `.env` file:
   ```ini
   OPENAI_API_KEY=sk-...
   # Optional:
   OPENAI_BASE_URL=https://api.openai.com/v1
   ```

## Usage Example

```python
import asyncio
from langchain_core.tools import tool
from core.agent_engine import AgentEngine

# 1. Define Tools
@tool
def calculator(expression: str) -> str:
    """Calculates a math expression."""
    return str(eval(expression))

# 2. Initialize Agent
agent = AgentEngine(
    tools=[calculator],
    system_prompt="You are a helpful math assistant.",
    model_name="gpt-4o"
)

# 3. Chat
async def main():
    response = await agent.chat("What is 123 * 456?")
    
    print(f"Answer: {response.content}")
    print("\nThinking Steps:")
    for step in response.thinking_steps:
        print(f"[{step.type}] {step.content}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🆕 v1.1 新增：刘小排「Claude Code 协作」最佳实践

> 来源：刘小排（Claude Code token 消耗榜一大哥）实战总结

### 三条铁律

**铁律 #1：需求文档先行，禁止直接在对话框打字**

在调用任何 Agent 之前，先准备结构化需求文档：

```python
# 需求文档结构验证器
# 文件路径：liuxiaopai-claude-workflow/scripts/validate_requirements.py

import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class RequirementsDoc:
    """刘小排需求文档标准格式"""
    background: str           # 产品背景（目标用户 + 核心痛点）
    core_features: List[str]  # 核心功能列表（MVP 必须有）
    tech_stack: dict          # 技术约束
    acceptance_criteria: List[str]  # 验收标准
    references: Optional[List[str]] = None  # 参考竞品

def validate_requirements(doc: dict) -> tuple[bool, List[str]]:
    """
    验证需求文档是否完整
    返回：(是否通过, 缺失项列表)
    """
    required_fields = {
        "background": "产品背景（目标用户 + 核心痛点）",
        "core_features": "核心功能列表",
        "tech_stack": "技术栈约束",
        "acceptance_criteria": "验收标准",
    }
    
    missing = []
    for field, description in required_fields.items():
        if field not in doc or not doc[field]:
            missing.append(f"缺少：{description}（字段：{field}）")
    
    if "core_features" in doc and len(doc["core_features"]) > 5:
        missing.append("⚠️  核心功能超过 5 个，请精简 MVP 范围（刘小排原则：砍掉 80% 非必要功能）")
    
    is_valid = len(missing) == 0
    return is_valid, missing
```

**铁律 #2：分模块开发，每次只做一个功能**

```python
# 任务分解器：将大需求拆分为可执行的最小单元
# 文件路径：liuxiaopai-claude-workflow/scripts/task_decomposer.py

import anthropic

client = anthropic.Anthropic()

DECOMPOSE_PROMPT = """
你是一位经验丰富的技术项目经理。
请将以下需求拆解为独立的开发任务...
"""
# (详细实现见脚本文件)
```

**铁律 #3：上下文管理，避免代码屎山**

```python
# 上下文管理器：防止 Agent 在长对话中「失忆」
# 文件路径：liuxiaopai-claude-workflow/scripts/context_manager.py

import json
from pathlib import Path
# (详细实现见脚本文件)
```

### 多模型协作（参考刘小排「三模型协作」工作流）

```python
# 多模型协作路由器
# 文件路径：liuxiaopai-claude-workflow/scripts/multi_model_router.py

# 逻辑分工：
# - Claude：逻辑复杂度高、需要长上下文的任务
# - GPT Codex：代码审查、测试生成
# - Gemini：UI/UX 设计、前端实现
```

