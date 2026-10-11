---
keyword: 증여세 신고기한
title: 증여세 신고기한 계산법과 월별 마감일 2026
slug: gift-tax-filing-deadline-calendar
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 3870 (PC 1290 / 모바일 2580)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3·v4 판정 2026-10-11 - 통과] WebSearch(미국 기준, 참고용) "증여세 신고기한 3개월 신고세액공제" 상위: bznav.com(세무 콘텐츠 사이트 3건) / wikidocs 개인 블로그 2건 / watax.kr(세무 서비스 콘텐츠) / jab-guyver.co.kr(소규모 사이트) / glasswallet.com(핀테크 블로그) / 국세청 PDF 1건.
  1) 진입 여지 - 있음. 개인 블로그와 소규모 콘텐츠 사이트가 상위 대부분이다.
  2) 검색 의도 - "언제까지 신고하나"를 묻는 정보 탐색형. 계산기·신청 도구 의도가 아니다.
  3) 답 완결 - 아님. 상위 글은 "3개월 이내" 한 줄과 예시 한 건이 중심이고, 2026년 증여월별 마감일을 주말·공휴일 보정까지 표로 낸 글, 상장주식 평가기간 종료 뒤 남는 일수, 신고기한을 기준으로 한 반환 시기별 과세 구분을 한 글에 담은 곳은 확인하지 못함(검색 요약 기준, 전수 확인 아님).
  이슈 근거: 연말 증여 시즌(12월 증여는 3월 31일 마감)과 7~10월 증여분 마감이 11월~내년 2월에 몰림.
unique_asset: |
  (a) 증여월별(7월~내년 1월) 신고·납부 마감일 표, 토요일·일요일·삼일절 보정 반영.
  (b) 12월 증여 가상 사례의 일정 타임라인(평가 기간 끝~마감 44일), 증여 1.5억~5억 신고세액공제 3% 막대 그림.
  (c) 신고기한 기준 반환 시기별 과세 구분 표와 사례 날짜 대입.
primary_source: |
  국세청(nts.go.kr)은 자동화 환경에서 WebFetch가 막혀 있어 사람이 2026-09-08 직접 저장한 국세청 증여세 안내 두 페이지(sources/nts-gift-tax-items-raw.txt, nts-gift-tax-calc-flowchart-raw.txt)의 값을 재사용했다(다른 초안에서 같은 출처·같은 기준일로 검증된 값).
  - 세율 5단계·누진공제, 증여재산공제 한도(성년 자녀 5천만원, 10년 합산), 신고세액공제 3%(2019년 이후 증여분, 신고기한까지 신고한 경우), 반환 시기별 과세 방법은 위 국세청 원문 그대로.
  - 신고기한 "증여받은 날이 속하는 달의 말일부터 3개월 이내"와 "기한 후 신고는 신고세액공제 미적용·가산세 가능": 이번 WebSearch에서 서로 무관한 사이트 5곳 이상(bznav, wikidocs 2건, watax, jab-guyver, glasswallet)이 같은 내용을 적었고 국세청 상속·증여 세금상식 PDF도 검색됨. 이미 발행된 주식 증여세 글에서도 같은 기한을 사용.
  - 마감일이 토요일·공휴일이면 다음 날: 같은 검색 결과에서 확인(국세기본법의 기한 특례 취지). 달력 계산은 날짜 산술이라 수학적 사실.
  - 상속세및증여세법 조문 번호(제68조 등)는 원문을 열람하지 못해 본문에서 번호를 쓰지 않았다.
