# AI Review Skills

OpenAI-native skills-only Plugin for evidence-preserving research and review in ChatGPT Chat, Work, and Codex. The existing Plugin directory is the canonical implementation for both local marketplace testing and public/universal submission; no duplicate workspace Skill is maintained.

| Skill | Dependencies |
|---|---|
| writing-quotation | none |
| documenting-with-sources | writing-quotation |
| survey | documenting-with-sources, writing-quotation; source access; optional subagents |
| paper-details | documenting-with-sources, writing-quotation; readable PDF; optional uv/Python/PyMuPDF |
| explain | optional Mermaid viewer |
| html | explain optional; browser/shared or inline assets |
| html-review | canonical Review Packet; optional Python renderer |

`ja-text-communication` and `grilling-viz` are excluded. `html` and `html-review` require explicit invocation (`@skill` in supported Chat/Work surfaces or `$skill` in Codex). `html-review` never becomes the agent-to-agent source of truth. Missing figure extraction does not stop paper text analysis and must emit `図表画像は未抽出`.

Install:

```text
codex plugin marketplace add <repository-root>
codex plugin add ai-review-skills@personal
```

The personal marketplace install is verified for Codex Local, but it does **not** guarantee Skill hydration in normal Chat or Work Cloud. In the v0.2.0 E2E test, Chat listed `ai-review-skills:paper-details` but could not load its `SKILL.md`; changing the entry from `local` to `git-subdir` did not fix that distribution boundary. The marketplace therefore uses the official same-repository `local` form again.

For managed Chat/Work distribution, a workspace administrator should import `https://github.com/hoku-ya/ai-review-skills` under **Admin > Plugins > Add > Import marketplace**, leave **Path** empty, select `main` (or leave the default branch), authorize GitHub, and review the import result. A public/universal Plugin is a separate reviewed publication path. A ChatGPT workspace Skill is also a separate lifecycle and does not inherit Plugin installation or ownership.

After any workspace import or update, select **Sync now**, start a new task, and test all three gates: (1) Skill listed, (2) `SKILL.md` loaded, and (3) referenced scripts/resources/assets usable. If a target surface cannot retrieve the selected Skill, stop; do not substitute a generic answer. A minimal E2E prompt is:

```text
Use @ai-review-skills:paper-details. First state the selected Skill name and whether its SKILL.md was loaded. If it was not loaded, stop without analyzing the PDF. If loaded, analyze the attached PDF and report product and execution_location separately.
```

When exporting a paper report with figures, run `python plugins/ai-review-skills/skills/paper-details/scripts/package_report.py <report.md> <destination-directory>` and deliver the entire destination directory, not a Markdown file alone.

Test with `python tests/run_tests.py` and the Plugin/Skill validators. See `UPSTREAM.md`, `THIRD_PARTY_LICENSES.md`, and `docs/verification-report.md`.

## Public submission status

The portable Agent Plugins 1.0 manifest is `plugins/ai-review-skills/plugin.json`; `.codex-plugin/plugin.json` remains the Codex compatibility fallback. Build the exact skills-only upload bundle with:

```text
python scripts/build_submission_bundle.py <output.zip>
```

Submission materials are in `docs/submission-checklist.md` and `docs/submission-test-cases.md`. Privacy, terms, and support disclosures are in `PRIVACY.md`, `TERMS.md`, and `SUPPORT.md`. Preparation does not mean the Plugin has been submitted, approved, or published. Chat/Work Cloud support remains unconfirmed until the published package reports `SKILL.md loaded: true` and its bundled resources pass E2E testing.

Public listing images are under `plugins/ai-review-skills/assets/`: `directory-light.png` and `directory-dark.png` are 512x512 Directory images; `composer-light.png` and `composer-dark.png` are 256x256 Composer images. The SVG sources remain alongside them.
