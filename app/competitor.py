"""
competitor.py – SEO Competitor Comparison Blueprint
===================================================

Routes
------
GET  /competitor            → UI page  (templates/competitor.html)
POST /competitor/compare    → JSON API (called by compare.js)
"""

from __future__ import annotations
import logging, re, traceback
from typing import List, Dict, Any

import requests, textstat
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, request, jsonify
from keybert import KeyBERT

# ────────────────────────── Blueprint ──────────────────────────
# ONE url_prefix; do *not* repeat it in app.register_blueprint
competitor_bp = Blueprint("competitor", __name__, url_prefix="/competitor")

kw_model = KeyBERT()
TAG_RE   = re.compile(r"<[^>]+>")
HEADERS  = {
    "User-Agent": "SEO-Helper-Bot/1.0 (+github.com/yourrepo)",
    "Accept":     "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ───────────────────── 1. SERP & Topic helpers ─────────────────────
def fetch_serp_urls(keyword: str, num_results: int = 3) -> List[str]:
    """Top Google links for `keyword` (fallback to placeholders)."""
    if not keyword.strip():
        raise ValueError("Keyword must not be blank")

    try:
        resp = requests.get(
            "https://www.google.com/search",
            params={"q": keyword, "num": num_results},
            headers=HEADERS, timeout=5
        )
        resp.raise_for_status()
        soup  = BeautifulSoup(resp.text, "html.parser")
        links = []
        for a in soup.select("a"):
            href = a.get("href", "")
            m = re.match(r"/url\\?q=(https?://[^&]+)", href)
            if m:
                links.append(m.group(1))
            if len(links) >= num_results:
                break
        if links:
            return links[:num_results]
        raise RuntimeError("No SERP links parsed")

    except Exception as e:
        logging.warning("SERP fetch failed: %s – using placeholders", e)
        return [f"https://example.com/result{i+1}" for i in range(num_results)]


def fetch_page(url: str) -> str:
    """Return HTML of a URL or empty string on error."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=8)
        r.raise_for_status()
        return r.text
    except Exception as e:
        logging.warning("fetch_page failed for %s – %s", url, e)
        return ""


def extract_topics(html: str) -> List[str]:
    """Headings + capitalised entities from a page."""
    soup = BeautifulSoup(html, "html.parser")
    headings = [
        h.get_text(" ", strip=True).lower()
        for h in soup.find_all(["h1", "h2", "h3"])
    ]
    text = soup.get_text(" ", strip=True)
    entities = re.findall(r"\\b([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)\\b", text)
    entities = [e.lower() for e in entities]

    seen, uniq = set(), []
    for t in headings + entities:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq


def get_competitor_topics(keyword: str, top_n: int = 3) -> List[str]:
    """keyword → SERP URLs → pages → merged topic list."""
    urls = fetch_serp_urls(keyword, top_n)
    all_topics: list[str] = []
    for u in urls:
        html = fetch_page(u)
        if html:
            all_topics.extend(extract_topics(html))
    seen, unique = set(), []
    for t in all_topics:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    return unique

# ───────────────────── 2. Lightweight analyser ─────────────────────
def analyse(content: str) -> Dict[str, Any]:
    """Return quick SEO stats from raw text or HTML snippet."""
    is_html = bool(TAG_RE.search(content))
    if is_html:
        soup = BeautifulSoup(content, "html.parser")
        text = soup.get_text(" ", strip=True)
        h1   = len(soup.find_all("h1"))
        h2   = len(soup.find_all("h2"))
    else:
        text, h1, h2 = content, 0, 0

    try:
        kw_count = len(kw_model.extract_keywords(text, top_n=5))
    except Exception:
        kw_count = 0

    return {
        "word_count":  len(text.split()),
        "readability": round(textstat.flesch_reading_ease(text), 2),
        "keywords":    kw_count,
        "h1":          h1,
        "h2":          h2,
    }

# ───────────────────── 3. Flask routes ─────────────────────
@competitor_bp.get("/")
def competitor_page():
    return render_template("competitor.html")


@competitor_bp.post("/compare")
def compare():
    """
    Expects JSON:
      { "your_content": "<p>…</p>", "competitor_url": "https://…" }
    Returns JSON:
      { "ok": true|false, "error": "...", "yours": {...}, "competitor": {...} }
    """
    try:
        data = request.get_json(force=True) or {}
        your_raw       = (data.get("your_content")   or "").strip()
        competitor_url = (data.get("competitor_url") or "").strip()

        if not your_raw or not competitor_url:
            return jsonify(ok=False, error="Both fields are required"), 200

        if not competitor_url.startswith(("http://", "https://")):
            competitor_url = "https://" + competitor_url

        try:
            resp = requests.get(
                competitor_url, headers=HEADERS,
                timeout=15, allow_redirects=True
            )
            resp.raise_for_status()
        except requests.RequestException as exc:
            return jsonify(ok=False, error=f"Cannot fetch URL: {exc}"), 200

        return jsonify(
            ok=True,
            yours=analyse(your_raw),
            competitor=analyse(resp.text)
        )

    except Exception as e:
        logging.error("compare fatal", exc_info=True)
        return jsonify(ok=False, error="Internal server error"), 500
