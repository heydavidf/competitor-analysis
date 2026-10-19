# Competitor Analysis

Compare competitors and other alternatives through one important customer task. Get an evidence matrix, a decision brief, and an HTML dashboard.

## Install

With the [GitHub CLI](https://cli.github.com/), install the skill for Claude Code:

```sh
gh skill install heydavidf/competitor-analysis competitor-analysis --agent claude-code --scope user
```

For Codex use `--agent codex`, and for Grok use `--agent grok`. `gh skill install --help` lists the other supported agents. With `--scope user` the skill goes to `~/.claude/skills/competitor-analysis` for Claude Code, `~/.agents/skills/competitor-analysis` for Codex and `~/.grok/skills/competitor-analysis` for Grok. `gh skill` is in preview, so its commands may change; this was tested with GitHub CLI 2.100.0. Without a version, `gh skill install` takes the latest release, or `main` if there is no release yet. To pin a version, write `competitor-analysis@v1.0.0` instead of `competitor-analysis`.

Without the GitHub CLI, clone this repository and copy the `skills/competitor-analysis` folder into the skills folder your agent reads. Keep the folder name `competitor-analysis`; it must match the `name` in `SKILL.md`. If your agent does not load skills automatically, ask it to read `SKILL.md` and follow its relative references.

Or ask your agent: "Install the competitor-analysis skill from https://github.com/heydavidf/competitor-analysis by following its README, then check that you can find it."

**Changed in 1.0.0:** the skill moved from the repository root to `skills/competitor-analysis/`. If you copied the old root folder, replace your installed copy with the new `skills/competitor-analysis` folder.

## Use it

Live research needs web access and permission to write files; viewing the bundled example needs only a browser. There are no API keys, paid services, package installations, or build steps.

Give the agent a target customer, their problem, your proposed value, and one critical task. For example:

> Use competitor-analysis in rapid mode. Our fictional product, GatherSlot, helps a volunteer coordinator at a neighborhood food swap assign weekly pickup shifts. Compare alternatives for the task “fill Saturday's three pickup shifts without double-booking a volunteer.” Use only the bundled fictional fixture notes and label the result as a simulation. Write the three artifacts in a new output folder.

The fixture notes for this example are in the repository at `examples/fictional-food-swap/fixtures/`, not in the installed skill folder, so point your agent at a clone of the repository when you try it.

For a real study, also state the market or language, known alternatives, and where to save the output. The agent should confirm the competitor set before deep research unless you explicitly ask it to proceed autonomously. It should not claim that marketing pages prove the full product experience.

The output folder contains `research-matrix.csv`, `competitive-analysis-brief.md`, and `dashboard.html`. The [fictional worked example](examples/fictional-food-swap/README.md) shows the expected shape and an offline fixture. It is **synthetic**, not a real study or a claim about any real market, product, or customer.

## Limits and maintenance

This is a research procedure, not a source of current market facts. Live conclusions require current, cited evidence and customer validation. Product access, paywalls, local laws, and the agent's browsing capabilities can limit what can be observed; record those limits instead of filling gaps by guesswork. The dashboard is an offline presentation of the CSV and brief, not an independent evidence source.

To update, run `gh skill update competitor-analysis`, or replace the installed folder with a newer copy of `skills/competitor-analysis`. Keep your study output elsewhere. To uninstall, remove the installed folder; your separately saved studies remain.

For questions or defects, open an issue in this repository. Report security problems privately as described in [SECURITY.md](SECURITY.md). To change the skill, read [CONTRIBUTING.md](CONTRIBUTING.md); coding agents should start with [AGENTS.md](AGENTS.md). Changes are listed in [CHANGELOG.md](CHANGELOG.md).

**License:** [MIT](LICENSE).
