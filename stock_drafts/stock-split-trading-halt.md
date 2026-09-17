---
keyword: 액면분할
title: 액면분할 매매정지 기간
slug: stock-split-trading-halt
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1980 (PC 450 / 모바일 1530, 2026-09-17 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-17 — 통과]
  WebSearch "액면분할 뜻 효과 주가" + "액면분할 신주 상장일 절차 액면미달발행 제한" 상위 종합:
  brunch.co.kr(개인 블로그, ×2) / viva100.com(브릿지경제, 언론) / kbthink.com(KB 금융
  공식) / zuzu.network(스타트업 서비스 콘텐츠) / mofe.go.kr(기획재정부 시사경제용어사전,
  공식) / s-space.snu.ac.kr(학술논문 PDF) / namu.wiki(백과) / infobaksa.com(개인/소규모
  블로그, "총정리"형) / help-me.kr(법무법인 블로그, ×2) / casenote.kr(판례 정보) /
  korea.legal(법무사 블로그) / klca.or.kr(코스닥협회 PDF)
  1) 진입 여지 — 있음. brunch.co.kr·zuzu.network·infobaksa.com·help-me.kr·korea.legal 등
     개인/소규모 콘텐츠·법무법인 블로그가 상위 다수 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻이 뭔지, 왜 하는지, 주가에 어떤 영향인지"). 조회·계산기
     실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 대부분이 액면분할의 정의·효과·주가 영향까지만 다루는
     사전형 설명에 그치고, "액면분할을 발표하면 실제로 며칠 동안 거래가 정지되는지"라는
     절차적 사실을 다루는 글은 확인하지 못했다. 이 부분이 정보이득.
  → 탈락조건 1·2 미해당, 탈락조건 3은 매매정지 기간·절차 정보이득으로 상쇄해 통과.
unique_asset: |
  "액면분할=주가에 좋다/나쁘다"만 다루는 기존 콘텐츠와 달리, 액면분할을 결정하면 신주가
  상장되기 전까지 실제로 며칠 동안 거래가 정지되는지를 2026년 실제 사례 2건으로 보여준다.
  - 와이씨켐(코스닥): 2026-04-10 매매정지 시작 → 2026-04-29 변경상장(거래재개) = 19일간
    정지. 액면가 1,000원→500원(2대1 분할), 발행주식수 1,111만545주→2,022만1,090주.
  - 동일기연(코스닥): 2026-06-24 매매정지 시작 → 2026-07-13 변경상장(거래재개) = 19일간
    정지. 액면가 500원→100원(5대1 분할), 발행주식수 351만8,595주→1,759만2,975주.
  - 대림제지(코스닥)는 이 초안 작성 시점(2026-09-17) 기준 바로 다음날인 2026-09-18부터
    같은 사유로 매매정지에 들어가는 진행 중인 사례라 "지금도 같은 규정이 적용되고 있다"는
    최신성 근거로 반영.
  두 확정 사례 모두 19일로 일치하며, 이는 한국거래소가 발간한 코스닥시장 공시·상장관리
  해설서가 밝힌 "매매거래정지 기간은 분할기준일 1매매거래일 전부터 변경상장일 전일까지"
  라는 규정과 부합한다. 근거 규정(코스닥시장업무규정 제25조·시행세칙 제30조)까지 확인해
  "언제부터 언제까지, 왜 정지되는지"를 절차 타임라인표로 정리했다.
