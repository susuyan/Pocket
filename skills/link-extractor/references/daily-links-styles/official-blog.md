# 官方博客

适用: 官方团队发布的博客/公告,标题已清晰传达主题

格式:
```markdown
- [**博客标题**](URL) — 来自 [官方团队名](团队主页)
- 明细说明: 补充说明(仅当标题不够清晰时)
```

示例:
```markdown
- [**Agent Best Practices**](https://cursor.com/cn/blog/agent-best-practices) — 来自 [Cursor team](https://cursor.com)
- 明细说明: Official guide for agent-based coding: long-run, multi-file refactors, test-driven iteration
```

官方团队名识别摘要:
- 判定“官方”: 主域与产品域一致或 `blog.` 子域; 已知官方域名映射
- 提取优先级: JSON-LD → og:site_name → 品牌区域 → meta author/twitter:site → 域名回退
- 特例: cursor.com → Cursor team; news.ycombinator.com → Y Combinator; *.github.io → owner TitleCase; medium.com/<pub> → TitleCase
