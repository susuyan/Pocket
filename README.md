# Pocket

Claude Code 技能系统 (Skills) 开发仓库。用于定义、管理和维护 AI 辅助工作技能。

## 项目结构

```
Pocket/
├── .trae/skills/          # 技能定义目录
│   ├── <skill-name>/
│   │   ├── SKILL.md       # 技能主定义
│   │   └── references/    # 参考资料
│   │       ├── workflow.md
│   │       ├── output-format.md
│   │       └── methodologies.md
├── docs/
│   ├── daily-links/       # 每日链接归档
│   └── articles/          # 文章汇总
├── scripts/               # 自动化脚本 (待开发)
└── agents/                # Agent 定义
```

## 技能清单

| 技能 | 用途 |
|------|------|
| [link-extractor](.trae/skills/link-extractor/) | 社交媒体链接提取与归档 |
| [business-problem-solving](.trae/skills/business-problem-solving/) | 商业问题分析与解决 |
| [business-improvement](.trae/skills/business-improvement/) | 业务流程改进 |
| [market-analysis](.trae/skills/market-analysis/) | 市场研究与分析 |
| [strategy-planning](.trae/skills/strategy-planning/) | 战略规划制定 |
| [ideation-method](.trae/skills/ideation-method/) | 创意构思与头脑风暴 |
| [organization-management](.trae/skills/organization-management/) | 组织管理优化 |
| [problem-organizer](.trae/skills/problem-organizer/) | 问题结构化整理 |
| [TCA Best Practice Enforcer](.trae/skills/TCA%20Best%20Practice%20Enforcer/) | TCA 架构最佳实践检查 |

## 快速开始

### 使用现有技能
```bash
# 查看技能定义
cat .trae/skills/link-extractor/SKILL.md

# 查看参考资料
ls .trae/skills/link-extractor/references/
```

### 创建新技能
1. 复制技能模板结构
2. 编辑 `SKILL.md` 定义技能
3. 在 `references/` 添加工作流和方法论

## 文档归档

- **daily-links/**: 按 `YYYY-MM-DD.md` 格式归档的链接内容
- **articles/**: 深度文章和总结

## 开发计划

- [ ] 填充 `scripts/` 目录的自动化提取脚本
- [ ] 完善各技能的 references 文档
- [ ] 建立技能间的关联和调用机制