primary_source: |
  1차 시도: 한국거래소 KIND(kind.krx.co.kr) 매매거래정지 공시 페이지 WebFetch 1회 시도 →
  EGRESS_BLOCKED(2026-09-17). 대조군으로 무관한 도메인(www.digitaltoday.co.kr,
  www.google.com)에도 각 1회씩 추가 시도했으나 전부 동일하게 EGRESS_BLOCKED로 확인돼
  이번 세션의 전면 차단으로 판단했다(RULES.md 누적 기록 패턴과 일치, 그 이상 재시도하지
  않음).
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다.
  - 매매정지 근거 규정(코스닥시장업무규정 제25조·시행세칙 제30조)과 정지 기간 정의
    ("분할기준일 1매매거래일 전부터 변경상장일 전일까지")는 한국거래소가 발간한 「코스닥
    시장 공시·상장관리해설서」(kind.krx.co.kr 게시 PDF, 준정부기관 공식 발간물)에서
    확인했다.
  - 실제 사례 수치(정지 시작일·변경상장일·정지 기간·분할비율·발행주식수)는 서로 다른
    언론사 4곳 이상(디지털투데이, 데이터투자, 딜사이트, 블로터, 톱스타뉴스)이 와이씨켐·
    동일기연 각 사례에서 동일한 날짜와 비율로 보도해 충돌 없이 일치했다.
  - 매매정지 근거 규정과 실제 사례 모두 "언제부터 언제까지 정지되는가"라는 절차·사실
    관계이지, 세율·공제한도·과세표준처럼 이 프로젝트가 과거 오류를 잡아낸 유형의 숫자가
    아니라 교차검증으로 진행해도 되는 유형으로 판단했다.
