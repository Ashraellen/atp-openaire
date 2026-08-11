# ATP — Constraint-Preserved AI Transcreation

**Recommended theme:** B — Build  
**Artifact:** reusable workflow + code + methodology + reproducible OpenAIRE Graph demonstrator

## The question

Can AI-assisted literary transcreation preserve an author's intentional ambiguity, recurring terminology, character voice, structural progression, and unusual imagery across languages — while remaining auditable, reproducible, and grounded in open research?

Current AI translation workflows are often optimized for fluency. That is useful for ordinary text, but literary work can contain features that look like defects to a general-purpose model: unresolved ambiguity, repetition, strange metaphors, deliberate grammatical pressure, or continuity rules established hundreds of pages earlier. Repeated unconstrained revision can make a text smoother while moving it farther from the author's intent.

ATP treats this as a systems problem rather than a prompting trick.

## The journey

ATP began from a practical multilingual literary production workflow. The key observation was that the source text alone is not enough state for a reliable AI-assisted transcreation. A useful workflow also needs an explicit constraint layer: terminology, continuity, ambiguity, voice, structural rules, prohibited normalizations, revision limits, and a human acceptance gate.

For this hackathon, the method was separated from private literary material and rebuilt as a small public, reproducible artifact. A synthetic Russian passage and a public constraint file are used as the demonstration case.

The OpenAIRE Graph adds a separate scholarly-context layer. The demonstrator sends a real research query to the OpenAIRE Graph V3 research-products endpoint, retrieves relevant publications, normalizes their metadata, and records provenance. The source and constraint files are hashed with SHA-256, the API version and query are recorded, and the resulting research context is emitted both as JSON and as readable Markdown.

A deliberate trust boundary is central to the design: retrieved research metadata may inform context and verification, but it is not allowed to silently become an editorial instruction. The frozen source and authorial constraints remain authoritative. Model output, when used in the later transcreation stage, is treated as a proposal. Revision is bounded and human review remains explicit.

## The insight

The useful unit for human–AI literary translation is not simply `source -> model -> translation`.

It is closer to:

`frozen source + explicit authorial state + external research provenance -> candidate -> bounded revision -> human acceptance`.

This makes two normally invisible things visible: why a model was allowed to change something, and what external information was present when the decision was made.

Open scholarly infrastructure is valuable here not because research papers should dictate literary choices, but because scholarly context can be retrieved, cited, separated from authorial instructions, and inspected later. The separation itself is part of the contribution.

## What others can reuse

The repository contains a dependency-free Python OpenAIRE Graph V3 client, a small constraint loader, a research-product normalization/provenance layer, a reproducible demo runner, an architecture document, a methodology document, deterministic unit tests, and a GitHub Actions live smoke test.

The software can be reused independently of a particular language pair or AI provider. The constraint model is model-agnostic, and the OpenAIRE layer can be replaced or extended without changing the authority hierarchy.

Potential applications include literary translation, multilingual humanities research, museum and archival interpretation, multilingual editorial workflows, research communication, and any human–AI process where preserving intentional ambiguity and recording provenance matter as much as producing fluent text.

## Reproducibility and openness

The public demo contains no private manuscript material. Software is released under MIT; methodology, documentation, demo text, and submission materials are released under CC BY 4.0. OpenAIRE Graph metadata is acknowledged and retained with explicit provenance. A GitHub Actions workflow performs the live OpenAIRE query and uploads the generated reproducibility artifacts.

Repository: https://github.com/Ashraellen/atp-openaire
