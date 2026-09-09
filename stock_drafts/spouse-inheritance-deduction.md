---
keyword: 배우자 상속공제
title: 배우자 상속공제 한도 계산 방법
slug: spouse-inheritance-deduction
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 1550 (PC 390 / 모바일 1160)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요, 2026-09-09 네이버 검색광고 API 실측)
serp_check: |
  [게이트2 v3 판정 2026-09-09 — 통과]
  WebSearch "배우자 상속공제 한도 계산 방법 법정상속분" + "국세청 상속세 세액계산흐름도
  배우자상속공제 기초공제 일괄공제" 상위 종합:
  casenote.kr(판례/질의회신) / heumtax.com(세무법인, ×2) /
  magazine.securities.miraeasset.com(미래에셋증권 매거진) / tuzaga.com(세무사 블로그) /
  daeryunlaw-inherit.com(법무법인, ×2) / law.go.kr(공식) / nts.go.kr(국세청, 공식) /
  easylaw.go.kr(공식) / 부동산계산기.com(계산기) / jjongsemusa.com(세무사 블로그)
  1) 진입 여지 — 있음. 세무법인·법무법인·개인 세무사 블로그가 다수 상위에 진입.
     SERP 안 잠김.
  2) 검색 의도 — 정보 탐색+계산("한도가 얼마고 어떻게 계산하나"). 계산기 사이트가
     하나 있지만 상위 대부분은 설명형 콘텐츠.
  3) 답 완결 여부 — 부분적. 배우자상속공제의 기본 구조는 여러 글이 이미 설명하지만,
     상속재산이 상장주식일 때의 평가방법(11편 자료 재사용)과 금융재산공제까지
     엮어 "주식 상속"이라는 각도로 설명하는 글, 그리고 배우자 유무에 따른 실제
     세액 차이를 계산 예시로 보여주는 글은 못 찾음. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-09 — 국세청 원문 전부 확정]
  (a) 배우자상속공제 완전한 계산식(실제 상속액 5억원 미만이면 5억원, 5억원
      이상이면 실제 상속액(법정상속지분×상속재산가액과 30억원 중 작은 금액이
      한도)) + 기초공제(2억원) + 일괄공제(5억원) + 그 밖의 인적공제(자녀·미성년자·
      연로자·장애인공제) + 금융재산공제(주식 포함, 10억원 초과 시 2억원 고정)를
      전부 국세청 원문으로 확정.
  (b) 핵심 정보이득 — "배우자 상속재산 분할을 6개월 내에 안 하면 5억원만 공제
      받는다"는 절차 함정. 실제 상속받은 금액으로 공제받으려면 상속세 신고기한
      다음날부터 6개월(배우자 상속재산 분할 신고기한) 안에 등기·명의개서까지
      마쳐 분할하고 신고해야 한다 — 이 기한을 놓치면 실제 더 많이 상속받았어도
      5억원만 공제된다. 검색 상위 글 대부분이 한도액 계산 구조만 다루고 이
      절차 요건은 놓치는 경우가 많음.
  (c) 계산 예시 2건(배우자 있음 vs 없음, 동일 30억원 상장주식 상속)으로 배우자
      공제가 실제 세액에 얼마나 큰 차이를 만드는지 보여준다(9천만원 vs 7억
      6천만원).
  (d) 상속재산이 상장주식이면 상속개시일(사망일) 전후 각 2개월 종가 평균으로
      평가한다는 것(11편 법령 원문 재사용)과, 주식이 금융재산공제 대상에
      명시적으로 포함된다는 것을 "주식 상속"이라는 각도로 엮었다.
primary_source: |
  세 경로로 확보(2026-09-09).
  (1) 국세청(nts.go.kr) 「상속세 세액계산 흐름도」 — 세율표·세대생략할증·일괄공제
      개념·상속공제 종합한도 개념. sources/nts-inheritance-tax-calc-flowchart.md.
  (2) 국세청 「상속세 항목별 설명」(mi=6528&cntntsId=7956) — 기초공제(2억원)·
      배우자상속공제 전체 계산식·일괄공제(5억원)·그 밖의 인적공제·금융재산공제.
      사람이 일반 스크롤 캡처(10장)로 확보. sources/nts-inheritance-tax-items.md.
  (3) 상장주식 평가방법(상속세및증여세법 시행령 제52조의2)은 11편 자료
      (sources/decree-listed-stock-valuation.md) 재사용 — 법 제60조제1항제1호가
      증여(제63조)와 같은 조문을 인용해 상속에도 그대로 적용된다.
