---
keyword: 배당수익률
title: 배당수익률 계산법
slug: dividend-yield-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 860 (PC 280 / 모바일 580, 2026-09-17 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-17 — 통과]
  WebSearch "배당수익률" + "배당수익률 뜻 계산법" + "시가배당률 뜻 배당기준일 직전 평균주가"
  상위 종합: tradingview(해외 플랫폼, ×2) / tikr.com(해외 서비스) / toss.im(토스, 핀테크
  기업) / wikipedia(백과) / data.krx.co.kr(한국거래소, 공식) / stockplus(증권플러스,
  핀테크) / jptcalc.kr(개인·소규모 계산기 블로그) / bileotools.com(개인·소규모 블로그) /
  brunch.co.kr(개인 블로그) / econowide.com(개인 블로그) / dic.hankyung.com(한경용어사전,
  경제지 부속 사전) / kbthink.com(KB금융, 공식) / 대한금융신문(kbanker.co.kr, 언론사) /
  FunETF(funetf.co.kr, 소규모 투자정보 사이트) / 아이투자(itooza.com, 소규모 가치투자
  포털)
  1) 진입 여지 — 있음. jptcalc.kr·bileotools.com·brunch.co.kr·econowide.com·FunETF·
     아이투자 등 개인·소규모 콘텐츠가 상위 다수 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형(뜻·계산법·비교). 상위 결과 대부분이 정의·공식·설명형
     콘텐츠이고, 계산기 실행이 지배적 의도는 아니다(계산기형 사이트는 일부에 불과).
  3) 답 완결 여부 — 부분적. 상위 대부분이 "배당수익률=주당배당금÷주가" 공식과 배당컷
     위험 정도까지만 다루고, ① 배당수익률과 시가배당률의 기준일 차이(현재가 vs 배당기준일
     직전 평균가) ② 배당소득세 원천징수(15.4%) 반영한 세후 실수령 수익률 계산까지 하나의
     글에서 예시와 함께 엮어 보여주는 글은 확인하지 못했다. 이 두 가지가 정보이득.
  → 탈락조건 1·2 미해당, 탈락조건 3은 시가배당률 비교+세후 계산 정보이득으로 상쇄해 통과.
unique_asset: |
  "배당수익률=주당배당금÷주가"라는 공식만 알려주는 기존 콘텐츠와 달리, 실전에서 혼동되는
  두 가지를 계산 예시로 정리했다.
  - 배당수익률과 시가배당률은 계산 기준일이 다르다. 시가배당률은 기업이 배당을 공시할 때
    쓰는 값으로 배당기준일(또는 배당결정일) 직전 1주일 평균 주가를 쓰고, 배당수익률은
    증권사 앱·포털이 보여주는 값으로 오늘의 현재가를 쓴다. 같은 배당금이라도 주가가
    움직이면 두 숫자는 달라진다 — 예시로 공시 당시 40,000원이던 주가가 이후 50,000원으로
    오르면 시가배당률 5.0%가 배당수익률로는 4.0%로 낮아지는 것을 계산으로 보여준다.
  - 표시되는 배당수익률은 세전 값이다. 배당소득세 원천징수 15.4%(4편에서 확정한 수치)를
    반영하면 세전 5.0% 수익률이 세후로는 4.23%까지 낮아진다는 것을 원 단위 계산 예시로
    보여준다.
  - 배당수익률이 비정상적으로 높게 보이는 경우, 배당금이 늘어난 게 아니라 주가가 급락해
    분모가 작아졌을 때도 같은 현상이 나타난다는 점을 판별 체크리스트로 정리(특정 종목
    거론 없이 일반 판단 기준만 제시).
