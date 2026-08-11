# ATP — Constraint-Preserved AI Transcreation

An auditable human–AI workflow for multilingual literary and research transcreation with OpenAIRE Graph integration.

## What this repository explores

ATP treats literary transcreation as a constrained, stateful process rather than unconstrained rewriting. The workflow makes authorial constraints explicit — terminology, continuity, ambiguity, structural rules, voice and bounded revision requirements — and combines them with open scholarly context retrieved from the OpenAIRE Graph.

The project is being prepared as an OpenAIRE AI Hackathon 2026 artifact. The public repository contains only material prepared for open release; private literary masters and internal production canon are intentionally excluded.

## Initial demonstrator

The first demonstrator will:

1. define a small source passage and an explicit constraint set;
2. query OpenAIRE Graph V3 for relevant scholarly context;
3. retain provenance for the retrieved research products;
4. show a constraint-aware transcreation workflow;
5. produce a bounded QA/provenance report.

## OpenAIRE Graph

Production API used by the prototype:

`https://api.openaire.eu/graph/v3/research-products`

The client is designed to work without authentication for the small public demo. Authentication can be added later through configuration without changing the workflow model.

## Repository layout

```text
methodology/   ATP protocol and constraint model
src/           reusable Python modules
demo/          reproducible demonstration inputs and outputs
docs/          architecture and provenance notes
submission/    hackathon submission materials
```

## Status

Early public prototype. Interfaces and methodology may change while the hackathon artifact is being assembled.
