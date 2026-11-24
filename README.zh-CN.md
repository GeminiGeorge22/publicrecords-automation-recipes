**READMEs:** [English](README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [한국어](README.ko.md)

# Public Records — 自动化配方

可直接运行的示例，用于在**您自己的 Apify 账户**上调用 [Public Records](https://apify.com/publicrecords) 的 Apify Actor。将 `APIFY_TOKEN`（或平台密钥）设为您自己的令牌。请勿将其提交到仓库。

另见 [`publicrecords-mcp/templates`](https://github.com/GeminiGeorge22/publicrecords-mcp/tree/main/templates) 中的 17 个 n8n 工作流以及 Make / Zapier / Pipedream / Activepieces / Clay 的 HTTP 配方。

| 平台 | 路径 |
|---|---|
| Kestra | [`kestra/`](kestra/) |
| Prefect | [`prefect/publicrecords_grants_gov.py`](prefect/publicrecords_grants_gov.py) |
| Dagster | [`dagster/publicrecords_assets.py`](dagster/publicrecords_assets.py) |
| Pipedream | [`pipedream/publicrecords-grants-gov.mjs`](pipedream/publicrecords-grants-gov.mjs) |
| Windmill | [`windmill/publicrecords_grants_gov.ts`](windmill/publicrecords_grants_gov.ts) |
| Node-RED | [`nodered/publicrecords-grants-gov.json`](nodered/publicrecords-grants-gov.json) |
| Activepieces | [`activepieces/publicrecords-grants-gov.md`](activepieces/publicrecords-grants-gov.md) |
| Airbyte (recipe) | [`airbyte/publicrecords-grants-gov.md`](airbyte/publicrecords-grants-gov.md) |

各 Actor 的代码示例（Python、JavaScript、curl）及本地化 README 位于 [GeminiGeorge22](https://github.com/GeminiGeorge22) 下的 `publicrecords-*-examples` 仓库。

公开快照数据集：[Hugging Face @Publicrecords](https://huggingface.co/Publicrecords)。

说明：这些 Actor 由 Public Records 维护，在 Apify 上按使用量计费（提供免费套餐）。作者：Public Records。许可证：MIT。本仓库未启用 GitHub Actions。

