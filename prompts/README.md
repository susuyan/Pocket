# Prompts 目录

本目录存放可复用的 AI 提示词模板。

## 格式规范

每个提示词文件使用 YAML frontmatter 格式：

```markdown
---
name: "提示词名称"
description: "简短描述"
---

提示词内容...
```

## 现有提示词

| 文件 | 名称 | 描述 |
|------|------|------|
| [bug-triage.md](bug-triage.md) | Bug Triage | 分析错误日志并生成修复路线 |

## 使用方式

1. 复制提示词内容到 Claude Code
2. 或引用文件路径: `@prompts/xxx.md`

## 添加新提示词

1. 创建 `.md` 文件
2. 添加 YAML frontmatter (name + description)
3. 编写提示词内容
