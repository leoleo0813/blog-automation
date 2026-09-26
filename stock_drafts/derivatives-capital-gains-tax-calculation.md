---
keyword: 파생상품 양도소득세
title: 파생상품 양도소득세 계산 방법
slug: derivatives-capital-gains-tax-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 120 (PC 40 / 모바일 80)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-26 — 통과]
  WebSearch "파생상품 양도소득세" 상위 9개: kci.go.kr(학술논문 포털, 준정부
  성격) ×2 / myasset.com(유안타증권 공식 신고안내) / miraeasset PDF(공식
  신고도움자료) / kiwoom FAQ(공식) / kdajdqs.org(전문 세미나 자료) /
  nts.go.kr(국세청 공식, WebFetch는 막히나 검색 색인엔 존재) / wikipedia
  영문판(무관) + 보조 검색에서 taxtimes.co.kr(한국세정신문, 세무전문언론) /
  tseasy.moonglow1004.com(개인 티스토리) / syeum.com(개인·소규모 콘텐츠) /
  mofe.go.kr(정부 시사경제용어사전) / kcie.or.kr(한국경제교육협회 절세가이드).
  1) 진입 여지 — 있음. tseasy.moonglow1004.com·syeum.com 등 개인·소규모
     콘텐츠가 상위권에 존재한다.
  2) 검색 의도 — 세율·과세대상·계산법을 함께 묻는 개념+계산 탐색형이다.
     시세 조회나 계산기 실행이 지배적 의도는 아니다.
  3) 답 완결 여부 — 아니다. 상위 결과 대부분이 학술논문이거나 특정 연도
     귀속분 신고 공지(예: "2024년 귀속 신고 안내")여서 매년 갱신되는
     실무 정보를 개념부터 계산까지 한 번에 정리한 글이 없다. 이 프로젝트가
     직접 조사하는 과정에서도 "기본세율 22%"와 "탄력세율 11%", "CFD 세율"을
     혼동한 자료가 섞여 나올 정도로 정리가 안 돼 있다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 국내 코스피200선물 700만원 이익 + 해외선물 200만원 손실 + CFD 100만원
      이익을 실제로 통산해 기본공제 250만원을 뺀 뒤 세액까지 원 단위로
      계산하는 워크스루. 상위 검색 결과 중 국내·해외·CFD 세 종류를 한 번에
      섞어 계산한 예시는 찾지 못했다.
  (b) 과세대상 확대 연혁표(2016년 코스피200선물·옵션 도입 → 2019년
      코스닥150선물·KRX300선물 등 확대 → 2021년 CFD 추가) — 상위 글
      대부분은 현재 시점 과세대상만 나열하고 확대 연혁은 다루지 않는다.
  (c) "기본세율 20%(지방세 포함 22%)"와 "실제 적용되는 탄력세율 11%"를
      혼동하는 자료가 실제로 검색되는데(조사 중 CFD에 22%를 적용한다는
      자료 1건 발견), 국내·해외·CFD 모두 동일하게 탄력세율 11%가 적용된다는
      점을 브로커 공식 규정 안내로 재확인해 명확히 정리했다. 이 혼동 자체가
      상위 글이 풀지 못한 정보이득 지점이다.
primary_source: |
  nts.go.kr(국세청 "알기 쉬운 양도소득세" 파생상품 편)에 WebFetch를 1회
  시도했으나 EGRESS_BLOCKED. 대조군으로 kofia.or.kr도 함께 시도했으나
  동일하게 차단되어 이번 세션은 WebFetch가 전면 차단된 상태로 판단했다
  (RULES.md 「1차 출처가 막혔을 때」 기준 적용).
  WebSearch로 독립 출처 8곳 이상을 교차확인했다: 세무전문언론 1곳
  (한국세정신문 taxtimes.co.kr), 정부 도메인 1곳(mofe.go.kr 시사경제용어
  사전), 증권사 공식 신고안내·FAQ 다수(유진투자증권 CFD 양도소득세 과세
  시행 안내 — 소득세법 시행령 159의2·161의2 근거 조문까지 명시, 삼성증권
  국내외 파생상품 양도세 신고 안내, 미래에셋증권 신고도움자료, 키움증권
  FAQ), 전문 세미나·교육기관 자료(kdajdqs.org, 한국경제교육협회 절세가이드).
  핵심 수치(기본세율 20%, 지방소득세 포함 22% → 소득세법 시행령상 탄력세율
  적용 후 10%+1%=11%, 국내외 파생상품 손익 통산 후 기본공제 연 250만원,
  CFD는 2021-04-01부터 과세대상 포함)는 대부분 일치했다.
