# 使用示例

## 示例 1: 提取 Weibo 帖子
输入:
```bash
link https://weibo.com/1648815335/Qn8iCfNyt
```
输出:
```markdown
## 🤓 Fav Finds

- [MCP → SKILL 扩展机制](https://weibo.com/1648815335/Qn8iCfNyt) shared by [@username](https://weibo.com/1648815335)
- Split concerns: MCP standardizes connection, SKILL orchestrates workflow and externalizes state

```

## 示例 2: 提取官方博客
输入:
```bash
link https://cursor.com/cn/blog/agent-best-practices
```
输出:
```markdown
## 📘 Read This

- [**Agent Best Practices**](https://cursor.com/cn/blog/agent-best-practices) — 来自 [Cursor team](https://cursor.com)
- 明细说明: Official guide for agent-based coding: long-run, multi-file refactors, test-driven iteration
```

## 示例 3: 提取 GitHub 仓库
输入:
```bash
link https://github.com/pointfreeco/swift-composable-architecture
```
输出:
```markdown
## 🛠️ Tools

- [swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) — Swift 应用架构库,强调组合与可测试性

```

## 示例 4: 提取长文章(要点式)
输入:
```bash
link https://www.codusoperandi.com/posts/increasing-your-luck-surface-area
```
输出:
```markdown
## 📘 Read This

- [Increasing Your Luck Surface Area](https://www.codusoperandi.com/posts/increasing-your-luck-surface-area)

  **You can make your own luck** through a powerful principle of passion and communication.

  - **Pour energy into your passion**: when you're excited about something, you naturally pull others into your orbit
  - **Tell more people**: people will capture that value in ways you'd never predict — hiring you, partnering with you or investing in you
  - **Luck is 'doing' multiplied by 'telling'**: the more you do and the more people you tell about it, the larger your Luck Surface Area becomes
```

