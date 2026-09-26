# Fieldnotes

Fieldnotes is a home for **documentation written for AI agent consumption**. Use it to document any subject: a product, a technical system, a process, a field of knowledge, or another topic. Its primary output is a well-organized set of source-backed Markdown documents, with clear metadata, direct explanations, task-oriented procedures where relevant, and an `llms.txt` index that helps agents discover the right pages. A searchable website is generated from the same Markdown as a convenient human browsing experience.

## The goal

When you provide a subject, Fieldnotes helps create documentation that an AI agent can retrieve, understand, and use accurately. The documents should stand on their own, answer a specific question or task, explain relevant context and constraints, and cite the evidence they rely on. They should not assume an agent has read an entire manual or infer important details from vague prose.

Markdown is the canonical content. `llms.txt` is generated from the Markdown inventory to point agents to relevant files; it is not a duplicate copy of the content. MkDocs generates a searchable site from those same files. Validation checks page metadata, local links, and index consistency.

Fieldnotes does not automatically crawl or refresh sources. Research, verification, and review happen when a documentation collection is created or updated.

## How to use Fieldnotes with an AI agent

Give the agent the subject and the documentation outcome you want. It can follow [`AGENTS.md`](AGENTS.md) to plan the collection, research public sources and supplied materials, write and organize Markdown, refresh `llms.txt`, validate the content, and build the site.

For a new documentation collection, provide:

1. **Subject and goal:** what the documentation should explain or help someone do.
2. **Audience and agent tasks:** who will use the documentation and what questions or actions an AI agent should support.
3. **Scope:** which concepts, processes, systems, use cases, or other areas to include or exclude.
4. **Sources:** files, links, and authoritative public sources to research. Identify anything that must not be published.
5. **Requirements:** preferred terminology, format, depth, or existing documentation conventions.

Example request:

> Create documentation optimized for AI agents about **[subject]**. The agents should help **[audience]** with **[tasks/questions]**. Cover **[scope]**, exclude **[exclusions]**, and use **[provided sources]** plus current authoritative sources. Start with a documentation map, then create concise, source-backed Markdown pages with an index.

If you provide only a subject, the agent can propose the scope and documentation map first. Confirm assumptions that materially affect the content, such as product versions, dates, jurisdictions, or intended audience. Claims should be traceable, and uncertainties or conflicting sources should be visible rather than guessed away.

### Typical collection structure

For a subject called `example-subject`, a collection under `docs/topics/` might look like this:

```text
docs/topics/example-subject/
  index.md              # subject scope, agent tasks/questions, and document map
  sources.md            # source register with stable citation IDs
  overview.md           # core concepts and boundaries
  how-it-works.md       # explanation of a process or system
  procedure.md          # task-oriented instructions, when relevant
  reference.md          # precise reference material, when applicable
  ...                   # other focused pages as needed
```

The starters are in [`docs/starter-pages/`](docs/starter-pages/topic-overview.md). Adapt the structure to the subject and the tasks agents need to support rather than creating every example page by default. Give every page clear metadata and a focused purpose. Keep procedures explicit about prerequisites, inputs, steps, expected results, and verification when those details apply. Include relevant version or date boundaries when the subject requires them. The root `llms.txt` is regenerated from the Markdown pages so agents can discover them without maintaining a second copy.

## How to use the documentation yourself

1. Read [`AGENTS.md`](AGENTS.md) for the AI-agent-focused documentation rules.
2. Use the [getting started guide](docs/getting-started.md), [research workflow](docs/guides/research-workflow.md), [authoring guide](docs/guides/authoring.md), and [maintenance guide](docs/guides/maintenance.md).
3. Create a subject directory under `docs/topics/`, then adapt the relevant pages from `docs/starter-pages/`.
4. Keep each page focused and evidence-backed; record applicable boundaries and cite sources near substantive claims.
5. Regenerate `llms.txt`, run the checks below, and inspect the rendered site.

Never put confidential material, credentials, or personal data in this repository. Confirm that supplied documents may be published before including their contents in a GitHub repository.

## Local preview and checks

Requires Python 3.10 or later. From the repository root, create an environment and install the documentation dependency:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

After adding or changing Markdown pages, regenerate the LLM index and check the content:

```powershell
python scripts\build_llms.py
python scripts\validate.py
mkdocs build --strict
```

To preview and search the site while editing:

```powershell
mkdocs serve
```

Open the local URL printed by `mkdocs serve`. Re-run the index generator after adding, removing, or renaming Markdown pages. The GitHub workflow checks that the committed index is current; it does not silently rewrite it.

## Publish with GitHub Pages

Push this project to a GitHub repository with a `main` branch, then select **Settings > Pages > Build and deployment > GitHub Actions**. The workflow in `.github/workflows/pages.yml` validates the content, builds the site, and deploys it on pushes to `main` and on manual runs. Commit `llms.txt` with the Markdown so agents can discover the documentation directly from the repository even when they do not use the website.
