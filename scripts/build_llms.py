#!/usr/bin/env python3
"""Build the repository-root llms.txt index from the Markdown corpus."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "llms.txt"


def read_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*?)\s*$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip("\"'")
    return metadata


def markdown_pages() -> list[Path]:
    pages = list(DOCS.rglob("*.md"))
    return sorted(pages, key=lambda p: (p != DOCS / "index.md", p.relative_to(ROOT).as_posix().casefold()))


def render_index() -> str:
    lines = [
        "# Fieldnotes",
        "",
        "> Source-backed product documentation in Markdown, organized for AI agent discovery and consumption. The searchable website is rendered from these same files.",
        "",
        "## Documents",
        "",
    ]
    for page in markdown_pages():
        metadata = read_frontmatter(page)
        title = metadata.get("title")
        if not title:
            raise ValueError(f"{page.relative_to(ROOT)}: missing title in frontmatter")
        relative_path = page.relative_to(ROOT).as_posix()
        lines.append(f"- [{title}]({relative_path})")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if llms.txt is not up to date")
    args = parser.parse_args()

    try:
        expected = render_index()
    except (OSError, ValueError) as exc:
        print(exc, file=sys.stderr)
        return 1

    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print("llms.txt is missing or out of date; run python scripts/build_llms.py", file=sys.stderr)
            return 1
        print("llms.txt is up to date.")
        return 0

    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(markdown_pages())} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
