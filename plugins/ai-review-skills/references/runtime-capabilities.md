# Runtime capability routing

Detect capabilities from tools actually exposed; never infer them from product name. Record branch, used/unavailable capabilities, fallbacks, and audit mode.

- Codex Local: use local files, shell, Python, `uv`, image extraction, local artifacts, and subagents when available. Do not remove these accelerators for portability.
- Work Local: use only permitted local files/apps/code/shell; use cloud fallbacks when absent.
- Work Cloud: use uploaded, Project, Library, or authorized-app files plus hosted code/shell when exposed. Never assume device paths, local apps/sessions, packages, `uv`, or private networks.
- Audit: use parallel subagents when exposed; otherwise execute the identical checklist sequentially. Record `parallel-subagents` or `sequential-single-agent` truthfully.
- HTML: Work/unknown defaults to one file with inline CSS/JS and data-URI images; Codex Local may reuse shared relative CSS/JS/images and can also create a portable variant.
