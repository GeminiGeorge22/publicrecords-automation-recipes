**READMEs:** [English](README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [한국어](README.ko.md)

# Public Records — 自動化レシピ

[Public Records](https://apify.com/publicrecords) の Apify Actor を**あなた自身の Apify アカウント**で呼び出す実行例です。`APIFY_TOKEN`（または各プラットフォームのシークレット）に自分のトークンを設定してください。リポジトリにコミットしないでください。

17件の n8n ワークフローと Make / Zapier / Pipedream / Activepieces / Clay の HTTP レシピは [`publicrecords-mcp/templates`](https://github.com/GeminiGeorge22/publicrecords-mcp/tree/main/templates) にもあります。

| プラットフォーム | パス |
|---|---|
| Kestra | [`kestra/`](kestra/) |
| Prefect | [`prefect/publicrecords_grants_gov.py`](prefect/publicrecords_grants_gov.py) |
| Dagster | [`dagster/publicrecords_assets.py`](dagster/publicrecords_assets.py) |
| Pipedream | [`pipedream/publicrecords-grants-gov.mjs`](pipedream/publicrecords-grants-gov.mjs) |
| Windmill | [`windmill/publicrecords_grants_gov.ts`](windmill/publicrecords_grants_gov.ts) |
| Node-RED | [`nodered/publicrecords-grants-gov.json`](nodered/publicrecords-grants-gov.json) |
| Activepieces | [`activepieces/publicrecords-grants-gov.md`](activepieces/publicrecords-grants-gov.md) |
| Airbyte (recipe) | [`airbyte/publicrecords-grants-gov.md`](airbyte/publicrecords-grants-gov.md) |

Actor ごとのコード例（Python、JavaScript、curl）と各国語 README は、[GeminiGeorge22](https://github.com/GeminiGeorge22) の `publicrecords-*-examples` リポジトリにあります。

公開スナップショットデータセット: [Hugging Face @Publicrecords](https://huggingface.co/Publicrecords)。

開示: これらの Actor は Public Records が維持し、Apify の従量課金（無料枠あり）で実行します。作者: Public Records。ライセンス: MIT。このリポジトリに GitHub Actions はありません。

`publicrecords/tennis-scores-api` のレシピもあります（Apify API、利用者自身のトークン。MCP エンドポイントはありません）。サンプルリポジトリの一覧は [README.md](README.md) にあります。