기준일: 2026년 10월 11일 기준
refresh_due: 2026-12-31
refresh_reason: "연말 증여 시즌 종료 후 내년 증여월별 마감일 표를 2027년 증여분으로 교체하고 법령 개정 반영 여부 재확인"
tags: 증여세 신고기한, 증여세 신고 마감일, 증여세 신고세액공제, 증여세 기한후신고, 주식 증여 신고, 증여 반환 기한, 12월 증여 신고기한, 증여재산공제, 증여세 3개월, 증여세 납부기한
cannibalization_note: |
  주식 증여세 계산 방법 글은 평가 방법과 세액 계산 중심이고, 이 글은 신고·납부 마감일 계산과 월별 달력, 기한 안 신고 효과, 반환 시기 구분에 집중한다. 기한후신고 가산세 계산은 별도 글 영역이라 이 글에서 다루지 않는다. 주식 증여세 글과 상속세 신고기한 글로 내부 링크.
gate_pass: true
gate_pass_note: |
  게이트1 3,870회(세부·제도 100 이상). 게이트2 v3·v4 통과. 게이트3 월별 마감일 달력표, 신고세액공제 계산, 반환 시기 표. 게이트4는 국세청 원문 값 재사용(9/8 사람 캡처)과 신고기한 규정의 다수 출처 일치로 처리, 세율·공제는 이전에 확정된 값이라 새 수치 없음. 사람은 발행 전 국세청 증여세 신고 안내에서 "말일부터 3개월" 문구만 눈으로 확인하면 충분하다.
self_check: |
  [2026-10-11 gate_pass:true]
  후보 경위: 이슈 스캔(서머타임 종료·공모주·증시 일정은 이미 125·133·129편으로 발행/대기) 후 12개 실측(테슬라 실적발표 250·애플 20·미국 소매판매 180·사이드카 20·FOMC 일정 20 등 탈락, 미국 고용보고서 910·마이크로소프트 실적발표 920은 임계값 간신히 통과, 배당락일 3,210은 16편과 겹쳐 갱신 대상, 증여세 신고기한 3,870이 최대 통과). 연말 증여 시즌(7~10월 증여분 마감 11월~2월)이 시의성 근거.
  YMYL: 특정 종목·증여 시점 추천 없음, 사례 숫자는 전부 가상으로 표시, 세율·공제는 국세청 확정값 재사용.
  첫 문장 유형: 문제제기형("신고기한이 일요일이면 언제까지인가"). 직전 147 절차형, 146 정의형, 145 정의형과 다름.
  글 구조 유형: 계산형(첫 H2 바로 아래가 마감일 계산 박스, 설명 문단보다 먼저). 직전 147 절차형, 146 비교형과 다름.
  어투 모드: C 사례형(가상 인물 A씨가 12월 15일에 증여받는 시나리오를 끝까지 따라감, 가상임을 명시). 직전 147 B, 146 A와 다름. 꾸며낸 1인칭 경험 없음.
  기관 안내 문장 홈택스·국세청 링크 처리, 출처 목록 전부 링크 처리.
  내부 링크: 주식 증여세 계산 방법(11, published)·미국주식 세금 종류와 상속세 주의점(15, published)·상속세 신고기한과 가산세 2026(36, published).
  AI 티 점검: em대시 0개, 다만 0회, mark 4개, FAQ 5개(직전 147은 4개, 146은 5개), FAQ 헤딩 "달력 앞에서 멈칫하는 순간"(신규), 요약박스 제목 "🗓 마감 전에 달력에 적어 둘 것"(적갈색 신규), H2 5개 중 질문형 3개.
figure_plan: |
  2장
  1: 12월 15일 증여 사례의 일정 타임라인(증여일, 평가 기간 끝, 신고·납부 마감과 기한 후 신고 구간)
  2: 증여 규모별 신고세액공제 3% 크기 막대(30만~240만원)
  월별 마감일 표와 반환 시기 표는 날짜·구분을 정확히 읽어야 해서 표로 유지.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-11</p>

<p>신고기한이 일요일이면 언제까지 내야 할까요? 증여세 신고기한은 증여받은 날이 속하는 달의 말일부터 3개월 이내이고, 마지막 날이 토요일이나 공휴일이면 다음 날까지입니다.</p>

