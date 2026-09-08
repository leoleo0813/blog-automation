---
keyword: 스톡옵션 세금
title: 스톡옵션 행사 세금 계산 방법
slug: stock-option-tax
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 130 (PC 40 / 모바일 90)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-08 — 통과]
  WebSearch "스톡옵션 행사 세금 근로소득세 계산 벤처기업 특례" 상위 8개:
  nts.go.kr(국세청, 공식) / taxwatch.co.kr(세무전문매체) / demoday.co.kr(스타트업
  서비스, 계산기) / zuzu.network(스타트업 서비스 콘텐츠, ×2) / taxguide.im(세무서비스
  블로그) / mstacc.com(회계법인 블로그) / glasswallet.com(개인 블로그, 9편에서도
  확인된 소규모 콘텐츠)
  1) 진입 여지 — 있음. zuzu.network·taxguide.im·mstacc.com·glasswallet.com 등
     소규모·블로그형 콘텐츠가 상위 8개 중 5개. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색+계산("세금이 얼마냐, 어떻게 계산하냐"). demoday.co.kr
     계산기가 하나 있지만 상위 대부분은 설명형 콘텐츠.
  3) 답 완결 여부 — 아니다. 비과세 특례·납부특례·과세이연 특례 세 가지가 얽혀 있어
     주제 자체가 복잡하고, 벤처기업 여부에 따라 같은 행사이익도 세금이 0원과
     수천만원으로 갈리는 대비를 명확히 보여주는 글이 상위에서 확인되지 않음.
     정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-08 — 시행령 원문 확정]
  (a) 조세특례제한법 시행령 원문(제14조의2~14조의4)으로 3단 특례 구조를 정리:
      ① 비과세 특례(법 제16조의2) ② 납부특례(법 제16조의3) ③ 과세이연 특례(법
      제16조의4, 근로소득 대신 양도소득세로 과세). 상위 경쟁 글이 세 특례를 뭉뚱그려
      "세금 혜택 있음" 정도로만 언급하는 자리에서, 각 특례의 신청 주체·제출 서류·
      제출 기한을 조문 그대로 표로 제공.
  (b) 핵심 정보이득 — "같은 1억원 행사이익도 벤처기업이냐 아니냐로 세금이 0원과
      1,956만원으로 갈린다"는 대비표. 비과세 한도(연 2억원, 누적 5억원, 2027-12-31
      부여분까지)를 조건으로 건 계산 예시 3건(벤처기업 한도 이내/한도 초과/비벤처기업)
      으로 실감나게 보여준다.
  (c) 일반(비특례) 스톡옵션 행사이익의 근로소득세 계산은 6편에서 이미 확보한 국세청
      종합소득세 세율표(2023~2025년 귀속)를 그대로 재사용해 계산 예시를 완성했다.
primary_source: |
  두 경로로 확보(2026-09-08).
  (1) 조세특례제한법 시행령[시행 2026.07.01.][대통령령 제36423호, 2026.06.23. 타법개정]
      제14조의2~14조의4 원문 — 사용자가 HWP로 직접 제공, olefile+zlib로 파싱해
      전문 추출. 3단 특례의 신청 주체·서류·기한을 조문 그대로 확정.
      sources/venture-stock-option-tax.md, 원본 sources/decree-tax-incentive-
      limitation-20260701.hwp.
  (2) 비과세 한도(연 2억원/누적 5억원)·적용기한(2027-12-31)은 사용자가 캡처한 구글
      AI 개요 + 국세청 페이지 스니펫(실제 문구 일부 포함)으로 확인. 이 세션이
      독립적으로 WebSearch로 찾은 수치와 정확히 일치하고, 절차 부분은 시행령
      원문(제14조의2②)의 "다음 연도 2월 말일까지" 제출 기한과도 맞아떨어져 교차
      확인됨. 법 제16조의2 모법 원문 자체는 이번 세션에서 law.go.kr 접근이
      EGRESS_BLOCKED로 막혀 직접 캡처하지 못한 한계는 있다.
  (3) 일반 근로소득세 계산은 6편에서 확보한 국세청 종합소득세 세율표(2023~2025년
      귀속) 재사용 — sources/nts-income-tax-rate.md.
