# ATP OpenAIRE — official submission-template draft

> Working copy aligned to the OpenAIRE AI Hackathon 2026 submission template. Items marked **GATE** must be closed before submission.

## 0. Submission details

**Submission title:** ATP OpenAIRE — Research provenance for constraint-preserved AI transcreation  
**Theme:** B — Build  
**Applicant / team name:** Ashraellen / Solo  
**Type:** Individual  
**Country / base of operations:** Poland  
**Contact person:** Nikolai Kostyshev  
**Contact email:** use the email registered for the hackathon in the final form; do not duplicate it in public repository files unless required.  
**GitHub:** https://github.com/Ashraellen

## 1. The solution

### 1.1 Overall

ATP OpenAIRE is a research/provenance extension of the pre-existing Ashraellen Transcreation Protocol (ATP), a human-directed, model-agnostic protocol for AI-assisted multilingual literary transcreation.

The problem is simple to state but difficult to control in practice: AI can retrieve useful external knowledge while simultaneously allowing that knowledge to become an invisible editorial influence. In literary and humanities work, a plausible external explanation can destroy intentional ambiguity, normalize unusual imagery, flatten a voice, or override a constraint established elsewhere in a long work.

Core ATP addresses the authorial side of that problem by making durable state explicit: authorized source, terminology, continuity, ambiguity, voice, structural rules, exceptions, bounded revision and human acceptance. ATP OpenAIRE adds a separate scholarly-context layer sourced from the OpenAIRE Graph. Research metadata is retrieved, normalized and recorded with provenance, but it remains subordinate to the authorized source and authorial constraints.

The public artifact is deliberately small and inspectable. A synthetic multilingual example plus an explicit constraint file drives a live OpenAIRE Graph retrieval. The demonstrator records the API version and query, normalizes returned research products, hashes the source and constraints with SHA-256, and emits provenance JSON, readable research-context Markdown and a manifest. GitHub Actions reruns the process against the live Graph and uploads reproducibility artifacts.

The intended users are authors, translators, editors, digital-humanities researchers and cultural-memory teams who want AI assistance without collapsing source authority, external evidence and model proposals into one opaque context window.

### 1.2 Quick SWOT

**Strengths**
- Real pre-hackathon methodology and production lineage rather than a one-off demo.
- Explicit human/AI/research authority boundaries.
- Live OpenAIRE retrieval, provenance capture and CI verification.
- Rights-safe synthetic demonstrator and split licensing.
- Model-agnostic core method.

**Weaknesses**
- Current public demonstrator is intentionally narrow and metadata-oriented.
- It does not claim to evaluate literary quality automatically.
- **GATE:** Alien/OpenAIRE MCP path must still be executed and documented.

**Opportunities**
- Multilingual digital humanities, archives, museums, editorial workflows and research communication.
- Expansion from research-product metadata to projects, datasets, software and organisations.
- Comparative provenance studies of direct API versus agent/MCP research paths.

**Threats**
- Over-reliance on retrieved context can create false authority if trust boundaries are ignored.
- Search-query sensitivity can reduce recall.
- Upstream API/MCP schema or availability changes can affect reproducibility.

### 1.3 The story — use case

See [`STORY_FINAL.md`](STORY_FINAL.md).

## 2. Technical & scientific

### 2.1 How it works

```text
Authorized source + explicit constraints
              |
              v
      research question/query
              |
              v
OpenAIRE Graph research provider
 direct API + [GATE: Alien MCP evidence]
              |
              v
normalized attributable research context
              |
              v
provenance JSON + readable context + manifest
              |
              v
AI candidate (proposal only)
              |
              v
bounded revision
              |
              v
human acceptance / authorized state
```

The architectural rule is that research retrieval is a provider layer, not an authority escalation. OpenAIRE-derived context can support awareness and verification; it cannot silently rewrite source constraints. The public demonstrator focuses on the retrieval/provenance slice because that slice can be reproduced without exposing unpublished literary material.

### 2.2 OpenAIRE Graph elements used

**Direct API implemented:** OpenAIRE Graph V3 `research-products` endpoint.  
**Entity type:** research products.  
**Query mode:** keyword search.  
**Current CI demonstration scale:** five returned research products per smoke run.  
**Captured elements:** identifiers and available normalized research-product metadata used by the public client, plus query/API provenance.  
**MCP tool powered by Alien Intelligence:** **GATE — must be executed and documented before final submission.**

The small scale is intentional: the artifact demonstrates authority separation and reproducible provenance rather than bibliometric volume.

### 2.3 Documentation & reproducibility

Requirements are Python 3.10+ and internet access. The direct demonstrator has no third-party Python runtime dependencies.

Run:

```bash
python demo/run_demo.py
```

Outputs:

