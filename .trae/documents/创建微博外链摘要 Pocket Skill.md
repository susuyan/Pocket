## 目标
- 创建可在 Claude Code/Trae 中使用的技能,解析微博链接并输出“一行主链接+简短描述+(相关链接…)”。
- 技能名: weibo-link-extractor。

## 交付物
- 路径: .trae/skills/weibo-link-extractor/SKILL.md
- 内容: 前置 YAML(含 name/description),使用指南、决策流程、示例(含你提供的案例)、边界处理。

## 文件内容(SKILL.md)
```markdown
---
name: "weibo-link-extractor"
description: "从微博链接提取外部资源并生成‘主链接 - 简短描述 (相关链接…)’的一行摘要。遇到 weibo.com/m.weibo.cn 链接或用户要求解析微博时调用。"
license: Apache-2.0
metadata:
  author: pocket
  version: "1.0"
---

# Weibo Link Extractor

## 概述
解析微博正文,提取 GitHub/Twitter/博客等外链,选择一个主链接并生成简短描述,其余链接以括号列出,用于收藏/归档。

## 标准输出格式
`主链接` - 简短描述 (相关链接1) (相关链接2) ...

## 使用场景
- 用户提供微博 URL 要求“解析微博/提取外链”。
- 整理微博收藏中的技术资源,需要结构化输出。

## 核心功能
- 抽取正文与外链(展开短链,过滤无关统计/头像资源)。
- 主链接优先级: GitHub 仓库 > 官方文档/项目主页 > 明确标题的技术文章 > 文案强烈强调的链接。
- 生成 1 句不超过约 120 字符的客观描述(综合主链接标题与微博文案)。
- 相关链接按出现顺序去重后括号列出(3–5 个)。

## 流程与决策
1. 识别微博域名 → 抽取正文+全部外链。
2. 依据优先级选择主链接(多仓库取正文中最靠前)。
3. 压缩生成简短描述(类型+核心价值)。
4. 组装标准输出格式;多条输入逐条输出独立行。

## 示例(题主案例)
输入:
https://weibo.com/5167456916/J1HPK31Lf?refer_flag=1001030103_

输出:
https://github.com/pointfreeco/swift-composable-architecture - Library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. (https://github.com/antranapp/awesome-tca) (https://twitter.com/pointfreeco/status/1389614299832741891) (https://github.com/aacapella/swift-composable-undo)

## 边界处理
- 不可访问/删除: 返回该微博 URL + “无法访问或已删除”。
- 无外链: 返回 “无外链 - 微博主要内容简要总结”。
- 多条输入: 每条微博各自输出一行,不混淆链接。

## 验证清单
- name/description 合规并明确“何时调用”。
- 输出格式严格为一行: 主链接 + 描述 + 括号中的相关链接。
- 示例与优先级规则覆盖主要场景。
```

## 实施步骤(确认后执行)
- 新建目录 .trae/skills/weibo-link-extractor/
- 写入上述 SKILL.md 文件内容
- 快速自检: 路径/前言格式/示例一致性

## 后续扩展(可选)
- 增加批量解析说明与速记提示
- 添加更多域名映射与链接分类规则
- 引入自动短链展开策略说明