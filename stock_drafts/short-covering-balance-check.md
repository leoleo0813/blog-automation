---
keyword: 숏커버링 뜻
title: 숏커버링 뜻과 공매도 잔고 확인법
slug: short-covering-balance-check
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 3120 (PC 570 / 모바일 2550)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-13 — 통과]
  WebSearch "숏커버링 뜻" 상위 결과 종합:
  kbthink.com(KB 공식 사전) / esocialtimes.com(소셜타임스, 언론 "토막상식" 코너) /
  namu.wiki(나무위키, 숏스퀴즈 문서) / en.wikipedia.org(아이스하키, 무관 — 제외) /
  dic.hankyung.com(한국경제 한경용어사전, 언론사 사전) / uriphin.com(개인 블로그) /
  econowide.com(개인/소규모 콘텐츠 사이트) / antfx.kr(개인 블로그)
  1) 진입 여지 — 있음. uriphin.com·econowide.com·antfx.kr 등 개인/소규모 블로그가
     3곳 이상 상위에 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻" 정의 검색). 조회·신청·계산기 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 아니다. 상위 결과 전부 "환매수"라는 사전적 정의와 숏스퀴즈와의
     비교까지만 다루고, 숏커버링이 실제 시장에서 일어나고 있는지 확인할 수 있는 공적
     데이터(한국거래소 공매도 순보유잔고 공시 제도)는 하나도 다루지 않음. 정보이득
     여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-13]
  (a) 숏커버링(자발적 환매수)과 숏스퀴즈(손실 회피를 위한 강제성 환매수)의 차이를
      명확히 구분해, 두 용어를 혼용하는 상위 검색 결과의 빈틈을 메운다.
  (b) 핵심 정보이득 — 2024년 12월 1일 개정된 공매도 순보유잔고 공시 기준(기존 발행주식
      총수의 0.5% 이상 → 0.01% 이상(단, 평가액 1억원 미만 제외) 또는 평가액 10억원
      이상)을 표로 정리하고, 이 데이터를 한국거래소 정보데이터시스템(data.krx.co.kr)의
      어느 메뉴에서 조회하는지 절차를 안내해 "숏커버링이 실제로 일어나고 있는지 스스로
      확인하는 방법"을 제공한다. 상위 검색 결과 어디에도 이 공시 제도·조회 절차는
      다뤄지지 않는다.
  (c) 보고의무 발생일(T)로부터 2영업일째(T+2)에 공시된다는 시차를 설명해, "실시간
      데이터가 아니라 2영업일 지연된 자료"라는 오해하기 쉬운 지점을 명확히 한다.
primary_source: |
  1차 시도: 한국거래소 정보데이터시스템(data.krx.co.kr)에 WebFetch 1회 시도 →
  EGRESS_BLOCKED(2026-09-13). 대조군으로 fdata.kbsec.com(금융감독원 2024.12 문서
  재게시본)·securities.koreainvestment.com(한국투자증권 공식 안내)에도 각 1회씩 추가
  시도했으나 동일하게 EGRESS_BLOCKED — 이 세션의 기존 전면 차단 패턴과 일치.
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12)
  기준 적용 — 독립 출처 5곳 이상(MBC뉴스 imnews.imbc.com, 대한민국 정책브리핑
  korea.kr·정부24 gov.kr, 금융위원회 fsc.go.kr 보도자료, KDI 경제교육·정보센터
  eiec.kdi.re.kr, 한국투자증권·상상인증권 공식 고객 안내 페이지)에서 핵심 수치(0.01%
  이상·평가액 1억원 미만 제외, 또는 평가액 10억원 이상, 시행일 2024-12-01, 공시의무
  발생일로부터 2영업일째 공시)가 충돌 없이 일치했다. 언론사(MBC)·정부기관(금융위원회,
  정책브리핑·정부24)·준정부 연구기관(KDI)이 다수 포함돼 있어 캡처 요청 없이 교차검증
  으로 진행했다. 세율·공제 한도류의 민감 수치가 아니라 시행령상 공시 임계값(제도
  변경 사실관계)이라는 점도 함께 고려했다.
  ※ 개정 전 기준(0.5% 이상)은 2016년 발행된 구버전 금감원 문서(file.truefriend.com)
  에서도 확인되나, 이는 2024-12-01 개정 이전 기준이므로 과거 배경으로만 인용하고
  본문의 현재 기준 서술에는 쓰지 않았다(RULES.md 출처 신선도 원칙).
