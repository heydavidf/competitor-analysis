---
name: competitor-analysis
description: Compare the alternatives a customer could use for one important task, and judge whether a proposed value has room to compete. Use when mapping direct and indirect alternatives, benchmarking a critical customer task, or pressure-testing a value proposition.
license: MIT
compatibility: Requires an agent that can browse the web for live studies and write local files. The included fictional example can be inspected offline.
---

# Competitor Analysis

Run a customer- and UX-focused competitive analysis. Preserve useful business evidence, but do not let company trivia or feature counting displace the central question: how well do current alternatives help the target customer accomplish the critical task, and where is there room for a differentiated value proposition?

Read [references/method.md](references/method.md) before research. Use [templates/dashboard.template.html](templates/dashboard.template.html) to render the final dashboard.

This procedure is original. It overlaps with the outlook in Jaime Levy's *UX Strategy*: start from a specific customer and one important task, include indirect alternatives, and take a position on the proposed value. These instructions are written for an agent. They are not a summary of the book, and no book text is included. See [README.md](README.md) for installation and a wholly fictional example.

## 1. Frame the Decision

Collect or infer from supplied context:

1. Target customer segment. For B2B, distinguish buyer from user.
2. Customer problem or desired outcome.
3. Initial value proposition or focus product being evaluated.
4. Critical customer task to benchmark. Full mode may use up to three tasks.
5. Geographic or language scope.
6. Known competitors and any required comparison dimensions.
7. Mode: `rapid` or `full`. Default to `rapid` when the user does not specify.
8. Output location. Default to `competitive-analysis-[slug]/` in the working directory, unless the user specifies a location.

Do not begin deep research without the customer, problem, value proposition, and critical task. State any inferred framing and label it as an assumption.

## 2. Choose the Research Depth

### Rapid mode

- Research 4-6 competitors in total.
- Include both direct and indirect alternatives where they exist.
- Benchmark one critical customer task using public product evidence, demonstrations, reviews, and accessible flows.
- Produce directional conclusions suitable for early product decisions.

### Full mode

- Research 8-12 competitors in total.
- Seek a panoramic mix of direct, indirect, adjacent, manual, and do-nothing alternatives.
- Benchmark one to three critical tasks. Use the product firsthand when access is lawful, ethical, practical, and does not require misrepresentation.
- Capture screenshots or stable screen/page references when they materially support UX findings.
- Deepen review-pattern, business-model, and scale evidence where relevant.

Treat these ranges as targets. Explain a smaller set when the market is genuinely thin; ask before exceeding the range.

## 3. Discover and Confirm Competitors

Search from the target customer's headspace, not only from analyst category labels:

- The words a customer would use to accomplish the task.
- Variations suggested by search results and related searches.
- Alternatives named in customer interviews, reviews, forums, comparison pages, and stakeholder material.
- Products in adjacent markets or other regions that could satisfy the same need.
- Manual workarounds, combinations of tools, and choosing not to act.

Maintain a longlist with `candidate`, `customer-task relevance`, `direct/indirect rationale`, and `include/exclude decision`.

Classify competitors by the value proposition and customer need:

- **Direct:** substantially similar value proposition for substantially the same customer.
- **Indirect:** different value proposition or solution that still satisfies all or part of the same need.
- **Adjacent/manual/do nothing:** retain as an indirect subgroup when it reveals meaningful customer behaviour or substitution.

Confirm the final set with the user before deep research unless they explicitly requested an autonomous run. Organize comparable competitors into logical subgroups.

## 4. Build the Research Matrix

Research the same relevant dimensions across comparable competitors. Every factual claim needs a source URL and access date. Distinguish:

- `Observed`: directly visible in the product or a primary source.
- `Claimed`: stated by the competitor.
- `Reported`: stated by a customer or third party.
- `Inferred`: analyst interpretation based on cited evidence.

Use confidence `High`, `Medium`, or `Low`. Record `Not found` or `Not applicable` instead of guessing.

### Always collect

- Competitor name, type, subgroup, geography, and product URL.
- Why it competes for this customer and task.
- Value proposition and relevant customer segment.
- Relevant business/revenue model.
- Critical-task UX benchmark: entry point, steps, friction, strengths, weaknesses, outcome, and evidence.
- Top two competitive advantages or key differentiators, including how easily they appear replicable.
- Relevant customer-review patterns, with isolated anecdotes separated from recurring themes.
- Competitor-perspective SWOT focused on the value proposition and customer experience.
- Sources, access dates, evidence type, and confidence.

### Collect when relevant

- Year founded, funding, acquisitions, traffic, downloads, adoption, listings, users, or other scale signals.
- Pricing and notable limits.
- Primary categories, content types, personalization, UGC, crowdsourced data, social activity, and recent news.
- Security, integrations, ecosystem, regulatory, or regional attributes required by the category.

Do not pad empty or irrelevant columns merely because they appeared in an earlier analysis.

## 5. Benchmark and Analyze

