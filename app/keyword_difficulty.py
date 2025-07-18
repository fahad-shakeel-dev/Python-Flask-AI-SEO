# """
# keyword_difficulty.py
# ────────────────────────────────────────────────────────
# Mini‑SERP‑only wrapper around Ahrefs’ free RapidAPI endpoint:
#
#     /v1/keyword‑difficulty‑checker
#
# Returns:
#
#     {
#         "keyword":    "web development",
#         "difficulty": 76,
#         "shortage":   273,
#         "serp": [                  # first 10 organic rows (if present)
#             {
#                 "pos": 1,
#                 "title": "...",
#                 "url": "https://example.com",
#                 "dr":  92,
#                 "traffic": 8291,
#                 "cost": 3582569,
#                 "words": 5717
#             },
#             ...
#         ]
#     }
# """
#
# import os, http.client, json, urllib.parse
# from dotenv import load_dotenv
#
# load_dotenv()
# RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY") or ""
#
# _HOST = "ahrefs1.p.rapidapi.com"
# _HEADERS = {
#     "x-rapidapi-key":  RAPIDAPI_KEY,
#     "x-rapidapi-host": _HOST,
# }
#
# # ───────────────────────── internal helper ────────────────────────────
# def _get(path: str) -> dict:
#     conn = http.client.HTTPSConnection(_HOST)
#     conn.request("GET", path, headers=_HEADERS)
#     res = conn.getresponse()
#     body = res.read()
#
#     if res.status != 200:
#         raise RuntimeError(f"HTTP {res.status}: {body[:120]!r}")
#
#     try:
#         return json.loads(body.decode("utf-8"))
#     except json.JSONDecodeError:
#         raise RuntimeError("Invalid JSON from API")
#
# # ───────────────────────── public helper ──────────────────────────────
# def get_kd_and_serp(keyword: str, country: str = "us") -> dict:
#     if not keyword:
#         raise RuntimeError("Keyword is blank")
#
#     q = urllib.parse.quote_plus(keyword)
#     data = _get(f"/v1/keyword-difficulty-checker?keyword={q}&country={country}")
#
#     difficulty = (
#         data.get("difficulty")
#         or data.get("keyword_difficulty")
#         or data.get("keyword_difficulty_score")
#         or 0
#     )
#     shortage = data.get("shortage")
#
#     # Mini‑SERP rows bundled in the same payload
#     serp_rows = []
#     for blk in (data.get("serp", {}).get("results") or [])[:10]:
#         typ, payload = blk.get("content", [None, None])
#         if typ != "organic" or not isinstance(payload, dict):
#             continue
#
#         link = payload.get("link", [None, {}])[1]          # Ahrefs nested list
#         metrics = (link or {}).get("metrics") or {}
#
#         serp_rows.append({
#             "pos":      blk.get("pos"),
#             "title":    link.get("title"),
#             "url":      (link.get("url") or ["", {}])[1].get("url")
#                         if isinstance(link.get("url"), list) else None,
#             "dr":       metrics.get("domainRating"),
#             "traffic":  metrics.get("traffic"),
#             "cost":     metrics.get("cost"),
#             "words":    metrics.get("nrWords"),
#         })
#
#     return {
#         "keyword":    keyword,
#         "difficulty": int(difficulty),
#         "shortage":   shortage,
#         "serp":       serp_rows,
#     }
#
# # One‑liner kept for backward compatibility
# def get_kd(keyword: str, country: str = "us") -> int:
#     return get_kd_and_serp(keyword, country)["difficulty"]
#
#
#
# import os, http.client, json, urllib.parse
# from dotenv import load_dotenv
#
# load_dotenv()
# RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY") or ""
#
# _HOST = "ahrefs-keyword-research.p.rapidapi.com"
# _BASE_PATH = "/keyword-metrics"
#
# _HEADERS = {
#     "x-rapidapi-key": RAPIDAPI_KEY,
#     "x-rapidapi-host": _HOST,
# }
#
# def _get(path: str, params: dict) -> dict:
#     conn = http.client.HTTPSConnection(_HOST)
#     query = urllib.parse.urlencode(params)
#     conn.request("GET", f"{path}?{query}", headers=_HEADERS)
#     res = conn.getresponse()
#     body = res.read()
#
#     if res.status != 200:
#         raise RuntimeError(f"HTTP {res.status}: {body[:120]!r}")
#
#     try:
#         return json.loads(body.decode("utf-8"))
#     except json.JSONDecodeError:
#         raise RuntimeError("Invalid JSON from API")
#
# def get_kd_and_serp(keyword: str, country: str = "us") -> dict:
#     if not keyword:
#         raise RuntimeError("Keyword is blank")
#
#     params = {"keyword": keyword, "country": country}
#     data = _get(_BASE_PATH, params)
#
#     # Adjust based on response structure from test
#     api_data = data.get("data", {})
#     difficulty = api_data.get("difficulty") or 0
#     volume = api_data.get("searchVolume") or api_data.get("globalSearchVolume") or 0
#
#     serp_rows = []
#     results = api_data.get("serp_results") or api_data.get("serp") or []  # Adjust if SERP data exists
#     for item in results[:10]:
#         serp_rows.append({
#             "pos": item.get("position") or item.get("rank") or 0,
#             "title": item.get("title") or "N/A",
#             "url": item.get("url") or "N/A",
#             "dr": item.get("domain_rating") or item.get("dr") or 0,
#             "traffic": item.get("traffic") or item.get("trafficPotential") or 0,
#             "cost": item.get("cpc") or item.get("cost_per_click") or 0,
#             "words": item.get("word_count") or item.get("words") or 0,
#         })
#
#     return {
#         "keyword": api_data.get("keyword", keyword),
#         "difficulty": int(difficulty),
#         "shortage": volume,
#         "serp": serp_rows,
#     }
#
# def get_kd(keyword: str, country: str = "us") -> int:
#     return get_kd_and_serp(keyword, country)["difficulty"]















