# Airbyte custom HTTP source — ATP & WTA tennis scores

Airbyte does not ship a native tennis-scores source. You can add a **custom HTTP** (or CDK low-code) source that calls Apify on your account:

- Method: `POST`
- URL: `https://api.apify.com/v2/acts/publicrecords~tennis-scores-api/run-sync-get-dataset-items`
- Query: `token={{ secrets.APIFY_TOKEN }}`
- Body: `{ "tournament": "wimbledon", "date": "2026-07-12", "maxResults": 20 }`
- Incremental sync is optional; schedule a daily refresh for a date or tournament you care about.

Standby/MCP mode is not built; this recipe calls the Apify API only.

Store page: https://apify.com/publicrecords/tennis-scores-api

Disclosure: Public Records maintains this Actor (pay-per-use on Apify; free tier available). This is a recipe, not an official Airbyte connector. Author: Public Records.
