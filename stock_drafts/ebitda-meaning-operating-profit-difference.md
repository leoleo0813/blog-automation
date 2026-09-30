---
keyword: EBITDA 뜻
title: EBITDA 뜻과 영업이익 차이 계산법
slug: ebitda-meaning-operating-profit-difference
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 880 (PC 370 / 모바일 510, 2026-09-30 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-30 - 통과]
  WebSearch "EBITDA 뜻 계산 방법 영업이익 감가상각비" 상위 8개: tikr.com(해외 금융 콘텐츠 한국어판), namu.wiki(위키), support.stockplus.com(증권 앱 고객센터),
  crediview.co.kr(신용정보 서비스 콘텐츠), datacookbook.kr(개인 용어 블로그), finex.ceo(FP&A SaaS 콘텐츠), differian.com(티스토리 개인 블로그), lawinsider.com(해외 사전).
  1) 진입 여지: 있음. differian(티스토리)·datacookbook 같은 개인 블로그와 소규모 서비스 콘텐츠가 섞여 SERP가 잠겨 있지 않다.
  2) 검색 의도: 정의·계산 탐색형. 조회·계산기 의도가 아니다.
  3) 답 완결 여부: 부분적. 상위는 정의와 두 가지 산식을 설명하지만, 영업이익이 같은 두 가상 회사로 EBITDA 마진, EV/EBITDA, EBITDA-CAPEX를 끝까지 계산해 순위가 뒤집히는 과정을 보여 주는 글은 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 영업이익 400억으로 같은 가상 회사 X(제조)·Y(서비스) 비교표: EBITDA 1,000억 vs 450억, 영업이익률 8% vs 16%, EBITDA 마진 20% vs 18%(순위 역전).
  (b) 순이익 경로 검산표: 210+120+70+600=1,000, 292.5+10+97.5+50=450.
  (c) EV/EBITDA 6.0배 vs 8.0배 계산표, EBITDA-CAPEX 200억 vs 390억 표, DART에서 직접 계산하는 5단계.
primary_source: |
  기획재정부 시사경제용어사전(mofe.go.kr) WebFetch 1회 시도, EGRESS_BLOCKED. 대신 WebSearch 2회로 서로 무관한 출처를 교차 확인했다:
  벤처스퀘어(IT 매체), 크레디뷰, 증권플러스, TIKR, 나무위키, 브런치·finex 콘텐츠. 정의(이자·세금·감가상각비·무형자산상각비 차감 전 이익),
  두 산식(영업이익 + 상각비 / 순이익 + 이자 + 세금 + 상각비), 현금흐름이 아니라는 한계가 충돌 없이 일치했다.
  세율·한도 같은 법정 수치가 아니라 표준 재무 개념 설명이라 교차검증으로 진행했다. 예시 숫자는 전부 가상.
기준일: 2026년 9월 기준 (계산 예시는 전부 가상)
tags: EBITDA 뜻, EBITDA란, EBITDA 계산, EBITDA 영업이익 차이, EBITDA 마진, EV/EBITDA, 감가상각비, 무형자산상각비, 재무제표 읽는 법, 기업가치
gate_pass: true
gate_pass_note: |
  게이트1 880회, 게이트2 v3 통과, 게이트3 비교·계산표 확보, 게이트4 독립 출처 5곳 이상 교차검증(기획재정부 원문은 접속 불가).
  사람은 발행 전 기획재정부 시사경제용어사전 EBITDA 항목에서 정의 문구만 한 번 대조하면 된다.
