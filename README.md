# Topic Knowledge Base Starter

A reusable starter for building a focused, source-backed knowledge base on any subject. Markdown is the source of truth: the same pages are presented as a searchable website and listed in the LLM-oriented `llms.txt` index.

## How it works

- **You choose a subject and its boundaries.** Each topic lives in its own folder under `docs/topics/`, with an overview, source register, and focused articles.
- **Research is traceable.** The workflow can combine web research with materials you provide. Articles cite their evidence, while the topic's `sources.md` records source details and limitations.
- **Markdown powers both experiences.** MkDocs turns the pages into a browsable site with navigation and search. `scripts/build_llms.py` creates the repository-root `llms.txt` index from those same pages for LLM tools.
- **Checks catch drift.** `scripts/validate.py` checks page metadata, local links, and whether `llms.txt` matches the Markdown files. The strict MkDocs build catches documentation-site problems.

The starter currently has shared guidance and examples, but no subject-specific knowledge. It does not automatically crawl or refresh sources: research, citation, and review happen as part of each topic update.

## How to use it with Copilot

You can work conversationally from the repository. Give me the subject and the outcome you want; I can use this repository's authoring rules to scope the collection, research it, draft and organize the Markdown, update the index, run checks, and build the site.

For a new collection, tell me:

1. **Subject and goal:** what the knowledge base should explain or help someone do.
2. **Audience and depth:** who will use it and how technical or detailed it should be.
3. **Scope and exclusions:** which areas to cover or leave out. If you're unsure, ask me to propose a scope first.
4. **Sources:** provide files or links you want included, or ask me to research authoritative public sources as well. Mention any source that must not be published.
5. **Preferred structure:** name important questions, sections, or use cases, if you already have them.

Example request:

> Build a knowledge base about **[subject]** for **[audience]**. Focus on **[scope]**, exclude **[exclusions]**, and use the files in **[location]** plus current authoritative web sources. Start by proposing a topic outline, then create the collection with citations and a source register.

If you just give me a subject, I can suggest a scope and article map before drafting. For ambiguous choices that materially affect the result, I’ll clarify them rather than silently guessing. I’ll distinguish sourced facts from interpretation and flag uncertainty or conflicting evidence.

### What I'll create for a topic

For a topic called `example-subject`, the collection will generally look like this:

```text
docs/topics/example-subject/
  index.md       # scope, audience, entry points, and article map
  sources.md     # source register with stable citation IDs
  concepts.md    # focused explanations
  ...            # additional focused articles as needed
```

The topic overview and article starters are in [`docs/starter-pages/`](docs/starter-pages/topic-overview.md). Topic-specific pages include `topic` metadata matching their folder slug. The root `llms.txt` is regenerated from all Markdown pages; the website is built from the same files, so article content is maintained in one place.

## How to use the knowledge base yourself

1. Read [`AGENTS.md`](AGENTS.md) for the rules that guide authoring and research.
2. Browse the [getting started guide](docs/getting-started.md), [research workflow](docs/guides/research-workflow.md), [authoring guide](docs/guides/authoring.md), and [maintenance guide](docs/guides/maintenance.md).
3. Create a topic directory under `docs/topics/`. Copy the appropriate pages from `docs/starter-pages/` and replace the example content and metadata.
4. Keep each article focused, cite substantive claims near the evidence, and add those sources to the topic's `sources.md`.
5. Update the topic collection index, regenerate `llms.txt`, run the checks below, and review the rendered site.

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

Push this project to a GitHub repository with a `main` branch, then select **Settings > Pages > Build and deployment > GitHub Actions**. The workflow in `.github/workflows/pages.yml` validates the content, builds the site, and deploys it on pushes to `main` and on manual runs. Commit the generated `llms.txt` with the Markdown so it is also available to tools that read the repository directly.
