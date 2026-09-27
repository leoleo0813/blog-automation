---
keyword: EPS 뜻
title: EPS 뜻과 계산 방법
slug: eps-meaning-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1460 (PC 360 / 모바일 1100)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-27 — 통과]
  WebSearch "EPS 뜻 주당순이익 계산법" 상위 9개: tikr.com(글로벌 핀테크 콘텐츠 한국어판)/
  khan.co.kr(경향신문, 언론)/namu.wiki(백과)/cookiedeal.io(개인·소규모 콘텐츠)/
  support.stockplus.com(핀테크)/mna.bridgecode.kr(M&A 자문 콘텐츠)/jurinmap.com
  (개인·교육 콘텐츠)/trendmetriclab.com(개인·소규모 콘텐츠)/econowide.com(개인블로그).
  1) 진입 여지 — 있음. cookiedeal.io·jurinmap.com·trendmetriclab.com·econowide.com
     등 개인·소규모 콘텐츠가 상위 9개 중 4개를 차지한다.
  2) 검색 의도 — "뜻"과 "계산법"을 묻는 개념 탐색형이다. 계산기·조회 도구 실행이
     지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 EPS 정의와 "순이익÷발행주식수"
     공식, 기본/희석 구분 명칭까지는 언급하지만, 희석EPS를 실제 숫자로 계산해
     보여주는 글이나 EPS 성장률을 PER과 연결해 해석하는 글, 주식수 변동(자사주
     소각·무상증자)이 EPS를 왜곡시키는 방식을 다룬 글은 확인되지 않았다.
  → 탈락조건 1~3 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 기본EPS와 희석EPS를 가상 수치로 각각 실제 계산해 차이를 숫자로 보여준다
      (당기순이익 100억 원, 유통주식수 1,000만 주 → 기본EPS 1,000원, 전환사채
      잠재주식 200만 주 반영 시 희석EPS 약 833원).
  (b) EPS 성장률 계산 예시(전년 800원 → 올해 1,000원 = 25% 성장)와 이를 PER과
      함께 봐야 하는 이유 — 88편(PBR)·89편(ROE)에서 다룬 PER=주가/EPS 관계식과
      연결해, EPS 단독편에서만 다루는 "성장률" 관점으로 차별화한다.
  (c) 자사주 소각(50편)·무상증자(29편 감자와 반대 방향) 등 주식수 변동이 순이익
      변화 없이도 EPS를 바꿀 수 있다는 왜곡 요인 체크리스트 — 상위 검색결과에는
      이 연결 지점을 다룬 글이 없었다.
  (d) DART 전자공시시스템에서 실제 기업의 기본/희석 EPS를 확인하는 절차 안내.
primary_source: |
  기본EPS와 희석EPS를 나누어 공시하도록 규정하는 회계기준은 K-IFRS 제1033호
  '주당이익(Earnings Per Share)'이다. 자동화 세션에서 한국회계기준원
  www.kasb.or.kr에 WebFetch를 1회 시도했으나 EGRESS_BLOCKED로 막혔다.
  RULES.md 「1차 출처가 막혔을 때」 기준에 따라 WebSearch로 독립 출처
  교차검증을 진행했다. EPS 계산 공식(순이익÷발행주식수)과 기본/희석 구분이
  존재한다는 사실은 삼일회계법인의 회계기준서비스(samili.com, 4대 회계법인
  계열의 실무 소스, URL 자체가 "1978-1033"으로 K-IFRS 1033을 독립적으로
  가리킨다)·경향신문(khan.co.kr, 언론)·브릿지코드 M&A센터(mna.bridgecode.kr,
  전문 자문 콘텐츠) 3곳 이상에서 핵심 사실(계산 공식, 기본/희석 구분, 관련
  회계기준 번호)이 충돌 없이 일치했다. 이는 세율·공제한도처럼 매년 바뀌는
  수치가 아니라 오래 전 확정된 회계 항등식·기준 체계이므로 다수 독립 출처
  교차검증으로 진행해도 안전하다고 판단했다. 계산 예시에 쓰인 숫자는 전부
  가상의 수치이며 실제 기업 재무제표에서 가져온 것이 아니다.
