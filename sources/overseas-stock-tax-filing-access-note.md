# 1차 출처 접근 시도 기록: overseas-stock-tax-filing

수집 시각: 2026-09-05 (Routine 자동 실행)

## 시도한 도메인과 결과

| 도메인 | 시도 방법 | 결과 |
|---|---|---|
| www.hometax.go.kr (국세청 홈택스 — primary_source_plan) | WebFetch | EGRESS_BLOCKED |
| www.nts.go.kr (국세청) | WebFetch | EGRESS_BLOCKED |
| easylaw.go.kr (법제처 찾기쉬운 생활법령정보 — 주식투자자 > 주식거래에 따른 세금 납부하기) | WebFetch | EGRESS_BLOCKED |
| www.google.com (일반 접근성 대조군) | WebFetch | EGRESS_BLOCKED |

**주의:** 구글 대조군까지 막힌 것으로 보아 이번 세션도 dividend-income-tax(2026-09-04) / isa-limit-benefit(2026-09-04) 초안이 남긴 증상과 동일하게, 도메인별 차단이 아니라 이번 세션의 WebFetch 자체가 전면 차단된 상태로 판단된다. RULES.md "1차 출처 접근" 표는 nts.go.kr / easylaw.go.kr을 "열림"으로 적어두었지만, 세 번째로 같은 세션 전면 차단 증상이 재현된 것이므로 표를 임의로 고치지 않고 기록만 남긴다.

또한 이 주제(해외주식 양도소득세 신고 방법)의 primary_source_plan인 홈택스(hometax.go.kr)는 RULES.md에도 "로그인·공동인증 기반이라 화면 캡처 자체가 불가능할 가능성이 높음"으로 이미 미확인 표시되어 있었다 — 이번 EGRESS_BLOCKED와 무관하게, 실제 신고 화면 순서(엑셀 업로드 vs 합계액 직접 입력 등 UI 캡처)는 로그인 세션이 필요해 이 자동화 세션에서는 애초에 캡처가 불가능하다.

## WebSearch로 확인한 사실확인 단서 (본문 출처로 인용하지 않음)

- 다수 비공식 출처(증권사 세금안내 페이지, 은행 콘텐츠, 개인 블로그)가 다음을 공통적으로 언급: 해외주식 양도소득세 세율 20%(+지방소득세 2% = 총 22%), 기본공제 연 250만원(국내외 주식 양도차익 합산 1인당 1회), 신고기한 다음해 5월 1일~5월 31일 확정신고, 홈택스 로그인 후 "세금신고 > 양도소득세신고 > 확정신고" 경로.
- 이 수치들은 여러 비공식 출처에서 서로 충돌 없이 일치하지만, RULES.md 게이트4("1차 출처만 인정")를 이번 세션에서 원문으로 확인하지 못했으므로 확정 수치로 본문에 싣지 않았다.
- 결론: keyword_class를 human-assisted로, publish_effort를 capture로 재분류. 사람이 nts.go.kr(국세청) 또는 easylaw.go.kr 원문에서 세율·공제액·신고기한과 페이지 기준일을 확인하고, 홈택스 로그인 후 실제 신고 화면(양도소득세 확정신고 메뉴)을 캡처해야 발행 가능.
