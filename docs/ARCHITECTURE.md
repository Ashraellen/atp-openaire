# ATP Architecture

ATP separates authorial intent, scholarly retrieval, model generation, and review into explicit layers so that external research context cannot silently become editorial instruction.

```text
Frozen source
    +
Authorial constraint set
    |
    +-----------------------------+
    |                             |
    v                             v
OpenAIRE research query      Constraint package
    |                             |
    v                             |
Graph V3 metadata                 |
    |                             |
    v                             |
Normalized provenance ------------+
                  |
                  v
        model-agnostic transcreation stage
                  |
                  v
          bounded revision pass
                  |
                  v
             human review
                  |
                  v
          auditable final record
```

## Trust boundaries

1. **Source authority** — the frozen source is authoritative for meaning and unresolved ambiguity.
2. **Constraint authority** — explicit authorial constraints govern terminology, voice, continuity, structure, and prohibited transformations.
3. **Research context** — OpenAIRE metadata is evidence/context only. It may support terminology and research awareness but may not override the source or constraints.
4. **Model output** — generated text is a proposal, never an authority.
5. **Bounded revision** — revision is limited by the declared pass count so iterative smoothing cannot silently normalize intentional features.
6. **Human review** — the public demo requires a human acceptance gate before any output is treated as final.

## Reproducibility

The demo hashes the source and constraints with SHA-256, records the exact research query and API version, normalizes retrieved records, and stores a manifest linking those inputs to the generated research context. GitHub Actions performs a live smoke run against OpenAIRE Graph V3 and uploads the generated artifacts for inspection.

## Scope

The repository demonstrates the method on a synthetic passage. It intentionally excludes unpublished literary masters and private production state.
