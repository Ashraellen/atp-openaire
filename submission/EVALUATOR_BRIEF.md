# ATP OpenAIRE — one-minute evaluator brief

**Problem:** Fluent AI translation can erase intentional ambiguity, voice, repetition, terminology, and long-range continuity. External research can help, but becomes risky when retrieval silently turns into editorial authority.

**Prior work:** The Ashraellen Transcreation Protocol (ATP) already existed as a human-directed, model-agnostic method for preserving durable authorial state and explicit human acceptance in AI-assisted literary transcreation. It has a separate public repository and DOI-backed release history.

**Hackathon contribution:** ATP OpenAIRE is a bounded research/provenance extension. It retrieves scholarly metadata from OpenAIRE Graph V3, normalizes and attributes it, binds it to exact public source/constraint inputs through SHA-256 hashes, and keeps that external context structurally separate from authorial authority.

**Working proof:** GitHub Actions runs deterministic tests plus a live OpenAIRE Graph query, validates the generated manifest, and uploads provenance/context artifacts.

**Why it matters:** The design makes external research inspectable without giving retrieved material hidden permission to rewrite the source.

**Reuse:** The client, provenance layer, constraint model, manifest pattern, trust-boundary architecture, tests, and CI can be reused across multilingual digital humanities, editorial, archival, museum, and research-communication workflows.

**Core ATP:** https://github.com/Ashraellen/ashraellen-atp  
**DOI:** https://doi.org/10.5281/zenodo.21838981  
**Hackathon artifact:** https://github.com/Ashraellen/atp-openaire
