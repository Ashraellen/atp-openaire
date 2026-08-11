# ATP — Constraint-Preserved AI Transcreation

An auditable human–AI workflow for multilingual literary and research transcreation with OpenAIRE Graph integration.

## What this repository explores

ATP treats literary transcreation as a constrained, stateful process rather than unconstrained rewriting. The workflow makes authorial constraints explicit — terminology, continuity, ambiguity, structural rules, voice and bounded revision requirements — and combines them with open scholarly context retrieved from the OpenAIRE Graph.

The project is being prepared as an OpenAIRE AI Hackathon 2026 artifact. The public repository contains only material prepared for open release; private literary masters and internal production canon are intentionally excluded.

## Working demonstrator

The current public demonstrator implements the research-context side of the workflow end to end:

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
auditable manifest for the later transcreation stage
```

The prototype deliberately keeps scholarly retrieval separate from model-generated literary output. Research metadata can inform context and verification, but it cannot silently rewrite or override authorial constraints.

## Run it

Requirements: Python 3.10+ and an internet connection. No third-party Python packages and no OpenAIRE account are required for the small public demo.

From the repository root:

```bash
python demo/run_demo.py
```

The run writes:

```text
demo/generated/research_results.json   normalized OpenAIRE provenance
demo/generated/research_context.md     human-readable research context
demo/generated/demo_manifest.json      input hashes, constraints and pipeline state
```

The source and constraint files are hashed with SHA-256 in the manifest so a later transcreation result can be tied to the exact public inputs used for that run.

## OpenAIRE Graph

Production API used by the prototype:

`https://api.openaire.eu/graph/v3/research-products`

The current V3 research-products endpoint supports keyword search, type filtering, sorting, statistics, offset paging and cursor paging. The client uses only a small public query and therefore does not require authentication; a bearer token can be supplied later without changing the workflow model.

OpenAIRE Graph records are treated as external research metadata with explicit provenance. Their presence in the research context does not imply endorsement of a translation decision.

## Constraint model

`demo/constraints.yaml` is intentionally small and public. It defines:

- source and target languages;
- a research query;
- properties that must be preserved;
- transformations that are forbidden;
- the number of bounded revision passes;
- provenance and human-review requirements.

The demonstrator includes a tiny dependency-free parser for this limited YAML subset. It is not intended as a general-purpose YAML implementation.

## Repository layout

```text
methodology/   ATP protocol and constraint model
src/           reusable Python modules
demo/          reproducible demonstration inputs and runner
docs/          architecture and provenance notes
submission/    hackathon submission materials
```

## Public/private boundary

This repository does **not** contain private literary masters, unpublished MONOLITH canon, production prompts or internal project state. The demo passage is a synthetic public example created specifically for reproducibility and open release.

## Status

Public prototype. OpenAIRE retrieval, normalization, provenance capture, constraint loading and manifest generation are implemented. The next layer is a model-agnostic transcreation adapter plus bounded QA that consumes the frozen constraint set without allowing retrieved research metadata to become hidden editorial instruction.
