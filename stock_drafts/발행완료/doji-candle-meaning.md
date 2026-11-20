---
keyword: 도지캔들
title: 도지캔들 뜻과 종류, 몸통 비율 계산으로 십자형·잠자리형·비석형 구분하기 (5%·10% 기준 비교)
slug: doji-candle-meaning
track: chart
theme: plum
thumb_style: pop
thumb_title: 도지캔들 구분법|몸통 비율 계산
thumb_note: 5%·10% 기준 비교
thumb_art: chart
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 660 (PC 180 / 모바일 480)
gate1_pass: true (2026-11-13 실측)
serp_check: |
  [2026-11-16] 상위는 FX·코인 교육 페이지·트레이딩뷰 아이디어·해외 번역글. 모양 설명과 종류 소개는 많지만, 몸통 비율·꼬리 비율을
  숫자로 계산해 종류를 나누고, 정해진 기준이 없어 5%·10%에 따라 판정이 갈리는 경우와 몸통 10원인데 도지가 아닌 경우를 보여 주는 글은 드묾.
unique_asset: |
  (a) 낱말 풀이, (b) 캔들 A 몸통 비율 2.5% 따라 하기와 꼬리 190·200원, (c) 가정 캔들 4개 꼬리 비율 표(잠자리형 아랫꼬리 97.6%, 비석형 윗꼬리 97.6%),
  (d) 캔들 E 8.3%가 5% 기준이면 아님·10% 기준이면 도지, (e) 몸통 10원 A(폭 400원, 2.5%) vs G(폭 30원, 33.3%), (f) 해석 순서 4단계, (g) 오해 5가지.
primary_source: |
  도지 정의(시가≈종가, 몸통 거의 없음)와 종류(십자형·긴 다리·잠자리형·비석형), 약한 신호·확인 필요: The Right Trader·CFI·Capital.com·EBC 일치.
  몸통 비율 % 기준은 자료에서 공통 숫자를 찾지 못해 '정해진 숫자 없음'으로 쓰고, 5%·10%는 비교용 가정이라고 본문에 명시.
  예시는 가정값(assets/figures/doji-candle-meaning-data.py).
기준일: 2026-11-16
tags: 도지캔들, 도지캔들 뜻, 잠자리형 도지, 비석형 도지, 캔들 패턴, 십자형 캔들
gate_pass: true
gate_pass_note: |
  게이트1 660 통과. 게이트2 몸통·꼬리 비율 계산과 기준별 판정 비교로 정보이득. 게이트4 정의는 교육 자료 일치, 예시는 가정값.
self_check: |
  [2026-11-16] 차트·지표 편(생활정보 2편 뒤, 국가장학금은 2027-1학기 1차 공식 일정 여전히 미확인으로 보류). plum 테마, 팝 그림 3장 + 캐러셀 6장.
  반전 '가능성'으로만 쓰고 매매 신호처럼 쓰지 않음. 강조는 span 배경색. 내부 링크·함께 보면 좋은 글 3개(이동평균선·볼린저밴드·RSI, 발행 글).
refresh_due: 2027-05-16
refresh_reason: "서치 콘솔 검색어 반영, 차트 보는법 편 발행 후 서로 링크"
figure_plan: "3장(팝·plum): 1 가정 캔들 6개와 몸통 비율 / 2 캔들 E 5%·10% 기준 비교 카드 / 3 몸통 10원 A vs G 캔들 + 요약 캐러셀 6장"
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-11-16</p>

<p>도지캔들은 <span style="background-color:#fff3a3;padding:0 2px;">시가와 종가가 거의 같아서 몸통이 선처럼 얇은 캔들</span>이에요. 하루 동안 오르내렸지만 결국 시작한 가격 근처에서 끝난 날이라, 사려는 힘과 팔려는 힘이 비슷했던 날로 읽어요.</p>

<p>그런데 "거의 같다"는 게 몇 원 차이까지인지는 정해져 있지 않아요. 몸통 비율을 직접 계산해 도지 종류를 구분하고, 같은 캔들이 기준에 따라 도지가 되기도 하고 안 되기도 하는 경우까지 가정 캔들로 볼게요.</p>