```text
demo/generated/research_results.json
demo/generated/research_context.md
demo/generated/demo_manifest.json
```

The manifest ties outputs to exact synthetic source/constraint inputs using SHA-256. Unit tests verify normalization/context behavior. GitHub Actions executes the live OpenAIRE query, validates the manifest and uploads generated files as an artifact.

See README, `docs/ARCHITECTURE.md`, `methodology/ATP_METHOD_v0.1.md` and `requirements.txt`.

## 3. Innovation & risks

### What is new here

ATP OpenAIRE is not a generic RAG wrapper. Its contribution is an authority architecture: authorized source, durable authorial state, external research and model-generated candidates remain distinct. The OpenAIRE layer is therefore inspectable evidence with provenance rather than hidden prompt context that automatically acquires editorial authority.

The project also demonstrates how a pre-existing human-directed creative protocol can gain open-science research grounding without rewriting its prior history or opening private literary masters.

### Limitations and known failure modes

- Keyword retrieval is query-sensitive; long or over-constrained queries may return no results.
- Retrieved metadata can be incomplete and must not be treated as proof of a literary interpretation.
- Current demo covers a small research-products slice, not the full Graph relationship space.
- No automatic metric can certify preservation of authorial voice; human acceptance remains required.
- Live dependencies can change or become temporarily unavailable.
- **GATE:** final submission needs documented use of the OpenAIRE/Alien MCP connector.

### Use of AI

AI assistance is disclosed rather than hidden. OpenAI ChatGPT was used as a development collaborator for technical research, code drafting/review, documentation, submission editing and QA. Human authority remained responsible for project direction, acceptance of changes, rights boundaries and final submission decisions. The public runtime demonstrator itself does not require an LLM to perform the deterministic direct-API retrieval/provenance step.

**GATE:** once the OpenAIRE/Alien MCP connector is used, record the agent/platform, query/purpose and resulting provenance here.

### Data protection & third-party content

The public demonstrator uses synthetic literary content. No unpublished MONOLITH literary master or private production state is included. No credentials or API keys are committed. OpenAIRE metadata is used with attribution/provenance. Public written materials are CC BY 4.0; software is MIT. Literary works remain separately copyrighted.

## 4. Links & artifacts

| Item | Link | Status | Notes |
|---|---|---|---|
| Code repository | https://github.com/Ashraellen/atp-openaire | Public | Hackathon extension |
| Core methodology | https://github.com/Ashraellen/ashraellen-atp | Public | Predates hackathon |
| Core ATP DOI | https://doi.org/10.5281/zenodo.21838981 | Public | DOI-backed lineage |
| Live CI | repository Actions tab | Public | Direct API smoke run |
| Main artifact | repository root + `demo/` | Public | Code/workflow/methodology |
| Documentation / README | repository README | Public | Run and architecture guidance |
| Story | `submission/STORY_FINAL.md` | Public | 1–2 page write-up |
| Video walkthrough | **GATE / determine requirement in final interface** | — | If required, keep <3 minutes and publicly reachable without login; YouTube is not technically necessary if another public host is accepted |
| Archived hackathon version with DOI | Optional / recommended | — | Create after final MCP-complete release if useful |

## 5. Openness & licensing

**Written materials, documentation and public demo text:** CC BY 4.0 — confirmed.  
**Code:** MIT.  
**Data/outputs produced:** document explicit attribution/licensing in final package; OpenAIRE-origin metadata retains source provenance.  
**Right to submit included material:** confirmed subject to final human check.  
**OpenAIRE publication/community voting permissions:** to be confirmed in final submission interface by the participant.

## 6. Feedback (optional)

A useful technical observation from the direct Graph API path: highly specific multi-concept keyword queries can return zero records, while a shorter query can restore useful results. This reinforces the need to record exact retrieval queries as provenance rather than presenting research context as deterministic or exhaustive.

Further MCP-specific feedback will be added after the Alien/OpenAIRE connector path is exercised.

## 7. Before submission — current gate

- [x] Theme selected: B — Build
- [x] Public story written
- [x] README and run instructions present
- [x] LICENSE declarations present
- [x] Dependencies documented
- [x] Commit history visible
- [x] No credentials/API keys required for direct demo
- [x] Live direct OpenAIRE Graph CI passes
- [x] Provenance and rights boundaries documented
- [ ] **Use and document OpenAIRE/Alien AI MCP connector**
- [ ] Test every final link in private/incognito browser
- [ ] Resolve whether video is mandatory in the final submission interface; if required, provide <3-minute public walkthrough without mandatory YouTube
- [ ] Fill final contact email in the submission interface and monitor it through September 2026
- [ ] Confirm publication/community-voting checkboxes in the submission interface
- [ ] Submit before 20 August 2026, 23:59 CET; operationally target much earlier
