# Alien/OpenAIRE MCP — completion plan

Purpose: close criterion 1 of the official OpenAIRE AI Hackathon 2026 evaluation template with a real, evidenced MCP invocation rather than a paper claim.

## Constraint

Do not change ATP's authority hierarchy. MCP-retrieved scholarly context is evidence/provenance, not editorial authority.

## Minimum successful evidence

Capture at least one real invocation through the official OpenAIRE MCP powered by Alien Intelligence and preserve:

- date/time of invocation;
- client/platform used;
- MCP server / Open Science plugin identity as exposed by the client;
- tool name(s) actually called;
- user research question;
- tool arguments/query;
- entity type(s) returned;
- approximate result count or returned set size;
- stable identifiers/metadata for a small rights-safe sample;
- any MCP/agent-generated interpretation separately from raw tool results;
- explicit note that the result did not modify source constraints automatically.

## Query sequence

Use short, robust queries because direct Graph experiments showed over-constrained keyword queries can return zero results.

### Query A — baseline discovery

**Question:** Find research products about literary translation.

Goal: establish that the official MCP path can retrieve OpenAIRE scholarly records for the domain.

### Query B — AI-specific refinement

**Question:** Find research products about AI-assisted translation or large language models in translation.

Goal: obtain a closer research-context set while observing whether the MCP agent broadens/refines the search.

### Query C — provenance/quality follow-up

**Question:** For the strongest relevant results, return stable identifiers and the available citation/open-access/provenance-related metadata without adding literary interpretation.

Goal: demonstrate why the MCP path adds structured scholarly context rather than generic web search.

## Comparison artifact

After a successful MCP run, add a rights-safe comparison file:

`demo/mcp/mcp_run_record.json`

Recommended fields:

```json
{
  "provider": "OpenAIRE MCP powered by Alien Intelligence",
  "client": "<actual client>",
  "timestamp_utc": "<actual timestamp>",
  "question": "<actual question>",
  "tools_called": [],
  "arguments": {},
  "entity_types": [],
  "returned_count": null,
  "sample_records": [],
  "agent_summary": null,
  "authority_note": "External research context is advisory/provenance only and cannot override the authorized source or ATP constraints."
}
```

Also create `demo/mcp/MCP_RUN_NOTES.md` with a human-readable account of what happened, including dead ends or query reformulation.

## Final integration changes after evidence exists

1. Update `submission/OFFICIAL_TEMPLATE_DRAFT.md` section 2.2 with actual MCP tool/client/entity details.
2. Update `submission/EVALUATION_MATRIX.md` criterion 1 from OPEN GATE to PASS.
3. Update README status to MCP-complete.
4. Update the final story journey with the real MCP step and any lesson learned.
5. Close GitHub issue #5 only after evidence is public and links work.
6. Run CI again.

## Non-goals

- Do not fabricate MCP output from direct API results.
- Do not call an unrelated third-party MCP and label it as Alien/OpenAIRE.
- Do not expose credentials, bearer tokens or private manuscript data.
- Do not let an agent-generated literary interpretation become a canonical ATP constraint without human acceptance.
