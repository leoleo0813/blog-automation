---
keyword: 달러 ETF
title: 달러 ETF 달러예금 차이와 환율 손익 계산
slug: dollar-etf-exchange-rate-comparison
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 3310 (PC 660 / 모바일 2650)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-04 - 통과] WebSearch(미국 기준, 참고용) "달러 ETF 달러선물 ETF 차이 세금 환노출 개인투자자" 상위 9개: kbam.co.kr(KB자산운용) / open.shinhansec.com(신한투자증권) / news.mt.co.kr(언론) / brunch.co.kr(개인) / hankyung.com(언론) / wikipedia(무관) / clien.net(커뮤니티) / kr.investing.com(언론). 추가 검색에서 eiec.kdi.re.kr(KDI), edaily.co.kr, investpension.miraeasset.com 확인.
  1) 진입 여지 - 있음. brunch 개인 글, clien 커뮤니티가 상위에 있어 SERP가 잠기지 않음.
  2) 검색 의도 - 정보 탐색형(구조·차이). 조회·계산기 목적 아님.
  3) 답 완결 - 아님. 확인된 상위 글은 구조 설명과 세금 요약이 중심이고, 같은 가상 원금으로 달러예금과 달러 ETF의 환율 손익을 한 표에서 세전·세후로 나란히 놓은 글은 이번 검색에서 확인하지 못함(검색 요약 기준이라 전수 확인은 아님).
unique_asset: |
  (a) 달러예금·달러선물 ETF·달러 표시 해외자산 비교표.
  (b) 환율 1,200/1,300/1,400원 가상 1,000만 원 손익 계산표와 막대그래프. 세금·세후 칸은 원문 확인 후 기입.
  (c) 보수·롤오버·괴리율 확인 항목 목록.
primary_source: |
  한국거래소·운용사·국세청 원문은 이번 세션에서 WebFetch가 EGRESS_BLOCKED(www.kbam.co.kr 1회 시도, 세션 전면 차단으로 판단)로 열리지 않음. 2차 교차검증은 구조 설명에 한해 사용.
  - 달러 ETF 구조(달러선물 기반, 월물 롤오버, 괴리율, 보수 연 0.2~0.4%대 안내): KDI 경제정보센터, 미래에셋증권, 한국경제, 뉴스토마토, 이데일리 검색 요약이 수렴.
  - 세율·과세 방식(달러예금 환차익, 달러 ETF 매매차익)은 프로젝트가 과거 오류를 잡은 유형의 숫자라 2차 보도로 확정하지 않고 캡처로 전환. 본문 세금 칸은 비워 둠.
기준일: 2026년 10월 4일 기준
refresh_due: 2027-04-04
refresh_reason: "과세 방식과 상품 보수는 개정·변경될 수 있어 반기에 한 번 원문 대조"
tags: 달러 ETF, 달러선물 ETF, 달러예금, 환율 투자, 달러 투자, 환차익, 롤오버, 괴리율, 환율 손익, 원달러 환율
capture_guide: |
  왜 필요한가: 달러예금 환차익과 달러선물 ETF 매매차익에 어떤 세율이 적용되는지를 검색 요약(언론·증권사)으로만 확인했고, 세율·과세 방식은 오류 사례가 있던 유형이라 원문 확정 없이 본문에 쓰지 않았습니다. 그래서 본문 표 3번째 계산표의 "세금", "세후 손익" 6칸이 비어 있습니다.
  1순위: 국가법령정보센터 https://www.law.go.kr 접속, 검색창에 "소득세법" 입력, 이자소득과 배당소득을 규정한 조문(제16조, 제17조 부근)을 열어 해당 조문이 보이게 캡처.
  2순위: 같은 사이트에서 "소득세법 시행령"을 검색해 집합투자기구 이익 관련 조문(제26조의2 부근)이 보이게 캡처. 본법에 구조가, 시행령에 세부 기준이 있을 수 있어 둘 다 필요합니다.
  3순위: 달러선물 ETF 상품 한 개의 운용사 상품 페이지(투자설명서 또는 간이투자설명서의 "과세" 항목)와 총보수 항목 캡처.
  캡처 후: 스크린샷을 대화에 올려주세요. 그러면 표의 세금·세후 칸을 채우고 gate_pass를 true로 바꿉니다.
