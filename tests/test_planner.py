import unittest

from orbit_agent.planner import build_plan


class PlannerTests(unittest.TestCase):
    def test_build_plan_has_verification_step(self):
        plan = build_plan("refactor a small demo")
        self.assertGreaterEqual(len(plan), 4)
        self.assertEqual(plan[0].title, "Clarify the goal")
        self.assertEqual(plan[-1].title, "Verify the result")

