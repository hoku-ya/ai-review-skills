# Verification report

Date: 2026-09-09 JST. Tested environment: Codex Local on Windows. Work Local and Work Cloud were not executed and remain `未確認`. Official basis: [Plugins](https://developers.openai.com/plugins), [Work overview](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-overview), [Sandbox](https://learn.chatgpt.com/docs/sandboxing).

## Tests

Plugin validator, all seven Skill validators, Python compilation, and `tests/run_tests.py` passed locally. The suite checks structure/dependencies, explicit-only metadata, PDF body reading, forced figure-extraction failure with continued body output and `図表画像は未抽出`, audit routing, unchanged canonical Markdown/JSON input, offline single HTML, escaping, citations, quotes, Evidence IDs/locators/states, and test statuses. Live invocation on Chat/Work/Codex and Work E2E remain unconfirmed.

Audit execution: three read-only subagents were launched in parallel for upstream/license/dependencies, Plugin/Work compatibility, and html-review design. Findings returned, but final turns hit the usage limit. The main agent completed the same checklist sequentially. Effective completion mode: `sequential-single-agent` after a documented parallel attempt.

## Capability comparison

| Capability | Codex Local | Work Local | Work Cloud |
|---|---|---|---|
| Plugin instructions | 同等 | 条件付きで同等 | 条件付きで同等 |
| Provided/uploaded files | 同等 | 同等 | 同等 |
| Direct device files | 同等 | 条件付きで同等 | 代替手段あり |
| Local apps/browser sessions | 同等 | 条件付きで同等 | 利用不可 |
| Code/Shell/Python | 同等 | 未確認 | 未確認 |
| uv | 利用不可（今回のhost） | 未確認 | 未確認 |
| PDF body analysis | 同等 | 未確認 | 未確認 |
| Figure extraction | 条件付きで同等 | 未確認 | 未確認 |
| Figure-failure continuation | 同等 | 同等（指示経路） | 同等（指示経路） |
| Parallel subagents | 同等（利用可） | 未確認 | 未確認 |
| Sequential audit | 同等 | 同等 | 同等 |
| Local durable save | 同等 | 条件付きで同等 | 代替手段あり |
| Shared CSS/images | 同等 | 条件付きで同等 | 代替手段あり |
| Offline single HTML | 同等 | 同等 | 同等 |
| Live explicit invocation | 未確認 | 未確認 | 未確認 |

## Work migration differences

No Codex feature was removed from the Plugin. Work Cloud cannot directly inherit device files/apps/browser sessions; use uploads, Project/Library, or an authorized app, and retain Codex for local/private workflows. Python/uv/PyMuPDF and subagents vary by exposed tools/policy; use body-only analysis with the extraction notice and the identical sequential audit checklist. Cloud cannot rely on shared local assets or fixed local paths; inline assets in one HTML and return a generated file. These differences are why the Codex Local paths remain necessary.
