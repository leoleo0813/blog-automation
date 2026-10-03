---
keyword: 엔캐리트레이드
title: 엔캐리트레이드 청산 원리와 손익분기 환율
slug: yen-carry-trade-breakeven-rate
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 2200 (PC 750 / 모바일 1450, 2026-10-03 실측)
gate1_pass: true (일반 주제 기준 월 500 이상)
serp_check: |
  [게이트2 v3 판정 2026-10-03 - 통과]
  WebSearch "엔캐리트레이드 뜻 청산 원리 금리차" 상위 9개: brunch.co.kr(개인), kbthink.com 2개(KB 사전·이슈), eiec.kdi.re.kr(국책 교육), a-ha.io 3개(Q&A 커뮤니티), ecodemy.cafe24.com(개인 경제 블로그), news.hada.io(커뮤니티).
  1) 진입 여지: 있음. brunch 개인 글, 개인 경제 블로그, Q&A 커뮤니티가 상위에 섞여 있다.
  2) 검색 의도: 뜻과 청산 원리를 찾는 탐색형. 조회·계산기 아님.
  3) 답 완결 여부: 부분적. 상위는 정의와 청산 개념 설명 중심이고, 금리차와 환율 변화로 손익분기 환율을 직접 계산해 보여 주는 글은 요약 단계에서 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 1억 엔 차입 사례의 1년 손익 계산표와 손익분기 환율 계산식(약 144.29엔).
  (b) 엔 조달금리별(0.25%, 1.0%, 1.25%) 손익분기 환율 비교표.
  (c) 환율 시나리오별 손익 막대 그림, 일본은행 정책금리 시점별 표.
primary_source: |
  1차 출처인 일본은행 boj.or.jp WebFetch 1회 EGRESS_BLOCKED(2026-10-03). 한국은행 이슈 자료와 일본은행 결정문은 열지 못했다.
  교차검증: 2024년 8월 5일 닛케이225 12.4% 하락, 코스피 8.77% 하락, 2024년 7월 일본 정책금리 0.25%는 아시아경제·한국경제 등이 충돌 없이 일치. 일본 정책금리 0.75%(2025년 12월), 1.0%(2026년 6월 16일), 1.25%(2026년 9월 18일)는 신한금융그룹 인사이트·여성경제신문·글로벌이코노믹·헤럴드경제가 일치하고 10월 추가 인상론은 헤럴드경제 보도에 근거한다. 단 정책금리는 현재 값 유형의 숫자라 일본은행 결정문 원문 대조 전에는 gate_pass를 true로 하지 않는다.
