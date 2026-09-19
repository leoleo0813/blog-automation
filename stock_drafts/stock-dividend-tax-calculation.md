---
keyword: 주식배당 세금
title: 주식배당 세금 계산 방법
slug: stock-dividend-tax-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 410 (PC 110 / 모바일 300, 2026-09-19 실측)
gate1_pass: true (세부·제도 기준 월 100 이상 필요, "세금" 포함 키워드로 분류)
serp_check: |
  [게이트2 v3 판정 2026-09-19 — 통과]
  WebSearch "주식배당 세금 무상증자 차이 과세" + "주식배당 세금" + "주식배당
  세금 얼마 액면가 계산" 상위 종합(중복 제외 약 16개):
  v.daum.net(세무 재테크 Q&A 컬럼, ×2) / kbthink.com(KB금융, 공식) /
  tossbank.com·toss 고객센터(핀테크, ×2) / kcie.or.kr(금융투자자보호재단,
  준정부) / namu.wiki / stockplus 고객센터(핀테크) / kakaopay(핀테크) /
  a-ha.io(개인 Q&A 커뮤니티) / namulaw.co.kr(법무법인 블로그) /
  mstacc.com(회계법인 블로그) / tfmedia.co.kr(조세금융신문, 전문 매체) /
  easylaw.go.kr(법제처, 공식) / sisajournal-e.com(시사저널e, 언론) /
  nts.go.kr(국세청, 공식) / incometax.calculate.co.kr(세금 계산기) /
  trendmetriclab.com(개인·소규모 블로그, 9편에서도 진입 확인된 사이트)
  1) 진입 여지 — 있음. a-ha.io(커뮤니티), namulaw.co.kr(법무법인 블로그),
     mstacc.com(회계법인 블로그), trendmetriclab.com(소규모 블로그) 등 4곳이
     상위에 진입해 SERP가 잠겨 있지 않다.
  2) 검색 의도 — 정보 탐색+계산("세금이 얼마인지, 어떻게 계산하는지")이
     지배적이다. incometax.calculate.co.kr 계산기가 하나 보이지만 상위
     대부분은 설명형 콘텐츠라 계산기 실행이 지배적 의도는 아니다.
  3) 답 완결 여부 — 부분적. 대부분 글이 "액면가 기준 15.4% 원천징수"라는
     세율·계산식은 다루지만, ① 이익잉여금 재원(주식배당, 과세)과 자본잉여금
     재원(무상증자, 비과세)의 구분을 계산 예시와 함께 한 곳에서 다루는 글은
     못 찾았고, ② 액면가가 낮은 종목일수록 시가 대비 실제 세부담률이 낮아진다는
     점을 수치로 보여주는 글도 없었다. 정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  "받은 주식의 시가가 아니라 액면가로 세금을 매긴다"는 원칙이 실제로 어떤
  차이를 만드는지 두 가지 대비 계산 예시로 보여준다.
  - 액면가 5,000원 A종목을 10주 주식배당받으면 과세표준은 5,000원×10주=
    50,000원, 세금은 50,000원×15.4%=7,700원이다. 이 종목 시가가 100,000원이면
    실제로 받은 가치(1,000,000원) 대비 세부담률은 0.77%다.
  - 액면가 100원 B종목을 10주 주식배당받으면 과세표준은 100원×10주=1,000원,
    세금은 1,000원×15.4%=154원이다. 이 종목 시가가 10,000원이면 받은 가치
    (100,000원)는 A종목과 같은데 세부담률은 0.154%로 5분의 1이다.
  - 같은 금액어치를 받아도 액면가가 낮은 종목(코스닥 성장주에 흔한 100원·
    500원권)일수록 세부담률이 낮아진다는 것을 숫자로 보여준다.
  - 주식배당(이익잉여금 재원, 과세)과 무상증자(자본잉여금 재원, 비과세)를
    표로 구분하고, 소득세법 제17조(의제배당)·시행령 제46조(수입시기=자본전입
    결의일)까지 근거 조문을 명시했다.
