---
name: html-review
description: Explicitly invoked only. Convert canonical Markdown, JSON, Evidence, and test results into a human-readable HTML snapshot without making HTML the source of truth.
---

# HTML Review

Render an integrated Review Packet for human review. This projection layer does not research, judge correctness, launch agents, approve, replace tests, mutate canonical inputs, publish, or act as an agent return contract. Invoke only by explicit skill selection, never for ordinary HTML/Markdown/JSON responses.

Read `references/review-packet.schema.json` and `../../references/runtime-capabilities.md`. JSON and referenced Markdown/Evidence/tests remain canonical; HTML is `derived_snapshot`. Preserve wording, IDs, paths, URLs, timestamps, citations, verification and test states. Render absent optional values as `未提供`/`未確認`; never invent or silently omit. Reject missing/invalid canonical packets before rendering.

Keep conclusion, P0/P1, Blocked, Warning, Human Decision, and unresolved items expanded. Use semantic text, not color alone. Escape all input; do not runtime-fetch. Work/unknown outputs one offline HTML with inline CSS/JS and data-URI images (or locator plus `画像は未埋め込み`). Codex Local may reuse relative shared assets and must retain a portable option. Use one HTML writer.

When Python exists: `python scripts/render_review.py <packet.json> <output.html>`. Otherwise fill `assets/template.html` under identical rules. Validate all IDs/locators/citations/quotes/statuses, unchanged canonical hashes, no external dependencies, and truthful audit mode. Report HTML and canonical paths together; agents continue exchanging the packet, never HTML.
