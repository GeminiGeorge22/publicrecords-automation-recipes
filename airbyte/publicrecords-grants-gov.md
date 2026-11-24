# Airbyte custom HTTP source — open US federal grants

Airbyte does not ship a native Grants.gov source. You can add a **custom HTTP** (or CDK low-code) source that calls Apify on your account:

- Method: `POST`
- URL: `https://api.apify.com/v2/acts/publicrecords~grants-gov-scraper/run-sync-get-dataset-items`
- Query: `token={{ secrets.APIFY_TOKEN }}`
- Body: `{ "status": "posted", "maxItems": 200 }`
- Incremental sync is not required for a full open-opportunity snapshot; schedule a daily refresh.

Store page: https://apify.com/publicrecords/grants-gov-scraper

Disclosure: Public Records maintains this Actor (pay-per-use on Apify; free tier available). This is a recipe, not an official Airbyte connector.
