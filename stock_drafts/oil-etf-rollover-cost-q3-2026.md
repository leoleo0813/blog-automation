---
keyword: 원유 ETF
title: 원유 ETF 3분기 수익률과 롤오버 비용
slug: oil-etf-rollover-cost-q3-2026
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 760 (PC 250 / 모바일 510, 2026-10-04 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-04 - 통과] WebSearch(미국 기준, 참고용) "원유 ETF 롤오버 콘탱고 수익률 차이 WTI 선물 ETF 괴리" 상위 10개: munhwa.com(언론) / dealsite.co.kr(언론) / brunch.co.kr(개인) / straightnews.co.kr(언론) / hankyung.com(언론) / wikipedia(무관) / ebc.com(해외 브로커) / seekingalpha(해외). 보조 검색 "원유 ETF 롤오버 비용 콘탱고 백워데이션 개인투자자 ETF ETN 차이": v.daum.net(언론) / brunch.co.kr(개인) / postype.com(개인) / benzinga(해외).
  1) 진입 여지 - 있음. brunch 개인 글, postype 개인 글이 상위에 있어 SERP가 잠기지 않음.
  2) 검색 의도 - 정보 탐색형(롤오버·수익률 차이의 이유). 시세 조회나 계산기가 아님.
  3) 답 완결 - 아님. 확인된 상위 글은 뉴스 기사(수익률 순위)와 개념 설명(콘탱고 뜻)으로 갈라져 있고, 2026년 3분기 실제 수익률과 WTI 상승률의 차이, 월 롤오버율별 1년 환산 손익 계산을 한 글에서 같이 보여 주는 글은 이번 검색에서 확인하지 못함(검색 요약 기준이라 전수 확인은 아님).
  이슈 근거(주제 선정 v3 1순위 유형): 2026-10-04 한국경제 보도로 3분기 ETF 수익률 1위가 원유선물 ETF로 확정, 같은 날 뉴스1도 보도.
unique_asset: |
  (a) 2026년 3분기 WTI 상승률과 원유선물 ETF 수익률 대조표 및 5.12%p 차이 해석 틀.
  (b) 월 롤오버율(0.5%·1%·2% 콘탱고, 1% 백워데이션)별 1년 환산 손익 계산표와 막대그래프.
  (c) 환헤지 여부·롤오버 방식·ETF와 ETN 구조 차이 비교표, 사기 전 확인 항목.
primary_source: |
  한국거래소·운용사·DART 원문은 이번 세션에서 WebFetch가 EGRESS_BLOCKED(www.samsungfund.com 1회 시도)로 열리지 않음. 2차 교차검증으로 진행.
  - 3분기 수치(WTI 6월 말 69.50달러, 9월 말 90.42달러, +30.10%, KODEX WTI원유선물(H) 3분기 +35.22%, 국내 상장 ETF 1위): 한국경제(2026-10-04)와 뉴스1이 같은 수치로 수렴, 두 검색에서 반복 확인. 30.10%는 90.42÷69.50-1로 직접 검산해 일치.
  - 총보수 연 0.350%: KODEX 상품 페이지가 검색 요약에 노출된 값(원문 미열람).
  - 롤오버 구조(콘탱고·백워데이션 정의, ETF는 롤오버 비용이 순자산가치에 반영, ETN은 발행사 부담): 다음 뉴스 설명·파이낸셜뉴스·뉴스핌 등 3곳 이상이 일치. 상품별 롤오버 방식 차이는 2020년 뉴스핌 보도 기준이라 현재 운용 방식과 다를 수 있어 본문에 날짜를 밝히고 단정하지 않음.
  - 세율·과세 방식은 오류 이력 유형 숫자라 본문에 쓰지 않고 기존 세금 글로 연결.
