---
name: ai-site-architect
description: AI 工具与服务站的 SEO 架构规范。包含分类层级、详情页结构、聚合页逻辑和内链策略。
keywords: ai site, site architecture, seo, taxonomies, internal linking
---

# 🏗️ AI Site Architect (ASA) Protocol

**Role**: SEO Architect (流量架构师)
**Core Function**: 快速构建符合工业标准的 AI 工具与服务站点。

## When This Skill Applies
*   当需要生成 `game.config.json` 或设计站点架构时。

## Instructions

### 1. 核心方法论 (The Theory)

#### 1.1 三层架构模型 (The 3-Layer Architecture)
所有站点必须遵循以下分层，以实现 80% 的代码复用：
*   **Layer 1: 核心层 (Core)**: 100% 复用的基础设施 (Next.js, Sitemap, CF Pages)。
*   **Layer 2: 主题层 (Theme)**: `ai-tool.config.json` 驱动的 UI 风格。
*   **Layer 3: 特性层 (Feature)**: 工具特异性功能（如 API 聚合、提示词库）。

#### 1.2 关键词布局策略 (Keyword Strategy)
*   **Hub**: 首页及一级导航 (Categories, Best Tools, Use Cases)。
*   **Spoke (PSEO)**: 批量生成的实体页 (AI Tool Profiles, Comparison Pages)。
*   **Trending**: 注入 `TOOL_VERSION` 变量 (e.g., "Updated for 2026")。

### 2. 实操落地指南 (Actionable Instructions)

#### Step 1: 建立配置源
创建 `data/game.config.json` 是第一步。
```json
{
  "seo": { "toolName": "Jasper AI", "version": "v2.0" },
  "routes": [{ "path": "/codes", "keyword": "codes" }]
}
```

#### Step 2: 实现 PSEO 动态页
*   Data: `data/items.ts`
*   Route: `app/items/[slug]/page.tsx`
*   Metadata: 动态生成 Title/Description

#### Step 3: 部署自动化内容管线 (The Gemini Loop)
不要手动写 Blog。
*   **Source**: YouTube 视频。
*   **Process**: 使用 `youtube-content-gen` 技能每天自动生成。
*   **Goal**: 保持 "Content Velocity"。

### 3. Verification
*   检查是否所有 Hub 页面都存在。
*   检查 PSEO 页面是否生成了正确的 Sitemap。
