# 创建 Daily Links

## 概述
- 个人/团队每日技术链接归档的结构化文档
- 统一分为六大板块(详见 ./categories.md)
- 通过脚本创建/格式化,保持一致性与可维护性

## 文件结构
```
docs/daily-links/
├── YYYY-MM-DD.md
└── ...
```

## 模板内容
```markdown
# Daily Links YYYY-MM-DD

## 🪶 Remember This

## 🤓 Fav Finds

## 📘 Read This

## 🛠️ Tools

## 🔧 Try This

## 🎧 Listen To
```

## 规则与指引
- 空板块移除: 当日某板块无内容(只有空行/分隔线)时在格式化阶段自动移除
- 新增板块: 在 docs/daily-links 模板中添加标题与图标,并在 ./categories.md 定义映射与样式
- 分类与映射: 详见 ./categories.md
- 去重策略: 详见 ./categories.md

## 配套脚本

### scripts/create-daily-links.sh
- 作用: 创建今日或指定日期的 Daily Links 文件
- 用法:
```bash
./scripts/create-daily-links.sh
./scripts/create-daily-links.sh 2026-01-16
```

### scripts/format-daily-links.sh
- 作用: 统一格式化 Daily Links 文档
- 行为:
  - 在各板块之间插入分隔线 `---`
  - 相邻空行不超过 1 行
  - 去除行尾空白
  - 自动移除空板块
- 用法:
```bash
./scripts/format-daily-links.sh
./scripts/format-daily-links.sh docs/daily-links/2026-01-16.md
```

## 样式
- 概念式(两行): ./daily-links-styles/concept-style.md
- 要点式摘要: ./daily-links-styles/bullets-summary.md
- 官方博客: ./daily-links-styles/official-blog.md
- GitHub Repo: ./daily-links-styles/github-repo.md
- 图标单行: ./daily-links-styles/icon-single-line.md
