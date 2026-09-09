# Runtime capability routing

Determine product and execution location from explicit task or host metadata first, then detect capabilities from exposed tools. Never infer `Codex Local` merely because files, shell, or Python exist: Work Local may expose them too. If host metadata is unavailable, record `Unknown`. Record product, execution location, used/unavailable capabilities, fallbacks, and audit mode separately.

- Codex Local: use local files, shell, Python, `uv`, image extraction, local artifacts, and subagents when available. Do not remove these accelerators for portability.
- Work Local: use only permitted local files/apps/code/shell; use cloud fallbacks when absent.
- Work Cloud: use uploaded, Project, Library, or authorized-app files plus hosted code/shell when exposed. Never assume device paths, local apps/sessions, packages, `uv`, or private networks.
- Audit: use parallel subagents when exposed; otherwise execute the identical checklist sequentially. Record `parallel-subagents` or `sequential-single-agent` truthfully.
- HTML: Work/unknown defaults to one file with inline CSS/JS and data-URI images; Codex Local may reuse shared relative CSS/JS/images and can also create a portable variant.

Use separate metadata fields when relevant: `product: Codex | Work | Chat | Unknown`, `execution_location: Local | Cloud | Unknown`, and `capabilities_used: ...`. Do not replace them with a guessed combined label.