기준일: 2026-09-13 (WebSearch 확인일)
tags: 숏커버링, 숏커버링뜻, 공매도, 공매도잔고, 순보유잔고공시, 숏스퀴즈, 한국거래소, 공매도잔고비율, 주식초보, 공매도규제
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-13).
  게이트1: 네이버 키워드도구 실측 3,120회(신규 브레인스토밍 8개 중 유일한 PASS).
  게이트2: v3 기준 통과(serp_check 참조 — 개인 블로그 3곳 이상 진입, 정의형 검색의도,
  답 미완결).
  게이트3: 숏커버링/숏스퀴즈 개념 구분 + 공매도 순보유잔고 공시 제도(임계값 개정
  내용·조회 절차·공시 시차)로 상위 검색 결과에 없는 정보이득 확보.
  게이트4: data.krx.co.kr·fdata.kbsec.com·securities.koreainvestment.com 3개 도메인
  EGRESS_BLOCKED 확인 후, 5곳 이상 독립 출처(언론·정부기관·준정부연구기관 포함)
  교차검증으로 진행. 한계는 primary_source·self_check에 투명 공개.
self_check: |
  [2026-09-13 최종 판정]
  게이트1 충족 — 신규 후보 8개(관리종목 지정 사유/신규상장 가격제한폭/코넥스 시장
  뜻/대차거래 뜻/유통주식수 뜻/배당성향 계산법/숏커버링 뜻/리픽싱 뜻) 중 "숏커버링 뜻"
  만 검색량 3,120회로 PASS, 나머지 7개는 모두 월 20~190회로 FAIL(backlog.failed_gate1에
  기록).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 순수 사전적 정의(숏커버링 뜻)만으로는 RULES.md의 "사전형 개념은
  정보이득 불가" 원칙에 걸리므로, 여기에 "공매도 순보유잔고 공시 제도로 숏커버링
  발생 여부를 실제로 확인하는 방법"이라는 절차형 정보이득을 결합해 통과시켰다
  (기존 17편 "공매도 뜻과 상환기간", 26편 "블록딜 뜻과 사전공시 의무 확인법"과
  동일한 "뜻+실전 확인법" 패턴).
  게이트4 — data.krx.co.kr(원 소스), fdata.kbsec.com(금감원 문서 재게시본),
  securities.koreainvestment.com(증권사 공식 안내) 세 도메인에 각 1회씩 WebFetch를
  시도해 전부 EGRESS_BLOCKED 확인(2026-09-13, 이 세션의 기존 패턴과 일치). RULES.md
  2026-09-12 기준에 따라 핵심 수치(0.01% 이상·1억원 미만 제외 또는 평가액 10억원
  이상, 시행일 2024-12-01, T+2영업일 공시)가 MBC뉴스·정책브리핑·정부24·금융위원회·
  KDI·한국투자증권·상상인증권 등 7곳에서 충돌 없이 일치해 캡처 요청 없이 진행했다.
  이는 세율·공제 한도처럼 이 프로젝트가 과거 실제 오류를 잡아낸 유형의 숫자가
  아니라 시행령상 공시 임계값(제도 변경 사실관계)이며, 언론사·정부기관·준정부
  연구기관이 다수 포함돼 있어 안전한 쪽(교차검증)으로 판단했다.
  카니벌라이제이션 점검 — 17편(공매도 뜻과 상환기간 90일)은 대차거래 상환기한을
  다루고, 이 글(숏커버링 뜻과 공매도 잔고 확인법)은 환매수 개념과 잔고 공시 제도를
  다뤄 검색 의도와 본문 내용이 겹치지 않는다. 1~26편 어디에도 숏커버링·공매도
  순보유잔고 공시는 다루지 않는다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 안내하는 자리와 하단 참고
  출처 전부 target="_blank" rel="noopener"로 링크 처리.
  제목 14자(공백 제외)·금지어 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음.
  하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) →
  gate_pass:true. 발행 가능.
