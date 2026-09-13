---
keyword: ETF 괴리율
title: ETF 괴리율 계산법 관리기준 2026
slug: etf-divergence-rate-2026
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 850 (PC 320 / 모바일 530, 2026-09-13 실측, check-keywords.yml)
gate1_pass: true (일반 주제 기준 월 500 이상 필요, 850회로 충족)
serp_check: |
  [게이트2 v3 판정 2026-09-13 — 통과]
  WebSearch "ETF 괴리율 뜻 계산 확인하는 방법" 상위 6개:
  funetf.co.kr(ETF 운용사 콘텐츠) / brunch.co.kr(개인 브런치) / kcie.or.kr(금융교육원 계열
  모바일 콘텐츠) / simpleinvest.co.kr(개인/소규모 블로그) / etfdata.net(개인 서비스형 블로그)
  / etflove.com(개인 블로그, 10편 SERP에서도 확인된 도메인)
  1) 진입 여지 — 있음. brunch.co.kr·simpleinvest.co.kr·etfdata.net·etflove.com 등 개인/소규모
     콘텐츠가 상위 6개 중 4개. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻·계산법·보는법"). 조회/신청/계산기 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 아니다. 상위 글 전부 괴리율의 정의·계산식·기본 해석까지만 다루고,
     2026-08-19 시행된 금융위원회·한국거래소의 괴리율 관리기준 강화(국내 3%→2%, 해외 6%→5%,
     투자유의종목 지정절차 3단계→2단계 축소, 거래정지 기준)는 다루는 글이 없음. 정보이득
     여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  "괴리율 뜻과 계산식"까지는 상위 글도 다 다루지만, 2026-08-19부터 강화된 관리기준과 그 이후
  절차(투자유의종목 지정·단일가매매·거래정지)를 실제 숫자와 개정 전후 비교표로 정리한 글은
  SERP에 없다. (1) NAV·시장가 실제 숫자를 대입한 괴리율 계산 예시, (2) 관리기준 개정 전후
  비교표(국내 3%→2%, 해외 6%→5%), (3) 관리기준의 2배(국내 4%/해외 10%) 초과 시 투자유의종목
  적출·지정예고, 지정 후 3거래일 단일가매매, 마지막 날 3배(국내 6%/해외 15%) 이상 확대 시
  1거래일 거래정지라는 단계별 절차표, (4) 한국거래소 상장공시시스템(kind.krx.co.kr)에서
  "괴리율 초과 발생" 공시를 직접 찾아보는 방법을 정보이득으로 반영.
primary_source: |
  금융위원회 보도자료 원문(fsc.go.kr/no010101/87353, 2026-08-12 임시 정례회의 의결·2026-08-19
  시행) 및 한국거래소 유가증권시장 업무규정 개정안에 WebFetch를 1회 시도했으나 EGRESS_BLOCKED로
  확인(2026-09-13). 대조군으로 www.google.com도 동일하게 차단되어 이번 세션 전면 차단으로
  판단(9회 이상 연속 재현된 기존 패턴과 일치).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12) 기준 적용 —
  관리기준 강화 수치(국내 2%·해외 5%, 개정 전 3%·6%)와 절차(투자유의종목 지정 2단계 축소,
  3거래일 단일가매매, 3배 초과 시 거래정지)는 서로 무관한 9개 이상 독립 출처가 충돌 없이
  일치했다: 언론 7곳(파이낸셜뉴스 fnnews.com ×2, 디지털타임스 dt.co.kr ×2, 헤럴드경제
  heraldcorp.com, 중앙이코노미뉴스 joongangenews.com, 아주경제 ajunews.com, 이비엔뉴스
  ebn.co.kr, 서울파이낸스 seoulfn.com), 법률전문매체 1곳(법률신문 lawtimes.co.kr), 정부 뉴스
  포털 1곳(정책브리핑 korea.kr). 금융위원회 보도자료 원문 제목·URL(no010101/87353)도 WebSearch
  스니펫으로 확인해, 위 언론 보도가 실제 존재하는 공식 발표를 인용하고 있음을 교차 확인했다.
  단, ETF·ETN의 "실시간 공시 기준"(장중 순간 괴리율 초과 시 즉시 공시하는 별도 기준, 관리기준과는
  다른 수치로 일부 자료에 1%/2%로 언급됨)은 출처가 2곳(funetf.co.kr·kcie.or.kr, 둘 다 개인/교육
  콘텐츠 성격)뿐이라 신뢰도 기준 미달로 판단해 본문에 반영하지 않았다 — 원문 없이 지어내지
  않는다는 원칙에 따름.
