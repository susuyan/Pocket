# Guide

## 目录
- 常见问题
- 进阶技巧
- 最佳实践
- 验证清单

## 常见问题

### Q1: 如何处理付费墙内容?
标注"需订阅"或"付费内容",仍提取可见的标题和描述。

```markdown
- [高级架构模式](https://premium.example.com/post) — 🔒 需订阅
- 探讨企业级应用的架构设计模式
```

### Q2: 链接同时包含多个价值点,如何归类?
选择主要价值归类,其他价值在描述中体现。

```markdown
## 🛠️ Tools

- [Cursor](https://cursor.com) — AI-powered code editor
- 内置 agent 模式,支持 multi-file 重构(详见官方教程)
```

### Q3: 如何处理系列文章?
每篇单独提取,或提取系列入口页。

**选项 1: 单独提取**
```markdown
- [深入理解 React (1/3)](https://example.com/part1)
- [深入理解 React (2/3)](https://example.com/part2)
- [深入理解 React (3/3)](https://example.com/part3)
```

**选项 2: 提取系列入口**
```markdown
- [深入理解 React 系列](https://example.com/react-series)
- 三篇系列文章,涵盖核心概念、Hooks 和性能优化
```

### Q4: 相关链接过多怎么办?
只保留最相关的 3-5 个,避免信息过载。

### Q5: 如何处理非英文内容?
中文内容保持中文描述;日文/韩文等可翻译为中文或保留原文+中文注释。

```markdown
- [React 完全指南](https://qiita.com/example) (日文)
- React の基本から応用まで — React 从基础到进阶的完整指南
```

## 进阶技巧

### 技巧 1: 使用别名简化引用
```markdown
- [TCA][tca] — Swift 组合式架构库

  关键词: [Swift][swift], [Composable][tca]

[tca]: https://github.com/pointfreeco/swift-composable-architecture
[swift]: https://swift.org
```

### 技巧 2: 组合样式
对于复杂内容,可组合多种样式:

```markdown
## 📘 Read This

- [**Building Production-Ready AI Apps**](https://example.com/ai-apps) — 来自 [OpenAI team](https://openai.com)
  **Complete guide for deploying AI applications at scale**

  - Architecture patterns: microservices, event-driven
  - Monitoring & observability: logging, tracing
  - Cost optimization: caching, batch processing

  相关: [Langchain][ref1]

[ref1]: https://langchain.com
```

### 技巧 3: 添加上下文标签
```markdown
## 🛠️ Tools

- 🆕 [新工具名称](https://example.com) — 刚发布的工具
- 🔥 [热门工具](https://example.com) — HN 热榜第一
- 📌 [核心依赖](https://example.com) — 项目必备
```

## 最佳实践

### 1. 描述撰写原则
- **简洁**: ≤120 字符,避免冗余
- **客观**: 陈述事实,不加主观评价
- **核心价值**: 突出"为什么值得阅读/使用"
- **支持 Markdown**: 可使用加粗、斜体强调关键词

### 2. 关键词提取
- **相关性**: 只标注与内容直接相关的技术/概念
- **数量**: 3-5 个,不要过多
- **格式**: 使用 `[关键词][ref]` 格式
- **去重**: 同一关键词仅标注一次

### 3. 样式选择建议
```
GitHub 仓库         → GitHub Repo 样式
官方博客文章        → 官方博客样式
长文章(需深度)      → 要点式摘要
工具名称自解释      → 图标单行
其他              → 概念式(两行)
```

### 4. 分类决策
- 优先明确分类: 能确定的直接归类
- 模糊时看核心价值:
  - 重在"学习" → 📘 Read This
  - 重在"实践" → 🔧 Try This
  - 重在"使用" → 🛠️ Tools
  - 重在"收藏" → 🤓 Fav Finds

### 5. 归档维护
- **每日一文件**: 不跨日合并
- **保持一致性**: 同一板块使用相同样式
- **定期回顾**: 每周检查质量,调整分类

## 验证清单

提交归档前,检查以下项目:

- [ ] URL 有效,非 404
- [ ] 主链接正确,选择了最核心的资源
- [ ] 描述精准,≤120 字符,突出核心价值
- [ ] 分类合理,归入正确的板块
- [ ] 样式一致,同一板块使用统一样式
- [ ] 引用链接格式正确,无悬空引用
- [ ] 去重检查,同一 URL 当日仅出现一次
- [ ] 语言规范,中英混排得当
- [ ] 空板块已删除
- [ ] 板块间有分隔线 `---`
