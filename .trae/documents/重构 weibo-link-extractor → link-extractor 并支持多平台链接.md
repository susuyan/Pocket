## 目标
- 将 weibo-link-extractor 更名为 link-extractor,通用化解析规则。
- 支持 Weibo、X/Twitter、Reddit、Hacker News、各类博客/文章链接。
- 保持 Markdown 输出(含引用链接关键词)与 Daily 归档,分类更通用。

## 变更点
- 目录与前言
  - 重命名目录: `.trae/skills/link-extractor/`
  - 更新 SKILL.md 前言:
    - name: "link-extractor"
    - description: "从社交/新闻/博客链接提取主资源并生成 Markdown 条目与引用关键词;在遇到 weibo/twitter/x/reddit/news.ycombinator.com/博客文章时调用。"
  - 标题改为 "Link Extractor"。

- 支持域与识别
  - 平台域名映射:
    - Weibo: `weibo.com`, `m.weibo.cn`
    - X/Twitter: `x.com`, `twitter.com`
    - Reddit: `reddit.com`
    - Hacker News: `news.ycombinator.com`
    - 博客/文章: 常见博客域/自定义域,通过页面标题与正文线索判断。
  - 链接抽取与展开短链策略说明(保持实现无侵入,以说明为准)。

- 主链接选择与分类
  - 主链接优先: 代码仓库 > 官方文档/项目主页 > 产品/工具页 > 明确标题的技术文章 > 强调链接。
  - 分类映射:
    - 代码仓库: `github.com`/代码托管
    - 工具: 产品/服务/CLI/应用主页
    - 文档/文章: 博客/指南/官方文档
    - 知识点概念: 方法论/架构/思考贴(无明确资源链接或以理念为主)
    - 其他: 不易归类内容

- Markdown 输出
  - 条目格式(不变):
    - [主链接标题](主链接URL) — 简短描述
      
      关键词: [K1][ref1], [K2][ref2]
      
      相关: [Link A][refA], [Link B][refB]
  - 引用链接在条目尾部定义 `[ref]: URL`。

- Daily 归档
  - 将归档文件通用化为 `docs/daily-links/YYYY-MM-DD.md`(可选迁移: 若当天已存在 `daily-weibo` 则沿用,否则新建 `daily-links`)。
  - 标题 `# Daily Links YYYY-MM-DD`。
  - 分类小节沿用并更通用: "知识点概念/工具/代码仓库/文档/文章/其他"。

- 示例扩充
  - Weibo、X/Twitter 推文链接、Reddit 帖子、Hacker News 条目、博客文章各给出一条示例条目。
  - 保留原 Weibo TCA 示例,并给出新 Markdown 引用样例。

- 兼容性
  - 保留旧单行输出格式的说明,但推荐 Markdown 条目。

## 执行步骤(确认后实施)
1. 新建 `.trae/skills/link-extractor/` 并迁移/更新 SKILL.md。
2. 在 `docs/daily-links/` 目录按需创建当天文件(或沿用现有 `daily-weibo`),写入骨架分类。
3. 验证: 读取新 SKILL.md 与当日归档文件,确保无诊断问题。
4. 可选: 将既有 `weibo-link-extractor` 目录标注为废弃或移除以避免歧义。

## 风险与处理
- 引用技能名变化可能影响触发: 在说明中强调触发条件,并在使用文案中更新为新技能名。
- 归档路径迁移的兼容: 先检测旧路径,存在则沿用;否则使用新路径。

请确认以上方案,我将开始重构并更新相关文件。