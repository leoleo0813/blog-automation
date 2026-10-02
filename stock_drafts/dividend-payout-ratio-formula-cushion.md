---
keyword: 배당성향
title: 배당성향 공식과 이익 줄 때 배당 변화
slug: dividend-payout-ratio-formula-cushion
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 570 (PC 300 / 모바일 270, backlog.verified 기록 인용)
gate1_pass: true (일반 주제 기준 월 500 이상)
serp_check: |
  [게이트2 v3 판정 2026-10-02 - 통과]
  WebSearch "배당성향 뜻 계산 방법" 상위 8개: brunch 개인 글, Daum 팁(Q&A), 나무위키, 12manage(경영 용어 사이트), dividendletter 블로그, a-ha.io Q&A 2건, 기타 1건.
  1) 진입 여지: 있음. 개인 블로그·Q&A·소규모 사이트가 대부분이고 증권사 공식 페이지는 없었다.
  2) 검색 의도: 뜻과 계산법을 찾는 탐색형. 조회·계산기 실행 의도 아님.
  3) 답 완결 여부: 부분적. 상위 요약은 정의, 공식, 순이익 100억 중 40억 배당 한 줄 예시였다. 배당수익률이 같은 두 회사의 배당성향 비교, 순이익 25% 감소 시 배당 시나리오 표, 배당성향÷PER 연결식은 요약 단계에서 확인하지 못했다(본문 전체는 열어보지 못함).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 두 회사(배당성향 40%·90%, 배당수익률 4.0% 동일) 지표 비교표.
  (b) 순이익 25% 감소 시 배당성향 유지 vs DPS 유지 시나리오 표(가나다전자 53.3%, 라마바화학 120.0%, 주당 300원 초과 지급).
  (c) 배당수익률 = 배당성향 ÷ PER 항등식 검산표(40%÷10.0=4.0%, 90%÷22.5=4.0%).
primary_source: |
  배당성향은 기관이 수치를 공표하는 지표가 아니라 회계 비율의 정의라서 1차 수치 출처가 따로 없다.
  dart.fss.or.kr(금융감독원 전자공시), nts.go.kr WebFetch 각 1회 시도, 모두 EGRESS_BLOCKED.
  WebSearch 2회로 독립 출처 교차 확인: 배당성향 = 현금배당 ÷ 당기순이익(또는 DPS ÷ EPS)이 brunch, dividendletter, 12manage, Daum 팁, a-ha.io, 증권플러스 고객센터에서 일치(검색 결과 요약 단계 확인, 본문 미열람). 기획재정부 시사경제용어사전(KDI)은 검색에서 링크만 확인.