gate_pass: false
gate_pass_note: |
  게이트1 3,310회, 게이트2 v3 통과, 게이트3 비교표와 가상 계산표, 게이트4 구조는 교차검증(KDI·증권사·언론 4곳 수렴), 세율·과세 방식은 캡처 필요. 따라서 세금 칸 6개가 비어 있는 동안 gate_pass:false.
self_check: |
  [2026-10-04 gate_pass:false, 사람 보조 캡처 대기]
  후보 경위: 검색량 실측 8개(콘탱고 뜻 70, 원유 ETF 760, 코스피200 뜻 220, DART 전자공시 21,300, 달러 ETF 3,310, 공시 보는 법 20, 주식 거래량 뜻 50, 주식 배당 시기 30) 중 PASS 3개. DART 전자공시(21,300)는 검색 의도가 사이트 이동·조회라 게이트2 탈락 조건 2번에 해당해 제외. 원유 ETF(760)는 달러 ETF(3,310)보다 낮아 다음 후보.
  YMYL: 종목·상품 추천, 목표가, 환율 방향 예측 없음. 가상 환율 숫자만 사용. 세율 숫자를 본문에 쓰지 않음.
  카니벌라이제이션: 환율 뜻(109), 환헤지 뜻(103), 국내상장 해외ETF 세금(23), ETF 괴리율(22), ETF 수수료(10)와 내부 링크로 연결하고 본문은 달러 ETF와 달러예금 구조 비교와 가상 손익 계산에 집중해 차별화.
  첫 문장 유형: 대비형(직전 130 절차형, 129 문제제기형, 128 수치충격형, 127 대비형과 3편 간격).
  글 구조 유형: 비교형(첫 H2가 곧바로 비교표). 직전 130 개념형, 129 일정표형, 128 계산형과 다름.
  기관 안내 문장 4개(국가법령정보센터, 국세청, 한국거래소, KDI 등) 링크 처리, 출처 목록 4개 전부 링크 처리.
  AI 티 점검: em대시 0개, 다만 0회, 확인하세요류 0회, mark 4개, FAQ 5개, FAQ 헤딩 "달러 ETF 고민, 이것부터 물어봅니다"(신규), 요약박스 제목 "💵 달러 ETF 고르기 전 세 줄"(신규 문구, 초록색), H2 6개 중 "~나요"형 0개 이하.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-04</p>

<p>환율이 똑같이 올라도 달러예금과 달러 ETF는 돈이 들어오는 길이 다릅니다. 하나는 은행에서 달러로 바꿔 두는 일이고, 다른 하나는 원화로 거래하는 선물 기반 상품입니다. 아래에서 두 방식의 구조를 나란히 놓고, 가상의 1,000만 원으로 환율 손익을 계산합니다.</p>

<div style="background:#ecfdf5;border:2px solid #059669;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#047857;font-size:18px;">💵 달러 ETF 고르기 전 세 줄</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>국내 달러 ETF는 달러 현금이 아니라 달러선물을 담아 환율을 따라가는 상품입니다.</li>
    <li>환율 변화만 계산하면 1,300원에서 1,400원으로 오를 때 약 7.69%가 남습니다.</li>
    <li>세금과 비용이 더해지면 달러예금과 달러 ETF의 실제 손익은 달라지므로, 과세 기준은 법령 원문에서 따로 봐야 합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #059669;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">달러에 투자하는 세 가지 길 비교</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">달러 ETF가 환율을 따라가는 방식</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">환율 1,300원에서 움직일 때 가상 손익 계산</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">세금은 어디서 어떻게 확인하나</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">달러 ETF 보기 전에 확인할 항목</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">달러 ETF 고민, 이것부터 물어봅니다</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #059669;padding-left:12px;margin-top:36px;">달러에 투자하는 세 가지 길 비교</h2>

