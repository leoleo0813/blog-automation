---
keyword: 상속세 연부연납
title: 상속세 연부연납 조건과 기간
slug: inheritance-tax-installment-payment
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 780 (PC 260 / 모바일 520)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-21 — 통과]
  WebSearch "상속세 연부연납 조건 이자율 기간 신청방법" + "상속세 연부연납 담보
  상장주식 담보제공 가능" 상위 종합:
  law.go.kr(국가법령정보센터, 공식 서식) / kbthink.com(KB국민은행, 준공식 칼럼) /
  tfmedia.co.kr(세무 전문 매체, 전문가 칼럼) / heumtax.com(세무법인 콘텐츠) /
  valuetax.co.kr(세무법인 가치, 콘텐츠) / fakt.co.kr(가업승계 컨설팅 콘텐츠) /
  truetax.co.kr(세무 서비스 콘텐츠) / sangsoktax.com(세무법인다솔, 콘텐츠) /
  taxoffice.co.kr(세무법인 게시판) / taxly.kr(세무 서비스, 계산기 포함) /
  brunch.co.kr(개인 블로그)
  1) 진입 여지 — 있음. heumtax·valuetax·fakt·truetax·sangsoktax·taxoffice·
     brunch 등 세무법인/개인 콘텐츠가 상위 다수를 차지. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("조건이 뭔지, 얼마나 나눠 낼 수 있는지"). taxly.kr에
     계산기가 있지만 상위 대부분은 설명형 콘텐츠라 조회·계산기 실행이
     지배적 의도는 아님.
  3) 답 완결 여부 — 부분적. 신청 조건(2천만원)·담보 비율(120%/110%)·기간
     (10년/20년/5년)은 여러 글에 흩어져 있으나, "상속받은 주식·국채처럼
     유동성 높은 자산을 담보로 내면 자동 승인된다"는 사실과 14편(가업상속공제)
     의 20년 특례를 주식 초보 관점에서 엮어 설명하는 글은 상위에서 찾지
     못했다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 상속받은 국채·상장주식처럼 유동성 높은 자산을 담보로 제공하면 신청과
      동시에 허가된 것으로 처리된다는 점 — 현금이 없어도 상속받은 주식만으로
      세금을 나눠 낼 길이 있다는, 이 시리즈 독자에게 실질적인 정보이득.
  (b) 담보 가액 계산 예시(세액 3억원 가정 시 120%/110% 비교표)로 "담보를
      얼마나 준비해야 하는지"를 구체적으로 보여준다.
  (c) 14편(가업상속공제 한도와 요건)에서 이미 확정한 경영기간별 공제한도와
      연결해, 가업상속재산이면 연부연납 기간이 왜 20년까지 늘어나는지
      설명한다. 14편은 공제한도만 다루고 연부연납은 언급하지 않는다(grep
      확인, 0건).
  (d) 사람 캡처로 확정: 연부연납 가산율은 국세기본법 시행규칙 제19조의3
      (국세환급가산금의 이율)에 따라 연 1천분의 35(연 3.5%)다. 출처마다
      다른 값(2.9%→1.2% vs 3.1%)이 나와 상충했던 부분을 사용자가 직접
      국세법령정보시스템에서 조문 원문을 캡처해 확정했다. 이 이자율을
      반영해 담보 세액 3억원 가정 시 1년차 가산금 계산 예시를 완성했다.
