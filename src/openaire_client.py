"""Minimal OpenAIRE Graph V3 client for the ATP demonstrator."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://api.openaire.eu/graph/v3"


@dataclass(frozen=True)
class OpenAIREClient:
    """Small dependency-free client for OpenAIRE Graph V3."""

    base_url: str = DEFAULT_BASE_URL
    timeout: float = 30.0
    bearer_token: str | None = None

    def search_research_products(
        self,
        search: str,
        *,
        product_type: str | None = None,
        page: int = 1,
        page_size: int = 10,
        sort_by: str = "relevance DESC",
        include_stats: bool = False,
    ) -> dict[str, Any]:
        if not search.strip():
            raise ValueError("search must not be empty")
        if page < 1:
            raise ValueError("page must be >= 1")
        if not 1 <= page_size <= 100:
            raise ValueError("page_size must be between 1 and 100")

        params: dict[str, str | int | bool] = {
            "search": search,
            "page": page,
            "pageSize": page_size,
            "sortBy": sort_by,
            "includeStats": str(include_stats).lower(),
        }
        if product_type:
            params["type"] = product_type

        return self._get_json("research-products", params)

    def get_research_product(self, product_id: str) -> dict[str, Any]:
        if not product_id.strip():
            raise ValueError("product_id must not be empty")
        return self._get_json(f"research-products/{product_id}", {})

    def _get_json(self, path: str, params: dict[str, Any]) -> dict[str, Any]:
        query = urlencode(params)
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        if query:
            url = f"{url}?{query}"

        headers = {
            "Accept": "application/json",
            "User-Agent": "atp-openaire/0.1 (+https://github.com/Ashraellen/atp-openaire)",
        }
        if self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"

        request = Request(url, headers=headers, method="GET")
        with urlopen(request, timeout=self.timeout) as response:
            payload = response.read().decode("utf-8")
            return json.loads(payload)