기준일: 2026년 10월 4일 기준 (3분기 수치는 2026년 9월 30일 종가 기준)
refresh_due: 2026-11-04
refresh_reason: "3분기 이후 WTI와 ETF 수익률이 바뀌고, 상품 보수와 롤오버 방식은 운용사 공지로 바뀔 수 있어 한 달 뒤 최신 수치로 교체"
tags: 원유 ETF, 원유선물 ETF, WTI 원유선물, 롤오버, 콘탱고, 백워데이션, 환헤지 ETF, 원자재 ETF, ETF 수익률, 3분기 ETF
cannibalization_note: |
  레버리지·인버스 ETF 글은 예탁금 기준 중심, 괴리율 글과 수수료 글은 일반 ETF 구조 중심이라 원유 선물 롤오버와 3분기 수익률 해석을 다루는 이 글과 겹치지 않음(grep으로 원유·WTI 언급 확인: 달러 ETF 초안에 롤오버 한 줄 외 없음).
gate_pass: true
gate_pass_note: |
  게이트1 760회(기준 500 이상), 게이트2 v3 통과, 게이트3 대조표와 롤오버 계산표, 게이트4 언론 2곳 이상 동일 수치와 직접 검산으로 충족. 원문(DART·KRX·운용사) 미열람이라 사람이 발행 전 한국경제 기사(2026-10-04)와 KODEX 상품 페이지의 보수 한 줄만 대조하면 충분.
self_check: |
  [2026-10-04 gate_pass:true]
  후보 경위: 이슈 스캔(10/4 한국경제 3분기 ETF 1위 원유선물) 후 8개 실측(원유 ETF 760 PASS, 신용점수 올리는 법 970 PASS이나 주식 주제 아님, 나머지 6개 FAIL). 시의성 있는 원유 ETF 채택. 검색량이 더 큰 후보는 주식 주제가 아니라 제외.
  YMYL: 종목·상품 추천, 목표가, 유가 방향 예측 없음. 특정 상품은 3분기 사실 수치로만 언급. 제목·소제목에 전망·추천 없음.
  카니벌라이제이션: 레버리지·인버스 ETF, ETF 괴리율, ETF 수수료, 환헤지 글과 내부 링크로 연결하고 본문은 원유 선물 롤오버와 3분기 해석에 집중.
  첫 문장 유형: 수치충격형(직전 131 대비형, 130 절차형, 129 문제제기형, 128 수치충격형 이후 3편 간격).
  글 구조 유형: 이슈 해설형(결과 표 먼저, 원리와 계산은 뒤). 직전 131 비교형, 130 개념형, 129 일정표형과 다름.
  기관 안내 문장 3개(한국거래소, 금융투자협회, 국세청 계열 세금 글 안내 등) 링크 처리, 출처 목록 5개 전부 링크 처리.
  내부 링크: 괴리율, 수수료, 환헤지, 레버리지·인버스, 국내상장 해외ETF 세금, 소비자물가지수 6개 전부 발행 완료(published) 글.
  AI 티 점검: em대시 0개, 다만 0회, 확인하세요류 0회, mark 3개, FAQ 5개, FAQ 헤딩 "원유 ETF 앞에서 자주 막히는 질문"(신규), 요약박스 제목 "🛢️ 원유 ETF 읽기 전 핵심 세 가지"(신규 문구, 주황색), H2 7개 중 "~나요"형 2개.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-04</p>

<p>2026년 3분기에 WTI 유가가 30.10% 오르는 동안 KODEX WTI원유선물(H)은 35.22% 올라 국내 상장 ETF 수익률 1위를 기록했습니다. 원유 ETF는 유가 자체가 아니라 원유선물을 매달 갈아타는 상품이라서, 유가가 제자리여도 롤오버 때문에 수익이 깎일 수 있습니다.</p>

