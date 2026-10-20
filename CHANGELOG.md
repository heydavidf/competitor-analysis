# Changelog

All notable changes to this skill are listed here. Versions follow [semantic versioning](https://semver.org/).

## 1.0.0 - 2026-10-20

First tagged version. The skill's method and outputs are unchanged.

### Changed

- The skill moved from the repository root to `skills/competitor-analysis/`, so `gh skill install heydavidf/competitor-analysis competitor-analysis` can find it. If you copied the old root folder, replace your installed copy with the new folder.
- The skill folder now carries its own copy of `LICENSE`, and `SKILL.md` links to the repository README by its web address, because installed copies contain only the skill folder.
- The README leads with `gh skill install` and keeps a manual install route.

### Added

- Automatic checks on pushes to `main`, on pull requests and weekly: lint and format, tests, skill layout, example rebuild, Agent Skills format, a tripwire for personal paths and silenced checks, secret scanning and link checks.
- `AGENTS.md`, `CONTRIBUTING.md` and `SECURITY.md`.
- `.gitignore`, so study output and local caches are not committed by mistake.

## Initial release - 2026-09-28

First public version, untagged.
