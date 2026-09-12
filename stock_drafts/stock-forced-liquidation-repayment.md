---
keyword: 반대매매 뜻
title: 반대매매 뜻 미수 신용 상환기한
slug: stock-forced-liquidation-repayment
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 970 (2026-09-12 네이버 키워드도구 실측, backlog.verified에서 승격)
gate1_pass: true (일반 주제 기준 월 500 이상 필요, 970회로 충족)
serp_check: |
  [게이트2 v3 판정 2026-09-12 — 통과]
  WebSearch "반대매매 뜻 미수 신용거래 상환기한" + "반대매매 발생 조건 체결시간 하한가 매도" 상위 종합:
  kbthink.com(KB 공식, ×2) / v.daum.net(언론) / dic.hankyung.com(한국경제 공식 사전) /
  stockplus.com(핀테크 콘텐츠) / namu.wiki(백과) / eugenefn.com(유진투자증권 공식) /
  clien.net(개인 커뮤니티) / a-ha.io(Q&A 커뮤니티, ×3) / kakaopaysec.com(증권사 공식)
  1) 진입 여지 — 있음. clien.net·a-ha.io(다수)·stockplus.com 등 커뮤니티·소규모 콘텐츠가
     상위에 다수 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻·발생 기준·시점"). 조회/신청/계산기 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 아니다. 상위 글들이 개념(미수·신용·반대매매 정의)은 설명하지만, 미수·신용·
     담보대출 3종의 반대매매 기준·상환기한을 한 표로 비교하지 않고, 담보유지비율 140% 기준으로
     "실제 몇 % 떨어지면 반대매매되는지"를 계산해 보여주는 글은 못 찾음. 커뮤니티 답변끼리도
     체결시각·상환기한 설명이 조금씩 달라(예: "90일" vs "30~150일") 정리된 정보가 부족함.
     정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-12]
  (a) 미수거래·신용거래(융자)·주식담보대출 3종의 반대매매 기준과 상환기한을 한 표로 비교.
  (b) 핵심 정보이득 — 담보유지비율 140% 기준을 실제 숫자(자기담보 400만원+신용융자금 600만원)에
      대입해 "매수가 대비 몇 % 하락하면 반대매매 대상이 되는지"(16%)를 직접 계산해서 보여준다.
      상위 검색 결과 대부분은 "140%"라는 숫자만 언급하고 이 계산까지 하지 않음.
  (c) 반대매매를 피하기 위한 실제 타임라인(담보부족 발생 → D+1까지 추가담보 요구 → D+2 아침
      하한가 주문)과, 하한가로 걸리는 이유(체결 보장, 실제 체결가는 시장가 흐름에 따름)를 정리.
primary_source: |
  금융투자협회 법규정보시스템(law.kofia.or.kr)의 신용거래융자 핵심설명서·신용거래설명서 규정
  원문에 WebFetch를 1회 시도했으나 EGRESS_BLOCKED로 확인(2026-09-12). 대조군으로 www.google.com도
  동일하게 차단되어 이번 세션 전면 차단으로 판단.
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12) 기준 적용 —
  담보유지비율 140%(최소 기준, 회사별 140~160%)와 상환기한 90일(연장 시 최장 150일)은 서로
  독립된 9개 이상의 증권사 공식 규정 문서(한국투자증권 truefriend.com, 신한투자증권 PDF,
  미래에셋증권, KB증권, 삼성증권, 하나증권 myasset.com, 교보증권, 한양증권, 카카오페이증권,
  유진투자증권)가 충돌 없이 일치했고, 이 문서들은 금융소비자보호법에 따라 금융소비자보호
  총괄책임자 검토를 거쳐 게시되는 공식 규정 설명서라 언론 보도보다도 신뢰도가 높다고 판단해
  캡처 요청 없이 교차검증으로 진행했다. 미수거래 T+2 상환기한·30일 100% 증거금 징수(미수동결계좌)는
  한국투자증권 공식 안내(truefriend.com)를 1차로, kbthink.com(KB 공식)으로 재확인했다.
기준일: 2026-09-12 (WebSearch 확인일)
tags: 반대매매, 미수거래, 신용거래, 담보유지비율, 상환기한, 위탁증거금, 강제매도, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-12).
  게이트1: 네이버 키워드도구 실측 970회(2026-09-12, backlog.verified 기록 재확인).
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 3종 거래 반대매매 기준 비교표 + 담보유지비율 140% 실제 계산 예시(16% 하락 시
  반대매매 대상)로 정보이득 확보.
  게이트4: law.kofia.or.kr 1회 시도 EGRESS_BLOCKED 확인 후, RULES.md 2026-09-12 기준에 따라
  9개 이상 증권사 공식 규정설명서 교차검증으로 진행. 한계 투명 공개.
