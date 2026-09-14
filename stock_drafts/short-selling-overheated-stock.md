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
     정확히 정리한 글이 없다. 오히려 조사 중 자료마다 다른 수치가 나오는 것을
     확인해(아래 source_conflict), 이 혼선 자체를 원문으로 바로잡는 것이 정보이득이다.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [부분 완성 — 시장별 지정기준 수치표는 캡처 대기]
  (a) 확정 반영: 제도 도입 취지(공매도 급증·주가 급락 종목을 지정·공개해 투자자 주의
      환기 + 지정 익일 자동 공매도 거래 금지), 도입 시점(2016-11-10 금융위원회 신설),
      2022-10-24 시행된 연장 규정(공매도 금지일 또는 금지 연장일에 주가가 5% 이상
      추가로 떨어지면 금지 기간이 다음 거래일까지 자동 연장) — 4개 이상 독립 출처가
      충돌 없이 일치.
  (b) 캡처 대기: 실제 지정 기준(당일 공매도 비중·전일 대비 하락률·공매도 거래대금
      증가배율)을 코스피·코스닥·코넥스 시장별로 찾아보면 서로 다른 두 조합이 검색된다
      — 하나는 "비중 30%·하락률 3%·증가배율 2배"(시장 구분 없음), 다른 하나는
      "비중 20%(코스닥·코넥스는 15%)·하락률 5%·증가배율 100% 이상 증가"다. 전자는
      2017년 무렵 언론 기사에서, 후자는 비교적 최근 요약에서 확인돼 개정 이력에
      따른 신구 수치가 섞였을 가능성이 있으나, 한국거래소 원문을 직접 대조하기
      전까지는 어느 쪽이 현재(2026-09) 유효한 기준인지 자동화가 확정할 수 없다.
      이 혼선을 원문으로 정리해 시장별 정확한 표를 완성하는 것 자체가 상위 글에
      없는 정보이득이다.
  (c) 지정 종목을 한국거래소 정보데이터시스템(data.krx.co.kr)에서 직접 조회하는
      절차 — 상위 글 다수가 "거래소에서 확인 가능"이라고만 쓰고 구체적인 메뉴
      경로를 안내하지 않는다.
primary_source: |
  1차 시도: 한국거래소 정보데이터시스템의 "공매도 과열종목 지정기준" 페이지
  (data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC02030402)에
  WebFetch를 1회 시도했으나 EGRESS_BLOCKED로 확인(2026-09-14). 대조군으로
  금융위원회(fsc.go.kr) 보도자료, 자본시장연구원(kcmi.re.kr) 이슈보고서 PDF,
  kbthink.com(무관 도메인 성격 확인용)에도 각 1회씩 추가 시도했으나 전부 동일하게
  EGRESS_BLOCKED — 이 세션의 기존 전면 차단 패턴과 일치(구글 대조군도 동일 증상
  재확인).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12)
  기준 적용 — 제도의 도입 취지·효과·2022년 연장 규정은 4개 이상 독립 출처(언론·
  준정부 연구기관·학술논문 포함)가 충돌 없이 일치해 교차검증으로 확정했다. 그러나
  이 글의 핵심이 될 시장별 지정 기준 수치표는 검색 결과 자체가 서로 다른 두 조합을
  내놓아(source_conflict 참조) RULES.md의 교차검증 진행 조건("충돌 없이 일치")을
  충족하지 못했다. 시장 미시구조 규제 수치이긴 하지만 이 프로젝트가 과거 세율·
  공제한도에서 실제 오류를 잡아낸 사례(대주주 기준 5배 차이, 코스피 세율 4배 차이)와
  같은 성격의 "수치 충돌"이라 안전한 쪽(사람 캡처 요청)으로 판단했다.
source_conflict: |
  공매도 과열종목 지정 기준 수치가 WebSearch에서 서로 다른 두 조합으로 나왔다.
  (A) 당일 전체 거래대금 대비 공매도 거래대금 비중 30% 이상 / 주가 하락률(전일 대비)
      3% 이상 / 공매도 거래대금 증가 배율 2배 이상 — 시장 구분 없이 코스피·코스닥·
      코넥스에 동일 적용.
  (B) 당일 공매도 비중 20% 이상(코스닥·코넥스는 15% 이상) / 직전 40거래일 평균 대비
      공매도 비중 증가율 100% 이상(=2배) / 전일 종가 대비 주가 하락률 5% 이상.
  (A)는 2017년 무렵 언론 보도·일부 요약 콘텐츠에서, (B)는 비교적 최근 요약과
  자본시장연구원 이슈보고서 인용에서 확인돼, 2017년 이후 개정으로 (A)에서 (B)로
  강화·변경됐을 가능성이 있다고 추정되나 한국거래소 원문(공매도 과열종목 지정 및
  매매거래 정지 등에 관한 규정)을 직접 대조하기 전까지는 확정하지 않는다. 확정
  전에는 본문에 시장별 수치를 넣지 않는다.
