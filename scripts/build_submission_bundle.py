"""Build a review-uploadable ZIP from the canonical Plugin directory."""

from pathlib import Path
import argparse
import json
import zipfile


REQUIRED = {
    "plugin.json",
    ".codex-plugin/plugin.json",
    "LICENSE",
    "THIRD_PARTY_LICENSES.md",
    "assets/icon.svg",
    "assets/logo.svg",
    "skills/writing-quotation/SKILL.md",
    "skills/documenting-with-sources/SKILL.md",
    "skills/survey/SKILL.md",
    "skills/paper-details/SKILL.md",
    "skills/explain/SKILL.md",
    "skills/html/SKILL.md",
    "skills/html-review/SKILL.md",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    plugin = repo / "plugins" / "ai-review-skills"
    portable = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
    compatibility = json.loads(
        (plugin / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    if portable["name"] != compatibility["name"]:
        raise SystemExit("manifest name mismatch")
    if portable["version"] != compatibility["version"]:
        raise SystemExit("manifest version mismatch")

    files = [
        path
        for path in plugin.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    ]
    names = {path.relative_to(plugin).as_posix() for path in files}
    missing = REQUIRED - names
    if missing:
        raise SystemExit("missing required files: " + ", ".join(sorted(missing)))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, path.relative_to(plugin).as_posix())
    print(f"wrote {args.output} ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
