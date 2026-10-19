"""Regression tests for the skill layout check.

The repository's first public version kept SKILL.md at the root, so
`gh skill install heydavidf/competitor-analysis` found no skills. These tests
keep the skills/<name>/ layout in place and check that the guard catches the
old layout and the mistakes that would break an installed copy.

Run: python3 -B -m unittest discover -s tests -v
"""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CHECKER = REPO / ".github" / "check_skill_layout.py"
SKILL = "skills/competitor-analysis"


def run_checker(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-B", str(CHECKER), str(repo)],
        capture_output=True,
        text=True,
        check=False,
    )


class SkillLayoutTest(unittest.TestCase):
    def setUp(self):
        self.temp = Path(tempfile.mkdtemp(prefix="skill-layout-"))
        self.copy = self.temp / "repo"
        shutil.copytree(REPO / SKILL, self.copy / SKILL)
        shutil.copy2(REPO / "LICENSE", self.copy / "LICENSE")

    def tearDown(self):
        shutil.rmtree(self.temp)

    def assertFails(self, expected_message):
        result = run_checker(self.copy)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(expected_message, result.stdout)

    def test_repository_layout_passes(self):
        result = run_checker(REPO)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("skill layout: ok (competitor-analysis)", result.stdout)

    def test_copy_of_skill_folder_passes(self):
        result = run_checker(self.copy)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_old_root_layout_fails(self):
        # The layout of the first public version: SKILL.md at the root.
        shutil.move(str(self.copy / SKILL / "SKILL.md"), str(self.copy / "SKILL.md"))
        shutil.rmtree(self.copy / "skills")
        self.assertFails("no skills/<name>/SKILL.md found")
        self.assertFails("SKILL.md: SKILL.md must be at skills/<name>/SKILL.md")

    def test_name_must_match_folder(self):
        (self.copy / SKILL).rename(self.copy / "skills" / "competitor-research")
        self.assertFails("does not match folder 'competitor-research'")

    def test_licence_copy_required(self):
        (self.copy / SKILL / "LICENSE").unlink()
        self.assertFails("skills/competitor-analysis: missing LICENSE copy")

    def test_licence_copy_must_match_root(self):
        (self.copy / SKILL / "LICENSE").write_text("Different terms\n")
        self.assertFails("skills/competitor-analysis/LICENSE: differs from the root")

    def test_link_outside_skill_folder_fails(self):
        skill_md = self.copy / SKILL / "SKILL.md"
        (self.copy / "README.md").write_text("# Readme\n")
        skill_md.write_text(
            skill_md.read_text() + "\nSee [the readme](../../README.md).\n"
        )
        self.assertFails("link '../../README.md' leaves the skill folder")

    def test_reference_link_outside_skill_folder_fails(self):
        skill_md = self.copy / SKILL / "SKILL.md"
        (self.copy / "README.md").write_text("# Readme\n")
        skill_md.write_text(
            skill_md.read_text() + "\nSee [the readme][r].\n\n[r]: ../../README.md\n"
        )
        self.assertFails("link '../../README.md' leaves the skill folder")

    def test_missing_link_target_fails(self):
        (self.copy / SKILL / "references" / "method.md").unlink()
        self.assertFails("link 'references/method.md' points to a missing file")


if __name__ == "__main__":
    unittest.main()
