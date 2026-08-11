"""Run the public ATP + OpenAIRE end-to-end demonstrator.

Pipeline:
constraints.yaml -> OpenAIRE Graph V3 -> normalized provenance JSON ->
research_context.md -> demo_manifest.json

The script deliberately stops before any model-generated transcreation step. That
keeps the public demo reproducible without requiring a proprietary AI API key and
makes the boundary between retrieval, constraints, and later human–AI work explicit.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo"
sys.path.insert(0, str(ROOT))

from src.constraints import load_constraint_yaml
from src.openaire_client import OpenAIREClient
from src.research_context import build_research_context, render_context_markdown


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    constraints_path = DEMO / "constraints.yaml"
    source_path = DEMO / "source.txt"
    output_dir = DEMO / "generated"
    output_dir.mkdir(parents=True, exist_ok=True)

    constraints_text = constraints_path.read_text(encoding="utf-8")
    source_text = source_path.read_text(encoding="utf-8")
    constraints = load_constraint_yaml(constraints_path)

    query = str(constraints.get("research_query", "")).strip()
    if not query:
        raise ValueError("constraints.yaml must define a non-empty research_query")

    client = OpenAIREClient()
    raw_response = client.search_research_products(
        query,
        product_type="publication",
        page_size=5,
        sort_by="relevance DESC",
        include_stats=False,
    )
    context = build_research_context(query, raw_response)

    provenance_path = output_dir / "research_results.json"
    context_path = output_dir / "research_context.md"
    manifest_path = output_dir / "demo_manifest.json"

    provenance_path.write_text(
        json.dumps(context, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    context_path.write_text(render_context_markdown(context), encoding="utf-8")

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project_id": constraints.get("project_id"),
        "pipeline_stage": "research-context-ready",
        "inputs": {
            "source": {
                "path": "demo/source.txt",
                "sha256": sha256_text(source_text),
            },
            "constraints": {
                "path": "demo/constraints.yaml",
                "sha256": sha256_text(constraints_text),
            },
        },
        "research": {
            "provider": "OpenAIRE Graph",
            "api_version": "v3",
            "query": query,
            "returned": context["retrieval"]["returned"],
            "provenance_path": "demo/generated/research_results.json",
            "context_path": "demo/generated/research_context.md",
        },
        "constraint_summary": {
            "preserve": constraints.get("preserve", []),
            "forbid": constraints.get("forbid", []),
            "bounded_revision_passes": constraints.get("bounded_revision_passes"),
            "require_human_review": constraints.get("require_human_review"),
        },
        "next_stage": "constraint-aware transcreation followed by one bounded revision and human review",
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("ATP OpenAIRE demonstrator completed")
    print(f"query: {query}")
    print(f"research products returned: {context['retrieval']['returned']}")
    print(f"provenance: {provenance_path.relative_to(ROOT)}")
    print(f"context: {context_path.relative_to(ROOT)}")
    print(f"manifest: {manifest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