기준일: 2026-09-09 (국세청 페이지 캡처일)
tags: 상속세, 배우자상속공제, 기초공제, 일괄공제, 주식상속, 금융재산공제, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-09).
  게이트1: 네이버 키워드도구 실측 1,550회.
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 배우자상속공제 완전한 계산식 + 6개월 분할신고 절차 함정 + 배우자
  유무에 따른 세액 대비표(9천만원 vs 7억6천만원) + 주식 상속에 특화된 금융재산
  공제·평가방법 연결로 정보이득 확보.
  게이트4: 국세청 원문 두 페이지(세액계산흐름도·항목별 설명, 총 10장 사람 캡처)
  + 11편 법령 원문 재사용, 1차 출처 완비.
self_check: |
  [2026-09-09 국세청 원문 전부 확보 후 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 1,550회.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 배우자상속공제 계산식 전문, 6개월 분할신고 절차 함정, 배우자
  유무 세액 대비표, 주식 특화 각도(평가방법+금융재산공제)까지 검색 상위 글이
  다루지 않는 정보이득을 다수 확보했다.
  게이트4 충족 — 국세청 세액계산흐름도·항목별 설명 두 페이지를 사람이 직접
  캡처(총 10장)해 1차 출처로 확정. 검색 요약에서 본 숫자를 그대로 쓰지 않고
  전부 원문 캡처로 재확인했다.
  검산 — [배우자 있음] 30억원 상장주식, 배우자+자녀1명, 법정상속지분대로 분할
  (배우자 60%=18억원). 배우자공제: 한도 min(30억×60%=18억, 30억)=18억,
  실제상속액 18억(한도이내)이므로 18억원 공제. 기초공제2억+자녀공제5천만=2.5억
  vs 일괄공제5억 → 5억 선택. 금융재산공제(순금융재산 30억, 10억초과) 2억원.
  상속공제합계 5억+18억+2억=25억원. 과세표준 30억-25억=5억원. 세율20%
  (5억이하), 누진공제1천만 → 5억×20%-1천만=9천만원.
  [배우자 없음] 동일 30억원, 자녀1명 단독상속. 배우자공제 0원. 기초공제2억+
  자녀공제5천만=2.5억 vs 일괄공제5억 → 5억 선택. 금융재산공제 2억원. 상속공제
  합계 5억+2억=7억원. 과세표준 30억-7억=23억원. 세율40%(10억초과30억이하),
  누진공제1억6천만 → 23억×40%-1억6천만=7억6천만원.
  → 같은 30억원 상속에서 배우자 유무만으로 세액이 9천만원과 7억6천만원으로
  8.4배 차이. 배우자상속공제의 실질적 크기를 보여주는 검증된 대비.
  카니발라이제이션 점검 — 1~12편 어디에도 상속세는 없다. 겹침 없음.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문 기관 안내 문장과 하단 참고
  출처를 전부 링크 처리. target="_blank" rel="noopener", 정부기관이라 nofollow
  미부착.
  제목 12자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 3단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 하단 면책 문구
  포함.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p>배우자가 살아있으면 상속받은 금액에 따라 <mark>최소 5억원에서 최대 30억원까지</mark> 상속세 과세가액에서 공제받을 수 있습니다. 이 공제를 제대로 받으려면 <b>상속세 신고기한 다음날부터 6개월 안에 배우자의 상속재산을 실제로 분할</b>해야 한다는 조건까지 함께 알아둬야 합니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>배우자가 실제 상속받은 금액이 <b>5억원 미만(0원 포함)이면 5억원</b>을, <b>5억원 이상이면 실제 상속받은 금액</b>(한도 초과 시 한도액)을 공제받습니다.</li>
    <li>공제 한도는 <mark>상속재산가액×배우자 법정상속지분과 30억원 중 작은 금액</mark>입니다.</li>
    <li>실제 상속액으로 공제받으려면 <b>신고기한 다음날부터 6개월 안에 배우자 몫을 실제로 분할·신고</b>해야 합니다. 놓치면 5억원만 공제됩니다.</li>
    <li>상속재산이 상장주식이면 사망일 <mark>전후 각 2개월 종가 평균</mark>으로 평가하고, 별도로 <b>금융재산공제</b>도 받을 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>배우자 상속공제는 얼마까지인가요</li>
  <li>기초공제·일괄공제는 무엇이 다른가요</li>
  <li>상속재산이 주식이면 무엇이 달라지나요</li>
  <li>세율은 어떻게 적용하나요</li>
  <li>배우자 유무로 세금이 얼마나 차이 나나요</li>
  <li>신고는 언제, 어떻게 하나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배우자 상속공제는 얼마까지인가요</h2>

<p>피상속인의 배우자가 생존해 있으면 <mark>배우자가 실제 상속받은 금액에 따라</mark> 공제액이 정해집니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>배우자 상속공제액</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>실제 상속받은 금액이 없거나 5억원 미만 → <b>5억원 공제</b></li>
    <li>실제 상속받은 금액이 5억원 이상 → <b>실제 상속받은 금액</b>(공제한도액 초과 시 공제한도액) 공제</li>
  </ul>
  <b style="display:block;margin-top:14px;">배우자공제한도액 = ①, ② 중 작은 금액</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>① (상속재산가액 + 추정상속재산 + 10년 이내 증여재산가액 중 상속인 수증분 − 상속인 외의 자에게 유증·사인증여한 재산가액 − 비과세·과세가액불산입 재산가액 − 공과금·채무) × 배우자 법정상속지분 − 배우자의 사전증여재산에 대한 증여세 과세표준</li>
    <li>② <b>30억원</b></li>
  </ul>
</div>

<p>쉽게 말하면 <mark>법정상속지분만큼 곱한 금액과 30억원 중 작은 쪽이 한도</mark>이고, 그 한도 안에서 실제로 상속받은 금액만큼 공제받습니다. 자녀가 많아 배우자의 법정상속지분이 작아지면 한도도 함께 줄어듭니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>6개월 안에 분할하지 않으면 5억원만 공제됩니다.</b>
  <p style="margin:8px 0 0 0;">실제 상속받은 금액을 기준으로 공제받으려면 상속세 신고기한의 다음날부터 <b>6개월이 되는 날(배우자 상속재산 분할 신고기한)까지</b> 배우자의 상속재산을 분할(등기·등록·명의개서가 필요한 재산은 그것까지 완료)하고, 그 사실을 관할 세무서장에게 신고해야 합니다. 부득이한 사유(소송·심판청구 등)가 있으면 그 사유가 끝난 날부터 6개월까지 연장됩니다. 이 기한을 놓치면 실제로 더 많이 상속받았어도 <mark>5억원만 공제</mark>됩니다.</p>
</div>

<p style="font-size:13px;color:#888;">근거: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6528&amp;cntntsId=7956" target="_blank" rel="noopener">국세청 상속세 항목별 설명</a>(2026-09-09 확인).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">기초공제·일괄공제는 무엇이 다른가요</h2>

<p>배우자공제와 별개로 <mark>기초공제 2억원</mark>이 기본으로 적용됩니다. 다만 상속인이 배우자와 자녀 등 여러 명이면 기초공제 대신 <b>일괄공제 5억원</b>을 선택할 수 있습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <ul style="margin:0;padding-left:20px;">
    <li><b>기초공제</b> — 거주자·비거주자 사망 모두 2억원. 비거주자는 기초공제 2억원만 적용되고 배우자공제 등 다른 상속공제는 못 받습니다.</li>
    <li><b>그 밖의 인적공제</b> — 자녀공제(1인당 5천만원), 미성년자공제(1천만원×19세까지 잔여연수), 연로자공제(1인당 5천만원, 65세 이상), 장애인공제(1천만원×기대여명연수)</li>
    <li><b>일괄공제</b> — (기초공제+그 밖의 인적공제) 합계와 5억원 중 <b>큰 금액</b>을 선택. 상속세 신고를 아예 안 해도 자동으로 5억원이 공제됩니다.</li>
  </ul>
</div>

<p>배우자 혼자 단독으로 상속받는 경우에는 일괄공제를 쓸 수 없고 기초공제와 그 밖의 인적공제 합계로만 공제받습니다. 배우자와 자녀가 함께 상속받는 일반적인 경우라면, 자녀공제 등을 합쳐도 대부분 5억원(일괄공제)보다 작아서 <mark>일괄공제 5억원을 선택하는 경우가 많습니다.</mark></p>

<p style="font-size:13px;color:#888;">근거: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6528&amp;cntntsId=7956" target="_blank" rel="noopener">국세청 상속세 항목별 설명</a>(2026-09-09 확인).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">상속재산이 주식이면 무엇이 달라지나요</h2>

<p>상장주식(코스피·코스닥)이 상속재산에 포함되면 두 가지를 추가로 챙겨야 합니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>① 평가방법 — 사망일 종가가 아니라 전후 2개월 평균</b>
  <p style="margin:8px 0 0 0;">주식 증여세와 완전히 같은 규정(상속세및증여세법 시행령 제52조의2)이 상속에도 그대로 적용됩니다. 상속개시일(사망일) 전후 각 2개월, 총 4개월간 종가 평균으로 평가하며, 그 사이 증자·합병이 있으면 평가 기간이 재조정되고 거래정지·관리종목 지정 기간이 낀 종목은 제외될 수 있습니다.</p>
  <b style="display:block;margin-top:14px;">② 금융재산공제 — 주식도 대상</b>
  <p style="margin:8px 0 0 0;">상속재산에 포함된 금융재산(예금·적금·주식 등)의 가액에서 금융채무를 뺀 순금융재산가액을 기준으로 별도로 공제받습니다.</p>
</div>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">순금융재산가액</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">금융재산상속공제</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">2,000만원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">전액</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">2,000만원 초과 ~ 1억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">2,000만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">1억원 초과 ~ 10억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">순금융재산가액 × 20%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">10억원 초과</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>2억원</mark></td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">근거: 상속세및증여세법 시행령 제52조의2(11편 확인) + <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6528&amp;cntntsId=7956" target="_blank" rel="noopener">국세청 상속세 항목별 설명</a>(2026-09-09 확인).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">세율은 어떻게 적용하나요</h2>

<p>상속세 세율은 <mark>증여세와 완전히 동일한 5단계 초과누진세율</mark>입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">과세표준</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세율</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">누진공제액</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">1억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">10%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">없음</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">5억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">20%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">10억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">30%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">30억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">40%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1억 6천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">30억원 초과</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">50%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">4억 6천만원</td></tr>
  </tbody>
</table>

<p>산출세액 = 과세표준 × 세율 − 누진공제액입니다. 상속인이나 수유자가 피상속인의 자녀가 아닌 직계비속이면 30% 할증(미성년자가 20억원 초과 상속받으면 40%)이 추가됩니다.</p>

<p style="font-size:13px;color:#888;">근거: 국세청 「국세신고안내 > 상속세 > 세액계산흐름도」(2026-09-09 확인).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배우자 유무로 세금이 얼마나 차이 나나요</h2>

<p>같은 30억원 상당의 상장주식을 상속하더라도, <mark>배우자가 있는지 없는지에 따라 세액이 크게 갈립니다.</mark></p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">배우자+자녀 1명 상속</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">자녀 1명 단독 상속</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">상속재산가액</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">30억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">30억원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">배우자공제</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">18억원<br><span style="font-size:12px;color:#888;">(법정상속지분 60% 실제 분할)</span></td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">일괄공제</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5억원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">금융재산공제</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">2억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">2억원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">과세표준</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">23억원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;"><b>산출세액</b></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>9,000만원</mark></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>7억 6,000만원</mark></td></tr>
  </tbody>
</table>

<p>배우자공제 한 항목의 차이만으로 세액이 <b>8배 넘게</b> 벌어집니다. 배우자가 있다면 상속재산 분할과 신고를 6개월 기한 안에 마치는 것이 그만큼 중요합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고는 언제, 어떻게 하나요</h2>

<p>상속개시일(사망일)이 속하는 달의 말일부터 <mark>6개월 이내</mark>에 상속인이 신고·납부합니다. 배우자 실제 상속액을 기준으로 공제받으려면 앞서 본 것처럼 같은 기한(신고기한 다음날부터 6개월) 안에 별도로 <b>배우자 상속재산 분할 신고</b>도 해야 합니다. <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>에서 전자신고할 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배우자가 상속을 하나도 안 받으면 공제도 없나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 실제 상속받은 금액이 없어도 5억원은 기본으로 공제됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배우자공제는 최대 얼마까지 받을 수 있나요</summary>
  <p style="margin:10px 0 0 0;">법정상속지분만큼 계산한 금액과 30억원 중 작은 금액이 한도입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배우자 상속재산 분할을 늦게 하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">신고기한 다음날부터 6개월 안에 분할·신고하지 못하면 실제 상속액과 무관하게 5억원만 공제됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">기초공제와 일괄공제를 둘 다 받을 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. (기초공제+그 밖의 인적공제) 합계와 일괄공제 5억원 중 큰 금액 하나만 선택합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상속받은 주식은 언제 시점 가격으로 평가하나요</summary>
  <p style="margin:10px 0 0 0;">사망일 당일 종가가 아니라 사망일 전후 각 2개월, 총 4개월간의 종가 평균으로 평가합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상속세는 언제까지 신고해야 하나요</summary>
  <p style="margin:10px 0 0 0;">상속개시일이 속하는 달의 말일부터 6개월 이내에 신고·납부해야 합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6528&amp;cntntsId=7956" target="_blank" rel="noopener">국세청 상속세 항목별 설명</a> — 기초공제·배우자상속공제·일괄공제·금융재산공제(2026-09-09 확인)</li>
    <li>국세청 「국세신고안내 > 상속세 > 세액계산흐름도」 — 세율표(2026-09-09 확인)</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> — 상속세및증여세법 시행령 제52조의2(11편 확인)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> — 상속세 전자신고</li>
    <li>기준일: 2026-09-09(국세청 페이지 확인일)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 판단과 책임은 본인에게 있습니다. 세율·공제 한도는 세법 개정으로 바뀔 수 있으므로 신고 전 국세청 최신 안내를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "배우자 상속공제 한도 계산 방법",
  "description": "배우자 상속공제의 계산 구조와 6개월 분할신고 요건, 기초공제·일괄공제·금융재산공제, 상장주식 상속 시 평가방법을 정리하고 배우자 유무에 따른 실제 세액 차이를 계산 예시로 보여줍니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-09",
  "dateModified": "2026-09-09",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/spouse-inheritance-deduction"
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
      "name": "배우자가 상속을 하나도 안 받으면 공제도 없나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 실제 상속받은 금액이 없어도 5억원은 기본으로 공제됩니다." }
    },
    {
      "@type": "Question",
      "name": "배우자공제는 최대 얼마까지 받을 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "법정상속지분만큼 계산한 금액과 30억원 중 작은 금액이 한도입니다." }
    },
    {
      "@type": "Question",
      "name": "배우자 상속재산 분할을 늦게 하면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "신고기한 다음날부터 6개월 안에 분할·신고하지 못하면 실제 상속액과 무관하게 5억원만 공제됩니다." }
    },
    {
      "@type": "Question",
      "name": "기초공제와 일괄공제를 둘 다 받을 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. (기초공제+그 밖의 인적공제) 합계와 일괄공제 5억원 중 큰 금액 하나만 선택합니다." }
    },
    {
      "@type": "Question",
      "name": "상속받은 주식은 언제 시점 가격으로 평가하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "사망일 당일 종가가 아니라 사망일 전후 각 2개월, 총 4개월간의 종가 평균으로 평가합니다." }
    },
    {
      "@type": "Question",
      "name": "상속세는 언제까지 신고해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "상속개시일이 속하는 달의 말일부터 6개월 이내에 신고·납부해야 합니다." }
    }
  ]
}
</script>