primary_source: |
  1차 시도: 한국거래소 정보데이터시스템(data.krx.co.kr, PER/PBR/배당수익률 데이터 페이지)
  WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-17). 대조군으로 무관한 도메인(google.com)에도
  1회 추가 시도했으나 동일하게 EGRESS_BLOCKED로 확인돼 이번 세션의 전면 차단으로 판단했다
  (RULES.md 누적 기록 패턴과 일치, 그 이상 재시도하지 않음).
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다.
  - 배당수익률·시가배당률의 정의와 계산 기준(현재가 vs 배당기준일 직전 평균가)은 서로
    무관한 독립 출처 5곳 이상(대한금융신문 - 언론사, KB금융 경제용어사전 kbthink.com,
    한경용어사전 dic.hankyung.com - 경제지 부속 사전, FunETF, 아이투자)이 충돌 없이
    일치했다. 단순 사전적 정의이자 오래 고정된 시장 관행(세율·공제한도처럼 이 프로젝트가
    과거 오류를 잡아낸 유형의 숫자가 아님)이라 교차검증으로 진행해도 되는 유형으로
    판단했다.
  - 배당소득세 원천징수세율 15.4%는 신규 확인이 아니라 4편(배당소득세 얼마 떼나,
    dividend-income-tax)에서 이미 법제처 원문(2026-08-15 기준)으로 확정한 수치를 그대로
    재사용했다(신규 캡처 불필요).
기준일: 2026-09-17 (WebSearch 확인일)
tags: 배당수익률, 시가배당률, 배당수익률계산법, 배당소득세, 배당투자, 배당컷, 주식초보, 재테크초보, 세후배당수익률
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-17).
  게이트1: 네이버 키워드도구 실측 860회(같은 배치, 2026-09-17 — 일반 주제 기준 500회
  이상). backlog.verified에 "단순 순서 대기"로 분류된 항목 중 유일하게 남은 후보라 이번
  편으로 채택했다(같은 배치에서 검색량이 더 높았던 배당기준일 1,090회·미수거래 970회는
  각각 16편·21편과 카니벌라이제이션 점검이 먼저 필요해 대기 상태로 남아있다).
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그 진입 여지 있고, 시가배당률
  비교+세후 실수령 계산을 함께 다루는 글이 상위에 없어 정보이득 여지 있음.
  게이트3: 시가배당률 vs 배당수익률 계산 비교 + 세전/세후(15.4%) 계산 예시 + 배당수익률
  함정(배당컷) 판별 체크리스트로 정보이득 확보.
  게이트4: data.krx.co.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군(google.com)도 차단돼
  세션 전면 차단 확인 후 RULES.md 2026-09-12 기준에 따라 교차검증 진행 — 정의·계산기준은
  독립 출처 5곳 이상(언론사 포함)이 충돌 없이 일치, 세율 15.4%는 4편에서 이미 확정된
  수치 재사용.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 860회(일반 주제 기준 500회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은 시가배당률
  비교+세후 계산 정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 시가배당률과의 계산 기준 차이, 세전/세후 실수령 수익률 계산 예시,
  배당컷 위험 판별 체크리스트로 상위 결과가 다루지 않는 각도를 확보했다.
  게이트4 — data.krx.co.kr 직접 열람은 막혔고(대조군 google.com도 차단, 세션 전면 차단),
  정의·계산기준은 언론사 포함 독립 출처 5곳 이상으로 교차검증, 세율 15.4%는 4편에서
  이미 확정된 수치를 재사용했다.
  카니벌라이제이션 점검 — 4편(배당소득세)은 원천징수 세율·종합과세 여부 판단이 중심,
  6편(금융소득종합과세)은 2천만원 초과 합산과세 판단이 중심이라 이 글(배당수익률이라는
  투자 지표 자체의 정의·계산·함정)과 검색 의도가 겹치지 않는다. 4편으로 세율 부분만
  내부 링크로 연결하고 본문에서 세율을 재도출하지 않았다. 1~46편 어디에도 배당수익률
  지표 자체를 계산법 관점에서 다룬 글은 없다(그렙 검색 확인).
  기관 링크 점검(RULES.md「기관 링크 필수」) — 한국거래소 정보데이터시스템 안내 문장과
  하단 참고 출처 목록 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에
  nofollow 미부착. 출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "배당수익률 계산법" 9자(공백 포함)·금지어 없음·조사·접속사 없음. 슬러그 영문
  소문자+하이픈 3단어(dividend-yield-calculation). 인트로 문단 최상단 배치. 표는
  thead/tbody 시맨틱 사용. 기준일 명시. FAQ 6개와 JSON-LD 1:1 일치. 종목·상품 추천 표현,
  단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 언론사 포함 독립 출처 5곳 이상 교차검증 +
  4편 기확정 세율 재사용으로 대체, 한계는 본문·출처란에 투명 공개) → gate_pass:true.
  발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-17</p>

