# 边界处理

## 特殊场景处理

### 1. 链接失效(404/重定向)
**处理方式**:
- 标注链接状态
- 尝试通过 Wayback Machine 等归档服务查找
- 如果完全失效,仍可记录但标注"链接失效"

```markdown
- [已失效资源](https://example.com) — 🔒 链接失效,已归档到 Wayback Machine
- 原内容: XXX
```

### 2. 内容为空或极简
**处理方式**:
- 如果内容价值不高,跳过归档
- 如果有链接但无正文,仅记录链接作为参考

```markdown
- [分享资源列表](https://weibo.com/xxx)
- 未提供具体说明,包含 5 个链接,详见原帖
```

### 3. 同一资源多次出现
**处理方式**:
- 同一 URL 当日仅记录一次
- 保留最完整的描述和上下文
- 可在描述中提及来源

```markdown
- [重要工具](https://example.com/tool)
- 被 A、B、C 三方推荐,核心功能为 XXX
```

### 4. 长篇内容如何取舍
**处理方式**:
- 优先提取文章中的核心观点
- 识别并记录关键链接
- 使用要点式提炼主要信息
- 不追求完整总结,突出价值点

### 5. 视频/音频内容
**处理方式**:
- 记录标题和简介
- 标注内容类型(视频/音频)
- 提取描述中的关键信息
- 如有相关文章链接,一并记录

```markdown
- [AI 发展趋势视频](https://youtube.com/watch?v=xxx) — 📺 视频
- 深度解析 2024 年 AI 领域的三大突破,时长 45 分钟
```

### 6. 中文内容
**处理方式**:
- 保持原始中文描述
- 不强制翻译为英文
- 适当添加英文关键词便于检索

```markdown
- [微前端架构实践](https://example.com/micro-frontends)
- 分享微前端在企业级应用中的落地经验

  关键词: [Micro Frontends][mf], [Architecture][arch]

[mf]: https://micro-frontends.org
[arch]: https://martinfowler.com/architecture
```

### 7. 系列文章/专栏
**处理方式**:
- 系列入口页优先
- 或提取最新/最重要的一篇
- 标注系列信息

```markdown
- [深入理解 React 系列](https://example.com/react-series) — 3 篇
- 涵盖核心概念、Hooks 和性能优化
```

### 8. 广告/推广内容
**处理方式**:
- 识别明显的推广内容
- 如果内容本身有价值,仍可记录
- 描述中客观陈述,不带推广语

```markdown
- [新发布的 AI 工具](https://example.com)
- 提供 XXX 功能,支持 YYYY
```

### 9. 需要登录/订阅的内容
**处理方式**:
- 标注访问限制
- 提取可见的标题和描述
- 如果是知名平台(如 Medium),可间接提及

```markdown
- [高级架构模式](https://premium.example.com/post) — 🔒 需订阅
- 探讨企业级应用的架构设计模式
```

### 10. 技术栈不相关的内容
**处理方式**:
- 即使技术栈不同,仍可记录有价值的内容
- 在描述中明确技术栈
- 便于后续分类和检索

```markdown
- [Go 语言并发模式](https://example.com/go-concurrency)
- 介绍 Goroutine 和 Channel 的最佳实践(Go 语言)

  关键词: [Concurrency][conc], [Goroutine][goroutine]

[conc]: https://en.wikipedia.org/wiki/Concurrency
[goroutine]: https://go.dev/tour/concurrency/1
```

## 决策原则

### 记录 vs 跳过
**应该记录**:
- 有明确价值的内容
- 能学到知识或技能
- 有实用工具或资源
- 值得收藏的观点

**可以跳过**:
- 纯广告内容
- 重复信息
- 极简无实质内容
- 链接失效且无备份

### 描述详略
**简短描述**(≤50字符):
- 工具名称自解释
- 标题已包含核心信息

**中等描述**(50-120字符):
- 补充核心价值
- 说明适用场景

**详细描述**(>120字符,需分点):
- 长文章深度总结
- 复杂工具/项目说明
- 多价值点内容

## 常见错误避免

### 错误 1: 过度翻译
❌ 将中文内容全部翻译为英文
✅ 保持原始语言,仅必要时添加英文关键词

### 错误 2: 主观评价
❌ "这是一个很棒的工具"
✅ "提供 XXX 功能,支持 YYYY"

### 错误 3: 描述冗长
❌ "这是一个基于 React 开发的前端框架,它可以帮助开发者快速构建现代化的 Web 应用..."
✅ "React-based frontend framework for rapid modern web development"

### 错误 4: 关键词过多
❌ 标注 10+ 个关键词
✅ 标注 3-5 个最相关的关键词

### 错误 5: 忽略失效链接
❌ 完全跳过失效但有价值的内容
✅ 标注明状态,仍记录核心信息
