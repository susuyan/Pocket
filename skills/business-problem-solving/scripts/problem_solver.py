#!/usr/bin/env python3
"""
商业问题解决框架 - 交互式分析脚本

支持四步分析流程：
1. 差距分析 (As is / To be)
2. 6W2H 检视
3. 5 Why 原因分析
4. 可控性分析

使用方法:
    # 完整分析
    python problem_solver.py

    # 单步分析
    python problem_solver.py --step gap
    python problem_solver.py --step 6w2h
    python problem_solver.py --step why
    python problem_solver.py --step control

    # 从 JSON 文件加载/保存
    python problem_solver.py --load data.json
    python problem_solver.py --save data.json
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# ANSI 颜色代码
class Colors:
    BOLD = '\033[1m'
    DIM = '\033[2m'
    NC = '\033[0m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'


def print_header(title: str):
    """打印章节标题"""
    os.system('clear' if os.name == 'posix' else 'cls')
    separator = "=" * 48
    print(f"{Colors.BLUE}{Colors.BOLD}{separator}{Colors.NC}")
    print(f"{Colors.BLUE}{Colors.BOLD}   商业解决问题框架 - {title}{Colors.NC}")
    print(f"{Colors.BLUE}{Colors.BOLD}{separator}{Colors.NC}")
    print()


def ask(prompt: str, default: str = "") -> str:
    """交互式输入"""
    print(f"{Colors.BOLD}{prompt}{Colors.NC}")
    value = input("> ").strip()
    if not value:
        value = default
    print()
    return value


def load_data(filepath: str) -> Dict:
    """从 JSON 文件加载数据"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Colors.YELLOW}警告: 文件 '{filepath}' 不存在，使用空数据{Colors.NC}")
        return {}
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}错误: JSON 解析失败: {e}{Colors.NC}")
        return {}


