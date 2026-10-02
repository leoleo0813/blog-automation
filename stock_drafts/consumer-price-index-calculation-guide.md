---
keyword: 소비자물가지수
title: 소비자물가지수 계산 방법과 보는 순서
slug: consumer-price-index-calculation-guide
keyword_class: human-assisted
publish_effort: oneclick
monthly_search_volume: 8460 (PC 3270 / 모바일 5190)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-29 - 통과]
  WebSearch "소비자물가지수 뜻 계산 방법 품목 가중치 근원물가 주가 영향" 상위 9개: kostat.go.kr 2건(공식 계산식·가중치 페이지),
  tossbank.com(핀테크 콘텐츠), ko.wikipedia.org, csr.co.kr(소규모), namu.wiki, mitrade.com(브로커 콘텐츠),
  trendmetriclab.com(소규모 콘텐츠), ecodemy.cafe24.com(개인 운영 사이트).
  1) 진입 여지: 있음. trendmetriclab, ecodemy, csr.co.kr 등 소규모·개인 콘텐츠가 상위에 섞여 있다.
  2) 검색 의도: 정의·계산 탐색형이 중심이다. 지수 조회 의도가 섞여 있으나 지배적이지 않다.
  3) 답 완결 여부: 부분적. 공식 페이지는 산식과 가중치 개념을 설명하지만, 가상 3개 부문으로 종합지수와 부문별 기여도를 직접
     계산하는 예시, 물가 3%를 구매력으로 옮긴 계산, 근원물가 두 종류(401개/309개)의 품목 범위 비교표, 2020→2022 가중치 변화표를
     한 글에서 보여주는 콘텐츠는 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 3개 부문 종합지수 계산(111.0 → 113.7, 상승률 약 2.4%)과 부문별 기여도 표(44%/33%/22%).
  (b) 물가 3% 구매력 계산(100만 원 → 103만 원, 구매력 약 97.1%).
  (c) 근원물가 두 지수 비교표(401개/309개)와 2020→2022 가중치 변화표(5개 부문).
primary_source: |
  국가데이터처 보도자료 "2022년 기준 소비자물가지수 가중치 개편 결과"(mods.go.kr 게시, 2023-12-19) 원문 화면을 사람이
  캡처해 확인했다(2026-10-02). 부문별 가중치 5개(131.3→144.7, 57.5→62.9, 106.0→110.6, 154.5→142.0, 53.9→45.6),
  "2023년 12월 소비자물가동향부터 2022년 기준 가중치 적용", 2023년 11월 전년누계비 3.6%(2022년 기준)와 3.7%(2020년 기준)가
  본문과 일치한다. 근원물가 401개, 458개 품목, 2020=100, 1,000분비는 사람이 올린 e-나라지표 엑셀(2026-10-02 갱신)로 확인했다. 309개(식료품·에너지 제외)는 엑셀에 품목 수가 없어 통계설명자료·
  아시아경제·더스쿠프·뉴스핌 검색 요약의 일치로 확인했다(원문 WebFetch는 EGRESS_BLOCKED).
기준일: 2026년 9월 기준 (가중치는 2022년 기준 가중치, 2023년 12월 동향부터 적용. 최근 물가 표는 e-나라지표 2026-10-02 갱신분. 계산 예시는 전부 가상)
tags: 소비자물가지수, 소비자물가지수 계산, 물가상승률 계산, 근원물가지수, CPI, 소비자물가 가중치, 물가지수 보는 법, 국가데이터처, 인플레이션, 구매력
gate_pass: true
gate_pass_note: |
  게이트1 8,460회, 게이트2 v3 통과, 게이트3 계산 예시·비교표 확보. 게이트4는 가중치 표·적용 시기·상승률을 사람이 올린 원문
  캡처로 대조 완료(2026-10-02). 남은 확인은 식료품·에너지 제외지수 309개 품목 수(검색 요약 다수 일치)뿐이며 발행을 막을 정도는 아니다.
  원문 게시일이 2023-12-19라 본문은 "2023년 12월 적용분"으로 한정해 서술하고 이후 개편 여부는 최신 공지 확인을 안내했다.
