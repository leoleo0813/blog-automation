---
keyword: 해외주식 배당소득세
title: 해외주식 배당소득세 얼마 떼나
slug: overseas-stock-dividend-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 300 (PC 80 / 모바일 220)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요 — check-keywords.yml 2026-09-16 실측)
serp_check: |
  [게이트2 v3 판정 2026-09-16 — 통과]
  WebSearch "해외주식 배당소득세 원천징수 15% 외국납부세액공제 계산" + "해외주식 배당소득세
  얼마나 떼나요" + "해외주식 배당세율 국가별 미국15% 중국10% 일본 원천징수" 상위 종합:
  toss.im(토스, 공식) / kbcapital.co.kr·kbthink.com(KB, 공식 ×2) / hanwhawm.com(한화투자증권,
  공식) / kcie.or.kr(금융투자자보호재단, 준정부 ×2) / daolsecurities.com(다올투자증권, 공식) /
  iprovest.com(교보증권, 공식) / kiwoom.com(키움증권, 공식) / hanaw.com(하나증권, 공식) /
  imfnsec.com(아이엠증권, 공식) / heumtax.com(세무법인) / casenote.kr(국세청 유권해석 정리) /
  ttegl.com(개인·소규모 블로그) / 2ndsystem.net(개인 블로그) / hometax-go.kr(세무서비스 콘텐츠)
  1) 진입 여지 — 있음. ttegl.com·2ndsystem.net 같은 개인·소규모 블로그가 상위권에 진입해
     SERP가 잠겨 있지 않음(대부분은 증권사 공식 콘텐츠지만 완전히 잠긴 상태는 아님).
  2) 검색 의도 — 정보 탐색+계산("얼마나 떼나, 어떻게 계산하나"). 조회·계산기 실행이
     지배적 의도가 아님.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 국가별 세율(미국 15%/중국 10%/일본
     15.315%)과 "현지세율이 국내 14%보다 높으면 추가징수 없다"는 원칙까지는 다루지만,
     (a) 국가별로 실제 원 단위가 얼마나 달라지는지 계산예시로 보여주는 글, (b) 4편(국내
     배당소득세 15.4%)·15편(미국주식 세금, 요약 한 줄만)과 겹치지 않게 "해외주식만의
     이중과세 조정 메커니즘"에 집중해 국가별 비교+종합과세 전환 시 외국납부세액공제까지
     한 편에 정리한 글은 찾지 못했다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  기존 4편(배당소득세)은 국내 배당(15.4% 원천징수)만 다루고, 15편(미국주식 세금)은
  해외 배당 부분을 "미국에서 15% 원천징수 후 한국에서 정산됩니다" 한 줄로만 요약한다.
  이 글은 그 사이 공백 — "해외주식만의 이중과세 조정 메커니즘" — 을 채운다.
  (1) 국가별 현지 원천징수율(미국 15%/중국 10%/일본 15.315%/홍콩 0%)과, 국내 14%
      기준보다 높으면 국내 추가징수가 없고 낮으면 차액만 추가로 걷는다는 원칙을
      100만원 배당 기준 실제 원 단위 계산 4개국 비교표로 보여준다.
  (2) 금융소득(이자+배당 합산) 2천만원을 넘어 종합과세로 전환되면, 해외에서 이미 낸
      세금을 다시 내지 않도록 외국납부세액공제(소득세법 제57조, 공제한도 = 종합소득
      산출세액 × 국외원천소득/종합소득금액)가 적용된다는 원리를 설명한다. 개인별
      종합소득 구성에 따라 산출세액이 달라 원 단위 예시는 만들지 않고 공식과 개념만
      정확히 전달한다(수치를 지어내지 않는다는 원칙 우선).