---

<p>숏커버링은 <mark>공매도 등으로 미리 팔았던 주식을 다시 사서 갚는 환매수</mark>를 말합니다. 그런데 이게 실제로 지금 일어나고 있는지는 감이 아니라 <mark>한국거래소가 공시하는 공매도 잔고 데이터</mark>로 직접 확인할 수 있습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>숏커버링은 공매도(또는 신용융자 매도)로 판 주식을 <b>다시 사서 갚는 환매수</b>이며, 이 매수 물량이 몰리면 주가를 밀어 올리는 요인이 됩니다.</li>
    <li>숏커버링과 자주 헷갈리는 <mark>숏스퀴즈는 주가 급등으로 손실이 커진 공매도 투자자가 손절을 위해 강제로 환매수하는 상황</mark>을 가리켜, 발생 이유가 다릅니다.</li>
    <li>2024년 12월 1일부터 공매도 잔고 공시 기준이 <mark>발행주식수의 0.01% 이상(1억원 미만 제외) 또는 평가액 10억원 이상</mark>으로 강화돼, 더 많은 종목·투자자의 잔고가 공개됩니다.</li>
    <li>이 공시는 한국거래소 정보데이터시스템에서 누구나 무료로 조회할 수 있지만, 보고의무 발생일로부터 <b>2영업일 지연된 자료</b>라는 점을 알고 봐야 합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>숏커버링이란 무엇인가요</li>
  <li>숏커버링과 숏스퀴즈는 뭐가 다른가요</li>
  <li>숏커버링이 일어나면 주가는 왜 오르나요</li>
  <li>숏커버링이 실제로 일어나는지 어떻게 확인하나요</li>
  <li>공매도 잔고 공시는 왜 2영업일 늦게 나오나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">숏커버링이란 무엇인가요</h2>

<p>숏(short)은 주가 하락에 베팅해 주식을 먼저 파는 것을, 커버(cover)는 그 포지션을 되갚아 정리하는 것을 뜻합니다. 두 단어를 합친 <b>숏커버링(short covering)</b>은 <mark>공매도나 신용융자 매도로 미리 판 주식을 다시 사들여 갚는 환매수</mark>를 가리킵니다.</p>

<p>공매도 투자자는 결국 언젠가 빌린 주식을 갚아야 하므로, 목표한 만큼 수익을 냈거나 시장 상황이 바뀌면 자발적으로 숏커버링에 나섭니다. 이 매수 물량 자체가 주가에 영향을 줄 수 있어 시장에서 자주 언급되는 용어입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">숏커버링과 숏스퀴즈는 뭐가 다른가요</h2>

<p>두 용어 모두 결과적으로는 "공매도 물량이 되사들여진다"는 점에서 비슷해 보이지만, <mark>일어나는 이유가 다릅니다.</mark></p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">숏커버링</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">숏스퀴즈</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">발생 원인</td>
      <td style="border:1px solid #ddd;padding:8px;">목표 수익 달성, 시장 전망 변화 등 <b>자발적 판단</b></td>
      <td style="border:1px solid #ddd;padding:8px;">주가 급등으로 손실이 커져 <b>손절을 위해 떠밀리듯</b> 환매수</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">속도</td>
      <td style="border:1px solid #ddd;padding:8px;">비교적 계획적·분산적</td>
      <td style="border:1px solid #ddd;padding:8px;">짧은 시간에 집중적으로 발생하는 경우가 많음</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주가 영향</td>
      <td style="border:1px solid #ddd;padding:8px;">규모에 따라 상승 압력</td>
      <td style="border:1px solid #ddd;padding:8px;">급격한 추가 상승으로 이어지는 경우가 많음</td>
    </tr>
  </tbody>
