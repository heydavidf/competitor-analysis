#!/usr/bin/env python3
"""Check that every skill sits where `gh skill install` and other agents look for it.

Usage: python3 -B .github/check_skill_layout.py [REPO_DIR]

The check fails (exit 1) when:
- there is no skills/<name>/SKILL.md;
- a SKILL.md sits anywhere else, for example at the repository root (the old layout);
- the `name` in a SKILL.md front matter is not the name of its folder;
- a skill folder has no LICENSE identical to the root LICENSE;
- a relative link in a skill's Markdown (inline or reference style) points outside its
  folder or to a missing file.
  An installed copy contains only the skill folder, so such links would break.

Standard library only. skills-ref validates the rest of the Agent Skills format.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RULE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FENCE = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)
LINK = re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
REF_LINK = re.compile(r"^ {0,3}\[[^\]]+\]:\s*<?([^\s>]+)>?", re.MULTILINE)
EXTERNAL = ("http://", "https://", "mailto:", "#")


def front_matter_name(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    match = re.search(r"^name:\s*(.*?)\s*$", text[4:end], re.MULTILINE)
    return match.group(1).strip("'\"") if match else None


def check(repo: Path) -> list[str]:
    problems: list[str] = []
    skills_root = repo / "skills"
    found = sorted(
        p for p in repo.rglob("SKILL.md") if ".git" not in p.relative_to(repo).parts
    )
    expected = sorted(skills_root.glob("*/SKILL.md"))
    for stray in sorted(set(found) - set(expected)):
        problems.append(
            f"{stray.relative_to(repo)}: SKILL.md must be at skills/<name>/SKILL.md"
        )
    if not expected:
        problems.append("no skills/<name>/SKILL.md found")

    root_license = repo / "LICENSE"
    for skill_md in expected:
        folder = skill_md.parent
        rel = folder.relative_to(repo).as_posix()
        if not NAME_RULE.match(folder.name) or len(folder.name) > 64:
            problems.append(
                f"{rel}: folder name must be lowercase letters, digits and hyphens"
            )
        name = front_matter_name(skill_md.read_text(encoding="utf-8"))
        if name != folder.name:
            problems.append(
                f"{rel}/SKILL.md: front matter name {name!r} does not match "
                f"folder {folder.name!r}"
            )
        copy = folder / "LICENSE"
        if not copy.is_file():
            problems.append(f"{rel}: missing LICENSE copy")
        elif root_license.is_file() and copy.read_bytes() != root_license.read_bytes():
            problems.append(f"{rel}/LICENSE: differs from the root LICENSE")
        for md in sorted(folder.rglob("*.md")):
            text = FENCE.sub("", md.read_text(encoding="utf-8"))
            for target in LINK.findall(text) + REF_LINK.findall(text):
                if target.startswith(EXTERNAL):
                    continue
                path = (md.parent / target.split("#", 1)[0]).resolve()
                where = md.relative_to(repo).as_posix()
                if not path.is_relative_to(folder.resolve()):
                    problems.append(f"{where}: link {target!r} leaves the skill folder")
                elif not path.exists():
                    problems.append(
                        f"{where}: link {target!r} points to a missing file"
                    )
    return problems


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems = check(repo)
    for problem in problems:
        print(problem)
    if problems:
        print(f"skill layout: {len(problems)} problem(s)")
        return 1
    names = ", ".join(
        p.parent.name for p in sorted((repo / "skills").glob("*/SKILL.md"))
    )
    print(f"skill layout: ok ({names})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