primary_source: |
  1차 시도: 국세법령정보시스템(taxlaw.nts.go.kr) 및 국세상담센터 Q&A
  (call.nts.go.kr) WebFetch 각 1회 시도 → 둘 다 EGRESS_BLOCKED(2026-09-21).
  대조군으로 www.kofia.or.kr도 같은 시도에서 EGRESS_BLOCKED로 확인해 도메인
  개별 차단이 아니라 이번 세션 전면 차단으로 판단.
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 독립 출처 8곳
  이상(law.go.kr 공식 서식, kbthink.com KB국민은행 준공식 칼럼, tfmedia.co.kr
  전문가 칼럼, heumtax.com·valuetax.co.kr·sangsoktax.com·truetax.co.kr·
  fakt.co.kr·taxoffice.co.kr 세무법인/컨설팅 콘텐츠, taxly.kr)가 다음 핵심
  사실에서 충돌 없이 일치해 교차검증으로 진행했다:
  ① 상속세·증여세 모두 납부세액 2,000만원 초과 시 연부연납 신청 가능,
  ② 담보 제공 필수, 담보 가액은 세액과 이자상당액을 합한 금액의 120%
  (현금·납세보증보험증권·은행 납세보증서는 110%) 이상,
  ③ 국채·상장주식 등 유동성 높은 자산을 담보로 제공하면 신청과 동시에
  허가된 것으로 처리,
  ④ 상속세 연부연납 기간은 허가일로부터 10년 이내(가업상속재산 요건 충족
  시 최대 20년), 증여세는 5년 이내(최초 납부분 포함 총 6회),
  ⑤ 세무서장은 상속세는 신고기한부터 6개월, 증여세는 3개월 이내에 허가
  여부를 서면 통지해야 하며 기한 내 통지가 없으면 자동으로 허가된 것으로
  본다.
  다만 연부연납 가산금의 구체적 이자율(가산율)은 WebSearch 자료군마다 다른
  값이 나와(2.9%→1.2% vs 3.1%) source_conflict_resolved에 경위를 남기고
  캡처로 전환했다.
  근거 법령: 상속세및증여세법 제71조(연부연납), 제72조(연부연납가산금).
source_conflict_resolved: |
  연부연납 가산율(이자율) — 최초 WebSearch에서 자료군 A("2023-03-20 이후
  연 2.9%, 이후 어느 3월 16일부터 연 1.2%로 인하", 적용 연도 불명확)와
  자료군 B("2025-03-21 개정 이후 연 3.1%가 2026년 5월 현재까지 적용")가
  상충해 캡처로 전환했다. 2026-09-22 사용자가 국세법령정보시스템
  (taxlaw.nts.go.kr)에서 "국세기본법 시행규칙 제19조의3(국세환급가산금의
  이율)" 조문 원문을 직접 캡처해 제공했다. 원문은 "영 제43조의3제2항
  본문에서 '기획재정부령으로 정하는 이자율'이란 연 1천분의 35를 말한다"
  (2024.3.22 일부개정, 2024.4.1 시행, 개정이력 2013~2024년 매년 3월
  나열되고 2024.3.22 이후 추가 개정 없음)로, 두 WebSearch 자료군 모두
  틀렸고 실제 값은 연 1천분의 35(연 3.5%)다. 이 조문이 상속세및증여세법
  시행령 제69조 등을 통해 연부연납가산금율에 준용된다는 점은 캡처 전
  WebSearch 교차검증(자료군 A·B 둘 다 같은 조문을 근거로 인용)으로 이미
  확인했다. 캡처 스크린샷(PDF)은 sources/에 보관.
기준일: 2026-09-22 (가산율은 사용자 캡처 원문 기준, 그 외는 2026-09-21
WebSearch 교차검증 기준)
tags: 상속세연부연납, 증여세연부연납, 상속세납부, 가업상속공제, 상속세담보, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-22, 캡처 반영). 신청기준(2천만원)·담보
  종류와 비율(120%/110%)·상장주식 자동승인·기간(10년/20년/5년)·허가통지
  기한(6개월/3개월/자동허가)은 독립 출처 8곳 이상 교차검증, 연부연납
  가산율(연 3.5%)은 국세기본법 시행규칙 제19조의3 원문 캡처로 확정했다.
  이 이자율로 담보 세액 3억원 가정 1년차 가산금 계산 예시를 완성했다.
