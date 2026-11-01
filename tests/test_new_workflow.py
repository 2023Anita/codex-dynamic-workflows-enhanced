import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "new_workflow.py"


class NewWorkflowTests(unittest.TestCase):
    def test_creates_new_workflow(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "Example"], cwd=tmp, capture_output=True, text=True
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            run = Path(tmp) / ".workflow" / "example"
            self.assertEqual(
                {p.name for p in run.iterdir()},
                {"packets", "results", "plan.md", "orchestration.md", "final-report.md", "state.json"},
            )

    def test_existing_incomplete_workflow_is_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / ".workflow" / "example"
            run.mkdir(parents=True)
            (run / "plan.md").write_text("existing work", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "Example"], cwd=tmp, capture_output=True, text=True
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual({p.name for p in run.iterdir()}, {"plan.md"})
            self.assertEqual((run / "plan.md").read_text(encoding="utf-8"), "existing work")


if __name__ == "__main__":
    unittest.main()
