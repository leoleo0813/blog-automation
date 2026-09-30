---
keyword: 테이퍼링 뜻
title: 테이퍼링 뜻과 양적완화 축소 일정 계산
slug: tapering-meaning-qe-schedule
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 3570 (PC 330 / 모바일 3240)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-30 - 통과]
  WebSearch "테이퍼링 뜻 양적완화 자산매입 축소 주식 영향" 상위 9개: kofia.or.kr(금융투자협회 연구자료, 공식), toss.im/tossfeed(핀테크 콘텐츠), kbthink.com(KB 사전),
  upbitcare.com(거래소 교육), blog.lxinternational.com(기업 블로그), dic.hankyung.com(언론사 사전), finlizehub.com(소규모 개인 콘텐츠), a-ha.io(Q&A 커뮤니티). arxiv 논문 1개는 무관.
  1) 진입 여지: 있음. finlizehub 같은 소규모 콘텐츠 사이트와 a-ha 커뮤니티가 상위에 섞여 SERP가 잠겨 있지 않다.
  2) 검색 의도: 뜻과 영향을 찾는 탐색형. 조회·계산기 의도가 아니다.
  3) 답 완결 여부: 부분적. 상위는 "양적완화를 줄이는 것"이라는 정의와 "금리 상승 우려"를 말로 설명하지만, 월 매입액이 매달 얼마씩 줄어 언제 0이 되는지 계산한 표와 2013년·2021년 두 사례 대조표는 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 2021년 월 1,200억 달러 매입이 월 150억 달러씩 줄 때(원안)와 2022년 1월부터 월 300억 달러씩 줄 때(가속)의 월별 매입액 비교표. 원안은 2022년 6월, 가속은 2022년 3월에 0이 되는 계산 과정 공개.
  (b) 2013~2014년과 2021~2022년 두 테이퍼링 사례 대조표(시작 시점, 매입 규모, 첫 축소 폭, 종료 시점).
  (c) 양적완화·테이퍼링·양적긴축·금리 인상 구분표.
primary_source: |
  금융투자협회 「미국 연준 테이퍼링(자산매입축소)의 글로벌 자본시장 영향」(kofia.or.kr) WebFetch 1회 시도, EGRESS_BLOCKED. 대신 WebSearch 2회로 서로 무관한 출처를 교차 확인했다:
  2013년 사례는 CNBC, Brookings, 미 의회조사국(CRS, congress.gov), CRFB가 동일 수치(월 850억 → 750억 달러, 국채 400억·MBS 350억, 2014년 10월 종료)로 수렴.
  2021년 사례는 이투데이, 녹색경제신문, 이코노미스트, 치과신문 등이 동일 수치(2020년 3월부터 월 1,200억 달러, 2021년 11월 월 150억 달러 축소 시작, 2022년 3월 종료)로 수렴.
  세율·한도 같은 법정 수치가 아니라 공개된 연준 정책 이력이며, 본문 월별 표는 이 수치를 단순 산수로 계산한 값이다.
기준일: 2026년 9월 기준 (과거 정책 이력이라 현재 연준 정책 상태는 서술하지 않음)
tags: 테이퍼링 뜻, 테이퍼링이란, 양적완화 뜻, 양적긴축 차이, 테이퍼 텐트럼, 연준 자산매입, 2013 테이퍼링, 2021 테이퍼링, FOMC, 미국 증시 금리
gate_pass: true
gate_pass_note: |
  게이트1 3,570회, 게이트2 v3 통과, 게이트3 월별 매입액 계산표와 두 사례 대조표 확보, 게이트4 독립 출처 4곳 이상 교차검증(금투협 원문은 접속 불가).
  사람은 발행 전 금융투자협회 연구자료 또는 연준 FOMC 성명서(federalreserve.gov)에서 2013년 12월 월 850억 → 750억 달러, 2021년 11월 월 150억 달러 축소 수치만 한 번 대조하면 된다.