기준일: 2026-09-14 (WebSearch 확인일 — 확정 원문은 사람 캡처 대기)
tags: 공매도, 공매도과열종목, 과열종목지정, 공매도금지, 한국거래소, 시장경보제도, 공매도규제, 주식초보, 코스피, 코스닥
gate_pass: false
gate_pass_note: |
  게이트1·2 충족, 게이트3(정보이득)은 방향이 확정됐으나 핵심 수치표가 캡처 대기,
  게이트4 미충족 — 시장별 지정 기준 수치가 WebSearch 결과마다 다른 두 조합으로
  나와(source_conflict 참조) 원문 없이는 자동화가 확정할 수 없다. RULES.md
  「1차 출처가 막혔을 때」 기준의 "출처마다 수치가 다르다" 조건에 해당해 캡처
  요청으로 전환했다. gate_pass:false로 두고 발행 대기 상태로 저장.
capture_guide: |
  (1) 왜 필요한가 — 공매도 과열종목 지정 기준 수치(공매도 비중·주가 하락률·거래대금
  증가배율)가 검색마다 다른 두 조합으로 나온다(비중 30%·하락률 3%·증가배율 2배 vs
  비중 20%/코스닥 15%·하락률 5%·증가배율 100% 이상). 어느 쪽이 2026년 9월 현재
  유효한 기준인지, 코스피·코스닥·코넥스 시장별로 정확히 어떻게 다른지 원문 확인이
  필요하다.
  (2) 시도할 사이트 (우선순위)
    1순위 — 한국거래소 정보데이터시스템 "공매도 과열종목 지정기준" 페이지:
      https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC02030402
      접속 → 시장별(코스피/코스닥/코넥스) 지정기준 표 전체를 캡처.
    2순위 — 같은 사이트의 "공매도 과열종목" 통계 화면(실제 지정 종목 목록과 지정
      사유가 함께 표시되는지 확인):
      https://data.krx.co.kr/contents/MMC/SRTS/srts/MMCSRTS007.cmd
    3순위 — 금융위원회에서 "공매도 과열종목" 검색 후 가장 최근 지정기준 개정
      보도자료 캡처: https://www.fsc.go.kr (검색창에 "공매도 과열종목" 입력)
  (3) 캡처가 끝나면 — 스크린샷을 대화에 올려주세요. 시장별 정확한 지정 기준표를
  확정해 본문에 반영하고 gate_pass를 재판정합니다.
self_check: |
  [2026-09-14 판정 — gate_pass:false로 저장]
  게이트1 충족 — 신규 후보 8개(자사주 처분 신고/실권주 청약 방법/우회상장 뜻/
  매매거래정지 해제 조건/공매도 과열종목 지정/주식배당 뜻/ETF 유동성공급자/감자 뜻)
  중 "공매도 과열종목 지정"(1,040회)과 "감자 뜻"(530회) 2개만 PASS, 나머지 6개는
  월 20~150회로 FAIL(backlog.failed_gate1에 기록). 이 중 검색량이 더 높은 "공매도
  과열종목 지정"을 이번 편으로 선택.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 부분 충족 — 제도 취지·효과·2022년 연장 규정은 확정해 본문에 반영했다.
  다만 이 글의 핵심이 되어야 할 "시장별 정확한 지정 기준 수치"는 확정되지 않아
  아직 표로 완성할 수 없다.
  게이트4 미충족 — data.krx.co.kr·fsc.go.kr·kcmi.re.kr에 WebFetch를 각 1회씩
  시도해 전부 EGRESS_BLOCKED 확인(2026-09-14, google.com 대조군도 동일 차단되어
  세션 전면 차단으로 판단). WebSearch 교차검증을 시도했으나 지정 기준 수치 자체가
  서로 다른 두 조합으로 나와(source_conflict) RULES.md의 교차검증 진행 조건
  (충돌 없이 일치)을 충족하지 못했다. 시장 미시구조 규제 수치이지만 이 프로젝트가
  과거 세율·공제한도에서 실제 오류를 잡아낸 유형과 같은 "수치 충돌"이라 애매하면
  안전한 쪽(사람 캡처 요청)으로 기운다는 RULES.md 원칙에 따라 캡처로 전환했다.
  카니벌라이제이션 점검 — 17편(공매도 뜻과 상환기간 90일)은 대차거래 상환기한·
  담보비율·NSDS·사전교육을 다루고, 27편(숏커버링 뜻과 공매도 잔고 확인법)은 순보유
  잔고 공시 제도를 다룬다. 이 글은 "공매도가 과도하게 몰린 종목을 시장이 어떻게
  경보·차단하는가"라는 별도의 시장경보제도를 다뤄 검색 의도와 본문 내용이 겹치지
  않는다. 1~27편 어디에도 공매도 과열종목 지정제도는 다루지 않는다.
  기관 링크 점검 — 본문에서 안내하는 자리와 하단 참고 출처 전부 target="_blank"
  rel="noopener"로 링크 처리.
  제목 14자(공백 제외)·금지어 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음.
  하단 면책 문구 포함. 지정기준 표는 뼈대만 두고 값은 비워 수치를 지어내지 않았다.
  종합 판정: 게이트4 미충족으로 gate_pass:false. 캡처 후 재판정 필요.