<div style="background:#fff7ed;border:2px solid #b45309;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#92400e;font-size:18px;">🗓 마감 전에 달력에 적어 둘 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>10월에 증여받았다면 마감은 1월 31일이 아니라 2027년 2월 1일(월)입니다.</li>
    <li>기한 안에 신고하면 산출세액의 3%를 깎아 주고, 하루만 넘겨도 이 공제가 없습니다.</li>
    <li>주식을 받았다면 증여받은 뒤 2개월 종가 평균이 끝난 다음에도 마감까지 한 달 넘게 남습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">증여세 신고기한 계산법, 월별 마감일 표</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">마감일이 주말이나 공휴일이면 어떻게 되나요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">12월 15일에 주식을 받은 A씨의 일정표</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">기한 안에 신고하면 3%는 얼마나 깎이나요</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">신고기한이 주식 투자자에게 중요한 이유</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">증여세 신고기한 계산법, 월별 마감일 표</h2>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>🧮 계산 순서</strong>
  <ol style="margin:8px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>증여받은 날이 속한 달의 말일을 찾습니다.</li>
    <li>그 말일에서 3개월을 더합니다. 이 날이 법정 신고·납부 마감일입니다.</li>
    <li>그 날이 토요일이나 공휴일이면 다음 날로 미룹니다.</li>
  </ol>
</div>

<p>신고기한은 증여받은 날부터 90일이 아니라 <mark>증여받은 달의 말일부터 3개월</mark>입니다. 같은 달 안에서는 1일에 받든 31일에 받든 마감일이 같습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">증여받은 달</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">말일부터 3개월</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">실제 마감일</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 7월</td><td style="border:1px solid #ddd;padding:8px;">10월 31일(토)</td><td style="border:1px solid #ddd;padding:8px;">11월 2일(월)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 8월</td><td style="border:1px solid #ddd;padding:8px;">11월 30일(월)</td><td style="border:1px solid #ddd;padding:8px;">11월 30일(월)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 9월</td><td style="border:1px solid #ddd;padding:8px;">12월 31일(목)</td><td style="border:1px solid #ddd;padding:8px;">12월 31일(목)</td></tr>
    <tr style="background:#fff7ed;"><td style="border:1px solid #ddd;padding:8px;">2026년 10월</td><td style="border:1px solid #ddd;padding:8px;">2027년 1월 31일(일)</td><td style="border:1px solid #ddd;padding:8px;">2027년 2월 1일(월)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 11월</td><td style="border:1px solid #ddd;padding:8px;">2027년 2월 28일(일)</td><td style="border:1px solid #ddd;padding:8px;">2027년 3월 2일(화)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026년 12월</td><td style="border:1px solid #ddd;padding:8px;">2027년 3월 31일(수)</td><td style="border:1px solid #ddd;padding:8px;">2027년 3월 31일(수)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2027년 1월</td><td style="border:1px solid #ddd;padding:8px;">2027년 4월 30일(금)</td><td style="border:1px solid #ddd;padding:8px;">2027년 4월 30일(금)</td></tr>
  </tbody>
</table>

<p>2026년 11월 증여분이 눈에 띕니다. 2월 28일이 일요일이고 다음 날 3월 1일이 삼일절이라 마감이 3월 2일까지 밀립니다.</p>

<p>신고와 납부는 같은 날까지입니다. <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>에서 전자신고하면 세금 납부까지 한 번에 할 수 있습니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">마감일이 주말이나 공휴일이면 어떻게 되나요</h2>

<p><mark>마지막 날이 토요일이나 공휴일이면 다음 날이 마감</mark>입니다. 위 표에서 7월, 10월, 11월 증여분이 이 보정을 받았습니다.</p>

<ul>
  <li>토요일이나 일요일이 마감일이면 다음 월요일까지입니다.</li>
  <li>월요일이 공휴일이면 다음 평일(화요일)까지입니다.</li>
  <li>보정은 마지막 날 하나에만 적용되고, 3개월을 다시 세지 않습니다.</li>
