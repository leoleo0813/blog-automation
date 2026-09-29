---
keyword: 달러인덱스 뜻
title: 달러인덱스 뜻 구성 통화 비중과 계산식
slug: dollar-index-meaning-currency-weights
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1750 (PC 380 / 모바일 1370, 2026-09-29 실측)
gate1_pass: true (일반 주제 기준 월 500 이상)
serp_check: |
  [게이트2 v3 판정 2026-09-29 - 통과]
  WebSearch "달러인덱스 뜻 구성 통화 비중" 상위 결과: tossbank.com(핀테크 콘텐츠), kbthink.com(KB 용어사전),
  ko.wikipedia.org(백과), dic.hankyung.com(한경용어사전), namu.wiki(위키), yellow.kr(개인 운영 금융 사이트 2건),
  fcbfi.org(소규모 콘텐츠), mitrade.com(해외 브로커 콘텐츠).
  1) 진입 여지: 있음. yellow.kr, fcbfi.org 등 소규모 콘텐츠가 상위에 섞여 있다.
  2) 검색 의도: 정의 탐색형. 시세 조회가 지배적이지 않다.
  3) 답 완결 여부: 부분적. 상위는 정의와 비중 나열 위주이고, 산식에 가상의 환율을 넣어 통화별
     1% 변동이 지수에 주는 영향을 끝까지 계산한 글, 원/달러 환율과의 구조적 차이(원화는 구성 통화가
     아님)를 표로 정리한 글은 확인되지 않았다. 이 두 각도가 정보이득이다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상의 환율 6개를 산식에 대입한 지수 계산(102.77)과 유로/달러 1% 하락 시 103.37 재계산.
  (b) 구성 통화 6개별 비중 + "달러 1% 강세 시 지수 변동폭" 표(유로 0.58% ~ 스위스프랑 0.04%).
  (c) 달러인덱스 vs 원/달러 환율 비교표.
primary_source: |
  ICE(Intercontinental Exchange) U.S. Dollar Index FAQ PDF와 ICE 제품 가이드 PDF를 WebFetch로 각 1회
  시도했으나 모두 EGRESS_BLOCKED(theice.com, ice.com)로 막혀 원문 직접 열람은 실패했다.
  WebSearch 교차검증: 토스뱅크, KB의생각 용어사전, 한경용어사전, 위키백과(이상 국내), TraderMade,
  EarnForex, Yahoo Finance(이상 해외, 언론 포함)에서 6개 통화 비중(57.6/13.6/11.9/9.1/4.2/3.6%)과
  산식 상수 50.14348112, 기준 1973년 3월=100이 충돌 없이 일치했다. 검색 결과에 ICE 공식 FAQ 문서가 노출되어
  ICE 산하 ICE Data Indices가 산출한다는 점도 확인했다.
  출처 간 불일치 1건: 일부 국내 용어사전 요약은 "FRB 작성·발표"로 적고 있으나, 산식 검색 결과와 ICE FAQ의
  존재는 ICE 산출을 가리킨다. 본문은 ICE 산출로 쓰고 이 불일치를 FAQ에서 공개했다.
기준일: 2026년 9월 기준 (구성 비중은 발표 시점 공개 자료, 계산 예시 환율은 전부 가상)
tags: 달러인덱스, 달러인덱스 뜻, 달러지수, DXY, 달러인덱스 구성 통화, 달러인덱스 계산식, 원달러 환율, 달러 강세, 환율 지표
gate_pass: true
gate_pass_note: |
  게이트1 1,750회(500 이상). 게이트2 v3 통과. 게이트3 산식 대입 계산과 통화별 민감도 표.
  게이트4는 원문 WebFetch 2개 도메인 실패 후 다수 독립 출처 교차검증(비중은 제도 수치가 아닌 지수 정의).
  사람은 발행 전 ICE 공식 FAQ(ice.com/publicdocs/futures_us/ICE_Dollar_Index_FAQ.pdf)에서 비중과 산출 주체만
  눈으로 확인하면 충분하다.