<div style="background:#f7f4fb;border:2px solid #2d1e4a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2d1e4a;font-size:18px;">🕯 한눈에 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>뜻:</b> 시가 ≈ 종가, 몸통이 아주 얇은 캔들</li>
    <li><b>계산:</b> 몸통 비율 = |종가 − 시가| ÷ (고가 − 저가) × 100</li>
    <li><b>종류:</b> 꼬리 위치로 십자형·긴 다리·잠자리형·비석형</li>
    <li><b>기준:</b> 몇 % 이하가 도지인지 정해진 숫자는 없어요</li>
    <li><b>해석:</b> 혼자서는 방향을 알려 주지 않는 약한 신호</li>
  </ul>
</div>

<div style="margin:24px 0;"><div style="display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding-bottom:8px;"><div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/carousel/doji-candle-meaning-01.png" alt="도지캔들 숫자로 구분하기: 몸통 ÷ 하루 폭 × 100" style="width:100%;border-radius:14px;display:block;"></div><div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/carousel/doji-candle-meaning-02.png" alt="몸통 비율 계산 예시 2.5%" style="width:100%;border-radius:14px;display:block;"></div><div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/carousel/doji-candle-meaning-03.png" alt="잠자리형·비석형·십자형 꼬리 비율" style="width:100%;border-radius:14px;display:block;"></div><div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/carousel/doji-candle-meaning-04.png" alt="같은 캔들도 5%·10% 기준에 따라 판정이 갈리는 예시" style="width:100%;border-radius:14px;display:block;"></div><div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/carousel/doji-candle-meaning-05.png" alt="몸통 10원이어도 하루 폭이 작으면 도지가 아닌 예시" style="width:100%;border-radius:14px;display:block;"></div><div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/carousel/doji-candle-meaning-06.png" alt="도지캔들 해석 주의점" style="width:100%;border-radius:14px;display:block;"></div></div><p style="font-size:13px;color:#888;margin:6px 0 0 0;">옆으로 넘겨 보세요 → (카드 6장 요약)</p></div>

<div style="background:#fbf8f1;border:1px dashed #b8a98f;border-radius:10px;padding:14px 18px;margin:20px 0;">
  <strong style="font-size:16px;">📖 처음이라면 이것만 — 낱말 풀이</strong>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>시가·종가:</b> 그날 처음 거래된 가격과 마지막 가격.</li>
    <li><b>고가·저가:</b> 그날 가장 높았던 가격과 가장 낮았던 가격.</li>
    <li><b>몸통(실체):</b> 시가와 종가 사이의 굵은 막대. 양봉(빨강)은 종가가 높고, 음봉(파랑)은 시가가 높아요.</li>
    <li><b>꼬리(그림자):</b> 몸통 위아래로 튀어나온 가는 선. 고가·저가까지 갔다가 돌아온 흔적이에요.</li>
    <li><b>하루 폭:</b> 고가 − 저가. 이 글에서 비율을 계산할 때 기준으로 써요.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">도지캔들은 무엇인가요?</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">도지인지 어떻게 계산하나요?</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">도지캔들 종류는 어떻게 구분하나요?</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">몇 % 이하면 도지인가요?</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">몸통이 작으면 무조건 도지인가요?</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">도지캔들이 나오면 어떻게 읽어야 하나요?</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">자주 하는 오해 5가지</a></li>
  <li><a href="#sec-8" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">도지캔들 Q&amp;A 5개</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">도지캔들은 무엇인가요?</h2>

<p>도지캔들은 <span style="background-color:#fff3a3;padding:0 2px;">시가와 종가가 거의 같아 몸통이 거의 없는 캔들</span>이에요. 하루 동안 가격이 위아래로 움직였더라도 마지막에 시작 가격 근처로 돌아왔다는 뜻이에요.</p>

