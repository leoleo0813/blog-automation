# 1차 출처 접근 시도 기록: financial-income-comprehensive-tax

수집 시각: 2026-09-06 (Routine 자동 실행)

## 시도한 도메인과 결과

| 도메인 | 시도 방법 | 결과 |
|---|---|---|
| www.nts.go.kr (국세청) | WebFetch | EGRESS_BLOCKED |
| www.easylaw.go.kr (찾기쉬운 생활법령정보) | WebFetch | EGRESS_BLOCKED |
| www.kofia.or.kr (금융투자협회, 접근성 대조군) | WebFetch | EGRESS_BLOCKED |
| www.google.com (일반 접근성 대조군) | WebFetch | EGRESS_BLOCKED |

**주의:** 구글 대조군까지 막힌 것으로 보아 이번 세션도 dividend-income-tax(2026-09-04) /
isa-limit-benefit(2026-09-04) / overseas-stock-tax-filing(2026-09-05) 초안이 남긴 증상과
동일하게, 도메인별 차단이 아니라 세션의 WebFetch 자체가 전면 차단된 상태로 판단된다. 이제 네
번째 연속 세션에서 같은 증상이 재현됐다. RULES.md "1차 출처 접근" 표의 nts.go.kr/easylaw.go.kr
"열림" 기록을 자동화가 신뢰하고 반복 시도하는 것은 더 이상 효율적이지 않다고 보고, 이번 실행에서
RULES.md 표에 "자동화 WebFetch는 4회 연속 세션 전면 차단 재현, 사람이 직접 열어야 확실함" 메모를
추가했다(별도 커밋 diff 참고).

## WebSearch로 확인한 사실확인 단서 (본문 출처로 인용하지 않음)

- 다수 공식·전문 출처(standardchartered.co.kr, call.nts.go.kr 국세청 상담센터 Q&A, pwc.com 삼일회계법인,
  skhybank.com 새마을금고, namu.wiki)가 공통적으로 "이자+배당 합산 연 2,000만원 초과 시 종합과세,
  2,000만원 이하는 원천징수(14%+지방소득세 1.4%)로 분리과세 종결, 초과분만 다른 종합소득과 합산해
  누진세율 적용, 배우자 금융소득은 합산 안 됨"을 언급.
- 다만 "비교과세"(원천징수보다 세부담이 줄지 않도록 하는 산출세액 비교 장치, 소득세법 제62조)의
  정확한 계산 공식과 현재 유효한 종합소득세 누진세율표(과세표준 구간·세율·누진공제액)는 1차 출처
  원문으로 확인하지 못했다. 이 부분이 이 글의 핵심 정보이득(계산 예시)에 해당하므로, 여러 비공식
  출처가 일치한다는 사실만으로 본문 확정 수치로 쓰지 않았다.
- 결론: keyword_class를 human-assisted로, publish_effort를 capture로 재분류. 사람이
  call.nts.go.kr(국세청 상담센터 Q&A) 또는 easylaw.go.kr 원문에서 비교과세 계산 방법과 종합소득세
  세율표, 페이지 기준일을 캡처해야 게이트3·4가 완성되고 발행 가능.
- 추가로 이 키워드는 WebSearch 상위 8개 결과 중 공식·언론·백과성 콘텐츠가 5개(standardchartered,
  국세청, pwc, namu.wiki, skhybank)로 RULES.md 게이트2 탈락 기준(5개 이상)에 해당해, 캡처와 별개로
  키워드 재선정 여부도 사람이 함께 판단해야 한다.
