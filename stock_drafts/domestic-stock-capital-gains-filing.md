---
keyword: 국내주식 양도소득세 신고방법
title: 국내주식 양도소득세 신고방법 2026
slug: domestic-stock-capital-gains-filing
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 140 (PC 50 / 모바일 90)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-14 — 통과]
  WebSearch "국내주식 양도소득세 신고방법 대주주 홈택스 예정신고" +
  "양도소득세 대주주 국내주식 예정신고 확정신고 방법 세무사" 상위 종합:
  help-me.kr(로펌 콘텐츠, 다만 해외주식 위주) / securities.koreainvestment.com(한국투자증권
  공식 공지) / eiec.kdi.re.kr(KDI 경제교육·정보센터, 준정부) / zuzu.network(스타트업
  서비스 콘텐츠 — 17·26·27·29·31·32편에서도 확인된 유형) / imfnsec.com(세무법인 PDF
  가이드) / mt.co.kr(머니투데이, 언론) / heumtax.com(세무법인 콘텐츠) /
  bintree.co.kr(개인·소규모 세무 블로그) / joseplus.com(조세전문 언론) /
  samili.com(삼일 계열 세무회계 뉴스) / money.make2t.kr(개인 블로그, "총정리"형)
  1) 진입 여지 — 있음. zuzu.network·bintree.co.kr·money.make2t.kr 등 개인/소규모
     콘텐츠가 상위권에 다수 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색+절차 확인("어떻게 신고하나"). 홈택스 자체는 로그인 서비스라
     검색결과 상위에 노출되지 않고, 계산기·조회 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 아니다. 상위 결과 대부분이 "해외주식" 신고 가이드에 치우쳐 있고,
     "국내 상장주식은 대주주만 낸다"는 전제를 못박은 뒤 그 대주주가 실제로 무엇을
     준비해 어디서 신고하는지(신고서식명, 전자신고/서면신고 두 경로, 국내주식은 종목코드만
     기재하면 된다는 점)까지 국내주식에 특화해 정리한 글이 드물다. 무신고가산세·
     납부지연가산세의 2026년 개정(일 단위→월 단위 이원화)을 반영한 글도 못 찾음.
     정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-14]
  (a) "국내 상장주식 양도소득세는 대주주 등 과세대상자만 신고한다"는 전제를 7편(대주주
      요건)과 명확히 연결해, 상위 검색 결과 다수가 국내·해외를 뭉뚱그려 설명하는 혼란을
      해소한다.
  (b) 예정신고 대상자의 두 가지 신고 경로 — 전자신고(홈택스·손택스) vs 주소지 관할
      세무서 서면신고 — 를 구체적으로 정리. 신고서식명(소득세법 시행규칙 별지 제84호
      서식 "양도소득과세표준 신고 및 납부계산서")과, 국내주식은 종목코드, 해외주식은
      국제증권식별번호(ISIN코드)를 기재해야 한다는 실무 차이까지 명시한 글은 상위
      검색 결과에 없었다.
  (c) 예정신고를 놓쳤을 때의 실제 불이익을 가상 숫자(과세표준 3,000만원 가정)로
      계산 예시까지 보여준다 — 무신고가산세 20% + 납부지연가산세. 특히 2026년 7월 1일부터
      납부지연가산세 계산 방식이 지정납부기한 경과분부터 일 단위(10만분의22)에서
      월 단위(1만분의67)로 바뀐 최신 제도 변경을 반영한 글은 상위 검색 결과에 없었다.
  (d) 2편(주식 매도 세금)·7편(대주주 요건)·5편(해외주식 양도소득세 신고 방법)으로
      역할을 나눠 상호 링크 — 세액 계산은 2편, 대주주 판정은 7편, 해외주식 신고는
      5편, 이 글은 "국내주식 신고 실무"만 담당해 카니벌라이제이션을 피한다.
