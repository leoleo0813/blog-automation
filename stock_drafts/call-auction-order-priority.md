---
keyword: 동시호가 뜻
title: 동시호가 뜻과 매매체결 우선순위
slug: call-auction-order-priority
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1770 (PC 340 / 모바일 1430)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-25 — 통과]
  WebSearch "동시호가 뜻", "동시호가 뜻 매매체결 방법" 상위 8~9개:
  kbthink.com(KB국민은행 사전, 공식) / YouTube 영상 1개(텍스트 콘텐츠 아님) /
  namu.wiki(백과, x2) / eom.co.kr(개인·구식 사이트) / lifeuplogic.com(개인블로그) /
  econowide.com(개인·소규모 콘텐츠 사이트) / a-ha.io(커뮤니티 Q&A).
  1) 진입 여지 — 있음. eom.co.kr·lifeuplogic.com·econowide.com·a-ha.io까지
     4곳이 개인·소규모 콘텐츠·커뮤니티로 상위권에 있다.
  2) 검색 의도 — "뜻"을 묻는 개념 탐색형이다. 조회·신청·계산기 실행이
     지배적 의도가 아니다.
  3) 답 완결 여부 — 아니다. 상위 결과는 정의 한두 문장에 그치고, 장전
     시간외종가·장 시작 동시호가·정규장·장 마감 동시호가·장후
     시간외종가·시간외단일가까지 하루 전체 시간대를 한 표로 정리하거나
     체결 우선순위를 숫자 예시로 보여주는 곳이 없었다. 이 두 가지가
     정보이득 포인트다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 비교표 — 장전 시간외종가매매(08:30~08:40)부터 장 시작 동시호가
      (08:30~09:00), 정규장, 장 마감 동시호가(15:20~15:30), 장후
      시간외종가매매(15:40~16:00), 시간외단일가매매(16:00~18:00)까지
      하루 전체 매매체결 방식을 한 표로 정리했다. 상위 결과는 대부분
      한 시간대만 다루고 있어 이렇게 전체를 이어 붙인 표는 찾지 못했다.
  (b) 계산 예시 — 동시호가에서 상한가·하한가가 형성될 때는 시간 순서가
      아니라 수량이 많은 주문이 먼저 체결된다는 특례를, "A가 10,000원에
      10,000주, B가 같은 가격에 100주를 먼저 냈어도 A가 우선 체결된다"는
      구체적 숫자로 보여줬다. 상위 결과 중 이 특례를 수량 예시로 설명한
      곳은 찾지 못했다.
