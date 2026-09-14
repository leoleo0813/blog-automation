---
keyword: 공매도 과열종목 지정
title: 공매도 과열종목 지정 뜻과 확인법
slug: short-selling-overheated-stock
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 1040 (PC 150 / 모바일 890)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-14 — 통과]
  WebSearch "공매도 과열종목 지정 요건 지정 효과" + "공매도 과열종목 뜻 확인하는 법" 상위 종합:
  khan.co.kr(경향신문, 언론) / kbthink.com(KB, 대형금융사 사전) / kci.go.kr(학술논문 ×2) /
  kcmi.re.kr(자본시장연구원, 준정부 연구기관 이슈보고서) / opinionnews.co.kr(언론) /
  orangeboard.co.kr(개인 리포트 블로그) / aeditian.com(개인/소규모 콘텐츠 블로그) /
  data.krx.co.kr·kind.krx.co.kr(한국거래소, 공식)
  1) 진입 여지 — 있음. orangeboard.co.kr·aeditian.com 등 개인/소규모 콘텐츠가 상위에
     진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("무슨 뜻이고 어떤 효과가 있나"). data.krx.co.kr가 상위에
     있지만 목록 조회 페이지이지 계산기·신청 성격이 아니라 지배적 의도는 여전히
     정보 탐색이다.
  3) 답 완결 여부 — 아니다. 상위 글 대부분 "지정되면 다음날 하루 공매도가 금지된다"는
     효과까지만 다루고, 실제 지정 기준 수치(공매도비중·하락률·증가배율)를 시장별로
     정확히 정리한 글이 없다. 조사 중 WebSearch 요약마다 다른 수치가 나오는 것도
     확인해(아래 source_conflict_resolved 참조), 이 혼선을 원문으로 바로잡은 것 자체가
     정보이득이다.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-14 — 사람이 data.krx.co.kr 원문 직접 캡처]
  (a) 제도 도입 취지(공매도 급증·주가 급락 종목을 지정·공개해 투자자 주의 환기 +
      지정 익일 자동 공매도 거래 금지), 도입 시점(2016-11-10 금융위원회 신설),
      2022-10-24 시행된 연장 규정(공매도 금지일에 주가가 5% 이상 추가로 떨어지면
      금지 기간이 다음 거래일까지 자동 연장) — WebSearch 교차검증으로 확정.
  (b) 핵심 정보이득 — 시장별(코스피/코스닥/코넥스) 지정 기준을 한국거래소
      정보데이터시스템(data.krx.co.kr) 원문 표로 확정. WebSearch만으로는 서로 다른
      두 조합이 나와 혼선이 있었는데(source_conflict_resolved 참조), 원문 표는
      유형①②③④ 네 가지 조합으로 시장별 적용 여부가 갈린다는 것을 보여준다 —
      코스피·코스닥은 자체 지수(코스피/코스닥150) 구성종목 평균과 비교하는 유형①이
      있지만, 그런 지수가 없는 코넥스는 대신 "직전 40거래일 공매도비중 평균" 기준인
      유형③을 쓴다는 구조적 이유까지 원문 각주로 확인했다. 상위 검색 결과 어디에도
      이 정확한 시장별 표와 "왜 코넥스만 유형③을 쓰는지"의 구조는 없었다.
  (c) 2025년 3월 31일 공매도 전면 재개 직후 한시적으로 기준이 더 강화됐다가('25.3.31
      ~4.30, '25.5.1~5.31 두 단계로) '25.6.1부터 원래 기준으로 되돌아간 이력도
      원문 각주로 확정 — 최근 재개 국면의 변화 과정을 보여주는 정보이득.
  (d) 사람이 함께 캡처한 2026-09-10~11 실제 지정 종목 데이터(엑셀)로, 표에 나온
      유형 분류가 실제로 어떻게 적용되는지 예시 1건을 실었다(특정 종목 매수·매도
      권유 목적이 아니라 유형 판독 예시).
primary_source: |
  1차 시도: 한국거래소 정보데이터시스템 "공매도 과열종목 지정기준" 페이지에
  WebFetch를 1회 시도했으나 EGRESS_BLOCKED로 확인(2026-09-14, RULES.md에 이미
  기록된 패턴과 일치). WebSearch 교차검증만으로는 시장별 수치 조합이 서로 달라
  RULES.md 「1차 출처가 막혔을 때」 기준상 캡처 요청으로 전환했고, 사람이 직접
  브라우저로 data.krx.co.kr/contents/MDC/STAT/srt/MDCSTAT310.jsp에 접속해
  "공매도 과열종목 지정기준" 원문 표 전체(시장별 유형①②③④ 수치, 각주 1~7,
  2025년 한시 강화 이력)와 "당일 공매도 비중" 조회 화면을 캡처(2026-09-14),
  같은 화면에서 2026-09-10~11 실제 지정 종목 데이터를 엑셀로 내려받아 함께
  제공했다. 이 초안은 그 원문 캡처를 그대로 반영했다.
  보조로 사람이 함께 캡처한 clobe.ai(블로그) "코스피 코스닥 코넥스 차이와 상장
  요건 비교(2026년 기준)" 표는 18편에서 이미 인용한 상장요건과 수치가 일치해
  교차 확인용으로만 참고했다(이 글 본문에는 미사용).
기준일: 2026-09-14 (한국거래소 정보데이터시스템 원문 사람 캡처일)
tags: 공매도, 공매도과열종목, 과열종목지정, 공매도금지, 한국거래소, 시장경보제도, 공매도규제, 주식초보, 코스피, 코스닥
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-14). 게이트4는 자동화 WebFetch 1회 시도 후
  EGRESS_BLOCKED, WebSearch 교차검증도 수치 충돌로 기준 미달 → 사람이 직접
  data.krx.co.kr 원문을 캡처해 확정. 이번에도 "1차 출처가 막혔을 때" 기준대로
  안전한 쪽(캡처 요청)을 택한 뒤 실제 캡처로 게이트4를 완전히 충족시킨 사례.
