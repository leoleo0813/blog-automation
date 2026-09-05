---
keyword: 해외주식 양도소득세
title: 해외주식 양도소득세 신고 방법
slug: overseas-stock-tax-filing
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 8750 (PC 1640 / 모바일 7110)
gate1_pass: true (일반 주제 기준 월 500 이상 필요 — 이미 확인된 값)
serp_check: WebSearch 확인(2026-09-05) — "해외주식 양도소득세" / "해외주식 양도소득세 신고 방법" 두 쿼리 상위 결과를 합쳐 보면 유안타증권(myasset.com), 신한투자증권(shinhansec.com), 한국투자증권(securities.koreainvestment.com 공지 및 file.koreainvestment.com PDF), 하나증권(hanaw.com), 토스뱅크(tossbank.com), KB(kbthink.com/kbcapital.co.kr) 등 증권사·은행 공식 안내 페이지가 최소 6~7개 확인됨. RULES.md 게이트2 기준("공식·언론·백과 5개 이상이면 재선정")을 넘어서는 것으로 판단 — 이 키워드는 경쟁 강도 기준에서 미달일 가능성이 높다. 다만 실제 구글 상위 10개를 직접 스크롤 확인한 것은 아니고 WebSearch 요약 기반 추정치이므로, 사람이 구글 검색으로 재확인 후 최종 판정 필요.
unique_asset_plan: 홈택스 신고 화면(로그인 후 세금신고>양도소득세신고>확정신고) 캡처 + 250만원 공제 적용 전후 계산 비교. 세율·공제액·신고기한 수치와 화면 캡처 모두 사람 확인 필요
primary_source: 미확보 — hometax.go.kr, nts.go.kr, easylaw.go.kr 전부 이번 세션에서 WebFetch가 EGRESS_BLOCKED로 실패. www.google.com 대조군도 동일하게 차단되어 이번 세션은 WebFetch 자체가 전면 차단된 상태로 판단(dividend-income-tax, isa-limit-benefit 초안과 동일 증상, 세 번째 재현). 게다가 hometax.go.kr은 로그인·공동인증 기반이라 접근이 가능해지더라도 실제 신고 화면은 사람이 직접 로그인해야만 캡처 가능. 상세 기록: sources/overseas-stock-tax-filing-access-note.md
기준일: 미확정 — 캡처 시 원문에 명시된 기준일을 그대로 기입할 것
tags: 해외주식양도소득세, 해외주식세금, 양도소득세신고, 홈택스신고방법, 해외주식세율, 250만원공제, 서학개미세금, 해외주식확정신고, 양도소득세계산
gate_pass: false
capture_guide: |
  왜 필요한가: 해외주식 양도소득세 세율(20%+지방소득세 2%)과 기본공제 250만원, 확정신고 기간(다음해
  5월)은 다수 증권사·은행 안내 페이지에서 공통적으로 언급되지만, RULES.md 게이트4(1차 출처만 인정)를
  이번 세션에서 원문으로 확인하지 못했습니다. 또한 홈택스 신고 화면 자체는 로그인이 필요해 이 자동화
  세션은 애초에 캡처할 수 없습니다. 아래 두 가지를 캡처해서 보내주시면 표와 절차 설명을 채우고
  게이트를 다시 판정하겠습니다.

  (1) 세율·공제액 원문 확인
  1순위 — 국세청: https://www.nts.go.kr 접속 → 검색창에 "해외주식 양도소득세" 또는 "국외주식 양도소득세"
  입력 → 세율(국세+지방소득세), 기본공제 250만원 여부, 신고기한이 함께 보이는 안내 페이지 캡처.
  2순위 — 법제처 찾기쉬운 생활법령정보: https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1701&ccfNo=2&cciNo=3&cnpClsNo=1
  ("주식투자자 > 주식의 거래 > 주식거래에 따른 세금 납부하기") 접속 → 국외 상장주식 양도소득세 항목에서
  세율·공제액과 "이 정보는 OOOO년 O월 O일 기준" 문구가 함께 보이도록 캡처.

  (2) 홈택스 신고 화면
  https://www.hometax.go.kr 로그인 후 "세금신고 > 양도소득세 신고 > 확정신고" 메뉴로 들어가
  국외주식 양도소득 신고 입력 화면(양도가액·취득가액·필요경비·기본공제 입력란이 보이는 단계)을
  개인정보(주민번호·계좌번호 등)는 가리고 캡처.

  캡처했으면: 스크린샷을 이 대화에 그대로 올려주세요. 그걸로 표와 절차 설명을 채우고 재판정하겠습니다.
  추가로, serp_check에서 확인된 경쟁 강도(증권사·은행 공식 자료 다수)가 실제로 게이트2 기준을
  초과하는지도 구글 검색으로 직접 재확인해 주세요 — 초과라면 이 키워드는 캡처와 별개로 재선정 대상입니다.
