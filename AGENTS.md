# Knowledge Base Authoring Instructions

Use these instructions whenever creating or editing topic knowledge in this repository.

## Workflow for a new subject

1. Ask for the topic's scope, intended audience, depth, and important exclusions if they are not clear. Record the agreed scope in `docs/topics/<topic-slug>/index.md`.
2. Collect both web research and user-provided materials when available. Prefer primary and authoritative sources; use secondary sources to add context or corroboration.
3. Create a source register in the topic folder. Give each source a stable ID and record its title, publisher or author, date (when available), URL or supplied-file location, and notes on authority or limitations.
4. Map the subject into a small set of useful, non-duplicative articles before drafting. Keep each article focused and link related concepts rather than copying the same explanation into multiple pages.
5. Cite claims near where they appear and include a references section linking citations to the source register. Distinguish sourced facts from interpretation, label uncertainty, and note material disagreements between sources.
6. Update the topic index, build `llms.txt`, run validation and a strict site build, and review the rendered pages and links.

## Content and safety rules

- Never invent a source, quotation, statistic, date, or factual claim. If evidence is missing or conflicting, say so explicitly.
- Use current sources for time-sensitive subjects and record when the research was performed. Do not imply that a page is current indefinitely.
- Preserve attribution and cite supplied files precisely (filename plus page, heading, or section when available). Do not assume supplied documents may be published.
- This starter is intended to become a GitHub repository. Do not add credentials, secrets, personal data, or private/confidential source content to tracked files. Ask before including material whose publication permission is unclear.
- Summarize in original wording. Quote only when necessary, keep quotations brief, and cite them.
- Keep the content in Markdown. Do not maintain a separate copy of article text for the website or for `llms.txt`.
- Use descriptive filenames in lowercase kebab-case. Add metadata to every Markdown page under `docs/`:

  ```yaml
  ---
  title: Human-readable page title
  topic: topic-slug
  last_updated: YYYY-MM-DD
  ---
  ```

- Update `last_updated` when substantive content changes. For shared guides and templates, use `topic: knowledge-base`.
- Keep the topic index useful to both readers and LLMs: define the boundaries, link the key concepts, and point to the most useful entry pages.
- Regenerate the root `llms.txt` after adding, removing, or renaming Markdown pages. The validator checks that it matches the current corpus.
