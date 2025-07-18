"""
site_audit.py
------------
Full‑fat helper around Google PageSpeed Insights (v5).
Returns category scores, lab metrics, field metrics, and opportunity advice.
"""

from __future__ import annotations
import logging, os, time, requests
from typing import Dict, List
from dotenv import load_dotenv

# ── Config ───────────────────────────────────────────────────────────────── #
load_dotenv()
TIMEOUT_SECS = int(os.getenv("PSI_TIMEOUT", 60))

API_KEY  = os.getenv("PSI_API_KEY", "")
BASE_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
CATEGORIES = ["performance", "best-practices", "seo"]
MAX_RETRIES, BACKOFF_BASE = 3, 2
TIMEOUT_SECS = 90


# ── Low‑level call (handles 403/429) ─────────────────────────────────────── #
def _call_psi(url: str, strategy: str, use_key: bool) -> dict:
    params: list[tuple[str, str]] = [
        ("url", url),
        ("strategy", strategy.lower()),
        *[( "category", c ) for c in CATEGORIES],
    ]
    if use_key and API_KEY:
        params.append(("key", API_KEY))

    r = requests.get(BASE_URL, params=params, timeout=TIMEOUT_SECS)

    # Rate‑limit → 429
    if r.status_code == 429:
        raise requests.HTTPError("429 Too Many Requests", response=r)

    try:
        r.raise_for_status()
    except requests.HTTPError as he:
        try:
            detail = r.json().get("error", {}).get("message", "")
        except Exception:
            detail = r.text[:200]
        raise RuntimeError(f"PSI API error {r.status_code}: {detail}") from he

    return r.json()


def run_pagespeed(url: str, strategy: str = "desktop") -> dict:
    """Retries on 429; falls back to key‑less when 403."""
    logging.info("PSI %s (%s)", url, strategy)
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return _call_psi(url, strategy, use_key=True)
        except requests.HTTPError as he:
            if he.response.status_code == 429:        # back‑off
                retry_after = he.response.headers.get("Retry-After")
                wait = int(retry_after) if retry_after else BACKOFF_BASE ** attempt
                logging.warning("429 – sleeping %ss", wait); time.sleep(wait); continue
            if "403" in str(he) and attempt == 1:     # one key‑less try
                logging.warning("403 – retrying without key")
                return _call_psi(url, strategy, use_key=False)
            raise
    raise RuntimeError("Rate‑limit exceeded – try later or raise your quota.")


# ── Friendly extractor ───────────────────────────────────────────────────── #
# ── Result extraction ───────────────────────────────────────────────── #
def extract_all(data: dict) -> dict:
    """
    Build four sections:
      • category_scores  – Performance, A11Y, etc.
      • lab_metrics      – every numeric Lighthouse audit
      • field_metrics    – CrUX 75‑percentile CWV values
      • opportunities    – audits with 'opportunity' details
    Empty / missing values are rendered as '—'.
    """
    lh      = data["lighthouseResult"]
    audits  = lh["audits"]
    loading = data.get("loadingExperience", {}).get("metrics", {})

    # Category scores
    cat_scores = {
        cat_info["title"]: round(cat_info["score"] * 100)
        for cat_info in lh["categories"].values()
    }

    # Lab metrics – guard against missing displayValue
    lab = {}
    for audit in audits.values():
        if audit.get("scoreDisplayMode") == "numeric":
            title = audit["title"]
            display = (
                audit.get("displayValue")           # normal case
                or audit.get("numericValue")        # fallback raw number
                or "—"
            )
            lab[title] = display

    # Field (CrUX) metrics
    field = {
        m.replace("_", " ").title(): v.get("percentile", "—")
        for m, v in loading.items()
    }

    # Opportunities – displayValue may also be missing
    opp = [
        {
            "title": a["title"],
            "displayValue": a.get("displayValue", "—"),
        }
        for a in audits.values()
        if a.get("details", {}).get("type") == "opportunity"
    ]

    return {
        "category_scores": cat_scores,
        "lab_metrics":     lab,
        "field_metrics":   field,
        "opportunities":   opp,
    }
