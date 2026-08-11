# OpenAIRE AI Hackathon 2026 — evaluation matrix

This file maps ATP OpenAIRE to the six criteria in the official submission template and records remaining gates honestly.

## 1. AI MCP connector using the OpenAIRE Graph API

**Current state:** PARTIAL / OPEN GATE.

The public demonstrator already queries the OpenAIRE Graph V3 API live and records the query, API version, returned records and provenance. The official template, however, explicitly scores use of the AI MCP connector powered by Alien Intelligence. That connector is therefore a required completion gate before final submission.

**Evidence already present:**
- `src/openaire_client.py`
- `demo/run_demo.py`
- `.github/workflows/smoke.yml`
- generated CI reproducibility artifacts

**Completion action:** execute and document at least one equivalent research-context retrieval through the OpenAIRE/Alien MCP connector, preserve the MCP invocation/result provenance, and compare the MCP path with the direct API path without changing ATP's authority hierarchy.

## 2. Usefulness and value

**Status:** STRONG.

ATP OpenAIRE addresses a concrete problem in AI-assisted multilingual literary and humanities workflows: external scholarly context is useful, but if it is silently blended into editorial instruction it can override authorial constraints. The extension makes research retrieval explicit, attributable and inspectable while keeping the authorized source and human decision layer authoritative.

Primary users: authors, literary translators, multilingual editors, digital-humanities researchers and cultural-memory teams using AI assistance.

## 3. Originality

**Status:** STRONG.

The contribution is not generic retrieval or generic RAG. It separates four authority domains that are commonly conflated: authorized source, durable authorial constraints, external scholarly context, and model-generated proposals. OpenAIRE is used as a bounded evidence layer rather than as hidden editorial authority.

The project also has verifiable pre-hackathon lineage through the core Ashraellen Transcreation Protocol and its DOI-backed releases.

## 4. Responsible use of data

**Status:** STRONG.

- Synthetic public demo; no unpublished literary master is exposed.
- OpenAIRE attribution and provenance are retained.
- No credentials or API keys are committed.
- Third-party scholarly metadata is not treated as authorial instruction.
- Public methodology/documentation/demo materials are CC BY 4.0; software is MIT.
- Private literary works remain separately copyrighted.

## 5. Reproducibility and interoperability

**Status:** STRONG.

- Python 3.10+; current direct demonstrator has no third-party runtime dependencies.
- Source and constraints are SHA-256 hashed in the manifest.
- API version and research query are recorded.
- Deterministic unit tests plus a live GitHub Actions smoke test.
- Generated provenance/context/manifest files are uploaded as CI artifacts.
- Core protocol is model-agnostic and the research provider is architecturally separable.

## 6. Clarity

**Status:** STRONG, final polish ongoing.

Judge-facing material is deliberately layered:
- `submission/ONE_MINUTE_BRIEF.md` — fast orientation
- `submission/STORY_FINAL.md` — 1–2 page story
- `docs/ARCHITECTURE.md` — authority and trust boundaries
- `submission/JUDGE_QA.md` — likely evaluator questions and evidence
- `submission/SUBMISSION_CHECKLIST.md` — final gate

## FAIR cross-cutting check

**Findable:** public GitHub repositories, DOI-backed core ATP release, citation metadata.

**Accessible:** public repository and documentation; small demonstrator requires no account for direct API execution.

**Interoperable:** model-agnostic protocol, structured JSON/Markdown outputs, explicit provider boundary.

**Reusable:** MIT code; CC BY 4.0 methodology/docs/demo; synthetic rights-safe example.

## Shortlist blockers

1. **MCP connector evidence must be added before final submission.**
2. Every public link must be tested in a private/incognito browser.
3. Final submission must explicitly disclose AI assistants/models used for coding, analysis and writing.
4. The official template includes a video walkthrough field/final-check item. If the submission interface treats it as required, provide a sub-3-minute public walkthrough without relying on YouTube; otherwise mark it not applicable only if the interface permits.
5. Contact email used for the submission must be monitored through September 2026.