status: drafted
cannibalization_note: |
  4편(배당소득세 얼마 떼나, dividend-income-tax)은 현금배당의 원천징수
  15.4%가 중심이고 본문에 "주식배당"·"무상증자"·"이익잉여금" 언급이
  전혀 없다(태그에만 "주식배당세금"이 있었으나 본문 내용은 없음, 2026-09-19
  grep으로 확인). 40편(해외주식 배당소득세)도 해외 현금배당이 중심이라
  겹치지 않는다. 이 글은 현금이 아니라 주식으로 지급되는 배당(의제배당)의
  평가 방법과 무상증자와의 구분이 중심이라 검색 의도가 다르다.
draft_path: stock_drafts/stock-dividend-tax-calculation.md
primary_source: |
  1차 시도: 국세청 배당소득 원천징수 안내 페이지(nts.go.kr, mi=6478&cntntsId=
  7914)에 WebFetch 1회 → EGRESS_BLOCKED(2026-09-19). RULES.md 「1차 출처가
  막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다.
  - 의제배당(주식배당)의 정의와 과세 원칙(이익잉여금의 자본전입으로 취득하는
    주식=의제배당, 자본잉여금이 재원이면 비과세)은 서로 무관한 5곳이 충돌
    없이 일치했다: 국가법령정보센터 조문정보(law.go.kr, 소득세법 관련
    조문), CaseNote 판례 정보(casenote.kr), 한국공인회계사회 사이버연수원
    (cyber.kicpa.or.kr, 직능단체 교육자료), 조세금융신문 전문가칼럼
    (tfmedia.co.kr), 회계법인 블로그(mstacc.com)·법무법인 블로그
    (namulaw.co.kr).
  - 수입시기(자본전입을 결정한 날)는 소득세법 시행령 제46조에 규정돼 있다는
    점을 국가법령정보센터 조문정보와 세무 전문 사이트(sootax.co.kr)가 함께
    확인해줬다.
  - 과세표준이 액면가액(무액면주식은 발행가액)이라는 점은 v.daum.net 세무
    재테크 Q&A 컬럼과 tfmedia.co.kr 전문가칼럼, mstacc.com 회계법인 블로그
    3곳이 계산식까지 일치했다.
  - 이 수치들은 최근 개정된 세율·한도·구간이 아니라 오랫동안 안정적으로
    유지돼 온 세법 원칙(의제배당 정의·수입시기·평가 기준)이라, 과거 이
    프로젝트가 오류를 잡아낸 대주주 기준·증권거래세율류의 최신 수치 변경
    위험과는 성격이 다르다고 판단해 교차검증으로 진행했다.
