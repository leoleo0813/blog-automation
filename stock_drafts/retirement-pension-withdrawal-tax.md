---
keyword: 퇴직연금 중도인출 세금
title: 퇴직연금 중도인출 세금 얼마 내나
slug: retirement-pension-withdrawal-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 530 (PC 180 / 모바일 350, 2026-09-22 실측)
gate1_pass: true (제도 기준 월 100 이상 필요, 일반 기준 500도 충족)
serp_check: |
  [게이트2 v3 판정 2026-09-22 — 통과]
  WebSearch "퇴직연금 중도인출 세금 사유 계산 방법 2026" + "퇴직연금 중도인출
  소득세법 부득이한 사유 연금외수령" 상위 종합:
  kbthink.com(KB국민은행, 준공식) / blog.koreainvestment.com(한국투자증권,
  준공식) / hankyung.com(한국경제, 언론) / investpension.miraeasset.com
  (미래에셋투자와연금센터, 준공식) / kcie.or.kr(금융투자자보호재단, 준정부) /
  ibkmagazine.co.kr(IBK기업은행, 준공식) / kmoney101.com(개인·소규모 콘텐츠,
  3개 글) / finanandinvest.kr(개인 블로그) / irp.astrowon100.com(개인 블로그) /
  casenote.kr(국세청 해석례 인용 콘텐츠) / nodong.kr·calculate.co.kr(계산기)
  1) 진입 여지 — 있음. kmoney101.com·finanandinvest.kr·irp.astrowon100.com
     등 개인·소규모 콘텐츠가 상위권에 다수 노출. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형(사유·세금이 궁금)이 지배적. 계산기 사이트
     (nodong.kr, calculate.co.kr)도 있으나 상위 대부분은 설명형 콘텐츠라
     조회·계산기 실행이 지배적 의도는 아님.
  3) 답 완결 여부 — 부분적. 법정 인출 사유 5가지와 "원금=퇴직소득세,
     운용수익=기타소득세 16.5% 또는 부득이시 저율과세"라는 골자는 여러
     글이 다루지만, "인출 사유 5가지 중 주택구입·전세보증금은 인출은 되어도
     세법상 저율과세 대상인 부득이한 사유에는 포함되지 않는다"는 구분과
     "DC형·기업형IRP만 있는 의료비 12.5% 요건(개인형IRP는 요건 없음)"을
     구체 수치로 함께 짚은 글은 상위에서 찾지 못했다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 근로자퇴직급여보장법상 "중도인출 허용 사유"(5가지)와 소득세법상
      "부득이한 사유"(세금 감면 대상)가 서로 다르다는 점을 명확히 구분한다.
      주택구입·전세보증금은 인출은 가능해도 세법상 부득이한 사유가 아니라서
      퇴직소득세 100%와 운용수익 기타소득세 16.5%가 그대로 붙는다는,
      혼동하기 쉬운 지점을 표로 정리했다.
  (b) 운용수익 300만원을 가정한 계산 예시로 "부득이한 사유"(연금소득세
      5.5% 적용 시 16만 5천원)와 "그 외 사유"(기타소득세 16.5% 적용 시
      49만 5천원)의 실제 세금 차이를 숫자로 보여준다.
  (c) DC형·기업형IRP는 요양 사유 인정에 연간 임금총액 12.5% 초과 의료비
      요건이 있지만, 개인이 스스로 가입한 개인형IRP는 이 비율 요건이 없다는
      계좌 유형별 차이를 표로 정리한다.