기준일: 2026년 10월 기준 (일본은행 정책금리는 2026년 9월 18일 결정)
refresh_due: 2026-10-31
refresh_reason: 일본은행 10월 금융정책결정회의 결과(추가 인상 여부)를 반영해 정책금리 표와 손익분기 표를 갱신
capture_guide: |
  (1) 왜 필요한가: 이 글의 현재 수치 표(일본은행 정책금리 1.25%, 2026년 9월 18일 인상)를 일본은행 원문으로 확인하지 못했습니다. 보도 4곳이 일치하지만 금리 수치는 원문 확정이 필요한 유형입니다.
  (2) 시도할 사이트(우선순위):
    1순위 일본은행 영문 사이트(https://www.boj.or.jp/en/) 접속 → 상단 Monetary Policy → Monetary Policy Meetings → 2026년 9월 회의의 Statement on Monetary Policy 첫 문단(uncollateralized overnight call rate 목표 수치)이 보이게 캡처.
    2순위 한국은행 홈페이지(https://www.bok.or.kr) 접속 → 검색창에 "엔캐리 트레이드" 입력 → 조사연구 자료 "최근 엔캐리 트레이드 수익률 변화와 청산가능 규모 추정" 첫 페이지 캡처(2024년 기준 분석이라 현재 금리 대조용은 아님).
  (3) 캡처 후: 스크린샷을 대화에 올려주세요. 표 값을 원문대로 확정한 뒤 gate_pass를 true로 바꾸겠습니다.
tags: 엔캐리트레이드, 엔캐리 청산, 엔 캐리 트레이드 뜻, 일본 기준금리, 손익분기 환율, 엔달러 환율, 금리차, 일본은행, 캐리트레이드 계산, 주식 용어
gate_pass: false
gate_pass_note: |
  게이트1·2·3 충족. 게이트4는 교차검증으로 진행했지만 현재 값(일본은행 정책금리 1.25%)이 일본은행 원문 미확인이라 gate_pass:false. 발행 전 사람이 할 일: capture_guide 1순위 화면(2026년 9월 결정문)을 캡처해 올려주세요. 일치하면 gate_pass를 true로 바꾸면 됩니다. 일본은행 10월 회의 결과가 나오면 refresh_due(10월 31일)에 맞춰 갱신 대상입니다.
self_check: |
  후보 경위: 신규 8개 검색량 확인(2026-10-03). PASS 5개: 신용등급 4,950 / 엔캐리트레이드 2,200 / 회사채 1,720 / 비농업고용지표 1,710 / 현금흐름표 830. FAIL 3개: 장단기금리차 480 / 양적긴축 150 / 수익률곡선 70. 엔캐리트레이드를 채택(SERP에 개인 글이 있고 계산 정보이득 가능). 비농업고용지표는 SERP에 증권사·CME·토스뱅크가 많아 보류.
  YMYL: 종목 추천·목표가·매매시점 없음. 청산 시점 예측 없음. 계산 예시는 가정 값임을 명시.
  제목 "엔캐리트레이드 청산 원리와 손익분기 환율" 20자 내외, 금지어 없음. 슬러그 5단어.
  첫 문장 유형: 대비형(직전 122 수치충격, 121 정의, 120 문제제기, 119 절차와 다름). 인트로 둘째 문장에 정의 포함, 메타 문장 없음.
  글 구조 유형: 계산형(첫 H2 바로 아래가 계산 박스). 직전 122 개념형, 121 절차형, 120 비교형과 다름.
  어투 모드: B 대화형(해요체 중심, 독자 질문 포함). 직전 122 C, 121 A와 다름.
  현재 수치 표: 일본은행 정책금리 시점별 표(최신 1.25%, 2026-09-18). 다음 회의 일정은 확인하지 못해 날짜를 적지 않고 "10월 추가 인상론"만 보도 기준으로 적음.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 4개, FAQ 7개(직전 122 5·121 6과 다름), H2 6개 중 "~나요"형 2개. 요약박스 장미색(#fdf0f0/#c9484b), 제목 "🧮 계산부터 보면 쉬워요", 중간 박스 "💡 금리 말고 환율이 더 크게 움직여요", 마무리 박스 "🔖 정리해 두면". FAQ 헤딩 "엔 캐리 얘기에서 자주 나오는 물음". 면책 문구 새 표현.
  기관 링크: 안내 문장·출처 목록 전부 링크 처리. 내부 링크 3개(103 환헤지, 98 달러인덱스, 105 국채금리), 모두 published. 그림 1장(환율 시나리오별 손익 막대).
  발행 글 갱신(refresh): lint_draft --due에 92·98·105편이 현재 수치 부재로 기한 도달. VIX·달러인덱스·국고채 금리의 1차 출처(시카고옵션거래소·한국은행 등) 접속이 불가해 수치를 지어낼 수 없으므로 이번 실행에서는 갱신하지 않고 다음 실행으로 넘김. lint_draft: FAIL 0.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-03</p>

<p>같은 엔화 대출인데 어떤 해에는 연 4%를 벌고, 어떤 해에는 환율 때문에 원금이 깎입니다. <mark>엔 캐리 트레이드는 금리가 낮은 엔화를 빌려 금리가 높은 자산에 투자해 금리 차이를 버는 거래</mark>이고, 엔화가 갑자기 오르면 한꺼번에 되돌려지는 게 청산이에요.</p>

<div style="background:#fdf0f0;border:2px solid #c9484b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8f2a2d;font-size:18px;">🧮 계산부터 보면 쉬워요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>엔 금리 1%로 빌려 연 5% 자산에 넣는 예시에서 손익분기 환율은 약 144.29엔입니다.</li><li>같은 거래라도 엔 조달금리가 0.25%에서 1.25%로 오르면 손익분기가 144.64엔 쪽으로 올라 버틸 여유가 줄어요.</li><li>2024년 8월 5일에는 닛케이225가 12.4%, 코스피가 8.77% 하락한 청산 충격이 있었습니다.</li></ul>
</div>

<h2>목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">엔 캐리 트레이드 손익 계산 예시</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">엔 캐리 트레이드가 돌아가는 순서</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">엔 캐리 청산은 언제 일어나나요</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">일본 정책금리가 오르면 손익분기가 달라지는 이유</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 왜 중요한가</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #c9484b;padding-left:12px;margin-top:36px;">엔 캐리 트레이드 손익 계산 예시</h2>

<div style="background:#fdf0f0;border:2px solid #c9484b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8f2a2d;font-size:18px;">1억 엔을 빌려 달러 자산에 1년 넣었을 때 (가정 예시)</strong>
  <ol style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>가정 값: 엔/달러 150엔, 엔 차입금리 연 1%, 달러 자산 수익률 연 5%, 세금·수수료 제외.</li><li>1억 엔을 150엔에 바꾸면 약 66만 6,667달러입니다.</li><li>1년 뒤 5%가 붙어 70만 달러가 됩니다.</li><li>갚을 돈은 원금 1억 엔에 이자 100만 엔을 더한 1억 100만 엔이에요.</li><li>손익분기 환율 = 1억 100만 엔 ÷ 70만 달러 = 약 144.29엔</li></ol>
</div>

<p>환율이 150엔 그대로면 1억 500만 엔을 받아 400만 엔을 벌어요. 엔화가 144.29엔까지 오르면, 그러니까 달러당 엔이 약 3.8% 내려가면 그 수익이 정확히 0이 됩니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">1년 뒤 환율별 손익 (위 가정 예시, 단위 만 엔)</caption>
  <thead>
    <tr style="background:#fdf0f0;"><th style="border:1px solid #ddd;padding:8px;">1년 뒤 엔/달러</th><th style="border:1px solid #ddd;padding:8px;">달러 자산 회수액(엔)</th><th style="border:1px solid #ddd;padding:8px;">상환액(엔)</th><th style="border:1px solid #ddd;padding:8px;">손익</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">130엔</td><td style="border:1px solid #ddd;padding:8px;">9,100만</td><td style="border:1px solid #ddd;padding:8px;">10,100만</td><td style="border:1px solid #ddd;padding:8px;">-1,000만</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">140엔</td><td style="border:1px solid #ddd;padding:8px;">9,800만</td><td style="border:1px solid #ddd;padding:8px;">10,100만</td><td style="border:1px solid #ddd;padding:8px;">-300만</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">145엔</td><td style="border:1px solid #ddd;padding:8px;">10,150만</td><td style="border:1px solid #ddd;padding:8px;">10,100만</td><td style="border:1px solid #ddd;padding:8px;">+50만</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">150엔</td><td style="border:1px solid #ddd;padding:8px;">10,500만</td><td style="border:1px solid #ddd;padding:8px;">10,100만</td><td style="border:1px solid #ddd;padding:8px;">+400만</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">155엔</td><td style="border:1px solid #ddd;padding:8px;">10,850만</td><td style="border:1px solid #ddd;padding:8px;">10,100만</td><td style="border:1px solid #ddd;padding:8px;">+750만</td></tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/yen-carry-trade-breakeven-rate-1.png" alt="환율별 엔 캐리 트레이드 손익 막대 그림. 130엔 -1,000만 엔, 140엔 -300만 엔, 145엔 +50만 엔, 150엔 +400만 엔, 155엔 +750만 엔" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 위 가정 값으로 직접 계산한 예시, 2026년 10월 기준</figcaption></figure>

<p>금리 차이로 버는 돈은 1년에 400만 엔인데, 환율이 10엔만 움직여도 700만 엔이 오르내려요. <mark>캐리 수익보다 환율 변동이 훨씬 크다</mark>는 점이 이 거래의 핵심 위험입니다.</p>

<div style="background:#fdf0f0;border:2px solid #c9484b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8f2a2d;font-size:18px;">💡 금리 말고 환율이 더 크게 움직여요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>위 표는 달러 자산 가격이 그대로라고 본 계산입니다. 자산 가격이 떨어지면 손실이 더 커져요.</li><li>환율 위험을 미리 잠그는 비용은 <a href="https://sensitiveboss3.tistory.com/entry/currency-hedge-cost-meaning" target="_blank" rel="noopener">환헤지 뜻과 비용 계산</a> 글에서 따로 정리했어요.</li></ul>
</div>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #c9484b;padding-left:12px;margin-top:36px;">엔 캐리 트레이드가 돌아가는 순서</h2>

<p>엔 캐리 트레이드는 세 단계로 움직입니다. 일본 금리가 낮을수록 빌리는 비용이 싸서 이 거래가 매력적이에요.</p>

<ol>
  <li>일본 금융기관에서 낮은 금리로 엔화를 빌립니다.</li>
  <li>엔화를 달러 등 다른 통화로 바꿉니다.</li>
  <li>그 돈으로 금리가 높은 채권이나 주식 같은 자산을 삽니다.</li>
</ol>

<p>수익은 금리 차이와 환율 변화, 그리고 자산 가격 변화에서 나와요. 이 중 금리 차이만 미리 알 수 있고 나머지 둘은 1년 뒤에야 알 수 있습니다.</p>

<p>엔화로 빌려 달러로 바꿨으니 갚을 때는 다시 엔화가 필요해요. 이때 엔화가 비싸져 있으면 같은 달러로 엔화를 덜 사게 되고, 앞의 표처럼 손실이 납니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #c9484b;padding-left:12px;margin-top:36px;">엔 캐리 청산은 언제 일어나나요</h2>

<p>청산은 엔화가 갑자기 오르거나 일본 금리가 예상보다 빨리 오를 때 몰려서 나타납니다. 손익분기 환율이 코앞으로 다가오면 너도나도 자산을 팔아 엔화를 갚으려 하기 때문이에요.</p>

<ul>
  <li>일본은행이 정책금리를 올려 엔 조달 비용이 늘어날 때</li>
  <li>엔화 가치가 빠르게 올라 손익분기 환율을 위협할 때</li>
  <li>투자한 자산 가격이 떨어져 손실 방어용으로 팔아야 할 때</li>
</ul>

<p>가장 자주 인용되는 사례가 2024년 8월 5일입니다. 그해 7월 일본은행이 정책금리를 0.25%로 올린 뒤, 8월 5일 닛케이225가 하루에 12.4%, 코스피가 8.77% 떨어졌다고 보도됐어요.</p>

<p>이 하락이 전부 엔 캐리 청산 때문이었다고 말할 수는 없습니다. 미국 경기 둔화 우려 같은 요인이 겹쳤고, 몇 퍼센트가 청산 몫인지는 분리해서 나온 공식 숫자가 없어요.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #c9484b;padding-left:12px;margin-top:36px;">일본 정책금리가 오르면 손익분기가 달라지는 이유</h2>

<p>엔 조달금리가 오르면 갚을 이자가 늘어서 손익분기 환율이 올라갑니다. 같은 가정(150엔, 달러 자산 5%)으로 금리만 바꿔 보면 이렇게 달라져요.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">엔 조달금리별 손익분기 환율 (1억 엔 차입, 150엔 매수, 달러 자산 5% 가정)</caption>
  <thead>
    <tr style="background:#fdf0f0;"><th style="border:1px solid #ddd;padding:8px;">엔 조달금리</th><th style="border:1px solid #ddd;padding:8px;">1년 뒤 상환액</th><th style="border:1px solid #ddd;padding:8px;">손익분기 환율</th><th style="border:1px solid #ddd;padding:8px;">150엔 대비 여유</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">0.25%</td><td style="border:1px solid #ddd;padding:8px;">1억 25만 엔</td><td style="border:1px solid #ddd;padding:8px;">약 143.21엔</td><td style="border:1px solid #ddd;padding:8px;">약 4.5%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1.0%</td><td style="border:1px solid #ddd;padding:8px;">1억 100만 엔</td><td style="border:1px solid #ddd;padding:8px;">약 144.29엔</td><td style="border:1px solid #ddd;padding:8px;">약 3.8%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1.25%</td><td style="border:1px solid #ddd;padding:8px;">1억 125만 엔</td><td style="border:1px solid #ddd;padding:8px;">약 144.64엔</td><td style="border:1px solid #ddd;padding:8px;">약 3.6%</td></tr>
  </tbody>
</table>

<p>금리 1%포인트가 올라도 손익분기는 1엔 남짓 움직입니다. 그래서 <mark>금리 인상 자체보다 그 소식이 엔화 가치를 얼마나 끌어올리느냐가 청산의 방아쇠</mark>가 돼요.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">일본은행 정책금리 시점별 수치 (보도 기준 2026년 10월 3일)</caption>
  <thead>
    <tr style="background:#fdf0f0;"><th style="border:1px solid #ddd;padding:8px;">시점</th><th style="border:1px solid #ddd;padding:8px;">정책금리</th><th style="border:1px solid #ddd;padding:8px;">비고</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2024년 7월</td><td style="border:1px solid #ddd;padding:8px;">0.25%</td><td style="border:1px solid #ddd;padding:8px;">2024년 8월 5일 증시 급락의 배경으로 자주 언급</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2025년 12월</td><td style="border:1px solid #ddd;padding:8px;">0.75%</td><td style="border:1px solid #ddd;padding:8px;">2026년 6월 인상 직전 수준</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 6월 16일</td><td style="border:1px solid #ddd;padding:8px;">1.0%</td><td style="border:1px solid #ddd;padding:8px;">6개월 만의 0.25%포인트 인상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 9월 18일</td><td style="border:1px solid #ddd;padding:8px;">1.25%</td><td style="border:1px solid #ddd;padding:8px;">현재 수준, 10월 추가 인상론이 보도됨</td></tr>
  </tbody>
</table>

<p>위 수치는 보도 여러 곳이 일치한 내용이고, 발표 기관인 <a href="https://www.boj.or.jp/en/" target="_blank" rel="noopener">일본은행</a> 원문 대조는 거치지 않았습니다. 10월 회의 결과가 나오면 표를 새 값으로 바꿀 거예요.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #c9484b;padding-left:12px;margin-top:36px;">주식 투자자에게 왜 중요한가</h2>

<p>엔 캐리 청산은 일본 증시만의 문제가 아니라, <mark>엔화를 빌려 해외 자산을 산 돈이 한꺼번에 빠지는 사건</mark>이에요. 시장이 이 이야기를 받아들이는 경로는 보통 이렇게 설명됩니다.</p>

<ul>
  <li>일본 금리 인상 소식 → 엔화 강세 → 엔 캐리 포지션의 손익분기 압박</li>
  <li>포지션 정리를 위한 해외 주식·채권 매도 → 변동성 확대, 위험자산 약세</li>
  <li>달러 대비 엔화 강세가 이어지면 → 달러 가치 흐름과 함께 원화 환율에도 영향</li>
</ul>

<p>변동성이 커지는 구간에서는 시장의 공포를 재는 VIX가 같이 뛰는 경우가 많아요. 지표의 구성은 <a href="https://sensitiveboss3.tistory.com/entry/vix-index-meaning-calculation" target="_blank" rel="noopener">VIX 지수 뜻과 계산 방식</a> 글에, 달러 흐름은 <a href="https://sensitiveboss3.tistory.com/entry/dollar-index-meaning-currency-weights" target="_blank" rel="noopener">달러인덱스 뜻과 통화 비중</a> 글에 정리해 뒀습니다.</p>

<p>금리차가 줄어드는지는 미국 쪽 금리도 같이 봐야 판단할 수 있어요. 미국 장기금리 흐름은 <a href="https://sensitiveboss3.tistory.com/entry/government-bond-yield-meaning" target="_blank" rel="noopener">국채금리 뜻</a> 글에서 볼 수 있습니다.</p>

<p>한 가지는 분명히 해 둘게요. 청산이 시작되는 시점이나 규모는 누구도 미리 맞히지 못하고, 이 글의 계산도 방향을 알려 주는 것이 아니라 구조를 보여 주는 예시입니다.</p>

<div style="background:#fdf0f0;border:2px solid #c9484b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8f2a2d;font-size:18px;">🔖 정리해 두면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>손익분기 환율은 상환할 엔화를 투자 회수 달러로 나눠서 구합니다.</li><li>엔 조달금리가 오르면 손익분기가 올라가지만, 실제 충격은 엔화 가치가 얼마나 빨리 오르느냐에서 와요.</li><li>청산 시점과 규모는 예측하지 못하는 영역이라 계산은 구조를 이해하는 용도로만 씁니다.</li></ul>
</div>

<h2 style="border-left:6px solid #c9484b;padding-left:12px;margin-top:36px;">엔 캐리 얘기에서 자주 나오는 물음</h2>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">엔 캐리 트레이드는 개인도 할 수 있나요?</summary><p>직접 엔화를 빌려 투자하는 개인은 드뭅니다. 보통 헤지펀드나 기관이 하고, 개인은 엔화 대출을 낀 상품이 아니라면 간접적으로 영향만 받아요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">엔화가 오르면 왜 주식이 떨어지나요?</summary><p>엔화로 빌린 돈이 해외 자산에 들어가 있으면, 엔화가 오를 때 그 자산을 팔아 빚을 갚는 쪽으로 움직이기 때문입니다. 판매 물량이 한꺼번에 나오면 가격이 흔들려요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">달러 캐리 트레이드도 같은 원리인가요?</summary><p>같은 원리입니다. 빌리는 통화만 달러로 바뀌고, 금리가 낮은 통화로 빌려 높은 자산에 넣는 구조는 똑같아요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">일본은행이 금리를 올리면 항상 청산이 일어나나요?</summary><p>항상 그렇지는 않습니다. 인상이 이미 시장에 반영돼 있었다면 충격이 작고, 예상보다 빠르거나 엔화가 급등할 때 청산 압력이 커집니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">엔 캐리 청산이 오면 코스피는 얼마나 빠지나요?</summary><p>미리 말할 수 있는 숫자는 없습니다. 2024년 8월 5일에 코스피가 8.77% 하락한 사례가 있지만, 그 하락에는 다른 요인도 섞여 있었어요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">손익분기 환율 계산에 세금과 수수료는 들어가나요?</summary><p>이 글의 예시에는 넣지 않았습니다. 실제 거래에서는 세금, 거래 수수료, 환전 스프레드가 더해져 손익분기가 더 불리하게 움직여요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">일본 정책금리 최신 수치는 어디서 보나요?</summary><p><a href="https://www.boj.or.jp/en/" target="_blank" rel="noopener">일본은행</a> 영문 사이트의 Monetary Policy Meetings 메뉴에서 회의별 결정문을 볼 수 있습니다.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, 아래 자료를 교차해 정리했습니다):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.boj.or.jp/en/" target="_blank" rel="noopener">일본은행 - 금융정책결정회의 결정문</a></li>
    <li><a href="https://www.bok.or.kr/portal/bbs/P0002353/view.do?nttId=10087065&amp;oldMenuNo=201150&amp;menuNo=200433&amp;programType=newsData&amp;depth=200433&amp;relate=Y" target="_blank" rel="noopener">한국은행 - 최근 엔캐리 트레이드 수익률 변화와 청산가능 규모 추정</a></li>
    <li><a href="https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000188223" target="_blank" rel="noopener">KDI 경제교육·정보센터 - 엔캐리 트레이드 수익률 변화와 청산가능 규모</a></li>
    <li><a href="https://www.asiae.co.kr/article/2024080810022351842" target="_blank" rel="noopener">아시아경제 - 전 세계 뒤흔든 엔캐리 청산 끝났나</a></li>
    <li><a href="https://www.g-enews.com/article/Global-Biz/2026/09/202609181258003931e7e8286d56_1" target="_blank" rel="noopener">글로벌이코노믹 - 일본은행 정책금리 1.0%서 1.25%로 인상</a></li>
    <li><a href="https://biz.heraldcorp.com/article/10890959" target="_blank" rel="noopener">헤럴드경제 - 일본은행 10월 추가 인상론</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 캐리 트레이드 구조를 풀어 쓴 정보성 글이며 특정 종목이나 상품의 매수·매도를 권하지 않습니다. 계산에 쓴 환율과 수익률은 설명용 가정이고, 투자 판단과 그 결과의 책임은 투자자 본인에게 있습니다. 금리 수치는 이후 결정으로 달라질 수 있습니다.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "엔캐리트레이드 청산 원리와 손익분기 환율",
  "description": "엔 캐리 트레이드가 돌아가는 순서, 1억 엔 차입 예시로 계산한 손익분기 환율 약 144.29엔, 일본 정책금리별 손익분기 비교와 2024년 8월 청산 사례를 정리했습니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-03",
  "dateModified": "2026-10-03",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/yen-carry-trade-breakeven-rate"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/yen-carry-trade-breakeven-rate-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "엔 캐리 트레이드는 개인도 할 수 있나요?", "acceptedAnswer": {"@type": "Answer", "text": "직접 엔화를 빌려 투자하는 개인은 드뭅니다. 보통 헤지펀드나 기관이 하고, 개인은 엔화 대출을 낀 상품이 아니라면 간접적으로 영향만 받아요."}},
    {"@type": "Question", "name": "엔화가 오르면 왜 주식이 떨어지나요?", "acceptedAnswer": {"@type": "Answer", "text": "엔화로 빌린 돈이 해외 자산에 들어가 있으면, 엔화가 오를 때 그 자산을 팔아 빚을 갚는 쪽으로 움직이기 때문입니다. 판매 물량이 한꺼번에 나오면 가격이 흔들려요."}},
    {"@type": "Question", "name": "달러 캐리 트레이드도 같은 원리인가요?", "acceptedAnswer": {"@type": "Answer", "text": "같은 원리입니다. 빌리는 통화만 달러로 바뀌고, 금리가 낮은 통화로 빌려 높은 자산에 넣는 구조는 똑같아요."}},
    {"@type": "Question", "name": "일본은행이 금리를 올리면 항상 청산이 일어나나요?", "acceptedAnswer": {"@type": "Answer", "text": "항상 그렇지는 않습니다. 인상이 이미 시장에 반영돼 있었다면 충격이 작고, 예상보다 빠르거나 엔화가 급등할 때 청산 압력이 커집니다."}},
    {"@type": "Question", "name": "엔 캐리 청산이 오면 코스피는 얼마나 빠지나요?", "acceptedAnswer": {"@type": "Answer", "text": "미리 말할 수 있는 숫자는 없습니다. 2024년 8월 5일에 코스피가 8.77% 하락한 사례가 있지만, 그 하락에는 다른 요인도 섞여 있었어요."}},
    {"@type": "Question", "name": "손익분기 환율 계산에 세금과 수수료는 들어가나요?", "acceptedAnswer": {"@type": "Answer", "text": "이 글의 예시에는 넣지 않았습니다. 실제 거래에서는 세금, 거래 수수료, 환전 스프레드가 더해져 손익분기가 더 불리하게 움직여요."}},
    {"@type": "Question", "name": "일본 정책금리 최신 수치는 어디서 보나요?", "acceptedAnswer": {"@type": "Answer", "text": "일본은행 영문 사이트의 Monetary Policy Meetings 메뉴에서 회의별 결정문을 볼 수 있습니다."}}
  ]
}
</script>