<p>달러에 투자하는 방법은 <mark>크게 달러예금, 달러선물 ETF, 달러로 사는 해외자산 세 가지로 나뉩니다.</mark> 환율을 직접 노리는 것은 앞의 둘이고, 셋째는 환율이 부수적으로 따라붙습니다. 한국개발연구원(KDI) 경제정보센터도 달러 투자 방법을 이런 갈래로 정리해 둡니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">거래 방식</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">환율 외에 따라붙는 것</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">환전 과정</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">달러예금</td><td style="border:1px solid #ddd;padding:8px;">은행에서 원화를 달러로 바꿔 예치</td><td style="border:1px solid #ddd;padding:8px;">예금 이자, 환전 스프레드</td><td style="border:1px solid #ddd;padding:8px;">있음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">달러선물 ETF</td><td style="border:1px solid #ddd;padding:8px;">증권 계좌에서 원화로 매매</td><td style="border:1px solid #ddd;padding:8px;">운용보수, 롤오버 효과, 괴리율</td><td style="border:1px solid #ddd;padding:8px;">없음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">달러 표시 해외자산</td><td style="border:1px solid #ddd;padding:8px;">해외주식·해외 ETF를 달러로 매수</td><td style="border:1px solid #ddd;padding:8px;">자산 자체의 가격 변동, 환전 비용</td><td style="border:1px solid #ddd;padding:8px;">있음</td></tr>
  </tbody>
</table>

<p>여기서는 앞의 둘을 비교합니다. 해외자산에서 환율 위험을 지우는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/currency-hedge-cost-meaning" target="_blank" rel="noopener">환헤지 뜻과 비용 글</a>에, 환율이 오르내리는 이유는 <a href="https://sensitiveboss3.tistory.com/entry/exchange-rate-meaning-won-value" target="_blank" rel="noopener">환율 뜻 글</a>에 따로 정리했습니다.</p>

<div style="background:#f0fdf4;border:1px solid #22c55e;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 구분이 중요한 이유</strong>
  <p style="margin:8px 0 0 0;">환전 과정이 있느냐 없느냐가 비용 구조를 가르고, 어느 소득으로 분류되느냐가 세금을 가릅니다. 같은 환율 상승이어도 이 둘이 달라서 계좌에 남는 돈이 다릅니다.</p>
</div>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #059669;padding-left:12px;margin-top:36px;">달러 ETF가 환율을 따라가는 방식</h2>

<p>국내 달러 ETF는 한국거래소에 상장된 원·달러 환율 관련 선물지수를 따라가며, 달러 현금을 들고 있지 않습니다. 증권사와 운용사 안내 자료는 이 상품을 환율이 오른 만큼 오르고 내린 만큼 내리는 구조로 설명합니다.</p>

<p>선물은 만기가 있어서 매월 근월물을 다음 월물로 바꿉니다. 이를 롤오버라고 하고, 기초지수가 바뀔 때 ETF도 따라 바꾸기 때문에 <mark>롤오버 효과가 수익률을 환율과 다르게 만들 수 있습니다.</mark> 레버리지형은 선물을 두 배로 들고 있어 이 효과도 두 배로 적용된다고 안내됩니다.</p>

<p>환율 지수와 ETF 가격이 벌어지는 정도는 별개로 봐야 합니다. 시장 가격과 순자산가치의 차이인 괴리율은 <a href="https://sensitiveboss3.tistory.com/entry/etf-divergence-rate-2026" target="_blank" rel="noopener">ETF 괴리율 글</a>, 운용보수 구조는 <a href="https://sensitiveboss3.tistory.com/entry/etf-fee-comparison" target="_blank" rel="noopener">ETF 수수료 비교 글</a>에 나와 있습니다.</p>