self_check: |
  [2026-09-12 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 970회(backlog.verified에서 이미 확인된 값).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — "얼마나 떨어져야 반대매매되는지"라는 실질적 궁금증에 담보유지비율 140%를
  대입한 계산 예시로 답하고, 3종 거래(미수·신용·담보대출)의 기준·상환기한을 표로 비교해
  상위 검색 결과와 차별화했다.
  게이트4 — law.kofia.or.kr에 1회 시도해 EGRESS_BLOCKED 확인, google.com 대조군도 차단되어
  세션 전면 차단으로 판단. 2026-09-12 RULES.md에 새로 정리된 "2차 출처 교차검증 vs 사람 캡처
  요청" 기준을 적용: 담보유지비율(140%)·상환기한(90일/150일)은 금융소비자보호법상 검토를 거쳐
  게시되는 증권사 공식 규정설명서 9곳 이상이 충돌 없이 일치해 캡처 요청 없이 진행했다. 계산
  예시(400만원+600만원, 16% 하락)는 확인된 140% 규정을 저자가 직접 대입해 도출한 것으로,
  특정 출처의 예시를 그대로 베낀 것이 아니다.
  카니벌라이제이션 점검 — 1~19편 어디에도 반대매매·미수거래·신용거래 상환기한은 다루지 않는다.
  19편(주식 예수금 뜻 증거금 100%)과는 위탁증거금 개념을 공유하지만, 19편은 "왜 매수가
  거부되는가"가 중심이고 이 글은 "빚을 못 갚으면 어떻게 강제매도되는가"가 중심이라 검색
  의도가 다르다. 본문에서 19편으로 내부 링크를 건다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 안내하는 자리와 하단 참고 출처 전부
  target="_blank" rel="noopener"로 링크 처리.
  제목 17자(공백 포함)·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음. 하단 면책
  문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) → gate_pass:true.
  발행 가능.
---

<p>반대매매는 증권사에 빌린 돈이나 부족한 담보를 <mark>정해진 기한까지 채우지 못하면</mark> 증권사가 동의 없이 내 주식을 강제로 파는 제도입니다. 미수거래와 신용거래는 반대매매 기준과 상환기한이 서로 다릅니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>반대매매는 미수금이나 부족 담보를 <mark>정해진 기한까지</mark> 못 채우면 증권사가 강제로 매도하는 제도입니다.</li>
    <li>미수거래는 매매일을 포함해 <b>3거래일(T+2)</b>까지 미수금을 못 갚으면 반대매매됩니다.</li>
    <li>신용거래는 담보유지비율이 <mark>140% 밑으로</mark> 떨어지고 추가담보를 못 채우면 반대매매되며, 상환기한은 통상 90일(연장 시 최장 150일)입니다.</li>
    <li>반대매매는 보통 하한가로 주문이 걸리지만, 실제 체결가는 그날 시장 상황에 따라 달라집니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>반대매매란 무엇인가요</li>
  <li>미수거래는 언제 반대매매되나요</li>
  <li>신용거래 반대매매 기준은 무엇인가요</li>
  <li>실제로 얼마나 떨어져야 반대매매되나요</li>
  <li>반대매매를 피하려면 언제까지 뭘 해야 하나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">반대매매란 무엇인가요</h2>

<p>반대매매(反對賣買)는 투자자가 증권사에서 빌린 돈이나 부족한 담보를 <mark>정해진 기한까지 채우지 못했을 때</mark>, 증권사가 투자자의 동의 없이 해당 주식을 강제로 파는 제도입니다.</p>

<p>반대매매가 나올 수 있는 거래는 크게 세 가지이고, 셋은 기준과 상환기한이 서로 다릅니다.</p>
<ul style="line-height:1.9;">
  <li><b>미수거래</b> — 매수 증거금 일부만 내고 나머지(미수금)를 외상으로 사는 방식</li>
  <li><b>신용거래(융자)</b> — 증권사에서 돈을 빌려 주식을 사는 방식, 담보유지비율이 적용됨</li>
  <li><b>주식담보대출</b> — 보유 중인 주식을 담보로 현금을 빌리는 방식</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">미수거래는 언제 반대매매되나요</h2>

