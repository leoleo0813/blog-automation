---
keyword: 레버리지 ETF
title: 레버리지 ETF 횡보장 손실 계산표와 배수별 차이
slug: leverage-etf-sideways-loss-table
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 16850 (2026-09~10 실측, 레버리지 ETF)
gate1_pass: true (일반 주제 기준 월 500 이상, 월 5,000 이상이라 개념형도 허용)
serp_check: |
  [게이트2 v4 판정 2026-10-06 - 통과] WebSearch(미국 기준, 참고용) "레버리지 ETF 뜻 일간 수익률 2배 복리 효과 횡보장 손실 계산" 상위 9개: toss.im·tossbank.com(핀테크 콘텐츠) / kbthink.com 2건(KB 용어사전·이슈) / kcie.or.kr 2건(금융투자교육원) / samsungfundblog.com(운용사 블로그) / richinfohub.com·dglmoney.com(소규모 콘텐츠 사이트 2건).
  1) 진입 여지 - 있음. 소규모 콘텐츠 사이트 2건이 상위에 있고 월 5,000 이상 키워드는 게이트2 v4상 이 이유만으로 탈락시키지 않는다.
  2) 검색 의도 - 뜻과 위험을 묻는 정보 탐색. 시세 조회·계산기 실행이 아니다.
  3) 답 완결 - 아님. 상위 글은 100 → 110 → 100이면 98이 된다는 한 가지 2일 예시까지만 다루고, 일간 변동 폭과 배수별 20일 손실표, 손실이 변동 폭 제곱과 k(k-1)에 비례한다는 공식, 추세장에서 결과가 뒤집히는 비교는 확인하지 못함(검색 요약 기준, 전수 확인 아님).
unique_asset: |
  (a) 일간 변동 폭(±1·2·5·10%) x 배수(2·3배) 20일 손실 계산표와 원점 회복에 필요한 상승률.
  (b) 왕복 배율 공식 1 - k(k-1)r²/(1+r)로 손실이 변동 폭 제곱, 배수 k(k-1)에 비례함을 보임(검산: r 5%, k 2에서 0.9952, 10회 곱 0.953).
  (c) 추세장(하루 +1%·-1% 20일 연속) 비교표, 그림 2장.
primary_source: |
  금융위원회 단일종목 레버리지 ETF·ETN 투자 유의사항(fsc.go.kr/no010101/86973) WebFetch 1회 시도, EGRESS_BLOCKED. 대신 WebSearch 교차 확인.
  - 정의(일간 수익률의 배수 추종)와 장기 보유 시 음의 복리효과: KB Think 용어사전, 토스뱅크, 토스피드, 삼성자산운용 블로그, 금융투자교육원 5곳이 충돌 없이 일치.
  - 100 -> 110 -> 100 예시에서 2배 ETF가 98 수준이 되는 점: 검색 요약상 상위 글 일치, 본문 계산(98.18)과 같음.
  - 가격제한폭 30%의 2배(하루 최대 60%) 이론상 손실 및 괴리율·교육 요건: 정책브리핑, 한국경제 보도로 확인. 60%는 30%x2 산술이고 예탁금 금액은 본문에 쓰지 않고 곱버스 글로 연결.
  - 표의 모든 수치는 공개된 공식으로 직접 계산한 값이며 제도 수치(세율·한도)는 쓰지 않았음.
기준일: 2026년 10월 6일 기준
refresh_due: 2027-01-05
refresh_reason: "구조 설명과 계산표라 수치가 바뀌지 않음. 단일종목 레버리지 상품 규정 문장이 있어 분기 1회 점검"
tags: 레버리지 ETF, 레버리지 ETF 뜻, 레버리지 ETF 장기 보유, 변동성 손실, 음의 복리효과, 횡보장 손실, 3배 레버리지, 레버리지 ETF 계산, 괴리율, ETF 투자 주의
cannibalization_note: |
  곱버스 뜻과 레버리지 예탁금 기준 글은 지수형 곱버스 뜻과 기본예탁금, 2거래일 예시 하나가 중심이다. 이 글은 변동 폭과 배수별 20일 손실표, 공식, 추세장 비교를 더한 계산 중심 글이고 곱버스·예탁금은 그 글로 링크한다. ETF 뜻 글은 ETF 구조 일반, 이 글은 레버리지 구조 한 가지에 한정.
