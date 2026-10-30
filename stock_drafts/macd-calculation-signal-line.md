---
keyword: MACD
title: MACD 보는법과 계산법, 골든크로스보다 빠른 이유
slug: macd-calculation-signal-line
track: chart
thumb_title: MACD 보는법|직접 계산해 보기
thumb_note: 골든크로스보다 빠를까?
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1920 (PC 620 / 모바일 1300), "MACD 보는법" 1600
gate1_pass: true (2026-10-30 실측)
serp_check: |
  [2026-10-30] 상위는 증권사·투자 교육 사이트, 나무위키, 해외 지표 사이트 번역 글. 공식과 "골든크로스=매수" 설명이 대부분.
  같은 가격에서 하루치를 손으로 계산하는 과정, 이평선 골든크로스와의 신호 순서 비교, 가짜 신호 구간을 보여 주는 글은 드묾.
unique_asset: |
  (a) 39일째 하루 MACD·시그널·히스토그램 손계산 표, (b) 가정 가격 78일 전체 계산 그림(①~④ 표시),
  (c) 같은 가격에서 MACD 시그널 교차(39)·5/20 골든크로스(44)·MACD 0선(48)·MACD 하향(64)·데드크로스(71) 순서 비교,
  (d) 가짜 신호 3가지(완만한 추세 엇갈림 35~38일, 횡보 구간, 원 단위라 종목 간 비교 불가).
primary_source: |
  수학적 정의(RULES: 기관 출처 불필요): MACD=EMA12−EMA26, 시그널=MACD의 EMA9, 히스토그램=MACD−시그널, α=2/(N+1).
  역사: 제럴드 아펠 1970년대 후반(1979 출간 언급), 토머스 아스프레이 1986 히스토그램 — LuxAlgo, S&C 잡지 V.6:8 목록, 위키 미러 일치.
  예시 수치는 전부 가정 가격으로 직접 계산(스크립트로 재현 가능, EMA 첫 값은 단순평균).
기준일: 2026-10-30
tags: MACD, MACD 계산, MACD 시그널, MACD 보는법, 골든크로스, 지수이동평균, 보조지표
gate_pass: true
gate_pass_note: |
  게이트1 1,810 통과(2026-10-27 방향 전환 B 기준 목록). 게이트2 계산·비교·한계로 정보이득. 게이트4 수학적 정의·직접 계산.
self_check: |
  [2026-10-30] 차트·지표 시리즈 첫 신규 편(RULES 「방향 전환」 B: ① 직접 계산 ② 이평선 골든크로스와 비교 ③ 틀리는 경우 — 3개 충족).
  매수·매도 권유 없음, 예시는 가정값 명시. 내부 링크 2개(이동평균선, RSI).
refresh_due: 2027-04-30
refresh_reason: "차트 시리즈 허브 글이 생기면 허브 링크 추가, 서치 콘솔 검색어 반영"
figure_plan: "1: 가정 가격 78일 종가+MACD·시그널·히스토그램(①~④) / 2: 같은 가격에서 신호 순서 타임라인"
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-30</p>

<p>MACD는 <mark>12일 지수이동평균(EMA)에서 26일 지수이동평균을 뺀 값</mark>이고, 이 MACD를 다시 9일 지수이동평균한 선을 <b>시그널선</b>이라고 불러요. 두 선이 교차하거나 MACD가 0을 넘는 순간을 보면 짧은 추세와 긴 추세가 언제 엇갈리는지 알 수 있어요.</p>

<p>공식만 보면 막막하니, 가정 가격 78일치로 MACD를 처음부터 직접 계산하고, 같은 가격에서 이동평균선 골든크로스와 어느 쪽이 먼저 신호를 냈는지, 가짜 신호는 어디서 나왔는지까지 비교해 볼게요.</p>