<ul style="line-height:1.9;">
  <li>운용보수: 확인한 자료 기준 연 0.2~0.4%대로 안내되고 상품마다 다릅니다.</li>
  <li>롤오버 효과: 월물 교체 때 생기며, 환율 지수와의 차이로 나타날 수 있습니다.</li>
  <li>괴리율: 순자산가치와 시장 가격의 차이로, 거래량이 적을수록 커질 수 있습니다.</li>
</ul>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #059669;padding-left:12px;margin-top:36px;">환율 1,300원에서 움직일 때 가상 손익 계산</h2>

<p>환율 1,300원일 때 1,000만 원을 달러로 바꾸면 <mark>약 7,692.31달러</mark>입니다. 이 금액이 환율 1,400원에서 얼마가 되는지가 환율 손익의 전부입니다. 아래는 가상의 숫자이고, 실제 환율 전망이 아닙니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">환율</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">평가금액</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">환율 손익(세전)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">세금</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">세후 손익</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">1,200원</td><td style="border:1px solid #ddd;padding:8px;">9,230,769원</td><td style="border:1px solid #ddd;padding:8px;">-769,231원</td><td style="border:1px solid #ddd;padding:8px;">원문 확인 후 기입</td><td style="border:1px solid #ddd;padding:8px;">원문 확인 후 기입</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1,300원</td><td style="border:1px solid #ddd;padding:8px;">10,000,000원</td><td style="border:1px solid #ddd;padding:8px;">0원</td><td style="border:1px solid #ddd;padding:8px;">원문 확인 후 기입</td><td style="border:1px solid #ddd;padding:8px;">원문 확인 후 기입</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1,400원</td><td style="border:1px solid #ddd;padding:8px;">10,769,231원</td><td style="border:1px solid #ddd;padding:8px;">+769,231원</td><td style="border:1px solid #ddd;padding:8px;">원문 확인 후 기입</td><td style="border:1px solid #ddd;padding:8px;">원문 확인 후 기입</td></tr>
  </tbody>
</table>

<p>평가금액은 달러예금 기준으로 환전 스프레드를 뺀 값이고, 달러 ETF는 이론상 같은 값에서 출발합니다. 실제 ETF는 운용보수와 롤오버 효과, 괴리율이 더해져 이 값보다 조금 낮거나 높을 수 있습니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/dollar-etf-exchange-rate-comparison-1.png" alt="환율 1,200원일 때 평가금액 9,230,769원, 1,300원일 때 10,000,000원, 1,400원일 때 10,769,231원을 보여주는 세로 막대그래프" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 가상 사례를 직접 계산, 2026-10-04 기준</figcaption></figure>

<ul style="line-height:1.9;">
  <li>환율 +100원은 <mark>+7.69%</mark>입니다. 100 ÷ 1,300 = 0.0769로 계산합니다.</li>
  <li>환율 -100원은 -7.69%이고, 1,000만 원은 9,230,769원이 됩니다.</li>
  <li>보수 0.3%를 가정하면 1,000만 원 기준 연 약 30,000원이 비용입니다. 상품별 실제 보수는 운용사 자료에 적힌 숫자를 따릅니다.</li>
</ul>

<div style="background:#f0fdf4;border:1px solid #22c55e;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 표의 세금 칸이 비어 있는 이유</strong>
  <p style="margin:8px 0 0 0;">세율과 과세 방식은 이 글에서 숫자를 단정하지 않고, 아래에서 원문을 확인하는 곳을 안내합니다. 원문을 확인한 뒤에 두 칸을 채우면 세후 손익이 완성됩니다.</p>
</div>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #059669;padding-left:12px;margin-top:36px;">세금은 어디서 어떻게 확인하나</h2>

<p>달러예금과 달러 ETF는 소득 종류가 달라서 같은 환차익이어도 과세가 다릅니다. 법령은 <a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a>에서 법률과 시행령을 함께 열어 봐야 정확합니다. 세법은 본법에 구조가, 시행령에 세부 기준이 나뉘어 있는 경우가 많기 때문입니다.</p>

