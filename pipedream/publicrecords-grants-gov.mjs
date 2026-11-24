// Pipedream component: run publicrecords/grants-gov-scraper with YOUR Apify token.
// Disclosure: Public Records maintains this Actor (pay-per-use on Apify).
export default {
  name: "Public Records — Open Federal Grants",
  key: "publicrecords-grants-gov-scraper",
  version: "0.0.1",
  type: "action",
  props: {
    apifyToken: { type: "string", label: "Apify API token", secret: true },
    maxItems: { type: "integer", label: "Max items", default: 50 },
  },
  async run({ $ }) {
    const url = `https://api.apify.com/v2/acts/publicrecords~grants-gov-scraper/run-sync-get-dataset-items?token=${this.apifyToken}`;
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status: "posted", maxItems: this.maxItems }),
    });
    if (!res.ok) throw new Error(await res.text());
    const items = await res.json();
    $.export("$summary", `Fetched ${Array.isArray(items) ? items.length : 0} open grants`);
    return items;
  },
};
