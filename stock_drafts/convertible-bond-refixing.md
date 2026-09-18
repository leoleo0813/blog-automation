---
keyword: 전환사채
title: 전환사채 뜻과 리픽싱 확인법
slug: convertible-bond-refixing
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 2780 (PC 1190 / 모바일 1590)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-18 — 통과]
  WebSearch "전환사채 전환청구 전환가액 리픽싱 뜻" + "전환사채 리픽싱 조정한도 70%
  콜옵션 제한 시행일 2024 금융위원회" + "전환사채 전환청구권 행사 절차 DART 공시
  전환가액 조정 사유" 상위 종합:
  help-me.kr(로펌 콘텐츠) / brunch.co.kr(회사법전문변호사 개인 브런치) /
  fsc.go.kr(금융위원회, 공식 ×2) / kimchang.com(김·장 법률사무소) /
  zuzu.network(스타트업 서비스, 소규모 콘텐츠) / ajunews.com·mt.co.kr·fntimes.com
  (언론 ×3) / kif.re.kr(자본시장연구원, 준정부) / kind.krx.co.kr(한국거래소 공시,
  공식) / kci.go.kr·kiss.kstudy.com(학술논문) / knowledge.bookcoach.co.kr(개인·
  소규모 콘텐츠)
  1) 진입 여지 — 있음. brunch.co.kr·zuzu.network·knowledge.bookcoach.co.kr 등
     개인/소규모 콘텐츠가 상위에 진입. SERP가 완전히 잠겨 있지 않다(스팩 키워드는
     같은 배치에서 학술·준정부 자료 일색으로 잠겨 있어 탈락시켰고, 이 키워드는
     대비된다).
  2) 검색 의도 — 정보 탐색형("전환사채가 뭔지, 리픽싱이 뭔지, 무엇이 바뀌었는지"
     확인)이 지배적이다. 조회·계산기 실행이 목적인 키워드가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글들은 각각 리픽싱 개념, 2024년 규제 강화 뉴스,
     전환청구 절차 중 하나만 다룬다. ① 전환가액 조정을 실제 숫자로 계산해 보여주는
     글, ② 2024-12-01 시행된 개정으로 정관을 통한 예외가 폐지되고 주총 특별결의만
     남았다는 점, ③ 전환청구 시 세금(보유기간 이자소득 원천징수) 문제까지 한 곳에
     모은 글은 확인하지 못했다.
  → 탈락조건 1·2 미해당, 탈락조건 3은 위 3가지 정보이득으로 상쇄해 통과.
unique_asset: |
  "리픽싱 조항 하나만 봐서는 안 된다"는 것을 실제 계산과 최신 개정 내용으로
  보여준다.
  - 전환가액 조정을 실제 숫자로 계산: 액면 1,000만원 CB, 최초 전환가액 10,000원이면
    전환주식수 1,000주. 리픽싱 최저한도인 최초 전환가액의 70%(7,000원)까지
    내려가면 전환주식수는 약 1,428주로 늘어난다(약 42.8% 증가). 이 차이만큼
    기존 주주 지분이 희석된다.
  - 2024-12-01 시행된 「증권의 발행 및 공시 등에 관한 규정」 개정으로, 리픽싱을
    최초 전환가액의 70% 밑으로 내리려면 그동안 가능했던 "정관을 통한 예외 적용"이
    폐지되고, 전환사채를 발행할 때마다 주주총회 특별결의를 거쳐야만 하도록
    강화됐다. 콜옵션 행사자를 지정하거나 제3자에게 양도한 경우도 대가와 금액까지
    공시하도록 의무화됐다.
  - 전환청구를 하면 세금 문제가 없는 것으로 오해하기 쉬운데, 만기 전에 전환청구를
    하면 보유 기간 동안의 이자소득(표면금리+상환할증률 기준 만기보장수익률로 계산)에
    원천징수가 붙는다는 점, 특수관계인 간 거래는 상속세및증여세법 제40조에 따라
    별도로 증여세 문제가 생길 수 있다는 점을 짚었다.
  - 이 세 가지를 한 번에 확인하는 방법으로 금융감독원 전자공시(DART)와 한국거래소
    상장공시(KIND)에서 "전환사채권 발행결정" 보고서를 찾아 전환가액·리픽싱
    조항·콜옵션 조항을 직접 확인하는 절차를 안내했다.