<p>보통 캔들은 몸통 길이로 그날 누가 이겼는지를 보여 줘요. 종가가 시가보다 많이 높으면 긴 양봉, 많이 낮으면 긴 음봉이죠. 도지는 몸통이 거의 없으니 "이긴 쪽이 없는 날"이에요. 그래서 여러 자료가 도지를 사려는 힘과 팔려는 힘이 팽팽한 상태, 또는 방향이 정해지지 않은 상태로 설명해요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#2d1e4a;color:#fff;"><th style="border:1px solid #ddd;padding:8px;">구분</th><th style="border:1px solid #ddd;padding:8px;">몸통</th><th style="border:1px solid #ddd;padding:8px;">읽는 법</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">긴 양봉</td><td style="border:1px solid #ddd;padding:8px;">길고 빨강</td><td style="border:1px solid #ddd;padding:8px;">종가가 시가보다 크게 높음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">긴 음봉</td><td style="border:1px solid #ddd;padding:8px;">길고 파랑</td><td style="border:1px solid #ddd;padding:8px;">종가가 시가보다 크게 낮음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">도지</td><td style="border:1px solid #ddd;padding:8px;">거의 없음</td><td style="border:1px solid #ddd;padding:8px;">시가와 종가가 거의 같음</td></tr>
  </tbody>
</table>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">도지인지 어떻게 계산하나요?</h2>

<p>도지인지는 <span style="background-color:#fff3a3;padding:0 2px;">몸통 길이를 하루 폭(고가 − 저가)으로 나눈 비율</span>로 재요. 몸통이 몇 원인지보다, 그날 움직인 폭에서 몸통이 얼마나 차지하는지가 중요해요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/doji-candle-meaning-1.png" alt="가정 캔들 6개의 몸통 비율: A 십자형 2.5%, B 잠자리형 0%, C 비석형 1.2%, D 긴 다리 2.0%, E 경계 8.3%, F 양봉 71.4%" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산을 보여 주기 위한 가정 캔들이에요. 실제 종목이 아니에요.</figcaption></figure>

<div style="background:#f7f4fb;border-radius:10px;padding:14px 18px;margin:20px 0;line-height:2;">
  <strong>✍️ 따라 해 보기 (캔들 A: 시가 10,000 · 고가 10,200 · 저가 9,800 · 종가 10,010)</strong><br>
  ① 몸통: |10,010 − 10,000| = <b>10원</b><br>
  ② 하루 폭: 10,200 − 9,800 = <b>400원</b><br>
  ③ 몸통 비율: 10 ÷ 400 × 100 = <span style="background-color:#fff3a3;padding:0 2px;"><b>2.5%</b></span><br>
  ④ 꼬리: 윗꼬리 10,200 − 10,010 = 190원 · 아랫꼬리 10,000 − 9,800 = 200원 → 위아래가 비슷
</div>

<p>④의 꼬리 계산이 다음 장에서 종류를 나누는 기준이 돼요. 윗꼬리는 고가에서 몸통 위쪽까지, 아랫꼬리는 몸통 아래쪽에서 저가까지의 길이예요.</p>

<p>음봉도 계산은 똑같아요. 캔들 C는 시가 10,000원, 종가 9,995원으로 5원 내린 음봉이에요. 몸통은 |9,995 − 10,000| = 5원이고, 하루 폭은 10,400 − 9,990 = 410원이라 몸통 비율은 약 1.2%예요. 절댓값을 쓰기 때문에 오른 날이든 내린 날이든 몸통 길이만 보고 비교할 수 있어요. 시가와 종가가 완전히 같은 캔들 B는 몸통이 0원이라 비율도 0%이고, 차트에서는 가로줄 하나로 보여요.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">도지캔들 종류는 어떻게 구분하나요?</h2>

