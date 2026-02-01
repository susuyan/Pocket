---
name: link-extractor
description: 从社交媒体、技术新闻和博客文章中提取核心资源,生成结构化 Markdown 条目并归档到指定文件夹。支持智能分类和多种输出样式。
---

# SKILL — TCA Best Practice Enforcer

Purpose
将 The Composable Architecture（TCA）的官方理念 + 项目级最佳实践，
统一为一个可执行、可审查、可复用的架构 SKILL。

⸻

## 1. Skill 概述

Name
TCA_Best_Practice_Enforcer

Category
architecture / state-management

Description
该 SKILL 用于生成、校验与约束基于 The Composable Architecture (TCA) 的 Feature 设计，
确保 Reducer、State、Action、Dependency、Async Task、Navigation、Testing 等方面符合最佳实践。

⸻

## 2. Skill 适用场景（When to Use）
	•	设计一个新的 TCA Feature
	•	Code Review 一个已有 Reducer
	•	重构臃肿或不可测试的 Feature
	•	为团队统一 TCA 编码规范
	•	为 Agent 生成「合规的 TCA 模板」

⸻

## 3. 输入（Input Contract）

feature_context:
  type: object
  required: true
  description: Feature 的设计上下文
  fields:
    name:
      type: string
      description: Feature 名称
    responsibility:
      type: string
      description: Feature 的核心职责
    scope_level:
      type: enum
      values: [App, Flow, Screen, Component]
    side_effects:
      type: array[string]
      description: 网络、数据库、文件、传感器等副作用
    navigation:
      type: boolean
      description: 是否涉及路由或页面跳转

existing_structure:
  type: object
  required: false
  description: 已存在的 Reducer / State / Action 结构（如用于审查）


⸻

## 4. 输出（Output Contract）

recommended_structure:
  type: object
  description: 推荐的 TCA Feature 结构

best_practices:
  type: array[string]
  description: 当前 Feature 必须遵循的 TCA 实践要点

anti_patterns:
  type: array[string]
  description: 当前 Feature 中需要避免的反模式

checklist:
  type: array[string]
  description: 可用于 Code Review / 自检的清单


⸻

## 5. Skill 行为（Behavior Specification）

### 5.1 Reducer 结构约束
	•	一个 Reducer = 一个明确职责
	•	State 必须是单一事实源
	•	所有副作用必须：
	•	通过 @Dependency 注入
	•	通过 .run 发起
	•	所有异步 Effect 必须可取消

⸻

### 5.2 State 设计规则
	•	✅ 使用明确的枚举建模状态（如 LoadingState）
	•	✅ 路由状态使用 Route? 或枚举
	•	❌ 禁止多个 Bool 组合表达状态
	•	❌ 禁止 ViewState 与 DomainState 混杂

⸻

### 5.3 Action 设计规则

Action 必须语义分组：

enum Action {
  // Binding
  case binding(BindingAction<State>)

  // Lifecycle
  case onAppear
  case teardown

  // User Intent
  case refreshButtonTapped

  // Async
  case fetchItems
  case fetchItemsDone(Result<[Item], AppError>)

  // Navigation
  case setNavigation(Route?)

  // Child
  case child(Child.Action)
}


⸻

### 5.4 异步与取消策略
	•	所有异步任务必须：
	•	对应 CancelID
	•	在 teardown 中统一取消
	•	Reducer 中不允许：
	•	Task {}
	•	直接调用 async API

⸻

### 5.5 导航与生命周期
	•	路由是 State，不是 Effect
	•	路由关闭必须触发：
	•	子状态清理
	•	异步任务取消

⸻

## 6. 非目标（Non-Goals）

该 SKILL 不会：
	•	自动生成完整业务代码
	•	决定 UI 实现细节
	•	评判业务逻辑对错
	•	替代工程师做架构取舍

⸻

## 7. 测试约束（Testing Guarantees）

该 SKILL 输出的结构 必须满足：
	•	可使用 TestStore 覆盖：
	•	成功 / 失败
	•	取消
	•	路由
	•	所有依赖可被 Mock
	•	Reducer 行为可预测、可断言

⸻

## 8. 输出示例（语义级）

recommended_structure:
  State:
    - loadingState
    - items
    - route
  Action:
    - fetchItems
    - fetchItemsDone
    - setNavigation
  Dependency:
    - apiClient
  CancelID:
    - fetchItems

best_practices:
  - 使用 LoadingState 枚举表达请求状态
  - 路由关闭时统一 teardown
  - 异步任务必须 cancellable

anti_patterns:
  - 在 Reducer 中直接调用单例
  - 使用 Bool 组合表达状态
  - 在 Action 中混合 UI 与业务语义


⸻

9. 演进建议（Future Extensions）
	•	自动生成 {Feature}Reducer.swift 模板
	•	与 SwiftLint / Danger 集成
	•	Feature 复杂度评分
	•	Agent 级别自动重构建议

⸻

10. 一句话总结

这是一个：
“把 TCA 从‘经验型架构’压缩成‘可执行能力模块’的 SKILL。”

⸻