def save_data(data: Dict, filepath: str):
    """保存数据到 JSON 文件"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"{Colors.GREEN}数据已保存到: {filepath}{Colors.NC}")
    except IOError as e:
        print(f"{Colors.RED}错误: 保存失败: {e}{Colors.NC}")


def step_gap_analysis(data: Dict) -> Dict:
    """步骤 1: 差距分析 (As is / To be)"""
    print_header("Step 1: Define Problem & Gap (定义问题与差距)")
    print(f"{Colors.DIM}目标：明确问题主题，并将理想状况与现状的落差视觉化。{Colors.NC}\n")

    data['problem_statement'] = ask(
        f"{Colors.MAGENTA}Problem (问题主题){Colors.NC}\n"
        f"{Colors.DIM}一句话描述你要解决的问题{Colors.NC}",
        data.get('problem_statement', '')
    )
    data['as_is'] = ask(
        f"{Colors.YELLOW}As is (现状){Colors.NC}\n"
        f"{Colors.DIM}客观描述当前的情况、数据和表现{Colors.NC}",
        data.get('as_is', '')
    )
    data['to_be'] = ask(
        f"{Colors.GREEN}To be (理想){Colors.NC}\n"
        f"{Colors.DIM}明确期望达到的目标、状态或标准{Colors.NC}",
        data.get('to_be', '')
    )
    data['gap'] = ask(
        f"{Colors.RED}Gap (落差/问题){Colors.NC}\n"
        f"{Colors.DIM}两者之间的具体差距{Colors.NC}",
        data.get('gap', '')
    )

    return data


def step_6w2h(data: Dict) -> Dict:
    """步骤 2: 6W2H 检视"""
    print_header("Step 2: 6W2H (多维检视)")
    print(f"{Colors.DIM}目标：透过八个疑问词，全面检视问题的各个面向。{Colors.NC}\n")

    data['6w2h'] = data.get('6w2h', {})
    data['6w2h']['who'] = ask(f"{Colors.CYAN}Who{ Colors.NC} (谁是相关者？谁受影响？)", data['6w2h'].get('who', ''))
    data['6w2h']['what'] = ask(f"{Colors.CYAN}What{ Colors.NC} (发生了什么问题？)", data['6w2h'].get('what', ''))
    data['6w2h']['when'] = ask(f"{Colors.CYAN}When{ Colors.NC} (问题何时发生？持续多久？)", data['6w2h'].get('when', ''))
    data['6w2h']['where'] = ask(f"{Colors.CYAN}Where{ Colors.NC} (问题发生在哪里？)", data['6w2h'].get('where', ''))
    data['6w2h']['why'] = ask(f"{Colors.CYAN}Why{ Colors.NC} (为什么这是个问题？初步原因)", data['6w2h'].get('why', ''))
    data['6w2h']['which'] = ask(f"{Colors.CYAN}Which{ Colors.NC} (涉及哪些对象或选择？)", data['6w2h'].get('which', ''))
    data['6w2h']['how'] = ask(f"{Colors.CYAN}How{ Colors.NC} (问题是如何发生的？)", data['6w2h'].get('how', ''))
    data['6w2h']['how_much'] = ask(f"{Colors.CYAN}How Much{ Colors.NC} (程度如何？损失多少？成本多少？)", data['6w2h'].get('how_much', ''))

    return data


def step_5why(data: Dict) -> Dict:
    """步骤 3: 5 Why 原因分析"""
    print_header("Step 3: 原因分析 (5 Why)")
    print(f"{Colors.DIM}目标：深究问题产生的根本原因。{Colors.NC}\n")

    causes = data.get('causes', [])
    start_count = len(causes) + 1

    while True:
        current_count = start_count + (len(causes) - (start_count - 1))
        print(f"{Colors.MAGENTA}{Colors.BOLD}Why #{current_count}{Colors.NC} (为什么会发生？)")

        cause = input("> ").strip()
        if not cause:
            break

        causes.append(cause)
        print()

        if current_count >= 5:
            continue_ask = input(f"继续追问 Why? (y/N): ").strip()
            if not continue_ask.lower().startswith('y'):
                break
        else:
            continue_ask = input(f"继续追问 Why? (Y/n): ").strip()
            if continue_ask.lower().startswith('n'):
                break
        print()

    data['causes'] = causes
    return data


def step_control_analysis(data: Dict) -> Dict:
    """步骤 4: 可控性分析"""
    print_header("Step 4: 可控性 / 不可控制")
    print(f"{Colors.DIM}目标：掌握己方有能力改变的事物，聚焦资源。{Colors.NC}\n")

    causes = data.get('causes', [])
    if not causes:
        print(f"{Colors.YELLOW}警告: 没有找到原因，请先执行 5 Why 步骤{Colors.NC}")
        return data

    actions = data.get('actions', [])

    print("请分析之前识别出的原因/因素的可控性：\n")

    for i, cause in enumerate(causes):
        # 检查该原因是否已有分析
        existing = next((a for a in actions if a['cause'] == cause), None)
        if existing:
            type_str = existing['type']
            action_note = existing['action']
        else:
            print(f"原因: {Colors.DIM}{cause}{Colors.NC}")
            is_control = input("这是可控制的吗？ (Y/n): ").strip()
            if is_control.lower().startswith('n'):
                type_str = "不可控制"
                action_note = input("应对策略: ").strip()
            else:
                type_str = "可控制"
                action_note = input("行动/对策: ").strip()

            # 添加到 actions，防止重复
            if not any(a['cause'] == cause for a in actions):
                actions.append({
                    'cause': cause,
                    'type': type_str,
                    'action': action_note
                })
            print()

    data['actions'] = actions
    return data


def generate_report(data: Dict, output_path: Optional[str] = None) -> str:
    """生成 Markdown 报告"""
    import textwrap

    if output_path is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = f"problem_solving_report_{timestamp}.md"
    else:
        # 如果是目录，则添加文件名
        if os.path.isdir(output_path):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_path = os.path.join(output_path, f"problem_solving_report_{timestamp}.md")

    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Helper: wrapped text
    def wrap(text: str, width: int = 30) -> str:
        return "\n".join(textwrap.wrap(text, width))

    content = f"""# 📝 商业问题解决报告

**生成时间**: {timestamp_str}
**问题主题**: {data.get('problem_statement', 'N/A')}

---

## 1. 🌉 差距分析 (Gap Analysis)

目标：将理想状况与现状的落差视觉化。

```text
+-----------------------------------+           +-----------------------------------+           +-----------------------------------+
|            AS IS (现状)           |           |             GAP (落差)            |           |           TO BE (理想)            |
|-----------------------------------|           |-----------------------------------|           |-----------------------------------|
{textwrap.indent(wrap(data.get('as_is', 'N/A'), 33), "| ")}
|                                   |   -->     {textwrap.indent(wrap(data.get('gap', 'N/A'), 33), "| ")}
|                                   |           |                                   |   -->     {textwrap.indent(wrap(data.get('to_be', 'N/A'), 33), "| ")}
|                                   |           |                                   |           |                                   |
+-----------------------------------+           +-----------------------------------+           +-----------------------------------+
```

