---
keyword: 생산자물가지수
title: 생산자물가지수 뜻과 소비자물가 차이
slug: producer-price-index-cpi-difference
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 2700 (PC 1540 / 모바일 1160)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-30 - 통과]
  WebSearch "생산자물가지수 뜻 소비자물가 차이 PPI 발표" 상위 9개: m.kbam.co.kr(자산운용사 콘텐츠), mofe.go.kr(기획재정부 시사경제용어사전, 공식),
  cmegroup.com(거래소 교육), gklibrarykor.com(소규모 개인 콘텐츠), hyperrich.co.kr(소규모 개인 콘텐츠), a-ha.io(Q&A 커뮤니티), kr.tradingview.com(시세 페이지), arxiv 2건은 무관.
  1) 진입 여지: 있음. gklibrarykor, hyperrich 같은 소규모 콘텐츠와 a-ha 커뮤니티가 상위에 섞여 있다.
  2) 검색 의도: 뜻과 차이를 찾는 탐색형. 지수 조회 의도(tradingview)가 일부 섞였으나 지배적이지 않다.
  3) 답 완결 여부: 부분적. 상위는 정의와 CPI 대비 범위 차이를 말로 설명하지만, 가중 평균 계산 과정, 전월·전년 동월 상승률 계산, 원재료 비중으로 본 원가 전가 계산, 원재료·중간재·최종재 구분표를 한 글에서 보여 주는 콘텐츠는 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가중 평균 계산표(쌀·햄버거·휘발유, 합계 114,214 ÷ 1,000 = 약 114.2). 출처는 부산시 물가지수 설명의 작성 예.
  (b) 가상 전년 동월비 3.0%, 전월비 약 1.0% 계산 과정.
  (c) 원재료 비중 30%, 10% 상승 시 원가 3% 상승 계산(가상).
  (d) 생산자 vs 소비자 물가지수 범위 비교표와 원재료·중간재·최종재 구분표.
primary_source: |
  기획재정부 시사경제용어사전(mofe.go.kr) WebFetch 1회 시도, EGRESS_BLOCKED(한국은행·통계 원문도 같은 세션 제한으로 직접 열지 못함).
  대신 WebSearch 4회로 서로 다른 출처를 교차 확인했다:
  정의·범위 차이: 기획재정부 시사경제용어사전, CME Group, 한국은행 자료 요약, 부산시 설명이 같은 방향.
  기준연도 2020년, 조사 품목 884개(개편 당시)에서 886개(2025년): 이데일리·이투데이 보도, 공공데이터포털 한국은행 생산자물가조사 안내가 일치.
  원재료·중간재·최종재 구분과 월별 잠정치 공개: 한국은행 보도자료(2026년 1·4·7월), KDI 경제교육정보센터 게시분, 헤럴드경제가 일치.
  세율·한도가 아닌 통계 지표 설명이며, 최신 월의 실제 지수값은 일부러 쓰지 않았다.
기준일: 2026년 9월 기준 (품목 수 886개는 2025년 기준, 계산 예시는 가상)
tags: 생산자물가지수, 생산자물가지수 뜻, PPI, 소비자물가지수 차이, 물가지수 계산, 국내공급물가지수, 원재료 중간재 최종재, 한국은행 물가, 인플레이션, 물가 선행지표
gate_pass: true
gate_pass_note: |
  게이트1 2,730회, 게이트2 v3 통과, 게이트3 계산표·비교표 확보, 게이트4 원문 접속 불가이나 독립 출처 4곳 이상 교차검증.
  사람은 한국은행 생산자물가지수 페이지에서 기준연도 2020년, 조사 품목 886개, 원재료·중간재·최종재 구분만 대조하면 됩니다.
