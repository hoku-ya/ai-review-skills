# Public Plugin submission checklist

Status: **submission package prepared; not submitted; not published**.

Official references:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/app-guidelines
- https://developers.openai.com/plugins/guides/security-privacy

## Package

- [x] Skills-only Plugin; no MCP server, authentication, UI component, or remote developer service.
- [x] Portable Agent Plugins 1.0 `plugin.json` at the Plugin root.
- [x] `.codex-plugin/plugin.json` retained as the Codex compatibility fallback.
- [x] Seven existing Skills preserved under `skills/`, including their scripts, references, templates, assets, and explicit-invocation metadata.
- [x] MIT license and upstream attribution retained.
- [x] Final bundle can be produced by `scripts/build_submission_bundle.py` and verified by `tests/run_tests.py`.
- [x] No secrets, credentials, telemetry, developer endpoint, or fixed user-profile path in the Plugin package.

## Public listing

- [x] Name: `AI Review Skills`.
- [x] Category: `Productivity`.
- [x] Short and long descriptions prepared in both manifests.
- [x] Directory Light/Dark PNGs are bundled at 512x512; Composer Light/Dark PNGs are bundled at 256x256. The portable manifest references the Light PNGs, and the corresponding Dark PNGs are ready for the separate submission-form fields.
- [x] Website, repository, support, privacy, and terms destinations defined.
- [x] Repository, README, LICENSE, privacy, terms, and support content are anonymously reachable; verified through public GitHub/raw URLs on 2026-09-09.
- [ ] Publisher name and public URLs confirmed to match the verified developer identity selected in OpenAI Platform.

Verified public URLs:

- Website/repository: https://github.com/hoku-ya/ai-review-skills
- Support: https://github.com/hoku-ya/ai-review-skills/blob/main/SUPPORT.md
- Privacy: https://github.com/hoku-ya/ai-review-skills/blob/main/PRIVACY.md
- Terms: https://github.com/hoku-ya/ai-review-skills/blob/main/TERMS.md

## Portal fields

- [x] Submission type: `Skills only`.
- [x] Starter prompts prepared in the portable manifest.
- [x] At least five positive and three negative reviewer-reproducible test cases prepared in `docs/submission-test-cases.md`.
- [x] Initial release notes prepared below.
- [ ] Countries/regions selected by the publisher.
- [ ] Apps Management write permission confirmed for the submitting OpenAI Platform organization.
- [ ] Individual or business developer identity verified in that same organization.
- [ ] Final skill bundle uploaded and automated scan passed.
- [ ] Listing, prompts, tests, availability, and policy attestations reviewed by the publisher.
- [ ] `Submit for Review` selected.
- [ ] OpenAI review approved.
- [ ] Approved version published to the universal Plugins Directory.
- [ ] New Chat and Work Cloud tasks confirm `SKILL.md loaded: true` and exercise bundled resources.

## Initial release notes

Initial public submission of a skills-only Plugin containing seven evidence-preserving research and review workflows. It includes sourced Markdown conventions, surveys, faithful paper explanations, general explainers, portable HTML generation, and Review Packet-to-HTML projection. The package has no MCP server or developer-operated data service. Reviewers should note that figure extraction is capability-dependent and non-fatal, `html` and `html-review` require explicit invocation, and HTML is never the agent-to-agent source of truth.

## Stop conditions

Do not mark the Plugin as submitted until the portal confirms submission. Do not mark it as published until OpenAI approves it and the publisher explicitly publishes the approved version. Do not claim Chat/Work Cloud compatibility until a published or reviewer-hosted package passes all three E2E gates: Skill listed, `SKILL.md` loaded, and bundled support files usable.