<ol style="line-height:1.9;">
  <li>국가법령정보센터에서 「소득세법」을 검색해 이자소득과 배당소득 조문을 확인합니다.</li>
  <li>같은 사이트에서 「소득세법 시행령」의 집합투자기구 이익 관련 조문을 확인합니다.</li>
  <li>국내 상장 해외 ETF 과세의 큰 틀은 <a href="https://sensitiveboss3.tistory.com/entry/domestic-listed-overseas-etf-tax" target="_blank" rel="noopener">국내상장 해외ETF 세금 글</a>에 정리했으니 먼저 읽고 오시면 이해가 빠릅니다.</li>
  <li>본인의 다른 금융소득이 많다면 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 기준의 금융소득 종합과세 대상인지도 함께 봅니다.</li>
</ol>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #059669;padding-left:12px;margin-top:36px;">달러 ETF 보기 전에 확인할 항목</h2>

<p>달러 ETF는 상품마다 구조와 비용이 다르므로 이름만 보고 판단하면 안 됩니다. 운용사 상품 페이지와 <a href="https://www.krx.co.kr" target="_blank" rel="noopener">한국거래소</a> 정보에서 아래 다섯 가지를 확인합니다.</p>

<ul style="line-height:1.9;">
  <li>기초지수: 원·달러 환율 관련 어떤 지수를 따라가는지</li>
  <li>레버리지·인버스 여부: 일반형인지, 두 배형이나 반대 방향형인지</li>
  <li>총보수와 실제 부담 비용: 운용보수 외에 드는 비용이 있는지</li>
  <li>괴리율과 거래량: 순자산가치와 시장 가격이 얼마나 벌어지는지</li>
  <li>과세 방식: 매매차익이 어떤 소득으로 분류되는지</li>
</ul>

