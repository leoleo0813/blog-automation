# 1차 출처 접근 시도 기록: dividend-income-tax

수집 시각: 2026-09-04 (Routine 자동 실행, isa-limit-benefit과 같은 날 별도 실행)

## 시도한 도메인과 결과

| 도메인 | 시도 방법 | 결과 |
|---|---|---|
| www.easylaw.go.kr (찾기쉬운 생활법령정보 — 주식투자자 > 주식의 거래 > 양도소득세·증권거래세 및 배당소득세) | WebFetch | EGRESS_BLOCKED |
| www.nts.go.kr (국세청) | WebFetch | EGRESS_BLOCKED |
| www.kofia.or.kr (금융투자협회, 접근성 재확인용) | WebFetch | EGRESS_BLOCKED |
| www.google.com (일반 접근성 대조군) | WebFetch | EGRESS_BLOCKED |

**주의:** 구글 접근조차 막힌 것으로 보아 이번 세션은 WebFetch 자체가 전면 차단된 상태다(도메인별 차단이 아님). isa-limit-benefit 초안(같은 날 다른 실행)이 남긴 "세션별 프록시 허용 목록 차이로 추정"이라는 관찰이 다시 재현됐다 — 이제 두 번째 실행에서도 같은 증상이므로, RULES.md의 "1차 출처 접근" 표에서 kofia.or.kr / nts.go.kr / easylaw.go.kr을 "열림"으로 단정하는 것은 최소한 일부 세션에서는 신뢰할 수 없다. 표 자체는 사람 판단 없이 임의로 고치지 않았다.

## WebSearch로 확인한 사실확인 단서 (본문 출처로 인용하지 않음)

- 다수 비공식 출처(금융사 콘텐츠, 세금계산기 서비스, 개인 블로그)가 "배당소득세 원천징수세율 15.4%(소득세 14%+지방소득세 1.4%)", "이자·배당소득 합산 2천만원 초과 시 금융소득종합과세, 최고세율 45%(지방세 포함 49.5%)"라고 공통적으로 언급.
- 이 수치들은 여러 비공식 출처에서 서로 충돌 없이 일치하게 나타나긴 하지만, RULES.md 게이트4는 "1차 출처만 인정"이라고 명시하고 있고 이번 세션은 1차 출처 원문을 열람하지 못했다. 일치한다는 사실만으로 1차 출처 확인을 대체할 수 없다고 판단해 본문에 확정 수치로 쓰지 않았다.
- 결론: keyword_class를 human-assisted로, publish_effort를 capture로 재분류. 사람이 easylaw.go.kr 또는 nts.go.kr 원문 페이지를 직접 열어 세율·기준금액·종합과세 세율표와 페이지 기준일을 캡처해야 발행 가능.