self_check: |
  [2026-09-14 최종 판정 — 캡처 반영 후 gate_pass:true]
  게이트1 충족 — 실측 1,040회.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 시장별 정확한 지정 기준표 + "코넥스만 유형③을 쓰는 구조적 이유" +
  2025년 한시 강화 이력까지, 상위 검색 결과에 없는 정보이득을 원문 그대로 확보했다.
  게이트4 충족 — data.krx.co.kr 자동화 WebFetch 1회 시도 EGRESS_BLOCKED 확인 후,
  WebSearch 교차검증이 수치 충돌(source_conflict_resolved 참조)로 RULES.md 진행
  조건을 충족하지 못해 사람에게 캡처를 요청했고, 사람이 직접 브라우저로 원문 표
  전체와 각주, 실제 지정 종목 데이터(엑셀)까지 캡처해 제공했다. 자동화가 만든
  source_conflict 두 조합((A)비중30%·하락률3%·증가배율2배 시장구분없음, (B)비중
  20%(코스닥·코넥스15%)·하락률5%·증가배율100%이상)은 둘 다 원문과 다른 부정확한
  요약이었음을 원문으로 확인 — 실제로는 유형①②③④ 네 조합이 시장별로 다르게
  적용되는 구조였다. "애매하면 캡처 요청"이라는 RULES.md 원칙이 실제로 부정확한
  수치를 거를 수 있었던 사례.
  검산 — 원문 각주 2를 코스닥·코넥스 두 시장 라벨이 인접해 표시되는 원문 표
  레이아웃과 대조: 코스피·코스닥에는 자체 지수(코스피/코스닥150) 구성종목 평균과
  비교하는 유형①이 있고(코스닥150 언급이 원문에 명시), 그런 지수가 없는 코넥스는
  유형①이 아니라 유형③(직전40거래일 평균 비교)을 쓴다는 구조로 정리 — 코스피·
  코스닥은 유형①②④, 코넥스는 유형②③④를 적용하는 것으로 확정. 세 시장 모두
  유형④(당일 -3%하락+공매도비중30%+거래대금증가2배)는 공통 적용.
  카니벌라이제이션 점검 — 17편(공매도 뜻과 상환기간 90일)은 대차거래 상환기한·
  담보비율·NSDS·사전교육을 다루고, 27편(숏커버링 뜻과 공매도 잔고 확인법)은 순보유
  잔고 공시 제도를 다룬다. 이 글은 "공매도가 과도하게 몰린 종목을 시장이 어떻게
  경보·차단하는가"라는 별도의 시장경보제도를 다뤄 겹치지 않는다.
  기관 링크 점검 — 본문에서 안내하는 자리와 하단 참고 출처 전부 target="_blank"
  rel="noopener"로 링크 처리.
  제목 14자(공백 제외)·금지어 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 실제 지정 종목 예시는 유형 판독
  설명용일 뿐 매수·매도 권유가 아님을 본문에 명시. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