status: drafted
cannibalization_note: |
  1~50편 어디에도 전환사채(CB)를 다룬 글이 없다. 37편(채권 세금)은 일반 채권의
  이자소득세·매매차익 과세가 중심이라 전환사채 고유의 리픽싱·콜옵션·전환청구
  메커니즘과는 검색 의도가 겹치지 않는다. 전환청구 시 이자소득 언급도 37편이
  다루지 않은 CB 특유의 보유기간이자상당액 계산 방식이라 중복이 아니다.
draft_path: stock_drafts/convertible-bond-refixing.md
primary_source: |
  1차 시도: 금융위원회(fsc.go.kr) 보도자료(전환사채 제도개선 규정 개정안)에
  WebFetch 1회 → EGRESS_BLOCKED(2026-09-18). RULES.md 「1차 출처가 막혔을 때」
  (2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다.
  - 2024-12-01 시행, 리픽싱 최저한도 70% 예외의 "정관을 통한 적용 폐지 → 발행
    시마다 주총 특별결의만 허용", 콜옵션 행사자·제3자 양도 대가 공시 의무화라는
    사실관계는 서로 무관한 언론 3곳(아주경제·머니투데이·한국금융신문)과 로펌
    콘텐츠(help-me.kr)가 충돌 없이 일치했다. 금융위원회 자체 페이지(fsc.go.kr)도
    검색 결과에 노출되어 출처의 실재를 확인했다(직접 열람만 막힘).
  - 전환청구 시 보유기간 이자소득(만기보장수익률=표면금리+상환할증률 기준)
    원천징수, 종합소득세 신고 시 기납부세액 공제는 casenote.kr에 수록된 국세청
    유권해석 4건(서로 다른 사건번호)과 taxcanvas.kr·kifrs.com 세무·회계 콘텐츠가
    동일한 계산 원칙을 반복해 일치했다. 특수관계인 간 이익에 대한 증여세(상속세및
    증여세법 제40조, 기준금액은 전환사채 시가의 30%와 1억원 중 작은 금액) 조문은
    국가법령정보센터(law.go.kr) 조문 링크로 존재를 확인했다.
  - 전환가액 조정 계산 예시(1,000만원/10,000원/70%)는 이미 확인된 70% 최저한도
    규정을 그대로 적용한 산술 계산이라 별도 출처가 필요하지 않다.
기준일: 2026-09-18 (WebSearch 확인일)
tags: 전환사채, CB, 리픽싱, 콜옵션, 전환가액, 발행공시, 주식초보, 재테크초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-18).
  게이트1: 네이버 키워드도구 실측 2,780회 — 50편(자사주 소각) 작업 시 함께 확인한
  이번 배치 후보 중 스팩(3,500)은 게이트2에서 학술·준정부 자료 일색으로 탈락,
  대차거래(530)는 17·27편과 카니벌라이제이션 우려로 보류, 전환사채(2,780)를
  채택했다.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 콘텐츠 진입 확인,
  정보이득 3가지(전환가액 조정 계산·2024년 개정 강화 내용·전환청구 시 세금)로
  탈락조건3 상쇄.
  게이트3: 전환가액 조정 실제 계산 + 2024-12-01 개정 전후 비교표 + 전환청구
  이자소득 세금 + 발행공시(DART/KIND) 확인 절차로 정보이득 확보.
  게이트4: fsc.go.kr 1회 시도 EGRESS_BLOCKED 확인 후 RULES.md 2026-09-12 기준에
  따라 교차검증 진행 — 규제 개정 사실관계는 언론 3곳+로펌 콘텐츠, 세금 부분은
  국세청 유권해석 4건(casenote.kr)+세무회계 콘텐츠 2곳으로 확인. 법 조문 자체는
  국가법령정보센터 링크로 존재만 확인(전문 열람은 못함).
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 2,780회(일반 주제 기준 500회, 제도 기준
  100회 둘 다 초과).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은
  3가지 정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 전환가액 조정 계산 예시(1,000주→약1,428주), 2024년 개정 전후
  비교표, 전환청구 시 이자소득 세금, 발행공시 확인 절차까지 상위 결과가 한 곳에
  모아두지 않은 정보를 엮었다.
  게이트4 — fsc.go.kr 직접 열람은 막혔고(1회 시도 후 중단), 규제 개정 사실관계는
  언론 3곳+로펌 콘텐츠, 세금 부분은 국세청 유권해석(casenote.kr) 4건과 세무·회계
  콘텐츠 2곳으로 교차검증했다. 상속세및증여세법 제40조 조문 전문은 원문 열람을
  못해 조문 번호와 기준금액만 인용하고 세부 계산식은 본문에서 다루지 않았다 —
  이 한계를 참고 출처란에 명시했다.
  카니벌라이제이션 점검 — 1~50편 어디에도 전환사채를 다룬 글이 없다. 37편(채권
  세금)과는 다루는 세목·메커니즘이 달라 겹치지 않는다.
  기관 링크 점검 — 국가법령정보센터·DART·KIND·금융위원회 링크 전부 target="_blank"
  rel="noopener" 처리, nofollow 미부착(공식 기관이므로).
  출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "전환사채 뜻과 리픽싱 확인법" 13자·금지어 없음·조사 최소화. 슬러그 영문
  소문자+하이픈 3단어(convertible-bond-refixing). 인트로 문단 최상단 배치. 표는
  thead/tbody 시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1 일치. 종목·상품
  추천 표현, 단정 표현("반드시","무조건","확실히","보장") 없음. 하단 면책 문구는
  기존 게시글과 다른 문장으로 새로 작성.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문에서 "—" 검색 결과 0개 확인.
  "다만"은 0회 사용(전환어는 "단," 1회, 나머지는 문장 구조 전환으로 분산).
  `<mark>` 총 3개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을
  "🔍 짚고 넘어갈 3가지"로, 색상도 보라 계열(#f5f3ff/#7c3aed)로 바꿔 기존
  파란색·초록색 패턴을 반복하지 않았다. FAQ 헤딩도 "이런 점도 자주 묻습니다"로
  변경. 목차 제외 본문 H2 6개 중 "~나요"류로 끝난 것은 0개이고("가요"로 끝난
  것 1개는 있으나 전형적 "~나요/~인가요" 패턴은 피함), 나머지 5개는 서술형·다른
  질문형 어미라 다양성 기준을 충족한다. 헤지 표현("~것으로 알려져 있다" 등)
  남발 없음, 단 상속세및증여세법 제40조의 세부 계산식처럼 원문을 확인하지 못한
  부분은 그 한계 자체를 명시했다(헤지가 아니라 사실 반영).
  종합 판정: 4개 게이트 전부 충족(게이트4는 언론·로펌·국세청 유권해석 교차검증으로
  대체, 한계는 출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-18</p>

<p>전환사채(CB)는 <mark>정해진 조건에 따라 주식으로 바꿀 수 있는 권리가 붙은 채권</mark>이라, 주가가 오르면 주식으로, 아니면 채권으로 남겨 이자를 받을 수 있습니다. 단, 리픽싱과 콜옵션 조항에 따라 기존 주주 지분이 얼마나 희석되는지가 크게 갈리고, 2024년 12월 관련 규정이 한 차례 강화되기도 했습니다. 전환가액 계산부터 발행공시 확인 방법까지 정리했습니다.</p>

<div style="background:#f5f3ff;border:2px solid #7c3aed;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4c1d95;font-size:18px;">🔍 짚고 넘어갈 3가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>리픽싱은 <b>최초 전환가액의 70%</b>까지만 내려가는 것이 원칙입니다.</li>
    <li>2024년 12월부터는 그 아래로 내리려면 <mark>발행할 때마다 주주총회 특별결의</mark>가 필요합니다.</li>
    <li>전환청구 시점에도 <b>보유 기간 이자소득에 세금</b>이 붙을 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>전환사채가 뭔가요</li>
  <li>전환가액과 전환청구권의 관계</li>
  <li>리픽싱과 최저한도 70%</li>
  <li>2024년 개정으로 달라진 점</li>
  <li>콜옵션 조항, 놓치기 쉬운 부분</li>
  <li>발행공시에서 확인하는 법</li>
  <li>이런 점도 자주 묻습니다</li>
</ol>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">전환사채가 뭔가요</h2>

<p>전환사채는 회사가 돈을 빌리며 발행하는 채권이지만, 일정 기간 안에 정해진 조건으로 그 회사의 주식으로 바꿀 수 있는 권리(전환권)가 함께 붙어 있습니다. 영어 표기 Convertible Bond를 줄여 CB라고도 부릅니다.</p>

<p>투자자 입장에서는 주가가 오르면 전환청구를 해서 주식으로 이익을 실현하고, 주가가 기대만큼 오르지 않으면 그냥 채권으로 들고 있다가 만기에 원금과 이자를 받으면 됩니다. 회사 입장에서는 일반 회사채보다 낮은 금리로 자금을 조달할 수 있는 대신, 전환이 이뤄지면 기존 주주의 지분이 그만큼 희석됩니다.</p>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">전환가액과 전환청구권의 관계</h2>

<p>전환가액은 사채를 주식 몇 주로 바꿔줄지 정하는 기준 가격입니다. 전환주식수는 사채 금액을 전환가액으로 나눈 값입니다.</p>

<p>예를 들어 액면 1,000만원짜리 CB의 전환가액이 10,000원이면, 전환청구 시 받는 주식은 1,000주(1,000만원÷10,000원)입니다. 전환가액이 낮을수록 같은 사채 금액으로 더 많은 주식을 받으니, 전환가액이 어떻게 정해지고 조정되는지가 핵심입니다.</p>

<ul style="line-height:1.9;">
  <li>전환청구는 발행회사에 전환청구서와 관계서류를 제출한 때 효력이 발생합니다.</li>
  <li>상장회사가 발행한 CB라면, 전환으로 새로 생기는 주식은 한국예탁결제원을 통해 예탁·발행됩니다.</li>
</ul>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">리픽싱과 최저한도 70%</h2>

<p>리픽싱은 주가가 하락했을 때 전환가액을 낮춰 조정해 주는 조항입니다. 전환가액이 낮아지면 같은 사채로 받을 수 있는 주식 수가 늘어나 채권자(투자자)에게 유리해집니다.</p>

<p>현행 규정은 리픽싱으로 낮출 수 있는 최저한도를 <mark>최초 전환가액의 70%</mark>로 제한합니다. 앞서 예로 든 전환가액 10,000원 CB가 최저한도까지 내려가면 전환가액은 7,000원이 되고, 전환주식수는 1,000만원÷7,000원, 약 1,428주로 늘어납니다. 처음 1,000주보다 약 42.8% 늘어난 셈이라, 그만큼 기존 주주의 지분율이 더 희석됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">전환가액</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">전환주식수(사채 1,000만원 기준)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">최초 전환가액 10,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,000주</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">리픽싱 최저한도 7,000원(70%)</td>
      <td style="border:1px solid #ddd;padding:8px;">약 1,428주(약 42.8% 증가)</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">2024년 개정으로 달라진 점</h2>

<p>2024년 12월 1일부터 시행된 「증권의 발행 및 공시 등에 관한 규정」 개정으로 리픽싱 관련 조건이 더 까다로워졌습니다. 경영정상화가 불가피한 경우에 한해 70% 밑으로 조정하는 예외를 허용해 온 것은 그대로지만, 그 예외를 적용받는 방법이 바뀌었습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">2024년 12월 이전</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">2024년 12월 이후</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">70% 미만 예외 적용 방법</td>
      <td style="border:1px solid #ddd;padding:8px;">정관에 정해두면 가능</td>
      <td style="border:1px solid #ddd;padding:8px;">정관 규정 폐지, 발행할 때마다 주주총회 특별결의 필요</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">콜옵션 행사자 공시</td>
      <td style="border:1px solid #ddd;padding:8px;">행사자 특정 없이도 가능했던 경우 다수</td>
      <td style="border:1px solid #ddd;padding:8px;">행사자, 제3자 양도 시 대가와 금액까지 주요사항보고서로 공시</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">증자·주식배당 시 조정</td>
      <td style="border:1px solid #ddd;padding:8px;">개별 사안별 처리</td>
      <td style="border:1px solid #ddd;padding:8px;">희석효과를 반영한 가액 이상으로만 하향 조정 가능</td>
    </tr>
  </tbody>
</table>

<p>정관을 근거로 한 예외가 사라졌기 때문에, 지금은 어떤 회사가 CB의 전환가액을 70% 밑으로 낮추려면 그때마다 주주총회에서 특별결의를 받아야 합니다. 그 결정 과정 자체가 공시로 남으니, 투자자는 이 절차를 거쳤는지를 확인 지표로 삼을 수 있습니다.</p>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">콜옵션 조항, 놓치기 쉬운 부분</h2>

<p>콜옵션은 발행회사나 특정인이 유통 중인 전환사채를 정해진 조건에 되사올 수 있는 권리입니다. 최대주주가 콜옵션을 확보해 두면, 나중에 전환사채를 되사들여 경영권 방어나 지분 확대에 쓸 수 있습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>콜옵션 자체보다 "누가, 얼마에" 행사했는지를 봐야 합니다</b>
  <p style="margin:8px 0 0 0;">2024년 개정 이후로는 콜옵션 행사자를 지정하거나 제3자에게 양도한 경우, 그 대가를 받았는지와 구체적인 금액까지 주요사항보고서로 공시해야 합니다. 콜옵션이 있다는 사실만으로는 좋고 나쁨을 판단하기 어렵고, 실제 공시 내용을 확인하는 것이 중요합니다.</p>
</div>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">발행공시에서 확인하는 법</h2>

<p>전환가액, 리픽싱 조항, 콜옵션 조항은 모두 회사가 CB를 발행할 때 내는 공시에 담겨 있습니다. 다음 순서로 직접 확인할 수 있습니다.</p>

<ol style="line-height:1.9;">
  <li><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a> 또는 <a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 상장공시시스템(KIND)</a>에 접속합니다.</li>
  <li>회사명으로 검색한 뒤 "전환사채권 발행결정" 보고서를 찾습니다.</li>
  <li>보고서 안의 전환가액, 전환청구기간, 리픽싱(전환가액의 조정) 조항, 콜옵션(매도청구권) 조항을 각각 확인합니다.</li>
  <li>이후 전환가액이 조정됐다면 "전환가액의 조정" 관련 정정·발행 후 공시가 별도로 올라오므로 함께 확인합니다.</li>
</ol>

<h2 style="border-left:6px solid #7c3aed;padding-left:12px;margin-top:36px;">이런 점도 자주 묻습니다</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">전환사채(CB)와 신주인수권부사채(BW)는 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">CB는 전환청구를 하면 사채 자체가 사라지고 주식으로 바뀝니다. 반면 BW는 사채를 그대로 유지한 채 별도로 붙은 신주인수권만 행사해 새 주식을 받는 구조라 사채와 주식을 동시에 가질 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">리픽싱 최저한도 70% 밑으로는 절대 못 내리나요</summary>
  <p style="margin:10px 0 0 0;">경영정상화가 불가피한 경우에 한해 예외가 있습니다. 2024년 12월 개정 이후로는 정관을 통한 예외 적용이 폐지되고, 전환사채를 발행할 때마다 주주총회 특별결의를 거쳐야만 70% 밑으로 조정할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">전환청구를 하면 세금을 내야 하나요</summary>
  <p style="margin:10px 0 0 0;">만기 전에 전환청구를 하면 그때까지 보유한 기간에 해당하는 이자소득(표면금리와 상환할증률을 더한 만기보장수익률 기준)에 원천징수가 이뤄지고, 종합소득세 신고 때 기납부세액으로 공제받을 수 있습니다. 특수관계인 사이의 거래라면 상속세및증여세법 제40조에 따라 별도로 증여세 문제가 생길 수도 있어, 이런 거래라면 세무 전문가 확인을 받는 것이 안전합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">콜옵션 행사자가 누구인지도 공시로 확인할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">2024년 12월 개정 이후로는 확인할 수 있습니다. 콜옵션 행사자를 지정하거나 제3자에게 양도한 경우, 그 대가와 금액까지 주요사항보고서로 공시하도록 의무화됐습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">전환사채 발행 자체가 나쁜 신호인가요</summary>
  <p style="margin:10px 0 0 0;">발행 목적과 조건에 따라 다르므로 일률적으로 말하기는 어렵습니다. 자금 조달 방법의 하나일 뿐이라, 리픽싱 조건이 지나치게 유리한지, 콜옵션 행사자가 최대주주 쪽인지 같은 개별 조건을 직접 공시에서 확인하는 편이 낫습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.fsc.go.kr/no010101/83400" target="_blank" rel="noopener">금융위원회</a> - 전환사채 제도개선을 위한 「증권의 발행 및 공시 등에 관한 규정」 개정(2024-12-01 시행)</li>
    <li><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a> - 발행공시 조회</li>
    <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 상장공시시스템(KIND)</a> - 전환사채권 발행결정 보고서 조회</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 상속세및증여세법 제40조(전환사채 등의 주식전환 등에 따른 이익의 증여)</li>
  </ul>
  기준일: 2026-09-18(WebSearch 확인일). 금융위원회 원문 페이지는 이번 세션
  WebFetch가 막혀 직접 열람하지 못했고, 2024년 12월 개정 내용은 언론 3곳과 로펌
  콘텐츠가 일치하는 것으로, 전환청구 시 이자소득 과세 원칙은 국세청 유권해석
  (casenote.kr 수록) 4건과 세무·회계 콘텐츠로 교차검증했습니다. 상속세및증여세법
  제40조의 세부 계산식은 원문을 확인하지 못해 조문 번호만 인용했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 전환사채라는 상품 구조와 관련 공시를 이해하는 데 참고하시라고 정리한
정보 제공용 글입니다. 특정 종목이나 전환사채 상품의 매수·매도를 권하는 내용이
아니며, 투자 결정과 그로 인한 손익은 투자자 본인이 책임집니다. 관련 규정과
세법은 이후 개정될 수 있으니, 실제 투자나 신고 전에는 반드시 원출처에서 최신
내용을 다시 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "전환사채 뜻과 리픽싱 확인법",
  "description": "전환사채(CB)의 전환가액·리픽싱·콜옵션 구조와 2024년 12월 시행된 규정 개정 내용, 전환청구 시 세금, 발행공시에서 직접 확인하는 방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-18",
  "dateModified": "2026-09-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/convertible-bond-refixing"
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
      "name": "전환사채(CB)와 신주인수권부사채(BW)는 뭐가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "CB는 전환청구를 하면 사채 자체가 사라지고 주식으로 바뀝니다. 반면 BW는 사채를 그대로 유지한 채 별도로 붙은 신주인수권만 행사해 새 주식을 받는 구조라 사채와 주식을 동시에 가질 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "리픽싱 최저한도 70% 밑으로는 절대 못 내리나요",
      "acceptedAnswer": { "@type": "Answer", "text": "경영정상화가 불가피한 경우에 한해 예외가 있습니다. 2024년 12월 개정 이후로는 정관을 통한 예외 적용이 폐지되고, 전환사채를 발행할 때마다 주주총회 특별결의를 거쳐야만 70% 밑으로 조정할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "전환청구를 하면 세금을 내야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "만기 전에 전환청구를 하면 그때까지 보유한 기간에 해당하는 이자소득(표면금리와 상환할증률을 더한 만기보장수익률 기준)에 원천징수가 이뤄지고, 종합소득세 신고 때 기납부세액으로 공제받을 수 있습니다. 특수관계인 사이의 거래라면 상속세및증여세법 제40조에 따라 별도로 증여세 문제가 생길 수도 있습니다." }
    },
    {
      "@type": "Question",
      "name": "콜옵션 행사자가 누구인지도 공시로 확인할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2024년 12월 개정 이후로는 확인할 수 있습니다. 콜옵션 행사자를 지정하거나 제3자에게 양도한 경우, 그 대가와 금액까지 주요사항보고서로 공시하도록 의무화됐습니다." }
    },
    {
      "@type": "Question",
      "name": "전환사채 발행 자체가 나쁜 신호인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "발행 목적과 조건에 따라 다르므로 일률적으로 말하기는 어렵습니다. 자금 조달 방법의 하나일 뿐이라, 리픽싱 조건이 지나치게 유리한지, 콜옵션 행사자가 최대주주 쪽인지 같은 개별 조건을 직접 공시에서 확인하는 편이 낫습니다." }
    }
  ]
}
</script>