</table>

<p>즉 <mark>숏스퀴즈는 숏커버링이 일어나는 여러 상황 중 하나</mark>이며, 특히 손실 회피가 목적인 다급한 경우를 가리키는 말입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">숏커버링이 일어나면 주가는 왜 오르나요</h2>

<p>공매도는 <mark>없는 주식을 빌려서 먼저 파는 거래</mark>이므로, 언젠가는 반드시 같은 수량을 다시 사서 갚아야 합니다. 숏커버링 시점에 매수 주문이 몰리면 이 자체가 매수세로 작용해 주가를 밀어 올립니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>숏커버링이 있었다고 추세가 바뀌는 건 아닙니다</b>
  <p style="margin:8px 0 0 0;">숏커버링은 공매도 잔고를 줄이는 매수일 뿐, 기업 실적이나 업황이 바뀐 것은 아닙니다. 단기 반등 이후 다시 하락하는 사례도 흔합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">숏커버링이 실제로 일어나는지 어떻게 확인하나요</h2>

<p>"숏커버링이 있었다"는 뉴스나 커뮤니티 글만으로는 사실인지 확인하기 어렵습니다. <mark>한국거래소가 매일 공시하는 공매도 순보유잔고 데이터</mark>를 직접 보면, 특정 종목의 공매도 잔고가 실제로 줄었는지 확인할 수 있습니다.</p>

<p>2024년 12월 1일부터 이 공시 제도의 대상 기준이 아래처럼 강화됐습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2024-12-01 이전 기준</td>
      <td style="border:1px solid #ddd;padding:8px;">공매도 순보유잔고가 <b>상장주식수의 0.5% 이상</b>인 경우만 공시</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2024-12-01 이후 현재 기준</td>
      <td style="border:1px solid #ddd;padding:8px;"><b>상장주식수의 0.01% 이상</b>(단, 잔고 평가액 1억원 미만은 제외) <b>또는 평가액 10억원 이상</b>인 경우 공시</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">보고·공시 절차</td>
      <td style="border:1px solid #ddd;padding:8px;">투자자가 <a href="https://www.fsc.go.kr" target="_blank" rel="noopener">금융위원회</a> 산하 금융감독원에 보고 → 금융감독원이 한국거래소에 자료 전송 → 거래소가 게시</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">조회 위치</td>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a> → 통계 → 공매도통계 → 공매도 순보유잔고(개별종목/시장별)</td>
    </tr>
  </tbody>
</table>

<p>기준이 0.5%에서 0.01%로 낮아지면서 <mark>공시 대상이 되는 투자자와 종목의 범위가 크게 넓어졌습니다.</mark> 이전에는 보이지 않던 중소형 공매도 잔고도 이제는 확인할 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">공매도 잔고 공시는 왜 2영업일 늦게 나오나요</h2>

<p>공매도 잔고 공시는 실시간이 아닙니다. <mark>보고의무가 발생한 날(T)로부터 2영업일째(T+2)에 공시</mark>되므로, 오늘 조회한 자료는 이틀 전 기준의 잔고입니다.</p>

