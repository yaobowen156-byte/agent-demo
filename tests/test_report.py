import tempfile
import unittest
from pathlib import Path

from orbit_agent.collector import WorkspaceContext
from orbit_agent.planner import PlanStep
from orbit_agent.report import render_report


class ReportTests(unittest.TestCase):
    def test_render_report_contains_required_sections(self):
        with tempfile.TemporaryDirectory() as tmp:
            context = WorkspaceContext(
                root=Path(tmp),
                files=[],
                sample_contents={},
                todo_count=0,
            )
            report = render_report("summarize the workspace", [PlanStep("One", "Two")], context)
            self.assertIn("# Agent Demo Report", report)
            self.assertIn("## Plan", report)
            self.assertIn("## Verification", report)
