# 创建 Daily Links

## 📖 概述
每日技术链接归档的结构化 Markdown 文档,统一分为六大板块。

## 📁 文件结构
```
docs/daily-links/
├── YYYY-MM-DD.md
└── ...
```

## 📄 标准模板

```markdown
# Daily Links YYYY-MM-DD

## 🪶 Remember This

## 🤓 Fav Finds

## 📘 Read This

## 🛠️ Tools

## 🔧 Try This

## 🎧 Listen To
```

## 📊 板块说明

| 板块 | 内容 | 适用样式 |
|------|------|---------|
| 🪶 Remember This | 箴言/原则(1-3条) | 概念式 |
| 🤓 Fav Finds | 当日最值得收藏 | 概念式/图标单行 |
| 📘 Read This | 文章/长文/官方博客 | 概念式/要点式/官方博客 |
| 🛠️ Tools | 产品/服务/CLI/代码仓库 | 图标单行/概念式/GitHub Repo |
| 🔧 Try This | 教程/实验/可实践方法 | 概念式/要点式 |
| 🎧 Listen To | 播客/音频 | 概念式 |

## ✍️ 格式规范

### 📌 基本规则
- 空板块直接删除(不留标题)
- 板块间用 `---` 分隔
- 同一 URL 当日仅出现一次
- 描述 ≤120 字符

### 💡 样式示例

**🔧 图标单行**(工具自解释):
```markdown
- 🔧 [Vercel AI SDK](https://sdk.vercel.ai)
```

**📝 概念式**(两行):
```markdown
- [MCP → SKILL 扩展机制](https://weibo.com/xxx)
- Split concerns: MCP standardizes connection, SKILL orchestrates workflow
```

**🏢 官方博客**:
```markdown
- [**Agent Best Practices**](https://cursor.com/blog) — 来自 [Cursor team](https://cursor.com)
- **明细说明:** Official guide for agent-based coding
```

**📦 GitHub Repo**:
```markdown
- [swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture)
- Swift 应用架构库,强调组合与可测试性

  **关键词:** [Swift][swift]

[swift]: https://swift.org
```

**📋 要点式**(长文章):
```markdown
- [Increasing Your Luck Surface Area](https://example.com/luck)
  **You can make your own luck** through passion and communication.

  - Pour energy into your passion
  - Tell more people
  - Luck is doing multiplied by telling
```

## 🎯 分类映射

```
内容类型                    → 目标板块
─────────────────────────────────────────
官方博客/技术文章            → 📘 Read This
开源项目/工具/产品           → 🛠️ Tools
方法论/思考/原则             → 🤓 Fav Finds 或 🪶 Remember This
教程/实验/代码示例           → 🔧 Try This
播客/音频内容               → 🎧 Listen To
值得深挖的生态资源           → 🤓 Fav Finds
```

## 🔄 去重策略
- 同一 URL 当日仅记录一次
- 重复出现时合并来源信息
- 保留最完整的上下文

## ➕ 新增板块
1. 在模板中添加标题与图标
2. 在 [categories.md](categories.md) 定义映射与样式
3. 如需专用样式,在 references 目录新增样式文档