primary_source: |
  1차 시도: 국세청(nts.go.kr) 양도소득세 개요·서식 안내 페이지에 WebFetch 1회 시도 →
  EGRESS_BLOCKED(2026-09-14). 대조군으로 무관한 도메인(www.google.com)에도 WebFetch
  1회 추가 시도 → 동일하게 EGRESS_BLOCKED, 이 세션 전면 차단으로 확인(RULES.md에
  누적 기록된 기존 패턴과 일치).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12)
  기준 적용 — 두 갈래로 나눠 판단했다.
  ① 예정신고 기한(반기말+2개월)·확정신고(다음해 5월)·세율표(20%/25%/30%, 3억원
     구간)는 이미 이 시리즈 2편·7편에서 법제처·국세청 원문으로 확정한 값의 재사용이라
     신규 검증이 필요 없다.
  ② 신고서식명(별지 제84호서식)과 전자신고/서면신고 경로, 종목코드·ISIN코드 기재
     구분은 law.go.kr(서식 다운로드 페이지 존재 확인), nts.go.kr 서식 안내 하위페이지,
     신한투자증권 공식 파일(file.shinhansec.com PDF), help.jobis.co(세무 서비스
     고객센터) 등 서로 무관한 4곳 이상이 동일하게 서술해 충돌 없이 일치했다.
  ③ 무신고가산세 20%·납부지연가산세의 2026-07-01 개정(일 단위 10만분의22 →
     월 단위 1만분의67 이원화)은 세율·구간 수치라 RULES.md가 원문 확정을 특히
     강조하는 유형이나, 자동화 WebFetch로 국세기본법 원문(law.go.kr)에 직접
     접근하지 못해 아래처럼 서로 무관한 5곳 이상 출처로 교차검증했다:
     - casenote.kr — 국세기본법 제47조의4(납부지연가산세) 조문 자체를 인용
     - easyzetec.com·enjoytax.net — 개인/소규모 세무 콘텐츠, 2026-07-01 시행일과
       세율(일 10만분의22 → 월 1만분의67)을 동일하게 서술
     - joseilbo.com — 조세전문 언론, 관련 가산세 인하 배경 보도
     - nts.go.kr 서식·가산세 안내 하위페이지(WebSearch 스니펫으로 20% 무신고가산세
       확인, 직접 열람은 불가)
     5곳 모두 핵심 수치(20%, 개정 시행일 2026-07-01, 개정 전후 세율)에서 충돌이 없어
     교차검증으로 진행했다. 다만 국세기본법 원문 전문을 직접 확인하지 못한 한계는
     self_check에 투명 공개하고, 본문에도 "정확한 가산세액은 홈택스가 자동 계산하니
     참고용으로만 보라"는 안내를 덧붙였다.
기준일: 2026-09-14 (WebSearch 확인일. 납부지연가산세 계산방식 개정 시행일 2026-07-01)
tags: 국내주식양도소득세, 양도소득세신고, 예정신고, 확정신고, 대주주양도세, 홈택스신고, 무신고가산세, 주식초보, 양도소득과세표준신고서
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-14).
  게이트1: check-keywords.yml 실측 140회(세부·제도 기준 100회 이상). 같은 배치에서
  함께 확인한 "ETF 분배금 세금"(280회, 이 배치 중 최고)은 23편(국내상장 해외ETF 세금)이
  이미 "분배금은 얼마나 떼나요" H2로 매매차익·분배금 배당소득세 15.4% 원천징수를
  상세히 다루고 있어 카니벌라이제이션으로 판단해 제외, backlog에 기록.
  게이트2: v3 기준 통과(serp_check 참조 — 개인/소규모 콘텐츠 다수 진입, 상위 결과가
  해외주식 위주로 치우쳐 국내주식 특화 절차 정보이득 여지 뚜렷).
  게이트3: 대주주 전제 명확화 + 신고서식명·경로 구분 + 무신고가산세 계산 예시(2026년
  개정 반영)로 상위 검색 결과에 없는 정보이득 확보.
  게이트4: nts.go.kr·google.com 각 1회 WebFetch 시도 모두 EGRESS_BLOCKED 확인 후,
  기존 확정값 재사용 + 서식·절차는 4곳 이상 교차검증 + 가산세 개정은 5곳 이상
  교차검증(법조문 인용 1곳 포함)으로 진행. 한계는 self_check에 투명 공개.