<div style="background:#eef7f1;border:2px solid #2f6f4f;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1e4e36;font-size:18px;">📐 숫자 세 개로 끝나는 지표</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>MACD선</b> = 12일 EMA − 26일 EMA (원 단위)</li>
    <li><b>시그널선</b> = MACD의 9일 EMA</li>
    <li><b>히스토그램</b> = MACD − 시그널 (막대가 0 위면 MACD가 시그널보다 위)</li>
    <li>12·26·9는 1970년대 후반 제럴드 아펠이 쓴 관례값이고, 히스토그램은 1986년 토머스 아스프레이가 더했어요.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MACD 공식과 지수이동평균(EMA) 한 번에 이해하기</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">하루치 MACD 직접 계산해 보기</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">78일 예시로 보는 MACD·시그널·히스토그램</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MACD와 이동평균선 골든크로스, 어느 쪽이 먼저일까</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MACD 신호가 틀리는 경우 3가지</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MACD Q&amp;A 5개</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">MACD 공식과 지수이동평균(EMA) 한 번에 이해하기</h2>

<p>MACD는 이동평균 두 개의 <b>거리</b>를 재는 지표예요. 짧은 평균(12일)이 긴 평균(26일)보다 위에 있으면 MACD는 플러스, 아래면 마이너스예요. 거리가 벌어지면(발산) 추세가 세지고, 좁혀지면(수렴) 약해진다고 읽어요. 이름 Moving Average Convergence Divergence가 바로 이 뜻이에요.</p>

<p>여기서 쓰는 평균은 단순평균이 아니라 <mark>지수이동평균(EMA)</mark>이에요. 최근 가격에 가중치를 더 줘서 단순평균보다 빨리 움직여요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">가중치(α = 2 ÷ (기간+1))</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">오늘 EMA</td><td style="border:1px solid #ddd;padding:8px;">어제 EMA + α × (오늘 종가 − 어제 EMA)</td><td style="border:1px solid #ddd;padding:8px;">—</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12일 EMA</td><td style="border:1px solid #ddd;padding:8px;">위 식, 기간 12</td><td style="border:1px solid #ddd;padding:8px;">2/13 ≈ 0.154</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">26일 EMA</td><td style="border:1px solid #ddd;padding:8px;">위 식, 기간 26</td><td style="border:1px solid #ddd;padding:8px;">2/27 ≈ 0.074</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">시그널(9일)</td><td style="border:1px solid #ddd;padding:8px;">위 식을 MACD 값에 적용</td><td style="border:1px solid #ddd;padding:8px;">2/10 = 0.2</td></tr>
  </tbody>
</table>

<p>EMA의 첫 값은 보통 처음 12일(또는 26일) 종가의 단순평균으로 시작해요. 시작하는 방법이 앱마다 조금씩 달라서, 같은 종목이라도 증권사마다 MACD 값이 소수점 단위로 다를 수 있어요. 단순이동평균으로 계산하는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/moving-average-5-20-day-cross" target="_blank" rel="noopener">이동평균선 5일 20일 계산과 크로스 보는 법</a>에 정리해 뒀어요.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">하루치 MACD 직접 계산해 보기</h2>

<p>아래 예시 가격(가정값)의 39일째 하루만 손으로 계산해 볼게요. 전날(38일째) 값이 이미 있다고 하면 네 줄이면 끝나요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">항목</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">39일째 값</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">종가</td><td style="border:1px solid #ddd;padding:8px;">—</td><td style="border:1px solid #ddd;padding:8px;">9,760원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12일 EMA</td><td style="border:1px solid #ddd;padding:8px;">9,857.1 + 0.154 × (9,760 − 9,857.1)</td><td style="border:1px solid #ddd;padding:8px;">9,842.2</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">26일 EMA</td><td style="border:1px solid #ddd;padding:8px;">10,068.1 + 0.074 × (9,760 − 10,068.1)</td><td style="border:1px solid #ddd;padding:8px;">10,045.2</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;"><mark>MACD</mark></td><td style="border:1px solid #ddd;padding:8px;">9,842.2 − 10,045.2</td><td style="border:1px solid #ddd;padding:8px;"><b>−203.1</b></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;"><mark>시그널</mark></td><td style="border:1px solid #ddd;padding:8px;">−210.4 + 0.2 × (−203.1 − (−210.4))</td><td style="border:1px solid #ddd;padding:8px;"><b>−208.9</b></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">히스토그램</td><td style="border:1px solid #ddd;padding:8px;">−203.1 − (−208.9)</td><td style="border:1px solid #ddd;padding:8px;">+5.9</td></tr>
  </tbody>