<div style="background:#fff7ed;border:2px solid #ea580c;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#c2410c;font-size:18px;">🛢️ 원유 ETF 읽기 전 핵심 세 가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>유가가 그대로여도 선물 가격이 월 1%씩 비싼 구조(콘탱고)면 1년 뒤 약 11.26%가 깎입니다.</li>
    <li>3분기에 ETF가 WTI보다 5.12%p 더 오른 이유는 상품 자료만으로 분해되지 않아, 롤오버·환헤지·보수를 따로 살펴야 합니다.</li>
    <li>KODEX WTI원유선물(H)의 총보수는 연 0.350%로 안내되며, 이 보수는 롤오버 비용과 별개로 나갑니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2026년 3분기 원유 ETF 수익률 대조표</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">롤오버 비용은 어떻게 생기나요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">월 1% 콘탱고가 1년 수익률을 깎는 계산</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">같은 원유 ETF도 성과가 갈리는 세 가지 조건</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">원유 ETF를 보기 전 점검 항목</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 유가가 중요한 이유</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">원유 ETF 앞에서 자주 막히는 질문</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">2026년 3분기 원유 ETF 수익률 대조표</h2>

<p>2026년 3분기(7월 1일~9월 30일) 국내 상장 ETF 수익률 1위는 KODEX WTI원유선물(H)의 <mark>35.22%</mark>였습니다. 같은 기간 WTI는 6월 말 배럴당 69.50달러에서 9월 말 90.42달러로 30.10% 올랐습니다. 한국경제(2026-10-04)와 뉴스1이 같은 수치를 보도했습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">수치</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">기준 시점</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">출처</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">WTI 6월 말</td><td style="border:1px solid #ddd;padding:8px;">배럴당 69.50달러</td><td style="border:1px solid #ddd;padding:8px;">2026-06-30</td><td style="border:1px solid #ddd;padding:8px;"><a href="https://www.hankyung.com/article/2026100426661" target="_blank" rel="noopener">한국경제</a></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">WTI 9월 말</td><td style="border:1px solid #ddd;padding:8px;">배럴당 90.42달러</td><td style="border:1px solid #ddd;padding:8px;">2026-09-30</td><td style="border:1px solid #ddd;padding:8px;"><a href="https://www.news1.kr/finance/general-stock/6309193" target="_blank" rel="noopener">뉴스1</a></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">WTI 3분기 상승률</td><td style="border:1px solid #ddd;padding:8px;">+30.10%</td><td style="border:1px solid #ddd;padding:8px;">3분기</td><td style="border:1px solid #ddd;padding:8px;">90.42 ÷ 69.50 - 1로 직접 검산</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">KODEX WTI원유선물(H) 수익률</td><td style="border:1px solid #ddd;padding:8px;">+35.22%</td><td style="border:1px solid #ddd;padding:8px;">3분기</td><td style="border:1px solid #ddd;padding:8px;"><a href="https://www.hankyung.com/article/2026100426661" target="_blank" rel="noopener">한국경제</a></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">차이</td><td style="border:1px solid #ddd;padding:8px;">+5.12%p</td><td style="border:1px solid #ddd;padding:8px;">3분기</td><td style="border:1px solid #ddd;padding:8px;">35.22 - 30.10으로 직접 계산</td></tr>
  </tbody>
</table>

<p>10월 현재 WTI 가격은 이 표에 넣지 않았습니다. 시세는 매일 바뀌어서 이 글은 분기 말 수치만 고정해 두고, 다음 갱신 때 새 분기 값으로 바꿉니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/oil-etf-rollover-cost-q3-2026-1.png" alt="유가가 제자리일 때 월 롤오버율에 따른 1년 손익을 보여주는 가로 막대그래프. 월 0.5% 콘탱고 -5.81%, 월 1% 콘탱고 -11.26%, 월 2% 콘탱고 -21.15%, 월 1% 백워데이션 +12.68%" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 직접 계산한 예시, 2026-10-04 기준</figcaption></figure>

<p>ETF가 WTI보다 5.12%p 더 오른 이유는 이 글이 쓰는 자료만으로 나눠 볼 수 없습니다. 후보는 세 가지로 좁혀집니다.</p>

