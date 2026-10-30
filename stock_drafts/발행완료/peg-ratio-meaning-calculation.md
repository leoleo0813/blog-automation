---
keyword: PEG 뜻
title: PEG 뜻 계산 방법과 해석 기준
slug: peg-ratio-meaning-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 2070 (PC 320 / 모바일 1750)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-29 - 통과]
  WebSearch "PEG 뜻 계산법 PER 이익성장률 주가이익증가비율" 상위 10개: guinnessgi.com(해외 자산운용사 콘텐츠),
  dic.hankyung.com(한경용어사전), namu.wiki(백과), insight.stockplus.com(증권플러스 인사이트),
  jcinus.com(개인 운영 블로그), 12manage.com(소규모 경영 콘텐츠), kr/jp.tradingview.com 스크립트 페이지 4건.
  2차 검색(한계·음수 성장률)에서는 brunch.co.kr, buffettlab.co.kr, tbacking.com, jakup.com(계산기)도 노출.
  1) 진입 여지: 있음. jcinus.com, 12manage.com, brunch 등 개인·소규모 콘텐츠가 상위에 섞여 있다.
  2) 검색 의도: 정의 탐색형이 중심이다. 계산기 페이지(jakup.com)가 일부 있으나 지배적이지 않다.
  3) 답 완결 여부: 부분적. 상위 글은 정의, 공식, 린치의 0.5/1.5 기준까지 다루지만, 같은 PER이라도 성장률
     가정에 따라 PEG가 3.0에서 0.8까지 달라지는 민감도 표, 단년도 이익 급증(기저효과)이 PEG를 왜곡하는
     숫자 예시, PER만 보면 순서가 뒤집히는 3개 가상 기업 비교를 함께 보여주는 글은 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 기업 3곳 PER 대비 PEG 비교표(PER 30배 PEG 1.0 / PER 12배 PEG 4.0 / PER 20배 PEG 0.5).
  (b) 같은 PER 24배에 성장률 가정 8·12·24·30%를 넣은 PEG 민감도 표(3.0 / 2.0 / 1.0 / 0.8).
  (c) EPS 1,000→1,500원을 3년 연평균 성장률(약 14.5%)로 환산해 PEG 1.38을 구하는 계산 과정,
      그리고 단년도 100% 급증이 만드는 PEG 0.15의 착시 예시.
primary_source: |
  1차 출처(정부·거래소)에는 PEG 정의가 없어 한경용어사전(dic.hankyung.com/economy/view/?seq=4564)을
  WebFetch 1회 시도했으나 EGRESS_BLOCKED로 막혔다. 세율·한도 같은 제도 수치가 아니라 지표 정의라서
  WebSearch 교차검증으로 진행했다. 독립 출처 5곳(한경용어사전, 증권플러스 인사이트, Guinness Global
  Investors, 12manage, 나무위키)과 보조 4곳(brunch, buffettlab, tbacking, jcinus)에서 PEG = PER ÷ EPS 증가율,
  피터 린치의 0.5 이하 저평가·1.5 이상 고평가 기준, 성장률은 과거 3년 연평균 또는 향후 2~3년 예상 평균을
  쓴다는 점이 충돌 없이 일치했다. 일반 해석(1 미만 저평가, 1 적정, 1 초과 고평가)과 린치 기준의 임계값이
  다르다는 점은 본문에서 구분해 적었다.
기준일: 2026년 9월 기준 (지표 정의와 해석 기준. 계산 예시의 주가·EPS·성장률은 전부 가상)
tags: PEG, PEG 뜻, PEG 비율, 주가이익성장비율, PEG 계산, 피터 린치, PER, EPS 성장률, 성장주 지표, 주식 지표
gate_pass: true
gate_pass_note: |
  게이트1 2,070회(500 이상). 게이트2 v3 통과. 게이트3 가상 기업 비교표, 성장률 민감도 표, 계산 과정.
  게이트4는 원문 WebFetch 실패 후 다수 독립 출처 교차검증(제도 수치가 아니라 지표 정의).
  사람은 발행 전 한경용어사전 PEG 항목에서 린치 기준(0.5, 1.5)만 눈으로 확인하면 충분하다.
