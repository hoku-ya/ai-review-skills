# Changelog

## 0.2.0 - 2026-09-09

Build: `0.2.0+codex.20260909031818`

- Change the personal marketplace entry to an official GitHub `git-subdir` source so non-local surfaces have a remote hydration source instead of a device cache path.
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