<p><mark>증권사 앱에 뜨는 배당수익률과 기업이 공시하는 시가배당률은 계산 기준이 달라 같은 종목인데도 숫자가 다르게 보일 수 있습니다.</mark> 여기에 배당소득세까지 떼고 나면 실제로 손에 들어오는 수익률은 화면에 뜬 숫자보다 낮습니다. 계산 예시로 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>배당수익률은 <b>주당배당금 ÷ 현재 주가 × 100</b>으로 계산합니다.</li>
    <li>시가배당률은 <mark>배당기준일 직전 평균 주가</mark>를 쓰고, 배당수익률은 <mark>오늘 주가</mark>를 씁니다 — 그래서 숫자가 다릅니다.</li>
    <li>배당소득세 15.4%를 떼면 <b>세전 5.0% 수익률이 세후로는 4.23%</b>까지 낮아집니다.</li>
    <li>배당수익률이 비정상적으로 높다면 <b>배당이 늘어서가 아니라 주가가 급락해서</b>인 경우도 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>배당수익률이 뭔가요</li>
  <li>배당수익률은 어떻게 계산하나요</li>
  <li>배당수익률과 시가배당률은 뭐가 다른가요</li>
  <li>세금을 떼면 실제 수익률은 얼마나 낮아지나요</li>
  <li>배당수익률이 높으면 무조건 좋은가요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당수익률이 뭔가요</h2>

<p>배당수익률은 지금 주가로 그 주식을 산다면 배당금만으로 연간 몇 %의 수익을 얻을 수 있는지 나타내는 지표입니다. 증권사 앱이나 포털의 종목 정보 화면에 함께 표시되는 숫자입니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">주가와 배당금이 서로 다른 종목의 배당 매력을 같은 기준(%)으로 비교할 수 있다는 것이 배당수익률의 쓸모입니다.</span> 배당금 자체의 크기(원)만으로는 비싼 주식과 싼 주식을 나란히 비교하기 어렵기 때문입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당수익률은 어떻게 계산하나요</h2>

<p><b>배당수익률(%) = 주당배당금 ÷ 현재 주가 × 100</b>입니다. 1주당 연간 배당금을 지금 주가로 나눈 뒤 100을 곱하면 됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">현재 주가</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">연간 주당배당금</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산식</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">배당수익률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">40,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,000 ÷ 40,000 × 100</td>
      <td style="border:1px solid #ddd;padding:8px;">5.0%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">100,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,000 ÷ 100,000 × 100</td>
      <td style="border:1px solid #ddd;padding:8px;">2.0%</td>
    </tr>
  </tbody>
</table>

<p>같은 2,000원을 배당하더라도 <mark>주가가 낮을수록 배당수익률은 높게 계산</mark>됩니다. 분모(주가)가 매일 바뀌기 때문에, 배당수익률도 배당금이 그대로여도 주가에 따라 매일 달라집니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당수익률과 시가배당률은 뭐가 다른가요</h2>

<p>둘 다 "주당배당금 ÷ 주가"라는 공식은 같지만, <b>어느 시점의 주가를 쓰는지가 다릅니다.</b> 이 기준일 차이 때문에 같은 종목인데 숫자가 서로 다르게 보이는 혼동이 자주 생깁니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">배당수익률</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시가배당률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">누가 주로 쓰나</td>
      <td style="border:1px solid #ddd;padding:8px;">증권사 앱·포털 화면</td>
      <td style="border:1px solid #ddd;padding:8px;">기업이 배당 공시에 기재</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기준 주가</td>
      <td style="border:1px solid #ddd;padding:8px;">오늘의 현재가</td>
      <td style="border:1px solid #ddd;padding:8px;">배당기준일(또는 배당결정일) 직전 1주일 평균가</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">값이 바뀌는지</td>
      <td style="border:1px solid #ddd;padding:8px;">주가에 따라 매일 변함</td>
      <td style="border:1px solid #ddd;padding:8px;">공시 시점에 한 번 고정</td>
    </tr>
  </tbody>