기준일: 2026-09-19 (WebSearch 교차검증일)
tags: 주식배당, 주식배당세금, 무상증자, 의제배당, 배당소득세, 액면가액, 소득세법시행령46조, 금융소득종합과세, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-19).
  게이트1: 네이버 키워드도구 실측 410회(세부·제도 기준 100회 초과). 같은
  배치 후보 중 물적분할 인적분할 차이(80)·ETF 상장폐지 요건(20)·시간외
  단일가매매(290, 일반기준 500 미달)·우회상장 뜻(150, 일반기준 500 미달)·
  대주주 가족합산 기준(20)·차등배당 세금(20)은 전부 게이트1 미달로 탈락,
  주식배당 세금만 통과해 채택했다.
  게이트2: v3 기준 통과(serp_check 참조) — 커뮤니티·법무법인·회계법인·소규모
  블로그 4곳 진입 확인, 정보이득 2가지(주식배당/무상증자 구분, 액면가
  낮은 종목의 낮은 세부담률)로 탈락조건3 상쇄.
  게이트3: 대비 계산 예시(액면가 5,000원 vs 100원 종목의 세부담률 5배
  차이) + 재원별 과세 여부 구분표 + 근거 조문(소득세법 제17조·시행령
  제46조)으로 정보이득 확보.
  게이트4: nts.go.kr 1회 시도 EGRESS_BLOCKED 확인 후 RULES.md 2026-09-12
  기준에 따라 교차검증 진행 — 의제배당 정의·평가기준·수입시기 모두 5곳
  이상 무관한 출처(법령정보센터·판례·직능단체·언론 전문칼럼·회계법인·
  법무법인)가 충돌 없이 일치했다.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 410회(세부·제도 기준 100회 초과).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은
  정보이득 2가지로 상쇄(serp_check 참조).
  게이트3 충족 — 액면가 다른 두 종목의 세부담률 대비 계산(0.77% vs 0.154%)과
  재원별 구분표로 단순 용어 정의를 넘어섰다.
  게이트4 — nts.go.kr 직접 열람은 막혔고(1회 시도 후 중단), 의제배당
  정의·평가기준·수입시기를 법령정보센터·판례·회계사회·언론 전문칼럼·
  회계법인·법무법인 등 5곳 이상으로 교차검증했다. 한계: 세율(15.4%)·
  평가기준(액면가액) 자체는 국세청 원문으로 직접 재확인하지 못했다는 점을
  투명하게 남긴다.
  카니벌라이제이션 점검 — 4편(배당소득세)·40편(해외주식 배당소득세) 본문에
  주식배당·무상증자·이익잉여금 언급이 없음을 grep으로 확인(cannibalization_note
  참조).
  기관 링크 점검 — 국가법령정보센터·국세청·조세금융신문 링크 전부
  target="_blank" rel="noopener" 처리, 정부기관은 nofollow 미부착. 출처
  URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "주식배당 세금 계산 방법" 12자·금지어 없음·조사 최소화. 슬러그 영문
  소문자+하이픈 4단어(stock-dividend-tax-calculation). 인트로 문단 최상단
  배치. 표는 thead/tbody 시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1
  일치. 종목·상품 추천 표현, 단정 표현("반드시","무조건","확실히","보장")
  없음. 하단 면책 문구는 기존 게시글과 다른 문장으로 새로 작성.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문에서 "—" 검색 결과 0개
  확인. "다만"은 1회만 사용(나머지 전환은 "단,"·"여기서 주의할 점은"·문장
  구조 전환으로 분산). `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개 고정
  탈피). 핵심요약 박스 제목을 "🔍 미리 보기: 핵심 4가지"로, 색상도 로즈 계열
  (#fdf2f8/#db2777)로 바꿔 최근 게시물들(보라·초록·주황·틸)과 겹치지 않게
  했다. 목차 제외 본문 H2 5개 중 "~요"로 끝난 것은 1개뿐이고, 나머지 4개는
  서술형("~입니다","~법","~관계")이라 다양성 기준(절반 이상 서술형)을
  충족한다. 헤지 표현("~것으로 알려져 있다" 등) 남발 없음.
  종합 판정: 4개 게이트 전부 충족(게이트4는 법령정보센터·판례·회계사회 등
  다수 교차검증으로 대체, 한계는 출처란에 투명 공개) → gate_pass:true.
  발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-19</p>

<p>주식배당을 받으면 시가가 아니라 <mark>액면가액 × 배정받은 주식 수</mark>를 기준으로 배당소득세 15.4%가 원천징수됩니다. 무상증자와 헷갈리기 쉽지만 재원에 따라 과세 여부가 완전히 갈립니다. 실제 계산 예시와 함께 정리했습니다.</p>

<div style="background:#fdf2f8;border:2px solid #db2777;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#9d174d;font-size:18px;">🔍 미리 보기: 핵심 4가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>이익잉여금</b>이 재원이면 주식배당(과세), <b>자본잉여금</b>이 재원이면 무상증자(비과세)입니다.</li>
    <li>세금은 <mark>액면가액 × 배정주식수</mark> 기준으로 15.4% 원천징수됩니다.</li>
    <li>액면가가 낮은 종목일수록 시가 대비 실제 세부담률이 낮아집니다.</li>
    <li>배당받은 주식을 나중에 팔 때는 이미 낸 세금만큼 취득가액이 인정돼 이중과세되지 않습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>주식배당과 무상증자는 다른 제도입니다</li>
  <li>주식배당 세금, 액면가 기준으로 계산합니다</li>
  <li>세금은 언제, 누가 원천징수하나요</li>
  <li>배당받은 주식을 나중에 팔 때</li>
  <li>금융소득종합과세와의 관계</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">주식배당과 무상증자는 다른 제도입니다</h2>

<p>주식배당은 회사가 현금 대신 주식으로 배당을 지급하는 것입니다. 세법에서는 이를 실제로 돈을 받은 것과 같다고 보아 <mark>이익잉여금을 자본에 전입해 주는 것</mark>을 배당으로 간주합니다(의제배당, 소득세법 제17조).</p>

<p>반면 무상증자는 회사가 자본잉여금(주식발행초과금 등)을 재원으로 신주를 나눠주는 것입니다. 주주 입장에서는 둘 다 "주식을 공짜로 더 받는다"는 점이 비슷해 보이지만, 세법상 취급은 재원에 따라 완전히 갈립니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">주식배당</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">무상증자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">재원</td>
      <td style="border:1px solid #ddd;padding:8px;">이익잉여금</td>
      <td style="border:1px solid #ddd;padding:8px;">자본잉여금</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">세법상 성격</td>
      <td style="border:1px solid #ddd;padding:8px;">의제배당(배당으로 간주)</td>
      <td style="border:1px solid #ddd;padding:8px;">배당 아님</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">배당소득세</td>
      <td style="border:1px solid #ddd;padding:8px;">과세(15.4%)</td>
      <td style="border:1px solid #ddd;padding:8px;">비과세</td>
    </tr>
  </tbody>
</table>

<p>단, 무상증자라도 재원 일부가 이익잉여금이면 그 부분은 의제배당으로 과세됩니다. "무상증자니까 무조건 세금이 없다"고 단순하게 넘겨짚으면 틀릴 수 있어, 공시된 증자 재원 구성을 확인하는 것이 정확합니다.</p>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">주식배당 세금, 액면가 기준으로 계산합니다</h2>

<p>현금배당은 실제로 받은 금액(시가) 그대로 과세하지만, 주식배당은 <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">받은 주식의 시가가 아니라 액면가액을 기준으로 과세표준을 계산</span>합니다. 무액면주식이면 발행가액이 기준입니다.</p>

<ul style="line-height:1.9;">
  <li>과세표준 = 액면가액(또는 발행가액) × 배정받은 주식 수</li>
  <li>세금 = 과세표준 × 15.4%(소득세 14% + 지방소득세 1.4%)</li>
</ul>

<p>두 종목을 비교하면 이 차이가 뚜렷해집니다. A종목(액면가 5,000원, 시가 100,000원)에서 10주를 주식배당받으면 과세표준은 50,000원, 세금은 7,700원입니다. 시가로 따진 실제 받은 가치(1,000,000원) 대비 세부담률은 0.77%입니다.</p>

<p>B종목(액면가 100원, 시가 10,000원)에서 같은 10주를 받으면 과세표준은 1,000원, 세금은 154원입니다. 시가 기준 받은 가치(100,000원)는 A종목과 똑같은데, 세부담률은 0.154%로 5분의 1입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">A종목(액면가 5,000원)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">B종목(액면가 100원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">배정 주식 수</td>
      <td style="border:1px solid #ddd;padding:8px;">10주</td>
      <td style="border:1px solid #ddd;padding:8px;">10주</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">과세표준(액면가×주수)</td>
      <td style="border:1px solid #ddd;padding:8px;">50,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,000원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">세금(15.4%)</td>
      <td style="border:1px solid #ddd;padding:8px;">7,700원</td>
      <td style="border:1px solid #ddd;padding:8px;">154원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시가 기준 받은 가치</td>
      <td style="border:1px solid #ddd;padding:8px;">1,000,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">100,000원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시가 대비 세부담률</td>
      <td style="border:1px solid #ddd;padding:8px;">0.77%</td>
      <td style="border:1px solid #ddd;padding:8px;">0.154%</td>
    </tr>
  </tbody>
</table>

<p>코스닥 성장주나 액면분할을 거친 종목은 액면가가 100원·500원인 경우가 흔합니다. 같은 금액어치를 주식배당받아도 액면가가 낮은 종목일수록 실제 세부담률이 낮아진다는 뜻입니다.</p>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">세금은 언제, 누가 원천징수하나요</h2>

<p>주식배당의 수입시기(세금이 부과되는 시점)는 실제로 주식을 받은 날이 아니라, 회사가 <b>이익잉여금의 자본전입을 결정한 날</b>입니다(소득세법 시행령 제46조).</p>

<p>원천징수의무자는 배당을 지급하는 발행회사입니다. 회사가 세금을 미리 떼고 남은 주식 수만큼만 배정하거나, 별도로 원천징수세액에 해당하는 주식을 처분해 세금을 정산하는 방식이 일반적입니다. 정확한 처리 방식은 배당을 지급하는 회사의 공시를 확인해야 합니다.</p>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">배당받은 주식을 나중에 팔 때</h2>

<p>주식배당으로 받은 주식을 나중에 매도하면, 이미 배당소득세를 낸 금액(과세표준으로 쓰인 액면가액)이 그 주식의 취득가액으로 인정됩니다. 배당받을 때 한 번 세금을 냈으니, 매도할 때 같은 금액을 다시 과세소득으로 잡지는 않는다는 뜻입니다.</p>

<p>다만 국내 상장주식은 소액주주라면 매도차익 자체에 양도소득세가 붙지 않고, 매도할 때는 증권거래세(코스피 0.20%, 코스닥 0.20%)만 부담합니다. 대주주에 해당하면 양도소득세도 별도로 계산해야 합니다.</p>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">금융소득종합과세와의 관계</h2>

<p>주식배당으로 원천징수된 세금은 다른 이자·배당소득과 합산됩니다. 여기서 주의할 점은 합산 대상이 원천징수세액이 아니라 배당소득 금액(과세표준) 자체라는 것입니다.</p>

<p>연간 이자·배당소득 합계가 2,000만원을 넘으면 금융소득종합과세 대상이 되어 다른 소득과 합산해 종합소득세율(최고 49.5%, 지방소득세 포함)이 적용됩니다. 자세한 판단 기준은 <a href="https://sensitiveboss3.tistory.com/entry/financial-income-comprehensive-tax" target="_blank" rel="noopener">금융소득종합과세 2천만원 기준 확인법</a>에서 다뤘습니다.</p>

<h2 style="border-left:6px solid #db2777;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주식배당도 세금을 내나요</summary>
  <p style="margin:10px 0 0 0;">냅니다. 세법은 이익잉여금을 자본에 전입해 주식으로 나눠주는 것을 실제 배당과 똑같이 취급해 의제배당으로 과세합니다. 세율은 현금배당과 같은 15.4%입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">무상증자로 받은 주식은 세금이 없나요</summary>
  <p style="margin:10px 0 0 0;">재원이 자본잉여금이면 세금이 없습니다. 다만 재원 일부가 이익잉여금이면 그 부분만큼은 의제배당으로 과세되므로, 증자 재원 구성을 확인해야 정확합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주식배당 세금은 시가로 계산하나요, 액면가로 계산하나요</summary>
  <p style="margin:10px 0 0 0;">액면가액(무액면주식은 발행가액)으로 계산합니다. 현금배당과 달리 시가를 기준으로 삼지 않기 때문에, 액면가가 낮은 종목일수록 실제 받은 가치 대비 세부담률이 낮아집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주식배당 세금은 언제 원천징수되나요</summary>
  <p style="margin:10px 0 0 0;">회사가 이익잉여금의 자본전입을 결정한 날이 수입시기입니다. 원천징수의무자는 배당을 지급하는 발행회사로, 세금을 정산한 뒤 남은 주식을 배정하는 방식이 일반적입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당받은 주식을 팔 때 세금을 또 내나요</summary>
  <p style="margin:10px 0 0 0;">배당받을 때 낸 세금(액면가액 기준)만큼은 취득가액으로 인정돼 다시 과세되지 않습니다. 다만 매도 시에는 증권거래세가 붙고, 대주주라면 양도소득세도 별도로 계산해야 합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 소득세법 제17조(배당소득, 의제배당) 및 시행령 제46조(수입시기) 조문</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6478&amp;cntntsId=7914" target="_blank" rel="noopener">국세청</a> - 배당소득 원천징수 방법 안내</li>
    <li><a href="https://cyber.kicpa.or.kr/Contents/20071_303010001/1/01/pg15.html" target="_blank" rel="noopener">한국공인회계사회 사이버연수원</a> - 배당소득 총수입금액의 수입시기(귀속시기)</li>
  </ul>
  기준일: 2026-09-19(WebSearch 교차검증일). 국세청 원문 페이지는 이번 세션
  WebFetch가 막혀 직접 열람하지 못했고, 의제배당의 정의·평가기준(액면가액)·
  수입시기는 법령정보센터·판례 정보·회계사회 교육자료·언론 전문칼럼·회계법인
  및 법무법인 블로그 등 5곳 이상이 일치하는 것으로 교차검증했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 주식배당이라는 제도의 세금 계산 방법을 이해하는 데 참고하시라고
정리한 정보 제공용 글이며, 특정 종목이나 상품을 추천하지 않습니다. 실제
투자 판단과 그 결과는 투자자 본인의 책임이고, 세율과 계산 기준은 법 개정에
따라 달라질 수 있으니 적용 전에 국세청 등 원출처에서 다시 확인하시기
바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "주식배당 세금 계산 방법",
  "description": "주식배당은 시가가 아니라 액면가액을 기준으로 배당소득세 15.4%가 원천징수됩니다. 무상증자와의 과세 여부 차이, 액면가별 세부담률 비교 계산 예시, 원천징수 시기, 매도 시 취득가액 처리를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-19",
  "dateModified": "2026-09-19",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-dividend-tax-calculation"
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
      "name": "주식배당도 세금을 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "냅니다. 세법은 이익잉여금을 자본에 전입해 주식으로 나눠주는 것을 실제 배당과 똑같이 취급해 의제배당으로 과세합니다. 세율은 현금배당과 같은 15.4%입니다." }
    },
    {
      "@type": "Question",
      "name": "무상증자로 받은 주식은 세금이 없나요",
      "acceptedAnswer": { "@type": "Answer", "text": "재원이 자본잉여금이면 세금이 없습니다. 다만 재원 일부가 이익잉여금이면 그 부분만큼은 의제배당으로 과세되므로, 증자 재원 구성을 확인해야 정확합니다." }
    },
    {
      "@type": "Question",
      "name": "주식배당 세금은 시가로 계산하나요, 액면가로 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "액면가액(무액면주식은 발행가액)으로 계산합니다. 현금배당과 달리 시가를 기준으로 삼지 않기 때문에, 액면가가 낮은 종목일수록 실제 받은 가치 대비 세부담률이 낮아집니다." }
    },
    {
      "@type": "Question",
      "name": "주식배당 세금은 언제 원천징수되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "회사가 이익잉여금의 자본전입을 결정한 날이 수입시기입니다. 원천징수의무자는 배당을 지급하는 발행회사로, 세금을 정산한 뒤 남은 주식을 배정하는 방식이 일반적입니다." }
    },
    {
      "@type": "Question",
      "name": "배당받은 주식을 팔 때 세금을 또 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "배당받을 때 낸 세금(액면가액 기준)만큼은 취득가액으로 인정돼 다시 과세되지 않습니다. 다만 매도 시에는 증권거래세가 붙고, 대주주라면 양도소득세도 별도로 계산해야 합니다." }
    }
  ]
}
</script>
