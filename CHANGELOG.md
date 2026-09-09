# Changelog

## 0.2.1 - 2026-09-09

Build: `0.2.1+codex.20260909122358`

- Record the v0.2.0 normal Chat E2E failure: the Skill was listed but `SKILL.md` was not loaded, so support files were not reached.
- Revert the same-repository marketplace entry to the documented `source: local` form; `git-subdir` was valid but did not make a personal installation cloud-hydratable.
- Separate personal installation, workspace GitHub import, public Plugin publication, and ChatGPT workspace Skill distribution.
- Define three independent cross-surface gates: listing, `SKILL.md` load, and support-file execution.

## 0.2.0 - 2026-09-09

Build: `0.2.0+codex.20260909031818`

- Attempt to use the official GitHub `git-subdir` source as a remote hydration source. Subsequent normal Chat E2E showed that this did not resolve personal-installation hydration; see 0.2.1.
- Separate `product` from `execution_location`; do not label Work Local as Codex Local based on shared tools.
- Add portable Markdown report packaging with copied images and rewritten in-bundle links.
- Add archive-content, absolute-path, marketplace-source, and portable-image regression tests.
- Document workspace GitHub import, resync, and fail-closed Chat/Work Cloud E2E steps.

## 0.1.0 - 2026-09-09

- Package six MIT-licensed upstream skills and add `html-review`.
- Add Codex Local, Work Local, and Work Cloud capability routing.
- Add non-fatal paper figure extraction and sequential audit fallback.
- Make `html` and `html-review` explicit-only.
- Add portable HTML and evidence-preservation tests.
