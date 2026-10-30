---
keyword: 일목균형표
title: 일목균형표 보는법과 계산, 구름대·전환선·기준선 한 번에
slug: ichimoku-cloud-calculation
track: chart
thumb_title: 일목균형표|구름대 보는 법
thumb_note: 왜 26일 앞에 그릴까?
thumb_art: cloud
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 2180 (PC 690 / 모바일 1490)
gate1_pass: true (2026-10-30 실측, "일목균형표 보는법" 350)
serp_check: |
  [2026-10-30] 상위는 증권사 교육·나무위키·투자 커뮤니티. 공식과 "구름 위=상승" 설명이 대부분.
  하루치를 손으로 계산해 어느 칸에 그려지는지 보여 주는 글, 같은 가격에서 MACD·이평선과 신호 순서·가짜 신호 수를 비교한 글은 드묾.
unique_asset: |
  (a) 88일째 다섯 선 손계산 표(그려지는 칸까지), (b) 145일 전체 계산 그림(구름 색·미래 26일 칸, ①~④),
  (c) 선이 그려지는 위치 그림, (d) 같은 가격에서 MACD·5/20 이평·전환/기준·구름 신호 순서와 가짜 교차 수 비교, (e) 틀리는 경우 3가지.
primary_source: |
  수학적 정의(기관 출처 불필요): 전환선=(9일 고가+저가)/2, 기준선=26일, 선행1=(전환+기준)/2 26일 앞, 선행2=52일 26일 앞, 후행=종가 26일 뒤.
  기본값 9·26·52, 1969년 공개(일목산인=호소다 고이치): cTrader·backtrader 문서·Wikipedia·procharting 일치.
  예시 수치는 전부 가정 가격으로 직접 계산(assets/figures/ichimoku-cloud-calculation-data.py로 재현).
기준일: 2026-10-30
tags: 일목균형표, 일목균형표 보는법, 구름대, 전환선, 기준선, 후행스팬, 선행스팬, 보조지표
gate_pass: true
gate_pass_note: |
  게이트1 2,180 통과(방향 전환 B 목록). 게이트2 계산·비교·한계로 정보이득. 게이트4 수학적 정의·직접 계산.
self_check: |
  [2026-10-30] 차트·지표 시리즈 2번째. B 조건 ①계산 ②비교 ③한계 충족. 그림 3장 + 썸네일.
  내부 링크 3개(이동평균선·RSI 발행, MACD 발행 전 — MACD 먼저 발행).
refresh_due: 2027-04-30
refresh_reason: "차트 시리즈 허브 글이 생기면 허브 링크 추가, 서치 콘솔 검색어 반영"
figure_plan: "3장: 1 145일 계산 그림(구름·선·①~④) / 2 선이 그려지는 위치(손그림) / 3 신호 순서(손그림)"
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-30</p>

<p>일목균형표는 <mark>전환선(9일)·기준선(26일)·선행스팬1·선행스팬2(52일)·후행스팬</mark> 다섯 선으로 가격의 균형을 보는 지표예요. 선행스팬 두 개 사이를 칠한 <b>구름(구름대)</b> 위에 가격이 있으면 오름 쪽, 아래면 내림 쪽 균형으로 읽어요.</p>

<p>다른 지표와 가장 다른 점은 <b>선이 그려지는 칸이 오늘이 아니라는 것</b>이에요. 가정 가격 145일치로 다섯 선을 직접 계산하고, 같은 가격에서 MACD·이동평균선보다 신호가 언제 나왔는지 비교해 볼게요.</p>