기준일: 2026-09-13 (WebSearch 확인일, 개정 시행일 2026-08-19)
tags: ETF괴리율, ETF투자, NAV, 유동성공급자, 투자유의종목, 레버리지ETF, 주식초보, ETF관리기준
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-13).
  게이트1: 네이버 키워드도구 실측 850회(check-keywords.yml, 2026-09-13). 이번 배치 8개 후보 중
  유일하게 PASS(나머지 7개는 20~370회로 게이트1 미달).
  게이트2: v3 기준 통과(serp_check 참조) — 상위 SERP에 개인/소규모 콘텐츠 다수 진입, 2026-08-19
  개정 미반영으로 정보이득 여지 뚜렷.
  게이트3: 개정 전후 비교표 + 투자유의종목 지정·단일가매매·거래정지 단계표 + 실제 숫자 계산
  예시로 정보이득 확보.
  게이트4: fsc.go.kr 1회 시도 EGRESS_BLOCKED 확인(google.com 대조군도 차단, 세션 전면 차단) 후
  RULES.md 2026-09-12 기준에 따라 언론 7곳+법률신문+정책브리핑 등 9개 이상 독립 출처 교차검증으로
  진행, 수치 일치 확인, 한계(실시간 공시 기준 1%/2%는 출처 부족으로 미반영) 투명 공개.
self_check: |
  [2026-09-13 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 850회(일반 주제 기준 500회 이상).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 상위 검색 결과가 다루지 않는 2026-08-19 관리기준 개정(3%→2%, 6%→5%)과
  투자유의종목 지정·거래정지 절차를 실제 계산 예시·비교표·단계표로 정리해 차별화했다.
  게이트4 — fsc.go.kr에 1회 시도해 EGRESS_BLOCKED 확인, google.com 대조군도 차단되어 세션 전면
  차단으로 판단. 2026-09-12 RULES.md 기준을 적용해 언론 7곳+법률신문+정책브리핑 9개 이상 독립
  출처가 핵심 수치(2%/5%, 4%/10%, 3거래일, 3배 기준)에서 충돌 없이 일치함을 확인해 캡처 요청
  없이 진행했다. 신뢰도가 낮은 실시간 공시 기준(1%/2%)은 출처 2곳뿐이라 본문에서 제외했다.
  카니벌라이제이션 점검 — 1~21편 어디에도 ETF 괴리율·NAV·투자유의종목은 다루지 않는다. 10편
  (ETF 수수료 총보수 실부담 확인법)은 매년 떼는 보수 비용이 중심이고, 이 글은 거래 가격과
  순자산가치의 괴리(가격 왜곡) 문제라 검색 의도가 다르다. 본문에서 10편으로 내부 링크를 건다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 안내하는 자리와 하단 참고 출처 전부
  target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow 미부착.
  제목 "ETF 괴리율 계산법 관리기준 2026" 21자(공백 포함)·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 4단어(etf-divergence-rate-2026). FAQ 6개와 JSON-LD 1:1 일치.
  @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) → gate_pass:true.
  발행 가능.
---

