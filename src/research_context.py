"""Normalize OpenAIRE Graph results into a compact ATP research context."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _first(value: Any) -> Any:
    if isinstance(value, list):
        return value[0] if value else None
    return value


def _authors(product: dict[str, Any]) -> list[str]:
    raw = product.get("authors") or product.get("creators") or []
    names: list[str] = []
    if not isinstance(raw, list):
        raw = [raw]
    for item in raw:
        if isinstance(item, str):
            names.append(item)
        elif isinstance(item, dict):
            name = item.get("fullName") or item.get("name") or item.get("fullname")
            if name:
                names.append(str(name))
    return names


def _identifiers(product: dict[str, Any]) -> list[dict[str, str]]:
    candidates = product.get("pids") or product.get("identifiers") or []
    if not isinstance(candidates, list):
        candidates = [candidates]
    out: list[dict[str, str]] = []
    for item in candidates:
        if isinstance(item, str):
            out.append({"value": item})
        elif isinstance(item, dict):
            value = item.get("value") or item.get("id") or item.get("identifier")
            if value:
                row = {"value": str(value)}
                scheme = item.get("scheme") or item.get("type")
                if scheme:
                    row["scheme"] = str(scheme)
                out.append(row)
    return out


def normalize_product(product: dict[str, Any]) -> dict[str, Any]:
    """Extract stable, human-auditable fields while retaining the OpenAIRE id."""

    title = product.get("mainTitle") or product.get("title") or product.get("displayName")
    if isinstance(title, list):
        title = _first(title)
    publication_date = product.get("publicationDate") or product.get("dateOfAcceptance") or product.get("date")
    product_type = product.get("type") or product.get("resultType")
    access = product.get("bestAccessRight") or product.get("accessRight") or product.get("openAccessColor")

    return {
        "openaire_id": product.get("id"),
        "title": title,
        "publication_date": publication_date,
        "type": product_type,
        "authors": _authors(product),
        "identifiers": _identifiers(product),
        "access": access,
        "citation_count": product.get("citationCount") or product.get("citationsCount"),
    }


def build_research_context(query: str, response: dict[str, Any]) -> dict[str, Any]:
    """Create the compact research-context and provenance envelope used by ATP."""

    header = response.get("header") if isinstance(response.get("header"), dict) else {}
    raw_results = response.get("results") if isinstance(response.get("results"), list) else []
    products = [normalize_product(item) for item in raw_results if isinstance(item, dict)]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "name": "OpenAIRE Graph",
            "api_version": "v3",
            "endpoint": "https://api.openaire.eu/graph/v3/research-products",
            "query": query,
            "license_note": "OpenAIRE Graph records are reusable under CC BY with source acknowledgement.",
        },
        "retrieval": {
            "num_found": header.get("numFound"),
            "query_time_ms": header.get("queryTime"),
            "page": header.get("page"),
            "page_size": header.get("pageSize"),
            "returned": len(products),
        },
        "products": products,
    }


def render_context_markdown(context: dict[str, Any]) -> str:
    """Render a compact, reviewable Markdown research-context document."""

    source = context["source"]
    retrieval = context["retrieval"]
    lines = [
        "# ATP Research Context",
        "",
        f"**Query:** {source['query']}",
        f"**Source:** {source['name']} {source['api_version']}",
        f"**Retrieved:** {context['generated_at']}",
        f"**Matches reported by API:** {retrieval.get('num_found')}",
        "",
        "## Retrieved research products",
        "",
    ]

    if not context["products"]:
        lines.append("No research products were returned.")
    else:
        for index, product in enumerate(context["products"], 1):
            title = product.get("title") or "Untitled research product"
            authors = ", ".join(product.get("authors") or []) or "Unknown authors"
            lines.extend([
                f"### {index}. {title}",
                "",
                f"- Authors: {authors}",
                f"- Publication date: {product.get('publication_date') or 'Unknown'}",
                f"- OpenAIRE id: {product.get('openaire_id') or 'Unknown'}",
                f"- Type: {product.get('type') or 'Unknown'}",
                f"- Citation count: {product.get('citation_count') if product.get('citation_count') is not None else 'Unknown'}",
                "",
            ])

    lines.extend([
        "## Provenance note",
        "",
        "This file is generated from OpenAIRE Graph metadata. It is research context for an auditable human–AI transcreation workflow; retrieval does not by itself determine a translation or editorial decision.",
        "",
    ])
    return "\n".join(lines)
