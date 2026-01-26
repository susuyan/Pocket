# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

Pocket 是一个内容管理自动化项目，专注于社交媒体链接提取和归档。核心功能包括从微博和 Twitter/X 提取内容，并将其整理为结构化的 Markdown 文档归档到 `docs/daily-links/` 目录中。

## 核心脚本

`scripts/` 目录包含三个 Python 脚本，实现了链接提取功能：

### 使用方法

```bash
# 提取单个微博链接
python scripts/weibo_extractor.py https://weibo.com/xxx/xxx

# 提取单个 Twitter 链接（支持代理）
python scripts/twitter_extractor.py https://x.com/xxx/status/xxx -p http://proxy:port

# 使用统一提取器（自动识别平台）
python scripts/link_extractor.py <weibo_or_twitter_url> -p http://proxy:port
```

### 脚本架构

1. **`link_extractor.py`** (统一入口)
   - 自动检测链接类型（微博/Twitter）
   - 分发到对应的提取器
   - 支持代理参数（仅 Twitter 需要）

2. **`weibo_extractor.py`** (微博提取)
   - `WeiboExtractor` 类处理微博内容提取
   - 支持多种微博链接格式
   - 输出 Markdown/JSON/Plain 格式
   - 依赖: `requests`, `beautifulsoup4`

3. **`twitter_extractor.py`** (Twitter/X 提取)
   - `TwitterExtractor` 类支持多级回退策略
   - 优先: Guest Token API
   - 备选: Nitter 实例轮询
   - 保底: Syndication API
   - 自动检测系统代理（HTTP_PROXY, HTTPS_PROXY）

## 敏感信息处理

**CRITICAL**: `twitter_extractor.py` 中包含 Guest Bearer Token 等敏感信息：
- 这些是 X/Twitter 的公开端点凭证
- 当前代码直接硬编码在程序中
- 未来重构时应移至环境变量或配置文件

## Skills 系统 (Claude Code)

`.trae/skills/` 目录包含 Claude Code 技能定义（Markdown 格式）：

### 已有技能

- **`link-extractor/`**: 链接提取和处理技能
  - `references/`: 包含工作流、分类规则、样式模板、语言规范
  - 支持多种内容格式（GitHub 仓库、官方博客、概念式等）

- **`business-problem-solving/`**: 商业问题解决技能

- **`TCA Best Practice Enforcer/`**: TCA（The Composable Architecture）最佳实践强制执行器

### 创建新技能

参考 `SKILL_SKELETON_GUIDE.md` 和现有技能结构。

技能目录标准结构：
```
.trae/skills/<skill-name>/
├── SKILL.md              # 主技能定义
└── references/           # 参考资料（可选）
    ├── workflow.md
    ├── categories.md
    └── ...
```

## 文档归档格式

`docs/daily-links/` 遵循标准化格式：

### 日期文件命名
```
docs/daily-links/YYYY-MM-DD.md
```

### 内容板块分类
每个归档文件分为六大板块：
- 📘 **Read This** - 文章和阅读材料
- 🛠️ **Tools** - 工具和库
- 🔧 **Try This** - 教程和实践
- 🎧 **Listen To** - 播客和音频
- 🪶 **Remember This** - 箴言和原则
- 🤓 **Fav Finds** - 其他有价值的资源

### 描述规范（来自 `.trae/skills/link-extractor/references/language-rules.md`）
- 描述 ≤ 120 字符
- 无主观评价词汇（避免"很棒"、"优秀"）
- 技术术语准确
- 使用功能性描述

## 依赖管理

Python 脚本依赖：
```bash
pip install requests beautifulsoup4
```

## Git 相关

- 当前分支: `main`
- 最新提交: TCA 最佳实践相关
- 未追踪文件: `.trae/skills/business-problem-solving/`, `SKILL_SKELETON_GUIDE.md`