self_check: |
  게이트1 통과 — monthly_search_volume 8,750회(이전 실행에서 이미 확인됨), 일반 주제 기준 월 500 이상 충족.
  게이트2 미확정/우려 — WebSearch 상위 결과에 증권사·은행 공식 안내가 6~7개로 다수 확인되어 RULES.md
  기준(5개 이상 시 재선정)을 넘어설 가능성이 높음. 구글 상위 10개 직접 확인 전이라 단정하지 않고
  "미확정/우려"로 표기했으나, 사람이 재확인 결과 실제로 5개 이상이면 이 키워드는 캡처 여부와 무관하게
  재선정 대상이 된다는 점을 capture_guide에 함께 남김.
  게이트3 미충족 — 계산 예시가 정보 이득의 핵심인데 정확한 세율·공제액을 1차 출처로 확인하지 못해
  표 값이 비어 있고, 홈택스 신고 화면 캡처도 로그인이 필요해 자동화로는 확보 불가.
  게이트4 미충족 — hometax.go.kr / nts.go.kr / easylaw.go.kr 전부 WebFetch EGRESS_BLOCKED. 대조군인
  www.google.com도 동일하게 차단되어 이번 세션의 WebFetch 자체가 전면 차단된 것으로 판단
  (dividend-income-tax·isa-limit-benefit 초안과 동일 증상, 세 번째 재현).
  출처 신선도: 원문을 못 열어 확인 불가 — 캡처 시 반드시 페이지의 기준일/시행일을 함께 확인해야 함.
  제목 "해외주식 양도소득세 신고 방법" 15자, 30자 이내, 금지어 없음, 조사·접속사 없음. "절차형"
  패턴({대상} 신고 방법)에 부합.
  슬러그 overseas-stock-tax-filing 영문 소문자+하이픈 3단어.
  FAQ 6개와 JSON-LD 1:1 일치. @id를 티스토리 entry 패턴으로 지정.
  이미지 없음 — human-assisted/capture 유형이라 홈택스 신고 화면 캡처 이미지를 사람이 함께 준비하는 것을
  권장(개인정보 가리고, og:image 겸용).
  캡처 필요 항목: (1) 해외주식 양도소득세 세율(국세+지방소득세), (2) 기본공제 250만원 여부와 적용 방식,
  (3) 확정신고 기간, (4) 캡처한 공식 페이지의 URL과 기준일, (5) 홈택스 신고 입력 화면 캡처(개인정보 가림).
---

<p>해외주식을 팔아 이익이 났다면 <b>연 250만 원이 넘는 부분에 양도소득세를 직접 신고·납부</b>해야 합니다. 이 글은 신고 대상과 절차, 그리고 정확한 세율·공제액을 확인하는 방법을 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>해외주식은 대주주 여부와 상관없이 <mark>연간 순이익이 기본공제를 넘으면</mark> 양도소득세 신고 대상입니다.</li>
    <li>정확한 세율과 기본공제 금액은 자료마다 표현이 조금씩 달라 <b>공식 출처로 직접 확인</b>하는 것이 안전합니다.</li>
    <li>신고는 홈택스에서 투자자 본인이 직접 해야 하며, 증권사가 자동으로 대신 신고해주지 않습니다.</li>
    <li>신고 화면은 로그인이 필요해 이 글만으로는 화면 순서를 끝까지 보여줄 수 없어, 실제 화면 캡처를 함께 확인하는 것을 권장합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>해외주식 양도소득세는 누가 내야 하나요</li>
  <li>해외주식 양도소득세 세율은 왜 원문으로 다시 확인해야 하나요</li>
  <li>해외주식 양도소득세는 언제까지 신고하나요</li>
  <li>해외주식 양도소득세는 어떤 순서로 신고하나요</li>
  <li>해외주식 양도소득세 계산 예시 (확인 중)</li>
  <li>해외주식 양도소득세 관련 수치는 어디서 확인하나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 양도소득세는 누가 내야 하나요</h2>