source_conflict: |
  검증 과정에서 "해외 CFD는 22% 세율이 적용된다"고 서술한 자료 1건을
  발견했다(다른 자료들은 전부 CFD도 11%로 서술). 유진투자증권의 CFD 양도
  소득세 과세 시행 공식 안내(소득세법 시행령 159의2①2, 161의2④ 근거 조문
  명시)에서 CFD 세율을 지방소득세 포함 11%로 명확히 확인해 상충을
  해소했다. 22%는 탄력세율 적용 전의 "기본세율" 수치를 실제 적용세율로
  잘못 인용한 자료로 판단된다. 국세청 원문(nts.go.kr)은 이번 세션에서
  끝내 직접 확인하지 못했으므로, 발행 전 사람이 국세청 "알기 쉬운
  양도소득세 - 파생상품" 페이지에서 세율 11%(국내·해외·CFD 공통) 여부를
  한 번 더 확인하는 것을 권장한다.
기준일: 2026년 9월 기준 (탄력세율은 2016년 파생상품 양도소득세 도입 이후 계속 적용 중인 시행령 규정)
tags: 파생상품양도소득세, 선물옵션세금, CFD양도소득세, 파생상품세율, 코스피200선물옵션, 양도소득세계산, 탄력세율, 손익통산, 주식초보, 세금정보
gate_pass: false
gate_pass_note: |
  게이트1·2·3은 충족(위 참조). 게이트4는 국세청 원문 직접 접속이
  EGRESS_BLOCKED로 끝내 불발돼 WebSearch 교차검증으로 진행했고, 검증
  과정에서 CFD 세율 관련 상충 자료 1건을 발견해 브로커 공식 규정안내로
  해소했다(source_conflict 참조). RULES.md 「수치는 소관 부처 원문에서」
  절이 "출처 간 숫자가 다르면 소관 부처 원문으로 확정 전까지 gate_pass:false"
  로 못박고 있어, 이번 상충은 해소했다고 판단하지만 국세청 원문을 직접
  못 봤다는 한계 때문에 안전하게 gate_pass:false로 저장한다. 사람이
  nts.go.kr에서 11% 단일세율(국내·해외·CFD 공통)을 원문으로 재확인하면
  gate_pass:true로 바꿔도 된다.
capture_guide: |
  (1) 왜 필요한가: 파생상품 양도소득세율이 국내·해외·CFD 전부 동일하게
      11%(지방소득세 포함)인지를 국세청 원문에서 최종 확인하고 싶다.
      WebSearch 교차검증으로 8곳 이상에서 11%로 수렴했지만, 그중 1곳이
      "해외 CFD 22%"라고 써서 혼선이 있었고(브로커 공식 안내로 해소는
      했음), 이 프로젝트가 과거 세율 수치에서 실제 오류를 잡아낸 적이
      있어(대주주 기준 5배 차이 사례) 세율은 원문으로 한 번 더 보는 편이
      안전하다.
  (2) 시도할 사이트 (우선순위):
      1순위 — 국세청 "알기 쉬운 양도소득세" 파생상품 편:
      https://www.nts.go.kr/tax/sub/1.5.4.%ED%8C%8C%EC%83%9D%EC%83%81%ED%92%88%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%96%91%EB%8F%84%EC%86%8C%EB%93%9D%EC%84%B8%20%EC%8B%A0%EA%B3%A0%EB%82%A9%EB%B6%80%20%EC%95%88%EB%82%B4.html
      접속 → 페이지 안에서 "세율" 또는 "탄력세율" 항목을 찾아 국내파생상품·
      해외파생상품·CFD 각각에 적용되는 세율(%)이 표시된 부분을 캡처.
      2순위 — 홈택스(www.hometax.go.kr) 접속 → 세금종류별 서비스 →
      양도소득세 → 파생상품 양도소득세 안내 메뉴에서 같은 내용 확인.
      3순위 — 국세법령정보시스템(taxlaw.nts.go.kr)에서 "소득세법 시행령
      제159조의2" 검색 → 탄력세율 조문 원문 캡처.
  (3) 캡처 후: 스크린샷을 대화에 올려주세요. 세율이 11%(국내·해외·CFD
      공통)로 확인되면 이 초안의 gate_pass를 true로 바꾸고, 만약 CFD나
      해외파생상품에 다른 세율이 확인되면 본문 표와 계산 예시를 그
      수치로 고쳐야 한다.
