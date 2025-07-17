"""
keyword_difficulty.py
────────────────────────────────────────────────────────
Mini‑SERP‑only wrapper around Ahrefs’ free RapidAPI endpoint:

    /v1/keyword‑difficulty‑checker

Returns:

    {
        "keyword":    "web development",
        "difficulty": 76,
        "shortage":   273,
        "serp": [                  # first 10 organic rows (if present)
            {
                "pos": 1,
                "title": "...",
                "url": "https://example.com",
                "dr":  92,
                "traffic": 8291,
                "cost": 3582569,
                "words": 5717
            },
            ...
        ]
    }
"""

import os, http.client, json, urllib.parse
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY") or ""

_HOST = "ahrefs1.p.rapidapi.com"
_HEADERS = {
    "x-rapidapi-key":  RAPIDAPI_KEY,
    "x-rapidapi-host": _HOST,
}

# ───────────────────────── internal helper ────────────────────────────
def _get(path: str) -> dict:
    conn = http.client.HTTPSConnection(_HOST)
    conn.request("GET", path, headers=_HEADERS)
    res = conn.getresponse()
    body = res.read()

    if res.status != 200:
        raise RuntimeError(f"HTTP {res.status}: {body[:120]!r}")

    try:
        return json.loads(body.decode("utf-8"))
    except json.JSONDecodeError:
        raise RuntimeError("Invalid JSON from API")

# ───────────────────────── public helper ──────────────────────────────
def get_kd_and_serp(keyword: str, country: str = "us") -> dict:
    if not keyword:
        raise RuntimeError("Keyword is blank")

    q = urllib.parse.quote_plus(keyword)
    data = _get(f"/v1/keyword-difficulty-checker?keyword={q}&country={country}")

    difficulty = (
        data.get("difficulty")
        or data.get("keyword_difficulty")
        or data.get("keyword_difficulty_score")
        or 0
    )
    shortage = data.get("shortage")

    # Mini‑SERP rows bundled in the same payload
    serp_rows = []
    for blk in (data.get("serp", {}).get("results") or [])[:10]:
        typ, payload = blk.get("content", [None, None])
        if typ != "organic" or not isinstance(payload, dict):
            continue

        link = payload.get("link", [None, {}])[1]          # Ahrefs nested list
        metrics = (link or {}).get("metrics") or {}

        serp_rows.append({
            "pos":      blk.get("pos"),
            "title":    link.get("title"),
            "url":      (link.get("url") or ["", {}])[1].get("url")
                        if isinstance(link.get("url"), list) else None,
            "dr":       metrics.get("domainRating"),
            "traffic":  metrics.get("traffic"),
            "cost":     metrics.get("cost"),
            "words":    metrics.get("nrWords"),
        })

    return {
        "keyword":    keyword,
        "difficulty": int(difficulty),
        "shortage":   shortage,
        "serp":       serp_rows,
    }

# One‑liner kept for backward compatibility
def get_kd(keyword: str, country: str = "us") -> int:
    return get_kd_and_serp(keyword, country)["difficulty"]
