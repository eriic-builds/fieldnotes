---
title: Authoring and Citations
topic: knowledge-base
last_updated: 2026-09-25
---

# Authoring and Citations

## Page conventions

Every Markdown page under `docs/` starts with YAML frontmatter containing:

```yaml
---
title: Human-readable page title
topic: topic-slug
last_updated: YYYY-MM-DD
---
```

Use `topic: knowledge-base` for shared guidance and templates. Use the topic folder's slug for topic-specific pages. Update the date when the page's substance changes.

Write one page around one main question or concept. Begin with a direct explanation, define unfamiliar terms, and add examples or procedures only when supported by sources. Use descriptive headings and links to related pages. Avoid repeating long passages across articles.

## Citations and uncertainty

Add citations near the claims they support and include a references section on topic articles. Each reference should map to an entry in that topic's `sources.md`. Link public sources directly; for supplied documents, use a stable filename and page/section reference. Make it possible for a reader to locate the evidence without guessing.

Attribute quotations and keep them brief. Summarize source material in original wording. Mark estimates, interpretations, unresolved disputes, and time-sensitive details as such. Do not present a synthesis as though a source stated it verbatim.

## Review before publishing

- Confirm that the article is within the agreed scope.
- Verify key details, source links, dates, and names against the source material.
- Check that citations support the claims they follow and that limitations are represented.
- Make sure every Markdown page has valid metadata and every local link resolves.
- Regenerate `llms.txt`, run `python scripts/validate.py`, and build with `mkdocs build --strict`.