<p>도지 종류는 <span style="background-color:#fff3a3;padding:0 2px;">꼬리가 어느 쪽으로 길게 뻗었는지</span>로 나눠요. 꼬리 길이도 하루 폭에 대한 비율로 보면 헷갈리지 않아요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#2d1e4a;color:#fff;"><th style="border:1px solid #ddd;padding:8px;">캔들</th><th style="border:1px solid #ddd;padding:8px;">이름</th><th style="border:1px solid #ddd;padding:8px;">몸통 비율</th><th style="border:1px solid #ddd;padding:8px;">윗꼬리</th><th style="border:1px solid #ddd;padding:8px;">아랫꼬리</th><th style="border:1px solid #ddd;padding:8px;">모양</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">A</td><td style="border:1px solid #ddd;padding:8px;">십자형</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td><td style="border:1px solid #ddd;padding:8px;">47.5%</td><td style="border:1px solid #ddd;padding:8px;">50.0%</td><td style="border:1px solid #ddd;padding:8px;">+ 모양, 위아래 비슷</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">D</td><td style="border:1px solid #ddd;padding:8px;">긴 다리 도지</td><td style="border:1px solid #ddd;padding:8px;">2.0%</td><td style="border:1px solid #ddd;padding:8px;">48.0%</td><td style="border:1px solid #ddd;padding:8px;">50.0%</td><td style="border:1px solid #ddd;padding:8px;">폭 1,000원, 위아래 모두 김</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">B</td><td style="border:1px solid #ddd;padding:8px;">잠자리형</td><td style="border:1px solid #ddd;padding:8px;">0%</td><td style="border:1px solid #ddd;padding:8px;">2.4%</td><td style="border:1px solid #ddd;padding:8px;"><b>97.6%</b></td><td style="border:1px solid #ddd;padding:8px;">T자, 아랫꼬리만 김</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">C</td><td style="border:1px solid #ddd;padding:8px;">비석형</td><td style="border:1px solid #ddd;padding:8px;">1.2%</td><td style="border:1px solid #ddd;padding:8px;"><b>97.6%</b></td><td style="border:1px solid #ddd;padding:8px;">1.2%</td><td style="border:1px solid #ddd;padding:8px;">뒤집힌 T자, 윗꼬리만 김</td></tr>
  </tbody>
</table>

<p>잠자리형(B)은 장중에 크게 내려갔다가 시가 근처까지 다시 올라온 날이고, 비석형(C)은 반대로 크게 올라갔다가 시가 근처로 밀려 내려온 날이에요. 자료들은 잠자리형을 하락 뒤에 나오면 반등 가능성, 비석형을 상승 뒤에 나오면 하락 가능성으로 해석하는 경우가 많지만, 어디까지나 '가능성'이에요.</p>

<p>긴 다리 도지(D)는 십자형과 모양은 같은데 하루 폭이 훨씬 커요. 그날 위아래로 크게 흔들렸다는 점이 다르죠.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">몇 % 이하면 도지인가요?</h2>

<p><span style="background-color:#fff3a3;padding:0 2px;">정해진 숫자가 없어요.</span> 몸통 비율이 몇 % 이하여야 도지라는 공통 기준은 찾을 수 없었고, 자료마다 "아주 작은 몸통" 정도로만 설명해요. 그래서 기준을 어디에 두느냐에 따라 같은 캔들이 도지가 되기도 하고 안 되기도 해요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/doji-candle-meaning-2.png" alt="캔들 E 몸통 비율 8.3%: 5% 기준이면 도지 아님, 10% 기준이면 도지" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">이 글에서는 비교를 위해 5%와 10% 두 기준을 가정했어요.</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#2d1e4a;color:#fff;"><th style="border:1px solid #ddd;padding:8px;">캔들</th><th style="border:1px solid #ddd;padding:8px;">몸통 비율</th><th style="border:1px solid #ddd;padding:8px;">5% 기준</th><th style="border:1px solid #ddd;padding:8px;">10% 기준</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">A 십자형</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td><td style="border:1px solid #ddd;padding:8px;">도지</td><td style="border:1px solid #ddd;padding:8px;">도지</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">C 비석형</td><td style="border:1px solid #ddd;padding:8px;">1.2%</td><td style="border:1px solid #ddd;padding:8px;">도지</td><td style="border:1px solid #ddd;padding:8px;">도지</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">E 경계</td><td style="border:1px solid #ddd;padding:8px;">8.3%</td><td style="border:1px solid #ddd;padding:8px;"><b>도지 아님</b></td><td style="border:1px solid #ddd;padding:8px;"><b>도지</b></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">F 양봉</td><td style="border:1px solid #ddd;padding:8px;">71.4%</td><td style="border:1px solid #ddd;padding:8px;">아님</td><td style="border:1px solid #ddd;padding:8px;">아님</td></tr>
  </tbody>