</table>

<p>(소수점 반올림 때문에 마지막 자리는 0.1 정도 차이가 날 수 있어요.)</p>

<p>MACD는 아직 마이너스(−203)라서 12일 평균이 26일 평균보다 아래예요. 그런데 히스토그램이 플러스로 바뀌었어요. <b>"아직 하락 추세 안이지만 내려가는 힘이 줄기 시작했다"</b>는 뜻이고, 이게 MACD가 이동평균선보다 빨리 움직이는 이유예요.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">78일 예시로 보는 MACD·시그널·히스토그램</h2>

<p>같은 방법으로 78일을 모두 계산하면 아래 그림이 나와요. 가격은 38일째까지 천천히 내리다가, 39일째부터 오르고, 57일째쯤부터 옆으로 흔들리게 만든 가정값이에요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/macd-calculation-signal-line-1.png" alt="가정 가격 78일의 종가와 MACD, 시그널, 히스토그램, 신호가 나온 날 네 곳 표시" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">위는 종가, 아래는 MACD(남색)·시그널(주황)·히스토그램(막대)이에요. ①~④는 신호가 나온 날이에요.</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">표시</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">날</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">무슨 일</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">그날 종가</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">①</td><td style="border:1px solid #ddd;padding:8px;">39일째</td><td style="border:1px solid #ddd;padding:8px;">MACD가 시그널 위로 올라섬</td><td style="border:1px solid #ddd;padding:8px;">9,760원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">②</td><td style="border:1px solid #ddd;padding:8px;">44일째</td><td style="border:1px solid #ddd;padding:8px;">5일·20일 단순이동평균 골든크로스</td><td style="border:1px solid #ddd;padding:8px;">10,060원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">③</td><td style="border:1px solid #ddd;padding:8px;">48일째</td><td style="border:1px solid #ddd;padding:8px;">MACD가 0 위로(12일 EMA가 26일 EMA를 넘음)</td><td style="border:1px solid #ddd;padding:8px;">10,340원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">④</td><td style="border:1px solid #ddd;padding:8px;">64일째</td><td style="border:1px solid #ddd;padding:8px;">MACD가 시그널 아래로 내려감</td><td style="border:1px solid #ddd;padding:8px;">10,860원</td></tr>
  </tbody>
</table>

<p>세 선의 역할을 한 줄씩 정리하면 이래요. <b>MACD가 0보다 위</b>면 짧은 추세가 긴 추세보다 위에 있다는 뜻이고, <b>MACD가 시그널보다 위</b>(히스토그램 플러스)면 그 거리가 최근 벌어지는 중이라는 뜻이에요. 히스토그램 막대가 줄어들면 거리가 다시 좁혀지고 있다는 표시예요.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">MACD와 이동평균선 골든크로스, 어느 쪽이 먼저일까</h2>

<p>같은 가격으로 계산했을 때 신호가 나온 순서는 아래와 같아요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/macd-calculation-signal-line-2.png" alt="같은 가격에서 MACD 시그널 교차, 이동평균선 골든크로스, MACD 0선 교차, 데드크로스가 나온 순서" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">오를 때도 꺾일 때도 MACD와 시그널의 교차가 가장 먼저 나왔어요.</figcaption></figure>