gate_pass: true
gate_pass_note: |
  게이트1 16,850회, 게이트2 v4 통과, 게이트3 20일 손실표와 공식과 그림 2장, 게이트4 정의는 5곳 교차검증과 표는 직접 계산(제도 수치 없음). 금융위 원문은 접속 불가였으나 쓴 사실이 정의와 산술이라 사람 확인 불필요.
self_check: |
  [2026-10-06 gate_pass:true]
  후보 경위: 이슈 스캔(10월 증시 일정: 금통위 10/22, FOMC 10/27-28, 삼성전자 3분기 잠정실적 10/8) 후 8개 실측(배당락일 3,280 PASS, 코스피 7000 990 PASS, 엔비디아 실적발표 1,230 PASS, 금통위·FOMC 일정·미국 중간선거 증시·연말 대주주 양도세 각 20 FAIL, 테슬라 실적발표 210 FAIL). 엔비디아 실적발표는 날짜를 검색 결과로 확인하지 못해 제외(오래된 기사가 섞임). 배당락일은 16편·129편과 겹쳐 제외. 4주 안 시의성 후보가 없어 우선순위 목록의 5유형(월 5,000 이상 개념) 중 가장 큰 레버리지 ETF를 채택. 40편 갱신 대신 새 계산 중심 글로 쓰고 40편으로 링크(규칙 4번은 갱신 선호이나 이번엔 검색 의도가 다른 계산형이라 새 글로 판단).
  YMYL: 종목·상품 추천, 방향 예측, 매매 시점 없음. 제목·소제목에 전망·추천·목표가 없음. 모든 수치는 가정이라고 본문에 표시.
  첫 문장 유형: 문제제기형(지수는 제자리인데 내 ETF만 줄어 있는 경험). 직전 139 수치충격, 138 정의, 137 문제제기(3편 간격), 136 대비, 135 절차. 인트로 둘째 문장에 직접 답(95.3).
  글 구조 유형: 계산형(첫 H2 바로 아래가 A씨 20거래일 계산 박스, 설명 문단보다 먼저). 직전 139 개념형, 138 비교형, 137 계산형(2편 간격), 136 절차형.
  어투 모드: C 사례형(가상 인물 A씨, 가상임을 계산 박스 제목에 명시, 합쇼체). 직전 139 A, 138 B와 다름(135 이후 처음). 꾸며낸 1인칭 경험 없음.
  기관 안내 문장 금융투자교육원 1곳 링크 처리, 출처 목록 6개 전부 링크 처리.
  내부 링크: 곱버스 뜻과 레버리지 예탁금 기준 글(published), ETF 뜻과 구성종목 확인법 글(published), 원유 ETF 롤오버 비용 글(132, drafted gate_pass:true라 발행 순서 주의).
  AI 티 점검: em대시 0개, 다만 0회, mark 3개, FAQ 5개(직전 139는 6개, 138은 4개), FAQ 헤딩 "보유 전에 따져볼 의문 다섯 개"(신규, 걸리는·막히는·헷갈·세 줄 계열 어휘 없음), 요약박스 제목 "⚖️ 계산표 읽기 전 네 줄"(신규, 황토색), H2 6개 중 질문형 1개.
figure_plan: |
  2장
  1: 20일 꺾은선(지수 100 대 2배 ETF 95.3, 시간 경로)
  2: 일간 변동 폭별 20일 뒤 값 막대(변동 폭과 배수에 따른 크기 비교)
  계산표 2개는 숫자를 정확히 읽어야 해서 표로 유지.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-06</p>

<p>지수는 제자리인데 내 레버리지 ETF만 줄어 있는 걸 본 적이 있다면, 고장이 아니라 구조 때문입니다. 레버리지 ETF는 하루 수익률의 2배를 따라가므로, 오르내림이 반복되면 지수가 원점이어도 20일 뒤 값이 95.3까지 내려갈 수 있습니다.</p>