<div style="background:#eef7f1;border:2px solid #2f6f4f;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1e4e36;font-size:18px;">☁️ 평균이 아니라 '가운데 값'</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>이동평균선은 종가를 더해 나누지만, 일목균형표는 <b>기간 중 최고가와 최저가의 가운데</b>를 써요.</li>
    <li>선행스팬은 계산한 날보다 <b>26일 앞</b>에, 후행스팬은 <b>26일 뒤</b>에 그려요.</li>
    <li>설정 9·26·52는 일목산인(호소다 고이치)이 1969년 책으로 공개한 값이에요.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">일목균형표 다섯 선 공식</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">88일째 값 직접 계산해 보기</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">구름대 보는 법: 위·안·아래</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MACD·이동평균선과 신호 순서 비교</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">일목균형표가 틀리는 경우 3가지</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">일목균형표 Q&amp;A 5개</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">일목균형표 다섯 선 공식</h2>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">선</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">그리는 칸</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">전환선</td><td style="border:1px solid #ddd;padding:8px;">(최근 9일 최고가 + 최저가) ÷ 2</td><td style="border:1px solid #ddd;padding:8px;">오늘</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기준선</td><td style="border:1px solid #ddd;padding:8px;">(최근 26일 최고가 + 최저가) ÷ 2</td><td style="border:1px solid #ddd;padding:8px;">오늘</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;"><mark>선행스팬1</mark></td><td style="border:1px solid #ddd;padding:8px;">(전환선 + 기준선) ÷ 2</td><td style="border:1px solid #ddd;padding:8px;"><b>26일 앞</b></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;"><mark>선행스팬2</mark></td><td style="border:1px solid #ddd;padding:8px;">(최근 52일 최고가 + 최저가) ÷ 2</td><td style="border:1px solid #ddd;padding:8px;"><b>26일 앞</b></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">후행스팬</td><td style="border:1px solid #ddd;padding:8px;">오늘 종가 그대로</td><td style="border:1px solid #ddd;padding:8px;"><b>26일 뒤</b></td></tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/ichimoku-cloud-calculation-2.png" alt="일목균형표 선이 그려지는 위치: 후행스팬은 26일 전, 전환선·기준선은 오늘, 선행스팬은 26일 후" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산은 모두 오늘 하지만, 구름은 26일 앞에 그려서 차트 오른쪽 빈칸까지 이어져요.</figcaption></figure>

<p>전환선과 기준선은 기간만 다를 뿐 같은 방식이라, 짧은 이동평균선과 긴 이동평균선의 관계와 비슷해요. 종가 평균으로 계산하는 방식은 <a href="https://sensitiveboss3.tistory.com/entry/moving-average-5-20-day-cross" target="_blank" rel="noopener">이동평균선 5일 20일 계산과 크로스 보는 법</a>에서 비교해 볼 수 있어요.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">88일째 값 직접 계산해 보기</h2>

<p>아래 예시 가격(가정값)에서 오르기 시작한 지 일주일쯤 된 88일째를 손으로 계산해 볼게요. 필요한 건 기간별 최고가·최저가뿐이에요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">항목</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">값</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">전환선(9일)</td><td style="border:1px solid #ddd;padding:8px;">(10,440 + 9,790) ÷ 2</td><td style="border:1px solid #ddd;padding:8px;">10,115</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기준선(26일)</td><td style="border:1px solid #ddd;padding:8px;">(10,440 + 9,740) ÷ 2</td><td style="border:1px solid #ddd;padding:8px;">10,090</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">선행스팬1</td><td style="border:1px solid #ddd;padding:8px;">(10,115 + 10,090) ÷ 2 → <b>114일째 칸</b>에 그림</td><td style="border:1px solid #ddd;padding:8px;">10,102.5</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">선행스팬2(52일)</td><td style="border:1px solid #ddd;padding:8px;">(10,940 + 9,740) ÷ 2 → <b>114일째 칸</b>에 그림</td><td style="border:1px solid #ddd;padding:8px;">10,340</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">후행스팬</td><td style="border:1px solid #ddd;padding:8px;">88일째 종가 10,310 → <b>62일째 칸</b>에 그림</td><td style="border:1px solid #ddd;padding:8px;">10,310</td></tr>
  </tbody>
</table>