capture_guide: ""
self_check: |
  [2026-09-29 gate_pass:true]
  후보 경위: 신규 8개 실측(부채비율 뜻 50, 이자보상배율 뜻 50, PSR 뜻 270, EV/EBITDA 뜻 90, ROA 뜻 160,
  잉여현금흐름 뜻 40, 영업이익률 뜻 20 FAIL / PEG 뜻 2,070 PASS). 백로그에 이미 게이트1을 통과한 후보들은
  게이트2·4 또는 카니벌라이제이션 사유로 보류 상태여서 신규 키워드를 채택했다.
  카니벌라이제이션: 기존 98편 중 PEG 전용 편 없음. PER 뜻(per-meaning-calculation)·EPS 뜻 편은 PEG를 언급하지 않음(grep 0건).
  볼린저밴드 편의 PEG 언급은 무관한 문맥.
  YMYL: 특정 종목 추천·목표가·매매시점 없음. 예시 기업은 전부 가상 A·B·C. 저평가·고평가 판단은 "지표가 그렇게 읽힌다"로 한정하고 단정 표현 없음.
  기관 링크: 기관 안내 문장 1개(KRX, DART) 전부 링크, 출처 목록 4개 전부 링크.
  제목 "PEG 뜻 계산 방법과 해석 기준" 16자, 금지어 없음. 슬러그 영문 소문자 하이픈 4단어.
  첫 문장 유형: 결론형(직전 98편 수치충격형, 97편 문제제기형과 다름).
  글 구조 유형: 비교형(목차 직후 가상 기업 3곳 비교표). 직전 98편 계산형과 다름.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 5개, FAQ 5개, H2 5개 중 "~나요"형 2개.
  요약박스 보라색(#f3edf9/#6a3fa0), 제목 "🔎 PEG, 이것만 기억하세요". FAQ 헤딩 "PEG를 볼 때 자주 걸리는 질문".
  면책 문구 새 표현. 헤지 표현 최소화.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-29</p>

<p>PEG는 PER을 이익성장률로 나눈 값이라서, PER이 높아도 이익이 빠르게 자라는 회사는 낮게 나옵니다. 그래서 PER만 보면 비싸 보이던 회사가 PEG로는 다르게 읽힐 수 있습니다. 이 글은 PEG 뜻과 계산 방법, 수치 해석 기준, 성장률 가정에 따른 함정을 가상의 숫자로 정리합니다.</p>

<div style="background:#f3edf9;border:2px solid #6a3fa0;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4a2a78;font-size:18px;">🔎 PEG, 이것만 기억하세요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>PEG는 PER을 EPS(주당순이익) 증가율로 나눈 값입니다. 성장률은 % 숫자만 넣습니다.</li>
    <li>피터 린치는 0.5 이하를 저평가, 1.5 이상을 고평가로 봤고, 일반적으로는 1을 기준선으로 씁니다.</li>
    <li>성장률을 어떻게 잡느냐에 따라 같은 PER도 PEG가 크게 달라져서 산정 기준부터 확인해야 합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PER이 다른 가상 기업 3곳으로 PEG 비교하기</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PEG 뜻과 계산 공식</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PEG 수치를 읽는 기준</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">성장률 가정에 따라 PEG가 얼마나 달라지나요</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PEG가 잘 맞지 않는 경우</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PEG를 볼 때 자주 걸리는 질문</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">PER이 다른 가상 기업 3곳으로 PEG 비교하기</h2>

<p>PER 순서와 PEG 순서는 서로 다를 수 있습니다. 아래는 이해를 돕기 위해 만든 가상의 기업 A, B, C입니다. 실제 종목이 아닙니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가상 기업</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">PER</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">EPS 증가율</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">PEG</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">A</td><td style="border:1px solid #ddd;padding:8px;">30배</td><td style="border:1px solid #ddd;padding:8px;">연 30%</td><td style="border:1px solid #ddd;padding:8px;">1.0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">B</td><td style="border:1px solid #ddd;padding:8px;">12배</td><td style="border:1px solid #ddd;padding:8px;">연 3%</td><td style="border:1px solid #ddd;padding:8px;"><mark>4.0</mark></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">C</td><td style="border:1px solid #ddd;padding:8px;">20배</td><td style="border:1px solid #ddd;padding:8px;">연 40%</td><td style="border:1px solid #ddd;padding:8px;">0.5</td></tr>
  </tbody>
</table>

<p>PER만 보면 B가 가장 낮습니다. 그런데 이익이 연 3%밖에 늘지 않아서 PEG는 4.0으로 셋 중 가장 높습니다.</p>

<p>반대로 A는 PER이 30배로 가장 높지만, 성장률이 30%여서 PEG는 1.0입니다. PEG는 "이 PER을 성장 속도가 얼마나 받쳐주는가"를 보는 지표입니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">PEG 뜻과 계산 공식</h2>

<p>PEG(Price/Earnings-to-Growth ratio, 주가이익성장비율)는 PER을 EPS 증가율로 나눈 값입니다. 미국 투자자 피터 린치가 널리 알린 지표로, PER이 기업의 성장성을 반영하지 못하는 약점을 보완하려는 목적입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <strong>PEG = PER ÷ EPS 증가율(%)</strong><br>
  예: PER 20배, EPS 증가율 15% → 20 ÷ 15 = 약 1.33
</div>

<p>계산할 때는 증가율에서 % 기호를 떼고 숫자만 넣습니다. 15%면 15로 나눕니다. 0.15로 나누면 값이 100배로 커집니다.</p>

<p>PER과 EPS의 뜻이 아직 낯설다면 <a href="https://sensitiveboss3.tistory.com/entry/per-meaning-calculation" target="_blank" rel="noopener">PER 뜻과 계산 방법</a> 글을 먼저 보면 이해가 빠릅니다. 종목별 PER과 EPS는 <a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a>에서 무료로 조회할 수 있고, EPS의 근거가 되는 재무제표 원문은 <a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a>에서 열람합니다.</p>

<p>EPS 증가율을 직접 구하는 예시도 하나 봅니다. 가상 기업의 EPS가 3년 전 1,000원에서 올해 1,500원이 됐다면 3년 연평균 증가율은 약 14.5%입니다.</p>

<ol style="line-height:1.9;">
  <li>3년간 총 증가 배수는 1,500 ÷ 1,000 = 1.5배입니다.</li>
  <li>연평균 증가율은 1.5의 3제곱근 - 1 = 약 0.1447, 즉 14.5%입니다.</li>
  <li>이 기업의 PER이 20배라면 PEG는 20 ÷ 14.5 = <mark>약 1.38</mark>입니다.</li>
</ol>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">PEG 수치를 읽는 기준</h2>

<p>가장 널리 쓰이는 해석은 PEG 1을 기준선으로 보는 방식입니다. 1보다 낮으면 성장에 비해 PER이 낮은 편, 1보다 높으면 성장에 비해 PER이 높은 편으로 읽습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">PEG 값</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">일반적 해석</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">피터 린치 기준</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">0.5 이하</td><td style="border:1px solid #ddd;padding:8px;">1 미만: 성장 대비 PER 낮음</td><td style="border:1px solid #ddd;padding:8px;"><mark>저평가로 판단</mark></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1 전후</td><td style="border:1px solid #ddd;padding:8px;">성장과 PER이 균형(공정 가치)</td><td style="border:1px solid #ddd;padding:8px;">별도 구간 없음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1.5 이상</td><td style="border:1px solid #ddd;padding:8px;">1 초과: 성장 대비 PER 높음</td><td style="border:1px solid #ddd;padding:8px;"><mark>고평가로 판단</mark></td></tr>
  </tbody>
</table>

<p>기준이 두 갈래인 이유는 경계가 다르기 때문입니다. 일반 해석은 1 하나로 가르고, 린치는 0.5와 1.5 사이를 넓은 중간지대로 둡니다.</p>

<p>이 표는 지표를 읽는 방법일 뿐 매수·매도 신호가 아닙니다. 어느 기준을 따를지는 읽는 사람이 정합니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">성장률 가정에 따라 PEG가 얼마나 달라지나요</h2>

<p>PEG의 분모는 사람이 고르는 숫자라서, 같은 PER도 성장률 가정에 따라 값이 달라집니다. 성장률로는 최근 3년 EPS 연평균 증가율(과거 기준)을 쓰기도 하고, 향후 2~3년 예상 EPS 증가율(증권사 전망 기준)을 쓰기도 합니다.</p>

<p>PER 24배인 가상 기업에 성장률 가정만 바꿔서 넣은 결과입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">가정한 EPS 증가율</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">계산</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">PEG</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">8%</td><td style="border:1px solid #ddd;padding:8px;">24 ÷ 8</td><td style="border:1px solid #ddd;padding:8px;">3.0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12%</td><td style="border:1px solid #ddd;padding:8px;">24 ÷ 12</td><td style="border:1px solid #ddd;padding:8px;">2.0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">24%</td><td style="border:1px solid #ddd;padding:8px;">24 ÷ 24</td><td style="border:1px solid #ddd;padding:8px;">1.0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">30%</td><td style="border:1px solid #ddd;padding:8px;">24 ÷ 30</td><td style="border:1px solid #ddd;padding:8px;"><mark>0.8</mark></td></tr>
  </tbody>
</table>

<p>같은 기업인데 3.0에서 0.8까지 벌어집니다. 그래서 PEG 수치를 볼 때는 값 자체보다 어떤 성장률을 썼는지가 먼저입니다.</p>

<p>단년도 이익이 급증한 경우도 조심해야 합니다. 가상 기업의 EPS가 1,000원, 600원, 500원, 1,000원으로 움직였다고 하겠습니다. 마지막 해만 보면 전년 대비 100% 증가이고, PER이 15배면 PEG는 15 ÷ 100 = 0.15로 아주 낮게 나옵니다.</p>

<p>그런데 3년 전 1,000원에서 올해 1,000원이라 3년 연평균 증가율은 0%입니다. 같은 기업이 어느 기간을 잡느냐에 따라 저평가처럼도, 계산 불가처럼도 보입니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">PEG가 잘 맞지 않는 경우</h2>

<p>이익이 줄거나 적자인 기업에는 PEG를 그대로 쓸 수 없습니다. 증가율이 음수면 PEG도 음수가 되고, 음수 PEG는 "싸다"는 뜻이 아닙니다.</p>

<ul style="line-height:1.9;">
  <li>EPS가 감소하거나 적자인 기업: 증가율이 음수라서 의미 있는 값이 나오지 않습니다.</li>
  <li>일회성 이익이나 기저효과로 EPS가 갑자기 튄 기업: 단년도 성장률이 PEG를 왜곡합니다.</li>
  <li>성장이 거의 없는 성숙 산업: 증가율이 0에 가까워 PEG가 매우 커지거나 계산이 안 됩니다.</li>
  <li>예상 EPS가 증권사마다 크게 다른 기업: 어느 전망을 쓰느냐에 따라 값이 달라집니다.</li>
</ul>

<p>PEG는 PER 하나만 볼 때의 빈틈을 채우는 보조 지표입니다. 부채 수준, 현금흐름, 업종 특성 같은 다른 정보를 대신해 주지 않으므로 여러 지표 중 하나로 읽는 편이 안전합니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #6a3fa0;padding-left:12px;margin-top:36px;">PEG를 볼 때 자주 걸리는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PEG가 1보다 낮으면 무조건 사도 되나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. PEG는 성장 대비 PER 수준을 보여주는 지표이고 매수 신호가 아닙니다. 성장률 가정이 틀리면 낮은 PEG도 착시일 수 있습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PEG 계산에서 성장률은 몇 년치를 쓰나요</summary>
  <p style="margin:10px 0 0 0;">정해진 표준은 없습니다. 최근 3년 EPS 연평균 증가율이나 향후 2~3년 예상 EPS 증가율의 평균을 쓰는 방식이 흔하고, 어느 쪽인지 밝히지 않은 PEG는 비교하기 어렵습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PER과 PEG 중 무엇이 더 좋은 지표인가요</summary>
  <p style="margin:10px 0 0 0;">우열을 가릴 수 없고 용도가 다릅니다. PER은 현재 이익 대비 가격, PEG는 성장 속도까지 반영한 가격 수준을 보여주므로 함께 봅니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PEG가 음수로 나오면 어떻게 읽나요</summary>
  <p style="margin:10px 0 0 0;">해석하지 않습니다. EPS가 줄었거나 적자라는 신호이고, PEG는 이익이 늘어나는 기업을 전제로 한 지표입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">피터 린치의 0.5와 1.5 기준은 지금도 통하나요</summary>
  <p style="margin:10px 0 0 0;">참고용 기준선으로 소개되는 수치입니다. 시장과 업종에 따라 적정 수준이 달라서 절대적인 합격선으로 쓰기는 어렵습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://dic.hankyung.com/economy/view/?seq=4564" target="_blank" rel="noopener">한국경제 - 한경용어사전 PEG</a></li>
    <li><a href="https://insight.stockplus.com/articles/5683" target="_blank" rel="noopener">증권플러스 인사이트 - PEG를 보면 저평가·성장주 보인다</a></li>
    <li><a href="https://www.guinnessgi.com/insights/peg-ratio" target="_blank" rel="noopener">Guinness Global Investors - Price/Earnings-to-Growth (PEG) Ratio</a></li>
    <li><a href="https://www.12manage.com/methods_peg_ratio_ko.html" target="_blank" rel="noopener">12manage - 주가수익성장성비율(PEG Ratio)</a></li>
  </ul>
  기준일: 2026년 9월 기준. 본문의 기업, 주가, EPS, 성장률은 이해를 돕기 위한 가상의 예시이며 실제 종목과 무관합니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 지표의 계산과 해석을 설명하는 정보 글로, 특정 종목이나 상품의 매수·매도를 권하지 않습니다. 실제 투자 결정과 그에 따른 손익은 투자자 본인의 몫이며, 지표 값은 시점과 산정 방식에 따라 달라지므로 최신 자료를 직접 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "PEG 뜻 계산 방법과 해석 기준",
  "description": "PEG 뜻과 PER을 EPS 증가율로 나누는 계산 방법, 피터 린치의 해석 기준, 성장률 가정에 따라 값이 달라지는 이유를 가상의 숫자로 정리합니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Organization",
    "name": "센시티브보스"
  },
  "datePublished": "2026-09-29",
  "dateModified": "2026-09-29",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/peg-ratio-meaning-calculation"
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
      "name": "PEG가 1보다 낮으면 무조건 사도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. PEG는 성장 대비 PER 수준을 보여주는 지표이고 매수 신호가 아닙니다. 성장률 가정이 틀리면 낮은 PEG도 착시일 수 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "PEG 계산에서 성장률은 몇 년치를 쓰나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 표준은 없습니다. 최근 3년 EPS 연평균 증가율이나 향후 2~3년 예상 EPS 증가율의 평균을 쓰는 방식이 흔하고, 어느 쪽인지 밝히지 않은 PEG는 비교하기 어렵습니다."
      }
    },
    {
      "@type": "Question",
      "name": "PER과 PEG 중 무엇이 더 좋은 지표인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "우열을 가릴 수 없고 용도가 다릅니다. PER은 현재 이익 대비 가격, PEG는 성장 속도까지 반영한 가격 수준을 보여주므로 함께 봅니다."
      }
    },
    {
      "@type": "Question",
      "name": "PEG가 음수로 나오면 어떻게 읽나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "해석하지 않습니다. EPS가 줄었거나 적자라는 신호이고, PEG는 이익이 늘어나는 기업을 전제로 한 지표입니다."
      }
    },
    {
      "@type": "Question",
      "name": "피터 린치의 0.5와 1.5 기준은 지금도 통하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "참고용 기준선으로 소개되는 수치입니다. 시장과 업종에 따라 적정 수준이 달라서 절대적인 합격선으로 쓰기는 어렵습니다."
      }
    }
  ]
}
</script>