source_conflict_resolved: |
  자동화가 WebSearch만으로 찾았던 두 조합 (A) 비중30%·하락률3%·증가배율2배
  (시장구분없음) / (B) 비중20%(코스닥·코넥스15%)·하락률5%·증가배율100%이상은
  둘 다 한국거래소 원문과 다른 부정확한 요약이었다. 원문(2026-09-14 사람 캡처)
  기준 정확한 기준은 본문의 시장별 지정기준표를 참조.
---

<p>공매도 과열종목으로 지정되면 <mark>지정 다음 거래일 하루 동안 해당 종목의 공매도가 자동으로 금지</mark>됩니다. 공매도가 비정상적으로 몰리고 주가가 급락한 종목을 한국거래소가 골라내 투자자에게 알리는 시장경보제도입니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>공매도 과열종목으로 지정되면 <b>지정 다음 거래일 하루 동안 그 종목의 공매도가 자동 금지</b>됩니다.</li>
    <li>2016년 11월 금융위원회가 신설한 제도로, 공매도 급증·주가 급락 종목에 <mark>투자자의 주의를 환기</mark>시키는 목적입니다.</li>
    <li>2022년 10월 24일부터는 <b>금지일에 주가가 5% 이상 더 떨어지면 금지 기간이 다음 거래일까지 자동 연장</b>되는 규정이 추가됐습니다.</li>
    <li>지정 기준은 <mark>코스피·코스닥은 유형①②④, 코넥스는 유형②③④</mark>를 적용합니다. 세 시장 모두 유형④(당일 -3%↓·공매도비중30%·거래대금 2배↑)는 공통입니다.</li>
    <li>2025년 3월 공매도 재개 직후에는 한시적으로 기준이 더 엄격했다가, <b>2025년 6월 1일부터 원래 기준으로 돌아왔습니다.</b></li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>공매도 과열종목 지정이란 무엇인가요</li>
  <li>왜 이런 제도가 필요한가요</li>
  <li>지정되면 어떤 효과가 있나요</li>
  <li>정확히 어떤 기준으로 지정되나요</li>
  <li>지정 여부는 어디서 확인하나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">공매도 과열종목 지정이란 무엇인가요</h2>

<p>공매도 과열종목 지정제도는 <mark>공매도 거래가 비정상적으로 급증하고 주가가 크게 떨어진 종목을 한국거래소가 골라 공개하는 시장경보제도</mark>입니다. 2016년 11월 10일 금융위원회가 신설했습니다.</p>

<p>이름이 비슷한 "관리종목"이나 "투자경고종목"과는 다른 별개의 제도로, 오직 <b>공매도 쏠림 현상</b>만을 근거로 지정됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">왜 이런 제도가 필요한가요</h2>