</ul>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 표에 없는 달은 이렇게</strong>
  <p style="margin:8px 0 0 0;">1월 증여분처럼 표에 없는 달은 말일에 3개월을 더해 날짜를 구한 뒤, 달력에서 요일만 보면 됩니다. 임시공휴일이 생기면 마감도 하루 밀릴 수 있으니 신고 직전에 홈택스 공지를 함께 보세요.</p>
</div>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">12월 15일에 주식을 받은 A씨의 일정표</h2>

<p>아래 사례는 설명용으로 만든 가상 인물입니다. 직장인 A씨(성년)가 2026년 12월 15일에 부모님에게서 상장주식 1억 5천만원어치를 받는다고 가정해 볼게요.</p>

<ul>
  <li>증여받은 달은 12월이라 말일은 12월 31일이고, 여기에 3개월을 더한 2027년 3월 31일(수)이 마감입니다.</li>
  <li>상장주식은 증여일 전후 각 2개월의 종가 평균으로 평가하므로 평가 기간은 2027년 2월 15일에 끝납니다.</li>
  <li>평가 기간이 끝난 뒤 <mark>마감까지 44일</mark>이 남습니다.</li>
</ul>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/gift-tax-filing-deadline-calendar-1.png" alt="12월 15일 증여 가상 사례 타임라인. 12월 15일 증여, 2월 15일 평가 기간 끝, 3월 31일 신고 납부 마감, 4월 1일부터 기한 후 신고" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 국세청 증여세 안내와 날짜 계산, 2026-10-11 (가상 사례)</figcaption></figure>

<p>평가 방법은 <a href="https://sensitiveboss3.tistory.com/entry/stock-gift-tax" target="_blank" rel="noopener">주식 증여세 계산 방법</a> 글에서 숫자까지 풀어 두었습니다. 증여 날짜만 다르게 잡아도 마감일 표 한 줄이 바뀝니다.</p>

<p>신고 날짜를 지나서 증여 재산을 돌려주는 경우에는 마감일이 또 하나의 기준선이 됩니다. 국세청은 반환 시점을 신고기한과 비교해 과세 방법을 달리 안내합니다. 아래 표는 금전이 아닌 재산(주식 등)에 해당합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">반환 시기</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">A씨 사례 날짜</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">증여세 과세</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">신고기한 이내</td><td style="border:1px solid #ddd;padding:8px;">2027년 3월 31일까지</td><td style="border:1px solid #ddd;padding:8px;">당초 증여와 반환 모두 과세하지 않음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기한 경과 후 3개월 이내</td><td style="border:1px solid #ddd;padding:8px;">4월 1일~6월 30일</td><td style="border:1px solid #ddd;padding:8px;">당초 증여는 과세, 반환은 과세하지 않음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기한 경과 후 3개월 초과</td><td style="border:1px solid #ddd;padding:8px;">7월 1일부터</td><td style="border:1px solid #ddd;padding:8px;">당초 증여와 반환 모두 과세</td></tr>
  </tbody>
</table>

<p>금전은 반환 시기와 관계없이 당초 증여와 반환에 모두 과세합니다. 국세청 증여세 안내 기준입니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">기한 안에 신고하면 3%는 얼마나 깎이나요</h2>

<p>기한 안에 신고하면 <mark>산출세액의 3%를 공제</mark>합니다. 국세청은 2019년 이후 증여분에 3%를 적용한다고 안내하고, 2018년 증여분은 5%였습니다.</p>

<p>A씨의 세금은 이렇게 계산됩니다. 모든 금액은 가상 사례입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;text-align:right;">금액</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">증여재산가액</td><td style="border:1px solid #ddd;padding:8px;text-align:right;">150,000,000원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">증여재산공제(성년 자녀)</td><td style="border:1px solid #ddd;padding:8px;text-align:right;">−50,000,000원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">과세표준</td><td style="border:1px solid #ddd;padding:8px;text-align:right;">100,000,000원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">산출세액(1억원 이하 10%)</td><td style="border:1px solid #ddd;padding:8px;text-align:right;">10,000,000원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">신고세액공제(3%)</td><td style="border:1px solid #ddd;padding:8px;text-align:right;">−300,000원</td></tr>
    <tr style="background:#fff7ed;"><td style="border:1px solid #ddd;padding:8px;"><b>납부할 세액</b></td><td style="border:1px solid #ddd;padding:8px;text-align:right;"><b>9,700,000원</b></td></tr>
  </tbody>
