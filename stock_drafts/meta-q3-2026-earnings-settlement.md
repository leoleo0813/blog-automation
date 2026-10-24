---
keyword: 메타 실적발표
title: 메타 실적발표 3분기, 합의금 반영 전후 비교
slug: meta-q3-2026-earnings-settlement
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 확인필요
gate1_pass: false
serp_check: |
  [게이트2 v4 판정 2026-10-24 - 통과] 메타 실적발표 월 23,500(2026-10-24 실측, PC 3,000 / 모바일 20,500)으로 v4 대상(월 5,000 이상).
  WebSearch(미국 기준, 참고용) 상위: 연합뉴스 계열 속보(specialtimes 등), 블록미디어·stockhub 같은 소규모 매체, 증권사·환율 정리 사이트. 발표 직후라 속보 기사 위주이고 진입 여지 있음(소규모 매체·개인 정리 글 다수).
  1) 진입 여지 - 있음. 2) 검색 의도 - 실적 결과 확인, 조회·신청 도구 아님. 3) 답 완결 - 아님. 속보는 매출·EPS 두 숫자 위주이고, 합의금 충당금 반영 전후 영업이익률 비교, 광고 노출×단가 분해, 설비투자와 잉여현금흐름 계산, 클래스C 주식배당 일정을 한 글에서 구분해 둔 곳은 확인하지 못함.
  → 탈락조건 1~3 미해당, 통과.
unique_asset: |
  (a) 공시값 vs 합의금 충당금 제외값 비교표(영업이익 12.99→22.88십억 달러, 영업이익률 20.1%→35.4%, EPS 3.83→7.40)와 막대그림.
  (b) 광고 매출 증가율 분해 계산(노출 +10% × 단가 +14% = 약 +25.4%)과 4분기 가이던스 증가율(+13.0~17.6%).
  (c) 영업활동 현금흐름 32.79 − 설비투자 34.91 = 잉여현금흐름 −2.12십억 달러 계산과 그림.
  (d) 클래스C 주식배당 진행 단계 타임라인 그림과 100주 보유 가상 계산.
primary_source: |
  메타 IR·SEC(EDGAR) 원문은 WebFetch getaddrinfo ENOTFOUND로 열람 불가. WebSearch가 보여 준 SEC 8-K·10-Q 요약과 언론 교차검증으로 진행.
  - 발표일 2026-10-21 미국 장 마감 후, 콘퍼런스콜 미국 동부 오후 4시 30분: 메타 IR 보도자료(10/12 공지), PRNewswire 재게재, 언론 다수 일치. 10/28로 적은 일부 일정 사이트는 공지 전 추정치로 판단해 제외.
  - 매출 646억 달러(+26%), 희석 EPS 3.83달러(전년 1.05달러), 영업이익 12.99십억 달러(-37%), 청소년 소송 합의 충당금 9.89십억 달러, 충당금 제외 EPS 7.40달러, 4분기 매출 가이던스 730억~760억 달러: 연합뉴스 계열(specialtimes), Variety, PPC Land, AP 계열(wdbo), SiliconANGLE 등 5곳 이상 일치.
  - 광고 노출 +10%, 광고당 평균 가격 +14%: 연합뉴스 계열과 AP 계열 일치.
  - 설비투자 34.91십억 달러, 영업활동 현금흐름 32.79십억 달러, 잉여현금흐름 -2.12십억 달러, 올해 설비투자 전망 135~145십억 달러(하한 130→135): 연합뉴스 계열과 영문 매체 2곳 이상 일치.
  - 클래스C 주식배당: 8-K(2026-10-19) 요약, 10-Q 요약, SiliconANGLE 보도 일치. 기준일·지급일은 이사회가 추후 결정.
  - 일부러 쓰지 않은 값: 시장 예상 EPS(3.56/5.46/5.75달러 등 집계처마다 달라 불일치), 합의 총액(185.9억 vs 180억 달러), 리얼리티랩스 수치(연합뉴스 계열 1곳), 시간외 주가 반응(2~4%로 보도 불일치). 매출 시장 예상은 "약 633억~634억 달러"로만 표기.
  - 세율·한도 같은 법정 수치는 없음.