<p>공매도 자체는 합법적인 투자 기법이지만, 특정 종목에 공매도가 짧은 시간에 몰리면 <mark>주가 하락을 가속시키는 요인</mark>이 될 수 있습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>제재가 아니라 경보입니다</b>
  <p style="margin:8px 0 0 0;">공매도 과열종목 지정은 해당 기업이나 투자자의 위법 행위를 처벌하는 것이 아닙니다. "공매도가 비정상적으로 몰리고 있다"는 사실을 시장에 알려, 투자자가 냉정하게 상황을 판단할 시간을 벌어주는 취지입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">지정되면 어떤 효과가 있나요</h2>

<p>공매도 과열종목으로 지정되면 <mark>지정된 날의 다음 거래일 하루 동안 해당 종목의 공매도 주문이 자동으로 금지</mark>됩니다. 별도의 신청이나 처분 절차 없이 시스템으로 즉시 적용됩니다.</p>

<ul style="line-height:1.9;">
  <li>지정 익일 하루 동안 공매도 금지</li>
  <li>공매도가 아닌 일반 매수·매도 주문은 평소대로 가능</li>
  <li>2022년 10월 24일 이후: 금지일에 주가가 <b>전일 대비 5% 이상 추가 하락</b>하면, 금지 기간이 다음 거래일까지 <mark>자동으로 하루 더 연장</mark>됩니다.</li>
</ul>

<p>제도 효과에 대한 평가는 엇갈립니다. 지정 이후 해당 종목의 주가 하락 폭이 줄었다는 분석이 있는 반면, 공매도는 원래 장기간에 걸쳐 이뤄지는 경우가 많아 <mark>하루짜리 금지로는 전체 흐름에 큰 영향을 주기 어렵다</mark>는 지적도 함께 나옵니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">정확히 어떤 기준으로 지정되나요</h2>

<p>지정 기준은 <mark>주가 하락률·공매도 비중·공매도 거래대금 증가배율</mark>을 조합한 4가지 유형(①~④)으로 나뉘고, 시장마다 적용되는 유형이 다릅니다. 한 종목이 유형을 하나라도 충족하면 지정됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시장</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">유형</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">주가(당일)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">공매도 비중</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">공매도 거래대금 증가배율</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;" rowspan="3">코스피</td><td style="border:1px solid #ddd;padding:8px;">①</td><td style="border:1px solid #ddd;padding:8px;">-5%~-10% 하락</td><td style="border:1px solid #ddd;padding:8px;">직전분기 코스피 구성종목 평균의 3배 이상(상한 20%)</td><td style="border:1px solid #ddd;padding:8px;">6배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">②</td><td style="border:1px solid #ddd;padding:8px;">-10% 이상 하락</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">6배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">④</td><td style="border:1px solid #ddd;padding:8px;">-3% 이상 하락</td><td style="border:1px solid #ddd;padding:8px;">당일 30% 이상</td><td style="border:1px solid #ddd;padding:8px;">2배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;" rowspan="2">코스닥</td><td style="border:1px solid #ddd;padding:8px;">①</td><td style="border:1px solid #ddd;padding:8px;">-5%~-10% 하락</td><td style="border:1px solid #ddd;padding:8px;">직전분기 코스닥150 구성종목 평균의 3배 이상(상한 20%)</td><td style="border:1px solid #ddd;padding:8px;">5배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">②</td><td style="border:1px solid #ddd;padding:8px;">-10% 이상 하락</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">5배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">코스닥·코넥스</td><td style="border:1px solid #ddd;padding:8px;">④</td><td style="border:1px solid #ddd;padding:8px;">-3% 이상 하락</td><td style="border:1px solid #ddd;padding:8px;">당일 30% 이상</td><td style="border:1px solid #ddd;padding:8px;">2배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;" rowspan="2">코넥스</td><td style="border:1px solid #ddd;padding:8px;">②</td><td style="border:1px solid #ddd;padding:8px;">-10% 이상 하락</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">5배 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">③</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">직전 40거래일 공매도비중 평균 5% 이상</td><td style="border:1px solid #ddd;padding:8px;">5배 이상</td></tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>왜 코넥스만 유형③을 쓰나요</b>
  <p style="margin:8px 0 0 0;">유형①은 "직전분기 코스피·코스닥150 구성종목 공매도 비중 평균"과 비교하는 방식인데, 코넥스는 이런 지수 자체가 없습니다. 그래서 코넥스는 유형① 대신 "직전 40거래일 자체 공매도 비중 평균"과 비교하는 유형③을 대신 씁니다. 유형④(당일 -3%↓·비중30%·2배↑)는 세 시장 모두 공통으로 적용됩니다.</p>
