## 目标

* 使 link-extractor 的归档分类与条目输出对齐 Trends.vc 风格,提升可读性与决策效率。

## 分类结构(Trends 风格)

* 顶层采用“主题卡片”而非简单按来源分类,每个主题一张卡片:

  * TL;DR: 1 句概括

  * Signals(为何现在): 1–3 条信号/动因

  * Opportunities: 2–3 条可操作机会

  * Risks: 1–2 条风险或注意事项

  * Key Links: 主链接 + 3–5 个相关链接(引用链接形式)

  * Tags: 平台/类型(工具/仓库/文章/概念)

* 索引区(文末): 将当天所有主题按类型聚合列表(工具/仓库/文章/概念/其他),便于快速跳转。

## 每条链接的输出模板( Markdown )

* 主题卡片:

  * [标题](主链接URL) — TL;DR(≤120 字符)

  * Signals:

    * • 信号1

    * • 信号2

  * Opportunities:

    * • 机会1

    * • 机会2

  * Risks:

    * • 风险1

  * Key Links:

    * [主链接](主链接URL) [相关A](相关URLA) [相关B](相关URLB)

  * Tags: 平台(x/twitter/weibo/reddit/hn/blog), 类型(tool/repo/article/concept/other)

  * 引用区:

    * <br />

    * <br />

    * <br />

## 信息抽取与映射规则

* 标题: 优先页面 `<title>`/主 `h1`; 社交贴取正文中最核心资源标题

* TL;DR: 压缩主链接简介 + 正文关键句,去形容词留事实与价值

* Signals: 从正文/元描述/评论提炼“为何现在”(趋势、政策、工具成熟度、成本变化等)

* Opportunities: 从使用场景/商业模式/落地案例抽 2–3 条可执行方向

* Risks: 从限制/合规/依赖/脆弱点提炼 1–2 条

* Key Links: 保留原顺序,去短链与重复,≤5 条

* Tags: 域名映射平台; 类型按域名与内容判断(如 github.com→repo, 产品官网→tool, 博客/文档→article, 无外链或方法论→concept)

## Daily 归档文件

* 路径: `docs/daily-links/YYYY-MM-DD.md`

* 结构:

  * `# Daily Links YYYY-MM-DD`

  * `## Topics`(主题卡片按出现顺序)

  * `## Index by Type`(工具/仓库/文章/概念/其他的索引列表,每项链接到对应卡片锚点)

* 去重策略: 同一 URL 当日仅记录一次(若重复出现,合并 Signals/相关链接)

## 示例(两条)

* Cursor Agent 最佳实践(工具)

  * TL;DR: 官方指南,讲解连续运行、跨文件重构与测试迭代的 Agent 使用范式

  * Signals: AI 编码工具成熟; 长时运行与多文件重构需求增长

  * Opportunities: 用于重构/迁移项目; 建立测试驱动的自动迭代流程

  * Risks: 环境依赖与权限风险; 长上下文溢出需状态外部化

  * Key Links: 主链接 + 官方文档/示例

  * Tags: platform=x/blog, type=tool

* 从 MCP 到 SKILL(概念)

  * TL;DR: 分工思路: MCP 做连接标准化,SKILL 做工作流编排与状态外部化

  * Signals: MCP 接入增多; 上下文预算瓶颈凸显

  * Opportunities: 以脚本+LLM封装场景化流程; 数据落地后仅摘要入上下文

  * Risks: 安全与沙箱; 标准化迁移成本

  * Key Links: 原微博贴

  * Tags: platform=weibo, type=concept

## 技能文件更新要点

* 更新 `.trae/skills/link-extractor/SKILL.md`:

  * 新增“Trends 风格”章节(分类、模板、抽取规则)

  * 说明兼容旧单行输出

  * Daily 文件结构改为 Topics + Index by Type

## 执行步骤(确认后实施)

1. 编辑 link-extractor 的 SKILL.md,加入上述分类与模板说明
2. 调整示例输出为主题卡片形式
3. 在 `docs/daily-links/` 生成当日示例文件结构(如需)
4. 验证文件无诊断问题

## 影响与兼容

* 保持与旧格式兼容; 优先生成主题卡片,必要时可降级为单行摘要

* 不改动已有 weibo-link-extractor 的弃用说明