self_check: |
  [2026-09-30 gate_pass:true]
  후보 경위: backlog.verified의 대기 후보 중 EBITDA 뜻(880), 콜옵션·풋옵션·선물(옵션 손익 예시는 종목추천 오해 여지와 카니벌라이제이션 점검이 더 필요해 후순위)을 비교해 EBITDA 채택. 신규 키워드 실측은 하지 않음(이미 검색량 확인된 대기 후보가 있어 규칙 1번 적용).
  카니벌라이제이션: stock_drafts grep 결과 EBITDA를 본문 주제로 다룬 글 없음(95편 감가상각비, 102편 CAPEX는 언급만 하고 본문에서 내부 링크로 연결). 콜옵션·풋옵션·선물·수급 등 나머지 후보는 그대로 백로그에 둔다.
  수치 검산: 순이익 경로 X 210+120+70+600=1,000, Y 292.5+10+97.5+50=450. 마진 1,000/5,000=20%, 450/2,500=18%, 영업이익률 8%·16%. EV 6,000·3,600, 배수 6.0·8.0, EBITDA-CAPEX 200·390.
  YMYL: 종목 추천·목표가·매매시점 없음. 배수가 낮다·높다 판단을 하지 않음. 계산 예시 전부 가상, 실제 기업 수치 미사용.
  기관 링크: 기관 안내 문장 전부 링크 처리, 출처 목록 5개 전부 링크 처리.
  제목 "EBITDA 뜻과 영업이익 차이 계산법" 글자수 21자, 금지어 없음. 슬러그 4단어 영문 소문자 하이픈.
  첫 문장 유형: 대비형(같은 영업이익, 다른 EBITDA). 글 구조 유형: 비교형(가상 두 회사).
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 3개, FAQ 5개, H2 6개(목차 제외) 중 "~나요"형 0개.
  요약박스 보라색(#f1ecfb/#6d4fc2), 제목 "💡 EBITDA, 세 줄로 먼저". FAQ 헤딩 "EBITDA 읽다가 자주 막히는 질문". 면책 문구 새 표현.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-30</p>

<p>영업이익이 400억 원으로 똑같은 두 회사도 EBITDA는 1,000억 원과 450억 원으로 크게 달라질 수 있습니다. EBITDA는 영업이익에 감가상각비와 무형자산상각비를 다시 더한 값이기 때문입니다. 이 글은 가상의 두 회사로 그 차이를 계산해 보고, 읽을 때 걸리는 한계까지 정리합니다.</p>

<div style="background:#f1ecfb;border:2px solid #6d4fc2;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#3f2b7a;font-size:18px;">💡 EBITDA, 세 줄로 먼저</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>EBITDA는 이자, 세금, 감가상각비, 무형자산상각비를 빼기 전의 이익이고, 가장 흔한 계산은 영업이익 + 감가상각비 + 무형자산상각비입니다.</li><li>설비가 많은 회사일수록 영업이익과 EBITDA의 간격이 크게 벌어집니다.</li><li>EBITDA는 현금흐름이 아니므로 설비투자(CAPEX)와 운전자본을 따로 봐야 합니다.</li></ul>
</div>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li>EBITDA 계산식과 두 가지 계산 경로</li>
  <li>영업이익이 같은 두 회사 비교</li>
  <li>EBITDA 마진과 EV/EBITDA 읽는 법</li>
  <li>EBITDA가 놓치는 것</li>
  <li>공시에서 EBITDA를 직접 계산하는 순서</li>
  <li>자주 나오는 질문</li>
</ol>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">EBITDA 계산식과 두 가지 계산 경로</h2>

<p>EBITDA는 Earnings Before Interest, Taxes, Depreciation and Amortization의 약자입니다. <mark>EBITDA = 영업이익 + 감가상각비 + 무형자산상각비</mark>로 계산하는 것이 가장 간단합니다.</p>

<p>순이익에서 거슬러 올라가는 경로도 있고, 값은 같습니다. 아래 표의 숫자는 뒤에서 쓸 가상 회사 두 곳의 값입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">경로</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">계산식</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 X(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 Y(가상)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">영업이익에서</td><td style="border:1px solid #ddd;padding:8px;">영업이익 + 감가상각비 + 무형자산상각비</td><td style="border:1px solid #ddd;padding:8px;">400 + 500 + 100 = 1,000억 원</td><td style="border:1px solid #ddd;padding:8px;">400 + 40 + 10 = 450억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">순이익에서</td><td style="border:1px solid #ddd;padding:8px;">순이익 + 이자비용 + 법인세비용 + 감가상각비 + 무형자산상각비</td><td style="border:1px solid #ddd;padding:8px;">210 + 120 + 70 + 600 = 1,000억 원</td><td style="border:1px solid #ddd;padding:8px;">292.5 + 10 + 97.5 + 50 = 450억 원</td></tr>
    </tbody>
</table>

<p>두 경로가 일치하는 이유는 영업이익에서 이자와 법인세를 반영하면 순이익이 되기 때문입니다. 이 예시는 영업외손익을 이자비용 하나로 단순화했고, 법인세는 세전이익의 25%로 가정했습니다.</p>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">영업이익이 같은 두 회사 비교</h2>

<p>결론부터 말하면, 영업이익이 같아도 감가상각비가 다르면 EBITDA 순위가 달라집니다. 회사 X는 설비가 많은 제조업, 회사 Y는 설비가 적은 서비스업이라고 가정했습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 X(제조, 가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 Y(서비스, 가상)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">매출</td><td style="border:1px solid #ddd;padding:8px;">5,000억 원</td><td style="border:1px solid #ddd;padding:8px;">2,500억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">영업이익</td><td style="border:1px solid #ddd;padding:8px;">400억 원</td><td style="border:1px solid #ddd;padding:8px;">400억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">감가상각비</td><td style="border:1px solid #ddd;padding:8px;">500억 원</td><td style="border:1px solid #ddd;padding:8px;">40억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">무형자산상각비</td><td style="border:1px solid #ddd;padding:8px;">100억 원</td><td style="border:1px solid #ddd;padding:8px;">10억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">EBITDA</td><td style="border:1px solid #ddd;padding:8px;">1,000억 원</td><td style="border:1px solid #ddd;padding:8px;">450억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">영업이익률 (영업이익 ÷ 매출)</td><td style="border:1px solid #ddd;padding:8px;">8.0%</td><td style="border:1px solid #ddd;padding:8px;">16.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">EBITDA 마진 (EBITDA ÷ 매출)</td><td style="border:1px solid #ddd;padding:8px;">20.0%</td><td style="border:1px solid #ddd;padding:8px;">18.0%</td></tr>
    </tbody>
</table>

<p>영업이익률로는 Y가 X의 두 배지만, EBITDA 마진으로는 X가 Y보다 2%p 높습니다. <mark>같은 회사인데 지표에 따라 우열이 뒤집힌다</mark>는 점이 EBITDA를 볼 때 가장 먼저 알아야 할 대목입니다.</p>

<div style="background:#f1ecfb;border:2px solid #6d4fc2;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#3f2b7a;font-size:18px;">📝 이 비교에서 읽을 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>EBITDA는 설비 규모의 영향을 걷어내 업종이 다른 회사를 같은 잣대로 놓게 해 줍니다.</li><li>걷어낸 감가상각비는 실제로 설비를 쓰면서 닳은 비용이라, 사라진 것이 아니라 가려진 것입니다.</li><li>위 숫자는 이해를 돕기 위한 가상 값입니다.</li></ul>
</div>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">EBITDA 마진과 EV/EBITDA 읽는 법</h2>

<p>EBITDA 마진은 매출 100원당 EBITDA가 얼마인지 보여 줍니다. 계산은 EBITDA를 매출로 나누면 끝납니다.</p>

<p>EV/EBITDA는 기업가치(EV)를 EBITDA로 나눈 배수입니다. EV는 시가총액에 순차입금을 더해 구하고, 빚까지 포함해 회사 전체의 값을 매기는 개념입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 X(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 Y(가상)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">시가총액</td><td style="border:1px solid #ddd;padding:8px;">4,000억 원</td><td style="border:1px solid #ddd;padding:8px;">3,400억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">순차입금</td><td style="border:1px solid #ddd;padding:8px;">2,000억 원</td><td style="border:1px solid #ddd;padding:8px;">200억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">EV (시가총액 + 순차입금)</td><td style="border:1px solid #ddd;padding:8px;">6,000억 원</td><td style="border:1px solid #ddd;padding:8px;">3,600억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">EBITDA</td><td style="border:1px solid #ddd;padding:8px;">1,000억 원</td><td style="border:1px solid #ddd;padding:8px;">450억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">EV/EBITDA</td><td style="border:1px solid #ddd;padding:8px;">6.0배</td><td style="border:1px solid #ddd;padding:8px;">8.0배</td></tr>
    </tbody>
</table>

<p>산식은 6,000 ÷ 1,000 = 6.0배, 3,600 ÷ 450 = 8.0배입니다. 이 배수가 낮다고 저평가, 높다고 고평가라는 결론은 나오지 않으며, 같은 업종 안에서 비교할 때만 참고가 됩니다.</p>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">EBITDA가 놓치는 것</h2>

<p>EBITDA는 현금흐름과 다릅니다. 재고와 외상 대금의 변화, 설비투자로 나간 현금이 빠져 있기 때문입니다.</p>

<p>가상 회사 X의 CAPEX가 800억 원, Y가 60억 원이라고 해 보겠습니다. EBITDA에서 CAPEX를 빼면 X는 200억 원, Y는 390억 원이 남습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 X(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">회사 Y(가상)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">EBITDA</td><td style="border:1px solid #ddd;padding:8px;">1,000억 원</td><td style="border:1px solid #ddd;padding:8px;">450억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">CAPEX</td><td style="border:1px solid #ddd;padding:8px;">800억 원</td><td style="border:1px solid #ddd;padding:8px;">60억 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">EBITDA - CAPEX</td><td style="border:1px solid #ddd;padding:8px;">200억 원</td><td style="border:1px solid #ddd;padding:8px;">390억 원</td></tr>
    </tbody>
</table>

<p>EBITDA만 보면 X가 두 배 넘게 커 보였지만 설비투자를 빼면 Y가 앞섭니다. CAPEX 자체는 <a href="https://sensitiveboss3.tistory.com/entry/capex-meaning-free-cash-flow" target="_blank" rel="noopener">CAPEX 뜻과 잉여현금흐름 계산 방법</a>에서, 감가상각비는 <a href="https://sensitiveboss3.tistory.com/entry/depreciation-meaning-calculation" target="_blank" rel="noopener">감가상각비 뜻과 계산 방법</a>에서 다뤘습니다.</p>

<p>그 밖에 알아 둘 한계는 아래와 같습니다.</p>

<ul style="line-height:1.9;">
  <li>회계기준이 정한 공식 항목이 아니라 분석용 지표라서 회사와 자료마다 산식이 조금씩 다릅니다.</li>
  <li>이자와 세금 부담이 큰 회사의 부담을 보여 주지 못합니다.</li>
  <li>설비 교체가 반드시 필요한 업종에서는 감가상각비를 빼고 보는 것이 실제와 멀어질 수 있습니다.</li>
</ul>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">공시에서 EBITDA를 직접 계산하는 순서</h2>

<ol style="line-height:1.9;">
  <li><strong>공시 열기:</strong> <a href="https://dart.fss.or.kr" target="_blank" rel="noopener">DART 전자공시</a>에서 회사명을 검색해 사업보고서를 엽니다.</li>
  <li><strong>영업이익 찾기:</strong> 연결 손익계산서에서 영업이익 줄을 확인합니다.</li>
  <li><strong>감가상각비 찾기:</strong> 현금흐름표의 영업활동 조정 항목이나 주석에서 감가상각비를 확인합니다.</li>
  <li><strong>무형자산상각비 찾기:</strong> 같은 위치에서 무형자산상각비도 확인합니다.</li>
  <li><strong>합산하기:</strong> 세 값을 더하면 EBITDA이고, 매출로 나누면 EBITDA 마진입니다.</li>
</ol>

<p>계산할 때는 <mark>연결 기준인지 별도 기준인지</mark> 세 값 모두 같은 기준으로 맞춰야 합니다. 표기 이름은 회사마다 조금씩 달라서 항목명이 다르면 주석을 함께 봅니다.</p>

<div style="background:#f1ecfb;border:2px solid #6d4fc2;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#3f2b7a;font-size:18px;">✅ 정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>EBITDA는 영업이익에 감가상각비와 무형자산상각비를 더해 구합니다.</li><li>설비가 많은 회사는 영업이익과 EBITDA의 차이가 커서 지표에 따라 순위가 뒤집힐 수 있습니다.</li><li>현금 창출력을 볼 때는 CAPEX와 영업활동현금흐름을 함께 확인합니다.</li></ul>
</div>

<h2 style="border-left:6px solid #6d4fc2;padding-left:12px;margin-top:36px;">EBITDA 읽다가 자주 막히는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EBITDA가 높으면 현금을 많이 번다는 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. EBITDA는 재고와 외상 대금의 증감, 설비투자로 나간 현금을 반영하지 않습니다. 현금 창출력은 현금흐름표의 영업활동현금흐름과 CAPEX를 함께 봐야 확인됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EBITDA는 손익계산서 어디에 나오나요</summary>
  <p style="margin:10px 0 0 0;">보통 별도 줄로 나오지 않습니다. 영업이익에 감가상각비와 무형자산상각비를 더해 직접 계산하는 경우가 많고, 이 두 항목은 현금흐름표나 주석에서 찾습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EBITDA와 EBIT는 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">EBIT는 이자와 법인세를 떼기 전 이익이고 감가상각비는 이미 비용으로 빠져 있습니다. EBITDA는 거기에 감가상각비와 무형자산상각비를 더한 값이라 항상 EBIT 이상입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EV/EBITDA 배수는 낮을수록 좋은가요</summary>
  <p style="margin:10px 0 0 0;">단정할 수 없습니다. 배수는 업종마다 수준이 달라서 같은 업종끼리 비교해야 의미가 있고, 이 글은 특정 종목의 높고 낮음을 판단하지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EBITDA 수치는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;"><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">DART 전자공시</a>의 사업보고서에서 영업이익, 감가상각비, 무형자산상각비를 찾아 더하면 됩니다. 증권사 리포트나 금융 정보 사이트가 계산해 둔 값을 쓸 때는 회사별로 산식이 다를 수 있으니 정의를 함께 확인하세요.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 - DART 전자공시시스템</a></li>
    <li><a href="https://www.venturesquare.net/835601/" target="_blank" rel="noopener">벤처스퀘어 - EBITDA와 영업 현금흐름의 차이</a></li>
    <li><a href="https://crediview.co.kr/blog/ebitda-vs-operating-profit" target="_blank" rel="noopener">크레디뷰 - EBITDA와 영업이익의 차이·계산법</a></li>
    <li><a href="https://support.stockplus.com/hc/ko/articles/5059492555673-%EC%96%B4%EB%A0%A4%EC%9B%8C%EB%B3%B4%EC%9D%B4%EC%A7%80%EB%A7%8C-%EC%89%AC%EC%9A%B4-EV-EBITDA" target="_blank" rel="noopener">증권플러스 - 어려워보이지만 쉬운 EV/EBITDA</a></li>
    <li><a href="https://www.tikr.com/ko/blog/ebitda-definition-formula-how-to-use-it" target="_blank" rel="noopener">TIKR - EBITDA 정의와 공식</a></li>
  </ul>
  기준일: 2026년 9월 기준. 계산 예시는 이해를 돕기 위한 가상의 숫자입니다. 기획재정부 시사경제용어사전 원문은 자동화 세션에서 접속이 막혀 검색으로 정의와 산식을 여러 출처에서 교차 확인했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 재무 지표의 계산과 해석을 설명하는 정보 글로, 특정 종목이나 상품을 사고팔라는 권유가 아닙니다. 지표의 산식은 자료마다 다를 수 있으니 실제 수치는 공시 원문으로 확인해 주세요. 투자에 따른 판단과 결과의 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "EBITDA 뜻과 영업이익 차이 계산법",
  "description": "EBITDA 뜻을 영업이익에 감가상각비를 더하는 공식으로 정리하고, 영업이익이 같은 가상의 두 회사로 EBITDA 마진과 EV/EBITDA 배수를 계산해 비교합니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-09-30",
  "dateModified": "2026-09-30",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/ebitda-meaning-operating-profit-difference"
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
      "name": "EBITDA가 높으면 현금을 많이 번다는 뜻인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. EBITDA는 재고와 외상 대금의 증감, 설비투자로 나간 현금을 반영하지 않습니다. 현금 창출력은 현금흐름표의 영업활동현금흐름과 CAPEX를 함께 봐야 확인됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "EBITDA는 손익계산서 어디에 나오나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "보통 별도 줄로 나오지 않습니다. 영업이익에 감가상각비와 무형자산상각비를 더해 직접 계산하는 경우가 많고, 이 두 항목은 현금흐름표나 주석에서 찾습니다."
      }
    },
    {
      "@type": "Question",
      "name": "EBITDA와 EBIT는 어떻게 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EBIT는 이자와 법인세를 떼기 전 이익이고 감가상각비는 이미 비용으로 빠져 있습니다. EBITDA는 거기에 감가상각비와 무형자산상각비를 더한 값이라 항상 EBIT 이상입니다."
      }
    },
    {
      "@type": "Question",
      "name": "EV/EBITDA 배수는 낮을수록 좋은가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "단정할 수 없습니다. 배수는 업종마다 수준이 달라서 같은 업종끼리 비교해야 의미가 있고, 이 글은 특정 종목의 높고 낮음을 판단하지 않습니다."
      }
    },
    {
      "@type": "Question",
      "name": "EBITDA 수치는 어디서 확인하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "DART 전자공시의 사업보고서에서 영업이익, 감가상각비, 무형자산상각비를 찾아 더하면 됩니다. 증권사 리포트나 금융 정보 사이트가 계산해 둔 값을 쓸 때는 회사별로 산식이 다를 수 있으니 정의를 함께 확인하세요."
      }
    }
  ]
}
</script>