self_check: |
  [2026-09-14 최종 판정]
  게이트1 충족 — check-keywords.yml 실측 140회(2026-09-14, 세부·제도 키워드 기준
  100회 이상). 같은 배치의 "IRP 중도인출 세금"(60)·"밸류업 지수 편입기준"(20)·
  "신용거래 미수금 뜻"(20)·"배당소득 분리과세 신청방법"(40)·"넥스트레이드
  거래방법"(100, 일반 기준 500 미달)은 전부 FAIL로 backlog.failed_gate1에 기록.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 상위 검색 결과가 해외주식 위주로 치우친 빈틈을 국내주식 특화 절차
  정보(신고서식명·경로 구분·가산세 계산 예시·2026년 개정)로 메웠다.
  게이트4 — nts.go.kr·google.com에 각 1회 WebFetch 시도해 모두 EGRESS_BLOCKED
  확인(2026-09-14, 세션 전면 차단 패턴과 일치). RULES.md 2026-09-12 기준에 따라
  절차·서식은 이미 확정된 값 재사용 또는 4곳 이상 교차검증, 가산세율 개정은
  법조문(국세기본법 제47조의4) 인용 출처를 포함한 5곳 이상 교차검증으로 진행했다.
  국세기본법 원문 전문 자체는 직접 열람하지 못한 한계가 있어, 본문에 "정확한
  가산세액은 홈택스에서 확인하라"는 안내를 덧붙여 단정을 피했다.
  카니벌라이제이션 점검 — 2편(주식 매도 세금)은 세액 계산과 신고 일정을 한 줄로만
  언급하고 신고서식·경로·가산세는 다루지 않는다. 7편(대주주 요건)은 본문에서
  명시적으로 "세율·계산·신고 절차는 별도 글(2편)로 안내한다"고 이 글의 존재를
  예비해 두었다. 5편(해외주식 양도소득세 신고 방법)은 해외주식 전용이라 대상이
  다르다. 따라서 이 글은 새 영역(국내주식 신고 실무)을 채우는 것이지 기존 편과
  겹치지 않는다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 홈택스·국세청·국가법령정보센터를
  안내하는 자리와 하단 참고 출처 전부 target="_blank" rel="noopener"로 링크 처리.
  law.go.kr의 개별 서식 다운로드 URL은 WebSearch 스니펫에서만 확인되고 RULES.md
  기관 링크 표에 없어, 지어내지 않고 국가법령정보센터 메인 도메인(표에 등재된 URL)만
  링크했다.
  제목 20자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 5단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음
  (가산세액은 "정확한 금액은 홈택스에서 확인" 안내로 단정 회피). 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4 세부 가산세율은 교차검증으로 대체, 한계
  투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-14</p>

<p><mark>국내 상장주식 양도소득세는 대주주 등 과세대상자만 신고합니다.</mark> 소액주주는 증권거래세만 내고 신고할 게 없지만, 대주주에 해당하면 반기별 예정신고와 다음 해 확정신고를 직접 챙겨야 합니다. 이 글은 신고 대상 확인부터 실제 신고 경로, 놓쳤을 때의 불이익까지 절차 중심으로 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>국내 상장주식은 <b>대주주·비상장주식 보유자</b>만 양도소득세를 신고합니다. 소액주주는 신고할 필요가 없습니다.</li>
    <li>신고는 <mark>주식을 판 반기의 말일부터 2개월 이내 예정신고</mark>, 다음 해 <b>5월 1일~31일 확정신고</b> 두 단계입니다.</li>
    <li>신고 경로는 <b>전자신고(홈택스·손택스)</b> 또는 <b>주소지 관할 세무서 서면신고</b> 중 하나를 고르면 됩니다.</li>
    <li>예정신고를 놓치면 <mark>무신고가산세 20%에 납부지연가산세까지 추가</mark>로 붙습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>국내주식 양도소득세는 누가 신고하나요</li>
  <li>예정신고와 확정신고, 언제 하나요</li>
  <li>신고는 실제로 어떻게 하나요</li>
  <li>신고를 놓치면 어떻게 되나요</li>
  <li>해외주식 신고와는 뭐가 다른가요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">국내주식 양도소득세는 누가 신고하나요</h2>

<p>국내 상장주식을 증권시장 안에서 파는 <b>소액주주는 원칙적으로 양도소득세 신고 대상이 아닙니다.</b> 신고 의무가 생기는 쪽은 <mark>대주주(코스피 1%·50억원, 코스닥 2%·50억원, 코넥스 4%·50억원 등)와 비상장·장외거래 양도자</mark>입니다.</p>

<p>본인이 대주주 요건에 해당하는지부터 확인해야 이 글이 필요한지 알 수 있습니다. 지분율·보유금액 기준과 판정 시점은 <a href="https://sensitiveboss3.tistory.com/entry/stock-capital-gains-tax-target" target="_blank" rel="noopener">주식 양도소득세 대주주 요건</a> 글에서 자세히 정리했습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">예정신고와 확정신고, 언제 하나요</h2>

