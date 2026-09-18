---
keyword: 퇴직연금 실물이전
title: 퇴직연금 실물이전 대상 상품과 신청 방법
slug: retirement-pension-in-kind-transfer
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 250 (PC 120 / 모바일 130)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-16 — 통과]
  WebSearch "퇴직연금 실물이전 제도 방법" + "퇴직연금 실물이전 사전조회 서비스 신청 방법" +
  "금융감독원 퇴직연금 실물이전 개선 TF" 상위 종합:
  newspim.com(언론) / kbthink.com(KB, 공식) / moel.go.kr(고용노동부, 공식) /
  eiec.kdi.re.kr(KDI 경제교육정보센터, 준정부) / easyzetec.com(개인·소규모 재테크 블로그) /
  cbilder.com(개인 블로그) / imaeil.com·dt.co.kr·sankyungtoday.com·sidae.com·khan.co.kr·
  sedaily.com·heraldcorp.com·viva100.com·intn.co.kr(언론 다수) / kiri.or.kr(보험연구원,
  준정부 연구기관) / kbstar.com(KB, 공식)
  1) 진입 여지 — 있음. easyzetec.com·cbilder.com 같은 개인·소규모 재테크 블로그가
     "총정리"류 콘텐츠로 상위권에 진입해 있어 SERP가 잠겨 있지 않음.
  2) 검색 의도 — 정보 탐색+절차 확인("무엇이 가능하고 어떻게 신청하나"). 조회·계산기
     실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 "실물이전 제도가 있다"는 개념과 사전조회
     서비스 신청법까지는 다루지만, (a) 2026-08 금융감독원 TF 킥오프 이후 DC→타사 IRP
     확대 추진 상황과 목표 시점(2027년까지 정비), (b) 2024-10-31 도입 후 2026-06월말
     기준 누적 실물이전 금액·건수를 제도별(IRP/DC/DB)로 나눈 통계, (c) 이전 가능 상품
     유형과 이전 불가(환매중단펀드 등) 상품을 한 표로 정리한 콘텐츠는 찾지 못했다.
     정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  상위 글들이 다루지 않는 두 가지를 통합했다.
  (1) 2024-10-31 서비스 도입 후 2026년 6월 말까지 누적 실물이전 15조 9,000억원(25만여건)을
      제도별로 나눈 실측 통계표(IRP 6조 8,000억원 / DC형 4조 8,000억원 / DB형 4조 3,000억원 —
      세 금액의 합이 총액과 정확히 일치함을 직접 검산).
  (2) "지금 되는 것"과 "2027년까지 확대될 것"을 분리한 표 — 현재는 DB→DB·DC→DC·IRP→IRP
      등 동일 제도 간에만, 그것도 수관회사가 취급하는 상품(원리금보장상품·공모펀드(MMF
      제외)·채무증권·ETF)만 가능하고, DC→타사 IRP와 환매중단펀드는 2026-08 금융감독원 TF
      킥오프 이후 논의 중인 확대 대상이라는 점을 상위 글들처럼 뭉뚱그리지 않고 시점별로 나눴다.
primary_source: |
  1차 시도: 고용노동부 보도자료(moel.go.kr, news_seq=17141) WebFetch 1회 시도 →
  EGRESS_BLOCKED(2026-09-16). 대조군 www.google.com도 동일하게 EGRESS_BLOCKED로 확인돼
  세션 전면 차단으로 판단(RULES.md에 누적 기록된 기존 패턴과 일치).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12) 기준
  적용 — 세율·공제한도·과세표준처럼 과거 오류가 발견된 숫자 유형이 아니라 제도 시행일·
  통계·절차 같은 검증 가능한 사실관계이므로 교차검증으로 진행했다.
  ① 실물이전 제도 개요(2024-10-31 도입, 동일 제도 간에만 가능, DC→타사 IRP 불가,
     환매중단펀드 제한)는 moel.go.kr(고용노동부, 공식) / kbthink.com(KB, 공식) /
     eiec.kdi.re.kr(KDI 경제교육정보센터, 준정부) 3곳 이상이 동일하게 설명해 충돌 없음.
  ② 사전조회 서비스(2025-07-21 시행, 이관회사 신청 → 대상회사 전송 → 익영업일까지
     결과 통보, 대상 상품 유형)는 khan.co.kr(경향신문)·sedaily.com(서울경제)·
     heraldcorp.com(헤럴드경제)·viva100.com(브릿지경제)·intn.co.kr(일간NTN) 등 언론 5곳과
     kiri.or.kr(보험연구원, 준정부 연구기관 위클리트렌드 PDF)가 동일 날짜·절차로 수렴했다.
  ③ 2026-08 금융감독원 TF 킥오프와 확대 계획(DC→IRP, 환매중단펀드 포함 검토, 10월 전산
     개발 착수, 2027년까지 정비 완료 목표), 누적 실물이전 통계(15조 9,000억원·25만여건,
     제도별 IRP 6.8조/DC 4.8조/DB 4.3조)는 newspim.com·imaeil.com(매일신문)·dt.co.kr
     (디지털타임스)·sankyungtoday.com(산경투데이)·sidae.com 5개 언론이 동일 수치로
     일치했고, 세 제도별 금액의 합이 총액과 정확히 맞아 내적 정합성도 확인했다.
  세 갈래 모두 서로 무관한 독립 출처가 3곳 이상이고 핵심 사실(날짜·금액·절차)이 충돌
  없이 일치해 교차검증으로 진행했다. 고용노동부·금융감독원 원문 보도자료를 이번
  세션에서 직접 열람하지 못한 한계는 self_check에 투명 공개한다.