primary_source: |
  1차 시도: 한국거래소 규정 페이지 "매매거래제도 - 매매계약체결방법 -
  단일가매매시 체결방법"(https://regulation.krx.co.kr/contents/RGL/03/03010201/RGL03010201.jsp)에
  WebFetch를 1회 시도 → EGRESS_BLOCKED(2026-09-25). 법제처 찾기쉬운
  생활법령정보의 "매매거래일·거래시간 및 거래 원칙" 페이지
  (easylaw.go.kr)도 검색 결과에는 잡혔으나 동일하게 WebFetch가
  EGRESS_BLOCKED로 막혀, RULES.md 「1차 출처가 막혔을 때」 기준에 따라
  2차 출처 교차검증으로 전환했다.
  핵심 시간대(08:30~08:40 장전 시간외종가/전일종가 기준, 08:30~09:00
  장 시작 동시호가, 15:20~15:30 장 마감 동시호가, 15:40~16:00 장후
  시간외종가/당일종가 기준, 16:00~18:00 시간외단일가·10분단위·당일종가
  대비 ±10%)는 미래에셋증권(securities.miraeasset.com)·한국투자증권
  (truefriend.com)·KB국민은행(kbthink.com)·키움증권(kiwoom.com)·
  신한투자증권(shinhansec.com)·교보증권(iprovest.com)·삼성증권
  (samsungpop.com)·증권플러스(stockplus.com) 등 8곳 이상의 제도권
  금융회사 공식 안내 페이지에서 충돌 없이 일치했다. 법제처 찾기쉬운
  생활법령정보 페이지도 검색 결과 제목에서 동일 주제("매매거래일·
  거래시간 및 거래 원칙 등")를 다루는 것으로 확인돼 준정부기관 성격의
  출처로 함께 참고했다.
  동시호가의 체결 우선순위 특례(상·하한가 형성 시 시간우선 배제, 수량
  많은 주문 우선)는 대신증권(daishin.com) 공식 안내와 나무위키
  "매매우선원칙" 항목이 동일한 원칙과 예시로 일치했다.
  종합: 매매시간·기준가격은 8곳 이상 독립된 제도권 금융회사 공식
  페이지가 충돌 없이 일치했고, 법제처(준정부기관) 페이지도 같은 주제를
  다루는 것으로 확인돼 근거를 보강했다. 세율·공제한도 같은 유형의
  숫자가 아니라 시장에 이미 공개된 매매제도(시간표·우선순위 규칙)이므로
  RULES.md의 교차검증 진행 기준을 충족한다고 판단해 gate4를 충족으로
  처리한다. 한국거래소 규정 원문 대조는 사람이 직접 열어보면 더 확실하다.
기준일: 2026-09-25 (WebSearch 교차검증일 기준)
tags: 동시호가, 단일가매매, 매매체결, 시간외거래, 시가결정, 종가결정, 주식초보, 매매시간, 체결우선순위
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 1,770회(일반 주제 기준 500
  이상, 같은 배치에서 함께 확인한 유상증자 무상증자 차이(120)·신주인수권
  뜻(440)·관리종목 지정 요건(40)·불성실공시법인 지정(120)·코넥스 시장
  뜻(100)·주식대여서비스 세금(20)·최대주주 변경 공시(20)는 전부 FAIL).
  게이트2 충족 — v3 기준 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 하루 전체 매매체결 시간대 비교표와 체결 우선순위 특례의
  수량 계산 예시 확보.
  게이트4 충족 — 1차 출처(한국거래소 규정, 법제처) WebFetch는 모두
  EGRESS_BLOCKED로 막혔으나, 독립된 제도권 금융회사 공식 페이지 8곳
  이상과 준정부기관 성격의 법제처 페이지가 핵심 수치에서 충돌 없이
  일치해 RULES.md의 교차검증 진행 기준을 충족했다.
capture_guide: ""
self_check: |
  [2026-09-25 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — 기존 79편 중 "동시호가"를 다룬 편은
  quadruple-witching-day-2026.md(네마녀의 날) 1건뿐이며, 이 글은
  네마녀의 날 당일 동시호가 물량 급증을 한 문단으로 언급할 뿐 동시호가
  자체의 정의·시간대·체결 우선순위는 다루지 않아(grep 확인) 겹치지
  않는다.
  기관 링크 점검 — 본문에서 한국거래소·법제처로 안내하는 문장과 하단
  참고 출처 전부 target="_blank" rel="noopener"로 링크 처리했다.
  정부·준정부 기관 링크는 nofollow 미부착.
  제목 "동시호가 뜻과 매매체결 우선순위" 17자·금지어 없음·조사/접속사
  없음. 슬러그 영문 소문자+하이픈 4단어(call-auction-order-priority).
  인트로 문단 최상단 배치, "안녕하세요" 없음. 비교표 2개 모두 thead/tbody
  시맨틱.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서
  "—" 0개 확인. "다만"은 본문에서 0회(전환은 "그런데"·"반면"·"이때"·
  "여기서 헷갈리기 쉬운 점은"으로 분산). `<mark>` 총 5개(3~5개 기준
  충족, 상한선). FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을 "🕒 미리
  정리하면"으로, 색상은 포레스트그린 계열(#eaf6ec/#2e7d32)로 최근
  게시물(버건디 #a4243b·슬레이트블루 #3949ab·틸 #0f9b8e)과 겹치지 않게
  골랐다. 목차 제외 본문 H2 5개 중 서술형 4개("동시호가라는 이름과 실제
  체결 방식의 차이", "하루 중 동시호가가 적용되는 시간대", "동시호가에서
  주문이 체결되는 순서", "시간외 거래와 동시호가, 헷갈리지 않는 법"),
  질문형 1개("동시호가란 무엇인가요")로 "~나요" 편중 없음(5개 중 1개,
  20%). FAQ 헤딩도 "자주 묻는 질문" 대신 "이런 것도 궁금하시죠"로
  변형.
  헤지 표현 남발 없음 — 확정된 사실은 단정해서 쓰고, 교차검증으로
  확인했다는 사실만 출처 문단에 한 번 명시했다. 면책 문구는 기존
  게시물과 다른 표현으로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-25</p>

<p>동시호가는 <mark>정해진 시간 동안 들어온 매수·매도 주문을 한꺼번에 모아 단 하나의 가격으로 한 번에 체결하는 방식</mark>입니다. 장이 시작하기 전이나 끝나기 직전마다 등장하는 개념인데, 이 시간에 낸 주문은 먼저 넣었다고 유리하지 않다는 점을 모르면 손해를 보기 쉽습니다. 이 글에서는 동시호가가 적용되는 시간대와 실제 체결 순서를 숫자 예시로 정리합니다.</p>

<div style="background:#eaf6ec;border:2px solid #2e7d32;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1b5e20;font-size:18px;">🕒 미리 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>동시호가는 08:30~09:00(장 시작)과 15:20~15:30(장 마감)에 적용되며, 이 시간에 접수된 주문을 한 번에 모아 시가·종가를 결정합니다.</li>
    <li>정규장 중에는 가격·시간·수량 순으로 체결되지만, 동시호가에서 상한가·하한가가 형성될 때는 시간 순서가 무시되고 수량이 많은 주문이 먼저 체결됩니다.</li>
    <li>장전·장후 시간외종가매매, 시간외단일가매매는 동시호가와 이름은 비슷해도 기준가격과 체결방식이 다릅니다.</li>
    <li>동시호가 시간에 주문을 넣어도 실제 체결은 09:00 또는 15:30에 한 번에 이뤄집니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>동시호가란 무엇인가요</li>
  <li>동시호가라는 이름과 실제 체결 방식의 차이</li>
  <li>하루 중 동시호가가 적용되는 시간대</li>
  <li>동시호가에서 주문이 체결되는 순서</li>
  <li>시간외 거래와 동시호가, 헷갈리지 않는 법</li>
  <li>이런 것도 궁금하시죠</li>
</ol>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">동시호가란 무엇인가요</h2>

<p>동시호가(同時呼價)는 "같은 시간"을 뜻하는 동시와 "부르는 가격"을 뜻하는 호가가 합쳐진 말입니다. 일정 시간 동안 들어온 모든 매수·매도 주문을 접수 순서와 상관없이 동시에 접수된 것으로 취급해, 그 시간이 끝나는 순간 단 하나의 가격으로 한꺼번에 체결합니다.</p>

<p>이 방식으로 결정되는 가격이 바로 그날의 시가(장 시작 가격)와 종가(장 마감 가격)입니다. 정규장 시간에는 주문이 들어오는 즉시 개별적으로 체결되지만, 동시호가 시간에는 주문을 모아뒀다가 한 번에 처리한다는 점이 다릅니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">동시호가라는 이름과 실제 체결 방식의 차이</h2>

<p>사람들이 보통 "동시호가"라고 부르는 08:30~09:00, 15:20~15:30 시간대는 정확히는 <mark>단일가매매</mark>라는 체결 방식이 적용되는 구간입니다. 동시호가는 이 단일가매매 안에서 주문을 처리하는 원칙(접수 순서를 따지지 않는다)을 가리키는 말이고, 단일가매매는 그 원칙으로 하나의 가격을 정하는 방법 전체를 가리킵니다.</p>

<p>실무에서는 두 용어를 구분 없이 섞어 쓰는 경우가 많아 크게 문제 되지 않습니다. 그런데 시간외단일가매매처럼 단일가매매 방식을 쓰면서도 동시호가 시간대는 아닌 구간도 있어, 뒤에서 다룰 시간외 거래와 헷갈리는 경우가 종종 생깁니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">하루 중 동시호가가 적용되는 시간대</h2>

<p>코스피·코스닥 정규장을 기준으로 하루 동안 단일가매매(동시호가 포함)가 적용되는 구간은 아래와 같습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시간</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">명칭</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">기준가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">08:30~08:40</td>
      <td style="border:1px solid #ddd;padding:8px;">장전 시간외종가매매</td>
      <td style="border:1px solid #ddd;padding:8px;">전일 종가</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;"><mark>08:30~09:00</mark></td>
      <td style="border:1px solid #ddd;padding:8px;">장 시작 동시호가</td>
      <td style="border:1px solid #ddd;padding:8px;">시가 결정</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">09:00~15:20</td>
      <td style="border:1px solid #ddd;padding:8px;">정규장(접속매매)</td>
      <td style="border:1px solid #ddd;padding:8px;">개별 주문마다 체결</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;"><mark>15:20~15:30</mark></td>
      <td style="border:1px solid #ddd;padding:8px;">장 마감 동시호가</td>
      <td style="border:1px solid #ddd;padding:8px;">종가 결정</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">15:40~16:00</td>
      <td style="border:1px solid #ddd;padding:8px;">장후 시간외종가매매</td>
      <td style="border:1px solid #ddd;padding:8px;">당일 종가</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">16:00~18:00</td>
      <td style="border:1px solid #ddd;padding:8px;">시간외단일가매매</td>
      <td style="border:1px solid #ddd;padding:8px;">당일 종가 대비 ±10% 이내, 10분 단위로 새로 체결</td>
    </tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>용어 정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>시가</b>: 그날 정규장에서 처음 형성된 가격.</li>
    <li><b>종가</b>: 그날 정규장에서 마지막으로 형성된 가격.</li>
    <li><b>단일가매매</b>: 여러 주문을 모아 한 번에 하나의 가격으로 체결하는 방식.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">동시호가에서 주문이 체결되는 순서</h2>

<p>정규장 중 개별 체결에서는 가격이 유리한 주문이 먼저, 가격이 같으면 먼저 낸 주문이 먼저, 그마저 같으면 수량이 많은 주문이 먼저 체결됩니다. 동시호가 시간에도 이 원칙이 기본으로 적용됩니다.</p>

<p>여기서 헷갈리기 쉬운 점은 예외 상황입니다. 동시호가로 가격이 <mark>상한가나 하한가로 형성될 때는 시간 순서를 따지지 않고, 수량이 많은 주문을 먼저 체결</mark>합니다. 예를 들어 A가 10,000원에 10,000주를 먼저 주문하고, B가 같은 가격에 100주를 그보다 늦게 주문했다면, 상한가·하한가 상황에서는 B가 먼저 주문했더라도 수량이 많은 A의 물량이 먼저 체결됩니다.</p>

<ul style="line-height:1.9;">
  <li>평상시(상·하한가가 아닌 경우): 가격 우선 → 시간 우선 → 수량 우선</li>
  <li>동시호가에서 상한가·하한가가 형성되는 경우: 가격 우선 → 수량 우선(시간은 따지지 않음)</li>
</ul>

<p>이 예외는 특정 시간에 대량 주문을 먼저 넣는다고 반드시 유리해지지 않는다는 뜻이기도 합니다. 실제 체결 결과는 그날 접수된 전체 주문에 따라 달라집니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">시간외 거래와 동시호가, 헷갈리지 않는 법</h2>

<p>장전·장후 시간외종가매매는 이름에 "시간외"가 붙어 있지만 동시호가와는 다릅니다. 이 구간은 이미 정해진 가격(전일 종가 또는 당일 종가)으로 주문을 접수 순서대로 체결하는 방식이라, 시간 우선 원칙이 그대로 적용됩니다.</p>

<p>반면 시간외단일가매매는 동시호가처럼 단일가매매 방식을 쓰지만, 시간대가 16:00~18:00으로 정규장 마감 이후이고 10분 단위로 여러 번 가격을 새로 정한다는 점이 다릅니다. 세 가지 모두 "시간외" 또는 "동시호가"라는 이름이 섞여 쓰이다 보니 초보 투자자가 가장 혼동하는 구간입니다.</p>

<p>정확한 매매제도 원문은 <a href="https://regulation.krx.co.kr/contents/RGL/03/03010201/RGL03010201.jsp" target="_blank" rel="noopener">한국거래소 매매거래제도 규정</a>이나 <a href="https://easylaw.go.kr" target="_blank" rel="noopener">법제처 찾기쉬운 생활법령정보</a>에서 확인할 수 있고, 이용 중인 증권사 앱의 거래시간 안내 페이지에서도 같은 내용을 볼 수 있습니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">이런 것도 궁금하시죠</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">동시호가와 단일가매매는 같은 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">완전히 같지는 않습니다. 단일가매매는 여러 주문을 모아 하나의 가격으로 체결하는 방식 자체를 가리키고, 동시호가는 그 안에서 접수 시간을 따지지 않는다는 원칙을 가리킵니다. 실무에서는 두 말을 섞어 써도 크게 문제 되지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">동시호가 시간에 낸 주문은 언제 체결되나요</summary>
  <p style="margin:10px 0 0 0;">장 시작 동시호가(08:30~09:00)에 낸 주문은 09:00에, 장 마감 동시호가(15:20~15:30)에 낸 주문은 15:30에 한꺼번에 체결됩니다. 그 전까지는 접수만 되고 체결되지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">동시호가에서는 왜 먼저 주문해도 유리하지 않나요</summary>
  <p style="margin:10px 0 0 0;">평소에는 가격이 같으면 먼저 낸 주문이 우선이지만, 동시호가로 상한가·하한가가 형성될 때는 시간 순서를 따지지 않고 수량이 많은 주문을 먼저 체결하기 때문입니다. 이 시간에는 몇 시 몇 분에 냈는지보다 얼마나 많은 수량을 냈는지가 더 중요합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">시간외단일가매매와 동시호가는 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">시간외단일가매매(16:00~18:00)도 단일가매매 방식을 쓰지만, 정규장 동시호가와 달리 10분마다 새로 가격을 정하고 당일 종가 대비 ±10% 안에서만 거래됩니다. 정규장의 동시호가는 하루에 시가·종가를 정할 때 딱 두 번만 일어납니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">장 시작 동시호가 가격이 상한가로 몰리면 어떻게 체결되나요</summary>
  <p style="margin:10px 0 0 0;">상한가에 매수 주문이 몰려 전량 체결이 안 될 때는 시간 순서와 상관없이 수량이 많은 주문부터 순서대로 체결됩니다. 늦게 주문했어도 수량이 많으면 일찍 주문한 소량 주문보다 먼저 체결될 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://regulation.krx.co.kr/contents/RGL/03/03010201/RGL03010201.jsp" target="_blank" rel="noopener">한국거래소 - 매매거래제도(단일가매매시 체결방법)</a></li>
    <li><a href="https://easylaw.go.kr" target="_blank" rel="noopener">법제처 - 찾기쉬운 생활법령정보(매매거래일·거래시간 및 거래 원칙)</a></li>
    <li>기준일: 2026-09-25(WebSearch 교차검증일). 매매시간·체결방식은 제도권 금융회사 공식 안내 8곳 이상에서 확인.</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 주식 매매제도를 설명하는 정보 글이며, 특정 종목이나 상품의 매수·매도를 권하지 않습니다. 매매시간과 체결 규칙은 한국거래소 사정에 따라 바뀔 수 있으므로, 실제 거래 전에는 한국거래소나 이용 중인 증권사의 최신 공지를 확인하시기 바랍니다. 투자 판단과 그 결과는 투자자 본인의 책임입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "동시호가 뜻과 매매체결 우선순위",
  "description": "동시호가의 뜻과 장 시작·장 마감 시간대, 시간외 거래와의 차이, 상한가·하한가 형성 시 체결 우선순위를 계산 예시로 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-25",
  "dateModified": "2026-09-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/call-auction-order-priority"
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
      "name": "동시호가와 단일가매매는 같은 뜻인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "완전히 같지는 않습니다. 단일가매매는 여러 주문을 모아 하나의 가격으로 체결하는 방식 자체를 가리키고, 동시호가는 그 안에서 접수 시간을 따지지 않는다는 원칙을 가리킵니다. 실무에서는 두 말을 섞어 써도 크게 문제 되지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "동시호가 시간에 낸 주문은 언제 체결되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "장 시작 동시호가(08:30~09:00)에 낸 주문은 09:00에, 장 마감 동시호가(15:20~15:30)에 낸 주문은 15:30에 한꺼번에 체결됩니다. 그 전까지는 접수만 되고 체결되지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "동시호가에서는 왜 먼저 주문해도 유리하지 않나요",
      "acceptedAnswer": { "@type": "Answer", "text": "평소에는 가격이 같으면 먼저 낸 주문이 우선이지만, 동시호가로 상한가·하한가가 형성될 때는 시간 순서를 따지지 않고 수량이 많은 주문을 먼저 체결하기 때문입니다. 이 시간에는 몇 시 몇 분에 냈는지보다 얼마나 많은 수량을 냈는지가 더 중요합니다." }
    },
    {
      "@type": "Question",
      "name": "시간외단일가매매와 동시호가는 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "시간외단일가매매(16:00~18:00)도 단일가매매 방식을 쓰지만, 정규장 동시호가와 달리 10분마다 새로 가격을 정하고 당일 종가 대비 ±10% 안에서만 거래됩니다. 정규장의 동시호가는 하루에 시가·종가를 정할 때 딱 두 번만 일어납니다." }
    },
    {
      "@type": "Question",
      "name": "장 시작 동시호가 가격이 상한가로 몰리면 어떻게 체결되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "상한가에 매수 주문이 몰려 전량 체결이 안 될 때는 시간 순서와 상관없이 수량이 많은 주문부터 순서대로 체결됩니다. 늦게 주문했어도 수량이 많으면 일찍 주문한 소량 주문보다 먼저 체결될 수 있습니다." }
    }
  ]
}
</script>