기준일: 2026년 9월 기준 (K-IFRS 제1033호는 2015년 9월 25일 개정판이 현재도 적용 중)
tags: EPS, EPS뜻, 주당순이익, EPS계산법, 기본EPS, 희석EPS, PER, EPS성장률, DART, 주식투자지표
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 1,460회(일반 주제 기준 500회 이상).
  게이트2 충족 — v3 기준 3개 탈락조건 모두 미해당(개인·소규모 콘텐츠 4곳
  진입, 개념 탐색형 의도, 희석EPS 계산·성장률·주식수 왜곡 요인이라는 정보이득
  미확보 확인). 게이트3 충족 — 기본/희석 EPS 계산 예시 + 성장률 계산 + 주식수
  변동 왜곡 체크리스트라는 정보이득. 게이트4 충족 — 계산식 자체는 항등식이라
  기관 확인 불요, 근거 회계기준(K-IFRS 1033) 부분은 원문 WebFetch 1회 시도 후
  차단을 확인하고 3곳 이상 독립 출처(회계법인·언론·전문콘텐츠)가 충돌 없이
  일치하는 사실만 교차검증으로 확보했다.
capture_guide: ""
self_check: |
  [2026-09-27 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — stock_drafts/ 전체를 grep한 결과 EPS를 본문 주제로
  전용 편에서 다룬 기존 글은 없었다. 88편(PBR)은 "PER은 주가를 EPS로 나눈 값"
  이라는 관계식 설명에서 EPS를 한 문장으로만 언급하고, 89편(ROE)도 마찬가지로
  지나가는 언급뿐이라 본 편의 기본/희석 EPS 계산·성장률·주식수 왜곡 요인과는
  검색 의도가 겹치지 않는다.
  YMYL 안전장치 점검 — 특정 종목의 매수·매도 시점이나 목표가를 언급하지 않았다.
  계산 예시는 전부 가상의 수치로만 구성했다.
  기관 링크 점검 — DART 전자공시시스템 링크 1개, 한국거래소 정보데이터시스템
  링크 1개를 참고 출처 목록과 본문 안내 문장에 걸었다.
  제목 "EPS 뜻과 계산 방법" 12자·금지어 없음·조사 최소화.
  슬러그 영문 소문자+하이픈 3단어(eps-meaning-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—" 검색
  결과 0개 확인. "다만"은 한 번도 쓰지 않고 "단,"·"그런데"·"반대로"로 전환어를
  분산했다. `mark` 태그 총 3개(3~5개 기준 충족). FAQ 4개(직전 88편 5개·89편
  6개와 다르게 변화). 핵심 요약 박스 제목을 "🧮 EPS, 숫자로 먼저 보면"으로, 색은
  골든로드(#fef9e7/#b8860b)로 최근 게시물(포레스트그린#2e7d32·테라코타
  #c0562f·슬레이트#455a64 등)과 겹치지 않게 골랐다. 목차 제외 본문 H2 5개 중
  서술형 3개, 질문형 2개("기본EPS와 희석EPS는 왜 다른가요", "EPS는 어디서
  확인하나요")로 "~나요" 편중 없음(5개 중 2개, 40%). FAQ 헤딩도 "자주 묻는
  질문" 대신 "더 짚어두면 좋은 것들"로 변형. 헤지 표현("~것으로 알려져 있다"
  등)은 쓰지 않고 확정된 사실은 단정형으로 서술했다. 면책 문구는 88·89편과
  다른 표현으로 새로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-27</p>

<p>EPS는 회사가 주식 한 주당 얼마의 이익을 냈는지 보여주는 지표입니다. 계산식은 단순한 나눗셈이지만, 기본EPS와 희석EPS를 구분하지 않거나 주식수 변동을 놓치면 숫자를 잘못 읽기 쉽습니다. 이 글은 EPS 계산 공식과 기본·희석 구분, 성장률로 해석하는 방법을 정리합니다.</p>

<div style="background:#fef9e7;border:2px solid #b8860b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5c00;font-size:18px;">🧮 EPS, 숫자로 먼저 보면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>EPS는 당기순이익 ÷ 유통주식수로 계산하며, 주식 한 주가 벌어들인 이익을 뜻합니다.</li>
    <li>기본EPS와 희석EPS는 계산에 쓰는 주식수가 다르며, 희석EPS가 보통 더 낮게 나옵니다.</li>
    <li>전년 대비 EPS 성장률을 보면 이익 증가 속도를 가늠할 수 있습니다.</li>
    <li>자사주 소각이나 무상증자처럼 순이익과 무관한 사건도 EPS 숫자를 바꿀 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>EPS 뜻과 계산 공식</li>
  <li>기본EPS와 희석EPS는 왜 다른가요</li>
  <li>EPS 성장률 확인하는 법</li>
  <li>EPS만으로 판단하면 위험한 이유</li>
  <li>EPS는 어디서 확인하나요</li>
  <li>더 짚어두면 좋은 것들</li>
</ol>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">EPS 뜻과 계산 공식</h2>

<p>EPS(Earnings Per Share, 주당순이익)는 <mark>회사의 당기순이익을 유통주식수로 나눈 값</mark>입니다. 계산식은 EPS = 당기순이익 ÷ 유통주식수입니다.</p>

<p>가상의 F기업이 당기순이익 100억 원을 냈고 유통주식수가 1,000만 주라면, EPS는 100억 ÷ 1,000만 = 1,000원이 됩니다. 이 회사는 주식 한 주당 1,000원의 이익을 냈다는 뜻입니다.</p>

<ul style="line-height:1.9;">
  <li>유통주식수는 회계기간 동안의 가중평균 주식수를 씁니다.</li>
  <li>EPS 1,000원 자체보다 전년 대비 얼마나 늘거나 줄었는지가 더 중요한 정보입니다.</li>
  <li>주가를 EPS로 나누면 PER이 되어, 88편(PBR)·89편(ROE)에서 다룬 PER=주가/EPS 관계식으로 이어집니다.</li>
</ul>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">기본EPS와 희석EPS는 왜 다른가요</h2>

<p>전환사채나 스톡옵션처럼 나중에 주식으로 바뀔 수 있는 권리가 있으면, 그 권리가 전부 행사됐다고 가정한 EPS를 별도로 계산합니다. 이것이 희석EPS입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <p style="margin:8px 0 0 0;">앞선 F기업이 전환사채 보유자가 전환하면 200만 주가 새로 생기는 조건이라고 가정합니다.</p>
  <p style="margin:8px 0 0 0;">기본EPS = 100억 ÷ 1,000만 주 = 1,000원</p>
  <p style="margin:8px 0 0 0;">희석주식수 = 1,000만 주 + 200만 주 = 1,200만 주</p>
  <p style="margin:8px 0 0 0;">희석EPS = 100억 ÷ 1,200만 주 = 약 <mark>833원</mark>으로, 기본EPS보다 낮게 나옵니다.</p>
</div>

<p>순이익은 그대로인데 나눠 갖는 주식수만 늘어나므로, 희석EPS는 기본EPS와 같거나 낮게 나오는 구조입니다. 그런데 사업보고서 재무제표 주석에는 두 수치가 함께 표시되므로, 기본EPS만 보고 판단하면 잠재적 희석 효과를 놓칠 수 있습니다.</p>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">EPS 성장률 확인하는 법</h2>

<p>EPS 성장률은 <mark>(올해 EPS − 작년 EPS) ÷ 작년 EPS × 100</mark>으로 계산합니다. 작년 EPS가 800원이고 올해 EPS가 1,000원이라면, 성장률은 (1,000−800)÷800×100 = 25%입니다.</p>

<ul style="line-height:1.9;">
  <li>같은 EPS 1,000원이라도 전년보다 늘었는지 줄었는지에 따라 의미가 달라집니다.</li>
  <li>여러 해의 EPS를 나열해 성장률 추세가 꾸준한지 확인하는 편이 한 해 수치만 보는 것보다 정확합니다.</li>
  <li>EPS 성장률과 PER을 함께 보면, 이익이 빠르게 늘어나는 회사인지 그렇지 않은지 가늠하는 데 도움이 됩니다.</li>
</ul>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">EPS만으로 판단하면 위험한 이유</h2>

<p>EPS는 순이익뿐 아니라 주식수 변화만으로도 달라집니다. 순이익이 그대로여도 주식수가 줄면 EPS는 오르고, 주식수가 늘면 EPS는 내려갑니다.</p>

<p>예를 들어 <a href="https://sensitiveboss3.tistory.com/entry/treasury-stock-cancellation-tax" target="_blank" rel="noopener">자사주를 소각</a>하면 유통주식수가 줄어 순이익 개선 없이도 EPS가 오릅니다. 반대로 무상증자로 주식수가 늘면 순이익이 그대로여도 EPS는 낮아집니다.</p>

<ul style="line-height:1.9;">
  <li>EPS가 오른 이유가 순이익 증가인지 주식수 감소인지 구분해서 봅니다.</li>
  <li>일회성 이익(자산 매각 등)이 순이익에 섞여 EPS를 일시적으로 높였는지도 확인합니다.</li>
  <li>EPS 하나만 보지 말고 매출·영업이익 추세와 함께 봅니다.</li>
</ul>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">EPS는 어디서 확인하나요</h2>

<p>기업의 기본EPS와 희석EPS는 <a href="https://dart.fss.go.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a>에서 해당 기업의 사업보고서나 분기보고서를 열어 재무제표 주석의 '주당손익' 항목을 확인하면 됩니다. <a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a>이나 증권사 MTS의 종목 상세 화면에서도 EPS를 함께 보여줍니다.</p>

<h2 style="border-left:6px solid #b8860b;padding-left:12px;margin-top:36px;">더 짚어두면 좋은 것들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EPS가 마이너스면 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">당기순손실이 났다는 뜻입니다. 나누는 분자(순이익)가 음수이므로 EPS도 음수로 표시됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">희석EPS가 항상 계산되나요</summary>
  <p style="margin:10px 0 0 0;">전환사채·스톡옵션처럼 잠재적으로 주식으로 바뀔 수 있는 권리가 있는 기업만 희석EPS를 별도로 공시합니다. 그런 권리가 없으면 기본EPS와 희석EPS가 같습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EPS와 BPS는 무엇이 다른가요</summary>
  <p style="margin:10px 0 0 0;">EPS는 주당 순이익(1년 성과)을, BPS는 주당 순자산(누적 자기자본)을 나타냅니다. EPS를 BPS로 나누면 ROE가 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EPS는 분기마다 바뀌나요</summary>
  <p style="margin:10px 0 0 0;">네. 분기·반기 실적이 발표될 때마다 당기순이익과 유통주식수가 갱신되므로 EPS도 그때마다 다시 계산됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://dart.fss.go.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a></li>
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템 - 투자지표</a></li>
    <li><a href="https://www.khan.co.kr/article/201410211405291" target="_blank" rel="noopener">경향신문 - 오늘의 경제용어 주당순이익(EPS)</a></li>
  </ul>
  기준일: 2026년 9월 기준. 계산 예시는 이해를 돕기 위한 가상의 수치입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 EPS라는 재무지표를 계산하고 해석하는 방법을 설명하는 정보 글로, 특정 종목을 사라거나 팔라고 권하지 않습니다. 계산에 쓰인 숫자는 이해를 돕기 위해 만든 가상의 사례이며 실제 기업의 재무 수치가 아닙니다. 투자를 결정하기 전에는 해당 기업의 최신 공시를 직접 확인하시기 바랍니다. 투자 결과에 대한 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "EPS 뜻과 계산 방법",
  "description": "EPS(주당순이익)의 뜻과 계산 공식, 기본EPS와 희석EPS의 차이, EPS 성장률 계산법, 주식수 변동이 EPS를 왜곡시키는 이유를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-27",
  "dateModified": "2026-09-27",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/eps-meaning-calculation"
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
      "name": "EPS가 마이너스면 무슨 뜻인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "당기순손실이 났다는 뜻입니다. 나누는 분자(순이익)가 음수이므로 EPS도 음수로 표시됩니다." }
    },
    {
      "@type": "Question",
      "name": "희석EPS가 항상 계산되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "전환사채·스톡옵션처럼 잠재적으로 주식으로 바뀔 수 있는 권리가 있는 기업만 희석EPS를 별도로 공시합니다. 그런 권리가 없으면 기본EPS와 희석EPS가 같습니다." }
    },
    {
      "@type": "Question",
      "name": "EPS와 BPS는 무엇이 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "EPS는 주당 순이익(1년 성과)을, BPS는 주당 순자산(누적 자기자본)을 나타냅니다. EPS를 BPS로 나누면 ROE가 됩니다." }
    },
    {
      "@type": "Question",
      "name": "EPS는 분기마다 바뀌나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 분기·반기 실적이 발표될 때마다 당기순이익과 유통주식수가 갱신되므로 EPS도 그때마다 다시 계산됩니다." }
    }
  ]
}
</script>
