# Activepieces HTTP recipe — ATP & WTA tennis scores

Create an HTTP piece (or "Send HTTP request" step) in Activepieces:

- Method: `POST`
- URL: `https://api.apify.com/v2/acts/publicrecords~tennis-scores-api/run-sync-get-dataset-items?token={{APIFY_TOKEN}}`
- Headers: `Content-Type: application/json`
- Body:

```json
{ "tournament": "wimbledon", "date": "2026-07-12", "maxResults": 20 }
```

Store `APIFY_TOKEN` as a secret in Activepieces. The Actor runs on your Apify account. Standby/MCP mode is not built; this recipe calls the Apify API only.

Store page: https://apify.com/publicrecords/tennis-scores-api

Disclosure: Public Records maintains this Actor (pay-per-use on Apify; free tier available). Author: Public Records.