기준일: 2026년 10월 기준 (모든 회사·수치는 가상)
tags: 배당성향, 배당성향 계산, 배당성향 공식, 배당수익률, 배당금, 주당배당금, EPS, PER, 고배당주, 주식 용어
gate_pass: false
gate_pass_note: |
  게이트1 통과, 게이트2 v3 통과, 게이트3 표 3개 확보. 게이트4 미충족: 정의와 공식은 독립 출처 6곳에서 일치하나 금융감독원·한국거래소·기획재정부 사전 원문은 열람하지 못했다.
  사람이 할 일: KDI 시사용어사전(https://eiec.kdi.re.kr/material/wordDic.do)에서 '배당성향'을 검색해 정의가 현금배당 ÷ 당기순이익인지 확인하면 true로 바꿀 수 있습니다. 본문 계산값(40.0%, 90.0%, 53.3%, 120.0%, 4.0%)은 파이썬으로 재계산해 일치 확인함.
self_check: |
  [2026-10-02 gate_pass:false, 게이트4 기관 원문 미열람]
  후보 경위: 신규 8개 실측(check-keywords) 결과 손익분기점 3,020·순환매 880·보호예수 700 PASS. 손익분기점은 SERP가 기업 BEP(경영)라 주식 의도와 어긋나고, 보호예수는 오버행 편(overhang-lockup-release-check)이 49회 다뤄 카니벌라이제이션, 순환매는 사전형이며 정보이득·1차 출처 부재라 제외. backlog 대기 후보 배당성향(570) 채택. 잉여현금흐름 210, 외국인 지분율 40, 장단기 금리차 490, 경상수지 20, 따상 뜻 200은 게이트1 탈락.
  카니벌라이제이션: 47편(배당수익률 계산법)은 DPS÷주가, 4편(배당소득세)은 세금 중심이라 배당성향 계산·시나리오와 다름. 4편에 분리과세 요건 수치가 있어 이 글은 수치를 옮기지 않고 링크로 안내. 내부 링크 3개(47·EPS·PER편).
  YMYL: 종목 추천·목표가·매매시점 없음. 모든 회사·숫자 가상 명시. 세율·요건 수치 미기재.
  기관 링크: 본문의 기관 안내 문장 1개(국세청 원문 확인) 링크 처리(국세청 메인), 출처 목록 3개 전부 링크 처리.
  제목 "배당성향 공식과 이익 줄 때 배당 변화" 18자, 금지어 없음, 최근 5편의 "뜻과 계산" 틀 대신 "공식과 ~ 변화" 틀. 슬러그 5단어.
  첫 문장 유형: 문제제기형(직전 115 정의형과 다름). 인트로 둘째 문장에 정의·공식 포함, 메타 문장 없음.
  글 구조 유형: 개념형(첫 H2의 첫 블록이 가상 인물 A씨 사례 문단). 직전 115 계산형, 114·113 비교형과 다름.
  어투 모드: C 사례형(가상 인물 A씨와 가상 회사 2곳을 끝까지 따라감, 가상임을 명시). 직전 115 A, 114·113 B와 다름. 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 1회(FAQ 1곳), mark 밀도 4개, FAQ 5개(직전 115 6·114 7과 다름), H2 6개 중 "~나요"형 0개(목차 제외 5개 중 1개 "~되나"). 요약박스 초록(#eef8f0/#3a9a5b), 제목 "💬 A씨 이야기에서 건질 것", 마무리 "🧮 마지막으로 남길 계산". FAQ 헤딩 "배당성향 숫자를 읽다 떠오르는 궁금증 풀이"(걸리는·막히는·세 줄·묻게 어휘 회피). 면책 문구 새 표현.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>배당수익률이 똑같이 4%인데 한 회사는 이익의 40%를, 다른 회사는 90%를 배당으로 내놓는다면 어디를 봐야 배당 여력이 보일까요? 그 답이 배당성향이고, 순이익 중 배당으로 나간 비율(배당금 ÷ 순이익 × 100)입니다.</p>

<div style="background:#eef8f0;border:2px solid #3a9a5b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e38;font-size:18px;">💬 A씨 이야기에서 건질 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>배당성향은 <mark>순이익 중 배당으로 나가는 몫</mark>이라서 배당 여력을 가늠하는 숫자입니다.</li><li>배당수익률이 같아도 배당성향이 40%와 90%면 이익이 줄 때의 여유가 크게 다릅니다.</li><li>순이익이 25% 줄면 90%인 회사는 같은 배당을 유지할 때 배당성향이 120%로 올라갑니다.</li><li>배당수익률 = 배당성향 ÷ PER 관계로 세 지표를 한 줄에 연결할 수 있습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>배당수익률이 같은 두 회사, 배당성향은 왜 다를까</li>
  <li>배당성향 공식 두 가지와 분모 확인법</li>
  <li>이익이 25% 줄면 배당은 어떻게 되나</li>
  <li>배당성향이 100%를 넘으면 읽는 법</li>
  <li>배당수익률과 PER로 이어 보는 법</li>
</ol>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">배당수익률이 같은 두 회사, 배당성향은 왜 다를까</h2>

<p>가상의 투자자 A씨가 가나다전자와 라마바화학의 배당수익률이 모두 4.0%인 것을 발견했습니다. 두 회사와 A씨는 실제 인물이나 기업이 아닌 설명용 가상 설정입니다.</p>

<p>가나다전자는 주당 5,000원을 벌어 2,000원을 배당합니다. 라마바화학은 주당 2,000원을 벌어 1,800원을 배당합니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">가상 두 회사의 배당 지표 (단위: 원, 계산 결과)</caption>
  <thead>
    <tr style="background:#eef8f0;"><th style="border:1px solid #ddd;padding:8px;">항목</th><th style="border:1px solid #ddd;padding:8px;">가나다전자</th><th style="border:1px solid #ddd;padding:8px;">라마바화학</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">주당순이익(EPS)</td><td style="border:1px solid #ddd;padding:8px;">5,000</td><td style="border:1px solid #ddd;padding:8px;">2,000</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">주당배당금(DPS)</td><td style="border:1px solid #ddd;padding:8px;">2,000</td><td style="border:1px solid #ddd;padding:8px;">1,800</td></tr>
    <tr style="background:#eef8f0;"><td style="border:1px solid #ddd;padding:8px;">배당성향 = DPS ÷ EPS</td><td style="border:1px solid #ddd;padding:8px;">40.0%</td><td style="border:1px solid #ddd;padding:8px;">90.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">주가</td><td style="border:1px solid #ddd;padding:8px;">50,000</td><td style="border:1px solid #ddd;padding:8px;">45,000</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">배당수익률 = DPS ÷ 주가</td><td style="border:1px solid #ddd;padding:8px;">4.0%</td><td style="border:1px solid #ddd;padding:8px;">4.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">PER = 주가 ÷ EPS</td><td style="border:1px solid #ddd;padding:8px;">10.0배</td><td style="border:1px solid #ddd;padding:8px;">22.5배</td></tr>
  </tbody>
</table>

<p>배당성향은 가나다전자 40.0%, 라마바화학 90.0%입니다. 같은 4.0%여도 <mark>한쪽은 이익의 절반도 안 쓰고, 다른 쪽은 거의 다 쓰는 배당</mark>입니다.</p>

<p>비유하면 월급 500만 원 중 200만 원을 기부하는 사람과 450만 원을 기부하는 사람입니다. 지금 기부액은 비슷해 보여도 월급이 줄면 먼저 흔들리는 쪽은 뻔합니다.</p>

<p>배당수익률 자체가 궁금하다면 <a href="https://sensitiveboss3.tistory.com/entry/dividend-yield-calculation" target="_blank" rel="noopener">배당수익률 계산법</a> 편을 먼저 보면 이어집니다.</p>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">배당성향 공식 두 가지와 분모 확인법</h2>

<p>배당성향은 배당금 총액 ÷ 순이익 × 100, 또는 주당배당금(DPS) ÷ 주당순이익(EPS) × 100으로 구합니다. 두 식은 같은 값을 줍니다. 분자와 분모를 주식 수로 나눴을 뿐입니다.</p>

<ul>
  <li>총액 기준: 배당금 총액 40억 원 ÷ 순이익 100억 원 = 40%</li>
  <li>주당 기준: DPS 2,000원 ÷ EPS 5,000원 = 40%</li>
  <li>분자는 현금배당 기준으로 쓰는 경우가 많습니다.</li>
  <li>분모는 자료마다 당기순이익, 지배주주 귀속 순이익 등으로 다릅니다.</li>
</ul>

<p>짧게 정리하면, 숫자를 비교할 때는 분모부터 확인합니다. 같은 회사인데 배당성향이 다르게 나온다면 분모 정의가 달라서인 경우가 흔합니다.</p>

<div style="background:#eef8f0;border:2px solid #3a9a5b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e38;font-size:18px;">🧾 계산 때 챙길 항목</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>분자는 현금배당인지, 분모는 어떤 이익인지 적어 둡니다.</li><li>EPS와 DPS를 쓰면 주식 수 변화(액면분할 등)가 섞이지 않았는지 봅니다.</li><li>출처가 다른 두 숫자는 같은 기간·같은 분모일 때만 비교합니다.</li></ul>
</div>

<p>EPS 계산이 필요하면 <a href="https://sensitiveboss3.tistory.com/entry/eps-meaning-calculation" target="_blank" rel="noopener">EPS 뜻과 계산 방법</a> 편에 순서가 있습니다.</p>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">이익이 25% 줄면 배당은 어떻게 되나</h2>

<p>순이익이 25% 줄면 EPS는 가나다전자 3,750원, 라마바화학 1,500원이 됩니다. 이때 회사가 배당을 정하는 방식은 크게 두 가지로 나눠서 따져 볼 수 있습니다.</p>

<ol>
  <li>배당성향을 유지하면 DPS가 이익과 같은 비율로 줄어듭니다.</li>
  <li>DPS를 유지하면 배당성향이 올라갑니다.</li>
</ol>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">순이익이 25% 줄었을 때 두 가지 경우 (가상, 주가는 그대로 가정)</caption>
  <thead>
    <tr style="background:#eef8f0;"><th style="border:1px solid #ddd;padding:8px;">구분</th><th style="border:1px solid #ddd;padding:8px;">가나다전자</th><th style="border:1px solid #ddd;padding:8px;">라마바화학</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">줄어든 EPS(원)</td><td style="border:1px solid #ddd;padding:8px;">3,750</td><td style="border:1px solid #ddd;padding:8px;">1,500</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">경우 1: 배당성향 유지 → DPS(원)</td><td style="border:1px solid #ddd;padding:8px;">1,500</td><td style="border:1px solid #ddd;padding:8px;">1,350</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">경우 1: 배당수익률</td><td style="border:1px solid #ddd;padding:8px;">3.0%</td><td style="border:1px solid #ddd;padding:8px;">3.0%</td></tr>
    <tr style="background:#eef8f0;"><td style="border:1px solid #ddd;padding:8px;">경우 2: DPS 유지 → 배당성향</td><td style="border:1px solid #ddd;padding:8px;">53.3%</td><td style="border:1px solid #ddd;padding:8px;">120.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">경우 2: 이익을 넘어 나가는 배당(주당, 원)</td><td style="border:1px solid #ddd;padding:8px;">1,750</td><td style="border:1px solid #ddd;padding:8px;">300</td></tr>
  </tbody>
</table>

<p>경우 1에서는 두 회사 모두 배당수익률이 3.0%로 같아집니다. 경우 2에서는 가나다전자가 53.3%인 반면 <mark>라마바화학은 120.0%로 주당 300원을 이익보다 더 내보냅니다.</mark></p>

<p>어느 쪽을 택할지는 회사가 정합니다. 표는 배당성향이 높을수록 이익 변화에 쓸 수 있는 선택지가 좁아진다는 것만 보여 줍니다.</p>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">배당성향이 100%를 넘으면 읽는 법</h2>

<p>배당성향이 100%를 넘는다는 것은 그해 순이익보다 많은 금액을 배당했다는 뜻입니다. 배당은 그해 순이익만이 아니라 쌓아 둔 이익잉여금 한도 안에서 줄 수 있어서 가능한 일입니다.</p>

<ul>
  <li>일시적 이익 감소 때문이면 한 해만 100%를 넘기도 합니다.</li>
  <li>몇 해 연속이면 쌓아 둔 이익이 줄어드는 구조입니다.</li>
  <li>순이익이 적자면 배당성향은 음수가 되어 해석하지 않습니다.</li>
</ul>

<p>100%를 넘었다고 이미 정해진 배당을 못 받는 것은 아닙니다. 다음 해에도 같은 수준이 이어질지가 문제입니다.</p>

<p>고배당기업 배당소득 분리과세 특례처럼 배당성향이 세금 요건에 들어가는 제도도 있습니다. 요건 수치는 <a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax" target="_blank" rel="noopener">배당소득세 얼마 떼나</a> 편과 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 원문에서 확인하세요.</p>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">배당수익률과 PER로 이어 보는 법</h2>

<p>배당수익률은 배당성향을 PER로 나눈 값과 같습니다. 배당수익률 = DPS ÷ 주가이고, DPS = 배당성향 × EPS, 주가 = PER × EPS이므로 EPS가 서로 사라집니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">배당성향 40%와 90% 회사를 PER로 연결한 값</caption>
  <thead>
    <tr style="background:#eef8f0;"><th style="border:1px solid #ddd;padding:8px;">항목</th><th style="border:1px solid #ddd;padding:8px;">가나다전자</th><th style="border:1px solid #ddd;padding:8px;">라마바화학</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">배당성향 ÷ PER</td><td style="border:1px solid #ddd;padding:8px;">40% ÷ 10.0 = 4.0%</td><td style="border:1px solid #ddd;padding:8px;">90% ÷ 22.5 = 4.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">표의 배당수익률</td><td style="border:1px solid #ddd;padding:8px;">4.0%</td><td style="border:1px solid #ddd;padding:8px;">4.0%</td></tr>
  </tbody>
</table>

<p>두 회사 모두 4.0%로 일치합니다. 배당수익률이 같은 이유가 <mark>가나다전자는 낮은 배당성향에 낮은 PER, 라마바화학은 높은 배당성향에 높은 PER</mark>이어서 서로 상쇄된 결과라는 것도 이 식으로 읽힙니다.</p>

<p>PER 계산은 <a href="https://sensitiveboss3.tistory.com/entry/per-meaning-calculation" target="_blank" rel="noopener">PER 뜻과 계산 방법</a> 편에 정리돼 있습니다. 이 글의 모든 회사명과 숫자는 계산 설명용 가상 값이며 특정 종목에 대한 평가가 아닙니다.</p>

<div style="background:#eef8f0;border:2px solid #3a9a5b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e38;font-size:18px;">🧮 마지막으로 남길 계산</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>배당성향 = 배당금 ÷ 순이익, 또는 DPS ÷ EPS입니다.</li><li>배당수익률 = 배당성향 ÷ PER 이라서 세 숫자는 함께 읽어야 합니다.</li><li>이익이 줄 때 배당성향이 높은 쪽이 선택지가 좁습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #3a9a5b;padding-left:12px;margin-top:36px;">배당성향 숫자를 읽다 떠오르는 궁금증 풀이</h2>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">배당성향이 높으면 무조건 좋은 회사인가요?</summary><p>아닙니다. 배당성향이 높다는 것은 순이익 중 배당으로 나가는 비율이 크다는 뜻일 뿐입니다. 이익이 줄면 같은 배당을 유지하기 어려워질 수 있어서 이익 규모와 함께 봅니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">배당성향이 낮은 회사는 배당을 못 주는 회사인가요?</summary><p>그렇지 않습니다. 이익의 상당 부분을 사업에 다시 쓰는 회사는 배당성향이 낮게 나옵니다. 낮은 숫자는 배당 여력이 남아 있다는 뜻일 수도, 배당에 소극적이라는 뜻일 수도 있습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">순이익 대신 어떤 이익을 분모에 쓰나요?</summary><p>자료마다 당기순이익, 지배주주 귀속 순이익 등 분모 정의가 다를 수 있습니다. 같은 회사라도 출처에 따라 배당성향이 다르게 보이면 분모부터 비교하세요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">배당성향이 100%를 넘으면 배당을 못 받나요?</summary><p>아닙니다. 이미 지급이 결정된 배당은 받습니다. 다만 이익보다 많이 내보내는 상태라서 같은 수준이 계속될지는 이익 흐름에 달려 있습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">고배당기업 분리과세 특례와 배당성향은 관계가 있나요?</summary><p>있습니다. 특례 요건에 배당성향 기준이 들어 있습니다. 세율과 요건은 자주 바뀔 수 있어 이 글에서는 수치를 옮기지 않으니, 배당소득세 편과 국세청 원문에서 확인하세요.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, 배당성향은 기관이 수치를 공표하는 지표가 아니라 회계 비율의 정의이며 아래 자료는 정의와 공식 교차 확인용입니다):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://eiec.kdi.re.kr/material/wordDic.do" target="_blank" rel="noopener">KDI 경제교육·정보센터 - 시사용어사전</a></li>
    <li><a href="https://support.stockplus.com/hc/ko/articles/5054910176793-%EA%B8%B0%EC%97%85%EC%9D%98-%EB%B0%B0%EB%8B%B9-%EC%9D%98%EC%A7%80-%EB%B0%B0%EB%8B%B9%EC%84%B1%ED%96%A5-%EC%B2%B4%ED%81%AC" target="_blank" rel="noopener">증권플러스 고객센터 - 기업의 배당 의지? '배당성향' 체크!</a></li>
    <li><a href="https://www.12manage.com/methods_dividend_payout_ratio_ko.html" target="_blank" rel="noopener">12manage - 배당성향 (Dividend Payout Ratio)</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 배당성향이라는 지표를 풀어 쓴 정보성 글입니다. 특정 종목의 매수나 매도를 권하지 않으며, 본문의 회사와 숫자는 전부 가상입니다. 투자 판단과 그 책임은 투자자 본인에게 있고, 제도와 공시 기준은 달라질 수 있으니 필요하면 원출처를 확인해 주세요.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "배당성향 공식과 이익 줄 때 배당 변화",
      "description": "배당성향 공식(배당금 ÷ 순이익)을 가상 두 회사 사례로 계산하고, 순이익이 25% 줄 때 배당과 배당수익률이 어떻게 달라지는지 표로 정리했습니다.",
      "author": {
        "@type": "Person",
        "name": "센시티브보스"
      },
      "publisher": {
        "@type": "Person",
        "name": "센시티브보스"
      },
      "datePublished": "2026-10-02",
      "dateModified": "2026-10-02",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://sensitiveboss3.tistory.com/entry/dividend-payout-ratio-formula-cushion"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "배당성향이 높으면 무조건 좋은 회사인가요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "아닙니다. 배당성향이 높다는 것은 순이익 중 배당으로 나가는 비율이 크다는 뜻일 뿐입니다. 이익이 줄면 같은 배당을 유지하기 어려워질 수 있어서 이익 규모와 함께 봅니다."
          }
        },
        {
          "@type": "Question",
          "name": "배당성향이 낮은 회사는 배당을 못 주는 회사인가요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "그렇지 않습니다. 이익의 상당 부분을 사업에 다시 쓰는 회사는 배당성향이 낮게 나옵니다. 낮은 숫자는 배당 여력이 남아 있다는 뜻일 수도, 배당에 소극적이라는 뜻일 수도 있습니다."
          }
        },
        {
          "@type": "Question",
          "name": "순이익 대신 어떤 이익을 분모에 쓰나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "자료마다 당기순이익, 지배주주 귀속 순이익 등 분모 정의가 다를 수 있습니다. 같은 회사라도 출처에 따라 배당성향이 다르게 보이면 분모부터 비교하세요."
          }
        },
        {
          "@type": "Question",
          "name": "배당성향이 100%를 넘으면 배당을 못 받나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "아닙니다. 이미 지급이 결정된 배당은 받습니다. 다만 이익보다 많이 내보내는 상태라서 같은 수준이 계속될지는 이익 흐름에 달려 있습니다."
          }
        },
        {
          "@type": "Question",
          "name": "고배당기업 분리과세 특례와 배당성향은 관계가 있나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "있습니다. 특례 요건에 배당성향 기준이 들어 있습니다. 세율과 요건은 자주 바뀔 수 있어 이 글에서는 수치를 옮기지 않으니, 배당소득세 편과 국세청 원문에서 확인하세요."
          }
        }
      ]
    }
  ]
}
</script>