<p>국내주식 양도소득세는 <b>두 단계</b>로 신고합니다. 먼저 <mark>주식을 판 반기(1~6월, 7~12월)의 말일부터 2개월 이내에 예정신고</mark>를 하고 세액을 냅니다. 이후 같은 해에 여러 번 양도해 세액이 달라지면 <mark>다음 해 5월 1일부터 31일까지 확정신고</mark>로 정산합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">신고 기한</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">예정신고(상반기 양도분)</td>
      <td style="border:1px solid #ddd;padding:8px;">8월 31일까지</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">예정신고(하반기 양도분)</td>
      <td style="border:1px solid #ddd;padding:8px;">다음 해 2월 말일까지</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">확정신고(전체 정산)</td>
      <td style="border:1px solid #ddd;padding:8px;">다음 해 5월 1일~31일</td>
    </tr>
  </tbody>
</table>

<p>세율표와 실제 세액 계산 예시(과세표준 구간별 20%·25%·30%)는 <a href="https://sensitiveboss3.tistory.com/entry/stock-sell-tax-amount" target="_blank" rel="noopener">주식 매도 세금 얼마</a> 글에 정리해 두었으니, 이 글은 계산이 끝난 다음의 "신고 실무"에만 집중합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고는 실제로 어떻게 하나요</h2>

<p>신고 경로는 두 가지 중 하나를 고르면 됩니다.</p>

<ul style="line-height:1.9;">
  <li><b>전자신고</b>: <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> 웹사이트나 손택스(모바일 앱)에 공동인증서·간편인증으로 로그인해 [세금신고 → 양도소득세 신고]에서 진행합니다.</li>
  <li><b>서면신고</b>: 주소지 관할 세무서를 방문해 서류로 접수합니다.</li>
</ul>

<p>이때 쓰는 서식은 <mark>소득세법 시행규칙 별지 제84호서식 「양도소득과세표준 신고 및 납부계산서」</mark>입니다. 종목별 양도가액·취득가액·필요경비를 적어야 하는데, <b>국내주식은 종목코드</b>를, 해외주식은 국제증권식별번호(ISIN코드)를 기재한다는 점이 실무에서 자주 헷갈리는 부분입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>준비할 것</b>
  <p style="margin:8px 0 0 0;">증권사 거래내역서(양도가액·취득가액 확인용), 신고인 기본정보, 대주주 판정 근거자료(지분율·보유금액)를 미리 준비해두면 신고서 작성이 수월합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고를 놓치면 어떻게 되나요</h2>

<p>예정신고·확정신고를 하지 않으면 <mark>무신고가산세(내야 할 세액의 20%)</mark>가 붙고, 여기에 <b>납부지연가산세</b>가 추가됩니다.</p>

<p>납부지연가산세는 2026년 7월 1일부터 계산 방식이 바뀌었습니다. <b>지정납부기한까지는 1일 10만분의22(약 0.022%)</b>, <b>그 이후부터는 월 1만분의67(약 0.67%)</b>로 이원화됐습니다. 정확한 가산세액은 홈택스가 자동으로 계산해주니, 아래 예시는 대략적인 규모를 가늠하는 용도로만 참고하세요.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시</b>
  <p style="margin:8px 0 0 0;">과세표준 3,000만원(세율 20% 구간)이라면 양도소득세는 <mark>600만원</mark>입니다. 예정신고를 놓쳐 2개월 늦게 신고·납부했다면 무신고가산세 20%(120만원)에 납부지연가산세(월 1만분의67 기준 2개월분 약 8만원)가 더해져, <mark>대략 128만원의 가산세가 추가</mark>로 붙습니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외주식 신고와는 뭐가 다른가요</h2>