---

<p>공매도 과열종목으로 지정되면 <mark>지정 다음 거래일 하루 동안 해당 종목의 공매도가 자동으로 금지</mark>됩니다. 공매도가 비정상적으로 몰리고 주가가 급락한 종목을 한국거래소가 골라내 투자자에게 알리는 시장경보제도입니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>공매도 과열종목으로 지정되면 <b>지정 다음 거래일 하루 동안 그 종목의 공매도가 자동 금지</b>됩니다.</li>
    <li>2016년 11월 금융위원회가 신설한 제도로, 공매도 급증·주가 급락 종목에 <mark>투자자의 주의를 환기</mark>시키는 목적입니다.</li>
    <li>2022년 10월 24일부터는 <b>금지일에 주가가 5% 이상 더 떨어지면 금지 기간이 다음 거래일까지 자동 연장</b>되는 규정이 추가됐습니다.</li>
    <li>정확한 시장별(코스피·코스닥·코넥스) 지정 기준 수치는 자료마다 다르게 나와 원문 확인 중이며, 확정되는 대로 이 글에 반영합니다.</li>
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

<p>지정 기준은 크게 <mark>당일 공매도 비중, 전일 대비 주가 하락률, 평소 대비 공매도 거래대금 증가 배율</mark> 세 가지를 조합해 판단하며, 코스피·코스닥·코넥스 시장별로 기준이 다릅니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>시장별 정확한 수치는 원문 확인 중입니다</b>
  <p style="margin:8px 0 0 0;">조사 과정에서 지정 기준 수치가 자료마다 다르게 나오는 것을 확인했습니다(하나는 공매도 비중 30%·하락률 3%, 다른 하나는 코스피 20%·코스닥 15%·하락률 5%). 한국거래소의 정확한 원문을 직접 대조하기 전까지는 부정확한 숫자를 이 글에 표기하지 않습니다. 원문이 확인되는 대로 아래 표를 채워 갱신하겠습니다.</p>
</div>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시장</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">공매도 비중</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">주가 하락률</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">공매도 거래대금 증가배율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스피</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스닥</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코넥스</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
    </tr>
  </tbody>
</table>

<p>세 가지 조건을 <b>모두 충족</b>해야 지정되는 구조이며, 직전 40거래일 중 거래가 체결된 날이 20일 미만으로 드문 종목은 통계적 의미가 없어 지정 대상에서 빠집니다.</p>

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
  <p style="margin:10px 0 0 0;">네, 시장별로 기준이 다르게 적용됩니다. 다만 정확한 수치는 자료마다 다르게 검색돼 한국거래소 원문 확인 후 이 글에 표로 반영할 예정입니다.</p>
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
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템 — 공매도 과열종목·지정기준</a></li>
    <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 기업공시채널(KIND) — 공매도 과열종목 지정 공시</a></li>
  </ul>
  기준일: 2026-09-14(WebSearch 확인일). 시장별 정확한 지정 기준 수치는 원문 캡처 확인 후 갱신 예정.
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
      "acceptedAnswer": { "@type": "Answer", "text": "네, 시장별로 기준이 다르게 적용됩니다. 다만 정확한 수치는 자료마다 다르게 검색돼 한국거래소 원문 확인 후 이 글에 표로 반영할 예정입니다." }
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
