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

Test with `python tests/run_tests.py` and the Plugin/Skill validators. See `UPSTREAM.md`, `THIRD_PARTY_LICENSES.md`, and `docs/verification-report.md`.
