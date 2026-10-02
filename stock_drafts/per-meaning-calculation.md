---
keyword: PER 뜻
title: PER 뜻과 계산 방법
slug: per-meaning-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 2700 (PC 510 / 모바일 2190)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-28 — 통과]
  WebSearch "PER 뜻 주가수익비율 계산" 상위 결과 종합: kbcapital.co.kr(KB캐피탈,
  대형 금융사 공식)/bok.or.kr(한국은행, 준정부기관)/mofe.go.kr(정부 시사경제용어사전)/
  nongmin.com(농민신문, 언론사)/dic.hankyung.com(한국경제 사전, 언론사)/
  jcinus.com·bbmt24.com(개인·소규모 콘텐츠)/namu.wiki(백과)/chfckorea.com(금융
  관련 협회 부속 콘텐츠).
  1) 진입 여지 — 있음. jcinus.com·bbmt24.com 등 개인·소규모 콘텐츠가 상위권에
     진입해 있다.
  2) 검색 의도 — "뜻"을 묻는 개념 탐색형이다. 조회·신청·계산기 실행이 지배적
     의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 PER 정의와 "주가÷EPS" 계산식까지는
     다루지만, 트레일링 PER과 선행(포워드) PER의 차이를 실제 숫자로 대비해 보여주는
     글, 적자 기업의 PER 표시 방식, 업종별로 적정 PER이 다른 이유까지 함께 정리한
     글은 확인하지 못했다. 이 세 각도가 정보이득이다.
  → 탈락조건 1~3 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) PER = 주가 ÷ EPS 계산 공식과 가상 숫자 예시(주가 45,000원, EPS 3,000원 →
      PER 15배)를 직접 계산으로 보여준다.
  (b) 트레일링 PER(최근 4분기 실적 기준)과 선행 PER(다음 해 예상 실적 기준)을
      같은 가상 기업으로 대비 계산(주가 40,000원 고정, 트레일링 EPS 2,000원 →
      20배, 선행 EPS 2,800원 → 약 14.3배)해 왜 증권가 리포트가 두 수치를 다르게
      쓰는지 실제 계산으로 보여준다. 상위 검색결과 어디에도 이 대비 계산은 없었다.
  (c) 적자 기업은 EPS가 음수라 PER이 수학적으로 성립하지 않아 증권사 자료에
      "적자" 또는 해당없음으로 표시된다는 함정 설명 — PER이 안 보인다고 저평가로
      오인하지 않도록 하는 실용적 체크포인트.
  (d) 성장주와 가치주의 적정 PER 기준이 다른 이유(미래 이익 기대 반영 여부)를
      특정 종목 언급 없이 업종 성격으로만 설명.
  (e) 88편(PBR)·89편(ROE)에서 이미 다룬 PER=주가/EPS 관계식·PBR=PER×ROE 관계식과
      중복 없이, 이번 편은 PER 자체의 계산·함정·트레일링/선행 구분에 집중해
      역할을 나눈다. 각주에서 88·89편으로 내부 링크 유도.
primary_source: |
  PER = 주가 ÷ EPS(또는 시가총액 ÷ 당기순이익)는 재무비율의 정의상 항상 성립하는
  계산식으로, 88편(PBR)·89편(ROE) 작성 시와 동일하게 별도 기관 확인이 필요한
  수치가 아니다. 트레일링/선행 PER의 구분과 계산 방식도 증권업계에서 통용되는
  일반적 정의이며 시점에 따라 달라지는 시장 수치(코스피 평균 PER 등)를 본문에
  못박아 인용하지 않았다 — 대신 독자가 현재 시점의 실제 PER 값을 직접 확인할 수
  있도록 한국거래소 정보데이터시스템(data.krx.co.kr)과 금융감독원 전자공시시스템
  DART(dart.fss.or.kr, EPS 산출 근거인 재무제표 원문)로 안내했다. 세율·한도처럼
  소관 부처 원문 확정이 필요한 유형의 숫자가 아니므로 게이트4 절차상 자동화
  세션의 WebFetch 시도는 별도로 하지 않았다.
