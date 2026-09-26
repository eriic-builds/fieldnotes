---
title: Getting Started
topic: knowledge-base
last_updated: 2026-09-25
---

# Getting Started

## When a subject is selected

First establish the boundaries of the knowledge base: what the topic includes, who it is for, the required depth, and what to leave out. Then gather any supplied materials and identify reliable public sources that fill the gaps.

Create `docs/topics/<topic-slug>/` and add:

- `index.md` using [the topic overview starter](starter-pages/topic-overview.md)
- `sources.md` using [the source register starter](starter-pages/source-register.md)
- focused articles using [the article starter](starter-pages/article.md)

Use a short, descriptive lowercase slug with hyphens. The topic index should explain the scope and link to the articles in the collection. The site navigation is generated from the folder structure.

## Check and publish

After changing pages, regenerate and check the LLM index, run the content validator, and build the site in strict mode:

```text
python scripts/build_llms.py
python scripts/validate.py
mkdocs build --strict
```

See the [research workflow](guides/research-workflow.md) before drafting and the [authoring guide](guides/authoring.md) while writing.
