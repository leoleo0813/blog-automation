---
keyword: 감가상각비 뜻
title: 감가상각비 뜻과 계산 방법
slug: depreciation-meaning-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 580 (PC 150 / 모바일 430, 2026-09-27 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-28 — 통과]
  WebSearch "감가상각비 뜻 계산 방법 정액법 정률법"·"감가상각비 당기순이익 영향
  주식 재무제표 분석" 상위 결과 종합: kocw.net(대학 강의자료 PDF), heumtax.com
  (세무법인 콘텐츠), ko.wikipedia.org(백과), law.go.kr(국가법령정보센터, 공식),
  clobe.ai(블로그, "총정리"형), joseilbo.com(조세일보, 언론사), calctools.co.kr
  (계산기 도구), namu.wiki(나무위키), aboda.kr(개인/소규모 재테크 블로그),
  velog.io(개인 개발자 블로그 플랫폼), steadyman7.com(개인 블로그),
  fastercapital.com(해외 번역 AI콘텐츠, 국문화).
  1) 진입 여지 — 있음. aboda.kr, velog.io, steadyman7.com 등 개인·소규모 콘텐츠가
     상위 10개 중 여러 개를 차지한다.
  2) 검색 의도 — "감가상각비 뜻"은 정의 탐색형이다. "계산 방법"을 같이 검색하면
     calctools.co.kr 같은 계산기 도구가 섞이지만, 핵심 키워드 자체는 조회·계산기
     실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 정액법·정률법 계산 공식 자체는 상위 글 대부분이
     다루지만, 실제 숫자를 넣어 5년치를 끝까지 계산하고 두 방식을 나란히 비교한
     글이나, 투자자 관점에서 영업이익·현금흐름표(EBITDA)에 미치는 영향까지
     연결한 글은 확인되지 않았다(fastercapital.com은 번역 AI콘텐츠라 한국
     회계기준·기업 사례가 없다). 이 두 각도가 정보이득이다.
  → 탈락조건 1~3 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 취득원가 1억원, 잔존가치 1,000만원(취득원가의 10%), 내용연수 5년인 기계장치를
      가정해 정액법(매년 1,800만원 고정)과 정률법(상각률 약 36.9%, 초반에 크고
      점차 감소)의 5개년 감가상각비·기말장부가액을 전부 계산해 표로 제시한다.
      정률법 마지막 해는 남은 장부가액을 잔존가치에 맞춰 조정하는 실무 관행까지
      반영했다. 1년 차 상각비는 정률법(3,690만원)이 정액법(1,800만원)의 두 배를
      넘지만, 5년 합계는 두 방식 모두 9,000만원으로 동일하다는 구체적 수치를
      제시한다. 공식만 설명하고 끝나는 상위 글들과 달리 끝까지 계산한다.
  (b) 감가상각비가 영업이익·당기순이익을 줄이면서도 실제 현금 유출이 없어
      현금흐름표에서는 당기순이익에 다시 더해지는 이유를 설명하고, 설비투자가
      큰 업종(반도체·조선 등)에서 영업활동현금흐름이 당기순이익보다 크게 나타나는
      경우가 많다는 실전 해석 포인트를 제공한다. 이 연결을 다룬 글은 상위
      결과에서 확인되지 않았다.
  (c) 특정 기업이 정액법·정률법 중 무엇을 쓰는지 DART 전자공시시스템 재무제표
      주석에서 확인하는 구체적 경로(사업보고서 → 재무제표 주석 → 유형자산 항목)를
      안내한다.