</table>

<p>HTS의 캔들 패턴 자동 찾기 기능도 증권사마다 기준이 다를 수 있어요. 그래서 "도지가 떴다"는 말을 들으면 어떤 기준으로 찾은 건지부터 보는 게 좋아요. 직접 볼 때는 내 기준(예: 5% 이하)을 하나 정해 두고 같은 기준으로만 비교하면 헷갈리지 않아요. 기준을 바꿀 때는 지난 몇 달 차트에서 그 기준으로 도지가 몇 번 나왔는지 세어 보면, 너무 자주 잡히는지 너무 드문지 감을 잡을 수 있어요.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">몸통이 작으면 무조건 도지인가요?</h2>

<p>아니에요. <span style="background-color:#fff3a3;padding:0 2px;">몸통이 10원이어도 하루 폭이 작으면 도지가 아니에요.</span> 비율로 보면 전혀 다른 캔들이거든요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/doji-candle-meaning-3.png" alt="몸통이 둘 다 10원이지만 캔들 A는 하루 폭 400원으로 몸통 비율 2.5%, 캔들 G는 하루 폭 30원으로 33.3%" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">몸통 크기는 원이 아니라 하루 폭 대비 비율로 봐요.</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#2d1e4a;color:#fff;"><th style="border:1px solid #ddd;padding:8px;">캔들</th><th style="border:1px solid #ddd;padding:8px;">몸통</th><th style="border:1px solid #ddd;padding:8px;">하루 폭</th><th style="border:1px solid #ddd;padding:8px;">몸통 비율</th><th style="border:1px solid #ddd;padding:8px;">판정</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">A</td><td style="border:1px solid #ddd;padding:8px;">10원</td><td style="border:1px solid #ddd;padding:8px;">400원</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td><td style="border:1px solid #ddd;padding:8px;">도지</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">G</td><td style="border:1px solid #ddd;padding:8px;">10원</td><td style="border:1px solid #ddd;padding:8px;">30원</td><td style="border:1px solid #ddd;padding:8px;"><b>33.3%</b></td><td style="border:1px solid #ddd;padding:8px;">도지 아님</td></tr>
  </tbody>
</table>

<p>G는 하루 종일 거의 움직이지 않은 날이에요. 몸통이 작아 보여도 그날 움직인 폭의 3분의 1이 몸통이라, 시가와 종가가 "거의 같다"고 보기 어려워요. 거래가 적은 종목이나 장이 조용한 날에 이런 캔들이 자주 나와요.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">도지캔들이 나오면 어떻게 읽어야 하나요?</h2>

<p>도지캔들은 <span style="background-color:#fff3a3;padding:0 2px;">혼자서는 방향을 알려 주지 않는 약한 신호</span>로 보는 게 안전해요. 여러 자료가 도지를 확인이 필요한 신호로 설명하고, 다음 날 캔들과 그전까지의 추세를 함께 보라고 해요.</p>

<ol style="line-height:2;">
  <li><b>앞의 흐름 보기:</b> 계속 오르던 중인지, 내리던 중인지, 옆으로 가던 중인지 확인해요.</li>
  <li><b>위치 보기:</b> 이동평균선이나 볼린저밴드 같은 기준선 근처인지 봐요.</li>
  <li><b>다음 캔들 보기:</b> 다음 날 어느 쪽으로 몸통이 생기는지 확인해요.</li>
  <li><b>거래량 보기:</b> 평소보다 거래가 많았는지 적었는지 봐요.</li>