self_check: |
  [2026-09-30 gate_pass:true]
  후보 경위: backlog에 단순 대기 후보가 없어 신규 8개(환율 뜻, 디플레이션 뜻, 경기침체 뜻, 테이퍼링 뜻, 생산자물가지수, 비농업고용지수, 코픽스 뜻, CD금리 뜻)를 실측. PASS 4개(테이퍼링 뜻 3,570 / 생산자물가지수 2,730 / 환율 뜻 1,800 / 디플레이션 뜻 900), FAIL 4개(경기침체 240, 비농업고용지수 330, 코픽스 150, CD금리 380). 최고 검색량 테이퍼링 뜻 채택.
  카니벌라이제이션: stock_drafts grep 결과 "테이퍼링"을 본문 주제로 다룬 글 없음. 양적완화는 언급 수준. 98편 달러인덱스, 105편 국채금리 뜻과 내부 링크로 연결하되 각도가 다름(이 글은 자산매입 축소 정책의 정의와 일정 계산).
  수치 검산(python): 원안 1,200-150n 으로 2021-11 1,050 ... 2022-06 0. 가속안은 2021-11 1,050, 12월 900, 2022-01 600, 02월 300, 03월 0. 2013 사례 850-100=750(국채 450→400, MBS 400→350).
  제외한 수치: 2014년 회의별 세부 축소 폭, 양적긴축 시작일, 금리 인상 시점은 이번 교차검증에서 확인하지 않아 본문에 쓰지 않음.
  YMYL: 종목·상품 추천, 금리 방향 전망, 매수매도 시점 없음. "테이퍼링하면 주가가 내린다"류 단정 없이 2013년 발언 때와 결정 당일의 엇갈린 반응을 사례로만 제시.
  기관 링크: 출처 목록 6개 전부 WebSearch 결과에서 확인한 URL로 링크 처리. 본문 기관 안내는 연준·한국은행 사이트를 글자로만 쓰지 않고 승인된 URL이 없어 기관명만 표기. 금투협 PDF는 검색 결과로만 확인(미열람).
  제목 "테이퍼링 뜻과 양적완화 축소 일정 계산" 공백 포함 20자, 금지어 없음. 슬러그 4단어 영문 소문자 하이픈.
  첫 문장 유형: 정의형. 글 구조 유형: 사례 대조 + 일정 계산형.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 3개, FAQ 5개, H2 6개(목차 제외) 중 "~나요"형 2개.
  요약박스 보라색(#f3eefb/#7a52c7), 제목 "🔎 테이퍼링 핵심 세 줄". FAQ 헤딩 "테이퍼링 기사 읽다 막히는 질문". 면책 문구 새 표현.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-30</p>

<p>테이퍼링은 중앙은행이 양적완화로 사들이던 자산의 월 매입 규모를 조금씩 줄여 나가는 정책입니다. 돈을 풀던 속도를 줄이는 것이지, 이미 푼 돈을 거두는 것은 아닙니다. 이 글은 2013년과 2021년 두 차례의 미국 사례를 대조하고, 월 매입액이 줄어드는 과정을 직접 계산해 봅니다.</p>

<div style="background:#f3eefb;border:2px solid #7a52c7;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4f2f8f;font-size:18px;">🔎 테이퍼링 핵심 세 줄</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>테이퍼링은 자산 매입을 "줄이는" 단계이고, 매입을 멈추는 종료, 보유 자산을 줄이는 양적긴축과는 다른 단계입니다.</li><li>2013년에는 월 850억 달러에서 750억 달러로 줄이며 시작해 2014년 10월에 끝났습니다.</li><li>2021년에는 월 1,200억 달러 매입을 월 150억 달러씩 줄이기 시작했고, 이후 속도를 2배로 높여 2022년 3월에 마무리했습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li>테이퍼링은 무슨 뜻인가요</li>
  <li>양적완화, 테이퍼링, 양적긴축 구분표</li>
  <li>2013년 테이퍼링 경과</li>
  <li>2021년 월 1,200억 달러 축소 계산</li>
  <li>발표와 실행 때 시장 반응이 엇갈린 사례</li>
  <li>테이퍼링 기사 읽는 법</li>
  <li>테이퍼링 기사 읽다 막히는 질문</li>
</ol>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">테이퍼링은 무슨 뜻인가요</h2>

<p>테이퍼링(tapering)은 "점점 가늘어진다"는 뜻으로, 양적완화의 규모를 단계적으로 줄이는 것을 가리킵니다. 2013년 5월 벤 버냉키 당시 미국 연준 의장이 언급하면서 널리 알려진 말입니다.</p>

<p>양적완화는 중앙은행이 국채나 주택저당증권(MBS)을 사들여 시중에 돈을 공급하는 정책입니다. 테이퍼링에서는 이 매입을 매달 조금씩 줄입니다.</p>

<p><mark>테이퍼링을 해도 매입액이 0이 되기 전까지는 연준이 계속 자산을 사고 있습니다.</mark> 그래서 "돈줄을 죄는 정책"이라기보다 "돈을 푸는 속도를 늦추는 정책"으로 이해하는 편이 정확합니다.</p>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">양적완화, 테이퍼링, 양적긴축 구분표</h2>

<p>뉴스에는 이 용어들이 한꺼번에 나와 헷갈리기 쉽습니다. 단계별로 나누면 아래와 같이 정리됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">용어</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">하는 일</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">자산 매입액의 움직임</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">양적완화(QE)</td><td style="border:1px solid #ddd;padding:8px;">국채와 MBS를 사서 돈을 공급</td><td style="border:1px solid #ddd;padding:8px;">매달 일정 규모를 매입</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">테이퍼링</td><td style="border:1px solid #ddd;padding:8px;">매입 규모를 단계적으로 축소</td><td style="border:1px solid #ddd;padding:8px;">매달 줄어들지만 아직 0은 아님</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">매입 종료</td><td style="border:1px solid #ddd;padding:8px;">신규 매입을 멈춤</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기준금리 인상</td><td style="border:1px solid #ddd;padding:8px;">정책금리 자체를 올림</td><td style="border:1px solid #ddd;padding:8px;">매입과는 별개의 수단</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">양적긴축(QT)</td><td style="border:1px solid #ddd;padding:8px;">보유 자산을 줄여 돈을 흡수</td><td style="border:1px solid #ddd;padding:8px;">만기 채권을 재투자하지 않는 방식 등으로 감소</td></tr>
  </tbody>
</table>

<p>일반적으로 테이퍼링, 매입 종료, 금리 인상, 양적긴축 순으로 강도가 세지는 단계로 설명합니다. 단계마다 시점은 그때의 물가와 고용 상황에 따라 달라집니다.</p>

<div style="background:#f3eefb;border:2px solid #7a52c7;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4f2f8f;font-size:18px;">📝 용어 구분 기억법</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>테이퍼링은 "매입 속도"를 줄이는 것이고, 양적긴축은 "보유 잔액"을 줄이는 것입니다.</li><li>테이퍼링과 기준금리 인상은 서로 다른 수단이라 같은 날 발표되지 않을 수 있습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">2013년 테이퍼링 경과</h2>

<p>2013년 테이퍼링은 발언이 먼저 나오고 실제 축소가 몇 달 뒤에 시작된 사례입니다. 2013년 5월 버냉키 의장이 자산매입 축소 가능성을 언급했고, 같은 해 12월 FOMC(연방공개시장위원회)에서 실제 축소가 결정됐습니다.</p>

<p>12월 결정 내용은 국채 매입을 월 50억 달러, MBS 매입을 월 50억 달러 줄이는 것이었습니다. <mark>월 총 매입액이 850억 달러에서 750억 달러로 줄었습니다.</mark> 이후 회의마다 매입 규모가 더 줄었고, 2014년 10월에 종료됐습니다.</p>

<ol style="line-height:1.9;">
  <li>2013년 5월: 버냉키 의장이 자산매입 축소 가능성을 언급</li>
  <li>2013년 12월: 월 850억 달러에서 750억 달러로 축소 결정 (국채 400억, MBS 350억)</li>
  <li>2014년 10월: 축소를 이어 간 끝에 신규 매입 종료</li>
</ol>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">2021년 월 1,200억 달러 축소 계산</h2>

<p>2021년 테이퍼링은 코로나19 대응으로 커진 매입 규모를 줄인 사례입니다. 연준은 2020년 3월부터 매달 1,200억 달러(국채 800억 달러, MBS 400억 달러)를 사들이고 있었고, 2021년 11월부터 월 150억 달러씩 줄이기 시작했습니다.</p>

<p>월 150억 달러씩 줄이는 원안을 그대로 계산하면 아래와 같이 매입이 끝나는 시점이 나옵니다. 2022년 1월부터 축소 속도를 월 300억 달러로 높인 가속안도 나란히 계산했습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">시점</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">원안: 월 150억씩 축소 (월 매입액)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가속안: 2022년 1월부터 월 300억씩 (월 매입액)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2021년 10월</td><td style="border:1px solid #ddd;padding:8px;">1,200억 달러</td><td style="border:1px solid #ddd;padding:8px;">1,200억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2021년 11월</td><td style="border:1px solid #ddd;padding:8px;">1,050억 달러</td><td style="border:1px solid #ddd;padding:8px;">1,050억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2021년 12월</td><td style="border:1px solid #ddd;padding:8px;">900억 달러</td><td style="border:1px solid #ddd;padding:8px;">900억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022년 1월</td><td style="border:1px solid #ddd;padding:8px;">750억 달러</td><td style="border:1px solid #ddd;padding:8px;">600억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022년 2월</td><td style="border:1px solid #ddd;padding:8px;">600억 달러</td><td style="border:1px solid #ddd;padding:8px;">300억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022년 3월</td><td style="border:1px solid #ddd;padding:8px;">450억 달러</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022년 4월</td><td style="border:1px solid #ddd;padding:8px;">300억 달러</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022년 5월</td><td style="border:1px solid #ddd;padding:8px;">150억 달러</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2022년 6월</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
  </tbody>
</table>

<p><mark>원안대로라면 2022년 6월에 끝날 일정이 가속으로 2022년 3월로 석 달 당겨졌습니다.</mark> 당시 미국 소비자물가 상승률이 40년 만의 최고 수준으로 오르면서 속도를 높였다고 보도됐습니다.</p>

<p>표의 월별 금액은 공개된 출발점(1,200억 달러)과 축소 폭(150억, 300억 달러)으로 단순 계산한 값입니다. 실제 월별 매입 집행액은 연준 공식 자료로 확인해야 합니다.</p>

<h3 style="margin-top:24px;">두 사례를 나란히 놓으면</h3>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2013~2014년</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">2021~2022년</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">축소 전 월 매입액</td><td style="border:1px solid #ddd;padding:8px;">850억 달러</td><td style="border:1px solid #ddd;padding:8px;">1,200억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">첫 축소 폭</td><td style="border:1px solid #ddd;padding:8px;">월 100억 달러 (국채 50억, MBS 50억)</td><td style="border:1px solid #ddd;padding:8px;">월 150억 달러</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">실제 축소 시작</td><td style="border:1px solid #ddd;padding:8px;">2013년 12월 결정</td><td style="border:1px solid #ddd;padding:8px;">2021년 11월</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">종료</td><td style="border:1px solid #ddd;padding:8px;">2014년 10월</td><td style="border:1px solid #ddd;padding:8px;">2022년 3월</td></tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">발표와 실행 때 시장 반응이 엇갈린 사례</h2>

<p>테이퍼링 기사는 "주가 하락"이 제목으로 자주 붙지만, 실제 반응은 시점마다 달랐습니다. 2013년 5월 발언 직후에는 신흥국 금융시장이 크게 흔들려 이를 테이퍼 텐트럼(긴축 발작)이라고 부르게 됐습니다.</p>

<p>반면 2013년 12월 실제 축소가 결정된 당일에는 미국 증시가 올랐다는 보도가 있었습니다. 시장이 이미 예상한 내용이면 발표 자체보다 "예상과 얼마나 다른가"가 반응을 좌우한 것입니다.</p>

<p>달러 가치와 신흥국 자금 흐름도 함께 거론됩니다. 달러 지수의 구성과 움직임은 <a href="https://sensitiveboss3.tistory.com/entry/dollar-index-meaning-currency-weights" target="_blank" rel="noopener">달러인덱스 뜻과 통화 비중</a>에서 따로 정리했습니다.</p>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">테이퍼링 기사 읽는 법</h2>

<p>기사를 읽을 때는 네 가지만 확인하면 흐름이 잡힙니다. 각각 해당 기사의 본문에서 찾을 수 있습니다.</p>

<ol style="line-height:1.9;">
  <li><strong>지금 단계:</strong> 논의 단계인지, 결정 단계인지, 이미 시행 중인지 확인합니다.</li>
  <li><strong>축소 폭:</strong> 월 얼마씩 줄이는지, 국채와 MBS가 각각 얼마인지 봅니다.</li>
  <li><strong>종료 예정 시점:</strong> 원안 일정과 가속 여부를 구분해 읽습니다.</li>
  <li><strong>금리 인상과의 관계:</strong> 매입 축소와 기준금리 인상을 같은 말로 섞어 쓴 기사가 아닌지 봅니다.</li>
</ol>

<p>매입 축소가 채권 시장과 만나는 부분은 금리와 채권 가격의 관계로 이어집니다. 기초 계산은 <a href="https://sensitiveboss3.tistory.com/entry/government-bond-yield-meaning" target="_blank" rel="noopener">국채금리 뜻과 채권가격 반비례 계산</a>에서 볼 수 있습니다.</p>

<div style="background:#f3eefb;border:2px solid #7a52c7;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4f2f8f;font-size:18px;">✅ 마무리로 챙길 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>테이퍼링은 매입 규모를 줄이는 단계이며, 0이 되기 전까지는 매입이 이어집니다.</li><li>같은 테이퍼링이라도 출발 규모와 속도에 따라 끝나는 시점이 크게 달라집니다.</li><li>시장 반응은 발표 시점과 사전 기대에 따라 달랐으므로 한 방향으로 단정할 수 없습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #7a52c7;padding-left:12px;margin-top:36px;">테이퍼링 기사 읽다 막히는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">테이퍼링과 양적긴축은 같은 말인가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 테이퍼링은 신규 자산 매입의 속도를 줄이는 것이고, 양적긴축은 이미 보유한 자산의 규모를 줄이는 것입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">테이퍼링을 하면 금리도 오르나요</summary>
  <p style="margin:10px 0 0 0;">자동으로 오르지는 않습니다. 기준금리 인상은 별도의 결정이고, 매입 규모 축소가 시장금리에 영향을 줄 수는 있어도 두 가지는 다른 수단입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">2013년 테이퍼링은 언제 끝났나</summary>
  <p style="margin:10px 0 0 0;">2014년 10월에 끝났습니다. 2013년 12월 월 850억 달러에서 750억 달러로 줄이며 시작해 약 10개월에 걸쳐 축소했습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">테이퍼 텐트럼이 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">테이퍼링 기대에 시장이 발작하듯 반응하는 현상으로, 긴축 발작이라고도 합니다. 2013년 5월 버냉키 의장 발언 이후 신흥국 시장이 흔들린 일에서 나온 표현입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">한국은행도 테이퍼링을 하나요</summary>
  <p style="margin:10px 0 0 0;">이 글에서 다룬 테이퍼링은 미국 연준의 자산 매입 축소 사례입니다. 다른 나라 중앙은행의 정책은 각 기관의 공식 발표로 확인해야 합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.kofia.or.kr/brd/m_48/down.do?brd_id=www_research&amp;seq=209&amp;data_tp=A&amp;file_seq=1" target="_blank" rel="noopener">금융투자협회 - 미국 연준 테이퍼링(자산매입축소)의 글로벌 자본시장 영향</a></li>
    <li><a href="https://www.cnbc.com/2013/12/18/fed-begins-taper-program.html" target="_blank" rel="noopener">CNBC - Fed to taper bond buying by $10 billion a month</a></li>
    <li><a href="https://www.brookings.edu/articles/what-does-the-federal-reserve-mean-when-it-talks-about-tapering/" target="_blank" rel="noopener">Brookings - What does the Federal Reserve mean when it talks about tapering?</a></li>
    <li><a href="https://crsreports.congress.gov/product/pdf/IN/IN11792" target="_blank" rel="noopener">미 의회조사국 - Federal Reserve: Tapering of Asset Purchases</a></li>
    <li><a href="https://www.etoday.co.kr/news/view/2074953" target="_blank" rel="noopener">이투데이 - 연준, 이달 테이퍼링 돌입</a></li>
    <li><a href="https://toss.im/tossfeed/article/securities_tapering" target="_blank" rel="noopener">토스피드 - 테이퍼링이 뭔데 주식시장이 흔들리나요?</a></li>
  </ul>
  기준일: 2026년 9월 기준. 과거 정책 이력을 설명하는 글이며 현재 연준 정책 상태는 다루지 않았습니다. 금융투자협회 원문은 자동화 세션에서 접속이 막혀 검색 결과로만 확인했고, 수치는 여러 독립 출처에서 교차 확인했습니다. 월별 매입액 표는 공개된 출발점과 축소 폭으로 계산한 값입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 중앙은행 정책 용어를 설명하는 정보 글로, 특정 종목이나 금융상품의 매수와 매도를 권하지 않습니다. 금리와 시장 전망은 다루지 않았으며, 최신 정책은 연준과 한국은행의 공식 발표로 직접 확인해 주세요. 투자 판단과 그 결과는 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "테이퍼링 뜻과 양적완화 축소 일정 계산",
  "description": "테이퍼링 뜻을 양적완화, 양적긴축과 구분하고, 2013년과 2021년 미국 사례를 대조하며 월 1,200억 달러 매입이 줄어드는 과정을 표로 계산합니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/tapering-meaning-qe-schedule"
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
      "name": "테이퍼링과 양적긴축은 같은 말인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "다릅니다. 테이퍼링은 신규 자산 매입의 속도를 줄이는 것이고, 양적긴축은 이미 보유한 자산의 규모를 줄이는 것입니다."
      }
    },
    {
      "@type": "Question",
      "name": "테이퍼링을 하면 금리도 오르나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "자동으로 오르지는 않습니다. 기준금리 인상은 별도의 결정이고, 매입 규모 축소가 시장금리에 영향을 줄 수는 있어도 두 가지는 다른 수단입니다."
      }
    },
    {
      "@type": "Question",
      "name": "2013년 테이퍼링은 언제 끝났나",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "2014년 10월에 끝났습니다. 2013년 12월 월 850억 달러에서 750억 달러로 줄이며 시작해 약 10개월에 걸쳐 축소했습니다."
      }
    },
    {
      "@type": "Question",
      "name": "테이퍼 텐트럼이 무슨 뜻인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "테이퍼링 기대에 시장이 발작하듯 반응하는 현상으로, 긴축 발작이라고도 합니다. 2013년 5월 버냉키 의장 발언 이후 신흥국 시장이 흔들린 일에서 나온 표현입니다."
      }
    },
    {
      "@type": "Question",
      "name": "한국은행도 테이퍼링을 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이 글에서 다룬 테이퍼링은 미국 연준의 자산 매입 축소 사례입니다. 다른 나라 중앙은행의 정책은 각 기관의 공식 발표로 확인해야 합니다."
      }
    }
  ]
}
</script>
