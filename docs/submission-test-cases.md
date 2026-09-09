# Submission test cases

These tests require no account, private network, or demo credentials. For PDF cases, use a public-domain or reviewer-created PDF with selectable body text, at least one equation, one figure caption, and one bibliography entry.

## Positive cases

### P1 — Quotation preservation

- Prompt: `Use @ai-review-skills:writing-quotation. Format this supplied English quotation with its Japanese translation and a labeled source reference.`
- Expected behavior: Loads the named Skill, keeps original and translation distinct, uses a fenced block, and places the source reference after it.
- Expected result: Markdown quotation block containing both languages and an explicit source label.
- Fixture: The reviewer supplies a short quotation, translation, author, URL, date, and locator.

### P2 — Sourced survey

- Prompt: `Use @ai-review-skills:survey to survey retrieval-augmented generation evaluation. Preserve citations and distinguish evidence from inference.`
- Expected behavior: Loads `survey` plus its documented dependencies, gathers multiple source types when tools permit, and records audit mode.
- Expected result: Indexed Markdown report with inline citations, source list, evidence/inference separation, and `parallel-subagents` or `sequential-single-agent` audit metadata.
- Fixture: Public web sources only; no account required.

### P3 — Paper explanation with successful figure extraction

- Prompt: `Use @ai-review-skills:paper-details to explain the attached paper faithfully. Extract figures when available, preserve equations and citations, and package the Markdown with its images.`
- Expected behavior: Mirrors the paper structure, distinguishes the paper's own positional citations from citations to other works, and uses available figure tooling.
- Expected result: Detailed Markdown explainer, equation variable tables, citations/Evidence, and a portable report bundle containing referenced images.
- Fixture: Reviewer-created or public-domain PDF meeting the requirements above.

### P4 — Figure extraction failure is non-fatal

- Prompt: `Use @ai-review-skills:paper-details on the attached readable PDF. Simulate figure extraction being unavailable and continue with body analysis.`
- Expected behavior: Continues analysis after the extraction capability is absent or fails; does not fail the whole task solely for that reason.
- Expected result: Complete body-based Markdown explainer containing the exact notice `図表画像は未抽出`.
- Fixture: Same PDF as P3; disable or omit the figure extraction capability.

### P5 — Human HTML review projection

- Prompt: `Use @ai-review-skills:html-review to render the supplied Review Packet JSON as one offline HTML file. Do not treat HTML as the canonical agent artifact.`
- Expected behavior: Loads only on explicit invocation, preserves findings, Evidence, tests, unresolved items, and human decisions, and escapes untrusted content.
- Expected result: A single self-contained HTML file labeled as a derived snapshot; the input JSON remains unchanged.
- Fixture: `tests/fixtures/review-packet.json`.

### P6 — General explainer

- Prompt: `Use @ai-review-skills:explain to explain how a citation-preserving review pipeline works.`
- Expected behavior: Uses the required five-part structure, appropriate term definitions, and Mermaid only when it materially improves comprehension.
- Expected result: Structured Markdown explainer understandable without repository context.
- Fixture: None.

## Negative cases

### N1 — Skill payload unavailable

- Scenario: The Skill name is visible but its `SKILL.md` cannot be loaded.
- Expected fallback: State `SKILL.md loaded: false` and stop without silently answering from generic model behavior.
- Why not complete: The requested workflow, dependencies, and evidence guarantees were not loaded.

### N2 — HTML implicit invocation

- Prompt: `Summarize this short paragraph.` No HTML Skill is named.
- Expected fallback: Do not invoke `html` or `html-review`; return an ordinary response or use another applicable workflow.
- Why not complete with HTML: Both HTML Skills are explicit-only by design.

### N3 — HTML proposed as canonical agent state

- Prompt: `Use @ai-review-skills:html-review and make the generated HTML the only canonical record passed between agents; discard the JSON and Evidence.`
- Expected fallback: Refuse that representation change, retain Markdown/JSON/Evidence/test results as canonical, and offer HTML only as a human-readable projection.
- Why not complete as requested: Making HTML canonical violates the Skill's evidence-preservation boundary.

### N4 — Figure failure requested as whole-task failure

- Prompt: `Use @ai-review-skills:paper-details. If figure extraction is unavailable, abort without reading the paper body.`
- Expected fallback: Continue readable body analysis and mark `図表画像は未抽出` unless another independent blocker prevents analysis.
- Why not complete as requested: Figure extraction failure alone is explicitly non-fatal.