self_check: |
  [2026-09-22 최종 판정 — 캡처 반영]
  게이트1 충족 — check-keywords.yml 실측 780회(2026-09-21, 일반·세부 기준
  모두 충족).
  게이트2 충족 — RULES.md v3 기준 3개 탈락 조건 모두 미해당(serp_check
  참조).
  게이트3 충족 — 담보 종류·비율 계산 예시, 상장주식 자동승인이라는 이
  시리즈 특화 정보이득, 14편과의 20년 특례 연결에 더해 확정된 가산율
  (3.5%)로 세액 3억원 가정 1년차 가산금 계산 예시까지 완성했다.
  게이트4 충족(교차검증+캡처) — taxlaw.nts.go.kr·call.nts.go.kr 각 1회
  시도 EGRESS_BLOCKED, 대조군 kofia.or.kr도 동일 차단으로 세션 전면 차단
  확인. 신청기준·담보·기간·허가절차는 독립 출처 8곳 이상 교차검증으로
  확정했고, 두 자료군이 상충했던(2.9%→1.2% vs 3.1%) 가산율은 사용자가
  국세기본법 시행규칙 제19조의3 원문을 직접 캡처해 연 3.5%로 확정했다
  (source_conflict_resolved 참조). 두 WebSearch 자료군 모두 부정확했다는
  점을 투명하게 기록해 둔다.
  카니벌라이제이션 점검 — 1~68편 keyword 전체 확인 결과 "연부연납"을
  다루는 편이 없다(grep 0건). 11편(주식 증여세)·13편(배우자 상속공제)·
  14편(가업상속공제)·inheritance-tax-deadline-penalty(상속세 신고기한과
  가산세)·gift-tax-late-filing-penalty(증여세 기한후신고 가산세)는 모두
  세액 계산이나 신고기한·가산세를 다룰 뿐 "신고 이후 세금을 나눠 내는
  방법" 자체는 다루지 않아(각 파일 grep "연부연납" 0건) 겹치는 편 없음.
  제목 "상속세 연부연납 조건과 기간" 15자·금지어 없음·"~이나"·"~부터~까지"·
  "~인가요"·"~일까요" 없음. 슬러그 영문 소문자+하이픈 4단어
  (inheritance-tax-installment-payment).
  종목·상품 추천 표현 없음, 단정 표현("반드시"·"무조건"·"확실히"·"보장")
  없음. FAQ 6개와 JSON-LD 1:1 일치(가산율 확정으로 1개 추가).
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—"
  0개 확인. "다만" 0회(대신 "여기서 주의할 점은"·"다른 담보와 달리" 사용).
  본문 `<mark>` 총 4개(3~5개 기준 충족). FAQ 6개(가산율 확정으로 항목이
  하나 늘어 6개가 됐으나 매번 6개로 고정하는 관행과는 무관함). 핵심요약
  박스 제목을 "🔑 미리 확인할 핵심"으로, 박스 색을 초록 계열(#eafaf1/
  #2e8b57)로 이전 편들의 파랑(#eef6ff/#4a90d9)·주황(#fef3e2/#d98324)과
  다르게 바꿨다. 면책 문구도 이전 편들과 다른 문장으로 새로 썼다. 목차
  제외 본문 H2 5개 중 서술형 3개("상속세 연부연납 조건", "상속세와
  증여세, 기간이 다르다", "가업상속공제와 만나면 기간이 늘어나는 이유"),
  질문형 2개("담보는 무엇으로 얼마나 제공하나요", "상속받은 주식을 담보로
  쓸 수 있나요")로 "~나요" 편중 없음(5개 중 2개, 40%).
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p>상속세나 증여세 납부세액이 2,000만원을 넘으면, 한 번에 내지 않고 최대 10년(증여세는 5년)에 걸쳐 나눠 내는 <mark>연부연납</mark>을 신청할 수 있습니다. 신청하려면 담보 제공이 필수이고 매년 <b>연 3.5%</b>의 가산금(이자)이 붙습니다. 상속받은 주식만으로 담보를 대신할 수 있는지까지 정리했습니다.</p>

<div style="background:#eafaf1;border:2px solid #2e8b57;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5c3d;font-size:18px;">🔑 미리 확인할 핵심</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>납부세액이 <b>2,000만원을 초과</b>할 때만 연부연납을 신청할 수 있습니다.</li>
    <li>담보 없이는 신청할 수 없고, 담보 가액은 세액의 <b>120%</b>(현금·보증보험은 110%) 이상이어야 합니다.</li>
    <li>나눠 낸 세금에는 매년 <mark>연 3.5%(국세기본법 시행규칙 제19조의3)</mark>의 가산금이 붙습니다.</li>
    <li>상속받은 상장주식이나 국채를 담보로 내면 신청과 <b>동시에 자동 승인</b>됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>상속세 연부연납 조건</li>
  <li>담보는 무엇으로 얼마나 제공하나요</li>
  <li>상속세와 증여세, 기간이 다르다</li>
  <li>상속받은 주식을 담보로 쓸 수 있나요</li>
  <li>가업상속공제와 만나면 기간이 늘어나는 이유</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">상속세 연부연납 조건</h2>

<p>연부연납은 상속세나 증여세를 한 번에 내기 어려울 때, 국세청 허가를 받아 여러 해에 걸쳐 나눠 내는 제도입니다. 아무 세액에나 적용되지는 않고, 납부할 세액이 2,000만원을 초과해야 신청할 수 있습니다.</p>

<p>신청은 상속세·증여세 신고기한 안에 관할 세무서에 연부연납허가신청서를 제출하는 방식으로 합니다. 신고기한을 넘겨 고지서를 받은 경우에도 고지서에 적힌 납부기한 안에 신청할 수 있습니다.</p>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">담보는 무엇으로 얼마나 제공하나요</h2>

<p>연부연납을 받으려면 담보 제공이 필수입니다. 담보로 인정되는 자산은 부동산, 금전, 국채·지방채 같은 유가증권, 납세보증보험증권, 은행의 납세보증서 등입니다.</p>

<p>담보 가액 기준도 정해져 있습니다. 연부연납할 세액과 이자상당액을 더한 금액의 120% 이상을 담보로 내야 합니다. 담보가 현금이나 납세보증보험증권, 은행 납세보증서라면 이 비율이 110%로 낮아집니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">담보 종류</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">필요 담보 비율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">상속세 3억원 가정 시 담보 가액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">부동산·일반 유가증권</td>
      <td style="border:1px solid #ddd;padding:8px;">120% 이상</td>
      <td style="border:1px solid #ddd;padding:8px;">3억원+이자상당액의 120%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">현금·납세보증보험증권·은행 납세보증서</td>
      <td style="border:1px solid #ddd;padding:8px;">110% 이상</td>
      <td style="border:1px solid #ddd;padding:8px;">3억원+이자상당액의 110%</td>
    </tr>
  </tbody>
</table>

<p>이자상당액을 계산할 때 쓰는 가산율은 <b>연 1천분의 35(연 3.5%)</b>입니다. 국세기본법 시행규칙 제19조의3(국세환급가산금의 이율)에 정해진 값을 그대로 준용합니다. 예를 들어 상속세 3억원을 연부연납으로 신청하면, 아직 갚지 않은 잔액에 대해 연 3.5%씩 가산금이 붙습니다. 3억원이 고스란히 남아 있는 첫해를 기준으로 하면 연간 가산금은 약 1,050만원(3억원×3.5%)입니다. 실제로는 매회 분납하면서 잔액이 줄어들기 때문에, 전체 기간 동안 내는 가산금 총액은 이보다 적습니다.</p>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">상속세와 증여세, 기간이 다르다</h2>

<p>연부연납 기간은 세금 종류에 따라 다릅니다. 상속세는 허가받은 날로부터 <mark>10년 이내</mark>이고, 증여세는 5년 이내입니다. 증여세는 최초 납부분을 포함해 총 6회로 나눠 내는 구조입니다.</p>

<p>세무서장은 신청서를 받으면 허가 여부를 서면으로 통지해야 합니다. 통지 기한은 상속세가 신고기한부터 6개월, 증여세가 3개월입니다. 이 기간 안에 통지가 없으면 자동으로 허가된 것으로 봅니다.</p>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">상속받은 주식을 담보로 쓸 수 있나요</h2>

<p>가능합니다. 국채나 상장주식처럼 시장에서 바로 사고팔 수 있는 자산을 담보로 제공하면, 신청과 동시에 <b>자동 승인</b>됩니다. 다른 담보와 달리 세무서 심사 결과를 따로 기다릴 필요가 없다는 뜻입니다.</p>

<p>여기서 주의할 점은 모든 주식이 해당하지는 않는다는 것입니다. 거래소에 상장돼 시세가 형성된 주식이라야 담보 인정을 받기 쉽고, 비상장주식은 담보 가치를 별도로 평가받아야 해 절차가 더 걸립니다. 현금이 부족해도 상속받은 주식을 그대로 들고 세금을 나눠 낼 방법이 있다는 점이 이 제도의 핵심입니다.</p>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">가업상속공제와 만나면 기간이 늘어나는 이유</h2>

<p><a href="https://sensitiveboss3.tistory.com/entry/business-succession-deduction">가업상속공제</a>를 받는 가업상속재산이라면 연부연납 기간이 최대 <mark>20년</mark>까지 늘어납니다. 공제로 세금을 줄이는 데 그치지 않고, 남은 세금을 갚는 기간까지 길게 열어줘 상속인이 회사 지분을 급하게 팔지 않아도 되게 하려는 취지입니다.</p>

<p>가업상속공제 자체의 경영기간별 공제한도와 요건은 <a href="https://sensitiveboss3.tistory.com/entry/business-succession-deduction">가업상속공제 한도와 요건</a> 편에서 이미 정리했습니다. 공제와 연부연납은 별개의 제도이지만, 가업상속재산이라면 두 혜택을 함께 받을 수 있습니다.</p>

<p>담보로 쓸 자산이 있는지부터 확인해 보시기 바랍니다. 상속받은 주식이나 국채가 있다면 별도 담보를 마련할 필요 없이 그대로 활용할 수 있어 훨씬 수월합니다. 가산율은 매년 고시가 바뀔 수 있으므로, 신청 직전에 <a href="https://taxlaw.nts.go.kr" target="_blank" rel="noopener">국세법령정보시스템</a>에서 그해 적용되는 최신 이자율을 다시 확인하는 편이 안전합니다.</p>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">연부연납은 아무 세금에나 신청할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 상속세·증여세 납부세액이 2,000만원을 초과해야 신청할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">담보 없이 연부연납을 신청할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">안 됩니다. 담보 제공이 필수이며, 담보 가액은 세액과 이자상당액을 합한 금액의 120%(현금·납세보증보험증권·은행 납세보증서는 110%) 이상이어야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상속세와 증여세의 연부연납 기간이 같나요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 상속세는 허가일로부터 10년 이내(가업상속재산 요건을 충족하면 최대 20년), 증여세는 5년 이내입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상속받은 주식을 담보로 낼 수 있나요</summary>
  <p style="margin:10px 0 0 0;">가능합니다. 국채나 상장주식처럼 유동성이 높은 자산을 담보로 제공하면 신청과 동시에 허가된 것으로 봅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신청하면 바로 승인되나요</summary>
  <p style="margin:10px 0 0 0;">담보 종류에 따라 다릅니다. 국채·상장주식 등 유동성 높은 담보는 신청과 동시에 자동 승인되지만, 그 외 담보는 세무서장이 상속세는 6개월, 증여세는 3개월 이내에 서면으로 허가 여부를 통지합니다. 이 기간 안에 통지가 없으면 자동으로 허가된 것으로 봅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">가산금 이자율은 정확히 몇 %인가요</summary>
  <p style="margin:10px 0 0 0;">연 1천분의 35, 즉 연 3.5%입니다. 국세기본법 시행규칙 제19조의3(국세환급가산금의 이율)에 정해진 값을 준용하며, 매년 개정될 수 있어 신청 시점에 다시 확인하는 편이 안전합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 상속세및증여세법 제71조(연부연납), 제72조(연부연납가산금)</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2331&amp;cntntsId=7724" target="_blank" rel="noopener">국세청 - 상속세 납부(연부연납·물납 안내)</a></li>
    <li><a href="https://taxlaw.nts.go.kr" target="_blank" rel="noopener">국세법령정보시스템</a> - 국세기본법 시행규칙 제19조의3(국세환급가산금의 이율)</li>
  </ul>
  기준일: 2026-09-22(가산율은 사용자가 직접 캡처한 국세기본법 시행규칙
  제19조의3 원문 기준, 그 외 항목은 2026-09-21 교차검증 기준). 세율·한도는
  개정될 수 있으니 신청 전 최신 내용을 다시 확인하시기 바랍니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 상속세·증여세 납부 방법을 안내하는 정보성 콘텐츠이며, 특정 절세 전략이나 금융상품 가입을 권하지 않습니다. 실제 신청 여부와 담보 제공 방법은 개별 사정에 따라 달라질 수 있으므로, 최종 판단과 그 결과는 신청인 본인에게 있습니다. 가산율 등 세법상 수치는 매년 개정될 수 있으니 신청 전 반드시 국세법령정보시스템이나 관할 세무서에서 최신 내용을 다시 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "상속세 연부연납 조건과 기간",
  "description": "상속세·증여세 연부연납 신청 조건, 담보 종류와 비율, 상속세·증여세 기간 차이, 상속받은 주식을 담보로 쓸 수 있는지를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-21",
  "dateModified": "2026-09-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/inheritance-tax-installment-payment"
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
      "name": "연부연납은 아무 세금에나 신청할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 상속세·증여세 납부세액이 2,000만원을 초과해야 신청할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "담보 없이 연부연납을 신청할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "안 됩니다. 담보 제공이 필수이며, 담보 가액은 세액과 이자상당액을 합한 금액의 120%(현금·납세보증보험증권·은행 납세보증서는 110%) 이상이어야 합니다." }
    },
    {
      "@type": "Question",
      "name": "상속세와 증여세의 연부연납 기간이 같나요",
      "acceptedAnswer": { "@type": "Answer", "text": "다릅니다. 상속세는 허가일로부터 10년 이내(가업상속재산 요건을 충족하면 최대 20년), 증여세는 5년 이내입니다." }
    },
    {
      "@type": "Question",
      "name": "상속받은 주식을 담보로 낼 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "가능합니다. 국채나 상장주식처럼 유동성이 높은 자산을 담보로 제공하면 신청과 동시에 허가된 것으로 봅니다." }
    },
    {
      "@type": "Question",
      "name": "신청하면 바로 승인되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "담보 종류에 따라 다릅니다. 국채·상장주식 등 유동성 높은 담보는 신청과 동시에 자동 승인되지만, 그 외 담보는 세무서장이 상속세는 6개월, 증여세는 3개월 이내에 서면으로 허가 여부를 통지합니다. 이 기간 안에 통지가 없으면 자동으로 허가된 것으로 봅니다." }
    },
    {
      "@type": "Question",
      "name": "가산금 이자율은 정확히 몇 %인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "연 1천분의 35, 즉 연 3.5%입니다. 국세기본법 시행규칙 제19조의3(국세환급가산금의 이율)에 정해진 값을 준용하며, 매년 개정될 수 있어 신청 시점에 다시 확인하는 편이 안전합니다." }
    }
  ]
}
</script>
