#!/usr/bin/env python3
"""
TabSlayer Demo - Interactive version
Shows demo with no command-line issues
"""

import sys
import time
import json
from pathlib import Path
import requests
from datetime import datetime

def fetch_wikipedia_simple(query: str) -> list:
    """Fetch from Wikipedia API"""
    try:
        url = "https://en.wikipedia.org/w/api.php"
        headers = {"User-Agent": "TabSlayer/1.0"}
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srwhat": "text",
            "format": "json",
            "srlimit": 5
        }
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()

        findings = []
        for result in data.get("query", {}).get("search", [])[:5]:
            findings.append({
                "title": result["title"],
                "source": "Wikipedia",
                "url": f"https://en.wikipedia.org/wiki/{result['title'].replace(' ', '_')}",
                "snippet": result.get("snippet", "")[:100],
                "date": datetime.now().strftime("%Y-%m-%d"),
                "relevance": 0.9
            })

        print("[OK] Wikipedia: {} results".format(len(findings)))
        return findings
    except Exception as e:
        print("[WARNING] Wikipedia: {}".format(str(e)[:50]))
        return []

def fetch_arxiv_simple(query: str) -> list:
    """Fetch from arXiv API"""
    try:
        import xml.etree.ElementTree as ET

        url = "http://export.arxiv.org/api/query"
        params = {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": 5,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }

        response = requests.get(url, params=params, timeout=5)
        root = ET.fromstring(response.content)

        findings = []
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns)[:5]:
            try:
                title = entry.find("{http://www.w3.org/2005/Atom}title")
                summary = entry.find("{http://www.w3.org/2005/Atom}summary")
                arxiv_id = entry.find("{http://arxiv.org/schemas/atom}id")

                if title is not None:
                    findings.append({
                        "title": title.text.strip()[:80],
                        "source": "arXiv",
                        "url": f"https://arxiv.org/abs/{arxiv_id.text.split('/abs/')[-1]}" if arxiv_id else "",
                        "snippet": summary.text.strip()[:100] if summary else "",
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "relevance": 0.85
                    })
            except:
                continue

        print("[OK] arXiv: {} papers".format(len(findings)))
        return findings
    except Exception as e:
        print("[WARNING] arXiv: {}".format(str(e)[:50]))
        return []

def load_cache(query: str):
    """Load from cache"""
    cache_dir = Path(__file__).parent.parent / "cache"
    if not cache_dir.exists():
        cache_dir.mkdir(exist_ok=True)

    safe_query = "".join(c if c.isalnum() or c in "-_ " else "" for c in query).replace(" ", "_")
    cache_file = cache_dir / f"{safe_query}.json"

    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return json.load(f)
    return None

def save_cache(query: str, results: dict):
    """Save to cache"""
    cache_dir = Path(__file__).parent.parent / "cache"
    cache_dir.mkdir(exist_ok=True)

    safe_query = "".join(c if c.isalnum() or c in "-_ " else "" for c in query).replace(" ", "_")
    cache_file = cache_dir / f"{safe_query}.json"

    with open(cache_file, 'w') as f:
        json.dump(results, f, indent=2)

def aggregate_results(all_findings: list, query: str) -> dict:
    """Simple aggregation"""
    seen_urls = set()
    unique = []

    for finding in all_findings:
        url = finding.get("url", "").lower()
        if url not in seen_urls:
            unique.append(finding)
            seen_urls.add(url)

    unique = unique[:5]

    return {
        "query": query,
        "sources": len(set(f["source"] for f in unique)),
        "findings": unique,
        "timestamp": datetime.now().isoformat()
    }

def display_results(results: dict):
    """Display results nicely"""
    print("\n" + "="*80)
    print("RESULTS FOR: {}".format(results['query']))
    print("="*80)
    print("Found: {} findings\n".format(len(results['findings'])))

    for i, finding in enumerate(results['findings'], 1):
        print("{}. {} ({})".format(i, finding['title'], finding['source']))
        print("   " + finding['url'])
        print()

def run_demo():
    """Run the complete demo"""

    print("\n" + "="*80)
    print("TABSLAYER DEMO - LIVE RESEARCH AGGREGATION")
    print("="*80)

    query = "artificial intelligence"

    # DEMO 1
    print("\n[DEMO 1] Fresh Query")
    print("-" * 80)
    print("Researching: '{}'\n".format(query))

    cached = load_cache(query)
    if not cached:
        print(">>> Researching sources...\n")
        start = time.time()

        print(">>> Fetching Wikipedia...")
        wiki_results = fetch_wikipedia_simple(query)

        print(">>> Fetching arXiv papers...")
        arxiv_results = fetch_arxiv_simple(query)

        all_results = wiki_results + arxiv_results
        results1 = aggregate_results(all_results, query)

        elapsed1 = time.time() - start

        save_cache(query, results1)
    else:
        print(">>> Loaded from cache!\n")
        results1 = cached
        elapsed1 = 0.001

    display_results(results1)
    print("[TIME] Completed in: {:.2f} seconds".format(elapsed1))

    # DEMO 2
    print("\n" + "="*80)
    print("[DEMO 2] Same Query Again (Watch the caching magic!)")
    print("-" * 80)
    print("Researching: '{}' (repeat)\n".format(query))

    start = time.time()
    cached = load_cache(query)
    elapsed2 = time.time() - start

    if cached:
        print(">>> Loaded from cache INSTANTLY!\n")
        results2 = cached

    display_results(results2)
    print("[TIME] Completed in: {:.2f} seconds".format(elapsed2))

    if elapsed1 > 0:
        speedup = elapsed1 / max(elapsed2, 0.001)
        print("[SPEED] Speed improvement: {:.0f}x faster on cached queries".format(speedup))

    print("\n" + "="*80)
    print("DEMO COMPLETE - Press ENTER to close")
    print("="*80)

if __name__ == "__main__":
    try:
        run_demo()
        try:
            input()
        except:
            pass
    except Exception as e:
        print("\n[ERROR] {}".format(e))
        import traceback
        traceback.print_exc()
        try:
            input("Press ENTER to close...")
        except:
            pass
