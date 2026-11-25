// Pipedream component: run publicrecords/tennis-scores-api with YOUR Apify token.
// Disclosure: Public Records maintains this Actor (pay-per-use on Apify).
// Standby/MCP mode is not built; this component calls the Apify API only.
export default {
  name: "Public Records — Tennis Scores API",
  key: "publicrecords-tennis-scores-api",
  version: "0.0.1",
  type: "action",
  props: {
    apifyToken: { type: "string", label: "Apify API token", secret: true },
    maxResults: { type: "integer", label: "Max rows", default: 20 },
  },
  async run({ $ }) {
    const url = `https://api.apify.com/v2/acts/publicrecords~tennis-scores-api/run-sync-get-dataset-items?token=${this.apifyToken}`;
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ tournament: "wimbledon", date: "2026-07-12", maxResults: this.maxResults }),
    });
    if (!res.ok) throw new Error(await res.text());
    const items = await res.json();
    $.export("$summary", `Fetched ${Array.isArray(items) ? items.length : 0} tennis rows`);
    return items;
  },
};