primary_source: |
  1차 시도: 국세청(nts.go.kr) 배당소득 원천징수 안내 페이지 WebFetch 1회 시도 →
  EGRESS_BLOCKED(2026-09-16). 대조군 www.google.com도 동일하게 EGRESS_BLOCKED로 확인돼
  세션 전면 차단으로 판단(RULES.md 누적 기록 패턴과 일치).
  다만 이중과세 조정의 핵심 메커니즘("배당소득 원천징수: 국내세법 14%에서 외국
  원천징수세액 차감")과 "해외주식 배당소득: 연 금융소득 2천만원 이하+원천징수 시
  분리과세 종결, 초과 시 종합소득세 합산"은 이미 5편(해외주식 양도소득세 신고 방법)
  작업 시 사람이 국세청 홈페이지에서 직접 내려받아 이 저장소에 확보해 둔 1차 출처
  「2024년 해외주식과 세금(개인투자자용)」(국세청 국제조세담당관실, 2024-05 발간,
  sources/nts-overseas-stock-tax-2024.md/.pdf)에 이미 명시돼 있어 새 캡처 없이 재사용했다.
  국가별 구체 세율(미국 15%/중국 10%/일본 15.315%/홍콩 0%)과 국내 추가징수 공식(중국
  사례: 부족분 4% 소득세+그 10%인 0.4% 지방소득세)은 RULES.md 「1차 출처가 막혔을 때」
  (2026-09-12) 기준에 따라 2차 출처 교차검증으로 확정했다 — 서로 무관한 독립 출처
  6곳(키움증권·KB·다올투자증권·하나증권·아이엠증권 등 공식 증권사 콘텐츠 5곳 + 금융투자자
  보호재단(kcie.or.kr, 준정부) 1곳)이 전부 동일 수치로 일치하고 충돌이 없었다.
  외국납부세액공제 계산 공식(소득세법 제57조)은 국가법령정보센터(law.go.kr) 검색 스니펫에
  실린 조문 요지("종합소득산출세액에 국외원천소득이 종합소득금액에서 차지하는 비율을
  곱해 산출")와 casenote.kr(국세청 유권해석 정리)이 일치해 법령 원문 기준으로 확정했다.
기준일: 2026-09-16 (WebSearch 확인일. 이중과세 조정 메커니즘 자체는 국세청 공식 책자
  2024-05 발간분 — RULES.md 3년 신선도 기준 이내, 2026-09-16 현재 약 2년 4개월 경과)
tags: 해외주식배당소득세, 해외주식세금, 배당소득세, 외국납부세액공제, 미국주식배당세, 원천징수, 금융소득종합과세, 이중과세, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-16).
  게이트1: 네이버 키워드도구 실측 300회(check-keywords.yml, 2026-09-16 — 세부·제도 기준
  100회 이상). 같은 배치에서 개인투자용국채 세금(90회)·채권 매매방법(50회)·감사의견
  비적정 상장폐지(20회)·불성실공시법인 지정(110회)·증권계좌 이전 방법(20회)·주식
  양도소득세 예정신고(20회)·상장적격성 실질심사(130회)는 게이트1 미달로 탈락.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그 진입 여지 있고, 국가별
  비교+종합과세 전환 시 외국납부세액공제까지 통합한 콘텐츠 부재로 정보이득 여지 있음.
  게이트3: 100만원 배당 기준 4개국(미국/중국/일본/홍콩) 실제 원 단위 비교표 + 외국납부
  세액공제 원리(공식만, 개인별 수치는 지어내지 않음)로 정보이득 확보.
  게이트4: nts.go.kr WebFetch 1회 시도 EGRESS_BLOCKED 확인(google.com 대조군도 차단, 세션
  전면 차단) 후, 핵심 메커니즘은 이미 확보된 국세청 공식 책자(1차 출처, 2024-05)를
  재사용하고, 국가별 세율·공식은 RULES.md 2026-09-12 기준에 따라 6곳 이상 독립 출처
  교차검증(공식 증권사 5곳+준정부 1곳, 충돌 없음) + 법령(소득세법 제57조) 원문 인용으로
  진행. 이 방식은 15편(미국주식 세금)에서 같은 15% 원천징수 수치를 동일 방식으로
  cross-verify해 gate_pass:true로 발행한 선례와 일치한다.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 300회(제도 세부 키워드 기준 100회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 국가별(미국/중국/일본/홍콩) 100만원 배당 기준 실제 원 단위 비교표
  (실효세율 15% / 14.4% / 15.315% / 15.4%)와, 종합과세 전환 시 외국납부세액공제 원리를
  4편·15편이 다루지 않는 각도로 통합.
  게이트4 — nts.go.kr 직접 열람은 막혔으나(google.com 대조군도 차단, 세션 전면 차단),
  이중과세 조정 메커니즘의 핵심 문장은 이미 확보된 국세청 공식 책자(1차 출처, 2024-05
  발간, sources/nts-overseas-stock-tax-2024.md)를 재사용했다. 국가별 구체 세율은 서로
  무관한 독립 출처 6곳(공식 증권사 5곳 + 금융투자자보호재단 1곳)이 충돌 없이 일치함을
  확인했고, 외국납부세액공제 공식은 국가법령정보센터(law.go.kr)의 소득세법 제57조
  조문 요지로 확정했다. 개인별 종합소득에 따라 달라지는 세액공제 실제 원 단위는
  지어내지 않고 공식과 원리만 전달했다.
  카니벌라이제이션 점검 — 4편(배당소득세)은 국내 배당 15.4% 원천징수만 다루고, 이 글은
  해외 배당의 이중과세 조정(국가별 세율 비교)에 집중해 겹치지 않는다. 15편(미국주식
  세금)은 배당세를 "미국 15% 원천징수 후 한국에서 정산" 한 줄로만 요약하고 상속세에
  집중하므로, 이 글이 그 한 줄을 구체화하는 관계다. 본문에서 4편·15편으로 내부 링크.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 국세청 안내 문장과 하단 참고 출처 목록
  전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow 미부착.
  출처 URL은 이미 확보된 sources/ 파일과 WebSearch로 실제 확인된 주소만 사용(지어내지
  않음).
  제목 "해외주식 배당소득세 얼마 떼나" 16자(공백 포함)·금지어 없음. 4편과 동일한
  "{대상} 얼마 떼나" 패턴으로 일관성 유지. 슬러그 영문 소문자+하이픈 4단어
  (overseas-stock-dividend-tax). 인트로 문단 최상단 배치. 표는 thead/tbody 시맨틱 사용.
  기준일 명시. FAQ 6개와 JSON-LD 1:1 일치. 종목·상품 추천 표현, 단정 표현 없음. 하단
  면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 1차 출처 재사용 + 6곳 이상 독립 출처
  교차검증 + 법령 원문 인용으로 대체, 한계 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-16</p>

<p><mark>해외주식 배당소득세는 국내주식과 다르게, 투자한 나라에서 먼저 세금을 뗀 뒤 한국에서 나머지를 정산</mark>합니다. 그래서 같은 100만원을 배당받아도 미국·중국·일본 중 어디 주식이냐에 따라 실제로 떼이는 세금이 달라집니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>해외주식 배당은 <b>투자한 나라에서 먼저 원천징수</b>됩니다(미국 15%, 중국 10%, 일본 15.315%, 홍콩 0%).</li>
    <li>현지 세율이 <b>국내 기준 14%보다 높으면</b> 국내에서 추가로 떼지 않습니다(미국·일본).</li>
    <li>현지 세율이 <b>14%보다 낮으면</b> 부족한 만큼만 국내에서 추가로 걷습니다(중국·홍콩).</li>
    <li>연간 금융소득(이자+배당 합산)이 <mark>2,000만원을 넘으면</mark> 종합과세 대상이 되고, 해외에서 낸 세금은 외국납부세액공제로 이중과세를 조정받습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>해외주식 배당소득세는 어떻게 원천징수되나요</li>
  <li>나라마다 세율이 왜 다른가요</li>
  <li>국내에서 추가로 세금을 더 내야 하나요</li>
  <li>금융소득종합과세 대상이 되면 어떻게 되나요</li>
  <li>국내주식 배당소득세와 무엇이 다른가요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 배당소득세는 어떻게 원천징수되나요</h2>

<p>해외주식 배당금은 <b>투자한 나라(현지)에서 먼저 세금을 뗀 뒤</b> 나머지 금액이 국내 증권계좌로 들어옵니다. <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a>이 발간한 「2024년 해외주식과 세금」에 따르면, 국내 세법상 배당소득 원천징수세율 14%에서 이미 낸 외국 원천징수세액을 차감해 이중과세를 조정합니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">국내 배당소득세(4편, 15.4%)와 다른 점은 세금을 떼는 주체와 순서다</span>는 것입니다. 국내주식은 국내 세법 하나만 적용되지만, 해외주식은 현지 세율과 국내 세율(14%)을 비교해 부족한 부분만 추가로 걷습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">나라마다 세율이 왜 다른가요</h2>

<p>현지 원천징수세율은 나라마다 다르고, 이 세율이 <b>국내 기준 14%보다 높은지 낮은지</b>에 따라 국내 추가 징수 여부가 갈립니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">국가</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">현지 원천징수율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">국내 기준(14%) 대비</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">미국</td>
      <td style="border:1px solid #ddd;padding:8px;">15%</td>
      <td style="border:1px solid #ddd;padding:8px;">높음 — 국내 추가징수 없음</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">일본</td>
      <td style="border:1px solid #ddd;padding:8px;">15.315%</td>
      <td style="border:1px solid #ddd;padding:8px;">높음 — 국내 추가징수 없음</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">중국</td>
      <td style="border:1px solid #ddd;padding:8px;">10%</td>
      <td style="border:1px solid #ddd;padding:8px;">낮음 — 부족분(4%) 국내 추가징수</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">홍콩</td>
      <td style="border:1px solid #ddd;padding:8px;">0%</td>
      <td style="border:1px solid #ddd;padding:8px;">낮음(없음) — 국내 14% 전액 징수</td>
    </tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>세율표는 언제든 바뀔 수 있습니다</b>
  <p style="margin:8px 0 0 0;">위 세율은 각국 세법과 한국과의 조세조약에 따라 정해지며, 조약 개정이나 세법 변경으로 달라질 수 있습니다. 투자 전 증권사 고객센터나 국세청 안내로 최신 세율을 다시 확인하는 것이 안전합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">국내에서 추가로 세금을 더 내야 하나요</h2>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">100만원을 배당받았다고 가정하면, 나라별로 실제 손에 쥐는 금액이 달라집니다.</span></p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">국가</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">현지 징수</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">국내 추가 징수</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">실효세율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">미국</td>
      <td style="border:1px solid #ddd;padding:8px;">15만원(15%)</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">15%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">중국</td>
      <td style="border:1px solid #ddd;padding:8px;">10만원(10%)</td>
      <td style="border:1px solid #ddd;padding:8px;">소득세 4만원(4%)+지방소득세 4천원(0.4%)</td>
      <td style="border:1px solid #ddd;padding:8px;">14.4%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">일본</td>
      <td style="border:1px solid #ddd;padding:8px;">15만 3,150원(15.315%)</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">15.315%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">홍콩</td>
      <td style="border:1px solid #ddd;padding:8px;">없음(0%)</td>
      <td style="border:1px solid #ddd;padding:8px;">소득세 14만원(14%)+지방소득세 1만 4,000원(1.4%)</td>
      <td style="border:1px solid #ddd;padding:8px;">15.4%</td>
    </tr>
  </tbody>
</table>

<p>중국처럼 현지 세율이 14%보다 낮으면 <b>부족한 부분만</b> 국내에서 걷고, 지방소득세는 그 부족분(4%)의 10%인 0.4%만 붙습니다. 홍콩처럼 현지 원천징수가 아예 없으면 국내주식과 동일하게 14%+지방소득세 1.4%=15.4%가 그대로 적용됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">금융소득종합과세 대상이 되면 어떻게 되나요</h2>

<p>이자·배당을 합친 연간 금융소득이 <mark>2,000만원을 넘으면</mark> 해외주식 배당도 다른 금융소득과 합산해 다음 해 5월 종합소득세로 신고해야 합니다. 이때 해외에서 이미 낸 세금을 다시 내지 않도록 <b>외국납부세액공제</b>가 적용됩니다.</p>

<ul style="line-height:1.9;">
  <li>공제 대상 — 조세조약과 외국 세법에 따라 적법하게 납부한 외국 세액(소득세법 제57조)</li>
  <li>공제 한도 — 종합소득산출세액 × (국외원천소득 ÷ 종합소득금액)</li>
  <li>한도를 넘는 금액은 이월해 <b>10년 이내</b> 공제 가능</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>실제 공제액은 사람마다 다릅니다</b>
  <p style="margin:8px 0 0 0;">공제 한도는 그해 전체 종합소득 구성(근로·사업·금융소득 등)에 따라 달라져 일률적인 원 단위 계산이 어렵습니다. 종합과세 대상이라면 <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> 종합소득세 신고 안내나 세무 전문가 상담으로 본인의 정확한 공제액을 확인해야 합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">국내주식 배당소득세와 무엇이 다른가요</h2>

<p>국내주식 배당은 <a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax" target="_blank" rel="noopener">이전 글(배당소득세 얼마 떼나)</a>에서 다룬 것처럼 국내 세법 15.4%(14%+지방소득세 1.4%) 하나만 적용됩니다. 해외주식은 여기에 <b>현지 원천징수</b>라는 단계가 하나 더 있고, 국가별로 실효세율이 15%~15.4% 사이에서 달라진다는 점이 다릅니다.</p>

<p>미국주식을 보유하다 사망하는 경우의 <b>미국 연방 상속세</b> 이슈는 배당·양도세와는 완전히 다른 세목입니다. 자세한 내용은 <a href="https://sensitiveboss3.tistory.com/entry/us-stock-tax" target="_blank" rel="noopener">이전 글(미국주식 세금 종류와 상속세 주의점)</a>에서 다룹니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 배당소득세는 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">투자한 나라의 현지 원천징수율에 따라 다릅니다. 미국 15%, 일본 15.315%처럼 국내 기준 14%보다 높으면 그 세율이 최종 실효세율이고, 낮으면 국내에서 부족분을 추가로 걷어 최대 15.4%까지 올라갑니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">미국주식은 왜 국내에서 추가로 세금을 안 떼나요</summary>
  <p style="margin:10px 0 0 0;">미국 현지 원천징수율 15%가 국내 기준 14%보다 이미 높기 때문입니다. 국내 세법은 현지에서 낸 세금이 국내 기준을 넘으면 추가로 걷지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">중국주식은 왜 국내에서 세금을 추가로 떼나요</summary>
  <p style="margin:10px 0 0 0;">중국 현지 원천징수율이 10%로 국내 기준 14%보다 낮기 때문입니다. 부족한 4%를 국내에서 소득세로, 그 10%인 0.4%를 지방소득세로 추가 징수합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">외국납부세액공제는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">금융소득종합과세 대상이 됐을 때 해외에서 이미 낸 세금을 다시 내지 않도록 조정해주는 제도입니다. 공제 한도는 종합소득산출세액에 국외원천소득이 차지하는 비율을 곱해 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금융소득 2천만원 넘으면 어떻게 신고하나요</summary>
  <p style="margin:10px 0 0 0;">이자·배당을 합친 연간 금융소득이 2,000만원을 넘으면 다음 해 5월에 다른 소득과 합산해 종합소득세로 확정신고해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내주식 배당소득세와 다른가요</summary>
  <p style="margin:10px 0 0 0;">국내주식은 국내 세법 15.4% 하나만 적용되지만, 해외주식은 현지 원천징수가 먼저 있고 국내 14% 기준과 비교해 부족분만 추가로 걷는다는 점이 다릅니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> - 「2024년 해외주식과 세금(개인투자자용)」(2024-05 발간)</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 소득세법 제57조(외국납부세액공제)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> - 종합소득세 신고 안내</li>
  </ul>
  기준일: 2026-09-16(WebSearch 확인일). 이중과세 조정 메커니즘은 국세청 공식 책자
  2024-05 발간분 기준입니다. 국세청 원문 페이지는 이번 세션 WebFetch가 차단돼 직접
  열람하지 못했고, 이미 확보된 동일 책자와 복수 독립 증권사·준정부 기관의 교차 확인으로
  대체했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를
권유하지 않습니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "해외주식 배당소득세 얼마 떼나",
  "description": "해외주식 배당소득세의 국가별 원천징수율(미국 15%, 중국 10%, 일본 15.315%, 홍콩 0%)과 국내 추가징수 여부, 100만원 배당 기준 실효세율 비교, 금융소득종합과세 전환 시 외국납부세액공제 원리를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-16",
  "dateModified": "2026-09-16",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/overseas-stock-dividend-tax"
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
      "name": "해외주식 배당소득세는 얼마인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "투자한 나라의 현지 원천징수율에 따라 다릅니다. 미국 15%, 일본 15.315%처럼 국내 기준 14%보다 높으면 그 세율이 최종 실효세율이고, 낮으면 국내에서 부족분을 추가로 걷어 최대 15.4%까지 올라갑니다." }
    },
    {
      "@type": "Question",
      "name": "미국주식은 왜 국내에서 추가로 세금을 안 떼나요",
      "acceptedAnswer": { "@type": "Answer", "text": "미국 현지 원천징수율 15%가 국내 기준 14%보다 이미 높기 때문입니다. 국내 세법은 현지에서 낸 세금이 국내 기준을 넘으면 추가로 걷지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "중국주식은 왜 국내에서 세금을 추가로 떼나요",
      "acceptedAnswer": { "@type": "Answer", "text": "중국 현지 원천징수율이 10%로 국내 기준 14%보다 낮기 때문입니다. 부족한 4%를 국내에서 소득세로, 그 10%인 0.4%를 지방소득세로 추가 징수합니다." }
    },
    {
      "@type": "Question",
      "name": "외국납부세액공제는 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "금융소득종합과세 대상이 됐을 때 해외에서 이미 낸 세금을 다시 내지 않도록 조정해주는 제도입니다. 공제 한도는 종합소득산출세액에 국외원천소득이 차지하는 비율을 곱해 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "금융소득 2천만원 넘으면 어떻게 신고하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "이자·배당을 합친 연간 금융소득이 2,000만원을 넘으면 다음 해 5월에 다른 소득과 합산해 종합소득세로 확정신고해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "국내주식 배당소득세와 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "국내주식은 국내 세법 15.4% 하나만 적용되지만, 해외주식은 현지 원천징수가 먼저 있고 국내 14% 기준과 비교해 부족분만 추가로 걷는다는 점이 다릅니다." }
    }
  ]
}
</script>