<p>ETF 괴리율은 <mark>ETF의 시장가격과 순자산가치(NAV)가 얼마나 차이 나는지</mark>를 보여주는 지표입니다. 2026년 8월 19일부터 관리기준이 강화돼, 괴리율이 커진 ETF는 예전보다 더 빨리 투자유의종목으로 지정됩니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>괴리율 = <mark>(시장가격 − NAV) ÷ NAV × 100</mark>. 양수면 고평가, 음수면 저평가 상태입니다.</li>
    <li>2026-08-19부터 증권사(유동성공급자)의 종가 기준 괴리율 관리기준이 <b>국내 3%→2%, 해외 6%→5%</b>로 강화됐습니다.</li>
    <li>관리기준의 2배(국내 4%, 해외 10%)를 넘으면 즉시 투자유의종목으로 지정예고되고, 지정되면 3거래일간 단일가매매가 적용됩니다.</li>
    <li>단일가매매 마지막 날에도 관리기준의 3배 이상으로 괴리율이 벌어지면 하루 거래가 정지됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ETF 괴리율이란 무엇인가요</li>
  <li>괴리율은 어떻게 계산하나요</li>
  <li>괴리율은 어디서 확인하나요</li>
  <li>괴리율이 커지면 왜 문제가 되나요</li>
  <li>2026년 관리기준이 얼마나 강화됐나요</li>
  <li>투자유의종목 지정과 거래정지 기준은 무엇인가요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ETF 괴리율이란 무엇인가요</h2>

<p>ETF는 주식처럼 실시간으로 거래되지만, 그 안에 담긴 자산의 실제 가치인 <b>순자산가치(NAV, Net Asset Value)</b>는 별도로 계산됩니다. 이 둘 사이의 차이를 비율로 나타낸 것이 <mark>괴리율</mark>입니다.</p>

<p>괴리율이 <b>양수(+)</b>면 ETF가 실제 가치보다 비싸게(고평가) 거래되고 있다는 뜻이고, <b>음수(−)</b>면 실제 가치보다 싸게(저평가) 거래되고 있다는 뜻입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">괴리율은 어떻게 계산하나요</h2>

<p>계산식은 <b>{(시장가격 − NAV) ÷ NAV} × 100</b>입니다. 시장가격과 NAV의 차이가 NAV 대비 몇 %인지를 구하는 방식입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시</b>
  <p style="margin:8px 0 0 0;">어떤 ETF의 NAV가 31,000원이고 시장가격(종가)이 31,200원이라면, 괴리율은 (31,200−31,000)÷31,000×100 ≈ <mark>+0.65%</mark>입니다. 이 ETF는 실제 가치보다 약 0.65% 비싸게 거래되고 있다는 의미입니다.</p>
</div>

<p>NAV는 하루 한 번 장 마감 후 확정되므로, 장중에는 실시간으로 추정한 참고 NAV(iNAV)를 기준으로 괴리율이 계산됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">괴리율은 어디서 확인하나요</h2>

<p>가장 간단한 방법은 <b>증권사 앱이나 ETF 운용사 홈페이지</b>에서 종목별 NAV와 괴리율을 함께 조회하는 것입니다. 대부분의 증권사 앱은 ETF 상세 화면에 괴리율을 실시간 추정치로 표시합니다.</p>

<p>괴리율이 관리기준을 넘겨 공시된 내역은 <a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 상장공시시스템(KIND)</a>에서 종목명이나 "괴리율 초과 발생"으로 검색하면 실제 공시 원문을 확인할 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>증권사 앱·HTS의 ETF 상세 화면 (실시간 추정 괴리율)</li>
  <li>ETF 운용사(자산운용사) 홈페이지의 상품별 NAV 페이지</li>
  <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 상장공시시스템(KIND)</a> — 괴리율 초과 공시 원문</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">괴리율이 커지면 왜 문제가 되나요</h2>

<p>ETF의 시장가격이 NAV에 가깝게 유지되도록 호가를 촘촘히 제공하는 역할은 <b>유동성공급자(LP, Liquidity Provider)</b>인 증권사가 맡습니다. 시장 변동성이 크거나 헤지가 어려운 레버리지·인버스 상품일수록 LP가 가격을 붙잡아두기 어려워 괴리율이 벌어지기 쉽습니다.</p>