---

## 2. 🧩 6W2H 分析 (多维检视)

目标：透过八个疑问词，全面检视问题的各个面向。

| 维度 | 内容 |
|---|---|
| **Who** (谁) | {data.get('6w2h', {}).get('who', 'N/A')} |
| **What** (什么) | {data.get('6w2h', {}).get('what', 'N/A')} |
| **When** (何时) | {data.get('6w2h', {}).get('when', 'N/A')} |
| **Where** (何地) | {data.get('6w2h', {}).get('where', 'N/A')} |
| **Why** (为什么) | {data.get('6w2h', {}).get('why', 'N/A')} |
| **Which** (哪一个) | {data.get('6w2h', {}).get('which', 'N/A')} |
| **How** (如何) | {data.get('6w2h', {}).get('how', 'N/A')} |
| **How Much** (多少) | {data.get('6w2h', {}).get('how_much', 'N/A')} |

---

## 3. 🌳 根本原因分析 (5 Why Flow)

目标：深究问题产生的根本原因。

```text
"""

    causes = data.get('causes', [])
    for i, cause in enumerate(causes):
        content += f"""[ Why {i+1} ]
          |
          | 原因：{cause}
          v
"""

    content += """[ 🛑 根本原因 ]
```

---

## 4. 🎮 可控性与行动方案 (Controllability Matrix)

目标：掌握己方有能力改变的事物，聚焦资源。

| 原因 / 因素 | 类型 | 行动 / 对策 |
|---|---|---|
"""

    actions = data.get('actions', [])
    for action in actions:
        cause_text = action.get('cause', '')
        type_text = action.get('type', '')
        strategy = action.get('action', '')
        icon = "✅" if "可控制" in type_text else "❌"
        content += f"| {cause_text} | {icon} {type_text} | {strategy} |\n"

    content += """
---

*本报告由商业问题解决框架自动生成*
"""

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return os.path.abspath(output_path)
    except IOError as e:
        print(f"{Colors.RED}错误: 无法写入报告: {e}{Colors.NC}")
        return ""


def main():
    parser = argparse.ArgumentParser(
        description='商业问题解决框架 - 交互式分析脚本',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  完整分析:
    python problem_solver.py

  单步分析:
    python problem_solver.py --step gap
    python problem_solver.py --step 6w2h
    python problem_solver.py --step why
    python problem_solver.py --step control

  JSON 数据操作:
    python problem_solver.py --load data.json --save result.json
    python problem_solver.py --load data.json --step gap --save updated.json
        """
    )

    parser.add_argument('--step', choices=['gap', '6w2h', 'why', 'control'],
                        help='仅执行指定步骤')
    parser.add_argument('--load', help='从 JSON 文件加载数据')
    parser.add_argument('--save', help='保存数据到 JSON 文件')
    parser.add_argument('--output', help='指定报告输出路径')

    args = parser.parse_args()

    # 初始化数据
    data = {}
    if args.load:
        data = load_data(args.load)

    # 执行步骤
    if args.step == 'gap' or args.step is None:
        data = step_gap_analysis(data)

    if args.step == '6w2h' or args.step is None:
        # 检查是否跳过了 gap 步骤
        if not data.get('problem_statement') and args.step is not None:
            print(f"{Colors.YELLOW}警告: 建议先执行 gap 步骤定义问题{Colors.NC}")
        data = step_6w2h(data)

    if args.step == 'why' or args.step is None:
        if not data.get('6w2h') and args.step is not None:
            print(f"{Colors.YELLOW}警告: 建议先执行 6w2h 步骤{Colors.NC}")
        data = step_5why(data)

    if args.step == 'control' or args.step is None:
        if not data.get('causes') and args.step is not None:
            print(f"{Colors.YELLOW}警告: 建议先执行 why 步骤{Colors.NC}")
        data = step_control_analysis(data)

    # 保存数据
    if args.save:
        save_data(data, args.save)

    # 生成报告
    if not args.step:
        # 只有完整流程才生成报告
        report_path = generate_report(data, args.output)
        if report_path:
            print_header("分析完成")
            print(f"{Colors.GREEN}报告已生成: {Colors.BOLD}{report_path}{Colors.NC}")
    elif args.output:
        # 单步也可以生成报告
        report_path = generate_report(data, args.output)
        if report_path:
            print(f"{Colors.GREEN}报告已生成: {Colors.BOLD}{report_path}{Colors.NC}")


if __name__ == '__main__':
    main()
