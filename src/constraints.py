"""Load the small YAML subset used by the ATP public demonstrator.

This intentionally avoids external dependencies. Supported syntax is limited to:
- top-level scalar keys;
- top-level lists using ``- item``;
- comments and blank lines.

It is not a general YAML parser.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def _scalar(value: str) -> Any:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none", "~"}:
        return None
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def load_constraint_yaml(path: str | Path) -> dict[str, Any]:
    """Parse the deliberately small YAML subset used in ``demo/constraints.yaml``."""

    result: dict[str, Any] = {}
    current_list: str | None = None

    for line_number, raw_line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- "):
            if current_list is None:
                raise ValueError(f"List item without a key at line {line_number}")
            value = _scalar(stripped[2:])
            target = result[current_list]
            if not isinstance(target, list):
                raise ValueError(f"Internal parser state error at line {line_number}")
            target.append(value)
            continue

        if ":" not in raw_line:
            raise ValueError(f"Expected 'key: value' at line {line_number}")

        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError(f"Empty key at line {line_number}")

        if value == "":
            result[key] = []
            current_list = key
        else:
            result[key] = _scalar(value)
            current_list = None

    return result