</table>

<p>3월 31일을 넘겨 기한 후 신고를 하면 이 30만원 공제가 없고 가산세가 붙을 수 있습니다. 증여 규모가 클수록 공제액이 커집니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/gift-tax-filing-deadline-calendar-2.png" alt="신고세액공제 3% 크기. 증여 1억 5천만원 30만원, 2억원 60만원, 3억원 120만원, 5억원 240만원" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 국세청 증여세 세율·신고세액공제 기준으로 계산, 2026-10-11 (성년 자녀 공제 5천만원 가정)</figcaption></figure>

<p>세율 구간과 누진공제는 <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2340&amp;cntntsId=7728" target="_blank" rel="noopener">국세청 증여세 세액계산 흐름도</a>의 기본세율을 따랐습니다. 증여 5억원 사례는 과세표준 4억 5천만원에 20%와 누진공제 1천만원을 적용해 산출세액 8,000만원을 구한 뒤 3%를 곱한 값입니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">신고기한이 주식 투자자에게 중요한 이유</h2>

<p>주식은 증여일 종가가 아니라 전후 4개월 평균으로 평가해서 신고 날짜를 잘못 잡으면 숫자까지 달라집니다. 신고기한은 평가 기간이 끝난 뒤에야 의미 있는 숫자가 나오는 구조입니다.</p>

<ul>
  <li>평가액이 확정된 뒤 신고하더라도 마감 전이면 3% 공제를 받습니다.</li>
  <li>마감 직전에 몰려 신고하면 홈택스 접속이 느려질 수 있어 며칠 앞서 마치는 편이 낫습니다.</li>
  <li>같은 증여자에게서 10년 안에 받은 재산은 합산하고 공제 한도도 합쳐 적용하므로, 12월과 1월로 나눠 받아도 한도는 같이 소진됩니다.</li>
</ul>

<p>미국 주식을 증여받거나 해외 상속이 얽히면 확인할 항목이 더 많아집니다. 그 경우는 <a href="https://sensitiveboss3.tistory.com/entry/us-stock-tax" target="_blank" rel="noopener">미국주식 세금 종류와 상속세 주의점</a> 글을, 기한이 6개월로 달라지는 상속은 <a href="https://sensitiveboss3.tistory.com/entry/inheritance-tax-deadline-penalty" target="_blank" rel="noopener">상속세 신고기한과 가산세</a> 글을 보면 됩니다.</p>

