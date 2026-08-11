# ATP OpenAIRE — Research provenance for constraint-preserved AI transcreation

**Recommended theme:** B — Build  
**Artifact:** reusable OpenAIRE Graph extension + code + methodology + reproducible demonstrator

## The question

Can AI-assisted literary transcreation preserve an author's intentional ambiguity, recurring terminology, character voice, structural progression, and unusual imagery across languages — while remaining auditable, reproducible, and grounded in open research?

Current AI translation workflows are often optimized for fluency. That is useful for ordinary text, but literary work can contain features that look like defects to a general-purpose model: unresolved ambiguity, repetition, strange metaphors, deliberate grammatical pressure, or continuity rules established hundreds of pages earlier. Repeated unconstrained revision can make a text smoother while moving it farther from the author's intent.

ATP treats this as a systems problem rather than a prompting trick.

## Where ATP came from

ATP did not begin as a hackathon project or as a research abstraction. It grew out of sustained multilingual literary production and a practical problem: how to use modern AI tools to recover, organize, translate, revise, and carry long-form literary work across languages without allowing the tool to replace the authorial source of meaning.

The pre-existing core project — the [Ashraellen Transcreation Protocol](https://github.com/Ashraellen/ashraellen-atp) — formalized that experience into a human-directed, model-agnostic protocol. Its central question is:

> **How can AI help an author cross languages without replacing the author?**

The core ATP answer is to preserve durable authorial state: source authority, terminology, continuity, ambiguity, voice, structural rules, exceptions, bounded revision, validation, and explicit human acceptance. The protocol has its own public repository, DOI-backed release history, documentation, templates, and applied evidence from real multilingual literary production.

## Why OpenAIRE became the next step

Once authorial constraints are made explicit, another problem appears: external research context is useful, but it can become dangerous if it is silently blended into the model's editorial authority.

For this hackathon, we therefore did not invent a new protocol. We built a bounded extension of the existing one.

The OpenAIRE Graph becomes a separate scholarly-context layer. The demonstrator sends a real research query to the OpenAIRE Graph V3 research-products endpoint, retrieves publications, normalizes their metadata, and records provenance. The source and constraint files are hashed with SHA-256, the API version and query are recorded, and the resulting research context is emitted both as JSON and as readable Markdown.

A deliberate trust boundary is central to the design: retrieved research metadata may inform context and verification, but it is not allowed to silently become an editorial instruction. The frozen source and authorial constraints remain authoritative. Model output, when used in the later transcreation stage, is treated as a proposal. Revision is bounded and human review remains explicit.

## The system relationship

```text
Ashraellen Transcreation Protocol (core)
origin + human authority + durable state + validation
        ↓
ATP OpenAIRE extension
research retrieval + attribution + provenance + reproducibility
        ↓
AI candidate
        ↓
bounded revision
        ↓
human acceptance
```

The separation into two repositories is intentional. The core ATP repository remains the stable methodology. The hackathon repository is a focused implementation of one research/provenance extension. This lets the OpenAIRE artifact be inspected and reused without rewriting ATP's prior history or exposing private literary masters.

## The insight

The useful unit for human–AI literary translation is not simply `source -> model -> translation`.

It is closer to:

`authorized source + durable authorial state + attributable external research -> candidate -> bounded revision -> human acceptance`.

This makes two normally invisible things visible: why a model was allowed to change something, and what external information was present when the decision was made.

Open scholarly infrastructure is valuable here not because research papers should dictate literary choices, but because scholarly context can be retrieved, cited, separated from authorial instructions, and inspected later. The separation itself is part of the contribution.

## What the hackathon artifact actually does

The repository contains a dependency-free Python OpenAIRE Graph V3 client, a small constraint loader, a research-product normalization/provenance layer, a reproducible demo runner, an architecture document, a methodology note, deterministic unit tests, and a GitHub Actions live smoke test.

The live CI workflow queries OpenAIRE Graph, validates that research products were returned, builds the provenance/context files, validates the manifest, and uploads the generated artifacts. The public demonstrator therefore provides an observable execution path rather than only a conceptual architecture.

The software can be reused independently of a particular language pair or AI provider. The constraint model is model-agnostic, and the OpenAIRE layer can be replaced or extended without changing the authority hierarchy.

Potential applications include literary translation, multilingual humanities research, museum and archival interpretation, multilingual editorial workflows, research communication, and any human–AI process where preserving intentional ambiguity and recording provenance matter as much as producing fluent text.

## Reproducibility and openness

The public demo contains no private manuscript material. Software is released under MIT; methodology, documentation, demo text, and submission materials are released under CC BY 4.0. OpenAIRE Graph metadata is acknowledged and retained with explicit provenance.

Core ATP repository: https://github.com/Ashraellen/ashraellen-atp  
Core ATP DOI: https://doi.org/10.5281/zenodo.21838981  
Hackathon implementation: https://github.com/Ashraellen/atp-openaire