<div style="background:#fdf6ec;border:2px solid #c98a2b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8a5a12;font-size:18px;">⚖️ 계산표 읽기 전 네 줄</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>하루 ±5%로 20일 흔들리면 지수는 100 그대로, 2배 ETF는 95.3, 3배 ETF는 86.6입니다.</li>
    <li>왕복 손실은 일간 변동 폭의 제곱에 비례하고, 배수가 2배에서 3배로 가면 3배로 커집니다.</li>
    <li>한 방향으로만 움직이면 결과가 반대로 뒤집혀 2배보다 더 벌거나 덜 잃습니다.</li>
    <li>모든 수치는 보수·괴리율을 뺀 단순 계산이고 실제 상품 수익률이 아닙니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">횡보장에서 레버리지 ETF는 얼마나 줄어드나요</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">하루 변동 폭과 배수가 손실을 정하는 방식</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">한 방향으로 움직일 때는 결과가 뒤집힙니다</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 이 구조가 중요한 이유</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">보유 전에 따져보는 순서</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">보유 전에 따져볼 의문 다섯 개</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">횡보장에서 레버리지 ETF는 얼마나 줄어드나요</h2>

<div style="background:#fff8e6;border-left:4px solid #e0a83f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>계산 예시: A씨의 20거래일 (가상 인물, 가상 수치)</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>A씨는 2배 레버리지 ETF에 1,000만원을 넣었습니다. 기초지수는 첫날 5% 오르고 다음 날 정확히 원점으로 돌아오는 흐름을 10번 반복합니다.</li>
    <li>1일차: 지수 +5%, ETF는 +10%라 1,000만원이 1,100만원이 됩니다.</li>
    <li>2일차: 지수는 원점으로 -4.76%, ETF는 -9.52%라 1,100만원이 995만원이 됩니다.</li>
    <li>20일차: 지수는 100 그대로인데 ETF는 95.3, A씨 평가액은 약 953만원입니다.</li>
  </ul>
</div>

<p><mark>왕복 한 번(이틀)마다 값이 0.48%씩 깎이고, 이 깎임이 10번 곱해져 20일 뒤 4.7%가 사라집니다.</mark> 지수는 한 번도 원점 아래로 내려간 적이 없습니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/leverage-etf-sideways-loss-table-1.png" alt="20일 동안 기초지수와 2배 레버리지 ETF 비교 꺾은선. 지수는 100과 105를 오가고 2배 ETF는 110과 99.5에서 시작해 점점 낮아져 95.3으로 끝남" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 위 계산 예시를 그대로 그린 단순 모델(하루 +5%, 다음 날 원점 복귀 20일 반복), 비용 제외</figcaption></figure>

<p>같은 방식으로 일간 변동 폭과 배수를 바꿔 20일(왕복 10번) 뒤 값을 계산하면 아래와 같습니다. 기초지수는 모든 칸에서 100입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">일간 오르내림 폭</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2배 ETF</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">3배 ETF</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2배 ETF가 100으로 돌아가는 데 필요한 상승률</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">±1%</td><td style="border:1px solid #ddd;padding:8px;">99.8</td><td style="border:1px solid #ddd;padding:8px;">99.4</td><td style="border:1px solid #ddd;padding:8px;">0.2%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">±2%</td><td style="border:1px solid #ddd;padding:8px;">99.2</td><td style="border:1px solid #ddd;padding:8px;">97.7</td><td style="border:1px solid #ddd;padding:8px;">0.8%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">±5%</td><td style="border:1px solid #ddd;padding:8px;">95.3</td><td style="border:1px solid #ddd;padding:8px;">86.6</td><td style="border:1px solid #ddd;padding:8px;">4.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">±10%</td><td style="border:1px solid #ddd;padding:8px;">83.2</td><td style="border:1px solid #ddd;padding:8px;">57.1</td><td style="border:1px solid #ddd;padding:8px;">20.2%</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;margin-top:6px;">계산: 왕복 1회 배율 = (1+kr)×(1-kr/(1+r)), k는 배수, r은 오르는 날의 상승률. 보수·괴리율·거래비용 제외한 가정값입니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">하루 변동 폭과 배수가 손실을 정하는 방식</h2>