<ul style="line-height:1.9;">
  <li>롤오버 수익: 선물 곡선이 백워데이션이면 갈아탈 때 오히려 이익이 납니다.</li>
  <li>환헤지(H): 이 상품은 환헤지형이라, 원·달러 환율이 내려간 분기에 환노출형이 겪는 환차손을 피하는 방향으로 작용합니다.</li>
  <li>측정 시점 차이: WTI는 뉴욕 종가, ETF는 한국 종가를 기준으로 삼는 하루 단위 차이가 쌓일 수 있습니다.</li>
</ul>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 숫자를 읽을 때</strong>
  <p style="margin:8px 0 0 0;">한 분기 수익률은 과거 기록이고 다음 분기의 방향을 알려 주지 않습니다. 이 글은 어느 상품이 좋은지가 아니라, 같은 유가 상승에서 수익률이 왜 서로 다를 수 있는지를 설명합니다.</p>
</div>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">롤오버 비용은 어떻게 생기나요</h2>

<p>롤오버는 만기가 다가온 선물을 팔고 다음 만기 선물을 사서 포지션을 이어 가는 일입니다. 원유선물 ETF는 현물 원유를 들고 있을 수 없어서 이 작업을 매달 반복합니다.</p>

<p>이때 근월물보다 차월물이 비싼 상태를 콘탱고, 반대로 차월물이 더 싼 상태를 백워데이션이라 부릅니다. <mark>콘탱고에서는 갈아탈 때마다 손실이, 백워데이션에서는 이익이 생깁니다.</mark></p>

<p>숫자로 보면 쉽습니다. 근월물이 80.00달러, 차월물이 80.80달러(1% 비쌈)일 때 ETF는 근월물을 팔고 같은 금액으로 차월물을 삽니다. 한 달 뒤 유가가 그대로면 그 차월물이 근월물이 되어 80.00달러로 내려와, 갈아탄 금액의 약 0.99%가 사라집니다.</p>

<ul style="line-height:1.9;">
  <li>콘탱고: 차월물이 비쌈, 갈아탈 때 계약 수가 줄고 유가가 그대로면 손실</li>
  <li>백워데이션: 차월물이 쌈, 갈아탈 때 계약 수가 늘고 유가가 그대로면 이익</li>
  <li>ETF에서는 이 비용이 순자산가치에 이미 반영되어 투자자가 간접 부담합니다. ETN은 롤오버 매매비용을 발행사가 부담한다고 설명됩니다(<a href="https://v.daum.net/v/j3i7r6FYi3" target="_blank" rel="noopener">다음 뉴스 설명</a>).</li>
</ul>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">월 1% 콘탱고가 1년 수익률을 깎는 계산</h2>

<p>유가가 1년 내내 그대로이고 매달 차월물이 1% 비싼 구조라면, 1,000만 원은 1년 뒤 <mark>8,874,492원</mark>이 됩니다. 계산식은 1,000만 원 × (1 ÷ 1.01)^12입니다. 가정한 숫자이고 실제 시장의 롤오버율이 아닙니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">월 롤오버율</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">3개월 손익</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">1년 손익</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">1,000만 원의 1년 뒤 값</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">콘탱고 0.5%</td><td style="border:1px solid #ddd;padding:8px;">-1.49%</td><td style="border:1px solid #ddd;padding:8px;">-5.81%</td><td style="border:1px solid #ddd;padding:8px;">약 9,419,000원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">콘탱고 1%</td><td style="border:1px solid #ddd;padding:8px;">-2.94%</td><td style="border:1px solid #ddd;padding:8px;">-11.26%</td><td style="border:1px solid #ddd;padding:8px;">8,874,492원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">콘탱고 2%</td><td style="border:1px solid #ddd;padding:8px;">-5.77%</td><td style="border:1px solid #ddd;padding:8px;">-21.15%</td><td style="border:1px solid #ddd;padding:8px;">약 7,885,000원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">백워데이션 1%</td><td style="border:1px solid #ddd;padding:8px;">+3.03%</td><td style="border:1px solid #ddd;padding:8px;">+12.68%</td><td style="border:1px solid #ddd;padding:8px;">11,268,250원</td></tr>
  </tbody>