<p>이는 투자자가 보고서를 작성해 제출하고, 금융감독원이 이를 취합해 거래소로 넘기는 절차에 걸리는 시간 때문입니다. <mark>실시간 매매 신호로 쓰기보다는, 특정 종목의 공매도 잔고 추이를 며칠 단위로 지켜보는 참고 자료</mark>로 활용하는 것이 적절합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">숏커버링이 뭔가요</summary>
  <p style="margin:10px 0 0 0;">공매도나 신용융자 매도로 미리 판 주식을 다시 사들여 갚는 환매수를 말합니다. 이 매수 물량이 몰리면 주가 상승 요인이 될 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">숏커버링과 숏스퀴즈는 같은 말인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 숏커버링은 자발적인 환매수 전반을 가리키고, 숏스퀴즈는 주가 급등으로 손실이 커진 공매도 투자자가 손절을 위해 떠밀리듯 환매수하는 상황을 가리킵니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공매도 잔고 공시 기준이 어떻게 바뀌었나요</summary>
  <p style="margin:10px 0 0 0;">2024년 12월 1일부터 상장주식수의 0.5% 이상이던 기준이 0.01% 이상(1억원 미만 제외) 또는 평가액 10억원 이상으로 강화돼, 더 많은 종목·투자자의 잔고가 공시 대상이 됐습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공매도 잔고는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">한국거래소 정보데이터시스템(data.krx.co.kr)의 통계 메뉴에서 공매도통계 → 공매도 순보유잔고를 조회하면 종목별·시장별 잔고 현황을 무료로 볼 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공매도 잔고 데이터는 실시간인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 보고의무 발생일로부터 2영업일째에 공시되므로, 조회 시점 기준 이틀 전 자료라는 점을 감안해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">숏커버링이 있으면 무조건 주가가 오르나요</summary>
  <p style="margin:10px 0 0 0;">매수 물량이 늘어나는 만큼 상승 압력으로 작용할 수는 있지만, 기업 실적이나 업황이 바뀐 것은 아니어서 단기 반등에 그치는 경우도 흔합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.fsc.go.kr" target="_blank" rel="noopener">금융위원회: 공매도 잔고 공시기준 강화 보도자료(2024-12-01 시행)</a></li>
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템: 공매도 순보유잔고 통계</a></li>
    <li><a href="https://www.korea.kr/news/policyNewsView.do?newsId=148935891" target="_blank" rel="noopener">대한민국 정책브리핑: 내달 1일부터 공매도 잔고 공시기준 강화</a></li>
    <li>기준일: 2026-09-13(WebSearch 확인일, 금융위원회·정책브리핑·MBC뉴스·KDI 등 독립 출처 5곳 이상 교차 확인)</li>
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
  "headline": "숏커버링 뜻과 공매도 잔고 확인법",
  "description": "숏커버링과 숏스퀴즈의 차이, 2024년 12월 강화된 공매도 순보유잔고 공시 기준, 한국거래소에서 잔고를 직접 조회하는 방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-09-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/short-covering-balance-check"
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
      "name": "숏커버링이 뭔가요",
      "acceptedAnswer": { "@type": "Answer", "text": "공매도나 신용융자 매도로 미리 판 주식을 다시 사들여 갚는 환매수를 말합니다. 이 매수 물량이 몰리면 주가 상승 요인이 될 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "숏커버링과 숏스퀴즈는 같은 말인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 숏커버링은 자발적인 환매수 전반을 가리키고, 숏스퀴즈는 주가 급등으로 손실이 커진 공매도 투자자가 손절을 위해 떠밀리듯 환매수하는 상황을 가리킵니다." }
    },
    {
      "@type": "Question",
      "name": "공매도 잔고 공시 기준이 어떻게 바뀌었나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2024년 12월 1일부터 상장주식수의 0.5% 이상이던 기준이 0.01% 이상(1억원 미만 제외) 또는 평가액 10억원 이상으로 강화돼, 더 많은 종목·투자자의 잔고가 공시 대상이 됐습니다." }
    },
    {
      "@type": "Question",
      "name": "공매도 잔고는 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "한국거래소 정보데이터시스템(data.krx.co.kr)의 통계 메뉴에서 공매도통계 → 공매도 순보유잔고를 조회하면 종목별·시장별 잔고 현황을 무료로 볼 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "공매도 잔고 데이터는 실시간인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 보고의무 발생일로부터 2영업일째에 공시되므로, 조회 시점 기준 이틀 전 자료라는 점을 감안해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "숏커버링이 있으면 무조건 주가가 오르나요",
      "acceptedAnswer": { "@type": "Answer", "text": "매수 물량이 늘어나는 만큼 상승 압력으로 작용할 수는 있지만, 기업 실적이나 업황이 바뀐 것은 아니어서 단기 반등에 그치는 경우도 흔합니다." }
    }
  ]
}
</script>