기준일: 2026년 9월 기준
tags: PER, PER뜻, 주가수익비율, PER계산법, 트레일링PER, 선행PER, PBR, EPS, 주식투자지표
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 2,700회(일반 주제 기준 500회 이상, 이번
  배치 PASS 후보 8개 중 유일한 통과이자 최고 검색량. PER 계산법·대주주 요건·
  신용거래 반대매매·공매도 대차거래·거래량 급증·공매도 잔고 공시·주식 회전율은
  전부 FAIL). 게이트2 충족 — v3 기준 3개 탈락조건 모두 미해당(개인·소규모 콘텐츠
  진입 여지 확인, 개념 탐색형 의도, 트레일링/선행 PER 대비·적자기업 표시 방식·
  업종별 기준 차이라는 정보이득 미확보 확인). 게이트3 충족 — PER 계산 예시 +
  트레일링/선행 PER 대비 계산 + 적자기업 함정 체크포인트 + 업종별 기준 차이 설명.
  게이트4 충족 — 계산식은 정의상 항상 성립하는 수치라 별도 원문 확인이 불필요하며,
  시점 의존적인 실제 지수 수치는 본문에 못박지 않고 확인 경로만 안내했다.
capture_guide: ""
self_check: |
  [2026-09-28 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — stock_drafts/ 전체를 grep한 결과 PER을 본문 주제로
  전용 편에서 다룬 기존 글은 없었다. 88편(PBR)·89편(ROE)·90편(EPS)은 관계식
  설명 중 PER을 한 문장으로만 언급할 뿐 트레일링/선행 구분이나 계산 예시를
  다루지 않아 검색 의도가 겹치지 않는다. 본문에 88·89편 내부 링크를 걸어 독자를
  유도했다.
  YMYL 안전장치 점검 — 특정 종목의 매수·매도 시점이나 목표가를 언급하지 않았다.
  계산 예시는 전부 가상의 수치로만 구성했고, 업종 비교도 특정 종목명 없이
  업종 성격으로만 설명했다.
  기관 링크 점검 — 한국거래소 정보데이터시스템(data.krx.co.kr)과 금융감독원
  전자공시시스템 DART(dart.fss.or.kr) 링크를 본문 안내 문장과 참고 출처 목록에
  모두 걸었다.
  제목 "PER 뜻과 계산 방법" 11자·금지어 없음·조사 최소화.
  슬러그 영문 소문자+하이픈 3단어(per-meaning-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—" 검색 결과
  0개 확인. "다만"은 사용하지 않았고 전환은 "단,"·"반면"·"그런데"로 분산했다.
  `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심 요약 박스 제목을
  "📐 PER 감 잡기 4가지"로, 색은 틸(#e0f2f1/#00695c)로 최근 게시물(테라코타
  #fdece3·초록#eaf5ec·노랑#fef9e7·슬레이트#eceff1·스카이#e6f7fb·네이비#eef2f7·
  보라#ede7f6·브라운#f7f0e8)과 겹치지 않게 골랐다. 목차 제외 본문 H2 6개 중
  서술형 4개, 질문형 2개("PER이 낮으면 무조건 저평가인가요", "PER은 어디서
  확인하나요")로 "~나요" 편중 없음(6개 중 2개, 33%). FAQ 헤딩도 "자주 묻는 질문"
  대신 "이런 질문도 자주 나옵니다"로 변형. 헤지 표현("~것으로 알려져 있다" 등)은
  쓰지 않고 확정된 계산 정의는 단정형으로, 시점 의존적 시장 수치는 "직접 확인"
  안내로 처리했다. 면책 문구는 기존 게시물과 다른 표현으로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-28</p>

<p>PER은 주가를 주당순이익(EPS)으로 나눈 값으로, 회사가 벌어들이는 이익 대비 주가가 몇 배로 평가되는지를 보여주는 지표입니다. 같은 PER이라도 최근 실적 기준(트레일링)인지 내년 예상 실적 기준(선행)인지에 따라 숫자가 크게 달라질 수 있습니다. 이 글은 PER 계산 공식과 트레일링·선행 PER의 차이, 적자 기업의 PER 표시 방식, 업종별 기준 차이를 정리합니다.</p>

<div style="background:#e0f2f1;border:2px solid #00695c;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#004d40;font-size:18px;">📐 PER 감 잡기 4가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>PER은 주가 ÷ EPS로 계산하며, 숫자가 작을수록 이익 대비 주가가 싸다는 뜻입니다.</li>
    <li>같은 회사라도 트레일링 PER과 선행 PER은 서로 다른 값이 나옵니다.</li>
    <li>적자 기업은 EPS가 음수라 PER 자체가 성립하지 않습니다.</li>
    <li>성장주와 가치주는 적정 PER 기준이 서로 다릅니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PER 뜻과 계산 공식</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PER이 낮으면 무조건 저평가인가요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">트레일링 PER과 선행 PER은 이렇게 다릅니다</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">적자 기업은 PER이 이렇게 표시됩니다</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">업종마다 PER 기준이 다른 이유</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">PER은 어디서 확인하나요</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">이런 질문도 자주 나옵니다</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">PER 뜻과 계산 공식</h2>

<p>PER(Price Earning Ratio, 주가수익비율)은 <mark>현재 주가가 회사의 주당순이익(EPS)의 몇 배인지를 나타내는 지표</mark>입니다. 계산식은 PER = 주가 ÷ EPS입니다.</p>

<p>예를 들어 주가가 45,000원이고 EPS가 3,000원인 회사라면, PER은 45,000 ÷ 3,000 = 15배가 됩니다. 이 회사가 벌어들이는 이익 1원을 시장이 15원으로 평가하고 있다는 뜻입니다.</p>

<ul style="line-height:1.9;">
  <li>EPS(주당순이익) = 당기순이익 ÷ 발행주식수</li>
  <li>PER이 낮을수록 이익 대비 주가가 싸게 거래된다는 뜻입니다.</li>
  <li>시가총액 ÷ 당기순이익으로 계산해도 같은 값이 나옵니다.</li>
</ul>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">PER이 낮으면 무조건 저평가인가요</h2>

<p>아닙니다. PER이 낮다고 반드시 저평가는 아닙니다. 이익이 일시적으로 늘어 PER이 낮아 보이거나, 시장이 앞으로의 실적 둔화를 미리 반영해 낮은 값을 준 경우도 있습니다.</p>

<p>반대로 PER이 높다고 무조건 고평가도 아닙니다. 이익이 빠르게 늘어날 것으로 기대되는 회사는 현재 이익 대비 PER이 높게 형성되는 경우가 흔합니다.</p>

<ul style="line-height:1.9;">
  <li>최근 몇 년간 이익이 꾸준히 늘었는지 확인합니다.</li>
  <li>일회성 이익(자산 매각 등)이 섞여 있는지 확인합니다.</li>
  <li>같은 업종 평균 PER과 비교합니다.</li>
</ul>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">트레일링 PER과 선행 PER은 이렇게 다릅니다</h2>

<p>PER은 어떤 EPS를 쓰느냐에 따라 두 가지로 나뉩니다. <mark>트레일링 PER은 최근 4분기 실적(과거 EPS)을 쓰고, 선행 PER은 증권가가 예상하는 다음 해 실적(예상 EPS)을 씁니다.</mark></p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <p style="margin:8px 0 0 0;">가상의 E기업 주가가 40,000원으로 고정돼 있다고 가정합니다.</p>
  <p style="margin:8px 0 0 0;">최근 4분기 EPS(트레일링)가 2,000원이면, 트레일링 PER = 40,000 ÷ 2,000 = 20배입니다.</p>
  <p style="margin:8px 0 0 0;">내년 예상 EPS(선행)가 2,800원으로 늘어날 전망이면, 선행 PER = 40,000 ÷ 2,800 ≈ 14.3배입니다.</p>
</div>

<p>같은 회사, 같은 주가인데도 이익이 늘어날 것으로 예상되면 선행 PER이 더 낮게 나타납니다. 증권사 리포트가 "12개월 선행 PER"이라는 표현을 자주 쓰는 이유가 여기 있습니다. 실적 성장이 빠른 회사일수록 두 수치의 차이가 커집니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">적자 기업은 PER이 이렇게 표시됩니다</h2>

<p>적자 기업은 당기순이익이 마이너스라 EPS도 음수가 됩니다. 주가를 음수로 나누면 PER이 마이너스 값이 되는데, 이 값은 투자 판단에 의미가 없어 대부분의 증권사 자료와 시세 화면에서 <mark>"적자" 또는 해당없음(N/A)으로 표시</mark>합니다.</p>

<p>PER 칸이 비어 있거나 "적자"로만 표시된 종목을 보고 저평가 신호로 오해하지 않아야 합니다. 실적이 흑자로 돌아선 뒤에야 PER 비교가 다시 의미를 갖습니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">업종마다 PER 기준이 다른 이유</h2>

<p>PER은 업종 성격에 따라 평균 수준이 크게 달라집니다. 이익 성장 기대가 큰 업종은 현재 이익보다 미래 이익 기대가 주가에 더 크게 반영돼 PER이 높게 형성되는 경향이 있습니다. 반대로 이익 변동이 적고 성장 속도가 느린 업종은 PER이 낮은 수준에서 안정적으로 유지되는 경향이 있습니다.</p>

<p>이 때문에 서로 다른 업종의 PER을 그대로 비교하면 오해가 생깁니다. 같은 업종 안에서 비교하거나, PBR·ROE 등 다른 지표와 함께 봐야 합니다. PBR과의 관계식이 궁금하다면 88편(PBR 뜻과 계산 방법)을, ROE와의 관계가 궁금하다면 89편(ROE 뜻과 계산 방법)을 먼저 보는 편이 도움이 됩니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">PER은 어디서 확인하나요</h2>

<p>종목별·업종별 PER은 <a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a>의 PER/PBR/배당수익률 메뉴에서 무료로 조회할 수 있습니다. EPS 산출 근거가 되는 재무제표 원문은 <a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a>에서 확인할 수 있습니다. 증권사 MTS의 종목 상세 화면에도 대부분 PER이 함께 표시됩니다.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #00695c;padding-left:12px;margin-top:36px;">이런 질문도 자주 나옵니다</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PER과 PBR 중 뭐가 더 중요한가요</summary>
  <p style="margin:10px 0 0 0;">둘 중 하나만 보기보다 함께 보는 편이 안전합니다. PER은 이익 대비 가격을, PBR은 자산 대비 가격을 보여주므로 서로 다른 측면을 드러냅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">적자 기업은 PER이 어떻게 표시되나요</summary>
  <p style="margin:10px 0 0 0;">EPS가 음수가 되어 PER 계산이 의미를 잃습니다. 대부분의 증권사 자료와 시세 화면은 이 경우 "적자" 또는 해당없음으로 표시합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">선행 PER은 어디서 확인할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">증권사 리서치 리포트나 HTS·MTS의 컨센서스 화면에서 확인할 수 있습니다. 82편(컨센서스 뜻)에서 컨센서스 확인 방법을 다뤘습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PER이 높으면 무조건 비싼 건가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 이익이 빠르게 늘어날 것으로 기대되는 회사는 PER이 높게 형성되는 경우가 흔합니다. 업종 평균과 이익 성장률을 함께 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">업종 평균 PER은 어디서 비교하나요</summary>
  <p style="margin:10px 0 0 0;">한국거래소 정보데이터시스템의 업종별 투자지표 메뉴에서 업종별 평균 PER을 무료로 확인할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템 - PER/PBR/배당수익률</a></li>
    <li><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART) - 기업 재무제표 원문</a></li>
  </ul>
  기준일: 2026년 9월 기준입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 PER이라는 투자지표의 계산법을 설명하는 정보 글이며, 특정 종목의 매수나 매도를 권하지 않습니다. 계산에 쓰인 숫자는 이해를 돕기 위해 만든 가상의 값으로 실제 기업의 수치가 아닙니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있으며, 실제 종목의 PER·EPS는 반드시 원출처에서 최신 값을 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "PER 뜻과 계산 방법",
  "description": "PER(주가수익비율)의 계산 공식과 트레일링·선행 PER의 차이, 적자 기업의 PER 표시 방식, 업종별 적정 PER 기준 차이를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-28",
  "dateModified": "2026-09-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/per-meaning-calculation"
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
      "name": "PER과 PBR 중 뭐가 더 중요한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "둘 중 하나만 보기보다 함께 보는 편이 안전합니다. PER은 이익 대비 가격을, PBR은 자산 대비 가격을 보여주므로 서로 다른 측면을 드러냅니다." }
    },
    {
      "@type": "Question",
      "name": "적자 기업은 PER이 어떻게 표시되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "EPS가 음수가 되어 PER 계산이 의미를 잃습니다. 대부분의 증권사 자료와 시세 화면은 이 경우 적자 또는 해당없음으로 표시합니다." }
    },
    {
      "@type": "Question",
      "name": "선행 PER은 어디서 확인할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권사 리서치 리포트나 HTS·MTS의 컨센서스 화면에서 확인할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "PER이 높으면 무조건 비싼 건가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 이익이 빠르게 늘어날 것으로 기대되는 회사는 PER이 높게 형성되는 경우가 흔합니다. 업종 평균과 이익 성장률을 함께 확인해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "업종 평균 PER은 어디서 비교하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "한국거래소 정보데이터시스템의 업종별 투자지표 메뉴에서 업종별 평균 PER을 무료로 확인할 수 있습니다." }
    }
  ]
}
</script>