primary_source: |
  1차 시도: 국세청 「퇴직소득세 계산방법」 페이지(nts.go.kr/nts/cm/cntnts/
  cntntsView.do?mi=6444&cntntsId=7880) WebFetch 1회 시도 → EGRESS_BLOCKED
  (2026-09-22). 대조군으로 casenote.kr, kofia.or.kr도 같은 세션에서 WebFetch
  시도 → 둘 다 동일하게 EGRESS_BLOCKED로 확인되어 도메인 개별 차단이 아니라
  이번 세션 전면 차단으로 판단.
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 항목별로
  교차검증을 진행했다.
  ① 법정 중도인출 사유 5가지(주택구입/전세보증금/6개월이상요양/개인회생
  파산/천재지변)와 세금 구조(원금=퇴직소득세, 운용수익=기타소득세 16.5%
  또는 부득이시 연금소득세): hankyung.com(언론)/investpension.miraeasset.com
  (준공식)/kcie.or.kr(금융투자자보호재단, 준정부)/kbthink.com(KB국민은행
  준공식)/blog.koreainvestment.com(한국투자증권 준공식)/kmoney101.com/
  casenote.kr(국세청 해석례 원천세과-2130·원천세과-841 인용) 7곳이 충돌
  없이 일치.
  ② "부득이한 사유"는 인출 허용 사유 전부가 아니라 6개월이상요양·개인회생
  파산·천재지변 3가지에 한정되고 주택구입·전세보증금은 제외된다는 점:
  hankyung.com/investpension.miraeasset.com/kmoney101.com/
  irp.astrowon100.com 4곳이 일치, 충돌 없음.
  ③ 연금소득세 연령별 세율(55~69세 5.5%, 70~79세 4.4%, 80세이상 3.3%):
  metlife.co.kr/investpension.miraeasset.com/kcie.or.kr 3곳이 일치.
  ④ DC형·기업형IRP 의료비 12.5%(연간 임금총액 대비) 요건과 개인형IRP는
  이 비율 요건이 없다는 점: kbthink.com/ibkmagazine.co.kr/
  blog.koreainvestment.com/kmoney101.com 4곳이 일치.
  전부 세율·요건 구간 같은 민감한 숫자이지만, 항목마다 3곳 이상(언론·
  준정부기관·대형 금융사 준공식 콘텐츠 포함)이 충돌 없이 수렴해 RULES.md
  2026-09-12 기준의 교차검증 진행 조건을 충족했다고 판단했다.
기준일: 2026-09-22 (WebSearch 교차검증 확인일 기준)
tags: 퇴직연금, 중도인출, 퇴직소득세, 기타소득세, IRP, DC형퇴직연금, 연금소득세, 부득이한사유, 무주택자, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-22). 게이트1은 이번 실행에서 네이버
  키워드도구로 신규 실측(530회, 제도 기준 100 이상·일반 기준 500도 충족).
  게이트2는 RULES.md v3 기준으로 이번 세션에서 정식 판정. 게이트3은 인출
  사유별 세금 차이 표 + 운용수익 계산 예시 + 계좌 유형별 의료비 요건 비교표로
  충족. 게이트4는 1차 출처(nts.go.kr) 접근이 세션 전면 차단으로 막혀,
  RULES.md 2026-09-12 기준에 따라 항목별 독립 출처 3~7곳(언론·준정부기관·
  대형 금융사 준공식 콘텐츠 포함, 핵심 수치 충돌 없음)으로 교차검증했다.
capture_guide: |
  (해당 없음 — 이번 편은 교차검증으로 게이트4를 충족해 캡처가 필요하지
  않다. 사람이 최종 검토 시 아래 원문을 직접 열어 대조하면 더 안전하다.)
  1순위 — 국세청 퇴직소득세 계산방법 페이지(https://www.nts.go.kr/nts/cm/
  cntnts/cntntsView.do?mi=6444&cntntsId=7880)에서 원금·운용수익 과세
  구조 재확인.
  2순위 — 국가법령정보센터(https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=262801)
  에서 근로자퇴직급여 보장법 시행령의 중도인출 사유 조문 원문 확인.
  3순위 — 소득세법 시행령의 "부득이한 사유" 정의 조문은 국세법령정보시스템
  (taxlaw.nts.go.kr)에서 "소득세법 시행령 연금계좌" 로 검색해 원문 캡처.
