# Competitor Analysis

Compare competitors and other alternatives through one important customer task. Get an evidence matrix, a decision brief, and an HTML dashboard.

## Use it

Copy this entire `competitor-analysis` folder into the skills directory supported by your agent. Keep the folder name as `competitor-analysis`; it must match the `name` in `SKILL.md`. If your agent does not load skills automatically, ask it to read `SKILL.md` and follow its relative references. Live research needs web access and permission to write files; viewing the bundled example needs only a browser. There are no API keys, paid services, package installations, or build steps.

Give the agent a target customer, their problem, your proposed value, and one critical task. For example:

> Use competitor-analysis in rapid mode. Our fictional product, GatherSlot, helps a volunteer coordinator at a neighborhood food swap assign weekly pickup shifts. Compare alternatives for the task “fill Saturday's three pickup shifts without double-booking a volunteer.” Use only the bundled fictional fixture notes and label the result as a simulation. Write the three artifacts in a new output folder.

For a real study, also state the market or language, known alternatives, and where to save the output. The agent should confirm the competitor set before deep research unless you explicitly ask it to proceed autonomously. It should not claim that marketing pages prove the full product experience.

The output folder contains `research-matrix.csv`, `competitive-analysis-brief.md`, and `dashboard.html`. The [fictional worked example](examples/fictional-food-swap/README.md) shows the expected shape and an offline fixture. It is **synthetic**, not a real study or a claim about any real market, product, or customer.

## Limits and maintenance

This is a research procedure, not a source of current market facts. Live conclusions require current, cited evidence and customer validation. Product access, paywalls, local laws, and the agent's browsing capabilities can limit what can be observed; record those limits instead of filling gaps by guesswork. The dashboard is an offline presentation of the CSV and brief, not an independent evidence source.

To update, replace the installed skill folder with a newer reviewed copy while keeping your study output elsewhere. To uninstall, remove the installed folder; your separately saved studies remain. For questions or defects, use the repository's issue tracker once this candidate has a public repository.

**License:** [MIT](LICENSE).
