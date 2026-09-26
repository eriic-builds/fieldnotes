---
title: Agent-Ready Authoring and Citations
topic: knowledge-base
last_updated: 2026-09-25
---

# Agent-Ready Authoring and Citations

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

Write one page around one main product question, concept, task, or reference. Begin with the direct answer or outcome, define product-specific terms, and use descriptive headings. Keep pages understandable when retrieved on their own; state relevant product and release applicability instead of relying on context hidden in another page.

For procedures, include the prerequisites, permissions, inputs, ordered steps, expected result, and verification method when they apply. For troubleshooting, distinguish symptoms from causes and provide only verified resolution steps. For API or configuration references, preserve exact names, values, constraints, and version applicability from authoritative sources. Do not add a section simply to fill a template when it is not relevant.

Use links for deeper context, not to hide information essential to the current task. Do not rely on images or site-specific presentation for critical instructions; include that information as Markdown text.

## Citations and uncertainty

Add citations near the claims they support and include a references section on topic articles. Each reference should map to an entry in that topic's `sources.md`. Link public sources directly; for supplied documents, use a stable filename and page/section reference. Make it possible for a reader to locate the evidence without guessing.

Attribute quotations and keep them brief. Summarize source material in original wording. Mark estimates, interpretations, unresolved disputes, and time-sensitive details as such. Do not present a synthesis as though a source stated it verbatim.

## Review before publishing

- Confirm that the page is within the agreed product and version scope and supports a defined agent task or information need.
- Verify key details, source links, dates, and names against the source material.
- Check that citations support the claims they follow and that limitations are represented.
- Check that procedures are usable when retrieved independently and that prerequisites, outcomes, and verification are explicit where needed.
- Make sure every Markdown page has valid metadata and every local link resolves.
- Regenerate `llms.txt`, run `python scripts/validate.py`, and build with `mkdocs build --strict`.