1. Check the matrix for missing load-bearing evidence and conflicting sources.
2. Group like competitors and compare attribute by attribute.
3. Identify competitive parity: the baseline experience customers will expect.
4. Identify repeated UX conventions, friction, strengths, weaknesses, business-model patterns, and gaps.
5. Rank the most threatening competitors within direct and indirect groups. State why each is threatening.
6. Complete SWOT from each competitor's perspective. For an indirect competitor, analyze only the relevant portion of its offering.
7. Decide whether the marketplace is:
   - **Red:** crowded, mature alternatives with little obvious unmet space.
   - **Purple:** meaningful competition plus credible gaps or underserved segments.
   - **Blue:** limited direct competition and evidence of an underserved need. Lack of competitors alone is not proof of demand.

Keep the feature comparison tied to the critical task. Use `Yes`, `Partial`, `No`, or `Not observed`; use `Superior` only when comparative evidence defines why. Never recommend a feature merely because competitors have it.

### Contextual supplementary lenses

Include these only when they materially affect the value proposition, and label them `Supplementary`:

- **Pricing comparison:** when price, packaging, or monetization shapes customer choice.
- **Moat assessment:** when switching costs, network effects, proprietary data, brand, or technical advantage changes threat or replicability.
- **Positioning map:** when two evidence-derived axes clarify meaningful strategic clusters. Define both poles and cite the evidence behind placement. Do not invent decorative axes.

## 6. Take a Stand

The conclusion must state:

- Marketplace verdict and supporting evidence.
- Two or three most threatening competitors.
- Competitive parity the product must meet.
- The strongest unmet need or opportunity gap.
- Whether to continue, refine, pivot, or conduct more validation.
- The smallest differentiated value proposition or critical experience worth testing next.
- The key uncertainty and the next customer-facing experiment needed to reduce it.

Do not turn desk research into proof of product-market fit. Recommendations are hypotheses until validated with target customers.

## 7. Create the Artifacts

Create one folder containing exactly these primary artifacts:

### `research-matrix.csv`

The canonical raw evidence. Use one competitor per row. Quote fields containing commas or line breaks. Include a `sources` field with human-readable source names and URLs, separated consistently. Keep detailed evidence concise enough to scan.

### `competitive-analysis-brief.md`

Use this order:

1. Decision context and research scope.
2. Executive summary.
3. Marketplace verdict.
4. Most threatening competitors.
5. Direct competitor findings.
6. Indirect and substitute findings.
7. Critical-task UX benchmark and task-based feature comparison.
8. Business-model patterns.
9. Contextual supplementary lenses, only if relevant.
10. Opportunity, recommendation, and next validation step.
11. Limitations and unresolved evidence gaps.
12. Sources.

### `dashboard.html`

Copy the dashboard template and replace the single `__DASHBOARD_DATA__` token with JSON matching this contract:

```json
{
  "title": "Category or product",
  "targetCustomer": "Specific segment",
  "problem": "Customer problem",
  "valueProposition": "Initial value proposition",
  "criticalTask": "Task benchmarked",
  "mode": "rapid or full",
  "geography": "Scope",
  "date": "YYYY-MM-DD",
  "verdict": "Red, Purple, or Blue",
  "verdictRationale": "Evidence-based rationale",
  "topThreat": {"name": "Competitor", "why": "Reason"},
  "opportunity": {"label": "Gap", "evidence": "Supporting evidence"},
  "recommendation": {"summary": "Decision", "nextTest": "Experiment"},
  "matrixColumns": ["name", "type", "subgroup", "uxGrade", "confidence"],
  "competitors": [{"name": "Competitor", "type": "Direct", "subgroup": "Group", "rank": 1, "whyCompetes": "Reason", "valueProposition": "Promise", "uxGrade": "B", "strength": "Evidence", "friction": "Evidence", "confidence": "High"}],
  "sources": [{"name": "Source title", "url": "https://example.com", "accessed": "YYYY-MM-DD"}]
}
```

Additional competitor fields named in `matrixColumns` are allowed. Serialize the JSON with `<` escaped as `\u003c` so research text cannot terminate the script element. The dashboard is a synchronized presentation layer, not a new analysis. It must:

- Lead with verdict, threats, gaps, recommendation, and next test.
- Show competitor cards and critical-task evidence.
- Provide filters for competitor type and subgroup.
- Show the full matrix and clickable sources.
- Contain only claims and values already present in the CSV or brief.
- Embed all data and assets. Do not require a server, fetch local files, or depend on external libraries.

## 8. Verify Before Delivery

- Confirm competitor names, types, numbers, verdict, recommendation, and sources agree across all three artifacts.
- Reopen the CSV and verify every row has a source, access date, evidence type, and confidence.
- Search all outputs for unfinished placeholders, `__DASHBOARD_DATA__`, unsupported claims, and broken links.
- Open `dashboard.html` locally. Check overview, filters, competitor details, matrix, source links, keyboard navigation, and narrow-screen layout. A local example may cite bundled fixture files with `./` relative links.
- State clearly where evidence is missing, old, paywalled, or inferred.

## Writing Rules

- Be specific, concise, balanced, and evidence-led.
- Prefer primary sources for product claims, pricing, funding, and company facts. Use independent sources and customer evidence to challenge competitor claims.
- Cite the source nearest to the claim in the brief.
- Quantify only when a reliable source and date are available.
- Use recent evidence for volatile facts; do not discard older evidence that directly documents a stable product or historical event.
- No em dashes. Use commas, full stops, or colons.
- Do not editorialize in favor of the focus product.
- Do not use confidential information, impersonate customers, evade access controls, or share login credentials.