import os, http.client, json, urllib.parse
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY") or ""

_HOST = "ahrefs-keyword-research.p.rapidapi.com"
_BASE_PATH = "/keyword-metrics"

_HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": _HOST,
}

def _get(path: str, params: dict) -> dict:
    conn = http.client.HTTPSConnection(_HOST)
    query = urllib.parse.urlencode(params)
    conn.request("GET", f"{path}?{query}", headers=_HEADERS)
    res = conn.getresponse()
    body = res.read()

    if res.status != 200:
        raise RuntimeError(f"HTTP {res.status}: {body[:120]!r}")

    try:
        return json.loads(body.decode("utf-8"))
    except json.JSONDecodeError:
        raise RuntimeError("Invalid JSON from API")

def get_kd_and_serp(keyword: str, country: str = "us") -> dict:
    if not keyword:
        raise RuntimeError("Keyword is blank")

    params = {"keyword": keyword, "country": country}
    data = _get(_BASE_PATH, params)

    # Extract data from the nested structure
    api_data = data.get("data", {})
    difficulty = api_data.get("difficulty") or 0
    shortage = api_data.get("searchVolume") or 0
    clicks = api_data.get("clicks") or 0
    cpc = api_data.get("cpc") or 0.0
    global_volume = api_data.get("globalSearchVolume") or 0
    traffic_potential = api_data.get("trafficPotential") or 0

    serp_rows = []
    results = api_data.get("serp_results") or api_data.get("serp") or []  # Adjust if SERP data exists
    for item in results[:10]:
        serp_rows.append({
            "pos": item.get("position") or item.get("rank") or 0,
            "title": item.get("title") or "N/A",
            "url": item.get("url") or "N/A",
            "dr": item.get("domain_rating") or item.get("dr") or 0,
            "traffic": item.get("traffic") or item.get("trafficPotential") or 0,
            "clicks": item.get("clicks") or 0,
            "cpc": item.get("cpc") or 0.0,
        })

    return {
        "keyword": api_data.get("keyword", keyword),
        "difficulty": int(difficulty),
        "shortage": int(shortage),
        "clicks": int(clicks),
        "cpc": float(cpc),
        "globalVolume": int(global_volume),
        "trafficPotential": int(traffic_potential),
        "serp": serp_rows,
    }

def get_kd(keyword: str, country: str = "us") -> int:
    return get_kd_and_serp(keyword, country)["difficulty"]