<p>이날 <mark>전환선(10,115)이 기준선(10,090)을 처음 넘었고</mark>, 후행스팬(10,310)도 26일 전 종가(10,260) 위로 올라섰어요. 하지만 88일째 칸에 걸린 구름은 26일 전에 계산된 10,468~10,835라서, 종가 10,310은 <b>아직 구름 아래</b>예요. 단기 균형은 바뀌었는데 큰 균형은 아직 안 바뀐 상태예요.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">구름대 보는 법: 위·안·아래</h2>

<p>145일 전체를 계산하면 아래 그림이 나와요. 가격은 80일째까지 천천히 내리다가 81일째부터 오르고, 110일째쯤부터 옆으로 흔들리게 만든 가정값이에요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/ichimoku-cloud-calculation-1.png" alt="가정 가격 145일의 일목균형표: 종가, 전환선, 기준선, 후행스팬, 구름과 신호 네 곳" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">초록 구름은 선행스팬1이 위, 분홍 구름은 선행스팬2가 위예요. 오른쪽 회색 칸이 26일 앞에 미리 그려진 구름이에요.</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">표시</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">날</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">무슨 일</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">종가 / 그날 구름</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">①</td><td style="border:1px solid #ddd;padding:8px;">88일째</td><td style="border:1px solid #ddd;padding:8px;">전환선이 기준선 위로, 후행스팬도 위로</td><td style="border:1px solid #ddd;padding:8px;">10,310 / 구름 아래</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">②</td><td style="border:1px solid #ddd;padding:8px;">95일째</td><td style="border:1px solid #ddd;padding:8px;">종가가 구름 위로 올라섬</td><td style="border:1px solid #ddd;padding:8px;">10,800 / 10,305~10,680</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">③</td><td style="border:1px solid #ddd;padding:8px;">126일째</td><td style="border:1px solid #ddd;padding:8px;">전환선이 기준선 아래로</td><td style="border:1px solid #ddd;padding:8px;">11,300 / 구름 위</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">④</td><td style="border:1px solid #ddd;padding:8px;">137일째</td><td style="border:1px solid #ddd;padding:8px;">종가가 구름 안으로 들어옴</td><td style="border:1px solid #ddd;padding:8px;">11,090 / 10,745~11,198</td></tr>
  </tbody>
</table>

<ul style="line-height:1.9;">
  <li><b>구름 위:</b> 지난 26일·52일의 가운데 값보다 지금 가격이 높다는 뜻이에요. 예시의 95~136일째가 여기예요.</li>
  <li><b>구름 안:</b> 오름과 내림의 균형이 맞서는 구간이에요. 구름이 두꺼울수록 빠져나가는 데 가격이 더 움직여야 해요.</li>
  <li><b>구름 아래:</b> 큰 흐름이 아직 내림 쪽이라는 뜻이에요.</li>
  <li><b>구름 색이 바뀌는 곳</b>(선행스팬1과 2가 엇갈리는 곳)은 예시에서 119일째 칸이었어요. 이 값은 93일째에 계산된 것이라 26일 전에 미리 보였어요.</li>
</ul>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">MACD·이동평균선과 신호 순서 비교</h2>

<p>같은 145일 가격으로 다른 지표도 계산해서, 오르기 시작할 때 신호가 나온 순서를 비교했어요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/ichimoku-cloud-calculation-3.png" alt="같은 가격에서 MACD 시그널 교차 81일째, 5·20일 골든크로스 85일째, 전환선 기준선 교차 88일째, 구름 돌파 95일째" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">구름 돌파는 가장 늦었지만, 그 전 내림 구간에서 가짜 신호가 없었어요.</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">지표</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">오를 때 신호</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">꺾일 때 신호</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">61~80일째 내림 구간 가짜 교차</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">MACD·시그널 교차</td><td style="border:1px solid #ddd;padding:8px;">81일째(9,960원)</td><td style="border:1px solid #ddd;padding:8px;">113일째</td><td style="border:1px solid #ddd;padding:8px;"><mark>10번</mark></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5·20일 이평 교차</td><td style="border:1px solid #ddd;padding:8px;">85일째(10,200원)</td><td style="border:1px solid #ddd;padding:8px;">120일째</td><td style="border:1px solid #ddd;padding:8px;">0번</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">전환선·기준선 교차</td><td style="border:1px solid #ddd;padding:8px;">88일째(10,310원)</td><td style="border:1px solid #ddd;padding:8px;">126일째</td><td style="border:1px solid #ddd;padding:8px;">0번</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">구름 돌파·진입</td><td style="border:1px solid #ddd;padding:8px;">95일째(10,800원)</td><td style="border:1px solid #ddd;padding:8px;">137일째(구름 안)</td><td style="border:1px solid #ddd;padding:8px;">0번(구름은 78일째부터 생김)</td></tr>
  </tbody>
