"""Dagster asset: pull open US federal grants via the user's Apify token.

Disclosure: Public Records maintains the grants-gov-scraper Actor (pay-per-use on Apify).
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
