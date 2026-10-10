---
keyword: 국채금리 뜻
title: 국채금리 뜻과 채권가격 반비례 계산
slug: government-bond-yield-meaning
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 1970 (PC 400 / 모바일 1570)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-30 - 통과]
  WebSearch "국채금리 뜻 국채금리 오르면 주가 채권가격 반대" 상위 9개: tossbank.com(핀테크 은행 콘텐츠), brunch.co.kr(개인 블로그), eiec.kdi.re.kr(KDI 경제교육, 준정부),
  kbthink.com(KB 대형 금융사), kcie.or.kr(금융교육 기관), cidermics.com(경제 미디어), appastudy.com(개인 블로그), ecodemy.cafe24.com(개인 블로그), kr.tradingview.com(플랫폼 아이디어).
  1) 진입 여지: 있음. brunch·appastudy·ecodemy 등 개인 블로그가 상위에 3개 이상 섞여 SERP가 잠겨 있지 않다.
  2) 검색 의도: 뜻과 원리를 찾는 탐색형. 조회·계산기 의도가 아니다(현재 금리 조회는 별도 의도).
  3) 답 완결 여부: 부분적. 상위는 "금리와 채권가격은 반대"라는 결론을 말로 설명하지만, 같은 채권을 금리 2%·3%·4%에서 직접 현재가치로 계산하고 2년물과 10년물의 낙폭을 나란히 놓은 표는 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 액면 10,000원·표면금리 3%·연 1회 이자 채권의 2년물 가격표: 금리 2% 10,194.16원(+1.94%), 3% 10,000원, 4% 9,811.39원(-1.89%), 현금흐름별 할인 계산 과정 공개.
  (b) 같은 조건 10년물 가격표: 금리 2% 10,898.26원(+8.98%), 4% 9,188.91원(-8.11%). 금리 1%p 변화에 2년물 약 1.9%, 10년물 약 8~9% 움직여 만기가 길수록 민감하다는 대조.
  (c) 국채금리 vs 기준금리 비교표, bp 환산표(1bp=0.01%p, 25bp=0.25%p), 금리가 예금·대출·주식에 닿는 경로 목록.
primary_source: |
  KDI 경제교육·정보센터 「채권수익률과 가격결정」(eiec.kdi.re.kr) WebFetch 1회 시도, EGRESS_BLOCKED. 대신 WebSearch 2회로 서로 무관한 출처 5곳 이상을 교차 확인했다:
  KDI 경제교육(준정부, 검색 결과 요약만 확인), 토스뱅크, KB의 생각(kbthink), 사이다경제, 브런치, 아빠의 좌충우돌 경제공부, 에코데미.
  "국채금리는 채권을 사서 만기까지 보유할 때의 수익률(만기수익률)이고, 채권가격과 채권수익률은 역의 관계"라는 핵심 개념이 충돌 없이 일치했다.
  세율·한도 같은 법정 수치가 아니라 표준 채권 수학이고, 본문 가격은 전부 가상 채권을 현재가치 공식으로 직접 계산한 값이다. 실제 시장금리 수치는 쓰지 않았다.
기준일: 2026년 9월 기준 (계산 예시는 전부 가상)
tags: 국채금리 뜻, 국채금리란, 국채금리 오르면, 채권가격 금리 관계, 만기수익률, 국채 3년물 10년물, 기준금리 차이, bp 뜻, 채권 투자 기초, 채권 가격 계산
gate_pass: true
gate_pass_note: |
  게이트1 1,970회, 게이트2 v3 통과, 게이트3 가격 계산표(2년물·10년물) 확보, 게이트4 독립 출처 5곳 이상 교차검증(KDI 원문은 접속 불가).
  사람은 발행 전 KDI 경제교육 「채권수익률과 가격결정」에서 수익률과 가격이 역의 관계라는 문구만 한 번 대조하면 된다.