self_check: |
  [2026-09-30 gate_pass:true]
  후보 경위: backlog.verified의 생산자물가지수(2,730회, 오늘 실측)를 채택. 이번 실행은 같은 날 실측값이라 check-keywords 재실행 생략.
  카니벌라이제이션: 기존 106편에서 생산자물가 grep 0건. 100편(소비자물가지수)·101편(PCE)과는 지표 범위 비교로 차별화, 본문에서 재계산하지 않음.
  YMYL: 종목 추천·목표가·매매시점 없음. 계산 예시는 가상 또는 출처 명시. 주가 영향은 "단정할 수 없다"로 한정.
  기관 링크: 기관 안내 문장 전부 링크, 출처 목록 6개 전부 링크.
  제목 "생산자물가지수 뜻과 소비자물가 차이" 18자, 금지어 없음. 슬러그 영문 소문자 하이픈 5단어.
  발표일은 "매월 잠정치 공개"로만 적고 일자는 적지 않음(미확인). 최신 월 지수값은 쓰지 않음. 2026년 6월 상승률(원재료 2.1%, 중간재·최종재 0.5%)은 검색 요약 기반이라 사람 대조 권장.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 4개, FAQ 5개, H2 6개 중 "~나요"형 0개(FAQ 질문 제외). 요약박스 초록색(#eef8f1/#3a9a5b), 제목 "🏭 공장 문 앞 물가, 핵심 세 줄". FAQ 헤딩 "물가 지표 헷갈릴 때 보는 질문 5개". 면책 문구 새 표현.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-30</p>

<p>생산자물가지수는 한국은행이 국내 생산자가 국내시장에 내놓는 상품과 서비스의 출하 가격 변화를 재서 2020년을 100으로 나타낸 지표입니다. 소비자가 매장에서 내는 가격이 아니라 기업끼리 거래하는 1차 단계 가격을 본다는 점이 소비자물가지수와 다릅니다. 이 글은 두 지표의 범위 차이와 계산 방식, 뉴스에 나오는 원재료·중간재·최종재 구분을 순서대로 정리합니다.</p>

<div style="background:#eef8f1;border:2px solid #3a9a5b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e38;font-size:18px;">🏭 공장 문 앞 물가, 핵심 세 줄</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>생산자물가지수는 한국은행이 작성하며, 기준연도는 2020년(=100)이고 2025년 기준 조사 품목은 886개입니다.</li>
    <li>소비자물가지수가 가계 구매가격이라면, 생산자물가지수는 원재료·중간재·자본재와 기업용 서비스까지 포함한 기업 간 거래가격입니다.</li>
    <li>종합지수는 품목별 지수에 가중치를 곱해 합산한 가중 평균이고, 전년 동월 대비 변화율이 뉴스 속 상승률입니다.</li>
    </ul>
</div>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>생산자물가지수가 재는 것</li>
  <li>소비자물가지수와 범위 비교</li>
  <li>가중 평균 계산 예시</li>
  <li>원재료, 중간재, 최종재 구분</li>
  <li>소비자물가로 번지는 경로</li>
  <li>가중치 개편과 자주 받는 질문</li>
</ol>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">생산자물가지수가 재는 것</h2>
<p>생산자물가지수는 국내에서 생산된 상품과 기업서비스가 국내시장에 출하될 때 1차 단계에서 기업끼리 거래한 가격의 변동을 측정합니다. 작성 기관은 한국은행이고, 조사 설명은 <a href="https://www.data.go.kr/data/15059642/openapi.do" target="_blank" rel="noopener">공공데이터포털 한국은행 생산자물가조사</a>와 <a href="https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1061" target="_blank" rel="noopener">e-나라지표 생산자물가지수</a>에서 볼 수 있습니다.</p>
<p>기준연도는 2020년입니다. 2020년 평균을 100으로 놓기 때문에 지수가 120이면 2020년보다 <mark>20% 높은 가격 수준</mark>이라는 뜻입니다.</p>
<ul style="line-height:1.9;">
  <li>조사 품목 수는 2020년 기준 개편 때 884개였고, 이후 2개가 늘어 2025년 기준 886개입니다.</li>
  <li>품목은 해마다 일부 조정되므로 최신 개수는 한국은행 자료에서 확인해야 합니다.</li>
  <li>월별 잠정치는 <a href="https://www.bok.or.kr/portal/bbs/B0000501/view.do?nttId=10098068&amp;menuNo=200690" target="_blank" rel="noopener">한국은행 생산자물가지수 보도자료</a>로 공개됩니다.</li>
</ul>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">소비자물가지수와 범위 비교</h2>
<p>두 지표의 가장 큰 차이는 누구의 거래가격을 보느냐입니다. 소비자물가지수는 가구가 사는 가격이고, 생산자물가지수는 생산자가 파는 가격입니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">생산자물가지수</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">소비자물가지수</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">작성 기관</td><td style="border:1px solid #ddd;padding:8px;">한국은행</td><td style="border:1px solid #ddd;padding:8px;">국가데이터처(옛 통계청)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">측정 단계</td><td style="border:1px solid #ddd;padding:8px;">생산자의 1차 출하 거래가격</td><td style="border:1px solid #ddd;padding:8px;">소비자가 지불하는 구입가격</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">상품 범위</td><td style="border:1px solid #ddd;padding:8px;">소비재, 자본재, 원재료, 중간재</td><td style="border:1px solid #ddd;padding:8px;">소비재 중심</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">서비스 범위</td><td style="border:1px solid #ddd;padding:8px;">주로 기업용 서비스, 일부 개인서비스</td><td style="border:1px solid #ddd;padding:8px;">개인서비스</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">조사 품목 수</td><td style="border:1px solid #ddd;padding:8px;">886개(2025년 기준)</td><td style="border:1px solid #ddd;padding:8px;">458개(2020년 기준 지수)</td></tr>
    </tbody>
</table>
<p>범위 설명은 <a href="https://mofe.go.kr/sisa/dictionary/detail?idx=1411" target="_blank" rel="noopener">기획재정부 시사경제용어사전</a>과 CME 교육 자료, 한국은행 자료가 같은 방향으로 설명합니다. 소비자물가 쪽 품목 수는 이 저장소의 소비자물가지수 편에서 확인한 수치입니다.</p>
<div style="background:#eef8f1;border:2px solid #3a9a5b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e38;font-size:18px;">📝 비교할 때 주의할 점</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>두 지수는 품목과 가중치가 달라서 같은 달에 상승률이 크게 벌어질 수 있습니다.</li>
    <li>생산자물가지수가 올랐다고 해서 같은 크기로 소비자물가가 오른다고 읽으면 안 됩니다.</li>
    </ul>
</div>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">가중 평균 계산 예시</h2>
<p>물가지수는 품목마다 중요도가 다르기 때문에 가중치를 곱한 가중 평균으로 계산합니다. 가중치는 보통 거래액을 기준으로 정합니다.</p>
<p><a href="https://www.busan.go.kr/news/snsbusan03/view?dataNo=21892" target="_blank" rel="noopener">부산시 물가지수 설명</a>에 실린 작성 예를 그대로 계산해 보겠습니다. 쌀 124.76(가중치 400), 햄버거 102.85(가중치 200), 휘발유 109.35(가중치 400)입니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">품목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">지수</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가중치</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">지수 × 가중치</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">쌀(20kg)</td><td style="border:1px solid #ddd;padding:8px;">124.76</td><td style="border:1px solid #ddd;padding:8px;">400</td><td style="border:1px solid #ddd;padding:8px;">49,904</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">햄버거(1개)</td><td style="border:1px solid #ddd;padding:8px;">102.85</td><td style="border:1px solid #ddd;padding:8px;">200</td><td style="border:1px solid #ddd;padding:8px;">20,570</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">휘발유(1L)</td><td style="border:1px solid #ddd;padding:8px;">109.35</td><td style="border:1px solid #ddd;padding:8px;">400</td><td style="border:1px solid #ddd;padding:8px;">43,740</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">합계</td><td style="border:1px solid #ddd;padding:8px;"></td><td style="border:1px solid #ddd;padding:8px;">1,000</td><td style="border:1px solid #ddd;padding:8px;">114,214</td></tr>
    </tbody>
</table>
<p>합계 114,214를 가중치 총합 1,000으로 나누면 종합지수는 <mark>약 114.2</mark>입니다. 이 사례는 생산자물가 전용이 아니라 물가지수 작성 원리를 보여 주는 예입니다.</p>
<p>이제 상승률 계산입니다. 아래 숫자는 이해를 돕기 위한 가상의 값입니다.</p>
<ul style="line-height:1.9;">
  <li>전년 동월 지수 120.0, 당월 지수 123.6이라면 전년 동월 대비 상승률은 (123.6 ÷ 120.0 − 1) × 100 = <mark>3.0%</mark>입니다.</li>
  <li>전월 지수가 122.4라면 전월 대비 상승률은 (123.6 ÷ 122.4 − 1) × 100 = 약 1.0%입니다.</li>
  <li>기사에서 "전년 동월 대비"와 "전월 대비"가 섞여 나오므로 어느 기준인지 먼저 봐야 합니다.</li>
</ul>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">원재료, 중간재, 최종재 구분</h2>
<p>한국은행은 지수를 생산 단계별로 나눠 발표합니다. 같은 보도자료에서 원재료, 중간재, 최종재가 각각 얼마나 올랐는지 따로 보여 줍니다.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">단계</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">쉬운 설명</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">예를 드는 자리</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">원재료</td><td style="border:1px solid #ddd;padding:8px;">가공 전 재료</td><td style="border:1px solid #ddd;padding:8px;">원유, 광물, 농림수산물 같은 1차 품목</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">중간재</td><td style="border:1px solid #ddd;padding:8px;">다른 제품의 재료로 들어가는 것</td><td style="border:1px solid #ddd;padding:8px;">반도체, 철강판, 화학제품 같은 부품·소재</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">최종재</td><td style="border:1px solid #ddd;padding:8px;">소비나 투자로 끝나는 제품</td><td style="border:1px solid #ddd;padding:8px;">완성된 소비재와 설비 같은 자본재</td></tr>
    </tbody>
</table>
<p>2026년 6월 보도에서는 원재료 2.1%, 중간재 0.5%, 최종재 0.5%가 모두 올랐다고 전해졌습니다. 같은 자료는 세 단계 모두 수입품 영향이 컸다고 설명했습니다. 최신 월의 값은 <a href="https://eiec.kdi.re.kr/policy/materialView.do?num=281416&amp;pg=&amp;pp=&amp;topic=O" target="_blank" rel="noopener">KDI 경제교육정보센터 게시 보도자료</a>나 한국은행 원문에서 확인하세요.</p>
<p>국내공급물가지수는 이렇게 단계별로 나뉘는 대표 지수입니다. 수입품이 들어오기 때문에 환율과 국제 원자재 가격이 곧바로 반영됩니다.</p>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">소비자물가로 번지는 경로</h2>
<p>생산자물가는 원가 부담이 앞단에서 먼저 나타나는 지표라 소비자물가의 선행 신호로 자주 인용됩니다. 그러나 번지는 크기와 속도는 일정하지 않습니다.</p>
<p>가상의 계산으로 원리만 보겠습니다. 어떤 제품의 생산원가에서 원재료 비중이 30%이고, 원재료 가격이 10% 올랐다고 하겠습니다.</p>
<ul style="line-height:1.9;">
  <li>원가 상승폭은 30% × 10% = <mark>3%</mark>입니다.</li>
  <li>기업이 전부 가격에 반영하면 제품 가격이 3% 오르고, 절반만 반영하면 1.5%입니다.</li>
  <li>반영 여부는 경쟁 상황과 재고, 계약 방식에 따라 달라서 시차가 생깁니다.</li>
</ul>
<div style="background:#eef8f1;border:2px solid #3a9a5b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e38;font-size:18px;">📝 지표를 읽을 때 기억할 점</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>생산자물가 상승은 소비자물가 상승 가능성을 알리는 신호일 뿐 확정된 예고가 아닙니다.</li>
    <li>에너지나 원자재처럼 변동이 큰 품목이 지수를 크게 움직이는 달이 있으니 품목별 기여를 같이 보세요.</li>
    </ul>
</div>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">가중치 개편과 자주 받는 질문</h2>
<p>한국은행은 생산자물가지수의 가중치를 정기적으로 손봅니다. <a href="https://www.etoday.co.kr/news/view/2446710" target="_blank" rel="noopener">이투데이 가중치 개편 기사</a>는 공산품 가중치가 줄고 서비스 가중치가 커지는 흐름이 2년째 이어졌다고 전했습니다. 구체적인 비중 수치는 한국은행 원문에서 확인해야 합니다.</p>
<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">물가 지표 헷갈릴 때 보는 질문 5개</h2>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">생산자물가지수가 오르면 소비자물가도 반드시 오르나요</summary>
  <p style="margin:10px 0 0 0;">반드시 오르는 것은 아닙니다. 기업이 늘어난 비용을 제품 가격에 얼마나 반영하느냐에 따라 소비자물가로 이어지는 폭과 시간이 달라집니다. 생산자물가는 소비자물가보다 앞서 움직이는 경우가 있어 참고 지표로 쓰입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">생산자물가지수는 누가 얼마나 자주 발표하나요</summary>
  <p style="margin:10px 0 0 0;">한국은행이 생산자물가조사를 바탕으로 작성하고 매월 잠정치를 보도자료로 공개합니다. 발표 일정은 한국은행 공지에서 확인하세요.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">수출입 물가지수와 생산자물가지수는 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">생산자물가지수는 국내에서 생산해 국내시장에 공급하는 상품과 서비스의 가격을 잽니다. 수출입물가지수는 수출품과 수입품의 가격 변화를 따로 재는 별개 지표입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내공급물가지수와 총산출물가지수는 무슨 차이인가요</summary>
  <p style="margin:10px 0 0 0;">국내공급물가지수는 수입품까지 포함해 국내에 공급되는 물품의 가격을, 총산출물가지수는 국내 생산물의 출하 가격을 중심으로 합니다. 한국은행 보도자료는 생산자물가지수와 함께 이 지수들도 발표합니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">생산자물가지수가 오르면 주가는 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">방향을 단정할 수 없습니다. 물가 부담이 커지면 금리 전망이 바뀌고 기업 비용도 늘지만, 시기마다 시장 반응은 다릅니다. 이 글은 지표 읽는 법만 다루며 매매 판단을 제시하지 않습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.bok.or.kr/portal/bbs/B0000501/view.do?nttId=10098068&amp;menuNo=200690" target="_blank" rel="noopener">한국은행 생산자물가지수 보도자료</a></li>
    <li><a href="https://www.data.go.kr/data/15059642/openapi.do" target="_blank" rel="noopener">공공데이터포털 한국은행 생산자물가조사</a></li>
    <li><a href="https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1061" target="_blank" rel="noopener">e-나라지표 생산자물가지수</a></li>
    <li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=1411" target="_blank" rel="noopener">기획재정부 시사경제용어사전 생산자물가지수</a></li>
    <li><a href="https://www.etoday.co.kr/news/view/2446710" target="_blank" rel="noopener">이투데이 가중치 개편 기사</a></li>
    <li><a href="https://www.busan.go.kr/news/snsbusan03/view?dataNo=21892" target="_blank" rel="noopener">부산시 물가지수 설명</a></li>
  </ul>
  기준일: 2026년 9월 기준. 가상의 계산 예시(상승률, 원가 비중)는 이해를 돕기 위한 숫자이며 실제 통계가 아닙니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 통계 지표를 읽는 방법을 소개하는 정보 글이며, 어떤 종목이나 상품을 사고팔라는 안내가 아닙니다. 지수 값과 품목 수, 가중치는 개편으로 바뀔 수 있어 최신 내용은 한국은행 자료로 확인하셔야 합니다. 투자 판단과 그에 따른 결과는 투자자 본인이 책임집니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "생산자물가지수 뜻과 소비자물가 차이",
  "description": "생산자물가지수가 무엇을 재는지, 소비자물가지수와 범위가 어떻게 다른지, 가중 평균 계산과 원재료·중간재·최종재 구분까지 정리했습니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/producer-price-index-cpi-difference"
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
      "name": "생산자물가지수가 오르면 소비자물가도 반드시 오르나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "반드시 오르는 것은 아닙니다. 기업이 늘어난 비용을 제품 가격에 얼마나 반영하느냐에 따라 소비자물가로 이어지는 폭과 시간이 달라집니다. 생산자물가는 소비자물가보다 앞서 움직이는 경우가 있어 참고 지표로 쓰입니다."
      }
    },
    {
      "@type": "Question",
      "name": "생산자물가지수는 누가 얼마나 자주 발표하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "한국은행이 생산자물가조사를 바탕으로 작성하고 매월 잠정치를 보도자료로 공개합니다. 발표 일정은 한국은행 공지에서 확인하세요."
      }
    },
    {
      "@type": "Question",
      "name": "수출입 물가지수와 생산자물가지수는 어떻게 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "생산자물가지수는 국내에서 생산해 국내시장에 공급하는 상품과 서비스의 가격을 잽니다. 수출입물가지수는 수출품과 수입품의 가격 변화를 따로 재는 별개 지표입니다."
      }
    },
    {
      "@type": "Question",
      "name": "국내공급물가지수와 총산출물가지수는 무슨 차이인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "국내공급물가지수는 수입품까지 포함해 국내에 공급되는 물품의 가격을, 총산출물가지수는 국내 생산물의 출하 가격을 중심으로 합니다. 한국은행 보도자료는 생산자물가지수와 함께 이 지수들도 발표합니다."
      }
    },
    {
      "@type": "Question",
      "name": "생산자물가지수가 오르면 주가는 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "방향을 단정할 수 없습니다. 물가 부담이 커지면 금리 전망이 바뀌고 기업 비용도 늘지만, 시기마다 시장 반응은 다릅니다. 이 글은 지표 읽는 법만 다루며 매매 판단을 제시하지 않습니다."
      }
    }
  ]
}
</script>
