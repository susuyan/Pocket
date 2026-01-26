# 商业问题解决工作流

## 完整四步流程

本框架提供系统化的商业问题解决方法，包含四个核心步骤：

```
差距分析 → 6W2H检视 → 5Why分析 → 可控性分析
```

---

## 步骤 1: 差距分析 (Gap Analysis)

### 目标
明确问题主题，并将理想状况与现状的落差视觉化。

### 三个核心要素

**As is (现状)**
- 客观描述当前的情况
- 使用数据、事实、可观察的表现
- 避免主观判断和推测

**To be (理想)**
- 明确期望达到的目标
- 定义成功标准和状态
- 可量化的结果/指标

**Gap (落差)**
- 现状与理想之间的具体差距
- 可直接观察的差距表现
- 形成问题的直接证据

### 执行方式
```
使用脚本:
  python problem_solver.py --step gap

或进入完整流程:
  python problem_solver.py
```

### 关键原则
- 保持客观：仅描述事实，不作评价
- 使用数据：可量化、可验证
- 明确边界：避免范围无限扩大

---

## 步骤 2: 6W2H 检视

### 目标
透过八个疑问词，全面检视问题的各个面向。

### 八个维度

| 维度 | 问题 | 回答要点 |
|---|---|---|
| **Who** | 谁是相关者？谁受影响？ | 利益相关者、责任人、影响范围 |
| **What** | 发生了什么问题？ | 问题的具体表现和现象 |
| **When** | 问题何时发生？持续多久？ | 时间点、频率、持续时间 |
| **Where** | 问题发生在哪里？ | 地点/系统/部门/流程 |
| **Why** | 为什么这是个问题？(初步原因) | 问题的重要性判断 |
| **Which** | 涉及哪些对象或选择？ | 具体对象、选项、变体 |
| **How** | 问题是如何发生的？ | 触发条件、发生路径 |
| **How Much** | 程度如何？损失多少？成本多少？ | 量化指标、影响程度 |

### 执行方式
```
使用脚本:
  python problem_solver.py --step 6w2h
```

### 关键原则
- 全面性：八个维度都应回答
- 具体性：避免模糊不清的回答
- 量化性：尽可能使用数字

---

## 步骤 3: 5 Why 原因分析

### 目标
深究问题产生的根本原因。

### 方法
通过连续追问「为什么」，揭示问题的层层因果关系：

```
问题发生？
    ↓ Why?
原因1
    ↓ Why?
原因2
    ↓ Why?
原因3
    ↓ Why?
原因4
    ↓ Why?
原因5 (根本原因)
```

### 执行方式
```
使用脚本:
  python problem_solver.py --step why
```

### 何时停止
- 找到可控的根本原因
- 原因链无法继续深入
- 达到系统/组织边界

### 关键原则
- 基于事实：每一步都有证据支持
- 避免猜测：不确定时就调查研究
- 聚焦根本：而非表面症状

---

## 步骤 4: 可控性分析

### 目标
掌握己方有能力改变的事物，聚焦资源。

### 分析维度

对于每个识别出的原因：

**可控制因素**
- 有权/有能力改变的因素
- 资源覆盖范围内
- 可以采取行动

→ 制定具体**行动/对策**

**不可控制因素**
- 外部因素或超出权限
- 需要协调或等待

→ 制定**应对策略**（如监控、规避、缓解）

### 执行方式
```
使用脚本:
  python problem_solver.py --step control
```

### 关键原则
- 聚焦可控：把精力放在自己能影响的范围内
- 区分优先级：重点先处理主要可控因素
- 制定可执行步骤：每条对策都有具体行动

---

## 单步执行模式

如果只需要执行其中一步（例如已有问题描述只需要深究原因）：

```bash
# 只分析差距
python problem_solver.py --step gap

# 只做 6W2H 检视
python problem_solver.py --step 6w2h

# 只做 5 Why 分析
python problem_solver.py --step why

# 只做可控性分析
python problem_solver.py --step control
```

---

## 数据持久化

使用 JSON 文件保存和加载分析数据：

```bash
# 加载已有数据
python problem_solver.py --load data.json

# 保存分析结果
python problem_solver.py --save result.json

# 加载并继续分析
python problem_solver.py --load data.json --step why --save updated.json
```

---

## 完整流程示例

```bash
# 从头开始完整分析
python problem_solver.py

# 或分步执行
python problem_solver.py --step gap
python problem_solver.py --step 6w2h
python problem_solver.py --step why
python problem_solver.py --step control
```

最终生成 `problem_solving_report_YYYYMMDD_HHMMSS.md` 报告。
