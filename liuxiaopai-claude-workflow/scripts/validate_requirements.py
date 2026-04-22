# 需求文档结构验证器
# 文件路径：liuxiaopai-claude-workflow/scripts/validate_requirements.py

import json
from dataclasses import dataclass, asdict
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


if __name__ == "__main__":
    # 示例：验证需求文档
    sample_doc = {
        "background": "目标用户：独立开发者。痛点：手动生成 favicon 耗时且效果差",
        "core_features": [
            "输入文字或上传图片，生成 favicon",
            "支持导出 PNG/SVG/ICO 格式",
            "一键生成 PWA 所需全尺寸图标集",
        ],
        "tech_stack": {
            "frontend": "Next.js 14",
            "backend": "Python FastAPI",
            "deploy": "Vercel"
        },
        "acceptance_criteria": [
            "生成时间 < 5 秒",
            "支持移动端",
            "导出文件可直接用于生产环境",
        ]
    }
    
    is_valid, issues = validate_requirements(sample_doc)
    if is_valid:
        print("✅ 需求文档验证通过，可以开始开发")
    else:
        print("❌ 需求文档不完整，请补充以下内容：")
        for issue in issues:
            print(f"  - {issue}")