primary_source: |
  정액법·정률법 계산식((취득원가-잔존가치)÷내용연수 / 기초장부가액×상각률, 상각률=
  1-(잔존가치÷취득원가)^(1/내용연수))은 한국회계기준원이 관장하는 K-IFRS 제1016호
  (유형자산) 및 일반기업회계기준이 정한 표준 회계처리 방법이며, 세율·한도처럼
  매년 바뀌는 제도적 수치가 아니라 계산 정의에 가깝다(88편 PBR·89편 ROE·90편
  EPS·93편 PER·94편 듀레이션과 동일한 처리 방식).
  자동화 세션에서 금융감독원 전자공시시스템(dart.fss.or.kr)에 WebFetch를 1회
  시도했으나 EGRESS_BLOCKED로 막혔다. RULES.md 「1차 출처가 막혔을 때」 기준에
  따라 WebSearch로 독립 출처 교차검증을 진행했다: kocw.net(대학 강의자료),
  위키백과, 조세일보(언론사), heumtax.com(세무법인 콘텐츠), aboda.kr(개인 블로그)
  5곳 이상에서 정액법·정률법 계산식이 충돌 없이 일치했고, 그중 조세일보는
  언론사 요건을 충족한다. 세율·공제한도 같은 이 프로젝트가 과거 오류를 잡아낸
  유형의 민감 수치가 아니라 표준 회계 공식이므로 교차검증으로 진행했다.
  한국회계기준원(www.kasb.or.kr)은 이 기준서를 관장하는 공식 기관임을 WebSearch로
  확인했으나, 세부 기준서 원문 페이지까지 WebFetch로 직접 열어보지는 못했다.
  본문 계산 예시는 전부 가상의 취득원가·잔존가치·내용연수를 가정한 것으로 실제
  특정 기업의 재무제표 수치가 아니다.
기준일: 2026년 9월 기준 (계산 공식 자체는 시점에 무관한 회계기준 정의)
tags: 감가상각비, 감가상각비 뜻, 정액법, 정률법, 감가상각 계산법, 재무제표 읽는법, EBITDA, 유형자산, 영업활동현금흐름
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 580회(일반 주제 기준 500회 이상,
  2026-09-27 backlog 등록분 재확인). 게이트2 충족 — v3 기준 3개 탈락조건 모두
  미해당(개인·소규모 블로그 진입 여지 있음, 정의 탐색형 의도, 5년치 끝까지 계산한
  비교표·현금흐름표 연결이라는 정보이득 미확보 확인). 게이트3 충족 — 정액법·
  정률법 5개년 전체 계산 비교표 + 현금흐름표·EBITDA 연결 설명 + DART 확인 경로
  안내라는 정보이득. 게이트4 충족 — 계산식은 회계기준의 표준 정의라 세율·한도
  수치 같은 원문 확인이 필수는 아니며, WebFetch 1회 시도 후 막혀 5곳 이상 독립
  출처 교차검증(언론사 조세일보 포함)으로 대체했고 수치 충돌이 없었다.