capture_guide: ""
self_check: |
  [2026-09-29 gate_pass:true]
  후보 경위: 신규 8개 실측(FOMC 뜻 20, 점도표 뜻 70, 엔캐리트레이드 뜻 160, 양적긴축 뜻 30, 장단기금리차 뜻 20,
  스태그플레이션 뜻 460 FAIL / 달러인덱스 뜻 1,750, 필라델피아반도체지수 342,800 PASS). 필라델피아반도체지수는
  시세 조회 의도가 지배적(탈락조건 2 우려)이라 보류, 달러인덱스 뜻 채택.
  카니벌라이제이션: 기존 97편 중 달러인덱스 전용 편 없음(미국주식 세금·해외주식 편에서 환율 언급 정도).
  YMYL: 특정 종목·환전 시점 추천 없음, 예시 환율 전부 가상, 단정 표현 없음.
  기관 링크: 기관 안내 문장 1개(ICE) 링크, 출처 목록 3개 전부 링크.
  제목 "달러인덱스 뜻 구성 통화 비중과 계산식" 20자, 금지어 없음. 슬러그 영문 소문자 하이픈 4단어.
  첫 문장 유형: 수치충격형(직전 97편은 문제제기형, 96편은 정의형으로 겹치지 않음).
  글 구조 유형: 계산형(목차 직후 계산 박스 먼저). 직전 비교형·계산형·개념형 중 3편 연속 아님.
  AI 티 점검: em대시 0개, 다만 0회(본문 기준), mark 밀도 4개, FAQ 5개, H2 5개 중 "~나요"형 2개.
  요약박스 색 초록(#edf7ee/#2e7d32), 제목 "💵 달러인덱스, 세 줄로 정리". FAQ 헤딩 "알아두면 덜 헷갈리는 것들".
  면책 문구 새 표현. 헤지 표현 없음.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-29</p>

<p>달러인덱스의 절반이 넘는 57.6%는 유로 한 통화의 움직임으로 결정됩니다. 그래서 원화 환율이 그대로여도 유로가 흔들리면 지수는 크게 달라집니다. 이 글은 달러인덱스 뜻, 6개 구성 통화 비중, 가상의 환율로 직접 계산해 보는 산식을 정리합니다.</p>

<div style="background:#edf7ee;border:2px solid #2e7d32;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1b5e20;font-size:18px;">💵 달러인덱스, 세 줄로 정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>달러인덱스는 6개 통화 대비 미국 달러의 평균 가치이고, 1973년 3월을 100으로 잡습니다.</li>
    <li>유로 57.6%, 엔 13.6%, 파운드 11.9%, 캐나다달러 9.1%, 스웨덴크로나 4.2%, 스위스프랑 3.6%로 구성됩니다.</li>
    <li>원화는 구성 통화가 아니어서 달러인덱스와 원/달러 환율은 따로 움직일 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>산식에 숫자를 넣어 직접 계산하기</li>
  <li>달러인덱스 뜻과 구성 통화 비중</li>
  <li>달러 1% 강세가 지수에 미치는 영향</li>
  <li>달러인덱스와 원/달러 환율은 어떻게 다른가요</li>
  <li>알아두면 덜 헷갈리는 것들</li>
</ol>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">산식에 숫자를 넣어 직접 계산하기</h2>

<p>달러인덱스는 6개 환율을 비중만큼 거듭제곱해서 곱한 값입니다. 산식은 아래와 같습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <strong>USDX = 50.14348112 × EURUSD<sup>-0.576</sup> × USDJPY<sup>0.136</sup> × GBPUSD<sup>-0.119</sup> × USDCAD<sup>0.091</sup> × USDSEK<sup>0.042</sup> × USDCHF<sup>0.036</sup></strong>
</div>

<p>유로와 파운드는 "1유로가 몇 달러인가"로 표시해서 지수가 음의 지수를 갖습니다. 엔, 캐나다달러, 크로나, 프랑은 "1달러가 몇 단위인가"로 표시해서 양의 지수를 갖습니다.</p>

<p>아래는 이해를 돕기 위해 만든 가상의 환율입니다. 실제 시세가 아닙니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">환율(가상)</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">예시 값</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">산식 지수</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">EURUSD</td><td style="border:1px solid #ddd;padding:8px;">1.10</td><td style="border:1px solid #ddd;padding:8px;">-0.576</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">USDJPY</td><td style="border:1px solid #ddd;padding:8px;">150</td><td style="border:1px solid #ddd;padding:8px;">0.136</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">GBPUSD</td><td style="border:1px solid #ddd;padding:8px;">1.30</td><td style="border:1px solid #ddd;padding:8px;">-0.119</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">USDCAD</td><td style="border:1px solid #ddd;padding:8px;">1.35</td><td style="border:1px solid #ddd;padding:8px;">0.091</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">USDSEK</td><td style="border:1px solid #ddd;padding:8px;">10.5</td><td style="border:1px solid #ddd;padding:8px;">0.042</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">USDCHF</td><td style="border:1px solid #ddd;padding:8px;">0.90</td><td style="border:1px solid #ddd;padding:8px;">0.036</td></tr>
  </tbody>
</table>

<p>위 값을 산식에 넣으면 달러인덱스는 <mark>약 102.77</mark>입니다. 100보다 크니 이 가상 상황에서 달러는 1973년 3월보다 강하다는 뜻입니다.</p>

<p>이제 유로만 1% 약해져 EURUSD가 1.089가 됐다고 가정합니다. 나머지 환율은 그대로 두고 다시 계산하면 지수는 <mark>약 103.37</mark>로 0.58% 오릅니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">달러인덱스 뜻과 구성 통화 비중</h2>

<p>달러인덱스는 유로, 일본 엔, 영국 파운드, 캐나다 달러, 스웨덴 크로나, 스위스 프랑 6개 통화 대비 미국 달러의 가치를 하나의 숫자로 나타낸 지표입니다. 약칭은 USDX 또는 DXY이고, 1973년 3월의 가치를 100으로 놓고 비교합니다.</p>

<p>산출은 ICE(Intercontinental Exchange) 산하 ICE Data Indices가 맡고 있습니다. 자세한 정의는 <a href="https://www.ice.com/publicdocs/futures_us/ICE_Dollar_Index_FAQ.pdf" target="_blank" rel="noopener">ICE 달러인덱스 FAQ 문서</a>에서 볼 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">통화</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">비중</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">유로(EUR)</td><td style="border:1px solid #ddd;padding:8px;"><mark>57.6%</mark></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">일본 엔(JPY)</td><td style="border:1px solid #ddd;padding:8px;">13.6%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">영국 파운드(GBP)</td><td style="border:1px solid #ddd;padding:8px;">11.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">캐나다 달러(CAD)</td><td style="border:1px solid #ddd;padding:8px;">9.1%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">스웨덴 크로나(SEK)</td><td style="border:1px solid #ddd;padding:8px;">4.2%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">스위스 프랑(CHF)</td><td style="border:1px solid #ddd;padding:8px;">3.6%</td></tr>
  </tbody>
</table>

<p>유럽 통화(유로, 파운드, 크로나, 프랑)를 합치면 77.3%입니다. 달러인덱스는 사실상 "달러 대 유럽 통화" 지표에 가깝습니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">달러 1% 강세가 지수에 미치는 영향</h2>

<p>한 통화 대비 달러가 1% 강해지면 지수는 그 통화의 비중과 거의 같은 비율로 움직입니다. 위의 가상 환율에서 통화 하나씩만 바꿔 계산한 결과입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">달러가 1% 강해진 상대</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">지수 변동(가상 계산)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">유로</td><td style="border:1px solid #ddd;padding:8px;"><mark>약 +0.58%</mark></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">일본 엔</td><td style="border:1px solid #ddd;padding:8px;">약 +0.14%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">영국 파운드</td><td style="border:1px solid #ddd;padding:8px;">약 +0.12%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">캐나다 달러</td><td style="border:1px solid #ddd;padding:8px;">약 +0.09%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">스웨덴 크로나</td><td style="border:1px solid #ddd;padding:8px;">약 +0.04%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">스위스 프랑</td><td style="border:1px solid #ddd;padding:8px;">약 +0.04%</td></tr>
  </tbody>
</table>

<p>엔화가 아무리 크게 움직여도 유로가 같은 폭으로 움직일 때보다 지수 영향은 4분의 1 수준입니다. 지수가 오르내릴 때는 유로 흐름부터 확인하는 편이 빠릅니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">달러인덱스와 원/달러 환율은 어떻게 다른가요</h2>

<p>원화는 달러인덱스 6개 구성 통화에 들어 있지 않습니다. 원/달러 환율은 원화와 달러의 관계만 보여주고, 달러인덱스는 유럽·일본 등 6개 통화와 달러의 관계를 보여줍니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">달러인덱스</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">원/달러 환율</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">비교 대상</td><td style="border:1px solid #ddd;padding:8px;">6개 통화(유로 57.6% 등)</td><td style="border:1px solid #ddd;padding:8px;">원화 1개</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">원화 포함 여부</td><td style="border:1px solid #ddd;padding:8px;">미포함</td><td style="border:1px solid #ddd;padding:8px;">해당</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기준점</td><td style="border:1px solid #ddd;padding:8px;">1973년 3월 = 100</td><td style="border:1px solid #ddd;padding:8px;">기준점 없음, 1달러당 원화 값</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">수치 의미</td><td style="border:1px solid #ddd;padding:8px;">100 초과면 기준 시점보다 달러 강세</td><td style="border:1px solid #ddd;padding:8px;">숫자가 클수록 원화 약세</td></tr>
  </tbody>
</table>

<p>그래서 달러인덱스가 내려가는 날에도 원/달러 환율은 오를 수 있습니다. 두 지표가 다른 방향으로 갈 때는 원화만의 요인이 있다는 신호로 읽습니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">알아두면 덜 헷갈리는 것들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러인덱스가 100이면 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">기준 시점인 1973년 3월과 달러 가치가 같다는 뜻입니다. 100보다 높으면 그때보다 달러가 강하고, 낮으면 약합니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러인덱스에 원화나 위안화는 들어 있나요</summary>
  <p style="margin:10px 0 0 0;">들어 있지 않습니다. 구성 통화는 유로, 엔, 파운드, 캐나다달러, 스웨덴크로나, 스위스프랑 6개입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러인덱스는 미국 연준이 발표하나요</summary>
  <p style="margin:10px 0 0 0;">이 글이 확인한 자료 기준으로 산출 주체는 ICE 산하 ICE Data Indices입니다. 일부 국내 용어사전은 연준(FRB)이 작성한다고 적고 있으나, 연준이 따로 공표하는 무역가중 달러지수와 혼동한 것으로 보입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러인덱스가 오르면 주식시장에는 어떤 영향이 있나요</summary>
  <p style="margin:10px 0 0 0;">방향을 단정할 수 없습니다. 달러 강세가 수출기업 실적, 외국인 자금 흐름, 원자재 가격에 미치는 경로는 시기마다 다르고, 이 글은 지수 자체의 구조만 다룹니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러인덱스 구성 비중은 자주 바뀌나요</summary>
  <p style="margin:10px 0 0 0;">이 글이 확인한 자료에서는 위 6개 통화와 비중이 공통으로 제시됩니다. 최신 여부는 ICE 공식 문서에서 다시 확인하는 것이 안전합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.ice.com/publicdocs/futures_us/ICE_Dollar_Index_FAQ.pdf" target="_blank" rel="noopener">ICE - U.S. Dollar Index Contracts FAQ</a></li>
    <li><a href="https://dic.hankyung.com/economy/view/?seq=9266" target="_blank" rel="noopener">한국경제 - 한경용어사전 달러 인덱스</a></li>
    <li><a href="https://kbthink.com/dictionary/view.html?dictId=KED-00009266" target="_blank" rel="noopener">KB의 생각 - 달러 인덱스란</a></li>
  </ul>
  기준일: 2026년 9월 기준. 본문의 환율과 지수 계산값은 이해를 돕기 위한 가상의 예시이며 실제 시세가 아닙니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 지표의 구조를 설명하는 정보 글이며, 특정 종목이나 환전 시점을 권하지 않습니다. 환율과 지수는 계속 변하므로 최신 값은 직접 확인하시고, 투자 판단의 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "달러인덱스 뜻 구성 통화 비중과 계산식",
  "description": "달러인덱스 뜻과 6개 구성 통화 비중, 가상의 환율로 직접 계산해 보는 산식, 원/달러 환율과의 차이를 정리합니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Organization",
    "name": "센시티브보스"
  },
  "datePublished": "2026-09-29",
  "dateModified": "2026-09-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/dollar-index-meaning-currency-weights"
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
      "name": "달러인덱스가 100이면 무슨 뜻인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "기준 시점인 1973년 3월과 달러 가치가 같다는 뜻입니다. 100보다 높으면 그때보다 달러가 강하고, 낮으면 약합니다."
      }
    },
    {
      "@type": "Question",
      "name": "달러인덱스에 원화나 위안화는 들어 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "들어 있지 않습니다. 구성 통화는 유로, 엔, 파운드, 캐나다달러, 스웨덴크로나, 스위스프랑 6개입니다."
      }
    },
    {
      "@type": "Question",
      "name": "달러인덱스는 미국 연준이 발표하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이 글이 확인한 자료 기준으로 산출 주체는 ICE 산하 ICE Data Indices입니다. 일부 국내 용어사전은 연준(FRB)이 작성한다고 적고 있으나, 연준이 따로 공표하는 무역가중 달러지수와 혼동한 것으로 보입니다."
      }
    },
    {
      "@type": "Question",
      "name": "달러인덱스가 오르면 주식시장에는 어떤 영향이 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "방향을 단정할 수 없습니다. 달러 강세가 수출기업 실적, 외국인 자금 흐름, 원자재 가격에 미치는 경로는 시기마다 다르고, 이 글은 지수 자체의 구조만 다룹니다."
      }
    },
    {
      "@type": "Question",
      "name": "달러인덱스 구성 비중은 자주 바뀌나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이 글이 확인한 자료에서는 위 6개 통화와 비중이 공통으로 제시됩니다. 최신 여부는 ICE 공식 문서에서 다시 확인하는 것이 안전합니다."
      }
    }
  ]
}
</script>
