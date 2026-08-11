# Project relationship: ATP core and ATP OpenAIRE extension

## Core project

**Ashraellen Transcreation Protocol (ATP)**  
Repository: https://github.com/Ashraellen/ashraellen-atp  
DOI: https://doi.org/10.5281/zenodo.21838981

The core ATP project predates the OpenAIRE hackathon artifact. It defines the human-directed methodology for AI-assisted literary transcreation, including durable authorial state, terminology and continuity control, ambiguity preservation, bounded revision, validation, human authority, and reproducibility.

Its origin is practical rather than competition-driven: ATP emerged from sustained multilingual literary production and from the need to use AI as a coordination and transformation aid without transferring canonical authority away from the author.

## OpenAIRE extension

**ATP OpenAIRE**  
Repository: https://github.com/Ashraellen/atp-openaire

This repository is a bounded extension of the core ATP method. It does not replace or fork the core methodology. It adds an external scholarly-context and provenance layer using OpenAIRE Graph V3.

The extension demonstrates how a human-directed transcreation workflow can retrieve research metadata, preserve its provenance, bind it to exact source and constraint inputs, and keep that external context below the frozen source and authorial constraints in the authority hierarchy.

## Authority relationship

```text
Human authority / authorized source
        ↓
Core ATP durable constraint state
        ↓
OpenAIRE scholarly context (advisory, attributable)
        ↓
AI-generated candidate (proposal)
        ↓
Bounded validation and revision
        ↓
Human acceptance / rejection
```

OpenAIRE records may inform research awareness, verification, or methodological context. They may not silently rewrite the source, resolve protected ambiguity, alter locked terminology, or become hidden editorial instructions.

## Why two repositories

The separation is intentional:

1. `ashraellen-atp` remains the stable, model-agnostic methodology and public protocol.
2. `atp-openaire` remains a focused, reproducible implementation of one research/provenance extension.
3. The hackathon artifact can be evaluated and reused without changing the core ATP release history.
4. Private literary masters, including MONOLITH production canon, remain outside both public artifacts.

## Lineage statement for citation and evaluation

When describing this hackathon project, the accurate lineage is:

> ATP is a pre-existing human-directed AI-assisted transcreation protocol developed through real multilingual literary production. ATP OpenAIRE is a 2026 research/provenance extension built for the OpenAIRE AI Hackathon to test how open scholarly context can be integrated without weakening authorial authority or auditability.