</div>

<p>직전 40거래일 중 실제 거래가 체결된 날이 20거래일 미만인 종목은 통계적 의미가 없어 지정 대상에서 제외됩니다. 여러 유형을 동시에 충족하면 <b>유형① &gt; 유형③·④, 유형② &gt; 유형③·④, 유형③ &gt; 유형④</b> 순으로 적용됩니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>2025년 재개 직후엔 기준이 더 엄격했습니다</b>
  <p style="margin:8px 0 0 0;">2025년 3월 31일 공매도가 전면 재개된 직후에는 한시적으로 기준이 더 강화됐습니다. 2025년 3월 31일~4월 30일에는 유형④의 공매도 비중 기준이 30%→20%로, 2025년 5월 1일~5월 31일에는 30%→25%로 낮춰 지정 문턱을 낮췄습니다. 2025년 6월 1일부터는 위 표의 원래 기준으로 돌아왔습니다.</p>
</div>

<h3 style="margin-top:28px;">실제 지정 사례로 보기</h3>

<p>2026년 9월 11일 지정 사례 중 하나를 표에 대입해보면 이렇습니다(특정 종목 매수·매도를 권유하는 것이 아니라, 표를 실제로 어떻게 읽는지 보여주는 예시입니다).</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시장</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">당일 주가수익률</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">공매도 거래대금 증가배율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">해당 유형</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">코스피</td><td style="border:1px solid #ddd;padding:8px;">-14.76%</td><td style="border:1px solid #ddd;padding:8px;">11.72배</td><td style="border:1px solid #ddd;padding:8px;">유형②(-10%↓ + 6배↑ 요건 충족)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">코스닥</td><td style="border:1px solid #ddd;padding:8px;">-7.15%, 공매도비중 34.76%</td><td style="border:1px solid #ddd;padding:8px;">2.06배</td><td style="border:1px solid #ddd;padding:8px;">유형④(-3%↓ + 비중30%↑ + 2배↑ 요건 충족)</td></tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">지정 여부는 어디서 확인하나요</h2>

