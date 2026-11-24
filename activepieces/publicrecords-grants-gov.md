# Activepieces HTTP recipe — open US federal grants

Create an HTTP piece (or "Send HTTP request" step) in Activepieces:

- Method: `POST`
- URL: `https://api.apify.com/v2/acts/publicrecords~grants-gov-scraper/run-sync-get-dataset-items?token={{APIFY_TOKEN}}`
- Headers: `Content-Type: application/json`
- Body:

```json
{ "status": "posted", "maxItems": 50 }
```

Store `APIFY_TOKEN` as a secret in Activepieces. The Actor runs on your Apify account.

Store page: https://apify.com/publicrecords/grants-gov-scraper

Disclosure: Public Records maintains this Actor (pay-per-use on Apify; free tier available).
