# Verification report

Date: 2026-09-09 JST. Codex Local and Work Local paper-details execution were confirmed by the user; Work Local completed PDF analysis, figure extraction, Markdown, and section audit. Normal Chat and Work Cloud showed the Plugin/Skills but failed to retrieve SKILL.md. The post-fix Chat/Work Cloud E2E remains `未確認`. Official basis: [Plugins](https://learn.chatgpt.com/docs/plugins), [Build skills](https://learn.chatgpt.com/docs/build-skills), and [Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

Candidate build: `0.2.0+codex.20260909031818`.

## Root cause and fix

The installed local cache contained every SKILL.md, reference, script, and asset, so the bundle itself was not missing. The personal marketplace entry used `source: local`; normal Chat then tried to load a Windows cache path that a non-local runtime cannot access. This is a distribution-path mismatch. `source: local` remains valid for a marketplace imported from the same GitHub repository and was not considered generally invalid. For this personal cross-surface route, the entry now uses the officially supported `git-subdir` form with repository URL, subdirectory, and `main` ref. This gives the installer a remote hydration source. Chat/Work Cloud success must still be confirmed after reinstall in a new task.

Work Local was mislabeled because capability detection treated filesystem/Python as proof of Codex Local. Metadata now requires separate `product` and `execution_location` values from host/task context, falling back to `Unknown` rather than guessing.

The broken copied report resulted from copying Markdown without its `images-from-papers` sibling. `package_report.py` now copies each referenced local image into `assets/`, rewrites the links, and verifies the files.

## Tests

Plugin validator, all seven Skill validators, Python compilation, and `tests/run_tests.py` passed locally for the candidate build. The suite checks structure/dependencies, explicit-only metadata, PDF fallback, audit routing, canonical inputs, offline HTML, Evidence, a zip/archive-equivalent inventory, absence of local absolute paths, the remote-hydratable marketplace source, and portable Markdown image links. The existing `new-chat-2/outputs/2510.04618v3.md` was checked separately: seven image links, zero missing files. Post-fix Chat/Work Cloud invocation remains unconfirmed.

Audit execution: three read-only subagents were launched in parallel for upstream/license/dependencies, Plugin/Work compatibility, and html-review design. Findings returned, but final turns hit the usage limit. The main agent completed the same checklist sequentially. Effective completion mode: `sequential-single-agent` after a documented parallel attempt.

## Capability comparison

| Capability | Codex Local | Work Local | Work Cloud |
|---|---|---|---|
| Plugin instructions | 同等 | 同等（実機確認） | 未確認（修正後E2E待ち） |
| Provided/uploaded files | 同等 | 同等 | 同等 |
| Direct device files | 同等 | 条件付きで同等 | 代替手段あり |
| Local apps/browser sessions | 同等 | 条件付きで同等 | 利用不可 |
| Code/Shell/Python | 同等 | 未確認 | 未確認 |
| uv | 利用不可（今回のhost） | 未確認 | 未確認 |
| PDF body analysis | 同等 | 同等（実機確認） | 未確認 |
| Figure extraction | 条件付きで同等 | 同等（実機確認） | 未確認 |
| Figure-failure continuation | 同等 | 同等（指示経路） | 同等（指示経路） |
| Parallel subagents | 同等（利用可） | 未確認 | 未確認 |
| Sequential audit | 同等 | 同等 | 同等 |
| Portable Markdown + images | 同等 | 同等（package path） | 代替手段あり |
| Shared CSS/images | 同等 | 条件付きで同等 | 代替手段あり |
| Offline single HTML | 同等 | 同等 | 同等 |
| Live explicit invocation | 未確認 | 未確認 | 未確認 |

## Work migration differences

No Codex feature was removed from the Plugin. Work Cloud cannot directly inherit device files/apps/browser sessions; use uploads, Project/Library, or an authorized app, and retain Codex for local/private workflows. Python/uv/PyMuPDF and subagents vary by exposed tools/policy; use body-only analysis with the extraction notice and the identical sequential audit checklist. Cloud cannot rely on shared local assets or fixed local paths; inline assets in one HTML and return a generated file. These differences are why the Codex Local paths remain necessary.
