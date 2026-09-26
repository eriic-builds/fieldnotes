# Fieldnotes Authoring Instructions

Fieldnotes creates documentation about any subject in a content format optimized for AI agent consumption. Product documentation is one supported use case, not the limit. Use these instructions whenever creating or editing a documentation collection here. Markdown pages are the canonical source; the human-facing website is a rendered view of those pages.

## Workflow for a new collection

1. Establish the subject, audience, questions or tasks agents should support, scope, and exclusions. Clarify materially ambiguous details rather than silently guessing. Record the agreed context in `docs/topics/<collection-slug>/index.md`.
2. Collect user-provided material and current public sources where available. Prefer primary and authoritative sources appropriate to the subject; use secondary sources for context or corroboration.
3. Create a source register in the collection folder. Give each source a stable ID and record its title, publisher or author, date/version (when available), URL or supplied-file location, and notes on authority or limitations.
4. Map the documentation around the questions and tasks agents need to answer. Choose clear, non-duplicative pages, such as concepts, procedures, workflows, reference material, and troubleshooting, as relevant to the subject.
5. Write for retrieval and use: use descriptive titles and headings, define subject-specific terms, keep each page focused, and state prerequisites, inputs, steps, expected outcomes, and verification for procedures when applicable. Include relevant dates, versions, jurisdictions, or other boundaries. Keep each page understandable when an agent retrieves it independently, with links to related material for context.
6. Cite claims near where they appear and include references linking citations to the source register. Distinguish source-backed facts from interpretation, label uncertainty, and note material disagreements or version differences.
7. Update the collection index, regenerate `llms.txt`, run validation and a strict site build, and review the rendered pages and links.

## Content and safety rules

- Never invent a source, quotation, statistic, date, or factual claim. If evidence is missing or conflicting, say so explicitly.
- Use current sources for time-sensitive claims and record relevant source dates and applicability boundaries. For product documentation, identify releases or versions where they matter. Do not imply that a page is current indefinitely.
- Preserve attribution and cite supplied files precisely (filename plus page, heading, or section when available). Do not assume supplied documents may be published.
- This starter is intended to become a GitHub repository. Do not add credentials, secrets, personal data, or private/confidential source content to tracked files. Ask before including material whose publication permission is unclear.
- Summarize in original wording. Quote only when necessary, keep quotations brief, and cite them.
- Optimize the Markdown for agent retrieval, not just visual presentation: use semantic headings, precise terminology, explicit steps and conditions, and text that remains meaningful outside its surrounding page layout.
- Do not put essential instructions only in images, diagrams, styling, or interactive website elements. Provide the necessary information in Markdown text.
- Keep the content in Markdown. Do not maintain a separate copy of page text for the website or for `llms.txt`; `llms.txt` is a generated discovery index, not a content substitute.
- Use descriptive filenames in lowercase kebab-case. Add metadata to every Markdown page under `docs/`:

  ```yaml
  ---
  title: Human-readable page title
  topic: topic-slug
  last_updated: YYYY-MM-DD
  ---
  ```

- Update `last_updated` when substantive content changes. For shared guides and templates, use `topic: knowledge-base`.
- Keep each collection index useful to both readers and agents: define the subject boundaries, list supported agent tasks or questions, link key concepts and procedures, and point to the most useful entry pages.
- Regenerate the root `llms.txt` after adding, removing, or renaming Markdown pages. The validator checks that it matches the current corpus.