</table>

<ul style="line-height:1.9;">
  <li>이 표는 유가, 환율, 보수, 괴리율이 모두 변하지 않는다고 놓고 롤오버만 계산한 값입니다.</li>
  <li>총보수 연 0.350%를 더하면 1,000만 원 기준 연 약 35,000원이 따로 빠집니다.</li>
  <li>실제 수익은 유가 변동, 롤오버, 환헤지 비용, 보수가 한꺼번에 반영된 결과입니다.</li>
</ul>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">같은 원유 ETF도 성과가 갈리는 세 가지 조건</h2>

<p>이름에 원유가 들어가도 상품마다 환율 처리, 롤오버 규칙, 상품 구조가 다릅니다. 아래 표는 비교의 기준일 뿐이고 상품 평가는 아닙니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">조건</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">종류</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">수익률에 미치는 영향</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">환율 처리</td><td style="border:1px solid #ddd;padding:8px;">환헤지(H) / 환노출</td><td style="border:1px solid #ddd;padding:8px;">환노출형은 유가와 원·달러 환율 두 가지를 함께 받음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">롤오버 규칙</td><td style="border:1px solid #ddd;padding:8px;">근월물→차월물 / 일부 월물 건너뛰기</td><td style="border:1px solid #ddd;padding:8px;">콘탱고가 클수록 규칙에 따른 비용 차이가 커짐</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">상품 구조</td><td style="border:1px solid #ddd;padding:8px;">ETF / ETN</td><td style="border:1px solid #ddd;padding:8px;">ETN은 발행사 신용 위험과 괴리율 위험이 따로 있음</td></tr>
  </tbody>
</table>

<p>롤오버 규칙의 차이는 2020년 뉴스핌 보도가 잘 보여 줍니다. 당시 KODEX는 근월물을 팔고 차근월물을 사는 방식이었고, TIGER 원유선물Enhanced(H)는 근월과 차월의 가격 차가 0.5% 미만이면 차월물로, 그 이상이면 12월물로 갈아타도록 설계됐다고 소개됐습니다(<a href="https://www.newspim.com/news/view/20200410001060" target="_blank" rel="noopener">뉴스핌, 2020-04-10</a>). 지금도 같은 규칙인지는 상품 설명서에서 따로 봐야 합니다.</p>

<p>환헤지 구조 자체는 <a href="https://sensitiveboss3.tistory.com/entry/currency-hedge-cost-meaning" target="_blank" rel="noopener">환헤지 뜻과 비용 글</a>에, 시장가와 순자산가치의 차이는 <a href="https://sensitiveboss3.tistory.com/entry/etf-divergence-rate-2026" target="_blank" rel="noopener">ETF 괴리율 글</a>에 정리했습니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">원유 ETF를 보기 전 점검 항목</h2>

<p>상품 이름보다 기초지수와 구조가 먼저입니다. 운용사 상품 페이지와 <a href="https://www.krx.co.kr" target="_blank" rel="noopener">한국거래소</a> 정보에서 아래 항목을 열어 보면 됩니다.</p>

<ol style="line-height:1.9;">
  <li>기초지수: WTI인지 브렌트인지, 어떤 월물을 담는지</li>
  <li>환헤지 여부: 상품명 뒤에 (H)가 붙었는지</li>
  <li>총보수: 운용보수 외에 드는 비용이 있는지, <a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시</a>의 보수 항목과 비교</li>
  <li>괴리율과 거래량: 시장가가 순자산가치에서 얼마나 벌어지는지</li>
  <li>레버리지·인버스 여부: 일반형인지 두 배형이나 반대 방향형인지</li>
</ol>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 보수와 롤오버는 따로 봅니다</strong>
  <p style="margin:8px 0 0 0;">총보수는 상품 페이지에 숫자로 나오지만, 롤오버 비용은 숫자로 안내되지 않고 수익률에 섞여 나옵니다. 보수가 낮아도 콘탱고가 크면 성과는 낮아질 수 있습니다.</p>
