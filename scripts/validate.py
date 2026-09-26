#!/usr/bin/env python3
"""Validate Markdown metadata, local links, and the generated LLM index."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_llms import DOCS, ROOT, markdown_pages, read_frontmatter, render_index

REQUIRED_FIELDS = ("title", "topic", "last_updated")
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def validate_frontmatter(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        metadata = read_frontmatter(path)
    except (OSError, ValueError) as exc:
        return [str(exc)]

    for field in REQUIRED_FIELDS:
        if not metadata.get(field):
            errors.append(f"{path.relative_to(ROOT)}: missing {field} in frontmatter")

    updated = metadata.get("last_updated", "")
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", updated):
            raise ValueError
        date.fromisoformat(updated)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: last_updated must be a real YYYY-MM-DD date")
    return errors


def validate_local_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in LINK_PATTERN.finditer(text):
        raw_target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(raw_target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        if not target.is_file():
            errors.append(f"{path.relative_to(ROOT)}: broken local link {raw_target}")
    return errors


def main() -> int:
    errors: list[str] = []
    pages = markdown_pages()
    for page in pages:
        errors.extend(validate_frontmatter(page))
        errors.extend(validate_local_links(page))

    index = ROOT / "llms.txt"
    try:
        if not index.is_file() or index.read_text(encoding="utf-8") != render_index():
            errors.append("llms.txt is missing or out of date; run python scripts/build_llms.py")
    except (OSError, ValueError) as exc:
        errors.append(str(exc))

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    print(f"Validated {len(pages)} Markdown pages and llms.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
