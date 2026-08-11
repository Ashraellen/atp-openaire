# ATP Method v0.1

## Working definition

ATP (Constraint-Preserved AI Transcreation) is a human-directed workflow for multilingual literary and research transcreation in which source meaning, authorial state and explicit constraints remain first-class objects throughout AI-assisted drafting and revision.

## Constraint layers

The initial model separates constraints into six layers:

1. **Source fidelity** — facts, meanings, relationships and unresolved elements that must not drift.
2. **Terminology** — frozen names, recurring terms, labels and translation choices.
3. **Voice** — character, narrator and register constraints that must remain distinguishable.
4. **Continuity/state** — facts established elsewhere that govern the current unit.
5. **Structure** — sentence, paragraph, quotation, section and other structural requirements where they carry literary function.
6. **Anti-normalization** — explicit instructions not to smooth away ambiguity, strangeness, asymmetry or deliberate awkwardness merely because a more conventional target-language form exists.

## Bounded revision

ATP distinguishes free rewriting from bounded revision. A bounded revision may correct clear fidelity, grammar or structural drift, but it must not introduce a new interpretation, stylistic agenda or resolution that the source has not supplied.

## Research-grounding layer

OpenAIRE Graph is used as an external scholarly-context layer rather than as an authority over the literary source. Research retrieval can support questions about multilingual AI, translation studies, human–AI collaboration, authorship, ambiguity and evaluation. Retrieved records must retain provenance so that the research context used by the workflow is auditable.

## Demonstrator pipeline

```text
source unit
   ↓
constraint/state record
   ↓
research question generation
   ↓
OpenAIRE Graph retrieval
   ↓
provenance-preserving research context
   ↓
AI-assisted transcreation
   ↓
bounded revision
   ↓
constraint QA + provenance report
```

## Scope of the public artifact

The public demonstrator will use material specifically prepared for open release. It does not require publication of private literary masters, complete manuscripts or internal production canon.

## Status

This is an early methodological specification and will be revised as the demonstrator and evaluation protocol are implemented.
