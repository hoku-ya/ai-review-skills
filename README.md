# AI Review Skills

OpenAI-native skills-only Plugin for evidence-preserving research and review in ChatGPT Chat, Work, and Codex.

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

The marketplace entry uses the official `git-subdir` source so Chat and Work Cloud can hydrate the bundled Skill from GitHub instead of receiving a device-local cache path. For a managed workspace, an administrator can instead import `https://github.com/hoku-ya/ai-review-skills` under Admin > Plugins and sync it from GitHub; the repository-root marketplace layout is also valid for that route.

After updating, sync/reinstall the marketplace Plugin and start a new task. If a target surface reports that it cannot retrieve the selected Skill, stop; do not substitute a generic answer. A minimal E2E prompt is:

```text
Use @ai-review-skills:paper-details. First state the selected Skill name and whether its SKILL.md was loaded. If it was not loaded, stop without analyzing the PDF. If loaded, analyze the attached PDF and report product and execution_location separately.
```

When exporting a paper report with figures, run `python plugins/ai-review-skills/skills/paper-details/scripts/package_report.py <report.md> <destination-directory>` and deliver the entire destination directory, not a Markdown file alone.

Test with `python tests/run_tests.py` and the Plugin/Skill validators. See `UPSTREAM.md`, `THIRD_PARTY_LICENSES.md`, and `docs/verification-report.md`.
