#!/usr/bin/env python3
"""Create a portable Markdown directory and copy referenced local images."""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

IMAGE_RE = re.compile(r"(!\[[^\]]*\]\()([^)]+)(\))")


def package(source: Path, destination: Path) -> Path:
    source = source.resolve(strict=True)
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    assets = destination / "assets"
    assets.mkdir(exist_ok=True)
    markdown = source.read_text(encoding="utf-8")
    copied: dict[Path, str] = {}

    def replace(match: re.Match[str]) -> str:
        raw = match.group(2).strip().strip("<>")
        if raw.startswith(("http://", "https://", "data:")):
            return match.group(0)
        local = (source.parent / unquote(raw)).resolve(strict=True)
        if not local.is_file():
            raise FileNotFoundError(f"referenced image is not a file: {local}")
        if local not in copied:
            digest = hashlib.sha256(str(local).encode("utf-8")).hexdigest()[:8]
            name = f"{local.stem}-{digest}{local.suffix.lower()}"
            shutil.copy2(local, assets / name)
            copied[local] = name
        return f"{match.group(1)}assets/{copied[local]}{match.group(3)}"

    rewritten = IMAGE_RE.sub(replace, markdown)
    output = destination / source.name
    output.write_text(rewritten, encoding="utf-8")
    for name in copied.values():
        if not (assets / name).is_file():
            raise RuntimeError(f"portable image missing after copy: {name}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    print(package(args.report, args.destination))


if __name__ == "__main__":
    main()