<p>괴리율이 크다는 것은 <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">투자자가 실제 가치보다 비싸게 사거나 싸게 팔 위험이 커졌다는 뜻</span>이라, 거래소는 LP에게 종가 기준 괴리율을 일정 범위 안으로 관리할 의무를 지웁니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2026년 관리기준이 얼마나 강화됐나요</h2>

<p>2026년 8월 19일부터 <b>모든 ETF·ETN에 적용되는 LP의 종가 기준 괴리율 관리기준이 강화</b>됐습니다. 단일종목 레버리지·인버스 상품 출시 이후 커진 변동성에 대응하기 위한 조치입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">2026-08-19 이전</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">2026-08-19 이후</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">국내 투자 ETF·ETN</td>
      <td style="border:1px solid #ddd;padding:8px;">3%</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>2%</mark></td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">해외 투자 ETF·ETN</td>
      <td style="border:1px solid #ddd;padding:8px;">6%</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>5%</mark></td>
    </tr>
  </tbody>
</table>

<p>괴리율이 음수로 산출되는 경우 절대값을 적용하도록 산정 기준도 함께 명확해졌습니다. 고의·중과실이나 상습적으로 관리의무를 위반한 LP는 신규 유동성공급 업무 자체가 제한됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">투자유의종목 지정과 거래정지 기준은 무엇인가요</h2>

<p>괴리율이 관리기준의 <b>2배(국내 4%, 해외 10%)</b>를 넘으면 적출과 동시에 지정예고됩니다. 2거래일 연속 기준을 넘기면 최단 2거래일 만에 투자유의종목으로 지정될 수 있습니다. 지정 절차도 기존 3단계(적출→지정예고→지정)에서 <b>2단계(적출 및 지정예고→지정)</b>로 줄었습니다.</p>

<ol style="line-height:1.9;">
  <li>괴리율이 관리기준의 2배 초과 → 적출 및 지정예고</li>
  <li>지정예고 후에도 기준 초과 지속(최단 2거래일) → 투자유의종목 지정</li>
  <li>지정되면 3거래일간 단일가매매 적용</li>
  <li>3거래일 연속 괴리율이 관리기준 이내로 낮아지면 지정 해제</li>
  <li>단일가매매 마지막 날 괴리율이 관리기준의 3배 이상(국내 6%, 해외 15%)으로 확대 → 1거래일 거래정지 후 단일가매매 재개</li>
</ol>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>레버리지·인버스 ETF일수록 괴리율을 더 자주 확인하세요</b>
  <p style="margin:8px 0 0 0;">단일종목 레버리지·인버스 상품은 헤지가 까다로워 괴리율이 커지기 쉽습니다. 매수 전 증권사 앱에서 괴리율을 확인하고, <a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 상장공시시스템(KIND)</a>에 해당 종목의 "괴리율 초과 발생" 공시가 있었는지 검색해 보는 습관이 도움이 됩니다.</p>
</div>