</table>

<p>빠른 신호는 일찍 알려 주는 대신 흔들림에 자주 속고, 느린 신호는 덜 속는 대신 늦어요. 구름 돌파 날(10,800원)은 MACD 신호 날(9,960원)보다 840원(약 8%) 높은 곳이었어요. MACD 계산 과정은 <a href="https://sensitiveboss3.tistory.com/entry/macd-calculation-signal-line" target="_blank" rel="noopener">MACD 보는법과 계산법</a>에 따로 정리했어요.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">일목균형표가 틀리는 경우 3가지</h2>

<ol style="line-height:1.9;">
  <li><b>옆으로 흔들릴 때 구름 안에 오래 갇혀요.</b> 예시의 137일째 이후처럼 가격이 구름 안을 들락날락하면 위·아래 판단이 하루 만에 바뀌어요.</li>
  <li><b>급하게 움직이면 늦어요.</b> 52일 가운데 값을 쓰는 선행스팬2는 짧은 급등락을 거의 따라가지 못해요. 예시에서도 구름 돌파는 바닥(79일째)보다 16거래일 늦었어요.</li>
  <li><b>최고가·최저가 하루가 선을 크게 바꿔요.</b> 평균이 아니라 가운데 값이라, 하루짜리 큰 꼬리 하나가 9일·26일·52일 동안 선을 끌고 다녀요. 반대로 그 날이 기간 밖으로 빠지는 날에 선이 갑자기 꺾여요.</li>
</ol>