</ol>

<p>추세를 보는 기준선은 <a href="https://sensitiveboss3.tistory.com/entry/moving-average-5-20-day-cross" target="_blank" rel="noopener">이동평균선 5일 20일 계산과 크로스 보는 법</a>, 변동 폭을 보는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/bollinger-bands-calculation" target="_blank" rel="noopener">볼린저밴드 뜻과 계산법</a>, 오른 힘과 내린 힘을 비교하는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/rsi-meaning-14day-calculation" target="_blank" rel="noopener">RSI 뜻과 14일 값 직접 구하기</a>에서 볼 수 있어요.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">자주 하는 오해 5가지</h2>

<p>도지캔들에서 생기는 오해는 대부분 <span style="background-color:#fff3a3;padding:0 2px;">모양 하나로 결론을 내리는 데서</span> 생겨요.</p>

<div style="background:#fff4f1;border:2px solid #ff6f59;border-radius:10px;padding:14px 18px;margin:20px 0;">
  <strong style="font-size:16px;">⚠️ 이것만 피하세요</strong>
  <ol style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>도지가 나오면 반드시 방향이 바뀐다고 생각하기</b> → 혼자서는 약한 신호예요. 다음 캔들을 봐야 해요.</li>
    <li><b>몸통 원 단위로만 보기</b> → 몸통 10원도 하루 폭이 30원이면 33.3%예요.</li>
    <li><b>기준 없이 눈대중으로 판단하기</b> → 같은 8.3% 캔들도 기준에 따라 갈려요.</li>
    <li><b>잠자리형·비석형을 꼬리 길이 확인 없이 부르기</b> → 꼬리가 하루 폭의 대부분인지 계산해 보세요.</li>
    <li><b>거래가 적은 날 캔들도 같은 무게로 보기</b> → 조용한 날의 작은 캔들은 의미가 약해요.</li>
  </ol>
</div>

<h2 id="sec-8" style="scroll-margin-top:72px;border-left:6px solid #2d1e4a;padding-left:12px;margin-top:36px;">도지캔들 Q&amp;A 5개</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">도지캔들 뜻이 뭔가요</summary>
  <p style="margin:10px 0 0 0;">도지캔들은 시가와 종가가 거의 같아서 몸통이 선처럼 얇은 캔들이에요. 하루 동안 오르내렸지만 시작한 가격 근처에서 끝났다는 뜻이라, 사려는 힘과 팔려는 힘이 비슷했던 날로 읽어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">도지캔들인지 어떻게 계산하나요</summary>
  <p style="margin:10px 0 0 0;">몸통 비율 = |종가 − 시가| ÷ (고가 − 저가) × 100으로 구해요. 시가 10,000원, 종가 10,010원, 고가 10,200원, 저가 9,800원이면 10 ÷ 400 × 100 = 2.5%예요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">몸통 비율이 몇 % 이하면 도지인가요</summary>
  <p style="margin:10px 0 0 0;">정해진 숫자는 없어요. 자료마다 기준이 달라서, 같은 8.3% 캔들도 5% 기준이면 도지가 아니고 10% 기준이면 도지예요. 내가 쓸 기준을 먼저 정해 두는 게 좋아요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">잠자리형과 비석형은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">잠자리형은 아랫꼬리가 길고 윗꼬리가 거의 없는 T자 모양이고, 비석형은 반대로 윗꼬리가 길고 아랫꼬리가 거의 없는 뒤집힌 T자 모양이에요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">도지캔들이 나오면 추세가 바뀌나요</summary>
  <p style="margin:10px 0 0 0;">도지만으로는 방향을 알 수 없어요. 여러 자료가 도지를 약한 신호로 보고, 다음 캔들과 추세를 함께 봐야 한다고 설명해요.</p>
</details>

