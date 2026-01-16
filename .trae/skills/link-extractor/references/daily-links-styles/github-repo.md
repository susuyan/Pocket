# GitHub Repo

适用: GitHub 代码仓库(库/框架/工具/示例)

格式:
```markdown
- [仓库名称](仓库URL) — 仓库简要说明(可选)
```

提取规则:
- 仓库名称: 取 `owner/repo` 的 `repo`,保留大小写;或页面 H1/`og:title`
- 简要说明: 优先 `og:description`/页面描述;若无生成 1 句中文概要
- 当仓库名称足够表达功能时可省略说明

示例:
```markdown
- [swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) — Swift 应用架构库,强调组合与可测试性
- [awesome-tca](https://github.com/antranapp/awesome-tca)
```