기준일: 2026년 10월 24일 기준
refresh_due: 2026-11-21
refresh_reason: "클래스C 주식배당 기준일·지급일이 정해지면 반영, 메타 IR 원문과 3분기 보도자료 숫자 직접 대조"
tags: 메타 실적발표, 메타 3분기 실적, 메타 실적, 메타 클래스C 주식, 메타 주식배당, 메타 합의금, 메타 설비투자, 메타 잉여현금흐름, 메타 주식분할, 미국주식 실적 시즌
cannibalization_note: |
  엔비디아 실적발표 글은 발표일·한국시간 환산·가이던스 대비 매출, 컨센서스 글은 예상치 비교 일반론, CAPEX 글은 개념과 공식이다. 이 글은 메타 한 회사의 3분기 확정 숫자 해석(일회성 충당금 전후 비교, 설비투자로 마이너스가 된 현금흐름, 클래스C 일정)이라 대상과 의도가 다르다. 컨센서스·CAPEX·EPS·액면분할 글로 내부 링크.
gate_pass: true
gate_pass_note: |
  게이트1 23,500회(workflow 자동 기입 전 실측값), 게이트2 v4 통과, 게이트3 비교표·분해 계산·현금흐름 계산·그림 3장, 게이트4 원문 열람은 막혔으나 핵심 숫자는 5곳 이상 독립 보도가 일치(엇갈린 값은 본문에서 제외). 사람이 발행 전 메타 IR 3분기 보도자료(investor.atmeta.com)에서 매출 646억·EPS 3.83달러를 한 번 대조하면 더 안전.
figure_plan: |
  3장. 1: 공시 영업이익 vs 충당금 vs 합산(크기 비교). 2: 영업현금흐름·설비투자·잉여현금흐름(크기 비교, 다른 지표). 3: 클래스C 주식배당 진행 일정(시간 순서). 서로 다른 정보라 합치지 않음. 정확한 숫자를 읽어야 하는 비교표는 그림으로 중복하지 않고 표로 둠.
