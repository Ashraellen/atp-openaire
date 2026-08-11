# ATP OpenAIRE — walkthrough script (target: 2:15–2:45)

This script is designed for a short public screen-recorded walkthrough if the final OpenAIRE submission interface requires the video item from the official template. It does not require YouTube specifically.

## 0:00–0:20 — problem and project

**Screen:** repository README, title and lineage section.

**Voiceover:**

“ATP OpenAIRE is a research-provenance extension of the Ashraellen Transcreation Protocol, a pre-existing human-directed method for AI-assisted literary transcreation. The problem is not simply getting more information into an AI system. The problem is keeping external research useful without allowing it to silently override the author’s source, ambiguity, terminology or voice.”

## 0:20–0:45 — authority architecture

**Screen:** `docs/ARCHITECTURE.md` or the README flow.

**Voiceover:**

“ATP keeps four layers separate: the authorized source, durable authorial constraints, external scholarly context, and model-generated proposals. OpenAIRE belongs in the research layer. It can inform verification and awareness, but it does not automatically become an editorial instruction. Human acceptance remains the canonical gate.”

## 0:45–1:15 — working direct demonstrator

**Screen:** `demo/constraints.yaml`, then `demo/run_demo.py`, then GitHub Actions successful run.

**Voiceover:**

“The public demonstrator uses a synthetic passage and explicit constraints. It queries OpenAIRE Graph V3, normalizes returned research products, records the exact query and API version, hashes the source and constraints with SHA-256, and produces provenance JSON, readable research context and a manifest. GitHub Actions reruns the live query, validates the manifest and stores the generated artifacts.”

## 1:15–1:40 — OpenAIRE/Alien MCP

**Screen:** real MCP run evidence after criterion 1 is completed: `demo/mcp/MCP_RUN_NOTES.md` and/or the actual OpenAIRE/Alien client screen.

**Voiceover template — DO NOT record until true:**

“For the hackathon path, the same research question is also exercised through the OpenAIRE MCP powered by Alien Intelligence. We record the tool invocation, query, returned entity types and a rights-safe sample so that the agentic research path is inspectable rather than hidden. The MCP output remains subject to the same ATP trust boundary.”

## 1:40–2:05 — what is reusable

**Screen:** repository map, `requirements.txt`, licensing and core ATP link.

**Voiceover:**

“The reusable part is not a single translation prompt. It is the separation of authority and provenance. The direct demonstrator is Python 3.10 plus the standard library, the software is MIT licensed, public methodology and documentation are CC BY 4.0, and the core ATP methodology has a separate DOI-backed history. The same pattern can be applied to digital humanities, multilingual editing, archives and research communication.”

## 2:05–2:25 — limitation and close

**Screen:** `submission/EVALUATION_MATRIX.md` or limitations section.

**Voiceover:**

“This is deliberately not an autonomous literary judge. Search can be incomplete, metadata can be imperfect, and no metric can certify authorial voice. ATP’s answer is to make those limits visible and keep the final decision human. The goal is simple: research should become more traceable without becoming more authoritative than the work it is meant to support.”

## Recording checklist

- Keep total duration below 3 minutes.
- Use readable browser zoom; avoid tiny terminal text.
- Show only public repository content and rights-safe MCP results.
- Do not expose email inboxes, tokens, API keys, browser profiles or unpublished MONOLITH text.
- If a live command is shown, pre-test it; do not waste video time waiting on network latency.
- Include captions if the hosting method supports them.
- Verify the final video link from a private/incognito browser with no login.
- Do not say the MCP step is complete until a real OpenAIRE/Alien MCP invocation has been captured.