<p>해외주식은 <b>예정신고 의무가 없습니다.</b> 대주주 여부와 상관없이 다음 해 5월 확정신고만 하면 되고, 신고서식에는 종목코드 대신 <b>ISIN코드</b>를 적습니다. 해외주식 신고 절차는 <a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing" target="_blank" rel="noopener">해외주식 양도소득세 신고 방법</a> 글에서 따로 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 다시 한 번 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>국내주식 양도소득세는 대주주 등 과세대상자만 신고하며, 반기말+2개월 예정신고와 다음 해 5월 확정신고 두 단계입니다.</li>
    <li>홈택스·손택스 전자신고 또는 관할 세무서 서면신고 중 하나를 고르고, 별지 제84호서식에 종목코드를 기재합니다.</li>
    <li>기한을 놓치면 무신고가산세 20%에 납부지연가산세까지 더해지므로, 예정신고 기한부터 달력에 표시해두는 게 안전합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내주식도 양도소득세를 신고해야 하나요</summary>
  <p style="margin:10px 0 0 0;">소액주주라면 신고할 필요가 없습니다. 대주주(코스피 1%·50억원 등)나 비상장·장외거래로 주식을 양도한 경우에만 신고 의무가 생깁니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">예정신고는 언제까지 하나요</summary>
  <p style="margin:10px 0 0 0;">주식을 판 반기의 말일부터 2개월 이내입니다. 상반기(1~6월) 양도분은 8월 31일까지, 하반기(7~12월) 양도분은 다음 해 2월 말일까지 신고합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">확정신고는 예정신고와 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">확정신고는 한 해 동안의 양도소득을 다음 해 5월 1일부터 31일까지 최종 정산하는 절차입니다. 반기마다 예정신고를 이미 했더라도, 세액이 달라지면 확정신고로 다시 맞춥니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신고는 어디서 하나요</summary>
  <p style="margin:10px 0 0 0;">홈택스 웹사이트나 손택스 앱으로 전자신고하거나, 주소지 관할 세무서에 서면으로 신고할 수 있습니다. 서식은 소득세법 시행규칙 별지 제84호서식(양도소득과세표준 신고 및 납부계산서)입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">예정신고를 놓치면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">내야 할 세액의 20%가 무신고가산세로 붙고, 여기에 납부지연가산세가 추가됩니다. 2026년 7월 1일부터 납부지연가산세는 지정납부기한까지는 1일 10만분의22, 그 이후는 월 1만분의67로 계산 방식이 바뀌었습니다. 정확한 금액은 홈택스에서 확인할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식도 같은 방법으로 신고하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 해외주식은 예정신고 의무 없이 다음 해 5월 확정신고만 하면 되고, 서식에는 종목코드 대신 국제증권식별번호(ISIN코드)를 적습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">국세청 홈택스</a>: 양도소득세 전자신고</li>
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a>: 양도소득세 개요·서식 안내</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a>: 소득세법 시행규칙 별지 서식, 국세기본법 가산세 조문</li>
    <li>기준일: 2026-09-14(WebSearch 확인일. 납부지연가산세 계산방식 개정 시행일 2026-07-01)</li>
  </ul>
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
  "headline": "국내주식 양도소득세 신고방법 2026",
  "description": "국내 상장주식 양도소득세는 대주주만 신고 대상이라는 전제부터, 예정신고·확정신고 기한, 홈택스·서면 신고 경로, 신고서식, 무신고 시 가산세 계산 예시까지 실무 절차를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-14",
  "dateModified": "2026-09-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/domestic-stock-capital-gains-filing"
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
      "name": "국내주식도 양도소득세를 신고해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "소액주주라면 신고할 필요가 없습니다. 대주주(코스피 1%·50억원 등)나 비상장·장외거래로 주식을 양도한 경우에만 신고 의무가 생깁니다." }
    },
    {
      "@type": "Question",
      "name": "예정신고는 언제까지 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "주식을 판 반기의 말일부터 2개월 이내입니다. 상반기(1~6월) 양도분은 8월 31일까지, 하반기(7~12월) 양도분은 다음 해 2월 말일까지 신고합니다." }
    },
    {
      "@type": "Question",
      "name": "확정신고는 예정신고와 뭐가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "확정신고는 한 해 동안의 양도소득을 다음 해 5월 1일부터 31일까지 최종 정산하는 절차입니다. 반기마다 예정신고를 이미 했더라도, 세액이 달라지면 확정신고로 다시 맞춥니다." }
    },
    {
      "@type": "Question",
      "name": "신고는 어디서 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "홈택스 웹사이트나 손택스 앱으로 전자신고하거나, 주소지 관할 세무서에 서면으로 신고할 수 있습니다. 서식은 소득세법 시행규칙 별지 제84호서식(양도소득과세표준 신고 및 납부계산서)입니다." }
    },
    {
      "@type": "Question",
      "name": "예정신고를 놓치면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "내야 할 세액의 20%가 무신고가산세로 붙고, 여기에 납부지연가산세가 추가됩니다. 2026년 7월 1일부터 납부지연가산세는 지정납부기한까지는 1일 10만분의22, 그 이후는 월 1만분의67로 계산 방식이 바뀌었습니다. 정확한 금액은 홈택스에서 확인할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "해외주식도 같은 방법으로 신고하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 해외주식은 예정신고 의무 없이 다음 해 5월 확정신고만 하면 되고, 서식에는 종목코드 대신 국제증권식별번호(ISIN코드)를 적습니다." }
    }
  ]
}
</script>