self_check: |
  [2026-10-24 gate_pass:true]
  후보 경위: 이슈 스캔(빅테크 실적 시즌, 서머타임 종료, 11월 증시 일정) 뒤 실측 12개: 엔비디아 실적발표 1,710(143편이 다룸) / 마이크로소프트 1,080 / 애플 20·아마존 350·팔란티어 240 FAIL / 구글 1,370 / 메타 실적발표 23,500(채택) / 삼성전자 배당 기준일 11,490(126편이 다룸) / SK하이닉스 실적발표 4,990(142편이 다룸) / 연말정산 달라지는 것 20·2026 연말정산 변경 20 FAIL. 메타가 압도적 1위이고 10/21 발표 직후라 시의성 유형 1(이벤트 직후 수요). 시장 예상치·합의 총액처럼 보도가 엇갈리는 값은 본문에서 제외.
  105편 국채금리·98편 달러인덱스·119편 공포탐욕지수 갱신은 10/24에도 언론 2곳 일치 값을 못 구해 보류(기한 유지).
  YMYL: 매수·매도 권유, 목표가, 방향 예측 없음. 제목·소제목에 전망·추천 없음. 가상 계산은 A씨(가상) 명시.
  카니벌라이제이션: 위 cannibalization_note 참조. 내부 링크 4개(컨센서스 82·CAPEX 102·EPS 90·액면분할 45편) 전부 published, 엔비디아 글(143편, drafted)은 보조 링크 1개.
  글 구조 유형: 비교형(첫 H2가 비교표로 시작). 직전 164 계산형, 163 비교형(연속 아님, 164가 사이에 있음).
  첫 문장 유형: 절차형(직전 164 정의형, 163 문제제기형, 162 대비형, 161 수치충격형과 다름). 인트로 둘째 문장에 직접 답(매출 646억, EPS 3.83달러, 충당금 제외 7.40달러).
  어투 모드: C 사례형(가상 인물 A씨, 가상임을 명시). 직전 164 A, 163 B와 다름. 꾸며낸 1인칭 경험 없음.
  기관 안내 문장 링크 처리(메타 IR·SEC), 출처 목록 7개 전부 링크 처리. 본문에 내부 글 번호 노출 없음.
  AI 티 점검: em대시 0개, 다만 0회, mark 4개, FAQ 5개(직전 164 6개, 163 4개와 다름), FAQ 헤딩 "발표 다음 날 아침에 나오는 질문들"(신규), 요약박스 장미색(#fff1f2/#e11d48) 제목 "🧮 숫자 읽기 전에 쥘 것 셋"(신규).
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-24</p>

<p>메타 3분기 실적을 읽으려면 공시된 숫자와 일회성 합의금 충당금을 먼저 나눠 놓고 봐야 합니다. 매출은 646억 달러로 26% 늘었고, 희석 주당순이익 3.83달러에는 98억 9천만 달러 충당금이 들어 있어 이를 뺀 회사 설명값은 7.40달러입니다.</p>

<div style="background:#fff1f2;border:2px solid #e11d48;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#9f1239;font-size:18px;">🧮 숫자 읽기 전에 쥘 것 셋</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>영업이익 12.99십억 달러는 전년보다 37% 줄었지만, 충당금 9.89십억 달러를 더하면 22.88십억 달러가 됩니다.</li>
    <li>번 현금(32.79십억)보다 설비투자(34.91십억)가 커서 잉여현금흐름이 -2.12십억 달러였습니다.</li>
    <li>클래스C 주식배당은 정관 효력일이 2027년 1월 19일이고 기준일·지급일은 아직 없습니다.</li>
  </ul>
</div>

<h2>목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">공시값과 충당금 제외값을 나란히 놓으면</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">매출 26% 증가를 노출과 단가로 쪼개면</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">설비투자가 현금흐름을 마이너스로 만든 계산</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">클래스C 주식배당은 어디까지 정해졌나요</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">메타 실적이 주식 투자자에게 왜 중요한가</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">발표 다음 날 아침에 나오는 질문들</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #e11d48;padding-left:12px;margin-top:36px;">공시값과 충당금 제외값을 나란히 놓으면</h2>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:15px;">
  <thead><tr><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">공시값</th><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">충당금 제외 값</th><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">어떻게 나온 값인가</th></tr></thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">매출</td><td style="border:1px solid #ddd;padding:8px;">64.60십억 달러</td><td style="border:1px solid #ddd;padding:8px;">64.60십억 달러</td><td style="border:1px solid #ddd;padding:8px;">충당금은 비용이라 매출은 같음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">영업이익</td><td style="border:1px solid #ddd;padding:8px;">12.99십억 달러</td><td style="border:1px solid #ddd;padding:8px;">22.88십억 달러</td><td style="border:1px solid #ddd;padding:8px;">12.99 + 9.89 (계산)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">영업이익률</td><td style="border:1px solid #ddd;padding:8px;">20.1%</td><td style="border:1px solid #ddd;padding:8px;">35.4%</td><td style="border:1px solid #ddd;padding:8px;">영업이익 ÷ 매출 (계산)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">희석 주당순이익</td><td style="border:1px solid #ddd;padding:8px;">3.83달러</td><td style="border:1px solid #ddd;padding:8px;">7.40달러</td><td style="border:1px solid #ddd;padding:8px;">회사가 밝힌 충당금 제외값</td></tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/meta-q3-2026-earnings-settlement-1.png" alt="메타 2026년 3분기 공시 영업이익 12.99십억 달러, 합의 충당금 9.89십억 달러, 충당금을 더한 22.88십억 달러를 비교한 막대그래프" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 연합뉴스 계열·Variety·PPC Land 보도 교차 확인, 2026-10-24</figcaption></figure>

<p>충당금은 8월에 미국 주 정부들과 청소년 정신건강 관련 소송을 합의하면서 3분기 비용으로 잡은 일회성 항목입니다. <mark>같은 분기 영업이익은 전년 대비 37% 줄었는데, 그 원인이 광고 부진이 아니라 이 충당금이라는 점이 핵심입니다.</mark></p>

<p>가상 인물 A씨는 "EPS 3.83달러, 시장 예상 미달"이라는 제목만 보고 실적이 나빴다고 생각했다고 해 봅시다. 같은 기사 아래쪽을 보면 충당금을 빼면 7.40달러라는 회사 설명이 있습니다.</p>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 EPS 해석 때 알아 둘 점</strong>
  <p style="margin:8px 0 0 0;">충당금 제외값 7.40달러는 메타가 설명한 값이고 회계 기준 숫자는 3.83달러입니다. 보도마다 시장 예상 EPS가 3.56달러부터 5.75달러까지 달라서 이 글은 예상치와의 비교를 쓰지 않습니다. 예상치와 실제를 비교하는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/consensus-estimate-check-guide" target="_blank" rel="noopener">컨센서스 뜻과 확인 방법</a> 글에 있습니다.</p>
</div>

<p>EPS가 어떻게 계산되는지부터 알고 싶다면 <a href="https://sensitiveboss3.tistory.com/entry/eps-meaning-calculation" target="_blank" rel="noopener">EPS 뜻과 계산 방법</a> 글을 먼저 보면 이 표의 마지막 줄이 쉽게 읽힙니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #e11d48;padding-left:12px;margin-top:36px;">매출 26% 증가를 노출과 단가로 쪼개면</h2>

<div style="background:#f8f9fa;border:1px solid #dee2e6;border-radius:8px;padding:14px 18px;margin:16px 0;line-height:1.9;">
  <strong>광고 매출 증가율 ≈ (1 + 노출 증가율) × (1 + 단가 증가율) − 1</strong><br>
  광고 노출 +10%, 광고당 평균 가격 +14%<br>
  1.10 × 1.14 = 1.254, 약 +25.4%
</div>

<p>메타가 3분기에 보고한 광고 노출은 전년보다 10%, 광고 한 건당 평균 가격은 14% 올랐습니다. 두 숫자를 곱하면 약 25.4%이고, 앱 제품군 전체 매출 증가율 26% 안팎과 거의 같은 수준입니다.</p>

<p>노출과 단가 중 어느 쪽이 더 많이 기여했는지는 이 곱셈 구조에서 바로 보입니다. <mark>노출이 10% 늘고 단가가 14% 늘었다는 것은 광고를 더 많이 보여 주면서 한 건당 값도 더 받았다는 뜻입니다.</mark></p>

<p>회사가 제시한 4분기 매출 가이던스는 730억~760억 달러입니다. 3분기 646억 달러와 비교하면 아래처럼 계산됩니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:15px;">
  <thead><tr><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">4분기 가이던스</th><th style="border:1px solid #ddd;padding:8px;background:#fff1f2;text-align:left;">3분기 매출 대비</th></tr></thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">하단</td><td style="border:1px solid #ddd;padding:8px;">73.0십억 달러</td><td style="border:1px solid #ddd;padding:8px;">73 ÷ 64.60 − 1 ≈ +13.0%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">상단</td><td style="border:1px solid #ddd;padding:8px;">76.0십억 달러</td><td style="border:1px solid #ddd;padding:8px;">76 ÷ 64.60 − 1 ≈ +17.6%</td></tr>
  </tbody>
</table>

<p>3분기 매출 646억 달러는 시장 예상(보도마다 약 633억~634억 달러)보다 약 2% 높았습니다. 가이던스는 회사 전망이고 실제 결과는 4분기 실적 발표 때 확정됩니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #e11d48;padding-left:12px;margin-top:36px;">설비투자가 현금흐름을 마이너스로 만든 계산</h2>

<div style="background:#f8f9fa;border:1px solid #dee2e6;border-radius:8px;padding:14px 18px;margin:16px 0;line-height:1.9;">
  <strong>잉여현금흐름 = 영업활동 현금흐름 − 설비투자</strong><br>
  32.79 − 34.91 = −2.12 (십억 달러)<br>
  설비투자 ÷ 매출 = 34.91 ÷ 64.60 ≈ 54.0%
</div>

<p>3분기 설비투자는 34.91십억 달러였고, 같은 기간 영업활동으로 번 현금은 32.79십억 달러였습니다. 번 돈보다 데이터센터와 AI 칩 확보에 쓴 돈이 2.12십억 달러 더 많아서 잉여현금흐름이 마이너스가 됐습니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/meta-q3-2026-earnings-settlement-2.png" alt="메타 2026년 3분기 영업활동 현금흐름 32.79십억 달러, 설비투자 34.91십억 달러, 잉여현금흐름 마이너스 2.12십억 달러를 비교한 막대그래프" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 연합뉴스 계열·영문 매체 보도 교차 확인, 설비투자에는 금융리스 원금 상환 포함, 2026-10-24</figcaption></figure>

<p>메타는 올해 설비투자 전망을 135~145십억 달러로 좁혔고, 이전 범위(130~145십억 달러)보다 하단이 5십억 달러 올랐습니다. 잉여현금흐름이 왜 이익과 다르게 움직이는지는 <a href="https://sensitiveboss3.tistory.com/entry/capex-meaning-free-cash-flow" target="_blank" rel="noopener">CAPEX 뜻과 잉여현금흐름 계산 방법</a> 글에 단계별 계산이 있습니다.</p>

<p>충당금은 영업이익에는 잡히지만 설비투자는 현금 지출이라 두 숫자는 서로 다른 이야기를 합니다. 이번 분기에는 이익이 합의금 때문에 줄고, 현금은 설비투자 때문에 줄었다고 나누어 읽으면 됩니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #e11d48;padding-left:12px;margin-top:36px;">클래스C 주식배당은 어디까지 정해졌나요</h2>

<p>메타 이사회는 의결권 없는 클래스C 보통주를 기존 클래스A·B 주식 1주당 1주씩 한 번 나눠 주는 주식배당을 결의했습니다. 회사는 이 배당이 끝나면 클래스A 주가에 2대1 주식분할 효과가 반영될 것으로 본다고 밝혔습니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/meta-q3-2026-earnings-settlement-3.png" alt="메타 클래스C 주식배당의 이사회 결의 2026-10-19, 개정 정관 제출 10-21경, 효력 발생 2027-01-19, 기준일과 지급일 미정을 나타낸 타임라인" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 메타 8-K(2026-10-19) 요약 보도·SiliconANGLE, 2026-10-24</figcaption></figure>

<ul style="line-height:1.9;">
  <li>이 배당은 개정 정관이 효력을 얻는 조건으로 결의됐고, 효력일은 2027년 1월 19일입니다.</li>
  <li>기준일과 지급일은 이사회가 추후 정하며, 지급일은 정관 효력 발생 뒤 5영업일 이내입니다.</li>
  <li>클래스C 주식은 의결권이 없어서 주주의 의결권 비중은 바뀌지 않는다고 회사가 밝혔습니다.</li>
</ul>

<p>가상 인물 A씨가 클래스A 100주를 갖고 있다면 배당일 이후 클래스C 100주를 받아 총 200주가 됩니다. 한 주의 가격이 절반 수준으로 조정될 것이라는 회사 설명이 있지만 실제 가격은 시장에서 정해지고, 이 계산은 가상 사례입니다.</p>

<p>국내 상장사의 액면분할은 매매정지 기간 같은 절차가 따로 있습니다. 비교해 보고 싶다면 <a href="https://sensitiveboss3.tistory.com/entry/stock-split-trading-halt" target="_blank" rel="noopener">액면분할 매매정지 기간</a> 글을 참고하세요.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #e11d48;padding-left:12px;margin-top:36px;">메타 실적이 주식 투자자에게 왜 중요한가</h2>

<p>메타 실적은 온라인 광고 경기와 AI 투자 부담이 한 분기 안에서 동시에 드러나는 숫자입니다. 방향을 알려 주는 신호가 아니라 시장이 두 요소를 어떤 비중으로 읽는지 확인하는 재료입니다.</p>

<ul style="line-height:1.9;">
  <li>광고 경로: 노출과 단가가 함께 오르면 광고주의 지출이 이어진다는 신호로 읽혀, 다른 플랫폼 기업의 광고 매출 기대에도 번질 수 있습니다.</li>
  <li>비용 경로: 설비투자가 매출의 절반을 넘으면 이익이 늘어도 현금이 남지 않는다는 점이 부담 요인으로 거론됩니다.</li>
  <li>일회성 경로: 충당금처럼 한 번 잡히는 비용은 시장이 걸러서 보는 경우가 많아, 공시값과 제외값을 함께 봐야 합니다.</li>
</ul>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 한국 시간으로 보면</strong>
  <p style="margin:8px 0 0 0;">발표는 2026년 10월 21일 미국 장 마감 후였고, 콘퍼런스콜은 동부 오후 4시 30분이라 한국시간 10월 22일 새벽 5시 30분이었습니다. 11월 1일 서머타임이 끝나면 같은 미국 시각이 한국 기준 1시간 늦어집니다. 다른 미국 기업의 실적 일정은 <a href="https://sensitiveboss3.tistory.com/entry/nvidia-earnings-date-korea-time" target="_blank" rel="noopener">엔비디아 실적발표 일정과 한국시간 계산</a> 글에서 같은 방식으로 환산했습니다.</p>
</div>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #e11d48;padding-left:12px;margin-top:36px;">발표 다음 날 아침에 나오는 질문들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">메타 3분기 실적은 언제 발표됐나요?</summary>
  <p style="margin:10px 0 0 0;">2026년 10월 21일 미국 장 마감 후에 발표됐습니다. 한국시간으로는 10월 22일 새벽이었고, 일부 일정 사이트에 있던 10월 28일은 공지 전 추정치였습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">3분기 매출과 EPS는 얼마였나요?</summary>
  <p style="margin:10px 0 0 0;">매출은 약 646억 달러로 전년 대비 26% 늘었고, 희석 EPS는 3.83달러였습니다. 합의금 충당금 9.89십억 달러를 제외하면 7.40달러라고 회사가 설명했습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">영업이익이 37% 줄어든 이유는 무엇인가요?</summary>
  <p style="margin:10px 0 0 0;">8월에 합의한 청소년 정신건강 소송 비용 98억 9천만 달러가 3분기 비용으로 잡혔기 때문입니다. 이 충당금을 더하면 영업이익은 22.88십억 달러로 계산됩니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">클래스C 주식은 언제 받나요?</summary>
  <p style="margin:10px 0 0 0;">기준일과 지급일은 아직 정해지지 않았습니다. 개정 정관 효력일이 2027년 1월 19일이고, 지급일은 그 뒤 5영업일 이내로 정해져 있습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">실적이 좋으면 주가도 오르나요?</summary>
  <p style="margin:10px 0 0 0;">단정할 수 없습니다. 주가는 숫자 자체보다 시장이 미리 예상한 값과의 차이, 설비투자 같은 비용 전망에 함께 반응해서 매출이 예상을 넘어도 움직임이 엇갈릴 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-to-Announce-Third-Quarter-2026-Results/default.aspx" target="_blank" rel="noopener">Meta Investor Relations - Meta to Announce Third Quarter 2026 Results</a></li>
    <li><a href="https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066700/meta-20261019.htm" target="_blank" rel="noopener">SEC - Meta 8-K(2026-10-19, 클래스C 주식배당)</a></li>
    <li><a href="https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066773/meta-20260930.htm" target="_blank" rel="noopener">SEC - Meta 10-Q(2026-09-30 분기)</a></li>
    <li><a href="https://www.specialtimes.co.kr/news/articleView.html?idxno=476992" target="_blank" rel="noopener">스페셜타임스 - 메타 3분기 매출 26% 증가</a></li>
    <li><a href="https://au.variety.com/2026/biz/news/meta-q3-earnings-2026-41733/" target="_blank" rel="noopener">Variety - Meta's Almost $10 Billion Legal Costs Take Huge Toll on Q3 Earnings</a></li>
    <li><a href="https://ppc.land/meta-takes-9-89bn-teen-settlement-charge-as-ad-revenue-gains-26/" target="_blank" rel="noopener">PPC Land - Meta takes $9.89bn teen settlement charge as ad revenue gains 26%</a></li>
    <li><a href="https://siliconangle.com/2026/10/21/meta-beats-on-revenue-and-splits-its-stock-two-for-one-with-non-voting-class-c-shares/" target="_blank" rel="noopener">SiliconANGLE - Meta beats on revenue and splits its stock two-for-one with non-voting Class C shares</a></li>
  </ul>
  기준일: 2026년 10월 24일. 메타 IR과 SEC 원문은 이 환경에서 직접 열람하지 못해 언론 보도를 교차 대조했고, 영업이익률·충당금 합산·증가율은 위 숫자로 직접 계산한 값입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 실적 공시 숫자를 읽는 방법을 정리한 정보 글로, 특정 종목의 매수·매도를 권하거나 주가 방향을 예측하지 않습니다. 투자 판단과 그 결과의 책임은 투자자 본인에게 있고, 수치와 일정은 정정·변경될 수 있어 공시 원문과 대조가 필요합니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "메타 실적발표 3분기, 합의금 반영 전후 비교",
  "description": "메타 2026년 3분기 실적의 공시값과 합의금 충당금 제외값 비교, 광고 노출·단가 분해, 설비투자와 잉여현금흐름 계산, 클래스C 주식배당 일정을 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/meta-q3-2026-earnings-settlement-1.png",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-24",
  "dateModified": "2026-10-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/meta-q3-2026-earnings-settlement"
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
      "name": "메타 3분기 실적은 언제 발표됐나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "2026년 10월 21일 미국 장 마감 후에 발표됐습니다. 한국시간으로는 10월 22일 새벽이었고, 일부 일정 사이트에 있던 10월 28일은 공지 전 추정치였습니다."
      }
    },
    {
      "@type": "Question",
      "name": "3분기 매출과 EPS는 얼마였나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "매출은 약 646억 달러로 전년 대비 26% 늘었고, 희석 EPS는 3.83달러였습니다. 합의금 충당금 9.89십억 달러를 제외하면 7.40달러라고 회사가 설명했습니다."
      }
    },
    {
      "@type": "Question",
      "name": "영업이익이 37% 줄어든 이유는 무엇인가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "8월에 합의한 청소년 정신건강 소송 비용 98억 9천만 달러가 3분기 비용으로 잡혔기 때문입니다. 이 충당금을 더하면 영업이익은 22.88십억 달러로 계산됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "클래스C 주식은 언제 받나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "기준일과 지급일은 아직 정해지지 않았습니다. 개정 정관 효력일이 2027년 1월 19일이고, 지급일은 그 뒤 5영업일 이내로 정해져 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "실적이 좋으면 주가도 오르나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "단정할 수 없습니다. 주가는 숫자 자체보다 시장이 미리 예상한 값과의 차이, 설비투자 같은 비용 전망에 함께 반응해서 매출이 예상을 넘어도 움직임이 엇갈릴 수 있습니다."
      }
    }
  ]
}
</script>
