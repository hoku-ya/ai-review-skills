# Verification report

Date: 2026-09-09 JST. Codex Local and Work Local paper-details execution were confirmed by the user; Work Local completed PDF analysis, figure extraction, Markdown, and section audit. Normal Chat and Work Cloud showed the Plugin/Skills but failed to retrieve SKILL.md. After the v0.2.0 `git-subdir` change and reinstall, normal Chat again listed `ai-review-skills:paper-details` but reported `SKILL.md loaded: false` and attempted a Windows personal-cache path. It saw the PDF but correctly stopped before analysis. Chat/Work Cloud compatibility is therefore **not fixed**. Official basis: [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins), [Skill controls](https://learn.chatgpt.com/docs/enterprise/skills), [Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management), and [Submit plugins](https://developers.openai.com/plugins/deploy/submission).

Candidate build: `0.2.1+codex.20260909122358`.

## Root cause and fix

The installed local cache contained every SKILL.md, reference, script, and asset, so the bundle itself was not missing. The failure is at the distribution boundary: a personal installation exposed Skill metadata to normal Chat, while its executable content still resolved to a device-local cache path unavailable to the remote runtime. `git-subdir` is a valid marketplace source, but the v0.2.0 E2E proves it does not turn this personal installation into a cloud-hydrated package. The repository now returns to the officially documented `source: local` form for a Plugin in the same marketplace repository. No further manifest-source changes are justified without new product evidence.

Distribution routes are separate:

| Route | Intended boundary | Current conclusion |
|---|---|---|
| Personal marketplace install | Local Codex development/install | Codex Local verified; normal Chat/Work Cloud hydration cannot be guaranteed |
| Workspace GitHub marketplace import | Admin-managed Chat/Work workspace distribution and sync | Officially supported; requires admin import/GitHub authorization; E2E not yet performed |
| Public/universal Plugin | Public directory shared by ChatGPT and Codex | Official submission/review path; not submitted |
| ChatGPT workspace Skill | Workspace-owned focused workflow | Separate ownership/lifecycle; possible alternative, but not equivalent to installing this Plugin |

Work Local was mislabeled because capability detection treated filesystem/Python as proof of Codex Local. Metadata now requires separate `product` and `execution_location` values from host/task context, falling back to `Unknown` rather than guessing.

The broken copied report resulted from copying Markdown without its `images-from-papers` sibling. `package_report.py` now copies each referenced local image into `assets/`, rewrites the links, and verifies the files.

## Tests

Plugin validator, all seven Skill validators, Python compilation, and `tests/run_tests.py` passed locally for this candidate build. The suite checks structure/dependencies, explicit-only metadata, PDF fallback, audit routing, canonical inputs, offline HTML, Evidence, a zip/archive-equivalent inventory, absence of local absolute paths, the same-repository marketplace source, and portable Markdown image links. The existing `new-chat-2/outputs/2510.04618v3.md` was checked separately: seven image links, zero missing files.

Cross-surface gates are independent:

| Gate | Normal Chat personal v0.2.0 | Work Cloud personal | Codex Local | Work Local |
|---|---|---|---|---|
| 1. Skill listed | PASS | PASS (earlier user test) | PASS | PASS |
| 2. `SKILL.md` loaded | **FAIL** | **FAIL** (earlier user test) | PASS | PASS |
| 3. scripts/references/assets usable | BLOCKED (gate 2) | BLOCKED (gate 2) | PASS | PASS for exercised paper path |

Audit execution: three read-only subagents were launched in parallel for upstream/license/dependencies, Plugin/Work compatibility, and html-review design. Findings returned, but their final turns hit the usage limit. On the resumed compatibility audit, all three existing subagents were still stopped by the usage limit, so the main agent completed the same checklist sequentially. Effective completion mode: `sequential-single-agent` after documented parallel attempts.

## Capability comparison

| Capability | Codex Local | Work Local | Work Cloud |
|---|---|---|---|
| Plugin instructions | 同等 | 同等（実機確認） | 利用不可（personal経路の実機結果。workspace/public経路は未確認） |
| Provided/uploaded files | 同等 | 同等 | 同等 |
| Direct device files | 同等 | 条件付きで同等 | 代替手段あり |
| Local apps/browser sessions | 同等 | 条件付きで同等 | 利用不可 |
| Code/Shell/Python | 同等 | 未確認 | 未確認 |
| uv | 利用不可（今回のhost） | 未確認 | 未確認 |
| PDF body analysis | 同等 | 同等（実機確認） | 代替手段あり（Plugin Skill未読でも一般PDF機能は別。Skill準拠E2Eは未確認） |
| Figure extraction | 条件付きで同等 | 同等（実機確認） | 未確認 |
| Figure-failure continuation | 同等 | 同等（指示経路） | 未確認（SKILL.md未読） |
| Parallel subagents | 同等（利用可） | 未確認 | 未確認 |
| Sequential audit | 同等 | 同等 | 同等 |
| Portable Markdown + images | 同等 | 同等（package path） | 代替手段あり |
| Shared CSS/images | 同等 | 条件付きで同等 | 代替手段あり |
| Offline single HTML | 同等 | 同等 | 同等 |
| Live explicit invocation | 同等 | 同等（paper-details実機確認） | 利用不可（personal経路、Skill選択のみ成功） |

## Work migration differences

No Codex feature was removed from the Plugin. Work Cloud cannot directly inherit device files/apps/browser sessions; use uploads, Project/Library, or an authorized app, and retain Codex for local/private workflows. Python/uv/PyMuPDF and subagents vary by exposed tools/policy; once the Skill is actually loaded, use body-only analysis with the extraction notice and the identical sequential audit checklist. Cloud cannot rely on shared local assets or fixed local paths; inline assets in one HTML and return a generated file.

The additional loss observed when moving from the personal Codex installation to normal Chat/Work Cloud is the entire bundled instruction/resource layer: the UI can list the Skill, but the remote runtime cannot load its device-cache `SKILL.md`, so dependencies, evidence rules, figure-failure continuation, and bundled scripts/assets cannot be guaranteed. The cause is the personal-to-cloud distribution boundary, not missing repository files. The workaround is an admin-managed Workspace GitHub import, public Plugin publication, or separate ChatGPT workspace Skill distribution. Codex Local must remain supported because it is the verified path for local files, shared assets, Python helpers, figure extraction, and local output packaging.

## Public/universal submission preparation

Build `0.3.0+codex.20260909125944` adds a portable Agent Plugins 1.0 root manifest while retaining the Codex compatibility manifest. The skills-only upload tree contains all seven Skill entrypoints, references, scripts, HTML assets, the Plugin license, upstream MIT notice, and a logo. Submission materials include public-listing copy, privacy/terms/support disclosures, release notes, and six positive/four negative reviewer tests. The portable manifest validated against the live Agent Plugins 1.0 JSON Schema; Plugin and Skill validators and the local regression suite remain separate gates.

Preparation status is not submission status. After the publisher changed repository visibility, anonymous access to README, LICENSE, privacy, terms, and support content was verified through public GitHub/raw URLs on 2026-09-09. OpenAI Platform Apps Management write access, publisher identity verification, country selection, bundle upload/scan, attestations, review submission, approval, and publication require the publisher's account actions and remain unchecked. Chat/Work Cloud still requires a post-publication E2E with `SKILL.md loaded: true`; no current result is reclassified.
