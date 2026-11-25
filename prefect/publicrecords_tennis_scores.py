"""Prefect flow: pull ATP/WTA tennis scores via the user's Apify token.

Disclosure: Public Records maintains the tennis-scores-api Actor (pay-per-use on Apify).
Standby/MCP mode is not built; this flow calls the Apify API only.
"""
import os
import json
import urllib.request
from prefect import flow, task

ACTOR = "publicrecords~tennis-scores-api"

@task
def run_actor(max_results: int = 20):
    token = os.environ["APIFY_TOKEN"]
    url = f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items?token={token}"
    payload = {"tournament": "wimbledon", "date": "2026-07-12", "maxResults": max_results}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.load(resp)

@flow(name="publicrecords-tennis-scores")
def tennis_scores_flow(max_results: int = 20):
    items = run_actor(max_results)
    print(f"fetched {len(items) if isinstance(items, list) else 'n/a'} tennis rows")
    return items

if __name__ == "__main__":
    tennis_scores_flow()