</table>

<p>예를 들어 배당 공시 당시 주가가 40,000원이고 연간 배당금이 2,000원이라면 <b>시가배당률은 5.0%로 공시</b>됩니다. 이후 주가가 50,000원으로 오르면 같은 배당금인데도 <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">오늘 화면에 뜨는 배당수익률은 4.0%(2,000 ÷ 50,000 × 100)로 더 낮게 표시</span>됩니다. 배당금이 줄어든 게 아니라 주가가 올라서 벌어진 차이입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">세금을 떼면 실제 수익률은 얼마나 낮아지나요</h2>

<p>화면에 뜨는 배당수익률은 <b>세금을 떼기 전(세전) 수치</b>입니다. 국내 배당소득은 15.4%(소득세 14%+지방소득세 1.4%)가 원천징수되므로, 실제로 계좌에 들어오는 금액을 기준으로 다시 계산하면 수익률은 더 낮아집니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주가 40,000원 · 연간 주당배당금</td>
      <td style="border:1px solid #ddd;padding:8px;">2,000원 (세전 배당수익률 5.0%)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">원천징수세액 (2,000원 × 15.4%)</td>
      <td style="border:1px solid #ddd;padding:8px;">308원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">세후 실수령 배당금</td>
      <td style="border:1px solid #ddd;padding:8px;">1,692원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;"><b>세후 실수령 수익률</b> (1,692 ÷ 40,000 × 100)</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>4.23%</mark></td>
    </tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>배당소득세 세율 자체가 궁금하다면</b>
  <p style="margin:8px 0 0 0;">배당소득 원천징수 15.4%의 근거 조문과 금융소득종합과세(2천만원 초과 시)까지 이어지는 내용은 <a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax" target="_blank" rel="noopener">이전 글(배당소득세 얼마 떼나)</a>에서 자세히 다룹니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당수익률이 높으면 무조건 좋은가요</h2>

<p><b>아닙니다. 배당수익률은 분모인 주가가 급락해도 똑같이 높아집니다.</b> 배당금(분자)이 늘어난 게 아니라 주가(분모)가 떨어져서 수익률 숫자만 커지는 경우를 구분해야 합니다.</p>

<ul style="line-height:1.9;">
  <li>배당수익률이 갑자기 크게 오른 게 <b>배당금 증가</b> 때문인지, <b>주가 하락</b> 때문인지 원인을 먼저 확인합니다.</li>
  <li>회사 실적이 나빠지는 중이라면 다음 배당이 줄어들거나 아예 없어지는 <b>배당컷</b> 가능성을 함께 고려합니다.</li>
  <li>과거 배당 실적은 미래 배당을 보장하지 않으므로, 한 해 수익률만으로 판단하지 않습니다.</li>
</ul>