<p>공매도 과열종목 지정 여부와 지정 기준은 <mark><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a></mark>에서 누구나 무료로 확인할 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">확인 항목</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">경로</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">오늘 지정된 종목 목록</td>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://data.krx.co.kr" target="_blank" rel="noopener">정보데이터시스템</a> → 통계 → 공매도통계 → 공매도 과열종목</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">개별 종목의 지정 이력·사유</td>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 기업공시채널(KIND)</a>에서 종목명으로 검색 후 "공매도 과열종목 지정" 공시 확인</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공매도 과열종목 지정이 뭔가요</summary>
  <p style="margin:10px 0 0 0;">공매도가 비정상적으로 급증하고 주가가 크게 떨어진 종목을 한국거래소가 골라 공개하는 시장경보제도로, 2016년 11월 금융위원회가 신설했습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">지정되면 어떤 불이익이 있나요</summary>
  <p style="margin:10px 0 0 0;">지정 다음 거래일 하루 동안 해당 종목의 공매도만 자동으로 금지됩니다. 일반 매수·매도 주문은 평소대로 가능하며, 기업이나 투자자에 대한 처벌이 아닙니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공매도 금지가 연장될 수도 있나요</summary>
  <p style="margin:10px 0 0 0;">네. 2022년 10월 24일부터, 금지일에 주가가 전일 대비 5% 이상 더 떨어지면 금지 기간이 다음 거래일까지 자동으로 하루 더 연장됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코스피와 코스닥의 지정 기준이 다른가요</summary>
  <p style="margin:10px 0 0 0;">네. 코스피·코스닥은 유형①②④가 적용되고, 코넥스는 유형①이 없는 대신 유형②③④가 적용됩니다. 세 시장 모두 유형④(당일 -3%↓·공매도비중30%·거래대금 2배↑)는 공통입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">지정 여부는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">한국거래소 정보데이터시스템(data.krx.co.kr)의 공매도통계 메뉴에서 당일 지정 종목 목록을 확인할 수 있고, 개별 종목의 지정 이력은 기업공시채널(KIND)에서 검색할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">과열종목 지정과 관리종목 지정은 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 공매도 과열종목 지정은 오직 공매도 쏠림 현상만을 근거로 하는 별개의 제도이며, 관리종목·투자경고종목 지정과는 지정 사유와 효과가 다릅니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a> — 공매도 과열종목 지정기준·실제 지정 현황(2026-09-14 사람 직접 캡처)</li>
    <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 기업공시채널(KIND)</a> — 공매도 과열종목 지정 공시</li>
  </ul>
  기준일: 2026-09-14(한국거래소 정보데이터시스템 원문 캡처일).
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
  "headline": "공매도 과열종목 지정 뜻과 확인법",
  "description": "공매도 과열종목 지정제도의 뜻, 지정 시 다음날 공매도가 자동 금지되는 효과, 2022년 연장 규정, 지정 여부를 한국거래소에서 직접 확인하는 방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-14",
  "dateModified": "2026-09-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/short-selling-overheated-stock"
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
      "name": "공매도 과열종목 지정이 뭔가요",
      "acceptedAnswer": { "@type": "Answer", "text": "공매도가 비정상적으로 급증하고 주가가 크게 떨어진 종목을 한국거래소가 골라 공개하는 시장경보제도로, 2016년 11월 금융위원회가 신설했습니다." }
    },
    {
      "@type": "Question",
      "name": "지정되면 어떤 불이익이 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "지정 다음 거래일 하루 동안 해당 종목의 공매도만 자동으로 금지됩니다. 일반 매수·매도 주문은 평소대로 가능하며, 기업이나 투자자에 대한 처벌이 아닙니다." }
    },
    {
      "@type": "Question",
      "name": "공매도 금지가 연장될 수도 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 2022년 10월 24일부터, 금지일에 주가가 전일 대비 5% 이상 더 떨어지면 금지 기간이 다음 거래일까지 자동으로 하루 더 연장됩니다." }
    },
    {
      "@type": "Question",
      "name": "코스피와 코스닥의 지정 기준이 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 코스피·코스닥은 유형①②④가 적용되고, 코넥스는 유형①이 없는 대신 유형②③④가 적용됩니다. 세 시장 모두 유형④(당일 -3%↓·공매도비중30%·거래대금 2배↑)는 공통입니다." }
    },
    {
      "@type": "Question",
      "name": "지정 여부는 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "한국거래소 정보데이터시스템(data.krx.co.kr)의 공매도통계 메뉴에서 당일 지정 종목 목록을 확인할 수 있고, 개별 종목의 지정 이력은 기업공시채널(KIND)에서 검색할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "과열종목 지정과 관리종목 지정은 같은 건가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 공매도 과열종목 지정은 오직 공매도 쏠림 현상만을 근거로 하는 별개의 제도이며, 관리종목·투자경고종목 지정과는 지정 사유와 효과가 다릅니다." }
    }
  ]
}
</script>
