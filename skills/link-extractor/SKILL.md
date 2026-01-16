---
name: link-extractor
description: 从社交媒体(Weibo/X/Twitter/Reddit)、技术新闻(Hacker News)和博客文章中提取核心资源,生成结构化 Markdown 条目并自动归档到 Daily Links。支持多种输出样式(概念式/要点式/官方博客/GitHub Repo),智能分类到六大板块。触发关键词:weibo、twitter、x.com、reddit、news.ycombinator.com、博客链接、文章提取、daily links。
license: Apache-2.0
metadata:
  author: pocket
  version: "2.0"
  updated: "2026-01-16"
---

# Link Extractor

## 概述
Link Extractor 是一个智能链接提取与归档技能,专门用于从社交媒体、技术新闻和博客文章中提取核心资源,并生成结构化的 Markdown 文档。

## 目录
- 概述
- 支持平台
- 快速开始
- 核心功能概览
- References
- 推荐工作流

## 支持平台
- Weibo: weibo.com, m.weibo.cn
- X/Twitter: x.com, twitter.com
- Reddit: reddit.com
- Hacker News: news.ycombinator.com
- GitHub 仓库: github.com
- 博客/文章站点: 通用支持

## 快速开始
```bash
# 提取单个链接
link https://weibo.com/1648815335/Qn8iCfNyt

# 指定分类
link https://cursor.com/cn/blog/agent-best-practices "Read This"

# 指定分类与样式
link https://github.com/pointfreeco/swift-composable-architecture "Tools" "GitHub Repo"
```

---

## 核心功能概览

### 智能链接提取
- 提取逻辑: 识别平台 → 抓取正文/标题/描述/外链 → 展开短链 → 过滤无关资源
- 主链接优先级: GitHub 仓库 → 官方文档/主页 → 产品/工具页面 → 技术文章 → 被强调链接
- 输出样式选择: 概念式 / 要点式摘要 / 官方博客 / GitHub Repo / 图标单行
- 详见下文 References
- 社交媒体帖子优先提取被分享的资源


---

## References
- 分类与板块: ./references/categories.md
- 工作流程: ./references/workflow.md
- 决策树: ./references/decision-trees.md
- Guide(FAQ/最佳实践/验证清单/进阶技巧): ./references/guide.md
- 语言规则: ./references/language-rules.md
- 边界处理: ./references/edge-cases.md
- 使用示例: ./references/examples.md
- 创建 Daily Links: ./references/create-daily-links.md
- 输出样式:
  - 概念式(两行): ./references/daily-links-styles/concept-style.md
  - 要点式摘要: ./references/daily-links-styles/bullets-summary.md
  - 官方博客: ./references/daily-links-styles/official-blog.md
  - GitHub Repo: ./references/daily-links-styles/github-repo.md
  - 图标单行: ./references/daily-links-styles/icon-single-line.md


---


## **推荐工作流:**

1. 每日收集链接 → 2. 批量提取 → 3. 归档到 Daily Links → 4. 定期回顾优化
