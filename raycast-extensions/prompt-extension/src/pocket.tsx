import { Action, ActionPanel, Clipboard, Icon, List, Toast, closeMainWindow, showToast } from "@raycast/api";
import fs from "fs";
import os from "os";
import path from "path";

type Prompt = {
  name: string;
  description?: string;
  content: string;
  keywords?: string[];
};

// 默认 Prompts 数据（内嵌，确保始终可用）
const DEFAULT_PROMPTS: Prompt[] = [
  {
    name: "Bug Triage",
    description: "分析错误日志并生成修复路线",
    content: "你是资深工程师。阅读日志，定位根因，列修复步骤与验证方案。"
  },
  {
    name: "PR Reviewer",
    description: "代码评审要点清单",
    content: "检查架构一致性、边界条件、错误处理、安全、性能、可读性与测试覆盖率。"
  },
  {
    name: "Meeting Summary",
    description: "结构化会议纪要模版",
    content: "议题、决策、Action Items(负责人/截止)、风险、后续安排。"
  }
];

function readJSON(filePath: string): Prompt[] | null {
  try {
    if (!fs.existsSync(filePath)) return null;
    const raw = fs.readFileSync(filePath, "utf8");
    const data = JSON.parse(raw);
    if (!Array.isArray(data)) return null;
    return data
      .filter((p) => p && typeof p === "object" && typeof p.name === "string" && typeof p.content === "string")
      .map((p) => ({ ...p }));
  } catch {
    return null;
  }
}

function loadPrompts(): Prompt[] {
  const home = os.homedir();
  const userPath = path.join(home, "Workspace", "Prompt", "prompts.json");
  const fromUser = readJSON(userPath);
  if (fromUser && fromUser.length > 0) return fromUser;
  return DEFAULT_PROMPTS;
}

export default function Command() {
  const prompts = loadPrompts();
  return (
    <List searchBarPlaceholder="搜索 Prompt 名称或描述" isLoading={false} navigationTitle="Prompt 列表">
      {prompts.map((p) => (
        <List.Item
          key={p.name}
          title={p.name}
          subtitle={p.description}
          keywords={[p.name, p.description || "", ...(p.keywords || [])]}
          accessories={[{ icon: Icon.Clipboard, tooltip: "点击复制" }]}
          actions={
            <ActionPanel>
              <Action
                title="复制到剪贴板"
                icon={Icon.Clipboard}
                onAction={async () => {
                  await Clipboard.copy(p.content);
                  await closeMainWindow();
                }}
              />
              <Action.CopyToClipboard title="复制 Prompt 内容" content={p.content} />
              <Action.CopyToClipboard title="复制名称" content={p.name} />
              {p.description ? <Action.CopyToClipboard title="复制描述" content={p.description} /> : null}
            </ActionPanel>
          }
        />
      ))}
      {prompts.length === 0 ? (
        <List.EmptyView title="未找到 Prompt" description="数据为空" icon={Icon.Info} />
      ) : null}
    </List>
  );
}