<p>왕복 한 번의 배율은 1 - k(k-1)r²/(1+r)로 줄어듭니다. <mark>손실은 일간 변동 폭 r의 제곱에 비례하고, 배수 k가 2배에서 3배로 가면 k(k-1)이 2에서 6이 되어 손실이 3배로 커집니다.</mark></p>

<ul style="line-height:1.9;padding-left:20px;">
  <li>변동 폭이 1%에서 5%로 5배 커지면 왕복 손실은 약 25배 커집니다.</li>
  <li>배수가 2배에서 3배로 오르면 같은 변동에서 손실이 3배가 됩니다.</li>
  <li>변동 폭이 작은 잔잔한 장에서는 20일 손실이 0.2%대로 거의 보이지 않습니다.</li>
</ul>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/leverage-etf-sideways-loss-table-2.png" alt="일간 변동 폭별 20일 뒤 레버리지 ETF 값 막대 비교. ±1%는 2배 99.8과 3배 99.4, ±10%는 2배 83.2와 3배 57.1" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 위 계산표 값, 기초지수는 모두 20일 뒤 100, 비용 제외</figcaption></figure>

<p>손실이 커질수록 되돌리기도 어려워집니다. 83.2가 된 ETF가 100으로 돌아가려면 20.2% 올라야 하고, 57.1이 된 3배 ETF는 75.1%가 올라야 합니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">한 방향으로 움직일 때는 결과가 뒤집힙니다</h2>

<p>지수가 한 방향으로만 움직이면 복리가 손실이 아니라 이득으로 작용합니다. 하루 1%씩 20일 연속 같은 방향으로 움직인 경우의 값입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">20일 흐름</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">지수 변화</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2배 ETF 변화</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">지수의 2배</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">3배 ETF 변화</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">하루 +1%씩 상승</td><td style="border:1px solid #ddd;padding:8px;">+22.0%</td><td style="border:1px solid #ddd;padding:8px;">+48.6%</td><td style="border:1px solid #ddd;padding:8px;">+44.0%</td><td style="border:1px solid #ddd;padding:8px;">+80.6%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">하루 -1%씩 하락</td><td style="border:1px solid #ddd;padding:8px;">-18.2%</td><td style="border:1px solid #ddd;padding:8px;">-33.2%</td><td style="border:1px solid #ddd;padding:8px;">-36.4%</td><td style="border:1px solid #ddd;padding:8px;">-45.6%</td></tr>
  </tbody>
</table>

<p>상승 구간에서는 지수 2배보다 4.6%포인트 더 오르고, 하락 구간에서는 지수 2배 손실보다 3.2%포인트 덜 빠집니다. <mark>같은 상품이 추세에서는 배수 이상, 횡보에서는 배수 미만의 결과를 낸다는 것이 레버리지 ETF의 핵심 성질입니다.</mark></p>

<p style="font-size:13px;color:#888;margin-top:6px;">계산: 1.01의 20제곱 1.220, 1.02의 20제곱 1.486, 1.03의 20제곱 1.806 / 0.99, 0.98, 0.97의 20제곱 각각 0.818, 0.668, 0.544. 가정값이며 실제 시장 경로가 아닙니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">주식 투자자에게 이 구조가 중요한 이유</h2>

<p>레버리지 ETF의 성적은 기간 말 지수만 보고 맞힐 수 없고, 그 사이 경로에 달려 있습니다. 시장이 크게 출렁이는 시기에는 변동 폭 r이 커져 위 표의 오른쪽 아래 칸에 가까워집니다.</p>

<ul style="line-height:1.9;padding-left:20px;">
  <li>한 달 지수 수익률에 2를 곱한 값은 보유 결과가 아니라 일간 목표의 단순 환산입니다.</li>
  <li>하루 가격제한폭이 ±30%인 개별 종목을 기초로 한 상품은 2배 상품은 이론상 하루에 최대 60%까지 움직일 수 있어 r이 훨씬 큽니다.</li>
  <li>선물로 구성된 상품은 만기 교체 비용이 따로 붙습니다. 구조는 <a href="https://sensitiveboss3.tistory.com/entry/oil-etf-rollover-cost-q3-2026" target="_blank" rel="noopener">원유 ETF 롤오버 비용 글</a>에 정리했습니다.</li>