<h2 style="border-left:6px solid #b45309;padding-left:12px;margin-top:36px;">달력 앞에서 멈칫하는 순간</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증여세 신고기한은 증여일부터 90일인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 증여받은 날이 속하는 달의 말일부터 3개월이라, 같은 달에 받으면 며칠에 받았든 마감일이 같습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">마감일에 세금을 못 내면 신고만 해도 되나요</summary>
  <p style="margin:10px 0 0 0;">신고와 납부는 같은 기한이라 신고만 하고 납부를 미루면 이자 성격의 가산세가 붙을 수 있습니다. 세액이 크다면 홈택스에서 납부 방법을 먼저 알아보세요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">기한을 놓치면 신고세액공제 3%는 받을 수 없나요</summary>
  <p style="margin:10px 0 0 0;">받을 수 없습니다. 기한 후 신고에는 신고세액공제가 적용되지 않고 가산세가 붙을 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신고기한이 지난 뒤 받은 주식을 돌려주면 세금이 없어지나요</summary>
  <p style="margin:10px 0 0 0;">기한 경과 후 3개월 이내 반환이면 당초 증여는 과세되고 반환만 과세되지 않습니다. 기한 안에 돌려줘야 당초 증여까지 과세되지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">12월 31일에 받은 주식과 1월 1일에 받은 주식은 신고기한이 같나요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 12월 31일 증여분은 3월 31일, 1월 1일 증여분은 4월 30일이 마감입니다. 공제 한도는 10년 합산이라 두 증여가 같은 한도를 나눠 씁니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6533&amp;cntntsId=7960" target="_blank" rel="noopener">국세청 증여세 항목별 설명</a> - 신고세액공제 3%, 증여재산공제 한도, 반환 시기별 과세(2026-09-08 확인)</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2340&amp;cntntsId=7728" target="_blank" rel="noopener">국세청 증여세 세액계산 흐름도</a> - 세율 5단계와 누진공제(2026-09-08 확인)</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 상속세및증여세법 신고기한 규정</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> - 증여세 전자신고와 납부</li>
  </ul>
  기준일: 2026년 10월 11일. 신고기한과 월별 마감일은 법정 기한을 달력으로 계산한 값이며, 임시공휴일 지정 등으로 하루 정도 달라질 수 있습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 증여세 신고 일정을 안내하는 정보 글로, 특정 종목이나 상품을 사고팔라는 뜻이 아닙니다. 투자와 증여 판단, 그 결과는 본인 책임입니다. 세율, 공제, 기한은 바뀔 수 있으니 신고 전에 국세청 안내의 최신 내용을 기준으로 삼아 주세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "증여세 신고기한 계산법과 월별 마감일 2026",
  "description": "증여세 신고기한은 증여받은 달 말일부터 3개월입니다. 2026년 증여월별 마감일 표, 주말·공휴일 보정, 12월 증여 사례와 신고세액공제 3% 계산을 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/gift-tax-filing-deadline-calendar-1.png",
  "author": {"@type": "Person", "name": "센시티브보스"},
  "publisher": {"@type": "Person", "name": "센시티브보스"},
  "datePublished": "2026-10-11",
  "dateModified": "2026-10-11",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://sensitiveboss3.tistory.com/entry/gift-tax-filing-deadline-calendar"}
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "증여세 신고기한은 증여일부터 90일인가요", "acceptedAnswer": {"@type": "Answer", "text": "아닙니다. 증여받은 날이 속하는 달의 말일부터 3개월이라, 같은 달에 받으면 며칠에 받았든 마감일이 같습니다."}},
    {"@type": "Question", "name": "마감일에 세금을 못 내면 신고만 해도 되나요", "acceptedAnswer": {"@type": "Answer", "text": "신고와 납부는 같은 기한이라 신고만 하고 납부를 미루면 이자 성격의 가산세가 붙을 수 있습니다. 세액이 크다면 홈택스에서 납부 방법을 먼저 알아보세요."}},
    {"@type": "Question", "name": "기한을 놓치면 신고세액공제 3%는 받을 수 없나요", "acceptedAnswer": {"@type": "Answer", "text": "받을 수 없습니다. 기한 후 신고에는 신고세액공제가 적용되지 않고 가산세가 붙을 수 있습니다."}},
    {"@type": "Question", "name": "신고기한이 지난 뒤 받은 주식을 돌려주면 세금이 없어지나요", "acceptedAnswer": {"@type": "Answer", "text": "기한 경과 후 3개월 이내 반환이면 당초 증여는 과세되고 반환만 과세되지 않습니다. 기한 안에 돌려줘야 당초 증여까지 과세되지 않습니다."}},
    {"@type": "Question", "name": "12월 31일에 받은 주식과 1월 1일에 받은 주식은 신고기한이 같나요", "acceptedAnswer": {"@type": "Answer", "text": "다릅니다. 12월 31일 증여분은 3월 31일, 1월 1일 증여분은 4월 30일이 마감입니다. 공제 한도는 10년 합산이라 두 증여가 같은 한도를 나눠 씁니다."}}
  ]
}
</script>