<p>국내 상장주식은 <b>대주주가 아니면</b> 양도소득세를 내지 않는 경우가 많습니다. 반면 해외주식은 <mark>보유 지분이나 금액과 상관없이 일반 투자자도 신고 대상</mark>이 될 수 있다는 점이 가장 큰 차이입니다.</p>

<p>연간 해외주식 양도차익 합계가 기본공제 금액을 넘으면, 그 초과분에 대해 투자자 본인이 직접 세금을 계산해 신고·납부해야 합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 양도소득세 세율은 왜 원문으로 다시 확인해야 하나요</h2>

<p>해외주식 양도소득세의 세율과 기본공제 금액은 여러 증권사·은행 안내 페이지에서 비슷한 숫자로 소개되고 있습니다. 하지만 <mark>정확한 세율·공제액·신고기한은 소득세법에 근거한 수치</mark>이므로, 이 글은 국세청·법제처 같은 1차 출처 원문을 직접 확인하기 전까지 확정 수치를 싣지 않았습니다.</p>

<div style="background:#fff8e6;border-left:4px solid #e0a800;padding:14px 18px;margin:20px 0;">
  <b>확인이 필요한 이유</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>세율과 공제액은 세법 개정에 따라 바뀔 수 있는 수치입니다.</li>
    <li>증권사·은행 콘텐츠마다 작성 시점이 달라 최신 여부를 장담하기 어렵습니다.</li>
    <li>1차 출처(국세청·법제처) 원문을 직접 확인해야 기준일까지 함께 알 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 양도소득세는 언제까지 신고하나요</h2>

<p>해외주식 양도소득세는 예정신고 없이, 거래한 해의 <b>다음 해 5월 한 달간 확정신고</b>로 처리하는 방식이 일반적으로 안내됩니다. 다만 정확한 신고 시작일과 마감일은 1차 출처 확인 후 이 글에 확정 수치로 반영합니다.</p>

<p style="font-size:13px;color:#888;">정확한 신고 기간과 세율(%)은 1차 출처 캡처 전까지 이 글에서 확정하지 않습니다. 캡처가 반영되면 아래 표와 계산 예시가 채워집니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 양도소득세는 어떤 순서로 신고하나요</h2>

<p>일반적으로 안내되는 신고 절차의 큰 흐름은 다음과 같습니다. 다만 실제 화면 구성과 메뉴 명칭은 홈택스 로그인 후 확인해야 하며, 이 글은 로그인이 필요한 화면까지 자동으로 확인할 수 없습니다.</p>

<ol style="line-height:1.9;">
  <li>거래한 증권사에서 <b>연간 해외주식 거래내역(양도소득세 산출 보조자료)</b>을 발급받습니다.</li>
  <li>홈택스에 로그인해 <b>양도소득세 신고 메뉴</b>로 들어갑니다.</li>
  <li>양도가액·취득가액·필요경비 등을 입력하고 <b>기본공제</b>를 적용합니다.</li>
  <li>계산된 세액을 확인하고 <b>신고서를 제출</b>한 뒤 납부합니다.</li>
</ol>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>실제 화면을 캡처할 때 함께 확인할 것</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>거래내역을 <b>합계로 직접 입력</b>하는 방식과 <b>파일로 업로드</b>하는 방식 중 어떤 것을 안내하는지</li>
    <li>기본공제 금액이 입력란에 자동으로 반영되는지, 직접 입력해야 하는지</li>
    <li>국세와 별도로 지방소득세를 다른 곳에서 신고해야 하는지 여부</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 양도소득세 계산 예시 (확인 중)</h2>

<p>아래 표는 양도차익별 세금 계산 구조를 정리하는 틀입니다. 공식 출처로 세율과 공제액이 확인되는 대로 실제 수치를 채울 예정입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">연간 양도차익</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">기본공제 적용 후</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">적용 세율</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">납부 세액</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">200만 원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">1,000만 원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">5,000만 원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">위 표는 1차 출처(국세청·법제처) 원문과 홈택스 신고 화면을 캡처해 채운 뒤에만 발행합니다. 캡처 전에는 발행하지 않습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 양도소득세 관련 수치는 어디서 확인하나요</h2>

<p>정확한 세율·공제액·신고기한은 아래 공식 경로에서 직접 확인하는 것이 가장 안전합니다.</p>