</div>

<p>레버리지·인버스 원유 상품은 구조와 예탁금 조건이 달라서 <a href="https://sensitiveboss3.tistory.com/entry/leveraged-inverse-etf-deposit" target="_blank" rel="noopener">곱버스 뜻과 레버리지 예탁금 글</a>에서 따로 다뤘습니다. 매매차익에 붙는 세금 구조는 <a href="https://sensitiveboss3.tistory.com/entry/domestic-listed-overseas-etf-tax" target="_blank" rel="noopener">국내상장 해외ETF 세금 글</a>을 먼저 읽어 보시면 됩니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">주식 투자자에게 유가가 중요한 이유</h2>

<p>유가는 에너지 비용을 통해 물가에 번지고, 물가는 금리 기대를 거쳐 주식 가격에 영향을 줍니다. 시장은 보통 유가 상승을 물가 부담으로 받아들여 금리 인하가 늦어질 수 있다고 계산합니다.</p>

<ul style="line-height:1.9;">
  <li>경로 1: 유가 상승 → 휘발유·운송비 상승 → 소비자물가 상승 압력</li>
  <li>경로 2: 물가 압력 → 금리 인하 지연 기대 → 먼 미래 이익 비중이 큰 성장주의 할인율 부담</li>
  <li>경로 3: 연료 비중이 큰 항공·운송 업종은 비용이 늘고, 원유를 생산하거나 정제하는 업종은 매출 단가가 오르는 방향으로 영향이 갈림</li>
</ul>