기준일: 2026-09-17 (WebSearch 확인일)
tags: 액면분할, 매매정지, 신주상장, 변경상장, 코스닥, 주식초보, 재테크초보, 액면분할절차, 거래정지기간
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-17).
  게이트1: 네이버 키워드도구 실측 1,980회(check-keywords.yml, 2026-09-17 — 일반 주제
  기준 500회 이상). 같은 배치(2026-09-17)에서 함께 확인된 권리락(1,000회)·배당기준일
  (1,090회, 카니벌라이제이션 점검 필요)·미수거래(970회, 카니벌라이제이션 점검 필요)·
  배당수익률(860회)보다 검색량이 높고, "단순 순서 대기"로 분류된 항목 중 최고 검색량이라
  이번 편으로 채택했다.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그·법무법인 콘텐츠 진입 여지
  있고, 매매정지 실제 기간·절차를 다루는 글이 상위 결과에 없어 정보이득 여지 있음.
  게이트3: 2026년 실제 사례 2건(와이씨켐·동일기연, 정지기간 19일로 일치) + 진행 중인
  3번째 사례(대림제지) + 근거 규정·절차 타임라인표로 정보이득 확보.
  게이트4: kind.krx.co.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군(digitaltoday.co.kr·
  google.com)도 차단돼 세션 전면 차단 확인 후 RULES.md 2026-09-12 기준에 따라
  교차검증 진행 — 근거 규정·정지기간 정의는 한국거래소 공식 발간 해설서로, 실제 사례
  수치는 독립 언론 4곳 이상이 동일하게 보도해 신뢰도 확보.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 1,980회(일반 주제 기준 500회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은 매매정지
  기간·절차 정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 2026년 실제 사례 2건(19일로 수치 일치) + 진행 중인 사례 1건 + 근거
  규정·절차 타임라인표로 상위 결과가 다루지 않는 각도를 확보했다.
  게이트4 — kind.krx.co.kr 직접 열람은 막혔고(대조군 digitaltoday.co.kr·google.com도
  차단, 세션 전면 차단), 근거 규정·정지기간 정의는 한국거래소 공식 발간 해설서, 실제
  사례는 독립 언론 4곳 이상으로 교차검증해 진행했다.
  카니벌라이제이션 점검 — 1~44편 어디에도 액면분할·매매정지 관련 내용은 없다(그렙 검색
  확인). 배당기준일·미수거래처럼 기존 편과 검색 의도가 겹칠 우려가 없어 별도 점검 없이
  진행했다. 백로그에 남아있던 "액면가 뜻"(2,120회, 사전형이라 보류 중)과는 다른 각도
  (매매정지 절차)라 겹치지 않는다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 한국거래소 KIND 안내 문장과 하단 참고
  출처 목록 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow
  미부착. 출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "액면분할 매매정지 기간" 12자(공백 포함)·금지어 없음·조사·접속사 없음. 슬러그
  영문 소문자+하이픈 4단어(stock-split-trading-halt). 인트로 문단 최상단 배치. 표는
  thead/tbody 시맨틱 사용. 기준일 명시. FAQ 6개와 JSON-LD 1:1 일치. 종목·상품 추천
  표현, 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 한국거래소 공식 발간물 + 독립 언론 4곳
  이상 교차검증으로 대체, 한계는 본문·출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-17</p>

<p><mark>액면분할을 결정한 종목은 신주가 새로 상장되기 전까지 짧게는 2주에서 3주 가까이 거래 자체가 멈춥니다.</mark> 언제부터 언제까지 멈추는지, 그 사이 내 계좌의 주식은 어떻게 되는지 실제 사례로 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>매매정지는 <b>분할기준일 1매매거래일 전부터 변경상장일 전일까지</b> 이어집니다.</li>
    <li>2026년 실제 사례(와이씨켐·동일기연) 모두 <mark>정지 기간이 19일로 동일</mark>했습니다.</li>
    <li>정지 기간에도 <b>주식을 팔거나 새로 살 수는 없지만, 보유 자체는 그대로 유지</b>됩니다.</li>
    <li>액면분할은 발행주식수만 늘리는 것이라 <b>회사의 실제 가치(시가총액)는 바뀌지 않습니다.</b></li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>액면분할이 뭔가요</li>
  <li>액면분할을 하면 왜 거래가 멈추나요</li>
  <li>매매정지 기간은 실제로 며칠인가요</li>
  <li>액면분할은 어떤 순서로 진행되나요</li>
  <li>액면분할과 무상증자는 뭐가 다른가요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">액면분할이 뭔가요</h2>

<p>액면분할은 주식 1주의 액면가를 낮추는 대신 발행주식수를 그만큼 늘리는 절차입니다. 예를 들어 액면가 500원인 주식을 5대1로 분할하면 액면가는 100원이 되고, 주식 수는 5배로 늘어납니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">주식 수만 늘어날 뿐 회사가 가진 자산이나 시가총액은 액면분할 전후로 그대로입니다.</span> 1주당 가격만 낮아져 소액 투자자의 접근성이 좋아지고 거래량이 늘어나는 효과를 기대할 수 있어, 상장기업이 자주 활용하는 절차입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">액면분할을 하면 왜 거래가 멈추나요</h2>

<p>기존 주권(옛 액면가 기준)을 회수하고 새 액면가로 바뀐 신주권을 새로 발행해서 상장해야 하기 때문입니다. 이 교체 작업이 끝나기 전까지는 어느 시점의 주식이 진짜 내 주식인지 시스템상 확정할 수 없어, <b>한국거래소가 그 기간 동안 매매 자체를 정지</b>시킵니다.</p>

<p>정지 기간에도 <mark>주식을 사고팔 수만 없을 뿐, 보유하고 있던 주식과 그 권리(배당 등)는 그대로 유지</mark>됩니다. 정지 기간이 끝나고 신주가 변경상장되면 늘어난 주식 수만큼 계좌에 자동으로 반영되고, 다시 거래가 가능해집니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">매매정지 기간은 실제로 며칠인가요</h2>

<p><b>매매정지 기간은 분할기준일 1매매거래일 전부터 변경상장일 전일까지입니다.</b> 한국거래소가 발간한 코스닥시장 공시·상장관리해설서에 명시된 기준이며, 근거 규정은 코스닥시장업무규정 제25조와 그 시행세칙 제30조입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">종목</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">분할 비율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">매매정지 시작</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">변경상장(거래재개)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">정지 기간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">와이씨켐</td>
      <td style="border:1px solid #ddd;padding:8px;">2대1 (1,000원→500원)</td>
      <td style="border:1px solid #ddd;padding:8px;">2026-04-10</td>
      <td style="border:1px solid #ddd;padding:8px;">2026-04-29</td>
      <td style="border:1px solid #ddd;padding:8px;">19일</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">동일기연</td>
      <td style="border:1px solid #ddd;padding:8px;">5대1 (500원→100원)</td>
      <td style="border:1px solid #ddd;padding:8px;">2026-06-24</td>
      <td style="border:1px solid #ddd;padding:8px;">2026-07-13</td>
      <td style="border:1px solid #ddd;padding:8px;">19일</td>
    </tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>지금도 같은 규정이 적용되고 있습니다</b>
  <p style="margin:8px 0 0 0;">이 글을 쓰는 시점(2026-09-17) 기준, 대림제지도 같은 사유로 2026-09-18부터 매매정지에 들어갈 예정입니다. 특정 시기에만 있었던 규정이 아니라 지금도 동일하게 적용되는 절차입니다.</p>
</div>

<p>두 사례 모두 <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">19일이라는 같은 정지 기간</span>이 나온 것은 분할 비율(2대1이든 5대1이든)과 무관하게, 정지 기간이 "구주권 회수 → 신주권 발행 → 변경상장"이라는 행정 절차에 걸리는 시간이라 대체로 비슷하기 때문입니다. 다만 회사마다 며칠씩 차이가 날 수 있으므로, 보유 종목의 정확한 일정은 한국거래소 <a href="https://kind.krx.co.kr/investwarn/tradinghaltissue.do?method=searchTradingHaltIssueMain" target="_blank" rel="noopener">KIND 매매거래정지 공시</a>에서 종목명으로 검색해 확인하는 것이 정확합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">액면분할은 어떤 순서로 진행되나요</h2>

<ol style="line-height:1.9;">
  <li><b>이사회 결의 및 공시</b> — 액면분할 결정 사실과 분할 비율을 공시합니다.</li>
  <li><b>주주총회 결의</b> — 정관 변경(액면가 변경)이 필요해 주주총회 특별결의를 거칩니다.</li>
  <li><b>구주권 제출 공고</b> — 기존 주주에게 옛 주권을 제출하도록 일정 기간 공고합니다.</li>
  <li><b>매매거래정지</b> — 분할기준일 1매매거래일 전부터 거래가 멈춥니다.</li>
  <li><b>신주권 발행 및 변경상장</b> — 새 액면가의 신주권이 발행·상장되며 거래가 재개됩니다.</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">액면분할과 무상증자는 뭐가 다른가요</h2>

<p>둘 다 "주식 수가 늘어난다"는 결과만 보면 비슷해 보이지만 늘어나는 방식이 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">액면분할</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">무상증자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주식 수 증가 방식</td>
      <td style="border:1px solid #ddd;padding:8px;">1주를 여러 주로 쪼갬</td>
      <td style="border:1px solid #ddd;padding:8px;">회사가 새 주식을 무료로 나눠줌</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">자본금 변화</td>
      <td style="border:1px solid #ddd;padding:8px;">변화 없음</td>
      <td style="border:1px solid #ddd;padding:8px;">잉여금이 자본금으로 이동해 늘어남</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">거래정지 여부</td>
      <td style="border:1px solid #ddd;padding:8px;">발생함(신주상장까지)</td>
      <td style="border:1px solid #ddd;padding:8px;">권리락만 발생, 거래정지는 없음</td>
    </tr>
  </tbody>
</table>

<p>즉 액면분할은 기존 자산을 잘게 쪼개는 것이고, 무상증자는 회사가 쌓아둔 잉여금을 주식으로 바꿔 추가로 나눠주는 것입니다. 그래서 액면분할에만 신주권 교체를 위한 매매정지가 따라붙습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면분할이란 정확히 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">주식 1주의 액면가를 낮추고 그 비율만큼 발행주식수를 늘리는 절차입니다. 회사의 자산이나 시가총액은 바뀌지 않고 1주당 가격만 낮아집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면분할을 하면 왜 거래가 정지되나요</summary>
  <p style="margin:10px 0 0 0;">기존 주권을 회수하고 새 액면가의 신주권을 발행해 다시 상장해야 하기 때문입니다. 이 교체 절차가 끝날 때까지 한국거래소가 매매를 정지시킵니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">매매정지 기간은 정확히 언제부터 언제까지인가요</summary>
  <p style="margin:10px 0 0 0;">분할기준일 1매매거래일 전부터 변경상장일 전일까지입니다. 2026년 와이씨켐·동일기연 사례 모두 19일이었습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">매매정지 기간에 보유 주식은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">사고팔 수만 없을 뿐 보유 자체는 그대로 유지됩니다. 정지가 끝나면 늘어난 주식 수만큼 계좌에 자동으로 반영되고 거래가 재개됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면분할과 무상증자는 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">액면분할은 기존 주식을 잘게 쪼개는 것이라 자본금 변화가 없고 거래정지가 발생합니다. 무상증자는 잉여금을 자본금으로 옮겨 새 주식을 나눠주는 것이라 자본금이 늘고 거래정지 없이 권리락만 발생합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면분할하면 주가가 무조건 오르나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 1주당 가격이 낮아져 접근성이 좋아지는 효과는 있지만, 회사의 실적이나 가치가 바뀌는 것은 아니라서 분할 이후 주가가 오르지 않거나 하락하는 경우도 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://kind.krx.co.kr/investwarn/tradinghaltissue.do?method=searchTradingHaltIssueMain" target="_blank" rel="noopener">한국거래소 KIND</a> - 매매거래정지 공시(코스닥시장업무규정 제25조·시행세칙 제30조 근거, 자동화 세션에서는 접속이 막혀 직접 확인하지 못함)</li>
    <li><a href="https://kind.krx.co.kr/external/dst/reference/11499/(%EA%B3%B5%EC%A7%80)25%EB%85%84%EC%BD%94%EC%8A%A4%EB%8B%A5%EC%8B%9C%EC%9E%A5%EA%B3%B5%EC%8B%9C%EC%83%81%EC%9E%A5%EA%B4%80%EB%A6%AC%ED%95%B4%EC%84%A4%EC%84%9C.pdf" target="_blank" rel="noopener">한국거래소 코스닥시장 공시·상장관리해설서</a> - 매매거래정지 기간 정의(분할기준일 1매매거래일 전~변경상장일 전일)</li>
    <li><a href="https://www.digitaltoday.co.kr/disclosure/articleView.html?idxno=700808" target="_blank" rel="noopener">디지털투데이</a> - 대림제지 주식분할 매매거래정지 공시 보도(2026-09-17)</li>
  </ul>
  기준일: 2026-09-17(WebSearch 확인일). 한국거래소 KIND 원문은 이번 세션 WebFetch가
  차단돼 직접 열람하지 못했고, 근거 규정·정지기간 정의는 한국거래소 공식 발간 해설서,
  실제 사례 수치는 독립 언론 4곳 이상(디지털투데이·데이터투자·딜사이트·블로터·
  톱스타뉴스)의 보도가 일치하는 것으로 교차검증했습니다.
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
  "headline": "액면분할 매매정지 기간",
  "description": "액면분할을 하면 실제로 며칠 동안 거래가 정지되는지, 2026년 실제 사례와 근거 규정, 절차 순서를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-17",
  "dateModified": "2026-09-17",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-split-trading-halt"
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
      "name": "액면분할이란 정확히 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "주식 1주의 액면가를 낮추고 그 비율만큼 발행주식수를 늘리는 절차입니다. 회사의 자산이나 시가총액은 바뀌지 않고 1주당 가격만 낮아집니다." }
    },
    {
      "@type": "Question",
      "name": "액면분할을 하면 왜 거래가 정지되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "기존 주권을 회수하고 새 액면가의 신주권을 발행해 다시 상장해야 하기 때문입니다. 이 교체 절차가 끝날 때까지 한국거래소가 매매를 정지시킵니다." }
    },
    {
      "@type": "Question",
      "name": "매매정지 기간은 정확히 언제부터 언제까지인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "분할기준일 1매매거래일 전부터 변경상장일 전일까지입니다. 2026년 와이씨켐·동일기연 사례 모두 19일이었습니다." }
    },
    {
      "@type": "Question",
      "name": "매매정지 기간에 보유 주식은 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "사고팔 수만 없을 뿐 보유 자체는 그대로 유지됩니다. 정지가 끝나면 늘어난 주식 수만큼 계좌에 자동으로 반영되고 거래가 재개됩니다." }
    },
    {
      "@type": "Question",
      "name": "액면분할과 무상증자는 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "액면분할은 기존 주식을 잘게 쪼개는 것이라 자본금 변화가 없고 거래정지가 발생합니다. 무상증자는 잉여금을 자본금으로 옮겨 새 주식을 나눠주는 것이라 자본금이 늘고 거래정지 없이 권리락만 발생합니다." }
    },
    {
      "@type": "Question",
      "name": "액면분할하면 주가가 무조건 오르나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 1주당 가격이 낮아져 접근성이 좋아지는 효과는 있지만, 회사의 실적이나 가치가 바뀌는 것은 아니라서 분할 이후 주가가 오르지 않거나 하락하는 경우도 있습니다." }
    }
  ]
}
</script>
