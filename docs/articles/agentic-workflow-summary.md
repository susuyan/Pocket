# Agentic Workflow：从 Prompt Engineering 到系统工程

如果说 2023 年是 "Prompt Engineering" 的元年，那么 2024 年就是 "Agentic Workflow"（代理工作流）的爆发期。

Andrew Ng（吴恩达）在近期演讲中指出：**与其追求更强的模型（GPT-5），不如设计更好的工作流。** 良好的 Agentic Workflow 能让 GPT-3.5 表现出超越 GPT-4 的能力。

## 核心理念：System 2 Thinking

传统的 Zero-shot Prompting 类似于人类的 **System 1（快思考）**：直觉反应，脱口而出。
Agentic Workflow 则是 **System 2（慢思考）**：通过迭代、反思、规划，逐步逼近正确答案。

> **Don't ask the model to answer immediately. Ask it to think, plan, and refine.**

## 四大设计模式 (Design Patterns)

### 1. 反思 (Reflection)
最基础也最有效的模式。要求模型在生成结果后，审视自己的输出，寻找错误或改进点。
*   **应用场景**：代码 Debug、文章润色。
*   **流程**：`Draft -> Critique -> Refine`。

### 2. 工具使用 (Tool Use)
打破 LLM 的封闭性，连接外部世界。
*   **应用场景**：
    *   **搜索**：获取实时信息（Web Search）。
    *   **计算**：解决数学短板（Calculator/Python）。
    *   **执行**：操作数据库或文件系统。

### 3. 规划 (Planning)
面对复杂任务，先拆解步骤，再逐一执行。
*   **应用场景**：撰写长篇小说、开发完整软件。
*   **流程**：`Goal -> Plan -> Step 1 -> Step 2 ...`
*   **优势**：避免长 Context 下的注意力丢失（Lost in the Middle）。

### 4. 多智能体协作 (Multi-agent Collaboration)
通过角色扮演（Role Playing），让不同的 Agent 负责不同领域，相互协作或制衡。
*   **应用场景**：软件开发团队（PM + Dev + QA）。
*   **代表项目**：MetaGPT, ChatDev, CrewAI。

## 框架选型指南

*   **LangGraph**: LangChain 生态的进阶，基于图（Graph）的状态机控制。适合构建**复杂、有状态、精细控制**的工作流。
*   **AutoGen**: 微软出品，强调**对话式协作**。灵活性极高，但上手门槛稍高。
*   **CrewAI**: 专注于**角色扮演**，封装度高，上手简单，适合快速构建任务型团队。

## 总结

Agentic Workflow 标志着 AI 开发从“提示词技巧”转向了“软件工程架构”。未来的 AI 应用，不是一个简单的 Chatbot，而是一个由多个专门 Agent 组成的、拥有自我纠错和进化能力的**智能系统**。