<ul style="line-height:1.9;">
  <li><b>국세청</b> 홈페이지에서 "해외주식 양도소득세" 또는 "국외주식 양도소득세" 안내를 확인합니다.</li>
  <li><b>법제처 찾기쉬운 생활법령정보</b>에서 "주식거래에 따른 세금 납부하기" 항목을 확인합니다.</li>
  <li>실제 신고는 <b>홈택스</b>에 로그인해 양도소득세 신고 메뉴에서 화면 안내를 그대로 따릅니다.</li>
</ul>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>해외주식은 대주주 여부와 상관없이 이익이 기본공제를 넘으면 신고 대상입니다.</li>
    <li>신고는 증권사가 대신 해주지 않고 투자자 본인이 홈택스에서 직접 해야 합니다.</li>
    <li>정확한 세율·공제액·신고기한과 실제 화면 순서는 국세청·법제처 공식 자료와 홈택스 화면으로 확인해야 합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 양도소득세는 누가 내야 하나요</summary>
  <p style="margin:10px 0 0 0;">국내 상장주식과 달리 해외주식은 대주주 여부와 상관없이, 연간 양도차익이 기본공제 금액을 넘는 일반 투자자도 신고 대상이 될 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 양도소득세는 증권사가 자동으로 신고해주나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 배당소득세와 달리 양도소득세는 증권사가 원천징수해주지 않으며, 투자자 본인이 홈택스에서 직접 신고·납부해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 양도소득세 세율과 기본공제는 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">정확한 세율과 공제액은 소득세법에 근거한 수치이며, 이 글은 1차 출처(국세청·법제처) 원문 확인 전까지 확정 수치를 싣지 않았습니다. 공식 자료로 직접 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 양도소득세는 언제까지 신고하나요</summary>
  <p style="margin:10px 0 0 0;">거래한 해의 다음 해 5월 한 달간 확정신고로 처리하는 것이 일반적으로 안내되지만, 정확한 시작일·마감일은 국세청 공식 자료로 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 양도소득세 신고는 어디서 하나요</summary>
  <p style="margin:10px 0 0 0;">홈택스에 로그인해 양도소득세 신고 메뉴에서 진행합니다. 증권사에서 발급받은 거래내역(양도소득세 산출 보조자료)을 미리 준비해두면 편리합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 양도소득세 관련 최신 수치는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">국세청과 법제처 찾기쉬운 생활법령정보가 가장 정확합니다. 실제 신고 화면은 홈택스에 로그인해 직접 확인해야 합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li>1차 출처 캡처 대기 — 국세청 / 법제처 찾기쉬운 생활법령정보 중 확인된 페이지로 채울 예정 (sources/overseas-stock-tax-filing-access-note.md 참고)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를 권유하지 않습니다.
투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "해외주식 양도소득세는 누가 내야 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "국내 상장주식과 달리 해외주식은 대주주 여부와 상관없이, 연간 양도차익이 기본공제 금액을 넘는 일반 투자자도 신고 대상이 될 수 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "해외주식 양도소득세는 증권사가 자동으로 신고해주나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아니요. 배당소득세와 달리 양도소득세는 증권사가 원천징수해주지 않으며, 투자자 본인이 홈택스에서 직접 신고·납부해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "해외주식 양도소득세 세율과 기본공제는 얼마인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정확한 세율과 공제액은 소득세법에 근거한 수치이며, 이 글은 1차 출처(국세청·법제처) 원문 확인 전까지 확정 수치를 싣지 않았습니다. 공식 자료로 직접 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "해외주식 양도소득세는 언제까지 신고하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "거래한 해의 다음 해 5월 한 달간 확정신고로 처리하는 것이 일반적으로 안내되지만, 정확한 시작일·마감일은 국세청 공식 자료로 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "해외주식 양도소득세 신고는 어디서 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "홈택스에 로그인해 양도소득세 신고 메뉴에서 진행합니다. 증권사에서 발급받은 거래내역(양도소득세 산출 보조자료)을 미리 준비해두면 편리합니다."
      }
    },
    {
      "@type": "Question",
      "name": "해외주식 양도소득세 관련 최신 수치는 어디서 확인하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "국세청과 법제처 찾기쉬운 생활법령정보가 가장 정확합니다. 실제 신고 화면은 홈택스에 로그인해 직접 확인해야 합니다."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "해외주식 양도소득세 신고 방법",
  "description": "해외주식 양도소득세 신고 대상과 절차, 정확한 세율·기본공제·신고기한을 확인할 수 있는 공식 출처를 정리했습니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-05",
  "dateModified": "2026-09-05",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing"
  }
}
</script>