<p>이 경로가 항상 같은 크기로 작동하지는 않습니다. 같은 유가 상승이어도 원인이 수요 증가인지 공급 차질인지에 따라 업종별 영향이 달라집니다. 물가 지표를 읽는 법은 <a href="https://sensitiveboss3.tistory.com/entry/consumer-price-index-calculation-guide" target="_blank" rel="noopener">소비자물가지수 계산 방법과 보는 순서 글</a>에서 이어서 볼 수 있습니다.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #ea580c;padding-left:12px;margin-top:36px;">원유 ETF 앞에서 자주 막히는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">원유 ETF는 유가를 그대로 따라가나요</summary>
  <p style="margin:10px 0 0 0;">그대로 따라가지 않습니다. 원유 ETF는 원유선물을 매달 갈아타며 담고, 롤오버 효과와 보수, 환율 처리 방식이 수익률을 유가와 다르게 만듭니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">3분기에 ETF가 WTI보다 더 오른 이유는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">WTI는 30.10% 올랐고 KODEX WTI원유선물(H)은 35.22% 올라 차이는 5.12%p입니다. 이 차이를 나눈 공시 자료는 확인하지 못했고, 롤오버 수익과 환헤지 효과, 측정 시점 차이가 후보입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">콘탱고일 때 원유 ETF는 반드시 손해인가요</summary>
  <p style="margin:10px 0 0 0;">반드시는 아닙니다. 콘탱고는 롤오버 때 손실 요인이 되지만, 유가 자체가 그보다 크게 오르면 전체 수익률은 플러스가 될 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상품명 뒤의 (H)는 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">(H)는 환헤지형이라는 표시입니다. 원·달러 환율 변동의 영향을 줄이도록 설계되어, 환율이 내려간 분기에 환노출형보다 유리한 쪽으로 작용할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">원유 ETF와 원유 ETN은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">ETF는 운용사가 선물을 직접 담는 펀드이고, ETN은 증권사가 지표 수익률을 지급하겠다고 약속한 증권입니다. 그래서 ETN에는 발행사 신용 위험과 괴리율 위험이 따로 붙습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.hankyung.com/article/2026100426661" target="_blank" rel="noopener">한국경제 - 국제유가 급등 효과…원유 ETF, 수익률 1위 (2026-10-04)</a></li>
    <li><a href="https://www.news1.kr/finance/general-stock/6309193" target="_blank" rel="noopener">뉴스1 - 3분기 ETF 왕좌는 원유 선물…환율 급락에 달러 인버스도 '방긋'</a></li>
    <li><a href="https://www.newspim.com/news/view/20200410001060" target="_blank" rel="noopener">뉴스핌 - 유가 급등락에 희비 엇갈린 KODEX·TIGER 원유ETF (2020-04-10)</a></li>
    <li><a href="https://v.daum.net/v/j3i7r6FYi3" target="_blank" rel="noopener">다음 뉴스 - 롤오버? 콘탱고?..ETN 투자, 이것만은 알고 하자</a></li>
    <li><a href="http://asis-www.kodex.com/product_view.do?fId=2ETF72" target="_blank" rel="noopener">KODEX - KODEX WTI원유선물(H) 상품 상세정보</a></li>
  </ul>
  기준일: 2026년 10월 4일(3분기 수치는 9월 30일 기준). 한국거래소와 운용사 원문은 이 환경에서 열람하지 못해 언론 보도와 상품 페이지 검색 요약을 교차 대조했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 원유 ETF의 구조와 3분기 수치를 설명하는 정보 글이며, 특정 상품의 매수나 매도를 권하지 않습니다. 투자 결정과 손익은 투자자 본인이 책임집니다. 보수와 롤오버 규칙, 세율은 바뀔 수 있으니 상품 설명서와 법령의 최신 내용을 따라 주시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "원유 ETF 3분기 수익률과 롤오버 비용",
  "description": "2026년 3분기 WTI 상승률 30.10%와 KODEX WTI원유선물(H) 35.22%의 차이, 콘탱고·백워데이션 롤오버 구조, 월 1% 콘탱고의 1년 환산 손익 계산을 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/oil-etf-rollover-cost-q3-2026-1.png",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Person", "name": "센시티브보스" },
  "datePublished": "2026-10-04",
  "dateModified": "2026-10-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensitiveboss3.tistory.com/entry/oil-etf-rollover-cost-q3-2026" }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "원유 ETF는 유가를 그대로 따라가나요", "acceptedAnswer": {"@type": "Answer", "text": "그대로 따라가지 않습니다. 원유 ETF는 원유선물을 매달 갈아타며 담고, 롤오버 효과와 보수, 환율 처리 방식이 수익률을 유가와 다르게 만듭니다."}},
    {"@type": "Question", "name": "3분기에 ETF가 WTI보다 더 오른 이유는 무엇인가요", "acceptedAnswer": {"@type": "Answer", "text": "WTI는 30.10% 올랐고 KODEX WTI원유선물(H)은 35.22% 올라 차이는 5.12%p입니다. 이 차이를 나눈 공시 자료는 확인하지 못했고, 롤오버 수익과 환헤지 효과, 측정 시점 차이가 후보입니다."}},
    {"@type": "Question", "name": "콘탱고일 때 원유 ETF는 반드시 손해인가요", "acceptedAnswer": {"@type": "Answer", "text": "반드시는 아닙니다. 콘탱고는 롤오버 때 손실 요인이 되지만, 유가 자체가 그보다 크게 오르면 전체 수익률은 플러스가 될 수 있습니다."}},
    {"@type": "Question", "name": "상품명 뒤의 (H)는 무슨 뜻인가요", "acceptedAnswer": {"@type": "Answer", "text": "(H)는 환헤지형이라는 표시입니다. 원·달러 환율 변동의 영향을 줄이도록 설계되어, 환율이 내려간 분기에 환노출형보다 유리한 쪽으로 작용할 수 있습니다."}},
    {"@type": "Question", "name": "원유 ETF와 원유 ETN은 어떻게 다른가요", "acceptedAnswer": {"@type": "Answer", "text": "ETF는 운용사가 선물을 직접 담는 펀드이고, ETN은 증권사가 지표 수익률을 지급하겠다고 약속한 증권입니다. 그래서 ETN에는 발행사 신용 위험과 괴리율 위험이 따로 붙습니다."}}
  ]
}
</script>
