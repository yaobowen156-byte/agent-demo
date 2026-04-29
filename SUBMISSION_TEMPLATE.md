# Xiaomi MiMo Orbit Submission Template

Use this as a starting point and replace the bracketed parts with your real details.

## 1. Agent tool

Pick the tool you actually used to build the project:

- `Codex`，如果你主要就是在这边边做边改
- `Claude Code`，如果你主要靠它跑代码和改项目
- `Cursor`，如果你平时主要在 Cursor 里做
- `OpenClaw`，如果你就是用这个在做 agent 工作流
- `Aider`，如果你是那种命令行里一把梭的
- 其他你自己的 agent，也可以直接写出来

## 2. Model series

Pick the primary model family you actually used:

- `GPT`
- `Claude`
- `MiMo`
- `DeepSeek`
- `Gemini`
- `Doubao`
- `MiniMax`

如果你是混着用的，建议写你最主要的那个，别写太散。

## 3. Work description

Paste this and adjust it to your own facts:

> I built a small agent-style CLI and browser demo called Orbit Agent Demo. You give it a goal, it breaks the task into steps, scans a workspace for useful clues, and then generates a verified Markdown report plus a trace file. The whole thing is meant to show how an agent can plan, inspect, draft, and check itself in a very compact repo.

## 4. Proof materials

Attach at least one of these:

- `output/report.md`
- `output/trace.json`
- 一张终端运行截图，里面能看到 `python -m orbit_agent ...`
- 你的 GitHub 仓库链接
- 一个很短的录屏或者 GIF

如果你想更稳一点，建议至少放 3 个：

1. 终端截图
2. 报告文件
3. GitHub 仓库链接

## 5. Short form summary

If the form only gives you a small text box, use this:

> A tiny agent workflow that plans a task, inspects a workspace, writes a report, and verifies the output. It includes a small browser front end, a CLI, a sample workspace, and saved trace output.

## 6. More natural upload note

If there is a free-text upload/proof box, you can use this tone:

> 我这次做的是一个很小但完整的 agent demo。它不是只会“说自己会用 AI”，而是真的有任务拆解、目录扫描、证据整理和结果校验。仓库里也有可运行的 CLI、网页展示页、示例工作区和报告输出，方便你直接看它是怎么跑起来的。