<p>이 글은 배당수익률이라는 지표를 읽는 방법을 설명하는 것으로, 특정 종목의 매수·매도를 권하는 내용이 아닙니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당수익률이란 정확히 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">지금 주가로 주식을 살 때 배당금만으로 연간 몇 %의 수익을 얻을 수 있는지 나타내는 지표입니다. 주당배당금을 현재 주가로 나눈 뒤 100을 곱해 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당수익률은 어떻게 계산하나요</summary>
  <p style="margin:10px 0 0 0;">주당배당금 ÷ 현재 주가 × 100으로 계산합니다. 예를 들어 주가 40,000원에 연간 배당금이 2,000원이면 배당수익률은 5.0%입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당수익률과 시가배당률은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">기준 주가가 다릅니다. 배당수익률은 오늘의 현재가를 쓰고, 시가배당률은 기업이 공시 시점(배당기준일 직전 1주일 평균가)에 고정한 값을 씁니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">세금을 떼면 배당수익률이 얼마나 낮아지나요</summary>
  <p style="margin:10px 0 0 0;">배당소득세 15.4%를 반영하면 세전 5.0% 수익률이 세후로는 4.23%까지 낮아집니다. 화면에 뜨는 배당수익률은 세금을 떼기 전 수치이기 때문입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당수익률이 높으면 무조건 좋은 건가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 배당금이 늘어서가 아니라 주가가 급락해서 수익률 숫자만 높아지는 경우가 있습니다. 높아진 원인이 배당 증가인지 주가 하락인지부터 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당수익률은 어디서 확인할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">증권사 앱의 종목 정보 화면이나 한국거래소 정보데이터시스템에서 종목별 PER·PBR과 함께 확인할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://data.krx.co.kr/contents/MMC/ISIF/isif/MMCISIF002.cmd" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a> - PER·PBR·배당수익률 데이터(자동화 세션에서는 접속이 막혀 직접 확인하지 못함)</li>
    <li><a href="https://www.kbanker.co.kr/news/articleView.html?idxno=218431" target="_blank" rel="noopener">대한금융신문</a> - 시가배당률·배당수익률 계산 기준일 차이 보도</li>
    <li><a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax" target="_blank" rel="noopener">배당소득세 얼마 떼나(이전 글)</a> - 배당소득세 원천징수 15.4% 근거</li>
  </ul>
  기준일: 2026-09-17(WebSearch 확인일). 한국거래소 정보데이터시스템 원문은 이번 세션
  WebFetch가 차단돼 직접 열람하지 못했고, 정의·계산 기준은 언론사를 포함한 독립 출처
  5곳 이상이 일치하는 것으로 교차검증했습니다. 배당소득세 세율은 4편에서 법제처 원문으로
  이미 확정한 수치를 재사용했습니다.
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
  "headline": "배당수익률 계산법",
  "description": "배당수익률을 계산하는 공식과 시가배당률과의 차이, 배당소득세를 뗀 세후 실수령 수익률 계산 예시를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-17",
  "dateModified": "2026-09-17",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/dividend-yield-calculation"
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
      "name": "배당수익률이란 정확히 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "지금 주가로 주식을 살 때 배당금만으로 연간 몇 %의 수익을 얻을 수 있는지 나타내는 지표입니다. 주당배당금을 현재 주가로 나눈 뒤 100을 곱해 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "배당수익률은 어떻게 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "주당배당금 ÷ 현재 주가 × 100으로 계산합니다. 예를 들어 주가 40,000원에 연간 배당금이 2,000원이면 배당수익률은 5.0%입니다." }
    },
    {
      "@type": "Question",
      "name": "배당수익률과 시가배당률은 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "기준 주가가 다릅니다. 배당수익률은 오늘의 현재가를 쓰고, 시가배당률은 기업이 공시 시점(배당기준일 직전 1주일 평균가)에 고정한 값을 씁니다." }
    },
    {
      "@type": "Question",
      "name": "세금을 떼면 배당수익률이 얼마나 낮아지나요",
      "acceptedAnswer": { "@type": "Answer", "text": "배당소득세 15.4%를 반영하면 세전 5.0% 수익률이 세후로는 4.23%까지 낮아집니다. 화면에 뜨는 배당수익률은 세금을 떼기 전 수치이기 때문입니다." }
    },
    {
      "@type": "Question",
      "name": "배당수익률이 높으면 무조건 좋은 건가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 배당금이 늘어서가 아니라 주가가 급락해서 수익률 숫자만 높아지는 경우가 있습니다. 높아진 원인이 배당 증가인지 주가 하락인지부터 확인해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "배당수익률은 어디서 확인할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권사 앱의 종목 정보 화면이나 한국거래소 정보데이터시스템에서 종목별 PER·PBR과 함께 확인할 수 있습니다." }
    }
  ]
}
</script>
