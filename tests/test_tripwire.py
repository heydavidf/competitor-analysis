"""Regression tests for .github/tripwire.sh.

The first version printed "tripwire: clean" and passed when the comparison
point could not be used (for example origin/main in a clone without that
remote, or a commit with no shared history), so silenced checks were never
looked for. Each test builds a small throwaway
Git repository, so nothing here touches this repository's history.

Run: python3 -B -m unittest discover -s tests -v
"""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TRIPWIRE = REPO / ".github" / "tripwire.sh"
# Built from parts so this file does not trip the tripwire itself.
SILENCED = "value = 1  # " + "noqa"
PERSONAL = "/Use" + "rs/someone/notes.txt"


class TripwireTest(unittest.TestCase):
    def setUp(self):
        self.temp = Path(tempfile.mkdtemp(prefix="tripwire-"))
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")} | {
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_AUTHOR_NAME": "Test",
            "GIT_AUTHOR_EMAIL": "test@example.invalid",
            "GIT_COMMITTER_NAME": "Test",
            "GIT_COMMITTER_EMAIL": "test@example.invalid",
        }
        self.git("init", "--quiet", "--template=", "-b", "main")
        (self.temp / ".github").mkdir()
        shutil.copy2(TRIPWIRE, self.temp / ".github" / "tripwire.sh")
        self.commit("notes.md", "Plain notes.\n")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()

    def tearDown(self):
        shutil.rmtree(self.temp)

    def git(self, *args):
        return subprocess.run(
            ["git", "-c", "core.hooksPath=" + os.devnull, *args],
            cwd=self.temp,
            env=self.env,
            capture_output=True,
            text=True,
            check=True,
        )

    def commit(self, name, text):
        (self.temp / name).write_text(text)
        self.git("add", "-A")
        self.git("commit", "--quiet", "-m", "change " + name)

    def tripwire(self, *args):
        return subprocess.run(
            ["bash", ".github/tripwire.sh", *args],
            cwd=self.temp,
            env=self.env,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_clean_change_passes(self):
        self.commit("more.md", "More plain notes.\n")
        result = self.tripwire(self.base)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("tripwire: clean", result.stdout)

    def test_missing_base_fails(self):
        result = self.tripwire("origin/main")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Could not compare with base ref 'origin/main'", result.stdout)
        self.assertNotIn("tripwire: clean", result.stdout)

    def test_unrelated_base_fails(self):
        empty_tree = self.git("hash-object", "-t", "tree", os.devnull).stdout.strip()
        unrelated = self.git(
            "commit-tree", empty_tree, "-m", "unrelated"
        ).stdout.strip()
        result = self.tripwire(unrelated)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Could not compare with base ref", result.stdout)

    def test_silenced_check_fails(self):
        self.commit("code.py", SILENCED + "\n")
        result = self.tripwire(self.base)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("New lines that silence a check", result.stdout)

    def test_tracked_database_file_fails(self):
        self.commit("cache.db", "local cache\n")
        self.commit("notes.db-journal", "journal\n")
        result = self.tripwire()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Tracked files that should be ignored", result.stdout)
        self.assertIn("cache.db", result.stdout)
        self.assertIn("notes.db-journal", result.stdout)

    def test_personal_path_fails(self):
        self.commit("paths.md", "See " + PERSONAL + "\n")
        result = self.tripwire()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("Personal paths or private words", result.stdout)


if __name__ == "__main__":
    unittest.main()
