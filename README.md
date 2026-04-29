# Orbit Agent Demo

`orbit-agent` is a tiny, GitHub-friendly demo of an agentic workflow.

It does four simple but very visible things:

1. Plans a task into concrete steps.
2. Scans a target directory for useful context.
3. Summarizes findings into a Markdown report.
4. Verifies the report before printing it.

## What this repo is trying to show

- The core problem: turn a vague request into a structured execution brief.
- The core logic flow: `plan -> inspect -> draft -> verify`.
- The proof: terminal output, saved Markdown reports, a small trace JSON, and a simple browser UI.

## Why this looks like an agent

The project is intentionally small, but it still shows the parts people expect from an agent:

- Goal decomposition
- Context gathering
- Evidence-based drafting
- Final verification

It is also deterministic and dependency-free, so anyone can run it from a fresh clone.

## Quick start

```bash
python -m orbit_agent "summarize the demo workspace" --root demo_workspace --save-report output/report.md
```

Or install it locally:

```bash
pip install -e .
orbit-agent "summarize the demo workspace" --root demo_workspace
```

## Browser demo

Open [`web/index.html`](web/index.html) in a browser to see the lightweight front end.

The page shows:

- What the agent does
- A visual workflow
- The example output structure
- Copy-ready submission text
- The upload checklist in a more natural tone

## What it outputs

- A plan with 4 to 5 steps.
- A concise context snapshot.
- A Markdown report with sections for goal, plan, findings, and next actions.
- A machine-readable trace file when you ask it to save one.

## Demo workspace

The repository includes `demo_workspace/` so you can show a real run without any setup.

## Suggested GitHub title

`Orbit Agent Demo: a tiny planning + inspection + reporting workflow`

## Suggested submission wording

> I built a small agent-style CLI and a matching browser demo. It takes a goal, breaks it into steps, scans a workspace for useful evidence, and generates a verified Markdown report plus a trace file. The repo is meant to show planning, context gathering, drafting, and self-checking in one compact project.
