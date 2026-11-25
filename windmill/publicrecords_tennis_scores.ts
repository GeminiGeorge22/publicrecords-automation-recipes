// Windmill script: run publicrecords/tennis-scores-api with YOUR Apify token.
// Disclosure: Public Records maintains this Actor (pay-per-use on Apify).
// Standby/MCP mode is not built; this script calls the Apify API only.
export async function main(apify_token: string, max_results: number = 20) {
  const url = `https://api.apify.com/v2/acts/publicrecords~tennis-scores-api/run-sync-get-dataset-items?token=${apify_token}`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tournament: "wimbledon", date: "2026-07-12", maxResults: max_results }),
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}
