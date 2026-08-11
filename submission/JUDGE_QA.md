# ATP OpenAIRE — evaluator-facing QA

This document records the strongest likely evaluator questions and the corresponding evidence in the public artifact.

## Is OpenAIRE essential, or merely decorative?

It is essential to the hackathon extension. The artifact retrieves scholarly metadata from OpenAIRE Graph V3, normalizes it, records attribution/provenance, binds the research context to exact source/constraint inputs through a manifest, and verifies the live retrieval path in GitHub Actions. Removing OpenAIRE removes the research/provenance extension being submitted.

## Is this just RAG for translation?

No. Retrieval is deliberately prevented from becoming hidden editorial authority. ATP separates four layers: authorized source, durable authorial constraints, attributable external research context, and model proposals. Retrieved metadata can support awareness or verification, but cannot silently override the first two layers. The contribution is therefore as much about authority and provenance boundaries as retrieval.

## What existed before the hackathon?

The core Ashraellen Transcreation Protocol existed before this hackathon and remains separately versioned and DOI-backed. The hackathon contribution is the bounded OpenAIRE research/provenance extension and its reproducible implementation. This lineage is stated explicitly rather than presenting prior work as newly created.

## What actually works today?

The public repository contains a dependency-free OpenAIRE Graph V3 client, constraint loading, research metadata normalization, provenance generation, SHA-256 input binding, deterministic tests, and a live GitHub Actions smoke test. CI executes a real OpenAIRE query, validates the generated manifest, and uploads generated reproducibility artifacts.

## Where is the AI-assisted part?

ATP is the human-directed control protocol around AI-assisted transcreation. The public hackathon demonstrator focuses on the OpenAIRE research/provenance layer because that is the new build contribution and can be reproduced without requiring a proprietary model API key. The architecture explicitly defines where a model-generated candidate enters and keeps that output subordinate to authorial constraints and human acceptance.

## Why not automate the final literary decision?

Because the project treats authorial authority as a design requirement rather than inefficiency. AI may absorb coordination, comparison, search, and verification burden; canonical literary decisions remain human-authorized. Full autonomy would violate the problem definition ATP is designed to solve.

## What can another person reuse?

The OpenAIRE client, normalization/provenance pattern, constraint representation, manifest binding, trust-boundary architecture, tests, CI pattern, and methodology can all be reused independently of the original literary project or AI vendor.

## Is the project limited to literature?

Literary transcreation is the originating and strongest use case. The architecture generalizes to human–AI workflows where external research should inform a process without silently becoming instruction: digital humanities, archives, museums, multilingual editorial systems, and research communication.

## Are private literary works being open-sourced?

No. The public demonstrator is synthetic. Core methodology and public documentation are open, while unpublished literary masters and MONOLITH canon remain outside the repository and retain separate copyright.

## What is the clearest novelty claim?

ATP OpenAIRE combines durable authorial constraint state with an attributable scholarly-context layer and an explicit authority boundary. It makes external research provenance inspectable without giving retrieved material hidden permission to rewrite the source.

## What should an evaluator run?

From the repository root:

```bash
python demo/run_demo.py
```

For the already automated proof, inspect the latest successful `ATP smoke test` GitHub Actions run. It runs deterministic tests, performs a live OpenAIRE Graph V3 query, validates the manifest, and uploads generated artifacts.