<p>과열 정도처럼 0~100으로 보는 지표가 필요하면 <a href="https://sensitiveboss3.tistory.com/entry/rsi-meaning-14day-calculation" target="_blank" rel="noopener">RSI 14일 값 직접 구하기</a>를 함께 보면 서로 빈자리를 채워요.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2f6f4f;padding-left:12px;margin-top:36px;">일목균형표 Q&amp;A 5개</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">일목균형표 계산 공식은 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">전환선은 9일, 기준선은 26일 동안의 최고가와 최저가를 더해 2로 나눈 값이에요. 선행스팬1은 전환선과 기준선의 평균, 선행스팬2는 52일 최고가와 최저가의 가운데 값이고 둘 다 26일 앞에 그려요. 후행스팬은 오늘 종가를 26일 뒤에 그려요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">일목균형표 구름대는 어떻게 보나요</summary>
  <p style="margin:10px 0 0 0;">선행스팬1과 2 사이를 칠한 것이 구름이에요. 가격이 구름 위에 있으면 오름 쪽, 아래면 내림 쪽, 안에 있으면 균형이 맞서는 구간으로 읽어요. 구름이 두꺼울수록 빠져나가는 데 가격이 더 움직여야 해요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">구름이 왜 차트 오른쪽 빈칸까지 그려지나요</summary>
  <p style="margin:10px 0 0 0;">선행스팬은 오늘 계산한 값을 26일 앞 칸에 그리기 때문이에요. 그래서 앞으로 26일 동안 가격이 지나갈 구름이 미리 보이고, 구름 색이 바뀌는 지점도 미리 알 수 있어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">일목균형표 설정 9, 26, 52는 바꿔도 되나요</summary>
  <p style="margin:10px 0 0 0;">바꿀 수 있어요. 9·26·52는 일목산인이 공개한 기본값이고, 기간을 줄이면 신호가 빨라지는 대신 흔들림에 더 자주 반응해요. 앱마다 바꾼 설정이 저장돼 있을 수 있어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">일목균형표와 이동평균선은 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">이동평균선은 종가를 더해 나눈 평균이고, 일목균형표의 전환선·기준선은 기간 중 최고가와 최저가의 가운데 값이에요. 그래서 큰 꼬리가 있는 날의 영향을 더 크게 받고, 그날이 기간 밖으로 빠질 때 선이 갑자기 꺾여요.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://en.wikipedia.org/wiki/Ichimoku_Kink%C5%8D_Hy%C5%8D" target="_blank" rel="noopener">Wikipedia: Ichimoku Kinkō Hyō</a></li>
    <li><a href="https://help.ctrader.com/indicators/built-in/other/ichimoku-kinko-hyo/" target="_blank" rel="noopener">cTrader: Ichimoku Kinko Hyo(1969년 공개, 9·26·52)</a></li>
    <li><a href="https://backtrader.readthedocs.io/en/latest/api/indicators/backtrader.indicators.ichimoku.html" target="_blank" rel="noopener">backtrader: Ichimoku 지표 정의</a></li>
    <li>본문 계산: 가정 가격 145일(고가·저가·종가)로 직접 계산(실제 종목·시세 아님).</li>
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
  "headline": "일목균형표 보는법과 계산, 구름대·전환선·기준선 한 번에",
  "description": "일목균형표 다섯 선(전환선·기준선·선행스팬1·2·후행스팬) 공식과 그리는 위치, 가정 가격 145일로 직접 계산한 구름대 읽는 법, MACD·이동평균선과 신호 순서 비교, 틀리는 경우 3가지를 정리했어요.",
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
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/ichimoku-cloud-calculation-1.png",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/ichimoku-cloud-calculation"
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
      "name": "일목균형표 계산 공식은 무엇인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "전환선은 9일, 기준선은 26일 동안의 최고가와 최저가를 더해 2로 나눈 값이에요. 선행스팬1은 전환선과 기준선의 평균, 선행스팬2는 52일 최고가와 최저가의 가운데 값이고 둘 다 26일 앞에 그려요. 후행스팬은 오늘 종가를 26일 뒤에 그려요."
      }
    },
    {
      "@type": "Question",
      "name": "일목균형표 구름대는 어떻게 보나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "선행스팬1과 2 사이를 칠한 것이 구름이에요. 가격이 구름 위에 있으면 오름 쪽, 아래면 내림 쪽, 안에 있으면 균형이 맞서는 구간으로 읽어요. 구름이 두꺼울수록 빠져나가는 데 가격이 더 움직여야 해요."
      }
    },
    {
      "@type": "Question",
      "name": "구름이 왜 차트 오른쪽 빈칸까지 그려지나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "선행스팬은 오늘 계산한 값을 26일 앞 칸에 그리기 때문이에요. 그래서 앞으로 26일 동안 가격이 지나갈 구름이 미리 보이고, 구름 색이 바뀌는 지점도 미리 알 수 있어요."
      }
    },
    {
      "@type": "Question",
      "name": "일목균형표 설정 9, 26, 52는 바꿔도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "바꿀 수 있어요. 9·26·52는 일목산인이 공개한 기본값이고, 기간을 줄이면 신호가 빨라지는 대신 흔들림에 더 자주 반응해요. 앱마다 바꾼 설정이 저장돼 있을 수 있어요."
      }
    },
    {
      "@type": "Question",
      "name": "일목균형표와 이동평균선은 뭐가 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이동평균선은 종가를 더해 나눈 평균이고, 일목균형표의 전환선·기준선은 기간 중 최고가와 최저가의 가운데 값이에요. 그래서 큰 꼬리가 있는 날의 영향을 더 크게 받고, 그날이 기간 밖으로 빠질 때 선이 갑자기 꺾여요."
      }
    }
  ]
}
</script>