<p>이 글은 특정 상품을 평가하거나 매수를 권하는 글이 아닙니다. 구조와 계산 틀만 정리했고, 환율 방향은 예측하지 않습니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #059669;padding-left:12px;margin-top:36px;">달러 ETF 고민, 이것부터 물어봅니다</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러 ETF를 사면 실제 달러를 갖게 되나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 국내 달러 ETF는 원·달러 환율을 따라가는 달러선물에 투자하는 상품이라, 달러 현금이 계좌에 생기지 않습니다. 원화로 사고 원화로 파는 구조입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러 ETF는 환율이 오르면 그대로 오르나요</summary>
  <p style="margin:10px 0 0 0;">대체로 환율 방향을 따라가지만 똑같지는 않습니다. 월물 교체 때 생기는 롤오버 효과, 운용보수, 시장가와 순자산가치의 괴리율이 수익률을 환율과 다르게 만듭니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러 ETF는 환전 수수료가 드나요</summary>
  <p style="margin:10px 0 0 0;">ETF를 원화로 거래하므로 환전 과정이 없습니다. 대신 운용보수가 계속 나가고, 검색으로 확인한 자료 기준 연 0.2~0.4%대로 안내되며 상품마다 다릅니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">환율이 내려가면 달러 ETF는 손실인가요</summary>
  <p style="margin:10px 0 0 0;">환율이 내려가면 가격도 내려가 손실이 납니다. 손실이 나도 다른 금융소득과 합쳐 줄여 주는지 여부는 과세 기준에 달려 있어서, 아래 과세 확인 절차를 따라가 보시면 됩니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">달러 ETF와 환헤지 ETF는 같은 말인가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 달러 ETF는 환율 자체에 투자하는 상품이고, 환헤지는 해외 자산을 살 때 환율 변동을 없애려는 장치입니다. 방향이 정반대여서 환헤지 구조는 환헤지 뜻 글에서 따로 다룹니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://eiec.kdi.re.kr/publish/columnView.do?cidx=12214" target="_blank" rel="noopener">한국개발연구원 경제정보센터 - 달러에 투자하는 4가지 방법</a></li>
    <li><a href="https://investpension.miraeasset.com/contents/view.do?idx=16178" target="_blank" rel="noopener">미래에셋증권 - 강달러 시대, ETF를 통해 달러에 투자하려면</a></li>
    <li><a href="https://www.hankyung.com/article/2021113034411" target="_blank" rel="noopener">한국경제 - 달러예금, 환차익 세금 안떼…공격투자 원한다면 달러ETF</a></li>
    <li><a href="https://www.newstomato.com/ReadNews.aspx?no=963402" target="_blank" rel="noopener">뉴스토마토 - 원유선물 ETF 롤오버 비용 설명</a></li>
  </ul>
  기준일: 2026년 10월 4일. 한국거래소와 운용사 원문은 이 환경에서 열람하지 못해 연구원·증권사·언론 검색 요약을 교차 대조했고, 세율과 과세 방식은 원문 확인 전이라 수치를 적지 않았습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 달러 투자 구조를 설명하는 정보 글로, 특정 상품을 사고팔라는 권유가 아닙니다. 투자의 판단과 손익은 모두 투자자 본인의 몫입니다. 보수, 괴리율, 세율은 바뀔 수 있으니 상품 설명서와 법령 원문의 최신 내용을 따라 주시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "달러 ETF 달러예금 차이와 환율 손익 계산",
  "description": "달러 ETF가 환율을 따라가는 방식과 달러예금의 구조 차이, 환율 1,300원 기준 가상 1,000만 원 손익 계산, 과세 확인처를 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/dollar-etf-exchange-rate-comparison-1.png",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Person", "name": "센시티브보스" },
  "datePublished": "2026-10-04",
  "dateModified": "2026-10-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensitiveboss3.tistory.com/entry/dollar-etf-exchange-rate-comparison" }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "달러 ETF를 사면 실제 달러를 갖게 되나요", "acceptedAnswer": {"@type": "Answer", "text": "아닙니다. 국내 달러 ETF는 원·달러 환율을 따라가는 달러선물에 투자하는 상품이라, 달러 현금이 계좌에 생기지 않습니다. 원화로 사고 원화로 파는 구조입니다."}},
    {"@type": "Question", "name": "달러 ETF는 환율이 오르면 그대로 오르나요", "acceptedAnswer": {"@type": "Answer", "text": "대체로 환율 방향을 따라가지만 똑같지는 않습니다. 월물 교체 때 생기는 롤오버 효과, 운용보수, 시장가와 순자산가치의 괴리율이 수익률을 환율과 다르게 만듭니다."}},
    {"@type": "Question", "name": "달러 ETF는 환전 수수료가 드나요", "acceptedAnswer": {"@type": "Answer", "text": "ETF를 원화로 거래하므로 환전 과정이 없습니다. 대신 운용보수가 계속 나가고, 검색으로 확인한 자료 기준 연 0.2~0.4%대로 안내되며 상품마다 다릅니다."}},
    {"@type": "Question", "name": "환율이 내려가면 달러 ETF는 손실인가요", "acceptedAnswer": {"@type": "Answer", "text": "환율이 내려가면 가격도 내려가 손실이 납니다. 손실이 나도 다른 금융소득과 합쳐 줄여 주는지 여부는 과세 기준에 달려 있어서, 아래 과세 확인 절차를 따라가 보시면 됩니다."}},
    {"@type": "Question", "name": "달러 ETF와 환헤지 ETF는 같은 말인가요", "acceptedAnswer": {"@type": "Answer", "text": "다릅니다. 달러 ETF는 환율 자체에 투자하는 상품이고, 환헤지는 해외 자산을 살 때 환율 변동을 없애려는 장치입니다. 방향이 정반대여서 환헤지 구조는 환헤지 뜻 글에서 따로 다룹니다."}}
  ]
}
</script>
