"""Dagster asset: pull open US federal grants via the user's Apify token.

Disclosure: Public Records maintains the grants-gov-scraper and tennis-scores-api Actors (pay-per-use on Apify).
"""
import os, json, urllib.request
from dagster import asset

@asset
def open_federal_grants():
    token = os.environ["APIFY_TOKEN"]
    url = "https://api.apify.com/v2/acts/publicrecords~grants-gov-scraper/run-sync-get-dataset-items?token=" + token
    payload = {"status": "posted", "maxItems": 50}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.load(resp)


@asset
def tennis_scores():
    """ATP/WTA tennis scores via the user's Apify token. No MCP endpoint (Standby/MCP is not built)."""
    token = os.environ["APIFY_TOKEN"]
    url = "https://api.apify.com/v2/acts/publicrecords~tennis-scores-api/run-sync-get-dataset-items?token=" + token
    payload = {"tournament": "wimbledon", "date": "2026-07-12", "maxResults": 20}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.load(resp)