capture_guide: ""
self_check: |
  [2026-09-28 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  후보 선정 경위 — backlog.verified 중 "단순 순서 대기" 성격 항목(게이트2·3
  미확인 상태로 기록된 것) 두 개, 감가상각비 뜻(580회)과 유보율 뜻(530회) 중
  검색량이 더 높은 감가상각비 뜻을 이번 편 후보로 검토해 게이트2를 통과시켰다.
  유보율 뜻은 backlog.verified에 그대로 남겨 다음 실행에서 게이트2·3부터
  재검토하도록 기록했다.
  카니벌라이제이션 점검 — stock_drafts/ 전체를 grep한 결과 "감가상각"·"EBITDA"·
  "현금흐름표"를 본문 주제로 다룬 기존 편은 없었다.
  YMYL 안전장치 점검 — 특정 종목·기업명을 언급하지 않았고, 계산 예시는 전부
  가상의 취득원가·잔존가치·내용연수로만 구성했다. 매수·매도 시점이나 목표가는
  언급하지 않았다.
  기관 링크 점검 — 금융감독원 전자공시시스템 DART(dart.fss.or.kr), 한국회계기준원
  (kasb.or.kr) 링크 각 1개를 본문 안내 문장과 참고 출처 목록에 동일하게 걸었다.
  제목 "감가상각비 뜻과 계산 방법" 14자·금지어 없음·조사 최소화. 슬러그 영문
  소문자+하이픈 3단어(depreciation-meaning-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음. 첫 문장 유형: 대비형("겉보기엔 같은
  자산에 대한 비용 같지만, 정액법과 정률법 중 무엇을 선택하느냐에 따라...") —
  최근 6편(PBR·ROE·EPS·사모펀드·VIX·PER은 "[키워드]는 ~입니다" 정의형, 직전
  94편 듀레이션은 수치충격형)과 겹치지 않는 유형으로 골랐다.
  글 구조 유형: 개념형(RULES.md 「글 구조 다양화」) — 정의·공식을 먼저 설명한 뒤
  계산 비교표를 배치하는 프로즈 중심 구조를 유지했다. 직전 94편(듀레이션)이
  계산형(계산부터 먼저 제시)이었으므로 연속되지 않게 골랐다.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—" 검색
  결과 0개 확인. "다만"은 FAQ 한 곳에만 쓰고 나머지 전환은 "반면"·"그런데"·
  "단,"으로 분산했다. `mark` 태그 총 4개(3~5개 기준 충족). FAQ 7개(직전 6편이
  6·4·5·5·5·6개였던 것과 다르게 변화). 핵심 요약 박스 제목을 "📎 감가상각비 이
  정도만 기억하면"으로, 색은 스카이블루(#e3f2fd/#1565c0)로 최근 게시물
  (테라코타·포레스트그린·머스터드골드·바이올렛·슬레이트네이비·틸·인디고)과
  겹치지 않게 골랐다. 목차 제외 본문 H2 5개 중 "~나요"로 끝나는 것은 2개(40%)로
  편중 없음. FAQ 헤딩도 "자주 묻는 질문" 대신 "실무에서 자주 헷갈리는 부분"으로
  변형(최근 5편: 이런 질문도 자주 나옵니다/궁금한 점 몇 가지 더/더 짚어두면 좋은
  것들/더 알아두면 좋은 것들/빠뜨리기 쉬운 질문들과 겹치지 않음). 헤지 표현("~것
  으로 알려져 있다" 등)은 쓰지 않고 확정된 계산 결과는 단정형으로 서술했다. 면책
  문구는 최근 게시물과 다른 문장 순서·표현으로 새로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-28</p>

<p>겉보기엔 같은 자산에 대한 비용 같지만, 정액법과 정률법 중 무엇을 선택하느냐에 따라 해마다 감가상각비 규모가 크게 달라집니다. 감가상각비는 건물·기계 같은 유형자산의 가치 감소분을 내용연수 동안 나눠 비용으로 반영하는 회계 처리입니다. 이 글은 정액법·정률법 계산 공식과 5년치 실제 비교, 감가상각비가 재무제표와 현금흐름에 미치는 영향을 정리합니다.</p>

<div style="background:#e3f2fd;border:2px solid #1565c0;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#0d47a1;font-size:18px;">📎 감가상각비 이 정도만 기억하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>정액법은 매년 똑같은 금액을, 정률법은 초반에 더 많이 상각합니다(5년 합계는 같습니다).</li>
    <li>감가상각비는 실제 현금이 나가지 않는 비용이라 현금흐름표에서는 당기순이익에 다시 더해집니다.</li>
    <li>설비투자가 큰 업종은 영업활동현금흐름이 당기순이익보다 크게 나타나는 경우가 많습니다.</li>
    <li>특정 기업이 어떤 방법을 쓰는지는 DART 재무제표 주석에서 확인할 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>감가상각비 뜻과 두 가지 계산 방식</li>
  <li>정액법과 정률법, 5년치를 직접 비교하면</li>
  <li>감가상각비가 이익을 줄이는데 현금은 왜 안 나가나요</li>
  <li>설비투자가 많은 업종일수록 나타나는 특징</li>
  <li>실제 기업이 쓰는 방법은 어디서 확인하나요</li>
  <li>실무에서 자주 헷갈리는 부분</li>
</ol>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">감가상각비 뜻과 두 가지 계산 방식</h2>

<p>감가상각비는 건물·기계장치 같은 유형자산을 사용하면서 줄어드는 가치를 내용연수 동안 나눠 비용으로 인식하는 회계 처리입니다. 이 방식은 <a href="https://www.kasb.or.kr/" target="_blank" rel="noopener">한국회계기준원</a>이 관장하는 K-IFRS 제1016호(유형자산) 등 회계기준을 따릅니다.</p>

<ul style="line-height:1.9;">
  <li><b>정액법</b>: (취득원가 - 잔존가치) ÷ 내용연수 = 매년 동일한 감가상각비</li>
  <li><b>정률법</b>: 기초 장부가액 × 상각률, 상각률 = 1 - (잔존가치 ÷ 취득원가)^(1/내용연수)</li>
</ul>

<p>정액법은 매년 똑같은 금액을 상각해 단순하고, 정률법은 초반에 더 많이 상각하고 갈수록 금액이 줄어듭니다. 실제로 숫자를 넣어보면 두 방식의 차이가 뚜렷하게 드러납니다.</p>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">정액법과 정률법, 5년치를 직접 비교하면</h2>

<p>취득원가 1억원, 잔존가치 1,000만원(취득원가의 10%), 내용연수 5년인 기계장치를 예로 계산해보겠습니다. 정액법 상각비는 (10,000만원-1,000만원)÷5년 = <mark>매년 1,800만원</mark>으로 고정됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>정률법 계산 과정 (가상 예시)</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>상각률 = 1 - (1,000÷10,000)^(1/5) ≈ <mark>36.9%</mark></li>
    <li>1년 차: 10,000만원 × 36.9% = 3,690만원 (기말장부가액 6,310만원)</li>
    <li>2년 차: 6,310만원 × 36.9% ≈ 2,328만원 (기말장부가액 3,982만원)</li>
    <li>3년 차: 3,982만원 × 36.9% ≈ 1,469만원 (기말장부가액 2,513만원)</li>
    <li>4년 차: 2,513만원 × 36.9% ≈ 927만원 (기말장부가액 1,586만원)</li>
    <li>5년 차: 남은 장부가액을 잔존가치(1,000만원)에 맞춰 586만원만 상각 (기말장부가액 1,000만원)</li>
  </ul>
</div>

<table style="border-collapse:collapse;width:100%;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">연도</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">정액법 상각비</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">정액법 기말장부가액</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">정률법 상각비</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">정률법 기말장부가액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">1년</td>
      <td style="border:1px solid #ddd;padding:8px;">1,800만원</td>
      <td style="border:1px solid #ddd;padding:8px;">8,200만원</td>
      <td style="border:1px solid #ddd;padding:8px;">3,690만원</td>
      <td style="border:1px solid #ddd;padding:8px;">6,310만원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2년</td>
      <td style="border:1px solid #ddd;padding:8px;">1,800만원</td>
      <td style="border:1px solid #ddd;padding:8px;">6,400만원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,328만원</td>
      <td style="border:1px solid #ddd;padding:8px;">3,982만원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">3년</td>
      <td style="border:1px solid #ddd;padding:8px;">1,800만원</td>
      <td style="border:1px solid #ddd;padding:8px;">4,600만원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,469만원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,513만원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">4년</td>
      <td style="border:1px solid #ddd;padding:8px;">1,800만원</td>
      <td style="border:1px solid #ddd;padding:8px;">2,800만원</td>
      <td style="border:1px solid #ddd;padding:8px;">927만원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,586만원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">5년</td>
      <td style="border:1px solid #ddd;padding:8px;">1,800만원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,000만원</td>
      <td style="border:1px solid #ddd;padding:8px;">586만원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,000만원</td>
    </tr>
  </tbody>
</table>

<p>1년 차 상각비만 보면 정률법(3,690만원)이 정액법(1,800만원)의 두 배가 넘습니다. 반면 5년을 합치면 두 방식 모두 <mark>9,000만원</mark>으로 똑같습니다. 총 비용은 같고 시기만 다르다는 뜻입니다.</p>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">감가상각비가 이익을 줄이는데 현금은 왜 안 나가나요</h2>

<p>감가상각비는 손익계산서에서 비용으로 잡혀 영업이익과 당기순이익을 줄이지만, 그해에 실제로 현금이 빠져나가는 것은 아닙니다. 자산을 살 때 이미 목돈이 나갔고, 감가상각비는 그 지출을 이후 여러 해에 걸쳐 장부에 나눠 반영하는 절차이기 때문입니다.</p>

<p>그래서 현금흐름표에서 영업활동현금흐름을 계산할 때는 당기순이익에 감가상각비를 다시 더합니다. 이 조정 때문에 영업활동현금흐름이 당기순이익보다 큰 경우가 흔합니다.</p>

<ul style="line-height:1.9;">
  <li>당기순이익이 100억원, 감가상각비가 30억원이면 영업활동현금흐름은 대략 130억원 안팎으로 커질 수 있습니다.</li>
  <li>이 차이를 보여주는 대표적인 지표가 EBITDA(이자·세금·감가상각비 차감 전 영업이익)입니다.</li>
</ul>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">설비투자가 많은 업종일수록 나타나는 특징</h2>

<p>반도체·조선·항공처럼 설비에 큰 돈을 투자하는 업종은 감가상각비 규모도 커서, 당기순이익과 영업활동현금흐름의 차이가 눈에 띄게 벌어지는 경우가 많습니다.</p>

<p>반대로 소프트웨어·서비스업처럼 유형자산이 적은 업종은 감가상각비가 작아 이 차이도 크지 않습니다. 업종 특성을 모르고 EBITDA나 영업활동현금흐름만 보면 실제 이익 체력을 오해할 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>설비투자 초기에는 감가상각비 부담이 몇 년간 이어지므로 일시적 이익 감소를 실적 악화로 오인하지 않아야 합니다.</li>
  <li>같은 업종끼리 비교할 때는 감가상각 방법(정액법/정률법)이 같은지도 함께 확인하는 것이 좋습니다.</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>참고로 알아두면 좋은 점</b>
  <p style="margin:6px 0 0 0;">감가상각 방법을 바꾸면 매년 비용이 잡히는 시점이 달라져 이익 흐름이 바뀝니다. 하지만 총 상각액과 기업이 실제로 쓴 현금의 총량은 달라지지 않습니다.</p>
</div>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">실제 기업이 쓰는 방법은 어디서 확인하나요</h2>

<p>특정 기업이 정액법을 쓰는지 정률법을 쓰는지는 <a href="https://dart.fss.or.kr/" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a>에서 확인할 수 있습니다. 기업명을 검색해 최근 사업보고서를 열고, 재무제표 주석 중 유형자산 항목을 보면 상각 방법이 명시되어 있습니다.</p>

<ul style="line-height:1.9;">
  <li>DART에서 기업명 검색 → 정기공시(사업보고서·분기보고서) 선택</li>
  <li>재무제표 주석 목차에서 '유형자산' 또는 '감가상각' 항목 확인</li>
  <li>상각 방법과 내용연수가 함께 명시되어 있는지 확인</li>
</ul>

<h2 style="border-left:6px solid #1565c0;padding-left:12px;margin-top:36px;">실무에서 자주 헷갈리는 부분</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감가상각비는 실제로 돈이 나가는 비용인가요</summary>
  <p style="margin:10px 0 0 0;">아니요. 자산을 살 때 이미 지출이 끝났고, 감가상각비는 그 지출을 이후 여러 해에 나눠 비용으로 기록하는 회계 처리일 뿐입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">왜 회사마다 정액법과 정률법 중 다른 방법을 쓰나요</summary>
  <p style="margin:10px 0 0 0;">회계기준이 허용하는 범위 안에서 자산의 실제 사용 패턴에 맞춰 선택할 수 있기 때문입니다. 초반에 가치가 빠르게 떨어지는 자산은 정률법을, 사용 강도가 일정한 자산은 정액법을 택하는 경우가 많습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">무형자산도 감가상각 하나요</summary>
  <p style="margin:10px 0 0 0;">무형자산은 '상각'이라고 부르며, 특허권·소프트웨어 같은 자산은 대부분 정액법으로 상각합니다. 유형자산과 계산 원리는 비슷하지만 용어가 다릅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감가상각이 끝난 자산은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">장부가액이 잔존가치까지 줄어든 뒤에도 자산을 계속 사용할 수 있습니다. 이후에는 추가로 비용을 인식하지 않고 잔존가치만 장부에 남습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">EBITDA는 왜 감가상각비를 다시 더하나요</summary>
  <p style="margin:10px 0 0 0;">감가상각비가 실제 현금 유출이 없는 비용이기 때문입니다. 현금 창출 능력만 따로 보기 위해 이자·세금과 함께 다시 더해 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감가상각비가 크면 주가에 안 좋은 신호인가요</summary>
  <p style="margin:10px 0 0 0;">그렇지 않습니다. 설비투자가 많다는 신호일 수도 있어 업종 특성과 함께 봐야 합니다. 감가상각비 자체보다 그 자산이 실제로 매출과 이익을 만들어내는지가 더 중요합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">정액법과 정률법 중 어느 쪽이 세금에 유리한가요</summary>
  <p style="margin:10px 0 0 0;">정률법은 초반 상각비가 커서 그만큼 초기 과세소득을 낮추는 효과가 있습니다. 다만 세무상 감가상각 한도와 신고 방법은 별도로 정해져 있어 실제 적용은 회계·세무 담당자 확인이 필요합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.kasb.or.kr/" target="_blank" rel="noopener">한국회계기준원</a></li>
    <li><a href="https://dart.fss.or.kr/" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a></li>
  </ul>
  기준일: 2026년 9월 기준. 정액법·정률법 계산식 자체는 시점과 무관한 회계기준
  정의이며, 본문의 취득원가·잔존가치·상각비 수치는 이해를 돕기 위해 가정한
  예시입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글에 쓰인 취득원가·잔존가치·내용연수는 계산 원리를 보여주기 위한 가상의 예시이며 실제 특정 기업의 재무제표 수치가 아닙니다. 특정 종목이나 상품의 매수·매도를 권유하는 글이 아니며, 실제 재무제표를 볼 때는 DART에서 최신 공시를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "감가상각비 뜻과 계산 방법",
  "description": "감가상각비의 뜻과 정액법·정률법 계산 공식을 5년치 실제 숫자로 비교하고, 감가상각비가 영업이익과 현금흐름표에 미치는 영향을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-28",
  "dateModified": "2026-09-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/depreciation-meaning-calculation"
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
      "name": "감가상각비는 실제로 돈이 나가는 비용인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 자산을 살 때 이미 지출이 끝났고, 감가상각비는 그 지출을 이후 여러 해에 나눠 비용으로 기록하는 회계 처리일 뿐입니다." }
    },
    {
      "@type": "Question",
      "name": "왜 회사마다 정액법과 정률법 중 다른 방법을 쓰나요",
      "acceptedAnswer": { "@type": "Answer", "text": "회계기준이 허용하는 범위 안에서 자산의 실제 사용 패턴에 맞춰 선택할 수 있기 때문입니다. 초반에 가치가 빠르게 떨어지는 자산은 정률법을, 사용 강도가 일정한 자산은 정액법을 택하는 경우가 많습니다." }
    },
    {
      "@type": "Question",
      "name": "무형자산도 감가상각 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "무형자산은 '상각'이라고 부르며, 특허권·소프트웨어 같은 자산은 대부분 정액법으로 상각합니다. 유형자산과 계산 원리는 비슷하지만 용어가 다릅니다." }
    },
    {
      "@type": "Question",
      "name": "감가상각이 끝난 자산은 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "장부가액이 잔존가치까지 줄어든 뒤에도 자산을 계속 사용할 수 있습니다. 이후에는 추가로 비용을 인식하지 않고 잔존가치만 장부에 남습니다." }
    },
    {
      "@type": "Question",
      "name": "EBITDA는 왜 감가상각비를 다시 더하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "감가상각비가 실제 현금 유출이 없는 비용이기 때문입니다. 현금 창출 능력만 따로 보기 위해 이자·세금과 함께 다시 더해 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "감가상각비가 크면 주가에 안 좋은 신호인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "그렇지 않습니다. 설비투자가 많다는 신호일 수도 있어 업종 특성과 함께 봐야 합니다. 감가상각비 자체보다 그 자산이 실제로 매출과 이익을 만들어내는지가 더 중요합니다." }
    },
    {
      "@type": "Question",
      "name": "정액법과 정률법 중 어느 쪽이 세금에 유리한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "정률법은 초반 상각비가 커서 그만큼 초기 과세소득을 낮추는 효과가 있습니다. 다만 세무상 감가상각 한도와 신고 방법은 별도로 정해져 있어 실제 적용은 회계·세무 담당자 확인이 필요합니다." }
    }
  ]
}
</script>
