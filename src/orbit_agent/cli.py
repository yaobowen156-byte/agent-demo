"""Command line entry point for Agent Demo."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .collector import collect_workspace_context
from .planner import build_plan
from .report import render_report


def _build_trace(goal: str, context, plan) -> dict[str, Any]:
    return {
        "goal": goal,
        "root": str(context.root),
        "plan": [asdict(step) for step in plan],
        "files": [
            {
                "path": str(signal.path),
                "score": signal.score,
                "size": signal.size,
            }
            for signal in context.files
        ],
        "todo_count": context.todo_count,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="orbit-agent",
        description="Plan, inspect, and report on a task with a tiny agentic workflow.",
    )
    parser.add_argument("goal", help="The task or question the agent should handle.")
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace directory to inspect. Defaults to the current directory.",
    )
    parser.add_argument(
        "--save-report",
        default=None,
        help="Optional path to save the generated Markdown report.",
    )
    parser.add_argument(
        "--save-trace",
        default=None,
        help="Optional path to save the machine-readable trace JSON.",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=8,
        help="How many files to inspect before drafting the report.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    root = Path(args.root)
    plan = build_plan(args.goal)
    context = collect_workspace_context(root, max_files=args.max_files)
    report = render_report(args.goal, plan, context)

    print(report, end="")

    if args.save_report:
        report_path = Path(args.save_report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")

    if args.save_trace:
        trace_path = Path(args.save_trace)
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        trace_path.write_text(
            json.dumps(_build_trace(args.goal, context, plan), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