<div style="background:#f6f7fb;border-radius:10px;padding:14px 18px;margin:28px 0 0 0;">
  <strong style="font-size:16px;">📚 함께 보면 좋은 글</strong>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;"><li><a href="https://sensitiveboss3.tistory.com/entry/moving-average-5-20-day-cross" target="_blank" rel="noopener">이동평균선 5일 20일 계산과 크로스 보는 법</a></li><li><a href="https://sensitiveboss3.tistory.com/entry/bollinger-bands-calculation" target="_blank" rel="noopener">볼린저밴드 뜻과 계산법</a></li><li><a href="https://sensitiveboss3.tistory.com/entry/rsi-meaning-14day-calculation" target="_blank" rel="noopener">RSI 뜻과 14일 값 직접 구하기</a></li></ul>
</div>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://therighttrader.com/ko/learn/candlestick-patterns/doji" target="_blank" rel="noopener">The Right Trader: 도지 캔들 패턴</a></li>
    <li><a href="https://corporatefinanceinstitute.com/resources/capital-markets/doji" target="_blank" rel="noopener">Corporate Finance Institute: Doji</a></li>
    <li><a href="https://capital.com/doji-definition" target="_blank" rel="noopener">Capital.com: What does Doji mean?</a></li>
    <li><a href="https://www.ebc.com/kr/forex/270318.html" target="_blank" rel="noopener">EBC: 도지 캔들이란?</a></li>
  </ul>
  기준일: 2026년 11월 16일. 예시 캔들은 계산을 보여 주기 위한 가정값이에요.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
정보 제공을 목적으로 쓴 글이며 특정 종목의 매수·매도를 권유하지 않아요. 예시는 계산을 보여 주기 위한 가정값이고, 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있어요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "도지캔들 뜻과 종류, 몸통 비율 계산으로 십자형·잠자리형·비석형 구분하기 (5%·10% 기준 비교)",
  "description": "도지캔들(시가와 종가가 거의 같은 캔들)의 뜻과 몸통 비율 계산법, 가정 캔들 7개로 십자형·잠자리형·비석형·긴 다리 도지를 구분하고, 5%·10% 기준에 따라 판정이 갈리는 경우와 몸통 10원이어도 도지가 아닌 경우, 해석할 때 주의점을 정리했어요.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Organization",
    "name": "센시티브보스"
  },
  "datePublished": "2026-11-16",
  "dateModified": "2026-11-16",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/doji-candle-meaning-1.png",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/doji-candle-meaning"
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
      "name": "도지캔들 뜻이 뭔가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "도지캔들은 시가와 종가가 거의 같아서 몸통이 선처럼 얇은 캔들이에요. 하루 동안 오르내렸지만 시작한 가격 근처에서 끝났다는 뜻이라, 사려는 힘과 팔려는 힘이 비슷했던 날로 읽어요."
      }
    },
    {
      "@type": "Question",
      "name": "도지캔들인지 어떻게 계산하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "몸통 비율 = |종가 − 시가| ÷ (고가 − 저가) × 100으로 구해요. 시가 10,000원, 종가 10,010원, 고가 10,200원, 저가 9,800원이면 10 ÷ 400 × 100 = 2.5%예요."
      }
    },
    {
      "@type": "Question",
      "name": "몸통 비율이 몇 % 이하면 도지인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 숫자는 없어요. 자료마다 기준이 달라서, 같은 8.3% 캔들도 5% 기준이면 도지가 아니고 10% 기준이면 도지예요. 내가 쓸 기준을 먼저 정해 두는 게 좋아요."
      }
    },
    {
      "@type": "Question",
      "name": "잠자리형과 비석형은 어떻게 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "잠자리형은 아랫꼬리가 길고 윗꼬리가 거의 없는 T자 모양이고, 비석형은 반대로 윗꼬리가 길고 아랫꼬리가 거의 없는 뒤집힌 T자 모양이에요."
      }
    },
    {
      "@type": "Question",
      "name": "도지캔들이 나오면 추세가 바뀌나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "도지만으로는 방향을 알 수 없어요. 여러 자료가 도지를 약한 신호로 보고, 다음 캔들과 추세를 함께 봐야 한다고 설명해요."
      }
    }
  ]
}
</script>
