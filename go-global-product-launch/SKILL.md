---
name: go-global-product-launch
description: 出海 AI 产品从 0 到盈利完整闭环。整合哥飞「SEO 免费流量」体系与刘小排「AI 产品开发」方法论。适用于独立开发者、小团队快速验证并上线出海 AI 工具站。
version: 1.0.0
author: 7deer
tags: [go-global, ai-product, seo, monetization, launch]
---

# go-global-product-launch — 出海 AI 产品完整闭环

## 核心公式

```
出海 AI 产品成功 = 精准需求 × 快速实现 × SEO 免费流量 × 变现路径
                    （刘小排）    （刘小排）    （哥飞）        （哥飞）
```

## 第一阶段：需求发现（1~3天）

### 哥飞「词找站 / 站找词」法

```
方法一：词找站（从关键词反推产品）
1. 在 Google Trends 搜索你感兴趣的领域
2. 找到搜索量上升的词（过去 90 天趋势向上）
3. 搜索这个词，看 SERP 前 10 结果
4. 如果前 10 全是内容页而非工具页 → 机会！做工具
5. 如果前 10 有工具但体验差 → 机会！做更好的工具

方法二：站找词（从竞品反推关键词）
1. 在 Similarweb 找一个月流量 10~100 万的竞品站
2. 查它的 Top Keywords（免费版可看 5 个）
3. 这 5 个词就是你的起点
4. 用 AnswerThePublic 扩展成 20~50 个长尾词
```

### 刘小排「需求验证」法

```
验证步骤（目标：3天内完成）：

Day 1：社区调研
- Reddit：搜索 r/[你的领域] + 关键词，看 upvote 最多的痛点帖
- Twitter/X：搜索「I wish there was a tool that...」+ 你的领域
- ProductHunt：看近期上线的相似产品，读 1星差评（真实痛点）

Day 2：竞品分析
- 列出 5 个竞品
- 每个竞品找 10 条 1~2 星差评
- 提炼共同痛点 → 这就是你的差异化方向

Day 3：付费意愿测试
- 在 Twitter 发一条帖：「我在做一个解决 [痛点] 的工具，有没有人感兴趣？」
- 收到 20+ 互动 → 继续
- 愿意留邮件的人 > 5 → 值得做 MVP
```

## 第二阶段：MVP 开发（3~7天）

### 刘小排「最小化实现」原则

```python
# MVP 功能清单模板
mvp_checklist = {
    "必须有（Day 1~3）": [
        "核心功能可以跑通（哪怕界面丑）",
        "用户可以使用（不需要登录也行）",
        "结果可以被分享（截图/链接）",
    ],
    "可以等（Day 4~7）": [
        "用户账号系统",
        "支付功能",
        "邮件通知",
    ],
    "上线后再做": [
        "移动端优化",
        "多语言",
        "API 接口",
    ]
}

# 刘小排的时间分配
time_allocation = {
    "核心功能开发": "60%",
    "UI 打磨": "20%",  # 够用就行，不要追求完美
    "测试": "15%",
    "部署": "5%",
}
```

### 技术栈推荐（刘小排实战验证）

```
前端：Next.js 14 (App Router) + Tailwind CSS + shadcn/ui
后端：Next.js API Routes 或 Python FastAPI
数据库：Supabase（免费额度够用）
AI 接口：Claude API / OpenAI API（按需选择）
部署：Vercel（免费）
支付：Stripe + Lemon Squeezy
域名：Namecheap / Cloudflare
```

## 第三阶段：SEO 布局（上线前准备，1~2天）

### 哥飞「上线即 SEO」原则

```markdown
# 技术 SEO 上线 Checklist

## 必须在上线前完成
- [ ] 每个页面有唯一的 <title>（含核心关键词）
- [ ] 每个页面有 <meta description>（150~160字符）
- [ ] 有 sitemap.xml（提交给 Google Search Console）
- [ ] 有 robots.txt
- [ ] 首页加载时间 < 3秒（用 PageSpeed Insights 测试）
- [ ] 移动端适配（Google 移动优先索引）
- [ ] 有 Open Graph 标签（社交分享时显示好看）

## 核心页面 SEO
- [ ] 首页：优化品牌词 + 核心功能词
- [ ] 功能页：每个功能对应一个独立页面（哥飞原则：一词一页）
- [ ] 博客/文章：至少 5 篇高质量内容（上线前准备）

## Schema 标记
- [ ] WebApplication Schema（工具站必加）
- [ ] FAQPage Schema（FAQ 区块）
- [ ] SoftwareApplication Schema（如果有评分）
```

## 第四阶段：上线与流量获取（上线后第1~4周）

```
Week 1：种子流量
- ProductHunt 发布（提前1周预热）
- Hacker News「Show HN」帖子
- 相关 Reddit 社区（r/SideProject / r/[你的领域]）
- Twitter/X 发布帖（@哥飞 @刘小排 这类 KOL 如果用了你的工具可以请求转发）

Week 2~4：SEO 内容启动
- 每周发布 2~3 篇围绕目标关键词的内容
- 哥飞原则：内容要有「信息增量」，不要重复别人已有的内容
- 格式优先：How-to、对比文章、工具评测（这三类最容易排名）

持续：外链建设
- 提交到 AI 工具目录（使用 backlink-discovery 技能）
- 寻找友链交换
- 写客座文章
```

## 第五阶段：变现路径选择

```
根据流量规模选择变现方式：

月 UV < 1万：
→ 优先 Adsense（门槛低，被动收入）
→ 同时收集邮件，为付费做准备

月 UV 1万~10万：
→ Adsense + Freemium（免费功能 + 付费高级功能）
→ 定价参考：$9~19/月（哥飞建议：定价不要太低，用户会觉得不值钱）

月 UV > 10万：
→ 订阅制为主，Adsense 为辅
→ 可以考虑 API 接口变现（开发者付费）
→ 企业版/白标授权

哥飞变现公式：
月收入 = (UV × Adsense RPM / 1000) + (UV × 付费转化率 × 月订阅价)
```

## 使用示例

```
用户输入：「我想做一个出海 AI 工具，不知道做什么方向」

Agent 执行流程：
1. 引导用户完成「词找站」调研（输出 5 个有机会的方向）
2. 对每个方向做需求验证评分（竞争度 × 市场规模 × 实现难度）
3. 推荐 Top 1 方向，生成 MVP 功能清单
4. 生成技术方案（技术栈 + 文件结构）
5. 生成 SEO 上线 Checklist
6. 生成上线后第一个月的流量获取计划
7. 计算预期收益（保守/中性/乐观三种情景）
```
