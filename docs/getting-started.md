---
title: Getting Started
topic: knowledge-base
last_updated: 2026-09-25
---

# Getting Started

## When a product is selected

First establish the product and applicable version, intended audience, tasks agents should support, documentation scope, and exclusions. Then gather supplied product materials and identify authoritative public sources to fill gaps.

Create `docs/topics/<product-slug>/` and add:

- `index.md` using [the topic overview starter](starter-pages/topic-overview.md), adapted to record the product scope, version, and agent tasks
- `sources.md` using [the source register starter](starter-pages/source-register.md)
- focused product pages using [the article starter](starter-pages/article.md)

Use a short, descriptive lowercase slug with hyphens. The product index should explain scope and version applicability, describe the tasks supported, and link to the relevant procedures and references. Write each page so an agent can use it when retrieved independently. The site navigation is generated from the folder structure.

## Check and publish

After changing pages, regenerate and check the LLM index, run the content validator, and build the site in strict mode:

```text
python scripts/build_llms.py
python scripts/validate.py
mkdocs build --strict
```

See the [research workflow](guides/research-workflow.md) before drafting and the [authoring guide](guides/authoring.md) while writing.