<p>미수거래로 산 주식은 <mark>매매일을 포함해 3거래일째(T+2)</mark>까지 미수금(증거금을 낸 나머지 금액)을 갚지 못하면 반대매매됩니다.</p>

<p>예를 들어 위탁증거금율이 40%인 종목을 1,000만원어치 미수로 매수하면 400만원만 증거금으로 내고 나머지 600만원이 미수금입니다. 이 600만원을 3거래일째까지 채우지 못하면 보유 주식이 강제로 매도됩니다. (위탁증거금율은 종목마다 20~100%로 다르며, 자세한 내용은 <a href="https://sensitiveboss3.tistory.com/entry/stock-deposit-margin-rate" target="_blank" rel="noopener">이전 글(주식 예수금 뜻·증거금 100%)</a>에서 다뤘습니다.)</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>미수 발생 시 30일간 페널티</b>
  <p style="margin:8px 0 0 0;">미수금을 못 갚아 반대매매가 나오면 그다음 날부터 <b>30일간 위탁증거금을 현금으로 100%</b> 내야 하는 '미수동결계좌'로 지정됩니다. 이 기간에는 미수거래 자체가 불가능합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신용거래 반대매매 기준은 무엇인가요</h2>

<p>신용거래(융자)는 계좌의 <mark>담보유지비율이 최소 140%</mark> 아래로 떨어지면 반대매매 대상이 됩니다. 담보유지비율은 증권사별로 140~160% 사이에서 다르게 정합니다.</p>

<p>담보유지비율은 [담보평가금액 ÷ 신용융자금] × 100으로 계산합니다. 이 비율이 기준 미달이면 증권사가 정한 기한까지 추가담보를 채워야 반대매매를 피할 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">거래 유형</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">반대매매 기준</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">상환기한</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">미수거래</td>
      <td style="border:1px solid #ddd;padding:8px;">미수금 미상환</td>
      <td style="border:1px solid #ddd;padding:8px;">매매일 포함 3거래일(T+2)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">신용거래(융자)</td>
      <td style="border:1px solid #ddd;padding:8px;">담보유지비율 140% 미달 + 추가담보 미납</td>
      <td style="border:1px solid #ddd;padding:8px;">통상 90일, 연장 시 최장 150일(증권사별로 다름)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주식담보대출</td>
      <td style="border:1px solid #ddd;padding:8px;">상품별 담보유지비율 미달</td>
      <td style="border:1px solid #ddd;padding:8px;">상품·증권사마다 다름</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제로 얼마나 떨어져야 반대매매되나요</h2>

<p>신용거래로 자기 돈(담보) 400만원에 신용융자금 600만원을 더해 총 1,000만원어치 주식을 샀다고 가정해봅니다. 담보유지비율 140% 기준을 적용하면, 융자금 600만원의 140%인 <mark>840만원</mark> 이상의 평가금액을 계속 유지해야 합니다.</p>

<p>매수 총액 1,000만원 대비 840만원은 <b>16% 하락</b>한 수준입니다. 즉 이 경우 주가가 매수가 대비 16% 이상 떨어지면 담보가 부족해져 반대매매 대상이 될 수 있습니다.</p>

<p>이 하락 허용폭은 자기 돈(담보) 비율이 클수록 커집니다. 반대로 신용융자 비중이 높을수록 더 적은 하락에도 반대매매 위험이 커집니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">반대매매를 피하려면 언제까지 뭘 해야 하나요</h2>

<p>담보가 부족해지면 증권사는 보통 <mark>다음 영업일(D+1)까지 추가담보 납입을 요구</mark>하고, 이때까지 채우지 못하면 그다음 영업일(D+2) 아침 반대매매가 실행됩니다.</p>