</ul>

<p>투자 자격과 예탁금처럼 매매 전에 거쳐야 하는 절차는 <a href="https://sensitiveboss3.tistory.com/entry/leveraged-inverse-etf-deposit" target="_blank" rel="noopener">곱버스 뜻과 레버리지 예탁금 기준 글</a>에, ETF 자체의 구조는 <a href="https://sensitiveboss3.tistory.com/entry/etf-basics-holdings" target="_blank" rel="noopener">ETF 뜻과 구성종목 확인법 글</a>에 있습니다. 이 글의 표는 방향 예측이 아니라 보유 기간별로 구조가 만드는 차이만 보여 줍니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">보유 전에 따져보는 순서</h2>

<p>레버리지 ETF를 보유하기 전에는 아래 순서로 상품 설명서의 항목을 확인합니다. 금융당국과 운용사 안내도 같은 항목을 반복해서 강조합니다.</p>

<ol style="line-height:1.9;padding-left:22px;">
  <li><b>목표 배수와 기간:</b> 일간 수익률의 몇 배를 따르는지, 월간이 아니라 일간인지 봅니다.</li>
  <li><b>기초자산 변동성:</b> 지수인지 개별 종목인지에 따라 위 표에서 읽을 열이 달라집니다.</li>
  <li><b>총보수:</b> 보수는 보유 기간만큼 쌓이므로 위 표의 손실에 더해집니다.</li>
  <li><b>괴리율:</b> 시장가격과 순자산가치의 차이를 거래 시점에 확인합니다.</li>
  <li><b>의무 교육과 예탁금:</b> 신규 투자자는 사전교육과 기본예탁금 요건이 있어 <a href="https://www.kifin.or.kr/common/edu/1/detail.do" target="_blank" rel="noopener">금융투자교육원</a>에서 먼저 이수합니다.</li>
