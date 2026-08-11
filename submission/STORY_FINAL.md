# ATP OpenAIRE — Research provenance for constraint-preserved AI transcreation

**Theme:** B — Build  
**Artifact:** reusable OpenAIRE Graph extension + code + methodology + reproducible demonstrator

## The question

Can AI-assisted literary transcreation preserve an author's intentional ambiguity, recurring terminology, character voice, structural progression, and unusual imagery across languages — while remaining auditable, reproducible, and grounded in open research?

AI translation is increasingly fluent, but literary fidelity is not the same thing as fluency. Repetition, unresolved ambiguity, strange metaphors, grammatical pressure, or continuity rules established hundreds of pages earlier can look like defects to a general-purpose model. Repeated unconstrained revision can therefore make a text smoother while moving it farther from the author's intent.

ATP treats this as a systems problem rather than a prompting trick.

## Where ATP came from

ATP did not begin as a hackathon project. It grew out of sustained multilingual literary production and a practical problem: how to use modern AI tools to recover, organize, translate, revise, and carry long-form literary work across languages without allowing the tool to replace the authorial source of meaning.

The pre-existing core project — the **Ashraellen Transcreation Protocol** — formalized that experience into a human-directed, model-agnostic protocol. Its central question is:

> **How can AI help an author cross languages without replacing the author?**

The core ATP answer is to preserve durable authorial state: source authority, terminology, continuity, ambiguity, voice, structural rules, exceptions, bounded revision, validation, and explicit human acceptance. The protocol has its own public repository, DOI-backed release history, documentation, templates, and applied evidence from sustained multilingual literary production.

Core ATP: https://github.com/Ashraellen/ashraellen-atp  
DOI: https://doi.org/10.5281/zenodo.21838981

## Why OpenAIRE became the next step

Once authorial constraints are explicit, another problem appears: external research context is useful, but it becomes risky when it is silently blended into model authority.

For this hackathon, we therefore did not invent a new protocol. We built a bounded extension of the existing one.

The OpenAIRE Graph becomes a separate scholarly-context and provenance layer. The public demonstrator sends a real query to the OpenAIRE Graph V3 research-products endpoint, retrieves research products, normalizes their metadata, and records provenance. The source and constraint files are hashed with SHA-256, the API version and query are recorded, and the resulting research context is emitted both as JSON and readable Markdown.

A deliberate trust boundary is central to the design: retrieved research metadata may inform context and verification, but it is not allowed to silently become an editorial instruction. The authorized source and authorial constraints remain authoritative. Model output is a proposal. Revision is bounded. Human acceptance remains explicit.

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

The two-repository structure is intentional. The core ATP repository remains the stable methodology. The hackathon repository is a focused research/provenance implementation that can be inspected and reused without rewriting ATP's history or exposing private literary masters.

## The insight

The useful unit for human–AI literary transcreation is not simply:

`source -> model -> translation`

It is closer to:

`authorized source + durable authorial state + attributable external research -> candidate -> bounded revision -> human acceptance`

This makes two normally invisible things visible: why a model was allowed to change something, and what external information was present when the decision environment was constructed.

Open scholarly infrastructure is valuable here not because research papers should dictate literary choices, but because scholarly context can be retrieved, attributed, separated from authorial instructions, and inspected later. The separation itself is part of the contribution.

## What the artifact actually does

The hackathon repository contains:

- a dependency-free Python OpenAIRE Graph V3 client;
- a public constraint loader;
- research-product normalization and provenance capture;
- a reproducible demo runner;
- SHA-256 input binding in a manifest;
- deterministic unit tests;
- architecture and trust-boundary documentation;
- a live GitHub Actions smoke test against OpenAIRE Graph V3.

The live CI workflow queries OpenAIRE Graph, validates that research products were returned, generates provenance/context files, validates the manifest, and uploads the resulting demo files as a reproducibility artifact. The submission therefore includes an observable execution path, not only a conceptual architecture.

## What others can reuse

The implementation is independent of a particular language pair or AI provider. The OpenAIRE layer can be extended without changing the human-authority hierarchy. The same pattern can be useful anywhere external research must inform an AI-assisted process without silently becoming instruction.

Potential applications include literary translation, multilingual digital humanities, museum and archival interpretation, multilingual editorial workflows, research communication, and other human–AI systems where provenance, ambiguity preservation, and explicit authority boundaries matter as much as fluent output.

## Reproducibility and openness

The public demonstrator contains no private manuscript material. Software is released under MIT. Methodology, documentation, demo text, and submission materials are released under CC BY 4.0. OpenAIRE Graph metadata is retained with attribution and provenance.

Hackathon implementation: https://github.com/Ashraellen/atp-openaire
