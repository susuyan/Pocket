# Skills 目录

本目录存放所有 Claude Code 技能定义。

## 技能列表

| 技能 | 用途 | 状态 |
|------|------|------|
| `link-extractor` | 社交媒体链接提取与归档 | ✅ 完整 |
| `business-problem-solving` | 商业问题分析与解决 | ✅ 完整 |
| `business-improvement` | 业务流程改进 | ✅ 完整 |
| `market-analysis` | 市场研究与分析 | ✅ 完整 |
| `strategy-planning` | 战略规划制定 | ✅ 完整 |
| `ideation-method` | 创意构思与头脑风暴 | ✅ 完整 |
| `organization-management` | 组织管理优化 | ✅ 完整 |
| `problem-organizer` | 问题结构化整理 | ✅ 完整 |
| `TCA Best Practice Enforcer` | TCA 架构最佳实践检查 | ✅ 完整 |

## 技能结构

每个技能目录遵循以下结构：

```
<skill-name>/
├── SKILL.md              # 技能主定义（必需）
└── references/           # 参考资料（可选）
    ├── workflow.md       # 工作流程
    ├── output-format.md  # 输出格式
    ├── methodologies.md  # 方法论
    └── ...               # 其他参考文件
```

## 如何使用

### 在 Claude Code 中调用

```
/skill <skill-name>
```

例如：
```
/skill link-extractor
```

### 查看技能定义

```bash
cat skills/<skill-name>/SKILL.md
```

## 添加新技能

1. 在此目录下创建新文件夹
2. 编写 `SKILL.md` 定义技能
3. 在 `references/` 添加必要的参考资料
4. 在 `.trae/skills/` 创建软链接：

```bash
ln -s /Users/susuyan/Workspace/Pocket/skills/<new-skill> /Users/susuyan/Workspace/Pocket/.trae/skills/<new-skill>
```

## 注意事项

- 技能名称使用小写字母和连字符（kebab-case）
- `SKILL.md` 是必需的入口文件
- `.trae/skills/` 中的软链接指向此目录的实际技能
