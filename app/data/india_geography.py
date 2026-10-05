"""India-only geography catalogue used by the prototype map API.

The city names are stored in ``india_geography.json`` so they remain separate
from UI code and can later be replaced by an authoritative live GIS feed.
"""

import json
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def india_geography() -> dict:
    with (Path(__file__).with_name("india_geography.json")).open(encoding="utf-8") as source:
        return json.load(source)


def divisions() -> list[dict]:
    # The project review groups Jammu and Kashmir with the 29 selectable
    # state-level regions. The source catalogue otherwise keeps its modern UT
    # designation and remains the single source of city names.
    return [
        {**division, "type": "State" if division["name"] == "Jammu and Kashmir" else division["type"]}
        for division in india_geography()["states_and_union_territories"]
    ]


def cities_for(state: str) -> list[str]:
    return next((division["cities"] for division in divisions() if division["name"] == state), [])