</ol>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">보유 전에 따져볼 의문 다섯 개</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">레버리지 ETF를 하루만 들고 있어도 복리 손실이 생기나요?</summary>
  <p style="margin:10px 0 0 0;">하루 보유라면 복리 손실은 없습니다. 하루 수익률의 배수를 따르는 구조라서, 보유 기간이 이틀 이상으로 늘 때부터 경로에 따라 차이가 생깁니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">지수가 오르면 레버리지 ETF는 항상 2배 이상 오르나요?</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 한 방향으로 계속 오를 때만 2배보다 더 벌고, 오르내림이 섞이면 2배에 못 미치거나 오히려 손실이 날 수 있습니다. 위 추세 표에서 하루 1%씩 20일 오르면 지수 22.0%, 2배 ETF 48.6%였습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">3배 상품의 손실은 2배 상품의 딱 1.5배인가요?</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 왕복 손실은 배수 k에 대해 k(k-1)에 비례하므로 2배는 2, 3배는 6입니다. 같은 오르내림에서 3배 상품의 손실은 2배 상품의 약 3배로 커집니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">인버스 ETF도 같은 방식으로 줄어드나요?</summary>
  <p style="margin:10px 0 0 0;">같은 원리입니다. 인버스는 배수가 음수라서 한 방향 추세가 아니라 오르내림이 반복되는 구간에서 마찬가지로 값이 깎입니다. 곱버스 구조는 위에서 링크한 글에 정리해 두었습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">손실이 난 뒤 지수가 다시 오르면 원금을 회복하나요?</summary>
  <p style="margin:10px 0 0 0;">지수가 원점으로 돌아와도 회복되지 않습니다. 위 표의 ±10% 3배 상품은 57.1이라 원래 값 100으로 가려면 75.1% 올라야 하고, 이 계산은 보수와 괴리율을 뺀 값입니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://kbthink.com/dictionary/view.html?dictId=KED-00009326" target="_blank" rel="noopener">KB Think - 레버리지 ETF란</a></li>
    <li><a href="https://www.tossbank.com/articles/leverage-etf" target="_blank" rel="noopener">토스뱅크 - 레버리지 ETF</a></li>
    <li><a href="https://samsungfundblog.com/archives/49059" target="_blank" rel="noopener">삼성자산운용 블로그 - 2배 수익률을 추구하는 레버리지 ETF</a></li>
    <li><a href="https://www.kcie.or.kr/mobile/guide/3/18/web_view?series_idx=&amp;content_idx=522" target="_blank" rel="noopener">금융투자교육원 - ETF 투자 시 유의해야 할 5가지</a></li>
    <li><a href="https://www.korea.kr/news/policyNewsView.do?newsId=148965098" target="_blank" rel="noopener">정책브리핑 - 단일종목 레버리지 ETF 출시, 금융당국 유의사항</a></li>
    <li><a href="https://www.hankyung.com/article/202606184344i" target="_blank" rel="noopener">한국경제 - 금감원, 단일종목 레버리지 ETF 투자 주의보</a></li>
  </ul>
  기준일: 2026년 10월 6일. 금융위원회 원문은 열람하지 못해 금융교육기관·운용사·금융사·언론 6곳의 설명을 대조했고, 표의 수치는 모두 위 공식으로 직접 계산한 값입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 상품 구조를 설명하는 정보 글이며 특정 상품의 매수나 매도를 권하지 않습니다. 계산 예시는 가정이고 실제 수익은 달라질 수 있으며, 투자의 판단과 결과는 투자자 본인에게 있습니다. 보수와 규정은 바뀔 수 있어 가입 전 상품 설명서를 직접 보시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "레버리지 ETF 횡보장 손실 계산표와 배수별 차이",
  "description": "레버리지 ETF를 하루 ±5%로 20일 흔들리는 횡보장에서 보유하면 지수는 100인데 2배 ETF는 95.3, 3배는 86.6이 됩니다. 변동 폭과 배수별 손실 계산표와 추세장 비교를 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/leverage-etf-sideways-loss-table-1.png",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-06",
  "dateModified": "2026-10-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/leverage-etf-sideways-loss-table"
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
      "name": "레버리지 ETF를 하루만 들고 있어도 복리 손실이 생기나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "하루 보유라면 복리 손실은 없습니다. 하루 수익률의 배수를 따르는 구조라서, 보유 기간이 이틀 이상으로 늘 때부터 경로에 따라 차이가 생깁니다."
      }
    },
    {
      "@type": "Question",
      "name": "지수가 오르면 레버리지 ETF는 항상 2배 이상 오르나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. 한 방향으로 계속 오를 때만 2배보다 더 벌고, 오르내림이 섞이면 2배에 못 미치거나 오히려 손실이 날 수 있습니다. 위 추세 표에서 하루 1%씩 20일 오르면 지수 22.0%, 2배 ETF 48.6%였습니다."
      }
    },
    {
      "@type": "Question",
      "name": "3배 상품의 손실은 2배 상품의 딱 1.5배인가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. 왕복 손실은 배수 k에 대해 k(k-1)에 비례하므로 2배는 2, 3배는 6입니다. 같은 오르내림에서 3배 상품의 손실은 2배 상품의 약 3배로 커집니다."
      }
    },
    {
      "@type": "Question",
      "name": "인버스 ETF도 같은 방식으로 줄어드나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "같은 원리입니다. 인버스는 배수가 음수라서 한 방향 추세가 아니라 오르내림이 반복되는 구간에서 마찬가지로 값이 깎입니다. 곱버스 구조는 위에서 링크한 글에 정리해 두었습니다."
      }
    },
    {
      "@type": "Question",
      "name": "손실이 난 뒤 지수가 다시 오르면 원금을 회복하나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "지수가 원점으로 돌아와도 회복되지 않습니다. 위 표의 ±10% 3배 상품은 57.1이라 원래 값 100으로 가려면 75.1% 올라야 하고, 이 계산은 보수와 괴리율을 뺀 값입니다."
      }
    }
  ]
}
</script>