<ul style="line-height:1.9;">
  <li><b>오르기 시작할 때:</b> MACD·시그널 교차(39일째) → 5·20일 골든크로스(44일째) → MACD 0선 돌파(48일째) 순이었어요. 0선 돌파는 사실 <mark>12일·26일 EMA의 골든크로스</mark>와 같은 사건이라, 평균 기간이 긴 만큼 늦게 나와요.</li>
  <li><b>꺾일 때:</b> MACD가 시그널 아래로 내려간 날(64일째)이 5·20일 데드크로스(71일째)보다 7거래일 빨랐어요.</li>
  <li>대신 39일째 신호가 나온 날의 종가 9,760원과 0선 돌파 날의 10,340원은 580원(약 6%) 차이예요. 빠른 신호는 일찍 알려 주는 대신, 아래 같은 가짜 신호도 같이 내요.</li>
</ul>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">MACD 신호가 틀리는 경우 3가지</h2>

<ol style="line-height:1.9;">
  <li><b>천천히 같은 방향으로 움직일 때 엇갈림이 반복돼요.</b> 예시에서 가격이 하루 30원 안팎으로 꾸준히 내리던 35~38일째에 MACD와 시그널이 3번 엇갈렸어요. 두 선이 거의 붙어 있으면 작은 변동에도 교차가 생겨요.</li>
  <li><b>옆으로 흔들리는 구간에서는 신호가 의미를 잃어요.</b> 57일째 이후 가격은 10,740~11,040원 안에서 오갔는데, 5·20일 이평은 71·74·75일째에 연달아 교차했어요. MACD는 0 위에 머물면서 조금씩 줄어들 뿐이라 뚜렷한 방향을 보여 주지 못했어요.</li>
  <li><b>MACD 값은 원 단위라 종목끼리 비교할 수 없어요.</b> 1만원짜리 주식의 MACD 200과 100만원짜리 주식의 MACD 200은 전혀 다른 크기예요. 과열 정도를 0~100으로 보고 싶다면 <a href="https://sensitiveboss3.tistory.com/entry/rsi-meaning-14day-calculation" target="_blank" rel="noopener">RSI 14일 값 직접 구하기</a>처럼 비율로 나오는 지표가 맞아요.</li>
</ol>

<p>정리하면 MACD는 "추세가 바뀌기 시작했을 수 있다"를 빨리 알려 주는 도구이고, 그 신호가 맞는지는 시간이 지나야 알 수 있어요. 한 가지 지표만으로 판단하기보다 가격 흐름, 거래량, 다른 지표와 함께 보는 이유예요.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">MACD Q&amp;A 5개</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">MACD 계산 공식이 뭔가요</summary>
  <p style="margin:10px 0 0 0;">MACD = 12일 지수이동평균 − 26일 지수이동평균이에요. 시그널선은 MACD의 9일 지수이동평균이고, 히스토그램은 MACD에서 시그널을 뺀 값이에요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">MACD 시그널선 교차는 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">MACD가 시그널 위로 올라서면 짧은 평균과 긴 평균의 거리가 최근 벌어지기 시작했다는 뜻이고, 아래로 내려가면 좁혀지기 시작했다는 뜻이에요. 추세 변화를 빨리 보여 주지만 횡보 구간에서는 가짜 교차가 많아요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">MACD 0선 돌파와 골든크로스는 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">MACD가 0을 넘는 순간은 12일 지수이동평균이 26일 지수이동평균을 넘는 순간과 같아요. 그래서 0선 돌파는 지수이동평균끼리의 골든크로스라고 볼 수 있고, 5일·20일 단순이동평균 골든크로스와는 기간과 계산 방식이 달라요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">MACD 설정 12, 26, 9는 바꿔도 되나요</summary>
  <p style="margin:10px 0 0 0;">바꿀 수 있어요. 12·26·9는 만든 사람이 쓰던 관례값일 뿐이에요. 기간을 줄이면 신호가 빨라지는 대신 가짜 신호가 늘고, 늘리면 반대예요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증권사 앱마다 MACD 값이 다른 이유는 뭔가요</summary>
  <p style="margin:10px 0 0 0;">지수이동평균의 첫 값을 어떻게 시작하는지, 며칠치 데이터로 계산을 시작했는지가 앱마다 달라서 소수점 단위 차이가 생겨요. 교차가 나오는 날은 보통 같거나 하루 정도 차이예요.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.luxalgo.com/library/concept/macd/" target="_blank" rel="noopener">LuxAlgo: MACD 개념과 역사(제럴드 아펠, 12·26·9)</a></li>
    <li><a href="https://store.traders.com/-v06-c08-macd-pdf.html" target="_blank" rel="noopener">Technical Analysis of Stocks &amp; Commodities V.6:8, Thomas Aspray "MACD Momentum"(1986)</a></li>
    <li>본문 계산: 가정 가격 78일로 직접 계산(실제 종목·시세 아님). EMA 첫 값은 단순평균으로 시작.</li>
  </ul>
  기준일: 2026년 10월 30일.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