self_check: |
  [2026-09-30 gate_pass:true]
  후보 경위: backlog.verified의 대기 후보 중 콜옵션·풋옵션 뜻(1,590/1,550)을 먼저 SERP 확인했으나 상위 9개가 KB·토스뱅크·대신증권·유진선물·CME·나무위키뿐이라 개인 블로그 0개(탈락조건1)로 탈락, 상한가 뜻은 KRX 규정·기재부 사전·나무위키로 사전형이라 보류. 국채금리 뜻(1,970)은 개인 블로그 3개 이상이 섞여 통과해 채택.
  카니벌라이제이션: stock_drafts grep 결과 국채금리를 본문 주제로 다룬 글 없음(CAPEX·개인투자용국채는 언급만). 94편 듀레이션 뜻(가격 민감도 지표), 37편 채권 세금, 78편 개인투자용국채와는 내부 링크로 연결하되 각도가 다름(이 글은 금리의 정의, 기준금리와의 차이, bp, 가격 반비례의 첫 계산).
  수치 검산(python): 2년물 3% 이표 10,000원 기준 금리 2%: 300/1.02+10,300/1.0404=294.12+9,900.04=10,194.16, 금리 4%: 300/1.04+10,300/1.0816=288.46+9,522.93=9,811.39. 10년물 금리 2% 10,898.26, 4% 9,188.91. 변동률 +1.94%, -1.89%, +8.98%, -8.11%.
  YMYL: 종목·상품 추천, 금리 방향 전망, 매수매도 시점 없음. 실제 시장금리 수치 미사용, 가상 채권만 사용. "금리가 오르면 주가가 내린다"류 단정 없이 경로만 나열.
  기관 링크: 본문에서 링크할 승인 URL이 없는 한국은행 ECOS·금융투자협회 채권정보센터는 지어내지 않고 기관명만 표기. 출처 목록 5개는 WebSearch 결과에서 확인한 URL로 전부 링크 처리.
  제목 "국채금리 뜻과 채권가격 반비례 계산" 글자수 18자, 금지어 없음. 슬러그 4단어 영문 소문자 하이픈.
  첫 문장 유형: 결론형(금리가 오르면 가격이 내린다). 글 구조 유형: 계산 시연형(가상 채권 2종).
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 4개, FAQ 5개, H2 7개(목차 제외) 중 "~나요"형 1개.
  요약박스 청록색(#e6f4f1/#2e9c8a), 제목 "🧭 국채금리, 먼저 이것만". FAQ 헤딩 "국채금리를 처음 보는 사람이 묻는 것들". 면책 문구 새 표현.
figure_plan: "1장(현재 금리 막대). 나머지 표는 가상 채권 가격 계산표·bp 환산표라 정확한 숫자를 읽어야 해서 표가 낫다"
refresh_due: 2026-10-23
refresh_reason: "10/22 금통위 직후 금리 수치 갱신"
self_check_refresh: |
  [2026-10-10 갱신] 현재 수치 표 추가: 3년 3.933%·10년 4.369%(10/6 마감)는 SBS Biz와 핀포인트뉴스 두 곳이 같은 숫자를 보도해 통과(RULES 지표 수치 기준). 10/8 마감(3.983%/4.395%)은 SBS Biz 1곳뿐이라 쓰지 않음. 투자자 관점 H2, 그림 1장, 내부 링크(기준금리 글) 추가. lint 금지 어휘·메타 문장 수정.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-10</p>

<p>국채금리가 오르면 이미 발행된 국채의 가격은 내려갑니다. 국채금리는 국채를 사서 만기까지 들고 갈 때 얻는 연 수익률이고, 이자가 정해진 채권은 가격이 움직여야 수익률이 맞춰지기 때문입니다.</p>

<div style="background:#e6f4f1;border:2px solid #2e9c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6b5e;font-size:18px;">🧭 국채금리, 먼저 이것만</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>국채금리는 시장에서 거래되는 국채의 만기수익률이며, 한국은행이 정하는 기준금리와는 다른 금리입니다.</li><li>표면금리 3%짜리 2년 국채는 시장금리가 4%로 오르면 10,000원에서 9,811.39원으로 떨어집니다.</li><li>같은 조건에서 만기가 10년이면 낙폭이 8.11%로 커져서, 만기가 길수록 금리 변화에 민감합니다.</li></ul>
</div>

<h2 style="border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">국채금리는 무엇을 뜻하나요</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">국채금리와 기준금리 차이 비교</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">금리가 오르면 국채 가격이 내리는 계산</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">만기가 길수록 가격이 크게 흔들리는 이유</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">뉴스에 나오는 bp 읽는 법</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">국채금리가 예금, 대출, 주식에 닿는 경로</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">국채금리 확인하는 곳</a></li>
  <li><a href="#sec-8" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">국채금리를 처음 보는 사람이 묻는 것들</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">국채금리는 무엇을 뜻하나요</h2>

<p>국채금리는 정부가 발행한 채권을 시장에서 사고팔 때 형성되는 수익률입니다. 정확히는 지금 그 채권을 사서 만기까지 보유할 때 얻는 연 환산 수익률, 곧 만기수익률을 가리킵니다.</p>

<p>뉴스에서 "3년물 금리", "10년물 금리"라고 하면 만기가 3년, 10년인 국채의 이 수익률입니다. 만기마다 금리가 따로 있어서 국채금리는 숫자 하나가 아니라 만기별 여러 개입니다.</p>

<p>국채는 발행할 때 정한 이자(표면금리)를 만기까지 그대로 지급합니다. 그런데 시장에서 거래되는 가격은 매일 바뀝니다. <mark>이자는 고정이고 가격이 변하기 때문에, 국채금리는 가격이 바뀔 때마다 새로 계산되는 값</mark>입니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">국채금리와 기준금리 차이 비교</h2>

<p>국채금리와 기준금리는 이름이 비슷하지만 정하는 주체와 방식이 다릅니다. 기준금리는 한국은행 금융통화위원회가 회의에서 정하고, 국채금리는 시장의 매매로 정해집니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">기준금리</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">국채금리</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">누가 정하나</td><td style="border:1px solid #ddd;padding:8px;">한국은행 금융통화위원회</td><td style="border:1px solid #ddd;padding:8px;">시장 참가자의 매매</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">언제 바뀌나</td><td style="border:1px solid #ddd;padding:8px;">회의에서 결정할 때</td><td style="border:1px solid #ddd;padding:8px;">거래 시간 중 수시로</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">숫자 개수</td><td style="border:1px solid #ddd;padding:8px;">하나</td><td style="border:1px solid #ddd;padding:8px;">만기별로 여러 개(3년물, 10년물 등)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">성격</td><td style="border:1px solid #ddd;padding:8px;">정책 목표 금리</td><td style="border:1px solid #ddd;padding:8px;">시장이 매긴 수익률</td></tr>
  </tbody>
</table>

<p>두 금리는 서로 영향을 주고받지만 항상 같이 움직이지는 않습니다. 시장이 앞으로의 기준금리를 어떻게 볼지에 따라 국채금리가 먼저 움직이기도 합니다.</p>

<div style="background:#e6f4f1;border:2px solid #2e9c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6b5e;font-size:18px;">📝 한 줄로 기억하기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>회의로 정하면 기준금리, 시장이 정하면 국채금리입니다.</li><li>국채 기사에 나오는 "금리"는 대부분 국채금리를 뜻합니다.</li></ul>
</div>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">금리가 오르면 국채 가격이 내리는 계산</h2>

<p>가상의 국채로 직접 계산해 보겠습니다. 액면 10,000원, 표면금리 연 3%(이자 300원을 매년 1회 지급), 만기 2년인 채권입니다. 세금과 수수료는 넣지 않았습니다.</p>

<p>이 채권의 가격은 앞으로 받을 돈을 시장금리로 할인해 더한 값입니다. 시장금리가 4%로 오른 경우를 계산하면 아래와 같습니다.</p>

<ol style="line-height:1.9;">
  <li>1년 뒤 이자 300원을 4%로 할인: 300 ÷ 1.04 = 288.46원</li>
  <li>2년 뒤 이자와 원금 10,300원을 4%로 두 번 할인: 10,300 ÷ 1.0816 = 9,522.93원</li>
  <li>두 값의 합: 288.46 + 9,522.93 = <mark>9,811.39원</mark></li>
</ol>

<p>같은 방식으로 시장금리가 2%, 3%일 때도 계산하면 다음 표가 나옵니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">시장금리(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">채권 가격(2년물)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">액면 대비 변화</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2%</td><td style="border:1px solid #ddd;padding:8px;">10,194.16원</td><td style="border:1px solid #ddd;padding:8px;">+1.94%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3% (표면금리와 동일)</td><td style="border:1px solid #ddd;padding:8px;">10,000.00원</td><td style="border:1px solid #ddd;padding:8px;">0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">4%</td><td style="border:1px solid #ddd;padding:8px;">9,811.39원</td><td style="border:1px solid #ddd;padding:8px;">-1.89%</td></tr>
  </tbody>
</table>

<p>시장금리가 표면금리와 같은 3%이면 가격은 액면과 같습니다. 금리가 더 오르면 더 싼 값에 사야 수익률 4%가 맞고, 내리면 더 비싸게 거래됩니다.</p>

<p>이 반비례의 구조와 만기별 민감도를 수치로 재는 지표가 듀레이션입니다. 계산법은 <a href="https://sensitiveboss3.tistory.com/entry/duration-meaning-calculation" target="_blank" rel="noopener">듀레이션 뜻과 계산 방법</a>에서 따로 다뤘습니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">만기가 길수록 가격이 크게 흔들리는 이유</h2>

<p>같은 금리 변화라도 만기가 길수록 채권 가격은 더 크게 움직입니다. 낮은 이자를 받는 기간이 길어질수록 시장금리와의 차이가 오래 쌓이기 때문입니다.</p>

<p>앞의 채권과 조건은 같고 만기만 10년으로 늘린 경우를 계산했습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">시장금리(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2년물 가격</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">10년물 가격</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2%</td><td style="border:1px solid #ddd;padding:8px;">10,194.16원 (+1.94%)</td><td style="border:1px solid #ddd;padding:8px;">10,898.26원 (+8.98%)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3%</td><td style="border:1px solid #ddd;padding:8px;">10,000.00원</td><td style="border:1px solid #ddd;padding:8px;">10,000.00원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">4%</td><td style="border:1px solid #ddd;padding:8px;">9,811.39원 (-1.89%)</td><td style="border:1px solid #ddd;padding:8px;">9,188.91원 (-8.11%)</td></tr>
  </tbody>
</table>

<p><mark>금리가 3%에서 4%로 1%p 오르면 2년물은 1.89% 내리지만 10년물은 8.11% 내립니다.</mark> 뉴스에서 장기물 금리 변동을 더 크게 다루는 이유가 여기에 있습니다.</p>

<div style="background:#e6f4f1;border:2px solid #2e9c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6b5e;font-size:18px;">💡 계산 결과에서 읽을 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>만기까지 보유하면 원금과 약속된 이자를 받으므로, 가격 변동이 곧 손실로 확정되지는 않습니다.</li><li>중간에 팔 때만 그날의 시장 가격이 적용됩니다.</li><li>표의 금리와 가격은 이해를 돕기 위한 가상 값입니다.</li></ul>
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">뉴스에 나오는 bp 읽는 법</h2>

<p>bp(베이시스포인트)는 금리 변화를 나타내는 단위로, 1bp는 0.01%p입니다. 100bp가 1%p이고 25bp가 0.25%p입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">기사 표현</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">%p로 바꾸면</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">3.00%에서 움직인 뒤 금리(예시)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">1bp 상승</td><td style="border:1px solid #ddd;padding:8px;">0.01%p</td><td style="border:1px solid #ddd;padding:8px;">3.01%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">10bp 하락</td><td style="border:1px solid #ddd;padding:8px;">0.10%p</td><td style="border:1px solid #ddd;padding:8px;">2.90%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">25bp 상승</td><td style="border:1px solid #ddd;padding:8px;">0.25%p</td><td style="border:1px solid #ddd;padding:8px;">3.25%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">100bp 상승</td><td style="border:1px solid #ddd;padding:8px;">1.00%p</td><td style="border:1px solid #ddd;padding:8px;">4.00%</td></tr>
  </tbody>
</table>

<p>%와 %p는 다른 말입니다. 금리가 3%에서 4%로 올랐다면 1%p(100bp) 오른 것이고, 상승률로는 약 33.3%입니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">국채금리가 예금, 대출, 주식에 닿는 경로</h2>

<p>국채금리는 다른 금리를 매길 때 기준이 되는 값이라 여러 곳으로 번집니다. 이 경로가 곧 방향을 보장하지는 않으므로, 어디에 닿는지만 정리합니다.</p>

<ul style="line-height:1.9;">
  <li><strong>채권 시장:</strong> 이미 발행된 채권의 가격이 위 계산처럼 반대로 움직입니다.</li>
  <li><strong>예금과 대출:</strong> 금융기관이 자금을 조달하고 상품 금리를 정할 때 시장금리를 참고합니다.</li>
  <li><strong>기업 자금 조달:</strong> 회사채 금리는 국채금리에 기업의 신용 위험을 더해 형성되는 것이 일반적입니다.</li>
  <li><strong>주식 시장:</strong> 안전자산인 국채의 수익률이 달라지면 주식에 요구하는 수익률과 비교 기준도 달라집니다.</li>
</ul>

<p>주식 시장에 미치는 영향은 그때의 물가, 경기, 기업 실적에 따라 달라서 한 방향으로 정해져 있지 않습니다. 채권으로 얻는 이자에 붙는 세금은 <a href="https://sensitiveboss3.tistory.com/entry/bond-tax-guide" target="_blank" rel="noopener">채권 세금 얼마 떼나</a>에 정리했습니다.</p>

<h2 style="border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">지금 국고채 금리는 얼마인가요</h2>

<p>2026년 10월 6일 서울 채권시장 마감 기준 국고채 3년물은 연 3.933%, 10년물은 연 4.369%입니다. 10년물이 3년물보다 43.6bp 높습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead><tr style="background:#e6f4f1;"><th style="border:1px solid #ccc;padding:8px;">만기</th><th style="border:1px solid #ccc;padding:8px;">금리</th><th style="border:1px solid #ccc;padding:8px;">기준일</th></tr></thead>
  <tbody>
    <tr><td style="border:1px solid #ccc;padding:8px;">국고채 3년</td><td style="border:1px solid #ccc;padding:8px;">연 3.933%</td><td style="border:1px solid #ccc;padding:8px;">2026-10-06 마감</td></tr>
    <tr><td style="border:1px solid #ccc;padding:8px;">국고채 10년</td><td style="border:1px solid #ccc;padding:8px;">연 4.369%</td><td style="border:1px solid #ccc;padding:8px;">2026-10-06 마감</td></tr>
    <tr><td style="border:1px solid #ccc;padding:8px;">10년 - 3년</td><td style="border:1px solid #ccc;padding:8px;">43.6bp</td><td style="border:1px solid #ccc;padding:8px;">산술(4.369 - 3.933)</td></tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/government-bond-yield-meaning-1.png" alt="2026년 10월 6일 국고채 3년물 3.933%와 10년물 4.369% 비교 막대" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: <a href="https://biz.sbs.co.kr/article/20000338551" target="_blank" rel="noopener">SBS Biz</a>, <a href="https://www.pinpointnews.co.kr/news/articleView.html?idxno=493090" target="_blank" rel="noopener">핀포인트뉴스</a>, 2026-10-06 마감</figcaption></figure>

<p>금리는 매일 바뀌므로 이 표는 기준일의 값입니다. 오늘 값은 한국은행 경제통계시스템이나 증권사 앱에서 같은 만기끼리 비교해 보시면 됩니다. 다음 국고채 금리 갱신은 한국은행 금융통화위원회(2026-10-22) 이후로 잡았습니다.</p>

<h2 style="border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">국채금리 수준이 주식 투자자에게 중요한 이유</h2>

<p>국채금리는 주식에 요구하는 수익률의 비교 기준이라서, 주식 투자자는 이 숫자를 함께 봅니다. 10년물이 4.369%라면 위험이 거의 없는 국채가 연 4%대 수익을 주는 셈이므로, 주식은 그보다 높은 기대수익을 설명해야 합니다.</p>

<ul style="line-height:1.9;">
  <li><strong>성장주:</strong> 먼 미래의 이익을 현재 가치로 깎을 때 금리가 높을수록 할인폭이 커져 부담이 됩니다.</li>
  <li><strong>배당주:</strong> 배당수익률이 국채금리보다 낮아 보이면 비교 매력이 떨어졌다고 해석하는 시장 참여자가 많습니다.</li>
  <li><strong>대출 비중이 큰 기업:</strong> 회사채 금리가 국채금리에 연동되므로 이자 비용이 늘어납니다.</li>
</ul>

<p>이 경로가 실제 주가 방향으로 이어지는지는 물가, 경기, 실적에 따라 달라서 단정할 수 없습니다. 같은 금리 상승도 경기가 좋아서 오른 경우와 물가가 불안해서 오른 경우에 주식에 주는 의미가 다릅니다. 금리와 함께 <a href="https://sensitiveboss3.tistory.com/entry/base-rate-meaning-interest-calc" target="_blank" rel="noopener">기준금리 뜻과 이자 계산</a>도 같이 보면 흐름을 읽기 쉽습니다.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">국채금리 확인하는 곳</h2>

<ol style="line-height:1.9;">
  <li><strong>한국은행 경제통계시스템(ECOS):</strong> 국고채 만기별 시장금리의 일별, 월별 통계를 조회합니다.</li>
  <li><strong>금융투자협회 채권정보센터:</strong> 채권 종류별 최종호가 수익률을 확인합니다.</li>
  <li><strong>증권사 앱과 포털 금융 페이지:</strong> 3년물, 10년물 금리를 실시간에 가깝게 보여 줍니다.</li>
</ol>

<p>조회할 때는 <mark>어느 만기의 금리인지</mark> 먼저 확인합니다. 3년물과 10년물은 숫자가 다르고, 같은 날에도 서로 반대 방향으로 움직일 수 있습니다.</p>

<div style="background:#e6f4f1;border:2px solid #2e9c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6b5e;font-size:18px;">✅ 마무리 체크</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>국채금리는 시장이 정한 만기별 수익률이고 기준금리와 다릅니다.</li><li>금리가 오르면 국채 가격은 내리고, 만기가 길수록 그 폭이 큽니다.</li><li>기사 속 bp는 0.01%p 단위이며, 25bp는 0.25%p입니다.</li></ul>
</div>

<h2 id="sec-8" style="scroll-margin-top:72px;border-left:6px solid #2e9c8a;padding-left:12px;margin-top:36px;">국채금리를 처음 보는 사람이 묻는 것들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국채금리와 기준금리는 같은 금리인가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 기준금리는 한국은행 금융통화위원회가 정하고, 국채금리는 시장에서 국채가 거래되며 정해지는 만기수익률입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국채금리가 오르면 국채 가격은 왜 내리나요</summary>
  <p style="margin:10px 0 0 0;">국채의 이자는 발행 때 고정되기 때문입니다. 시장금리가 오르면 같은 이자를 주는 기존 채권의 매력이 줄어, 가격이 내려야 새 금리 수준의 수익률이 맞춰집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">1bp는 몇 %인가요</summary>
  <p style="margin:10px 0 0 0;">1bp는 0.01%p입니다. 100bp가 1%p이므로 25bp는 0.25%p, 50bp는 0.5%p입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국채금리는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">한국은행 경제통계시스템(ECOS)과 금융투자협회 채권정보센터에서 만기별 수익률을 조회할 수 있고, 증권사 앱에서도 3년물과 10년물 금리를 볼 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국채금리가 오르면 주가는 반드시 내리나요</summary>
  <p style="margin:10px 0 0 0;">정해진 방향은 없습니다. 같은 금리 상승이라도 그 원인이 경기 회복인지 물가 부담인지에 따라 주식 시장의 반응이 달라질 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://eiec.kdi.re.kr/material/clickView.do?click_yymm=201512&amp;cidx=1670" target="_blank" rel="noopener">KDI 경제교육·정보센터 - 채권수익률과 가격결정</a></li>
    <li><a href="https://www.tossbank.com/articles/bonds-and-base-rates" target="_blank" rel="noopener">토스뱅크 - 기준 금리가 내려갈 때, 채권가격은 올라간다</a></li>
    <li><a href="https://kbthink.com/main/asset-management/wealth-manage-tip/kbthink-original/202408/Relationshipbetween_bondprices_and_bondinterestrates.html" target="_blank" rel="noopener">KB의 생각 - 채권가격과 금리의 관계</a></li>
    <li><a href="https://cidermics.com/contents/detail/1429" target="_blank" rel="noopener">사이다경제 - 국채 금리 상승하면 국채 가격은 하락한다?</a></li>
    <li><a href="https://brunch.co.kr/@kys401/29" target="_blank" rel="noopener">브런치 - 왜 채권 가격이 오르면 금리는 떨어질까요</a></li>
  </ul>
  기준일: 2026년 9월 기준. 가격 계산 예시는 이해를 돕기 위한 가상의 채권이며 실제 시장금리가 아닙니다. KDI 원문은 자동화 세션에서 접속이 막혀 검색으로 개념을 여러 출처에서 교차 확인했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 채권과 금리의 원리를 설명하는 정보 글이며 특정 채권이나 투자 상품의 매수, 매도를 권하지 않습니다. 계산 예시는 가상의 숫자이니 실제 시장금리와 가격은 공식 통계로 확인해 주세요. 투자 결정과 그 결과는 투자자 본인의 몫입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "국채금리 뜻과 채권가격 반비례 계산",
  "description": "국채금리 뜻을 만기수익률로 정리하고, 기준금리와의 차이, 가상 채권 2년물과 10년물의 가격 계산, 뉴스 속 bp 읽는 법을 표로 설명합니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-09-30",
  "dateModified": "2026-10-10",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/government-bond-yield-meaning"
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
      "name": "국채금리와 기준금리는 같은 금리인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "다릅니다. 기준금리는 한국은행 금융통화위원회가 정하고, 국채금리는 시장에서 국채가 거래되며 정해지는 만기수익률입니다."
      }
    },
    {
      "@type": "Question",
      "name": "국채금리가 오르면 국채 가격은 왜 내리나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "국채의 이자는 발행 때 고정되기 때문입니다. 시장금리가 오르면 같은 이자를 주는 기존 채권의 매력이 줄어, 가격이 내려야 새 금리 수준의 수익률이 맞춰집니다."
      }
    },
    {
      "@type": "Question",
      "name": "1bp는 몇 %인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1bp는 0.01%p입니다. 100bp가 1%p이므로 25bp는 0.25%p, 50bp는 0.5%p입니다."
      }
    },
    {
      "@type": "Question",
      "name": "국채금리는 어디서 확인하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "한국은행 경제통계시스템(ECOS)과 금융투자협회 채권정보센터에서 만기별 수익률을 조회할 수 있고, 증권사 앱에서도 3년물과 10년물 금리를 볼 수 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "국채금리가 오르면 주가는 반드시 내리나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 방향은 없습니다. 같은 금리 상승이라도 그 원인이 경기 회복인지 물가 부담인지에 따라 주식 시장의 반응이 달라질 수 있습니다."
      }
    }
  ]
}
</script>
