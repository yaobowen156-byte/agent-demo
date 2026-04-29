"""Goal-to-plan helpers for the demo agent."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanStep:
    """A single step in the agent plan."""

    title: str
    detail: str


def build_plan(goal: str) -> list[PlanStep]:
    """Turn a goal into a compact action plan.

    The logic is intentionally simple and deterministic so the repo can run
    anywhere without API keys, while still looking like a real agent flow.
    """

    normalized = goal.strip().lower()
    steps = [
        PlanStep("Clarify the goal", f"Restate the request: {goal.strip()}"),
        PlanStep(
            "Inspect the workspace",
            "Scan the target directory for the most relevant files and signals.",
        ),
    ]

    if any(word in normalized for word in ("refactor", "cleanup", "review", "audit")):
        steps.append(
            PlanStep(
                "Look for code quality signals",
                "Collect TODOs, FIXME markers, and file hotspots that suggest next actions.",
            )
        )
    else:
        steps.append(
            PlanStep(
                "Extract key evidence",
                "Summarize file structure, top files, and any obvious context markers.",
            )
        )

    steps.append(
        PlanStep(
            "Draft a deliverable",
            "Write a short report that can be pasted into README, issue comments, or a form.",
        )
    )
    steps.append(
        PlanStep(
            "Verify the result",
            "Check that the final output contains the expected sections and evidence.",
        )
    )
    return steps

