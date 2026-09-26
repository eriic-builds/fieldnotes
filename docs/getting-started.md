---
title: Getting Started
topic: knowledge-base
last_updated: 2026-09-25
---

# Getting Started

## When a subject is selected

First establish the subject, intended audience, tasks or questions agents should support, documentation scope, and exclusions. Identify relevant boundaries, such as product versions, dates, jurisdictions, or technical environments, when they matter. Then gather supplied materials and identify authoritative public sources to fill gaps.

Create `docs/topics/<subject-slug>/` and add:

- `index.md` using [the topic overview starter](starter-pages/topic-overview.md), adapted to record the subject scope, applicable boundaries, and agent tasks
- `sources.md` using [the source register starter](starter-pages/source-register.md)
- focused pages using [the article starter](starter-pages/article.md)

Use a short, descriptive lowercase slug with hyphens. The collection index should explain scope and applicability, describe the tasks or questions supported, and link to the relevant procedures and references. Write each page so an agent can use it when retrieved independently. The site navigation is generated from the folder structure.

## Check and publish

After changing pages, regenerate and check the LLM index, run the content validator, and build the site in strict mode:

```text
python scripts/build_llms.py
python scripts/validate.py
mkdocs build --strict
```

See the [research workflow](guides/research-workflow.md) before drafting and the [authoring guide](guides/authoring.md) while writing.
