// Windmill script: run publicrecords/grants-gov-scraper with YOUR Apify token.
// Disclosure: Public Records maintains this Actor (pay-per-use on Apify).
export async function main(apify_token: string, max_items: number = 50) {
  const url = `https://api.apify.com/v2/acts/publicrecords~grants-gov-scraper/run-sync-get-dataset-items?token=${apify_token}`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: "posted", maxItems: max_items }),
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}
