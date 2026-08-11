# ATP — Constraint-Preserved AI Transcreation

An auditable human–AI workflow for multilingual literary and research transcreation with OpenAIRE Graph integration.

This repository is the **OpenAIRE research/provenance extension** of the [Ashraellen Transcreation Protocol (ATP)](https://github.com/Ashraellen/ashraellen-atp), a pre-existing human-directed protocol for AI-assisted literary transcreation. The core ATP repository contains the origin story, methodology, durable-state model, protocol templates, DOI-backed release history, and the human–AI authority framework. This repository adds a reproducible OpenAIRE Graph layer without redefining the underlying protocol.

ATP treats literary transcreation as a constrained, stateful process rather than unconstrained rewriting. It makes terminology, continuity, intentional ambiguity, voice, structural rules, prohibited normalization, bounded revision, provenance, and human review explicit.

Prepared as a public artifact for the OpenAIRE AI Hackathon 2026. Private literary masters and internal production canon are intentionally excluded.

## Project lineage

ATP did not originate as a hackathon project. It grew out of sustained multilingual literary production and the practical need to use AI without surrendering authorial control. The core question was:

> **How can AI help an author cross languages without replacing the author?**

The core protocol answers that by making authorial state durable and keeping canonical authority with the human. The OpenAIRE extension asks the next question:

> **How can external scholarly context be added to that workflow while remaining inspectable, attributable, and unable to silently override the author?**

The relationship is therefore:

```text
ashraellen-atp
core methodology + origin + authority model + durable state
        ↓
atp-openaire
OpenAIRE Graph retrieval + research provenance + reproducible demonstrator
```

Core protocol: https://github.com/Ashraellen/ashraellen-atp  
Core ATP DOI: https://doi.org/10.5281/zenodo.21838981

## Why ATP

Fluent AI output can still drift away from authorial intent. Literary features that look inefficient to a general-purpose model — repetition, unresolved ambiguity, strange imagery, structural pressure — may be deliberate. ATP separates four things that are often mixed together: source authority, authorial constraints, external research context, and model-generated proposals.

The OpenAIRE Graph is used as an explicit scholarly-context layer. Retrieved metadata may support research awareness and verification, but it may not silently override the authorized source or authorial constraints.

## Working demonstrator

```text
demo/source.txt
      +
demo/constraints.yaml
      ↓
OpenAIRE Graph V3
      ↓
normalized research metadata
      ↓
provenance JSON + research-context Markdown
      ↓
auditable manifest with SHA-256 input hashes
      ↓
later model-agnostic transcreation + bounded revision + human review
```

## Run it

Requirements: Python 3.10+ and an internet connection. No third-party Python packages and no OpenAIRE account are required for the small public direct-API demo. See [`requirements.txt`](requirements.txt).

```bash
python demo/run_demo.py
```

The run writes:

```text
demo/generated/research_results.json
demo/generated/research_context.md
demo/generated/demo_manifest.json
```

The source and constraints are SHA-256 hashed in the manifest so downstream output can be tied to exact public inputs.

## Continuous verification

GitHub Actions runs deterministic unit tests and a live smoke query against OpenAIRE Graph V3. A successful run validates that the API returned research products and uploads the generated demo directory as a reproducibility artifact.

## OpenAIRE Graph

Production endpoint:

`https://api.openaire.eu/graph/v3/research-products`

The V3 research-products endpoint supports keyword search, type filtering, sorting, statistics, offset paging, and cursor paging. ATP uses only a small public query; bearer-token authentication can be added without changing the workflow model.

## Constraint model

`demo/constraints.yaml` defines:

- source and target languages;
- the OpenAIRE research query;
- properties that must be preserved;
- transformations that are forbidden;
- bounded revision passes;
- provenance and human-review requirements.

The included parser intentionally supports only the small YAML subset used by this public demo.

## Architecture, method, and submission package

- [Core ATP repository](https://github.com/Ashraellen/ashraellen-atp) — origin, full protocol, reusable templates, reproducibility model, DOI-backed releases.
- [`methodology/ATP_METHOD_v0.1.md`](methodology/ATP_METHOD_v0.1.md) — OpenAIRE-extension constraint and revision protocol.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — authority hierarchy, trust boundaries, and reproducibility model.
- [`docs/PROJECT_RELATIONSHIP.md`](docs/PROJECT_RELATIONSHIP.md) — formal relationship between core ATP and this extension.
- [`submission/EVALUATOR_BRIEF.md`](submission/EVALUATOR_BRIEF.md) — one-minute project brief.
- [`submission/STORY_FINAL.md`](submission/STORY_FINAL.md) — final 1–2 page hackathon story.
- [`submission/REGISTRATION_TEXT.md`](submission/REGISTRATION_TEXT.md) — prepared registration form copy.
- [`submission/JUDGE_QA.md`](submission/JUDGE_QA.md) — evaluator-facing questions, claims, and evidence.
- [`submission/SUBMISSION_CHECKLIST.md`](submission/SUBMISSION_CHECKLIST.md) — public/manual submission gate.
- [`submission/OFFICIAL_TEMPLATE_DRAFT.md`](submission/OFFICIAL_TEMPLATE_DRAFT.md) — field-by-field draft aligned to the official OpenAIRE template.
- [`submission/EVALUATION_MATRIX.md`](submission/EVALUATION_MATRIX.md) — six-criterion scoring map and remaining gates.

## Repository layout

```text
.github/       CI / live OpenAIRE smoke test
methodology/   ATP extension protocol and constraint model
src/           reusable Python modules
demo/          synthetic demonstration inputs and runner
tests/         deterministic tests
docs/          architecture, provenance, and lineage notes
submission/    final hackathon submission materials
```

## Licensing

Software is licensed under MIT. Methodology, documentation, public demo text, and submission materials are licensed under CC BY 4.0. OpenAIRE metadata retains OpenAIRE attribution and provenance. See [`LICENSE.md`](LICENSE.md).

The separately maintained core ATP repository is licensed under CC BY 4.0 for its public methodology, documentation, and templates. Literary works including MONOLITH remain separately copyrighted and are not opened by either repository.

## Public/private boundary

This repository does **not** contain private literary masters, unpublished MONOLITH canon, production prompts, or private project state. The demo passage is synthetic and was created specifically for reproducibility and open release.

## Status

The direct OpenAIRE Graph V3 demonstrator, normalization/provenance layer, SHA-256 manifest, unit tests, live CI, methodology, architecture, licensing, citation metadata and judge-facing submission materials are implemented.

**Open completion gate:** the official hackathon template explicitly scores use of the Alien Intelligence OpenAIRE AI MCP connector. Direct API integration alone is therefore not presented as the finished competition state. MCP use will be added and evidenced before final submission; tracking issue: [#5](https://github.com/Ashraellen/atp-openaire/issues/5).