self_check: |
  [2026-09-26 판정 — gate_pass:false, 세율 원문 재확인 대기]
  게이트1 충족 — check-keywords.yml 실측 120회(PC 40/모바일 80, 세부·제도
  기준 100 이상). 같은 배치 7개 중 유일한 PASS(나머지 6개: RSI 계산법
  20회, 스토캐스틱 계산법 20회, ROE ROA 계산법 20회, 일목균형표 뜻 20회,
  국채선물 뜻 20회, 선물 증거금 뜻 20회 — 전부 임계값 미달로 FAIL,
  backlog.failed_gate1에 기록).
  게이트2 충족 — RULES.md v3 기준 3개 탈락 조건 모두 미해당(serp_check
  참조).
  게이트3 충족 — 국내+해외+CFD 손익통산 계산 워크스루, 과세대상 확대
  연혁표, 기본세율·탄력세율 혼동 정리로 상위 글보다 구체적인 정보이득을
  확보했다.
  게이트4 미충족 — nts.go.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군
  kofia.or.kr도 차단되어 세션 전면 차단으로 판단하고 WebSearch 교차검증
  8곳 이상으로 대체했다. 다만 검증 중 CFD 세율에 상충 자료(11% vs 22%)를
  발견했고, 브로커 공식 규정안내로 해소는 했으나 국세청 원문을 직접
  확인하지 못해 RULES.md 「수치는 소관 부처 원문에서」 기준에 따라
  gate_pass:false로 안전하게 저장한다(capture_guide 참조, 사람 확인 후
  true로 전환 가능).
  카니벌라이제이션 점검 — stock_drafts/*.md 85개 전체 grep 결과 "파생상품
  양도소득세"를 다룬 기존 편 없음. 37편(채권 세금)·52편(ETN 뜻)·73편
  (커버드콜 ETF 세금)은 각각 다른 상품군을 다뤄 겹치지 않는다. id85
  자체점검 기록에 "선물옵션 양도소득세 20회"가 별도 실패 후보로 언급된
  적 있으나 이는 이번 편의 키워드("파생상품 양도소득세", 120회)와
  검색량 측정치가 다른 별개 후보였다.
  YMYL·투자조언 안전장치 점검 — 특정 종목·상품을 추천하지 않았고, 매매
  타이밍이 아니라 세금 계산 절차만 다뤘다. 계산 예시는 전부 "가상의
  거래" 금액으로만 구성했다.
  제목 "파생상품 양도소득세 계산 방법" 15자·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 4단어(derivatives-capital-gains-tax-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—"
  0개 확인(검색 완료). "다만" 0회, 전환은 "그런데"·"단,"·"반대로"로
  분산. `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심
  요약 박스 제목을 "🧮 핵심만 계산해보면"으로, 색은 브라운/카라멜 계열
  (#f7f0e8/#8d6e63)로 최근 게시물(마젠타#c2185b·틸#00796b·앰버#d9812c·
  그린#2e7d32·슬레이트블루#3949ab·버건디#a4243b·퍼플#7b3fa0·
  스카이블루#0277bd)과 겹치지 않게 골랐다. 목차 제외 본문 H2 5개 중
  질문형 2개("어떤 파생상품에 과세되나요"·"세율은 얼마인가요"), 서술형
  3개로 "~나요" 편중 없음(5개 중 2개, 40%). FAQ 헤딩도 "자주 묻는 질문"
  대신 "헷갈리는 부분 정리"로 변형. 헤지 표현은 남발 없이 확정된 사실은
  단정문으로 썼다. 면책 문구는 기존 게시물과 다른 표현으로 작성.
  기관 링크 점검 — 국세청 링크 1회(본문 안내 문장), 홈택스 링크 1회,
  하단 참고 출처 목록 항목도 전부 링크 처리.
  종합 판정: 게이트1~3 충족, 게이트4는 원문 미확인으로 gate_pass:false.
  발행 대기(사람이 세율 원문 확인 후 전환 가능).
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-26</p>

<p>파생상품 양도소득세는 국내외 선물·옵션과 CFD(차액결제거래)에서 번 돈에 매기는 세금입니다. <mark>국내·해외·CFD 손익을 전부 합산한 뒤 연 250만원을 공제</mark>하고 남은 금액에 세율을 곱해 계산합니다. 이 글은 과세대상과 세율, 실제 숫자로 세금을 계산하는 방법까지 순서대로 정리합니다.</p>

<div style="background:#f7f0e8;border:2px solid #8d6e63;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4e342e;font-size:18px;">🧮 핵심만 계산해보면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>국내 파생상품, 해외 파생상품, CFD 손익을 전부 통산한 뒤 연 250만원을 공제합니다.</li>
    <li>기본세율은 20%(지방소득세 포함 22%)지만, 현재는 탄력세율이 적용돼 실제로는 11%를 냅니다.</li>
    <li>이 11%는 국내·해외·CFD 구분 없이 동일하게 적용됩니다.</li>
    <li>매년 5월에 국세청에 확정신고·납부합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>파생상품 양도소득세란</li>
  <li>어떤 파생상품에 과세되나요</li>
  <li>세율은 얼마인가요</li>
  <li>실제 숫자로 계산해보기</li>
  <li>신고납부 방법과 기한</li>
  <li>헷갈리는 부분 정리</li>
</ol>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">파생상품 양도소득세란</h2>

<p>파생상품 양도소득세는 선물·옵션 같은 파생상품을 사고팔아 얻은 이익에 매기는 세금입니다. 2016년 소득세법 개정으로 처음 도입됐고, 코스피200선물·옵션(미니 포함)부터 과세를 시작했습니다.</p>

<p>주식 양도소득세와 마찬가지로 매도할 때마다 세금을 떼는 방식이 아니라, 1년 동안의 손익을 모아 다음 해에 한 번 신고·납부하는 구조입니다.</p>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">어떤 파생상품에 과세되나요</h2>

<p>과세대상은 도입 이후 여러 차례 넓어졌습니다. 처음에는 코스피200선물·옵션만 대상이었지만, 지금은 훨씬 넓은 범위를 포함합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시점</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">추가된 과세대상</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2016년 도입</td>
      <td style="border:1px solid #ddd;padding:8px;">코스피200선물, 코스피200옵션(미니 포함)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2019년 4월 1일 양도분부터</td>
      <td style="border:1px solid #ddd;padding:8px;">코스닥150선물·옵션, KRX300선물, 유로스톡스50선물, 변동성지수선물, 배당지수선물, 섹터지수선물 등</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2021년 4월 1일부터</td>
      <td style="border:1px solid #ddd;padding:8px;">CFD(차액결제거래), 유가증권시장·코스닥시장 종목 전체</td>
    </tr>
  </tbody>
</table>

<p>여기에 해외선물·해외옵션도 처음부터 과세대상에 포함돼 있습니다. 즉 지금은 국내 장내파생상품, 해외 파생상품, CFD 세 갈래 모두 과세대상이라고 보면 됩니다.</p>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">세율은 얼마인가요</h2>

<p>법에 정해진 기본세율은 20%(지방소득세 2%를 더하면 22%)입니다. <mark>하지만 소득세법 시행령의 탄력세율 규정에 따라 실제로는 이보다 낮은 세율을 적용받습니다.</mark></p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">세율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기본세율(법정, 지방세 포함)</td>
      <td style="border:1px solid #ddd;padding:8px;">22%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">현재 적용 탄력세율(양도세 10%+지방세 1%)</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>11%</mark></td>
    </tr>
  </tbody>
</table>

<p>이 11%는 국내 파생상품, 해외 파생상품, CFD 구분 없이 동일하게 적용됩니다. 자료를 찾다 보면 CFD에 다른 세율을 적용한다고 쓴 글도 보이는데, 이는 탄력세율 적용 전 기본세율을 실제 세율로 착각한 경우로 보입니다. 발행 전 국세청 원문으로 한 번 더 확인할 예정이니, 정확한 최신 수치는 아래 참고 출처의 국세청 링크에서 직접 확인하시기 바랍니다.</p>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">실제 숫자로 계산해보기</h2>

<p>가상의 사례로 계산 순서를 짚어보겠습니다. 1년 동안 국내 코스피200선물에서 700만원 이익, 해외선물에서 200만원 손실, CFD에서 100만원 이익이 났다고 가정합니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <ol style="margin:8px 0 0 0;padding-left:20px;">
    <li>손익 통산: 700만원 − 200만원 + 100만원 = <mark>600만원</mark></li>
    <li>기본공제 적용: 600만원 − 250만원 = 과세표준 350만원</li>
    <li>세액 계산: 350만원 × 11% = <b>385,000원</b></li>
  </ol>
</div>

<p>여기서 중요한 점은 국내·해외·CFD를 따로따로 계산하지 않고 하나로 합쳐서 계산한다는 것입니다. 만약 해외선물에서 손실이 나지 않았다면 통산 손익은 800만원이 되어 세금도 그만큼 늘어납니다. 반대로 손실이 컸다면 통산 후 금액이 250만원 아래로 내려가 세금이 아예 없을 수도 있습니다.</p>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">신고납부 방법과 기한</h2>

<p>파생상품 양도소득세는 1년(1월 1일~12월 31일) 동안 발생한 손익을 다음 해 5월에 확정신고·납부합니다. <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> 또는 손택스(모바일 앱)에서 전자신고할 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>신고 기간: 다음 해 5월 1일부터 5월 31일까지(말일이 공휴일이면 다음 영업일까지)</li>
  <li>신고 대상: 국내외 파생상품, CFD에서 통산 이익이 발생해 세금이 나오는 투자자</li>
  <li>기한을 넘기면 무신고·과소신고 가산세와 납부지연 가산세가 추가로 붙습니다.</li>
</ul>

<h2 style="border-left:6px solid #8d6e63;padding-left:12px;margin-top:36px;">헷갈리는 부분 정리</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">모든 선물옵션 거래에 다 세금이 붙나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 코스피200선물·옵션 등 지정된 국내 파생상품과 해외선물·해외옵션, CFD가 과세대상입니다. 과세대상은 2016년 도입 이후 여러 차례 넓어져 왔습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내와 해외 파생상품 세금을 따로 계산하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 국내 파생상품, 해외 파생상품, CFD의 손익을 전부 합쳐서(통산) 계산한 뒤 기본공제를 적용합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">기본공제 250만원은 상품마다 따로 받나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 국내·해외 파생상품과 CFD를 전부 합산한 손익에서 연 1회, 250만원만 공제됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">CFD는 세율이 더 높나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. CFD도 국내·해외 파생상품과 동일하게 탄력세율 11%가 적용됩니다. 다른 세율을 언급한 자료가 있다면 탄력세율 적용 전 기본세율(22%)과 혼동했을 가능성이 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신고를 안 하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">기한(5월 31일)까지 신고·납부하지 않으면 무신고 또는 과소신고 가산세, 그리고 납부지연 가산세가 추가로 부과됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/tax/sub/1.5.4.%ED%8C%8C%EC%83%9D%EC%83%81%ED%92%88%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%96%91%EB%8F%84%EC%86%8C%EB%93%9D%EC%84%B8%20%EC%8B%A0%EA%B3%A0%EB%82%A9%EB%B6%80%20%EC%95%88%EB%82%B4.html" target="_blank" rel="noopener">국세청 - 알기 쉬운 양도소득세(파생상품에 대한 양도소득세 신고납부 안내)</a></li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a></li>
    <li>세율·과세대상 확대 연혁은 세무전문언론(한국세정신문)과 증권사 공식 신고안내·규정 자료를 교차확인해 정리했습니다. 자세한 기록은 저장소 sources/ 참고.</li>
  </ul>
  <p style="margin:8px 0 0 0;">기준일: 2026년 9월 기준.</p>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 세금 계산 절차를 설명하는 정보 글이며, 특정 종목이나 상품의 매수·매도를 권하지 않습니다. 세율과 공제 한도는 법령 개정에 따라 달라질 수 있으므로, 실제 신고 전에는 국세청 원문이나 세무 전문가를 통해 다시 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "파생상품 양도소득세 계산 방법",
  "description": "파생상품 양도소득세의 과세대상 확대 연혁, 세율(탄력세율 11%), 국내·해외·CFD 손익통산 계산 예시, 신고납부 기한을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-26",
  "dateModified": "2026-09-26",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/derivatives-capital-gains-tax-calculation"
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "모든 선물옵션 거래에 다 세금이 붙나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 코스피200선물·옵션 등 지정된 국내 파생상품과 해외선물·해외옵션, CFD가 과세대상입니다. 과세대상은 2016년 도입 이후 여러 차례 넓어져 왔습니다." }
    },
    {
      "@type": "Question",
      "name": "국내와 해외 파생상품 세금을 따로 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 국내 파생상품, 해외 파생상품, CFD의 손익을 전부 합쳐서(통산) 계산한 뒤 기본공제를 적용합니다." }
    },
    {
      "@type": "Question",
      "name": "기본공제 250만원은 상품마다 따로 받나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 국내·해외 파생상품과 CFD를 전부 합산한 손익에서 연 1회, 250만원만 공제됩니다." }
    },
    {
      "@type": "Question",
      "name": "CFD는 세율이 더 높나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. CFD도 국내·해외 파생상품과 동일하게 탄력세율 11%가 적용됩니다. 다른 세율을 언급한 자료가 있다면 탄력세율 적용 전 기본세율(22%)과 혼동했을 가능성이 있습니다." }
    },
    {
      "@type": "Question",
      "name": "신고를 안 하면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "기한(5월 31일)까지 신고·납부하지 않으면 무신고 또는 과소신고 가산세, 그리고 납부지연 가산세가 추가로 부과됩니다." }
    }
  ]
}
</script>
