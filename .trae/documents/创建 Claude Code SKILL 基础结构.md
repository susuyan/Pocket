## 目标

* 提供一套可复用的 Claude Code SKILL 基础骨架

* 采用清晰的目录、元数据与输入输出约定，便于快速扩展

## 产出物

* 技能目录结构与核心文件清单

* 最小可用 skill.json 与 prompt 模板

* 基础校验与示例用法

## 目录结构

* skills/claude-code/

* skills/claude-code/skill.json

* skills/claude-code/prompt.md

* skills/claude-code/schemas/input.schema.json

* skills/claude-code/schemas/output.schema.json

* skills/claude-code/examples/basic.yml

* skills/claude-code/tests/validation.spec

* skills/claude-code/README.md

## 元数据设计（skill.json 字段）

* name/version/title/description/author/tags

* runtime: language/entrypoint（prompt 驱动或脚本入口）

* permissions: 文件/网络/搜索等（默认空）

* inputs: JSON Schema，约束任务、上下文、限制项

* outputs: JSON Schema，约定 summary、actions 等

* commands: 列出可用指令，含 input/output schema 引用

* examples: 最小输入输出示例

## 最小模板

* skill.json

```json
{
  "name": "claude-code-skill",
  "version": "0.1.0",
  "title": "Claude Code Skill",
  "description": "用于代码辅助的通用技能",
  "author": "your-name",
  "tags": ["code", "review", "refactor"],
  "runtime": { "language": "none", "entrypoint": "prompt" },
  "permissions": [],
  "inputs": {
    "type": "object",
    "properties": {
      "task": {"type": "string"},
      "context": {"type": "string"},
      "constraints": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["task"]
  },
  "outputs": {
    "type": "object",
    "properties": {
      "summary": {"type": "string"},
      "actions": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["summary"]
  },
  "commands": [
    {
      "id": "analyze",
      "description": "分析任务并给出操作建议",
      "input_schema_ref": "./schemas/input.schema.json",
      "output_schema_ref": "./schemas/output.schema.json"
    }
  ],
  "examples": [
    {
      "input": {"task": "修复单元测试失败"},
      "output": {"summary": "定位并修复失败断言", "actions": ["查找失败用例", "更新断言"]}
    }
  ]
}
```

* prompt.md

```
角色：资深代码顾问
目标：在给定 inputs 下输出结构化的 summary 与 actions。
输出格式：严格遵循 outputs schema。
```

* input.schema.json / output.schema.json 与 skill.json 保持一致的 JSON Schema 定义

## 校验与示例

* schema 校验：对 examples/basic.yml 进行输入输出验证

* 用法示例：传入 task/context，产出 summary/actions

* 测试用例：tests/validation.spec 覆盖必填字段与格式

## 后续扩展

* 增加 commands（如 refactor、lint、scaffold）与对应 schema

* 引入权限细化与安全控制（文件/网络白名单）

* 增加多语言标签与更丰富 few-shot 示例

## 需要你确认

* 该 SKILL 的具体用途与首批 commands 名称

* 是否需要文件系统或网络权限

* 输出格式是否仅包含 summary/actions 或需结构化报告