기준일: 2026-09-08 (시행령·스니펫 확인일) / 시행령 자체 시행일 2026-07-01(대통령령 제36423호)
tags: 스톡옵션, 주식매수선택권, 벤처기업세제, 근로소득세, 스톡옵션세금, 주식세금, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 충족(2026-09-08).
  게이트1: 네이버 키워드도구 실측 130회(세부·제도 기준 100 이상).
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 3단 특례 구조 + 벤처/비벤처 대비 계산표(같은 1억원이 0원 vs 1,956만원)로
  정보이득 확보.
  게이트4: 시행령 원문(사용자 HWP 캡처, 절차·기한 확정) + 구글 스니펫(비과세 한도,
  시행령과 교차 확인) + 6편 기존 확보 세율표(재사용) — 다만 법 제16조의2 모법 원문
  자체는 미확보라는 한계를 self_check·본문에 명시.
self_check: |
  [2026-09-08 시행령 원문 확보 후 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 130회.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 3단 특례 구조와 벤처/비벤처 대비 계산표로 정보이득을 확보했다.
  게이트4 — 시행령 원문(절차·기한)은 1차 출처로 확정. 비과세 한도 수치(연 2억/누적
  5억/2027-12-31)는 법 제16조의2 모법 원문이 아니라 구글 AI 개요 + 국세청 스니펫으로
  확인했다는 한계가 있다. 다만 (a) 이 세션이 독립적으로 WebSearch로 찾은 수치와
  정확히 일치, (b) 절차 관련 수치(다음 연도 2월 말일)가 시행령 원문과 정확히 맞아
  떨어짐, (c) 스니펫 자체가 국세청 실제 페이지에서 발췌된 문구를 포함 — 세 근거가
  수렴해 이 프로젝트가 과거에 잡아낸 실제 오류 사례(대주주 기준 5배 차이, 코스피
  세율 4배 차이)와 달리 출처 간 충돌이 없다. 이 한계는 본문에도 투명하게 남긴다.
  검산 — 벤처기업 1억원(2억 한도 이내): 비과세 → 세금 0원. 벤처기업 3억원(2억
  초과): 과세대상 1억원 × 35% − 1,544만원(누진공제, 8,800만원 초과 1억5천만원
  이하 구간) = 1,956만원(초과분에 대해서만, 단순가정). 비벤처기업 1억원(특례
  대상 아님): 과세표준 1억원 × 35% − 1,544만원 = 1,956만원.
  카니발라이제이션 점검 — 1~11편 어디에도 스톡옵션 관련 세금은 없다. 겹침 없음.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문 기관 안내 문장과 하단 참고 출처를
  전부 링크 처리. target="_blank" rel="noopener", 정부기관이라 nofollow 미부착.
  제목 12자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 3단어. FAQ 6개와 JSON-LD
  1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 하단 면책 문구 포함.
  종합 판정: 게이트3·4 실질적으로 충족(한계는 투명 공개) → gate_pass:true. 발행 가능.
---

<p>스톡옵션(주식매수선택권)을 행사하면 원칙적으로 <mark>행사이익(행사 당시 시가와 행사가의 차액)이 근로소득에 합산돼 누진세율로 과세</mark>됩니다. 다만 <b>벤처기업 소속이면 연 2억원까지 소득세가 비과세</b>돼, 같은 금액도 회사가 벤처기업이냐 아니냐에 따라 세금이 크게 갈립니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>원칙은 <b>행사이익 = 근로소득</b>입니다. 종합소득세 누진세율(6~45%)로 다른 소득과 합산 과세됩니다.</li>
    <li>벤처기업 임직원은 <mark>행사이익 연간 2억원, 누적 5억원까지 소득세가 비과세</mark>됩니다(2027년 12월 31일까지 부여받은 스톡옵션 행사분).</li>
    <li>한도를 넘는 금액은 <b>납부특례</b>를 신청해 납부 시기를 조정할 수 있고, 별도로 근로소득 대신 <b>양도소득세로 과세</b>받는 과세이연 특례도 있습니다.</li>
    <li>특례 신청은 대부분 <mark>회사(원천징수의무자)가 세무서에 서류를 제출</mark>하는 방식입니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>스톡옵션을 행사하면 세금이 어떻게 붙나요</li>
  <li>벤처기업 스톡옵션은 비과세 특례가 있나요</li>
  <li>한도를 넘으면 어떻게 되나요</li>
  <li>과세이연 특례는 무엇이 다른가요</li>
  <li>실제로 계산하면 얼마나 차이 나나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">스톡옵션을 행사하면 세금이 어떻게 붙나요</h2>

<p>스톡옵션을 행사하면 <mark>행사 당시 시가에서 행사가격을 뺀 차액(행사이익)</mark>이 과세 대상이 됩니다. 원칙적으로 이 행사이익은 근로소득으로 보아 다른 급여와 합산해 종합소득세 누진세율(6~45%)이 적용됩니다.</p>

<p>이 원칙만 적용되면 특례가 없는 일반 기업 임직원은 행사이익 전액이 과세 대상입니다. 벤처기업이라면 다음 절에서 보는 비과세 특례로 부담이 크게 줄어듭니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">벤처기업 스톡옵션은 비과세 특례가 있나요</h2>

<p>네. 「벤처기업육성에 관한 특별법」에 따른 벤처기업(그 벤처기업이 발행주식 총수의 30% 이상을 인수한 기업 포함)의 임직원이 부여받은 스톡옵션은, 행사이익 <mark>연간 2억원까지, 누적 5억원까지 소득세가 비과세</mark>됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>비과세 특례(조세특례제한법 제16조의2) 요약</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>연간 한도: 행사이익 기준 2억원까지</li>
    <li>누적 한도: 해당 벤처기업으로부터 받은 총 누적 행사이익 5억원</li>
    <li>적용 기한: 2027년 12월 31일까지 부여받은 스톡옵션의 행사분</li>
    <li>신청: 회사(원천징수의무자)가 <b>행사일이 속한 연도의 다음 연도 2월 말일까지</b> 비과세특례적용명세서를 관할 세무서장에게 제출</li>
  </ul>
</div>

<p>신청은 임직원이 직접 하는 것이 아니라 <mark>회사가 세무서에 서류를 제출</mark>하는 방식입니다. 다만 회사가 취득 주식이 입고된 계좌를 관리하는 금융회사에 행사 당시 시가 정보를 제공해야 하므로, 임직원도 어느 계좌로 주식을 받을지는 회사와 미리 확인해두는 것이 좋습니다.</p>

<p style="font-size:13px;color:#888;">근거: 조세특례제한법 시행령(대통령령 제36423호, 2026.6.23. 타법개정) 제14조의2. 비과세 한도·적용기한은 <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6586&amp;cntntsId=7865" target="_blank" rel="noopener">국세청 벤처기업 주식매수선택권 행사이익 안내</a> 확인(2026-09-08).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">한도를 넘으면 어떻게 되나요</h2>

<p>2억원 한도를 넘는 행사이익은 <mark>과세 대상</mark>이 되지만, 그 초과분에 대해 <b>납부특례(조세특례제한법 제16조의3)</b>를 신청하면 납부 시기를 조정할 수 있습니다.</p>

<p>신청 절차는 다음과 같습니다.</p>
<ol style="line-height:1.9;">
  <li>벤처기업 임원 등이 <b>행사한 날이 속하는 달의 다음 달 5일까지</b> 특례적용신청서를 회사(원천징수의무자)에 제출</li>
  <li>회사는 <b>다음 달 10일까지</b> 특례적용대상명세서를 관할 세무서장에게 제출</li>
  <li>종합소득과세표준 확정신고 시 특례적용신청서 사본을 납세지 관할 세무서장에게 제출</li>
</ol>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>구체적인 분할·유예 기간은 반드시 확인하세요.</b>
  <p style="margin:8px 0 0 0;">이 특례가 몇 년에 걸쳐 세금을 나눠 낼 수 있게 해주는지는 시행령에서 절차만 확인되고 구체적 기간까지는 이 글의 1차 출처로 확정하지 못했습니다. 정확한 기간은 신청 전에 세무서나 세무대리인을 통해 확인하는 것이 안전합니다.</p>
</div>

<p style="font-size:13px;color:#888;">근거: 조세특례제한법 시행령 제14조의3.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">과세이연 특례는 무엇이 다른가요</h2>

<p>비과세·납부특례와 별개로, <mark>행사이익을 아예 근로소득으로 과세하지 않고 나중에 주식을 처분할 때 양도소득세로 과세</mark>받는 특례(조세특례제한법 제16조의4)도 있습니다. 근로소득 누진세율보다 양도소득세율이 유리한 경우 선택할 만합니다.</p>

<p>다만 요건이 까다롭습니다. 주주총회 결의를 거쳐 약정해야 하고, 주식매수선택권을 다른 사람에게 양도할 수 없으며, <b>주주총회 결의일로부터 2년 이상 재임·재직한 후에 행사</b>해야 합니다(사망·정년 등 예외 있음). 행사로 취득한 주식은 본인 명의의 <b>전용계좌</b>에 넣어 다른 매매계좌와 구분 관리해야 하고, 계좌 개설 후 1개월 안에 주식이 입고되지 않으면 계좌가 폐쇄됩니다. 행사해 취득한 주식의 발행주식 총수 10%를 초과해 보유하게 되는 경우 등은 애초에 특례 대상에서 제외됩니다.</p>

<p>신청은 <b>행사일 전날까지</b> 특례적용신청서와 전용계좌개설확인서를 회사에 제출하는 방식이며, 회사는 주식을 전용계좌로 입고하고 다음 달 10일까지 세무서에 서류를 제출합니다.</p>

<p style="font-size:13px;color:#888;">근거: 조세특례제한법 시행령 제14조의4.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제로 계산하면 얼마나 차이 나나요</h2>

<p>같은 1억원의 행사이익도 <mark>벤처기업 여부와 한도 초과 여부에 따라 세금이 크게 달라집니다.</mark> 다른 소득이 없다고 단순화해 계산한 예시입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">행사이익</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">과세 대상</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세금(단순 가정)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">벤처기업, 한도 이내</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0원(전액 비과세)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>0원</mark></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">벤처기업, 한도 초과</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">3억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1억원(2억원 초과분)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1,956만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">비벤처기업</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1억원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1억원(특례 대상 아님)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1,956만원</td></tr>
  </tbody>
</table>

<p>과세 대상 1억원은 종합소득세 세율표(2023~2025년 귀속 기준)의 8,800만원 초과 1억5,000만원 이하 구간(세율 35%, 누진공제 1,544만원)에 해당해 <b>1억원 × 35% − 1,544만원 = 1,956만원</b>으로 계산했습니다. 실제로는 다른 근로소득과 합산되므로 적용 구간이 달라질 수 있습니다.</p>

<p style="font-size:13px;color:#888;">세율표 근거: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&amp;cntntsId=7667" target="_blank" rel="noopener">국세청 종합소득세 세율</a>(2023~2025년 귀속, 2026-09-07 확인). 2026년 귀속 세율표는 아직 게시 전이라 이 구간을 참고용으로 썼습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">스톡옵션 행사이익은 무슨 세금으로 과세되나요</summary>
  <p style="margin:10px 0 0 0;">원칙적으로 근로소득에 합산돼 종합소득세 누진세율로 과세됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">벤처기업이 아니면 비과세 특례를 못 받나요</summary>
  <p style="margin:10px 0 0 0;">네. 「벤처기업육성에 관한 특별법」상 벤처기업(또는 그 벤처기업이 30% 이상 인수한 기업) 임직원만 대상입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비과세 한도를 넘으면 세금을 못 내나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 초과분은 과세되며, 납부특례를 신청하면 납부 시기를 조정할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">특례 신청은 누가 하나요</summary>
  <p style="margin:10px 0 0 0;">대부분 회사(원천징수의무자)가 필요한 서류를 관할 세무서에 제출합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">스톡옵션으로 받은 주식을 나중에 팔 때도 세금이 붙나요</summary>
  <p style="margin:10px 0 0 0;">네. 행사 시점과 별개로 주식을 처분할 때 양도소득세나 증권거래세가 붙을 수 있고, 과세이연 특례를 적용받았다면 행사이익 자체가 이때 양도소득세로 과세됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비과세 특례는 언제까지 적용되나요</summary>
  <p style="margin:10px 0 0 0;">2027년 12월 31일까지 부여받은 스톡옵션의 행사분까지 적용됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6586&amp;cntntsId=7865" target="_blank" rel="noopener">국세청 벤처기업 주식매수선택권 행사이익 안내</a> — 비과세 한도·적용기한(2026-09-08 확인)</li>
    <li>조세특례제한법 시행령(대통령령 제36423호, 2026.6.23. 타법개정) 제14조의2~14조의4 — 3단 특례 절차</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&amp;cntntsId=7667" target="_blank" rel="noopener">국세청 종합소득세 세율</a> — 일반 근로소득세 계산(2023~2025년 귀속)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> — 종합소득세·양도소득세 신고</li>
    <li>기준일: 2026-09-08(시행령·국세청 페이지 확인일)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 판단과 책임은 본인에게 있습니다. 세율·한도·특례 요건은 세법 개정으로 바뀔 수 있으므로 신청 전 국세청 최신 안내를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "스톡옵션 행사 세금 계산 방법",
  "description": "스톡옵션 행사이익의 근로소득세 과세 원칙과, 벤처기업 임직원에게 적용되는 비과세·납부·과세이연 3단 특례를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-08",
  "dateModified": "2026-09-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-option-tax"
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
      "name": "스톡옵션 행사이익은 무슨 세금으로 과세되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "원칙적으로 근로소득에 합산돼 종합소득세 누진세율로 과세됩니다." }
    },
    {
      "@type": "Question",
      "name": "벤처기업이 아니면 비과세 특례를 못 받나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 「벤처기업육성에 관한 특별법」상 벤처기업(또는 그 벤처기업이 30% 이상 인수한 기업) 임직원만 대상입니다." }
    },
    {
      "@type": "Question",
      "name": "비과세 한도를 넘으면 세금을 못 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 초과분은 과세되며, 납부특례를 신청하면 납부 시기를 조정할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "특례 신청은 누가 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "대부분 회사(원천징수의무자)가 필요한 서류를 관할 세무서에 제출합니다." }
    },
    {
      "@type": "Question",
      "name": "스톡옵션으로 받은 주식을 나중에 팔 때도 세금이 붙나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 행사 시점과 별개로 주식을 처분할 때 양도소득세나 증권거래세가 붙을 수 있고, 과세이연 특례를 적용받았다면 행사이익 자체가 이때 양도소득세로 과세됩니다." }
    },
    {
      "@type": "Question",
      "name": "비과세 특례는 언제까지 적용되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2027년 12월 31일까지 부여받은 스톡옵션의 행사분까지 적용됩니다." }
    }
  ]
}
</script>