<p>ETF 매매 수수료·보수 자체가 궁금하다면 <a href="https://sensitiveboss3.tistory.com/entry/etf-fee-comparison" target="_blank" rel="noopener">이전 글(ETF 수수료 총보수 실부담 확인법)</a>에서 총보수와 실부담비용의 차이를 다뤘습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF 괴리율이란 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">ETF의 시장가격과 순자산가치(NAV)의 차이를 NAV 대비 비율로 나타낸 지표입니다. 양수면 고평가, 음수면 저평가 상태를 뜻합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">괴리율은 어떻게 계산하나요</summary>
  <p style="margin:10px 0 0 0;">{(시장가격 − NAV) ÷ NAV} × 100으로 계산합니다. 예를 들어 NAV 31,000원, 시장가격 31,200원이면 괴리율은 약 +0.65%입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">괴리율은 어디서 확인할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">증권사 앱이나 ETF 운용사 홈페이지에서 실시간 추정 괴리율을 확인할 수 있고, 기준을 넘긴 공시 원문은 한국거래소 상장공시시스템(KIND)에서 조회할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">2026년 괴리율 관리기준은 얼마나 강화됐나요</summary>
  <p style="margin:10px 0 0 0;">2026년 8월 19일부터 LP의 종가 기준 관리기준이 국내 3%에서 2%로, 해외 6%에서 5%로 각각 1%포인트씩 낮아졌습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">투자유의종목은 언제 지정되나요</summary>
  <p style="margin:10px 0 0 0;">괴리율이 관리기준의 2배(국내 4%, 해외 10%)를 넘으면 적출 및 지정예고되고, 최단 2거래일 만에 투자유의종목으로 지정될 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">투자유의종목으로 지정되면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">3거래일간 단일가매매가 적용됩니다. 이 기간 마지막 날에도 괴리율이 관리기준의 3배 이상으로 벌어지면 1거래일 거래가 정지된 뒤 단일가매매가 재개됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.lawtimes.co.kr/news/articleView.html?idxno=226172" target="_blank" rel="noopener">법률신문 — ETF·ETN 괴리율 관리 강화 및 단일종목 레버리지 상품 모의거래 의무화</a></li>
    <li><a href="https://www.fnnews.com/news/202608121627203356" target="_blank" rel="noopener">파이낸셜뉴스 — 19일부터 ETF 괴리율 관리 강화…단일종목 레버리지 모의거래 의무화</a></li>
    <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 상장공시시스템(KIND)</a></li>
  </ul>
  기준일: 2026-09-13(WebSearch 확인일). 관리기준 개정 시행일은 2026-08-19입니다. 금융위원회 원문(fsc.go.kr/no010101/87353)은 이번 세션 WebFetch가 차단돼 직접 확인하지 못했고, 위 언론·법률전문매체 등 9개 이상 독립 출처의 교차 확인으로 대체했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 판단과 그 결과에 대한 책임은 본인에게 있습니다. 괴리율 관리기준·투자유의종목 지정 절차는 제도 개정에 따라 바뀔 수 있으므로 거래 전 반드시 한국거래소·금융위원회의 최신 공지를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ETF 괴리율 계산법 관리기준 2026",
  "description": "ETF 괴리율의 뜻과 계산법, 2026년 8월 19일부터 강화된 괴리율 관리기준(국내 2%·해외 5%)과 투자유의종목 지정·거래정지 절차를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-09-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/etf-divergence-rate-2026"
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
      "name": "ETF 괴리율이란 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "ETF의 시장가격과 순자산가치(NAV)의 차이를 NAV 대비 비율로 나타낸 지표입니다. 양수면 고평가, 음수면 저평가 상태를 뜻합니다." }
    },
    {
      "@type": "Question",
      "name": "괴리율은 어떻게 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "{(시장가격 − NAV) ÷ NAV} × 100으로 계산합니다. 예를 들어 NAV 31,000원, 시장가격 31,200원이면 괴리율은 약 +0.65%입니다." }
    },
    {
      "@type": "Question",
      "name": "괴리율은 어디서 확인할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권사 앱이나 ETF 운용사 홈페이지에서 실시간 추정 괴리율을 확인할 수 있고, 기준을 넘긴 공시 원문은 한국거래소 상장공시시스템(KIND)에서 조회할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "2026년 괴리율 관리기준은 얼마나 강화됐나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2026년 8월 19일부터 LP의 종가 기준 관리기준이 국내 3%에서 2%로, 해외 6%에서 5%로 각각 1%포인트씩 낮아졌습니다." }
    },
    {
      "@type": "Question",
      "name": "투자유의종목은 언제 지정되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "괴리율이 관리기준의 2배(국내 4%, 해외 10%)를 넘으면 적출 및 지정예고되고, 최단 2거래일 만에 투자유의종목으로 지정될 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "투자유의종목으로 지정되면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "3거래일간 단일가매매가 적용됩니다. 이 기간 마지막 날에도 괴리율이 관리기준의 3배 이상으로 벌어지면 1거래일 거래가 정지된 뒤 단일가매매가 재개됩니다." }
    }
  ]
}
</script>
