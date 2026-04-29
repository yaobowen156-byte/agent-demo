"""Report rendering helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .collector import WorkspaceContext
from .planner import PlanStep


def _format_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def render_report(goal: str, plan: list[PlanStep], context: WorkspaceContext) -> str:
    """Render a Markdown report for the agent run."""

    lines: list[str] = []
    lines.append("# Orbit Agent Report")
    lines.append("")
    lines.append(f"- Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"- Goal: {goal.strip()}")
    lines.append(f"- Workspace: `{context.root}`")
    lines.append("")

    lines.append("## Plan")
    for index, step in enumerate(plan, start=1):
        lines.append(f"{index}. {step.title} - {step.detail}")
    lines.append("")

    lines.append("## Workspace Signals")
    if context.files:
        for signal in context.files:
            lines.append(f"- `{_format_path(signal.path, context.root)}` ({signal.size} bytes)")
    else:
        lines.append("- No files were found in the target workspace.")
    lines.append("")

    lines.append("## Evidence Snapshot")
    if context.sample_contents:
        for path, content in context.sample_contents.items():
            rel = _format_path(path, context.root)
            preview = content.splitlines()[:8]
            preview_text = "\n".join(preview).strip()
            lines.append(f"### `{rel}`")
            lines.append("")
            lines.append("```text")
            lines.append(preview_text or "[empty file]")
            lines.append("```")
            lines.append("")
    else:
        lines.append("- No text samples were captured.")
        lines.append("")

    lines.append("## Verification")
    checks = [
        ("plan steps", len(plan) >= 4),
        ("workspace evidence", bool(context.files)),
        ("todo markers tracked", context.todo_count >= 0),
    ]
    for label, passed in checks:
        lines.append(f"- {label}: {'passed' if passed else 'failed'}")
    lines.append("")

    lines.append("## Next Action")
    if context.files:
        top = _format_path(context.files[0].path, context.root)
        lines.append(f"- Start with `{top}` because it scored highest in the scan.")
    else:
        lines.append("- Create a small demo workspace so the agent has something to inspect.")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"

