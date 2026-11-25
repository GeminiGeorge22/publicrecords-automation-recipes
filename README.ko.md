**READMEs:** [English](README.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [한국어](README.ko.md)

# Public Records — 자동화 레시피

[Public Records](https://apify.com/publicrecords) Apify Actor를 **본인 Apify 계정**에서 호출하는 바로 실행 가능한 예제입니다. `APIFY_TOKEN`(또는 플랫폼 시크릿)에 본인 토큰을 설정하세요. 저장소에 커밋하지 마세요.

17개의 n8n 워크플로와 Make / Zapier / Pipedream / Activepieces / Clay HTTP 레시피는 [`publicrecords-mcp/templates`](https://github.com/GeminiGeorge22/publicrecords-mcp/tree/main/templates)에도 있습니다.

| 플랫폼 | 경로 |
|---|---|
| Kestra | [`kestra/`](kestra/) |
| Prefect | [`prefect/publicrecords_grants_gov.py`](prefect/publicrecords_grants_gov.py) |
| Dagster | [`dagster/publicrecords_assets.py`](dagster/publicrecords_assets.py) |
| Pipedream | [`pipedream/publicrecords-grants-gov.mjs`](pipedream/publicrecords-grants-gov.mjs) |
| Windmill | [`windmill/publicrecords_grants_gov.ts`](windmill/publicrecords_grants_gov.ts) |
| Node-RED | [`nodered/publicrecords-grants-gov.json`](nodered/publicrecords-grants-gov.json) |
| Activepieces | [`activepieces/publicrecords-grants-gov.md`](activepieces/publicrecords-grants-gov.md) |
| Airbyte (recipe) | [`airbyte/publicrecords-grants-gov.md`](airbyte/publicrecords-grants-gov.md) |

Actor별 코드 예제(Python, JavaScript, curl)와 번역된 README는 [GeminiGeorge22](https://github.com/GeminiGeorge22)의 `publicrecords-*-examples` 저장소에 있습니다.

공개 스냅샷 데이터셋: [Hugging Face @Publicrecords](https://huggingface.co/Publicrecords).

고지: 이 Actor는 Public Records가 유지하며, Apify에서 사용량 기준으로 청구됩니다(무료 요금제 있음). 작성자: Public Records. 라이선스: MIT. 이 저장소에는 GitHub Actions가 없습니다.

`publicrecords/tennis-scores-api` 레시피도 있습니다(Apify API, 사용자 본인 토큰; MCP 엔드포인트 없음). 예제 저장소 목록은 [README.md](README.md)에 있습니다.
