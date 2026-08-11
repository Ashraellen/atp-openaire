# ATP — Constraint-Preserved AI Transcreation

An auditable human–AI workflow for multilingual literary and research transcreation with OpenAIRE Graph integration.

ATP treats literary transcreation as a constrained, stateful process rather than unconstrained rewriting. It makes terminology, continuity, intentional ambiguity, voice, structural rules, prohibited normalization, bounded revision, provenance, and human review explicit.

Prepared as a public artifact for the OpenAIRE AI Hackathon 2026. Private literary masters and internal production canon are intentionally excluded.

## Why ATP

Fluent AI output can still drift away from authorial intent. Literary features that look inefficient to a general-purpose model — repetition, unresolved ambiguity, strange imagery, structural pressure — may be deliberate. ATP separates four things that are often mixed together: source authority, authorial constraints, external research context, and model-generated proposals.

The OpenAIRE Graph is used as an explicit scholarly-context layer. Retrieved metadata may support research awareness and verification, but it may not silently override the frozen source or authorial constraints.

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

Requirements: Python 3.10+ and an internet connection. No third-party Python packages and no OpenAIRE account are required for the small public demo.

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

## Architecture and method

- [`methodology/ATP_METHOD_v0.1.md`](methodology/ATP_METHOD_v0.1.md) — constraint and revision protocol.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — authority hierarchy, trust boundaries, and reproducibility model.
- [`submission/STORY_DRAFT.md`](submission/STORY_DRAFT.md) — hackathon 1–2 page story draft.
- [`submission/REGISTRATION_TEXT.md`](submission/REGISTRATION_TEXT.md) — prepared registration form copy.

## Repository layout

```text
.github/       CI / live OpenAIRE smoke test
methodology/   ATP protocol and constraint model
src/           reusable Python modules
demo/          synthetic demonstration inputs and runner
tests/         deterministic tests
docs/          architecture and provenance notes
submission/    hackathon submission materials
```

## Licensing

Software is licensed under MIT. Methodology, documentation, public demo text, and submission materials are licensed under CC BY 4.0. OpenAIRE metadata retains OpenAIRE attribution and provenance. See [`LICENSE.md`](LICENSE.md).

## Public/private boundary

This repository does **not** contain private literary masters, unpublished MONOLITH canon, production prompts, or private project state. The demo passage is synthetic and was created specifically for reproducibility and open release.

## Status

Hackathon MVP: OpenAIRE retrieval, normalization, provenance capture, constraint loading, SHA-256 manifest generation, unit tests, architecture/methodology documentation, licensing, citation metadata, and live CI are implemented.
