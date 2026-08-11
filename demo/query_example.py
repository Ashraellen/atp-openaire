"""Small reproducible OpenAIRE Graph query for the ATP demonstrator."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.openaire_client import OpenAIREClient


QUERY = "literary translation large language models"


def main() -> None:
    client = OpenAIREClient()
    result = client.search_research_products(
        QUERY,
        product_type="publication",
        page_size=5,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