기준일: 2026-09-16 (WebSearch 확인일. 사전조회 서비스 시행일 2025-07-21, 통계 기준일
  2026년 6월 말, TF 킥오프 2026년 8월)
tags: 퇴직연금, 퇴직연금실물이전, IRP, DC형퇴직연금, DB형퇴직연금, 연금계좌이전, 사전조회서비스, 금융감독원, 주식초보, 연금저축
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-16).
  게이트1: 네이버 키워드도구 실측 250회(check-keywords.yml, 2026-09-16 — 세부·제도
  기준 100회 이상). 함께 확인한 금 ETF 세금(210회)도 PASS — backlog에 다음 편 후보로
  기록. 우리사주 세금·IRP 계좌 수수료·미성년자 주식 증여세·해외주식 소수단위 매매
  세금·K-OTC 세금·펀드 환매수수료는 20~50회로 게이트1 미달.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 재테크 블로그 진입 여지 있고,
  2026-08 TF 확대 계획·누적 통계·상품유형별 가능여부를 통합한 콘텐츠 부재로 정보이득
  여지 뚜렷.
  게이트3: 제도별 누적 이전 통계표(내적 정합성 검산 완료) + "지금 되는 것 vs 2027년까지
  확대될 것" 시점 분리표로 정보이득 확보.
  게이트4: moel.go.kr WebFetch 1회 시도 EGRESS_BLOCKED 확인(google.com 대조군도 차단,
  세션 전면 차단) 후 RULES.md 2026-09-12 기준에 따라 세 갈래 모두 3곳 이상 독립 출처
  교차검증(제도 개요 3곳, 사전조회 절차 6곳, TF·통계 5곳)으로 진행, 충돌 없음 확인.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 250회(제도 세부 키워드 기준 100회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 제도별 누적 이전 통계(2024-10-31 도입~2026-06월말 15조 9,000억원,
  25만여건)와 "지금 되는 것 vs 확대 예정" 시점 분리표가 핵심 정보이득.
  게이트4 — moel.go.kr 직접 열람 실패, google.com 대조군도 차단되어 세션 전면 차단으로
  판단. 제도 개요·사전조회 절차·TF 확대계획·통계 세 갈래 모두 서로 무관한 독립 출처
  3곳 이상(언론·KB 공식·KDI/보험연구원 등 준정부 연구기관 포함)이 충돌 없이 일치함을
  확인해 캡처 요청 없이 진행했다.
  검산 — IRP 6조 8,000억원 + DC형 4조 8,000억원 + DB형 4조 3,000억원 = 15조 9,000억원.
  기사에서 밝힌 총액과 정확히 일치해 세 출처(언론 3곳 이상)가 같은 자료를 인용하고
  있음을 교차확인했다.
  카니벌라이제이션 점검 — 3편(ISA 계좌 한도와 비과세 혜택)은 ISA 계좌의 납입한도·
  비과세혜택을 다루고, 8편(연금저축 세액공제)은 연금저축의 세액공제율을 다룬다. 이
  글은 퇴직연금 계좌를 "다른 금융사로 옮기는 절차와 대상 상품"이 중심이라 두 편과
  검색 의도가 겹치지 않는다. 본문에서 8편으로 내부 링크를 건다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 고용노동부·금융감독원을
  안내하는 자리와 하단 참고 출처 목록 전부 target="_blank" rel="noopener"로 링크
  처리, 공공기관 링크에 nofollow 미부착. 출처 URL은 WebSearch로 실제 확인된 주소만
  사용했다(지어내지 않음).
  제목 "퇴직연금 실물이전 대상 상품과 신청 방법" 22자(공백 포함)·금지어 없음.
  "상품과"의 "과"는 RULES.md 제목 패턴표의 "{제도명} 조건과 한도"와 같은 명사 나열
  용법으로 기존 관행(3편·26편·36편 등)과 일치.
  슬러그 영문 소문자+하이픈 5단어(retirement-pension-in-kind-transfer). 인트로 문단
  최상단 배치. 표는 thead/tbody 시맨틱 사용. 본문의 모든 수치가 WebSearch로 확인한
  2차 출처 교차검증값이며 원문 조회가 불가능한 한계를 본문에도 명시했다. 기준일
  명시. FAQ 6개와 JSON-LD 1:1 일치. 종목·상품 추천 표현, 단정 표현 없음. 하단 면책
  문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 3개 사실관계 갈래 모두 독립 출처 교차검증
  으로 대체, 한계 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-16</p>

<p><mark>퇴직연금 실물이전은 보유한 상품을 팔지 않고 계좌만 다른 금융사로 옮기는 서비스</mark>입니다. 다만 지금은 DB→DB, DC→DC, IRP→IRP처럼 같은 제도 사이에서만 되고, 옮길 수 있는 상품 종류도 정해져 있습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>실물이전은 2024년 10월 31일부터 시행 중이며, <b>같은 제도 간(DB→DB, DC→DC, IRP→IRP)</b>에만 가능합니다.</li>
    <li>원리금보장상품·공모펀드(MMF 제외)·채무증권·ETF는 실물이전 대상이지만, <b>환매중단펀드는 아직 안 됩니다.</b></li>
    <li>이전 전에 <b>사전조회 서비스</b>로 실물이전 가능 여부를 미리 확인할 수 있습니다.</li>
    <li>2026년 6월 말까지 누적 <mark>15조 9,000억원(25만여건)</mark>이 실물이전됐고, DC→타사 IRP 확대는 2027년까지 추진 중입니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>퇴직연금 실물이전이 무엇인가요</li>
  <li>지금 실물이전 할 수 있는 상품은 무엇인가요</li>
  <li>DB DC IRP 사이 어떤 조합이 안 되나요</li>
  <li>사전조회 서비스는 어떻게 신청하나요</li>
  <li>실제로 얼마나 이용했나요</li>
  <li>2027년까지 무엇이 바뀌나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">퇴직연금 실물이전이 무엇인가요</h2>

<p>퇴직연금 실물이전은 <b>보유하고 있는 펀드·ETF 같은 상품을 매도하거나 해지하지 않고</b>, 퇴직연금을 운용하는 금융회사(사업자)만 바꾸는 서비스입니다. <a href="https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=17141" target="_blank" rel="noopener">고용노동부</a>에 따르면 2024년 10월 31일부터 시행됐습니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">기존에는 계좌를 옮기려면 상품을 전부 현금화한 뒤 다시 사야 해서, 매도 시점의 손실이나 재매수 공백이 생기는 문제가 있었습니다.</span> 실물이전은 이 과정 없이 상품 그대로 새 회사 계좌로 넘어갑니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">지금 실물이전 할 수 있는 상품은 무엇인가요</h2>

<p>모든 상품이 실물로 옮겨지는 것은 아닙니다. 옮기려는 회사(수관회사)가 해당 상품을 취급하는 경우에만 실물이전이 되고, 그렇지 않으면 예전처럼 현금화해서 옮겨야 합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">상품 유형</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">실물이전 가능 여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">원리금보장상품(예금, GIC, ELB·DLB 등)</td>
      <td style="border:1px solid #ddd;padding:8px;">가능(수관회사 취급 시)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">공모펀드(MMF 제외)</td>
      <td style="border:1px solid #ddd;padding:8px;">가능(수관회사 취급 시)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">채무증권</td>
      <td style="border:1px solid #ddd;padding:8px;">가능(수관회사 취급 시)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">ETF</td>
      <td style="border:1px solid #ddd;padding:8px;">가능(수관회사 취급 시)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">MMF</td>
      <td style="border:1px solid #ddd;padding:8px;">불가: 현금화 후 이전</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">환매중단펀드</td>
      <td style="border:1px solid #ddd;padding:8px;">불가(포함 여부 논의 중)</td>
    </tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>수관회사가 취급하지 않으면 실물이전이 안 됩니다</b>
  <p style="margin:8px 0 0 0;">같은 표에 있는 상품이라도, 옮기려는 회사가 그 상품을 팔지 않으면 실물로는 못 옮기고 현금화해야 합니다. 신청 전에 반드시 다음 항목의 사전조회로 확인해야 하는 이유입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">DB DC IRP 사이 어떤 조합이 안 되나요</h2>

<p>실물이전은 <b>같은 퇴직연금 제도 사이에서만</b> 가능합니다. 확정급여형(DB)은 DB끼리, 확정기여형(DC)은 DC끼리, 개인형퇴직연금(IRP)은 IRP끼리만 실물로 옮길 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>DB → 다른 회사 DB: 가능</li>
  <li>DC → 다른 회사 DC: 가능</li>
  <li>IRP → 다른 회사 IRP: 가능</li>
  <li>DC → 다른 회사 IRP: <b>현재는 불가</b>(2027년까지 확대 추진 중)</li>
</ul>

<p>퇴사·이직으로 DC형 퇴직금을 받아 IRP로 옮기는 경우가 많은데, 지금은 이 구간에서 실물이전이 되지 않아 상품을 팔고 다시 사야 합니다. 관련 세액공제는 <a href="https://sensitiveboss3.tistory.com/entry/pension-savings-tax-credit" target="_blank" rel="noopener">이전 글(연금저축 세액공제 얼마 돌려받나)</a>에서 다뤘습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">사전조회 서비스는 어떻게 신청하나요</h2>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">2025년 7월 21일부터 사전조회 서비스가 시작돼, 계좌를 새로 만들지 않고도 실물이전 가능 여부를 미리 확인</span>할 수 있게 됐습니다. 신청 취소로 번거로웠던 문제를 줄이기 위해 도입됐습니다.</p>

<ol style="line-height:1.9;">
  <li>지금 가입한 회사(이관회사)의 홈페이지·앱에서 실물이전 사전조회 메뉴로 신청</li>
  <li>옮기려는 회사(조회 대상 회사)를 지정</li>
  <li>이관회사가 보유 상품 목록을 대상 회사에 전송해 가능 여부 조회</li>
  <li>신청한 날의 <b>다음 영업일까지</b> 조회 결과 통보</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제로 얼마나 이용했나요</h2>

<p>2024년 10월 31일 도입 후 <mark>2026년 6월 말까지 누적 실물이전 금액은 15조 9,000억원(25만여건)</mark>입니다. 제도별로 나누면 다음과 같습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">제도</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">누적 실물이전 금액(2026년 6월 말 기준)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">IRP</td>
      <td style="border:1px solid #ddd;padding:8px;">6조 8,000억원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">DC형</td>
      <td style="border:1px solid #ddd;padding:8px;">4조 8,000억원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">DB형</td>
      <td style="border:1px solid #ddd;padding:8px;">4조 3,000억원</td>
    </tr>
  </tbody>
</table>

<p>세 금액을 더하면 15조 9,000억원으로, 전체 누적 금액과 정확히 일치합니다. IRP 계좌 이동이 가장 활발했습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2027년까지 무엇이 바뀌나요</h2>

<p>2026년 8월, 금융감독원은 예탁결제원·금융투자협회·한국증권금융·주요 퇴직연금 사업자 등 17개 기관과 <b>퇴직연금 실물이전 개선 태스크포스(TF)</b>를 꾸려 개선 방안을 논의하기 시작했습니다.</p>

<ul style="line-height:1.9;">
  <li>DC형 계좌 상품을 매도 없이 <b>다른 회사 IRP로 직접 실물이전</b>할 수 있도록 전산 시스템 개발 추진</li>
  <li><b>환매중단펀드</b>도 실물이전 대상에 포함하는 방안 검토</li>
  <li>2026년 10월부터 전산 개발 착수, <b>2027년까지 제도 정비 완료</b> 목표</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>아직 확정된 시행일이 아닙니다</b>
  <p style="margin:8px 0 0 0;">위 계획은 2026년 9월 기준 추진·검토 단계입니다. DC→IRP 실물이전이 실제로 언제부터 가능해지는지는 <a href="https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=17141" target="_blank" rel="noopener">고용노동부</a>·금융감독원 공지를 확인해야 합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">퇴직연금 실물이전이 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">보유한 상품을 팔지 않고 퇴직연금을 운용하는 금융회사만 바꾸는 서비스로, 2024년 10월 31일부터 시행 중입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">지금 당장 실물이전 할 수 있는 상품은 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">원리금보장상품, 공모펀드(MMF 제외), 채무증권, ETF는 수관회사가 취급하면 실물이전이 가능합니다. MMF와 환매중단펀드는 현재 대상이 아닙니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">DC형 계좌를 다른 회사 IRP로 실물이전할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아직 안 됩니다. 실물이전은 DB→DB, DC→DC, IRP→IRP처럼 같은 제도 사이에서만 가능하고, DC→타사 IRP는 2027년까지 확대가 추진되고 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">사전조회 서비스는 어떻게 신청하나요</summary>
  <p style="margin:10px 0 0 0;">지금 가입한 회사의 홈페이지나 앱에서 옮기려는 회사를 지정해 신청하면, 신청일 다음 영업일까지 실물이전 가능 여부를 알려줍니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">실물이전을 실제로 얼마나 이용했나요</summary>
  <p style="margin:10px 0 0 0;">2024년 10월 31일 도입 후 2026년 6월 말까지 누적 15조 9,000억원(25만여건)이 이전됐고, IRP 6조 8,000억원, DC형 4조 8,000억원, DB형 4조 3,000억원 순입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">앞으로 언제부터 DC에서 타사 IRP로 실물이전이 가능해지나요</summary>
  <p style="margin:10px 0 0 0;">확정된 시행일은 아직 없습니다. 금융감독원은 2026년 10월부터 전산 개발에 착수해 2027년까지 제도 정비를 완료한다는 목표를 밝혔습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=17141" target="_blank" rel="noopener">고용노동부 - 보유 상품 그대로 다른 금융사로 옮길 수 있는 '퇴직연금 실물이전' 안내</a></li>
    <li><a href="https://www.sedaily.com/NewsView/2GVF9T1W69" target="_blank" rel="noopener">서울경제 - '퇴직연금 실물이전 사전조회' 21일부터 서비스 개시</a></li>
    <li><a href="https://www.imaeil.com/page/view/2026082417543166641" target="_blank" rel="noopener">매일신문 - 금감원, 퇴직연금 실물이전 'DC→타사 IRP' 등 장벽 허문다</a></li>
  </ul>
  기준일: 2026-09-16(WebSearch 확인일). 사전조회 서비스 시행일은 2025-07-21, 누적 이전
  통계 기준일은 2026년 6월 말, TF 킥오프는 2026년 8월입니다. 고용노동부·금융감독원
  원문 보도자료는 이번 세션 WebFetch가 차단돼 직접 확인하지 못했고, 위 언론 보도와
  KB·KDI·보험연구원 등 복수 독립 출처의 교차 확인으로 대체했습니다.
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
  "headline": "퇴직연금 실물이전 대상 상품과 신청 방법",
  "description": "퇴직연금 실물이전 대상 상품, DB·DC·IRP 간 이전 가능 여부, 사전조회 서비스 신청 절차, 2026년 6월 기준 누적 이전 통계와 2027년까지의 확대 계획을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-16",
  "dateModified": "2026-09-16",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/retirement-pension-in-kind-transfer"
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
      "name": "퇴직연금 실물이전이 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "보유한 상품을 팔지 않고 퇴직연금을 운용하는 금융회사만 바꾸는 서비스로, 2024년 10월 31일부터 시행 중입니다." }
    },
    {
      "@type": "Question",
      "name": "지금 당장 실물이전 할 수 있는 상품은 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "원리금보장상품, 공모펀드(MMF 제외), 채무증권, ETF는 수관회사가 취급하면 실물이전이 가능합니다. MMF와 환매중단펀드는 현재 대상이 아닙니다." }
    },
    {
      "@type": "Question",
      "name": "DC형 계좌를 다른 회사 IRP로 실물이전할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아직 안 됩니다. 실물이전은 DB→DB, DC→DC, IRP→IRP처럼 같은 제도 사이에서만 가능하고, DC→타사 IRP는 2027년까지 확대가 추진되고 있습니다." }
    },
    {
      "@type": "Question",
      "name": "사전조회 서비스는 어떻게 신청하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "지금 가입한 회사의 홈페이지나 앱에서 옮기려는 회사를 지정해 신청하면, 신청일 다음 영업일까지 실물이전 가능 여부를 알려줍니다." }
    },
    {
      "@type": "Question",
      "name": "실물이전을 실제로 얼마나 이용했나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2024년 10월 31일 도입 후 2026년 6월 말까지 누적 15조 9,000억원(25만여건)이 이전됐고, IRP 6조 8,000억원, DC형 4조 8,000억원, DB형 4조 3,000억원 순입니다." }
    },
    {
      "@type": "Question",
      "name": "앞으로 언제부터 DC에서 타사 IRP로 실물이전이 가능해지나요",
      "acceptedAnswer": { "@type": "Answer", "text": "확정된 시행일은 아직 없습니다. 금융감독원은 2026년 10월부터 전산 개발에 착수해 2027년까지 제도 정비를 완료한다는 목표를 밝혔습니다." }
    }
  ]
}
</script>