<p>반대매매 주문은 무조건 체결되도록 <b>하한가로 걸리는 경우가 많지만</b>, 실제 체결 가격은 그날 시장 상황에 따라 달라집니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>추가담보를 넣을 수 있는 마감 시각을 확인하세요</b>
  <p style="margin:8px 0 0 0;">증권사 시스템은 통상 반대매매 실행일 아침 일찍 반대매매 수량을 계산해 거래소에 주문을 보냅니다. 그 이전에 부족 금액을 입금하면 반대매매를 취소할 수 있는 경우가 많지만, 정확한 마감 시각은 증권사마다 다르므로 거래 중인 증권사 고객센터나 공지로 미리 확인해야 합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">반대매매란 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">투자자가 증권사에 빌린 돈이나 부족한 담보를 정해진 기한까지 채우지 못했을 때, 증권사가 동의 없이 주식을 강제로 매도하는 제도입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">미수거래 반대매매는 언제 발생하나요</summary>
  <p style="margin:10px 0 0 0;">매매일을 포함해 3거래일째(T+2)까지 미수금을 갚지 못하면 반대매매됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신용거래 반대매매 기준은 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">계좌의 담보유지비율이 최소 140% 아래로 떨어지고, 증권사가 정한 기한까지 추가담보를 채우지 못하면 반대매매됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신용거래 상환기한은 얼마나 되나요</summary>
  <p style="margin:10px 0 0 0;">통상 90일이며, 연장하면 최장 150일까지 가능합니다. 정확한 기간과 연장 조건은 증권사마다 다릅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">반대매매를 피하려면 어떻게 해야 하나요</summary>
  <p style="margin:10px 0 0 0;">담보부족 통지를 받으면 다음 영업일(D+1)까지 추가담보를 넣거나 빌린 돈 일부를 갚아 담보유지비율을 회복해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">반대매매 가격은 왜 하한가로 나오나요</summary>
  <p style="margin:10px 0 0 0;">무조건 체결되게 하기 위해서입니다. 증권사가 하한가로 매도 주문을 넣더라도 실제 체결 가격은 그날 시장 상황에 따라 달라집니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://law.kofia.or.kr/service/law/lawFullScreenContent.do?seq=291&amp;historySeq=1391" target="_blank" rel="noopener">금융투자협회 법규정보시스템 — 신용거래융자 핵심설명서(예시)</a></li>
    <li><a href="https://file.truefriend.com/Storage/customer/guide/regards/service_29.htm" target="_blank" rel="noopener">한국투자증권 — 신용거래(융자,대주) 설명서</a></li>
    <li><a href="https://www.eugenefn.com/serv/svlo/svlo107p.do" target="_blank" rel="noopener">유진투자증권 — 반대매매 안내</a></li>
    <li>기준일: 2026-09-12(WebSearch 확인일, 증권사 공식 규정설명서 9곳 이상 교차 확인)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 판단과 그 결과에 대한 책임은 본인에게 있습니다. 담보유지비율·상환기한 등 반대매매 관련 규정은 증권사와 상품에 따라 다르고 개정될 수 있으므로 거래 전 반드시 해당 증권사의 최신 공지를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "반대매매 뜻 미수 신용 상환기한",
  "description": "반대매매의 뜻과 미수거래·신용거래·주식담보대출별 발생 기준, 담보유지비율 140% 계산 예시, 반대매매를 피하는 방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-12",
  "dateModified": "2026-09-12",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-forced-liquidation-repayment"
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
      "name": "반대매매란 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "투자자가 증권사에 빌린 돈이나 부족한 담보를 정해진 기한까지 채우지 못했을 때, 증권사가 동의 없이 주식을 강제로 매도하는 제도입니다." }
    },
    {
      "@type": "Question",
      "name": "미수거래 반대매매는 언제 발생하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "매매일을 포함해 3거래일째(T+2)까지 미수금을 갚지 못하면 반대매매됩니다." }
    },
    {
      "@type": "Question",
      "name": "신용거래 반대매매 기준은 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "계좌의 담보유지비율이 최소 140% 아래로 떨어지고, 증권사가 정한 기한까지 추가담보를 채우지 못하면 반대매매됩니다." }
    },
    {
      "@type": "Question",
      "name": "신용거래 상환기한은 얼마나 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "통상 90일이며, 연장하면 최장 150일까지 가능합니다. 정확한 기간과 연장 조건은 증권사마다 다릅니다." }
    },
    {
      "@type": "Question",
      "name": "반대매매를 피하려면 어떻게 해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "담보부족 통지를 받으면 다음 영업일(D+1)까지 추가담보를 넣거나 빌린 돈 일부를 갚아 담보유지비율을 회복해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "반대매매 가격은 왜 하한가로 나오나요",
      "acceptedAnswer": { "@type": "Answer", "text": "무조건 체결되게 하기 위해서입니다. 증권사가 하한가로 매도 주문을 넣더라도 실제 체결 가격은 그날 시장 상황에 따라 달라집니다." }
    }
  ]
}
</script>
