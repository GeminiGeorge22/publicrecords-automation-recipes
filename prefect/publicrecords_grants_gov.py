"""Prefect flow: pull open US federal grants via the user's Apify token.

Disclosure: Public Records maintains the grants-gov-scraper Actor (pay-per-use on Apify).
"""
import os
import json
import urllib.request
from prefect import flow, task

ACTOR = "publicrecords~grants-gov-scraper"

@task
def run_actor(max_items: int = 50):
    token = os.environ["APIFY_TOKEN"]
    url = f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items?token={token}"
    payload = {"status": "posted", "maxItems": max_items}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.load(resp)

@flow(name="publicrecords-grants-gov")
def grants_gov_flow(max_items: int = 50):
    items = run_actor(max_items)
    print(f"fetched {len(items) if isinstance(items, list) else 'n/a'} open grants")
    return items

if __name__ == "__main__":
    grants_gov_flow()