self_check: |
  [2026-09-22 판정 — gate_pass:true]
  게이트1 충족 — 이번 실행 신규 실측 530회(제도 기준 100·일반 기준 500
  모두 충족).
  게이트2 충족 — RULES.md v3 기준 3개 탈락 조건 모두 미해당(serp_check
  참조).
  게이트3 충족 — 인출 사유 5가지와 부득이한 사유 여부 비교표 + 운용수익
  300만원 계산 예시 + DC형·기업형IRP vs 개인형IRP 의료비 요건 비교표.
  게이트4 충족(교차검증) — nts.go.kr 1회 시도 EGRESS_BLOCKED, 대조군
  casenote.kr·kofia.or.kr도 동일 차단으로 세션 전면 차단 확인. 항목별
  독립 출처 3~7곳이 핵심 수치에서 충돌 없이 일치해 RULES.md 2026-09-12
  기준의 교차검증 진행 조건을 충족했다고 판단.
  카니벌라이제이션 점검 — 8편(연금저축 세액공제)은 개인연금저축·IRP의
  세액공제·중도해지 추징을 다루고, 38편(퇴직연금 실물이전)은 이전 절차,
  54편(퇴직연금 DB DC 차이)은 운용방식 차이를 다뤄 이 편(퇴직연금 자체의
  중도인출 세금)과 검색 의도가 겹치지 않는다(grep 확인, "중도인출" 0건).
  제목 "퇴직연금 중도인출 세금 얼마 내나" 18자(공백 포함)·금지어 없음. 슬러그 영문
  소문자+하이픈 4단어(retirement-pension-withdrawal-tax).
  종목·상품 추천 표현 없음, 단정 표현("반드시"·"무조건"·"확실히"·"보장")
  없음. FAQ 5개와 JSON-LD 1:1 일치.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—"
  0개 확인. "다만" 0회(대신 "단,"·"여기서 헷갈리기 쉬운 부분은" 사용).
  본문 `<mark>` 총 5개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약
  박스 제목을 "🔑 핵심 포인트"로, 박스 색을 보라 계열(#f1eefc/#6a4fb6)로
  최근 편들의 주황(67편)·청록(68편)·초록(69편)과 다르게 바꿨다. 면책
  문구도 이전 편들과 다른 문장으로 새로 썼다. FAQ 헤딩도 "자주 묻는 질문"
  대신 "많이 물어보는 질문"으로 바꿨다. 목차 제외 본문 H2 5개 중 서술형
  3개("중도인출할 수 있는 법정 사유 5가지", "실제 계산 예시로 보는 세금
  차이", "DC형과 개인형IRP, 의료비 요건이 다르다"), 질문형 2개("퇴직연금
  중도인출이 뭔가요", "중도인출하면 세금은 얼마나 내나요")로 "~나요"
  편중 없음(5개 중 2개, 40%). 헤지 문구("~것으로 알려져 있습니다" 류)
  반복 없음, 확정된 사실은 단정형("~입니다")으로 서술.
  종합 판정: 4개 게이트 전부 충족, gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-22</p>

<p><mark>퇴직연금을 중도인출하면 퇴직급여 원금에는 퇴직소득세가, 그동안 불어난 운용수익에는 별도 세금이 붙습니다.</mark> 세금이 줄어드는 경우는 요양·개인회생·천재지변 같은 소득세법상 "부득이한 사유"일 때뿐이고, 주택 구입이나 전세보증금 같은 사유는 인출은 되어도 세금은 그대로 붙습니다.</p>

<div style="background:#f1eefc;border:2px solid #6a4fb6;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4a3579;font-size:18px;">🔑 핵심 포인트</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>법정 중도인출 사유는 주택구입·전세보증금·요양·개인회생파산·천재지변 5가지입니다.</li>
    <li>이 중 요양·개인회생파산·천재지변만 세법상 "부득이한 사유"로 인정돼 세금이 줄어듭니다.</li>
    <li>부득이한 사유가 아니면 운용수익에 기타소득세 <mark>16.5%</mark>가 그대로 붙습니다.</li>
    <li>DC형·기업형IRP는 요양 인정에 의료비 12.5% 요건이 있지만 개인형IRP는 없습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>퇴직연금 중도인출이 뭔가요</li>
  <li>중도인출할 수 있는 법정 사유 5가지</li>
  <li>중도인출하면 세금은 얼마나 내나요</li>
  <li>실제 계산 예시로 보는 세금 차이</li>
  <li>DC형과 개인형IRP, 의료비 요건이 다르다</li>
  <li>많이 물어보는 질문</li>
</ol>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">퇴직연금 중도인출이 뭔가요</h2>

<p>퇴직연금 중도인출은 DC형(확정기여형)이나 IRP(개인형 퇴직연금) 가입자가 퇴직하기 전에 적립금 일부 또는 전부를 미리 찾아 쓰는 제도입니다. 아무 때나 인출할 수 있는 것은 아니고, <a href="https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=262801" target="_blank" rel="noopener">근로자퇴직급여 보장법 시행령</a>이 정한 사유에 해당해야만 신청할 수 있습니다.</p>

<p>DB형(확정급여형)은 회사가 퇴직금 운용을 책임지는 구조라 원칙적으로 중도인출 대상이 아닙니다. 중도인출은 개인이 직접 운용 방식을 정하는 DC형·IRP 가입자에게만 해당합니다.</p>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">중도인출할 수 있는 법정 사유 5가지</h2>

<p>법으로 정한 인출 사유는 다섯 가지입니다. 사유마다 조건이 다르고, 뒤에서 다룰 세금 감면 여부도 사유별로 갈립니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">사유</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">조건</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">세법상 부득이한 사유</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">무주택자 주택 구입</td>
      <td style="border:1px solid #ddd;padding:8px;">본인 명의로 구입, 재직 중 1회</td>
      <td style="border:1px solid #ddd;padding:8px;">아니오</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">전세금·주택임차보증금</td>
      <td style="border:1px solid #ddd;padding:8px;">무주택자, 재직 중 1회</td>
      <td style="border:1px solid #ddd;padding:8px;">아니오</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">6개월 이상 요양</td>
      <td style="border:1px solid #ddd;padding:8px;">본인·배우자·부양가족 질병·부상</td>
      <td style="border:1px solid #ddd;padding:8px;">예</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">개인회생·파산선고</td>
      <td style="border:1px solid #ddd;padding:8px;">신청일 기준 5년 이내 결정, 효력 유지 중</td>
      <td style="border:1px solid #ddd;padding:8px;">예</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">천재지변 등 재난</td>
      <td style="border:1px solid #ddd;padding:8px;">고용노동부장관이 인정하는 재난 피해</td>
      <td style="border:1px solid #ddd;padding:8px;">예</td>
    </tr>
  </tbody>
</table>

<p>여기서 헷갈리기 쉬운 부분은 주택 구입과 전세보증금입니다. 인출 자체는 법정 사유로 허용되지만, 다음 장에서 볼 세금 감면 대상인 "부득이한 사유"에는 포함되지 않습니다.</p>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">중도인출하면 세금은 얼마나 내나요</h2>

<p>중도인출한 돈은 두 부분으로 나눠 과세됩니다. 원래 회사가 적립해준 퇴직급여 원금과, 그 돈을 운용해서 불어난 운용수익입니다.</p>

<p>원금에는 언제나 퇴직소득세가 붙습니다. 부득이한 사유(요양·개인회생파산·천재지변)에 해당하면 이 퇴직소득세가 30% 감면되어 70%만 부과되고, 해당하지 않으면(주택구입·전세보증금) 100% 그대로 부과됩니다.</p>

<p>운용수익에 붙는 세금은 차이가 더 큽니다. 부득이한 사유가 아니면 <mark>기타소득세 16.5%</mark>(지방소득세 포함)가 그대로 붙지만, 부득이한 사유에 해당하면 운용수익을 연금소득으로 보아 나이에 따라 3.3~5.5%의 낮은 연금소득세만 적용됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">부득이한 사유(요양·회생파산·재난)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">그 외 사유(주택구입·전세보증금)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">원금(퇴직급여)</td>
      <td style="border:1px solid #ddd;padding:8px;">퇴직소득세 70%만 부과(30% 감면)</td>
      <td style="border:1px solid #ddd;padding:8px;">퇴직소득세 100% 그대로</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">운용수익</td>
      <td style="border:1px solid #ddd;padding:8px;">연금소득세 3.3~5.5%(연령별)</td>
      <td style="border:1px solid #ddd;padding:8px;">기타소득세 16.5%</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">실제 계산 예시로 보는 세금 차이</h2>

<p>운용수익이 300만원이라고 가정해 보겠습니다. 55~69세 기준으로 계산하면 사유에 따라 세금 차이가 이렇게 벌어집니다.</p>

<ul style="line-height:1.9;">
  <li>부득이한 사유가 아닐 때(주택구입 등): 300만원 × 16.5% = <mark>49만 5천원</mark></li>
  <li>부득이한 사유일 때(요양 등, 55~69세 연금소득세 5.5% 적용): 300만원 × 5.5% = 16만 5천원</li>
  <li>운용수익만 놓고 보면 세금 차이는 33만원입니다.</li>
</ul>

<p>여기에 원금 부분의 30% 감면까지 더해지면, 부득이한 사유로 인출할 때와 그렇지 않을 때의 전체 세금 차이는 이보다 더 커집니다. 정확한 원금 세액은 근속연수와 환산급여에 따라 달라지므로, <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6444&cntntsId=7880" target="_blank" rel="noopener">국세청 퇴직소득세 계산방법</a> 페이지에서 본인 상황에 맞게 다시 확인하는 편이 정확합니다.</p>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">DC형과 개인형IRP, 의료비 요건이 다르다</h2>

<p>같은 "6개월 이상 요양" 사유라도 어떤 계좌에 가입했는지에 따라 인정 요건이 달라집니다. 이 차이를 모르고 신청했다가 요건 미달로 반려되는 경우가 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계좌 유형</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">요양 사유 인정 요건</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">DC형·기업형IRP</td>
      <td style="border:1px solid #ddd;padding:8px;">연간 임금총액의 <mark>12.5%</mark> 초과 의료비 지출이 확인돼야 함</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">개인형IRP(개인이 직접 가입)</td>
      <td style="border:1px solid #ddd;padding:8px;">별도 임금 비율 요건 없음. 6개월 이상 요양 필요성만 확인되면 인정</td>
    </tr>
  </tbody>
</table>

<p>회사를 통해 가입한 DC형이나 기업형IRP라면 의료비 영수증을 미리 모아 12.5% 기준을 충족하는지 확인해 두는 것이 좋습니다. 개인이 스스로 만든 개인형IRP는 이 비율 기준 없이 요양 필요성 서류만 갖추면 됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>사유 확인 서류는 6개월 안에 내야 합니다</b>
  <p style="margin:8px 0 0 0;">부득이한 사유로 중도인출하려면 그 사유가 확인된 날로부터 6개월 이내에 증빙 서류를 금융기관에 제출해야 합니다. 기한을 넘기면 저율 과세 대상에서 제외될 수 있으니 서류 준비를 미루지 않는 편이 안전합니다.</p>
</div>

<h2 style="border-left:6px solid #6a4fb6;padding-left:12px;margin-top:36px;">많이 물어보는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">퇴직연금은 아무 때나 중도인출할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 주택구입, 전세보증금, 6개월 이상 요양, 개인회생·파산선고, 천재지변 중 하나에 해당해야만 신청할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주택 구입 때문에 인출하면 세금을 적게 내나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 주택구입과 전세보증금은 인출 사유는 되지만 세법상 부득이한 사유에는 포함되지 않아, 퇴직소득세는 100% 그대로, 운용수익에는 기타소득세 16.5%가 그대로 붙습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">요양 목적으로 인출하면 세금이 얼마나 줄어드나요</summary>
  <p style="margin:10px 0 0 0;">원금에 붙는 퇴직소득세가 30% 감면되고(70%만 부과), 운용수익에는 기타소득세 16.5% 대신 나이에 따라 3.3~5.5%의 연금소득세가 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">개인형IRP도 의료비 12.5% 요건을 채워야 하나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 개인이 스스로 가입한 개인형IRP는 임금 대비 의료비 비율 요건이 없습니다. DC형·기업형IRP 가입자만 연간 임금총액의 12.5%를 초과하는 의료비 요건을 채워야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">중도인출 횟수에 제한이 있나요</summary>
  <p style="margin:10px 0 0 0;">주택구입과 전세보증금은 재직 중 각각 1회로 제한됩니다. 요양·개인회생파산·천재지변 사유는 그 사유가 새로 발생할 때마다 다시 신청할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6444&amp;cntntsId=7880" target="_blank" rel="noopener">국세청 - 퇴직소득세 계산방법</a></li>
    <li><a href="https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=262801" target="_blank" rel="noopener">국가법령정보센터 - 근로자퇴직급여 보장법 시행령</a></li>
    <li><a href="https://www.kcie.or.kr/mobile/guide/series/3/82/web_view?series_idx=82&amp;content_idx=1813" target="_blank" rel="noopener">금융투자자보호재단 - 퇴직연금 중도인출 안내</a></li>
  </ul>
  기준일: 2026년 9월 기준. 세율과 요건은 개정될 수 있으니 실제 신청 전
  최신 내용을 다시 확인하시기 바랍니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 퇴직연금 중도인출 제도와 세금 구조를 설명하는 정보성 콘텐츠이며,
특정 금융상품 가입이나 인출 여부를 권하지 않습니다. 인출 신청과 그 결과에
대한 최종 판단은 가입자 본인의 몫입니다. 세율과 인정 요건은 시점에 따라
달라질 수 있으므로, 신청 전에는 국세청이나 가입한 금융기관에서 최신 내용을
다시 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "퇴직연금 중도인출 세금 얼마 내나",
  "description": "퇴직연금 중도인출 법정 사유 5가지, 세법상 부득이한 사유와의 차이, 퇴직소득세·기타소득세·연금소득세 세율, DC형·개인형IRP의 의료비 요건 차이를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-22",
  "dateModified": "2026-09-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/retirement-pension-withdrawal-tax"
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
      "name": "퇴직연금은 아무 때나 중도인출할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 주택구입, 전세보증금, 6개월 이상 요양, 개인회생·파산선고, 천재지변 중 하나에 해당해야만 신청할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "주택 구입 때문에 인출하면 세금을 적게 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 주택구입과 전세보증금은 인출 사유는 되지만 세법상 부득이한 사유에는 포함되지 않아, 퇴직소득세는 100% 그대로, 운용수익에는 기타소득세 16.5%가 그대로 붙습니다." }
    },
    {
      "@type": "Question",
      "name": "요양 목적으로 인출하면 세금이 얼마나 줄어드나요",
      "acceptedAnswer": { "@type": "Answer", "text": "원금에 붙는 퇴직소득세가 30% 감면되고(70%만 부과), 운용수익에는 기타소득세 16.5% 대신 나이에 따라 3.3~5.5%의 연금소득세가 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "개인형IRP도 의료비 12.5% 요건을 채워야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 개인이 스스로 가입한 개인형IRP는 임금 대비 의료비 비율 요건이 없습니다. DC형·기업형IRP 가입자만 연간 임금총액의 12.5%를 초과하는 의료비 요건을 채워야 합니다." }
    },
    {
      "@type": "Question",
      "name": "중도인출 횟수에 제한이 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "주택구입과 전세보증금은 재직 중 각각 1회로 제한됩니다. 요양·개인회생파산·천재지변 사유는 그 사유가 새로 발생할 때마다 다시 신청할 수 있습니다." }
    }
  ]
}
</script>