정보 제공을 목적으로 쓴 글이며 특정 종목의 매수·매도를 권유하지 않아요. 예시 가격은 계산을 보여 주기 위한 가정값이고, 지표 신호가 미래 가격을 보장하지 않아요. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있어요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "MACD 보는법과 계산법, 골든크로스보다 빠른 이유",
  "description": "MACD(12일 EMA−26일 EMA)와 시그널선·히스토그램 계산을 가정 가격 78일로 직접 해 보고, 이동평균선 골든크로스와 신호 순서를 비교하고, 가짜 신호가 나오는 경우 3가지를 정리했어요.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Organization",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-30",
  "dateModified": "2026-10-30",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/macd-calculation-signal-line-1.png",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/macd-calculation-signal-line"
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
      "name": "MACD 계산 공식이 뭔가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "MACD = 12일 지수이동평균 − 26일 지수이동평균이에요. 시그널선은 MACD의 9일 지수이동평균이고, 히스토그램은 MACD에서 시그널을 뺀 값이에요."
      }
    },
    {
      "@type": "Question",
      "name": "MACD 시그널선 교차는 무슨 뜻인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "MACD가 시그널 위로 올라서면 짧은 평균과 긴 평균의 거리가 최근 벌어지기 시작했다는 뜻이고, 아래로 내려가면 좁혀지기 시작했다는 뜻이에요. 추세 변화를 빨리 보여 주지만 횡보 구간에서는 가짜 교차가 많아요."
      }
    },
    {
      "@type": "Question",
      "name": "MACD 0선 돌파와 골든크로스는 같은 건가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "MACD가 0을 넘는 순간은 12일 지수이동평균이 26일 지수이동평균을 넘는 순간과 같아요. 그래서 0선 돌파는 지수이동평균끼리의 골든크로스라고 볼 수 있고, 5일·20일 단순이동평균 골든크로스와는 기간과 계산 방식이 달라요."
      }
    },
    {
      "@type": "Question",
      "name": "MACD 설정 12, 26, 9는 바꿔도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "바꿀 수 있어요. 12·26·9는 만든 사람이 쓰던 관례값일 뿐이에요. 기간을 줄이면 신호가 빨라지는 대신 가짜 신호가 늘고, 늘리면 반대예요."
      }
    },
    {
      "@type": "Question",
      "name": "증권사 앱마다 MACD 값이 다른 이유는 뭔가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "지수이동평균의 첫 값을 어떻게 시작하는지, 며칠치 데이터로 계산을 시작했는지가 앱마다 달라서 소수점 단위 차이가 생겨요. 교차가 나오는 날은 보통 같거나 하루 정도 차이예요."
      }
    }
  ]
}
</script>