capture_guide: ""
self_check: |
  [2026-09-29 작성, 2026-10-02 원문 캡처 대조 후 gate_pass:true]
  후보 경위: 신규 8개 실측(소비자물가지수 8,460 PASS / PMI 지수 520 PASS / 기준금리 뜻 1,330 PASS / 사업보고서 보는법 50,
  분기보고서 60, 종가베팅 20, 경상수지 20, 금리인하 주식 20 FAIL). 검색량 최고인 소비자물가지수를 채택했고
  PMI 지수·기준금리 뜻은 백로그 대기.
  카니벌라이제이션: 기존 99편 중 소비자물가·CPI 전용 편 없음(grep 소비자물가 0건, CPI 0건).
  YMYL: 종목 추천·목표가·매매시점 없음. 계산 예시는 전부 가상. 주식시장 영향은 "단정할 수 없다"로 한정.
  기관 링크: 기관 안내 문장 4개(소비자물가지수 페이지, e-나라지표, 계산식 설명, 보도자료) 전부 링크, 출처 목록 5개 전부 링크.
  제목 "소비자물가지수 계산 방법과 보는 순서" 19자, 금지어 없음. 슬러그 영문 소문자 하이픈 5단어.
  첫 문장 유형: 결론형 정의문. 직전 99편 결론형과 유사하나 수치·구조가 다름.
  글 구조 유형: 절차형(본문 첫 섹션을 ol 5단계로 시작). 직전 99·98·97편(비교·계산·비교)과 다름.
  발표 시기는 "매월 발표"로만 적고 요일·일자는 적지 않았다(미확인).
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 4개, FAQ 5개, H2 6개 중 "~나요"형 0개(FAQ 질문 제외).
  요약박스 황토색(#fff6e8/#d98200), 제목 "🧮 물가 숫자, 이것만 챙기세요". FAQ 헤딩 "물가 지표, 자주 걸리는 질문". 면책 문구 새 표현. 헤지 표현 최소화.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-29</p>

<p>소비자물가지수는 458개 품목의 가격 변화를 도시 가구의 평균 지출 비중으로 가중 평균해 2020년을 100으로 나타낸 수치입니다. 뉴스에 나오는 물가상승률은 이 지수가 전년 동월보다 몇 퍼센트 변했는지를 계산한 값입니다. 이 글은 계산 방법과 근원물가지수, 가중치 개편까지 확인하는 순서대로 정리합니다.</p>

<div style="background:#fff6e8;border:2px solid #d98200;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8a4f00;font-size:18px;">🧮 물가 숫자, 이것만 챙기세요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>소비자물가지수는 2020년 평균을 100으로 잡고, 458개 대표품목에 가중치(총합 1,000)를 곱해 합산합니다.</li>
    <li>물가상승률은 (당월 지수 ÷ 전년 동월 지수 − 1) × 100으로 구합니다.</li>
    <li>근원물가지수는 변동이 큰 품목을 뺀 별도 지수이고, 401개 품목형과 309개 품목형 두 종류가 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>물가 뉴스를 읽는 5단계 순서</li>
  <li>지수는 어떻게 계산하는가</li>
  <li>물가상승률 3%가 내 돈에 뜻하는 것</li>
  <li>최근 물가상승률 흐름 표로 보기</li>
  <li>근원물가지수가 따로 있는 이유</li>
  <li>가중치 개편으로 달라진 것</li>
  <li>물가 지표, 자주 걸리는 질문</li>
</ol>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">물가 뉴스를 읽는 5단계 순서</h2>
<p>물가 기사는 아래 다섯 단계로 나눠 읽으면 숫자가 서로 헷갈리지 않습니다.</p>
<ol style="line-height:1.9;">
  <li><strong>지수 수준 확인:</strong> 2020년 평균이 100이므로 지수가 115면 2020년보다 15% 높은 물가 수준입니다.</li>
  <li><strong>전년 동월 대비 변화율 확인:</strong> 기사 제목의 "물가 3.0% 상승"이 이 값입니다.</li>
  <li><strong>근원물가 확인:</strong> 농산물·석유류 같은 변동 품목을 뺀 흐름을 함께 봅니다.</li>
  <li><strong>부문별 확인:</strong> 음식·숙박, 교통처럼 어느 부문이 지수를 끌어올렸는지 봅니다.</li>
  <li><strong>원자료 확인:</strong> 국가데이터처 <a href="https://kostat.go.kr/cpi/" target="_blank" rel="noopener">소비자물가지수 페이지</a>와 <a href="https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1060" target="_blank" rel="noopener">e-나라지표</a>에서 최신 값을 확인합니다.</li>
</ol>
<p>국가데이터처는 옛 통계청이며, 소비자물가지수를 매월 발표합니다. 최신 수치는 위 링크에서 직접 확인하시고, 이 글의 계산 예시는 모두 가상의 숫자입니다.</p>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">지수는 어떻게 계산하는가</h2>
<p>종합지수는 품목별 지수에 가중치를 곱해 전부 더한 뒤 가중치 총합으로 나눠 구합니다. 가중치 총합은 1,000입니다. 계산 원리는 국가데이터처 <a href="https://kostat.go.kr/menu.es?mid=b70101050000" target="_blank" rel="noopener">계산식 설명</a>에서 볼 수 있습니다.</p>
<p>아래는 이해를 돕기 위해 만든 가상의 3개 부문 예시입니다. 실제 부문 지수가 아닙니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가상 부문</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가중치</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">작년 지수</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">올해 지수</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">부문 상승률</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">A</td><td style="border:1px solid #ddd;padding:8px;">400</td><td style="border:1px solid #ddd;padding:8px;">105</td><td style="border:1px solid #ddd;padding:8px;">108</td><td style="border:1px solid #ddd;padding:8px;">약 2.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">B</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">110</td><td style="border:1px solid #ddd;padding:8px;">113</td><td style="border:1px solid #ddd;padding:8px;">약 2.7%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">C</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">120</td><td style="border:1px solid #ddd;padding:8px;">122</td><td style="border:1px solid #ddd;padding:8px;">약 1.7%</td></tr>
  </tbody>
</table>
<p>작년 종합지수는 (400×105 + 300×110 + 300×120) ÷ 1,000 = <mark>111.0</mark>입니다. 올해는 (400×108 + 300×113 + 300×122) ÷ 1,000 = 113.7이어서 상승률은 약 2.4%입니다.</p>
<p>지수가 2.7포인트 오른 몫을 부문별로 나누면 차이가 드러납니다. 상승률이 가장 큰 부문은 A지만, 가중치가 큰 만큼 종합지수를 밀어 올린 힘도 A가 가장 셉니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가상 부문</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가중치 × 지수 변화</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">종합지수 기여(포인트)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">기여 비중</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">A</td><td style="border:1px solid #ddd;padding:8px;">400 × 3 ÷ 1,000</td><td style="border:1px solid #ddd;padding:8px;">1.2</td><td style="border:1px solid #ddd;padding:8px;">약 44%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">B</td><td style="border:1px solid #ddd;padding:8px;">300 × 3 ÷ 1,000</td><td style="border:1px solid #ddd;padding:8px;">0.9</td><td style="border:1px solid #ddd;padding:8px;">약 33%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">C</td><td style="border:1px solid #ddd;padding:8px;">300 × 2 ÷ 1,000</td><td style="border:1px solid #ddd;padding:8px;">0.6</td><td style="border:1px solid #ddd;padding:8px;">약 22%</td></tr>
  </tbody>
</table>
<div style="background:#fff6e8;border:2px solid #d98200;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8a4f00;font-size:18px;">📝 계산할 때 주의할 점</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>가중치는 품목이 전체 소비지출에서 차지하는 비중이라, 같은 10% 가격 상승도 가중치가 큰 품목일수록 종합지수를 더 많이 움직입니다.</li>
    <li>종합지수 상승률은 부문 상승률의 단순 평균이 아니라 가중 평균입니다. 위 예시는 두 값이 우연히 비슷하지만, 가중치가 한쪽으로 쏠리면 크게 벌어지므로 기여도 표로 확인하세요.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">물가상승률 3%가 내 돈에 뜻하는 것</h2>
<p>물가상승률은 지수의 전년 동월 대비 변화율이고, 공식은 (당월 지수 ÷ 전년 동월 지수 − 1) × 100입니다. 전년 동월 지수가 110.0이고 당월 지수가 113.3이면 <mark>3.0%</mark>입니다.</p>
<p>이 3%를 현금의 구매력으로 옮겨 보면 감이 옵니다. 가상의 사례입니다.</p>
<ul style="line-height:1.9;">
  <li>1년 전 100만 원이던 장바구니는 물가가 3% 오르면 103만 원이 됩니다.</li>
  <li>같은 100만 원으로는 그 장바구니의 약 97.1%(100 ÷ 1.03)만 살 수 있습니다.</li>
  <li>은행 이자율이 물가상승률보다 낮으면 명목 금액은 늘어도 살 수 있는 양은 줄어듭니다.</li>
</ul>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">최근 물가상승률 흐름 표로 보기</h2>
<p>2026년 9월 소비자물가상승률은 전년 동월 대비 2.9%였고, 같은 달 근원물가는 2.7%, 생활물가는 2.5%였습니다. 아래 표는 e-나라지표에 게시된 전년비·전년동월비 수치입니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">연도</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">소비자물가</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">근원물가</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">생활물가</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2021</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td><td style="border:1px solid #ddd;padding:8px;">1.8%</td><td style="border:1px solid #ddd;padding:8px;">3.2%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022</td><td style="border:1px solid #ddd;padding:8px;">5.1%</td><td style="border:1px solid #ddd;padding:8px;">4.1%</td><td style="border:1px solid #ddd;padding:8px;">6.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2023</td><td style="border:1px solid #ddd;padding:8px;">3.6%</td><td style="border:1px solid #ddd;padding:8px;">4.0%</td><td style="border:1px solid #ddd;padding:8px;">3.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2024</td><td style="border:1px solid #ddd;padding:8px;">2.3%</td><td style="border:1px solid #ddd;padding:8px;">2.1%</td><td style="border:1px solid #ddd;padding:8px;">2.7%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2025</td><td style="border:1px solid #ddd;padding:8px;">2.1%</td><td style="border:1px solid #ddd;padding:8px;">2.2%</td><td style="border:1px solid #ddd;padding:8px;">2.4%</td></tr>
  </tbody>
</table>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2026년</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">소비자물가</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">근원물가</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">생활물가</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">4월</td><td style="border:1px solid #ddd;padding:8px;">2.6%</td><td style="border:1px solid #ddd;padding:8px;">2.2%</td><td style="border:1px solid #ddd;padding:8px;">2.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5월</td><td style="border:1px solid #ddd;padding:8px;">3.1%</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td><td style="border:1px solid #ddd;padding:8px;">3.3%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">6월</td><td style="border:1px solid #ddd;padding:8px;">3.2%</td><td style="border:1px solid #ddd;padding:8px;">2.4%</td><td style="border:1px solid #ddd;padding:8px;">3.4%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">7월</td><td style="border:1px solid #ddd;padding:8px;">2.8%</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">8월</td><td style="border:1px solid #ddd;padding:8px;">3.1%</td><td style="border:1px solid #ddd;padding:8px;">3.1%</td><td style="border:1px solid #ddd;padding:8px;">3.2%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">9월</td><td style="border:1px solid #ddd;padding:8px;"><mark>2.9%</mark></td><td style="border:1px solid #ddd;padding:8px;">2.7%</td><td style="border:1px solid #ddd;padding:8px;">2.5%</td></tr>
  </tbody>
</table>
<p>2022년에는 소비자물가가 5.1%, 생활물가가 6.0%까지 올랐고 2024년부터는 2%대로 내려왔습니다. 2026년 4월부터 9월까지는 2.6%에서 3.2% 사이를 오갔습니다.</p>
<p>생활물가지수는 소비자가 자주 구입하는 기본 생필품 144개 품목으로 만든 지수입니다. 이 표의 "근원물가"는 e-나라지표 설명 기준으로 농산물 및 석유류 제외지수입니다. 최신 값은 <a href="https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1060" target="_blank" rel="noopener">e-나라지표</a>에서 확인하세요.</p>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">근원물가지수가 따로 있는 이유</h2>
<p>근원물가지수는 날씨나 국제유가처럼 일시적 요인으로 크게 출렁이는 품목을 빼고 물가의 기조를 보려는 지표입니다. 우리나라는 두 가지 방식으로 작성합니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">농산물·석유류 제외지수</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">식료품·에너지 제외지수</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">작성 품목 수</td><td style="border:1px solid #ddd;padding:8px;">458개 중 401개</td><td style="border:1px solid #ddd;padding:8px;">458개 중 309개</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">성격</td><td style="border:1px solid #ddd;padding:8px;">우리나라 방식(2000년 2월부터 작성)</td><td style="border:1px solid #ddd;padding:8px;">OECD 국제 기준 방식(2010년 기준 지수부터 추가)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">빠지는 품목 예</td><td style="border:1px solid #ddd;padding:8px;">농산물, 석유류</td><td style="border:1px solid #ddd;padding:8px;">식료품 전반, 에너지(전기료, 지역난방비 등)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">빵·곡류·육류·과자</td><td style="border:1px solid #ddd;padding:8px;">포함</td><td style="border:1px solid #ddd;padding:8px;">제외</td></tr>
  </tbody>
</table>
<p>식료품·에너지 제외지수가 더 넓게 빼기 때문에 두 지수의 상승률이 다르게 나오는 달이 있습니다. 기사에서 "근원물가"라고만 적혀 있으면 어느 쪽인지 본문에서 확인해야 합니다.</p>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">가중치 개편으로 달라진 것</h2>
<p>국가데이터처(당시 통계청)는 2023년 12월 19일 보도자료에서 2022년 소비 구조를 반영한 가중치를 2023년 12월 소비자물가동향부터 적용한다고 발표했습니다. 이후 추가 개편이 있었는지는 국가데이터처 최신 공지에서 확인하세요. 가중치가 커진 부문과 작아진 부문은 아래와 같습니다. 출처는 <a href="https://kostat.go.kr/board.es?mid=a10301040200&amp;bid=213&amp;act=view&amp;list_no=428549" target="_blank" rel="noopener">국가데이터처 보도자료</a>입니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">부문</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2020년 기준 가중치</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2022년 기준 가중치</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">변화</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">음식 및 숙박</td><td style="border:1px solid #ddd;padding:8px;">131.3</td><td style="border:1px solid #ddd;padding:8px;">144.7</td><td style="border:1px solid #ddd;padding:8px;">증가</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">오락 및 문화</td><td style="border:1px solid #ddd;padding:8px;">57.5</td><td style="border:1px solid #ddd;padding:8px;">62.9</td><td style="border:1px solid #ddd;padding:8px;">증가</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">교통</td><td style="border:1px solid #ddd;padding:8px;">106.0</td><td style="border:1px solid #ddd;padding:8px;">110.6</td><td style="border:1px solid #ddd;padding:8px;">증가</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">식료품 및 비주류음료</td><td style="border:1px solid #ddd;padding:8px;">154.5</td><td style="border:1px solid #ddd;padding:8px;">142.0</td><td style="border:1px solid #ddd;padding:8px;">감소</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">가정용품 및 가사서비스</td><td style="border:1px solid #ddd;padding:8px;">53.9</td><td style="border:1px solid #ddd;padding:8px;">45.6</td><td style="border:1px solid #ddd;padding:8px;">감소</td></tr>
  </tbody>
</table>
<p>보도자료는 2020년 코로나19 영향으로 커졌던 식료품·보건·가정용품 비중이 줄고, 교육·교통·오락 비중이 다시 늘었다고 설명합니다. 같은 자료에서 2023년 11월 전년누계비 상승률은 2022년 기준 가중치로 <mark>3.6%</mark>, 2020년 기준으로는 3.7%였습니다.</p>
<p>가중치를 바꿔도 결과 차이는 0.1%p에 그쳤습니다. 부문별 기여도를 볼 때는 어느 해 가중치인지 확인해야 합니다.</p>

<h2 style="border-left:6px solid #d98200;padding-left:12px;margin-top:36px;">물가 지표, 자주 걸리는 질문</h2>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">소비자물가지수와 소비자물가상승률은 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 소비자물가지수는 2020년을 100으로 놓은 수준 값이고, 소비자물가상승률은 그 지수가 전년 동월보다 몇 퍼센트 변했는지 계산한 값입니다. 뉴스에서 말하는 "물가 3% 상승"은 후자입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">내가 느끼는 물가와 지수가 다른 이유는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">지수는 458개 품목을 도시 가구의 평균 소비 비중(가중치)으로 합산한 값이고, 특정 가구나 계층을 기준으로 하지 않기 때문입니다. 월세, 자녀 교육비, 차량 유지비처럼 내 지출 비중이 평균과 다르면 체감과 지수가 벌어질 수 있고, 체감에 가까운 별도 지표로 생활물가지수(144개 품목)가 있습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">미국 CPI와 한국 소비자물가지수는 같은 지표인가요</summary>
  <p style="margin:10px 0 0 0;">이름은 비슷하지만 나라별로 따로 만드는 별개 지표입니다. 한국은 국가데이터처가 산출하고, 조사 품목과 가중치도 각국의 소비 구조에 맞춰 다릅니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">물가지수가 오르면 주식시장은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">방향을 단정할 수 없습니다. 물가가 예상보다 높으면 금리 인하 기대가 약해져 시장이 흔들리는 경우가 있지만, 반대로 움직이는 시기도 있습니다. 이 글은 지표를 읽는 법만 다루며 투자 판단을 제시하지 않습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">지수가 2020년 기준인데 가중치는 2022년 기준이라는 말이 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">지수의 기준 시점(2020년 평균=100)과 품목별 비중을 정하는 기준 시점은 따로 바뀔 수 있습니다. 국가데이터처는 2022년 소비 구조를 반영한 가중치를 2023년 12월 동향부터 적용했다고 발표했습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://kostat.go.kr/cpi/" target="_blank" rel="noopener">국가데이터처 - 소비자물가지수</a></li>
    <li><a href="https://kostat.go.kr/menu.es?mid=b70101050000" target="_blank" rel="noopener">국가데이터처 - 소비자물가지수 계산식 및 계산방법</a></li>
    <li><a href="https://kostat.go.kr/board.es?mid=a10301040200&amp;bid=213&amp;act=view&amp;list_no=428549" target="_blank" rel="noopener">국가데이터처 - 2022년 기준 소비자물가지수 가중치 개편 결과</a></li>
    <li><a href="https://www.korea.kr/briefing/pressReleaseView.do?newsId=156606275" target="_blank" rel="noopener">대한민국 정책브리핑 - 2022년 기준 소비자물가지수 가중치 개편 결과</a></li>
    <li><a href="https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1060" target="_blank" rel="noopener">e-나라지표 - 소비자물가 및 생활물가지수 설명</a></li>
  </ul>
  기준일: 2026년 9월 물가 기준(e-나라지표 2026-10-02 갱신). 본문의 계산 예시(부문 지수, 가중치, 1년 전 100만 원 장바구니)는 이해를 돕기 위한 가상의 숫자이며 실제 통계가 아닙니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 통계 지표를 읽는 방법을 정리한 정보 글이며 특정 종목이나 상품을 사고팔라는 권유가 아닙니다. 지수 값과 가중치는 개편될 수 있으니 최신 수치는 국가데이터처에서 직접 확인해 주세요. 투자 판단과 그 결과는 투자자 본인의 몫입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "소비자물가지수 계산 방법과 보는 순서",
  "description": "소비자물가지수의 뜻과 계산 방법, 가상 예시로 보는 물가상승률, 근원물가지수 두 종류, 2022년 기준 가중치 개편까지 확인 순서대로 정리합니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-09-29",
  "dateModified": "2026-09-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/consumer-price-index-calculation-guide"
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
      "name": "소비자물가지수와 소비자물가상승률은 같은 건가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "다릅니다. 소비자물가지수는 2020년을 100으로 놓은 수준 값이고, 소비자물가상승률은 그 지수가 전년 동월보다 몇 퍼센트 변했는지 계산한 값입니다. 뉴스에서 말하는 \"물가 3% 상승\"은 후자입니다."
      }
    },
    {
      "@type": "Question",
      "name": "내가 느끼는 물가와 지수가 다른 이유는 무엇인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "지수는 458개 품목을 도시 가구의 평균 소비 비중(가중치)으로 합산한 값이고, 특정 가구나 계층을 기준으로 하지 않기 때문입니다. 월세, 자녀 교육비, 차량 유지비처럼 내 지출 비중이 평균과 다르면 체감과 지수가 벌어질 수 있고, 체감에 가까운 별도 지표로 생활물가지수(144개 품목)가 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "미국 CPI와 한국 소비자물가지수는 같은 지표인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이름은 비슷하지만 나라별로 따로 만드는 별개 지표입니다. 한국은 국가데이터처가 산출하고, 조사 품목과 가중치도 각국의 소비 구조에 맞춰 다릅니다."
      }
    },
    {
      "@type": "Question",
      "name": "물가지수가 오르면 주식시장은 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "방향을 단정할 수 없습니다. 물가가 예상보다 높으면 금리 인하 기대가 약해져 시장이 흔들리는 경우가 있지만, 반대로 움직이는 시기도 있습니다. 이 글은 지표를 읽는 법만 다루며 투자 판단을 제시하지 않습니다."
      }
    },
    {
      "@type": "Question",
      "name": "지수가 2020년 기준인데 가중치는 2022년 기준이라는 말이 무슨 뜻인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "지수의 기준 시점(2020년 평균=100)과 품목별 비중을 정하는 기준 시점은 따로 바뀔 수 있습니다. 국가데이터처는 2022년 소비 구조를 반영한 가중치를 2023년 12월 동향부터 적용했다고 발표했습니다."
      }
    }
  ]
}
</script>

