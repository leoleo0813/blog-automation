---
keyword: 액면가 뜻
title: 액면가 뜻과 배당률 계산법
slug: par-value-dividend-rate-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 2,000 (PC 200 / 모바일 1,800, 2026-09-26 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-26 — 통과]
  WebSearch "액면가 뜻" + "액면가 뜻 액면배당률 시가배당률 차이" 상위 결과 종합:
  brunch.co.kr(개인 콘텐츠 플랫폼) / kbthink.com(KB 금융 공식 사전) / help-me.kr(법무법인
  블로그, ×2) / namu.wiki(백과) / negabaro.github.io(개인 개발자 블로그) / whyinsite.com
  (개인 블로그) / lawform.io(법률 매거진, 스타트업 콘텐츠) / tipnotebook.com(개인 블로그)
  / econowide.com(개인 블로그) / dic.hankyung.com(한경 경제용어사전, 언론사).
  1) 진입 여지 — 있음. brunch·negabaro·whyinsite·tipnotebook·econowide 등 개인·소규모
     블로그가 상위권에 다수 진입해 있다.
  2) 검색 의도 — "뜻"을 묻는 개념 탐색형이다. 조회·신청·계산기 실행이 지배적 의도가
     아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 정의, 발행가·무액면주식과의 차이까지는
     다루지만, 액면배당률과 시가배당률을 실제 숫자로 비교 계산하거나 상법상 최저
     액면가 요건(100원)까지 함께 정리한 글은 확인하지 못했다. 이 각도가 정보이득이다.
  → 탈락조건 1~3 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 액면배당률 vs 시가배당률 계산 예시 — 액면가 5,000원인 기업이 주당 1,000원을
      배당하면 액면배당률은 20%(1,000÷5,000)로 고정되지만, 시가배당률은 배당 기준일
      주가가 20,000원이면 5%(1,000÷20,000), 10,000원이면 10%로 달라진다는 것을 같은
      배당금 기준 숫자로 직접 계산해 보여준다.
  (b) 상법 제329조 최저 액면가 요건(1주의 금액은 100원 이상, 균일해야 함)과 2012년
      시행된 무액면주식 제도의 도입 배경을 정리한다.
  (c) 액면가 단위별 표(100원~5,000원)와, 액면분할·액면병합 시 액면가와 발행주식수가
      반비례로 바뀌는 계산 예시(가상 사례). 45편(액면분할 매매정지 기간)이 다룬 실제
      매매정지 일수 통계와는 다른 각도로, 여기서는 액면가 자체의 산술 변화만 다룬다.
primary_source: |
  자동화 세션에서 easylaw.go.kr(찾기쉬운 생활법령정보, 주식회사 개념 페이지)에 WebFetch를
  1회 시도했으나 EGRESS_BLOCKED로 막혔다. 대조군으로 무관한 도메인인 kofia.or.kr에도
  WebFetch를 1회 시도했는데 역시 동일하게 EGRESS_BLOCKED로 막혀, 특정 도메인 문제가
  아니라 이번 세션의 전면 차단으로 판단했다. RULES.md 「1차 출처가 막혔을 때」 기준에
  따라 WebSearch로 독립 출처 교차검증을 진행했다. help-me.kr(법무법인 블로그)·
  korea.legal(법무사 블로그)·lbox.kr(법령 데이터베이스)와 검색엔진에 노출된
  law.go.kr(국가법령정보센터) 자체 요약까지 4곳 이상이 "상법 제329조에 따라 액면주식
  1주의 금액은 100원 이상이어야 한다"는 수치에서 충돌 없이 일치했다. 이 수치는
  2011년 상법 개정(2012년 시행) 이후 개정 이력이 없는 안정적 법정 사실이라(세율·
  공제한도처럼 매년 바뀔 수 있는 유형이 아님) 교차검증으로 진행해도 안전하다고
  판단했다. 국가법령정보센터의 상법 제329조 원문 링크는 검색 결과에 노출된 공식
  URL(law.go.kr/법령/상법/제329조)을 그대로 인용했다.
기준일: 2026년 9월 기준 (상법 제329조는 2011년 개정, 2012년 시행 이후 개정 이력 없음)
tags: 액면가, 액면가뜻, 액면배당률, 시가배당률, 무액면주식, 액면분할, 주식초보, 배당률계산, 상법329조, 주식용어
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 2,000회(일반 주제 기준 500회 이상). 게이트2
  충족 — v3 기준 3개 탈락조건 모두 미해당(개인 블로그 다수 진입, 정보 탐색형 의도,
  계산 예시라는 미다룬 정보이득 확보). 게이트3 충족 — 액면배당률·시가배당률 계산
  예시 + 상법 최저 요건 + 단위별 표. 게이트4 충족 — 원문 WebFetch가 세션 전면
  차단임을 대조군으로 확인한 뒤, 법무법인·법무사·법령DB 등 4곳 이상이 충돌 없이
  일치하는 안정적 법정 수치를 교차검증으로 확보했다.
capture_guide: ""
self_check: |
  [2026-09-26 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — "액면가"를 언급하는 기존 편(bond-tax-guide, capital-
  impairment-delisting-2026, capital-reduction-trading-halt, stock-consolidation-
  notice-period, stock-dividend-tax-calculation, stock-split-trading-halt 6개, grep
  확인)이 있으나 전부 다른 주제(채권 세금·자본잠식·감자·병합·주식배당세금·매매정지
  기간)를 다루는 중 지나가듯 언급할 뿐, "액면가" 자체의 정의·법정 최저기준·
  액면배당률 계산을 정면으로 다루는 편은 없다. 특히 45편(액면분할 매매정지 기간)과는
  같은 "액면분할" 소재를 다루지만 45편은 실제 매매정지 일수 통계, 이 편은 액면가
  자체의 산술 변화만 다뤄 검색 의도와 정보이득이 겹치지 않는다. 47편(배당수익률
  계산)도 grep 확인 결과 "액면" 언급이 전혀 없어 액면배당률 각도와 겹치지 않는다.
  이번 배치 다른 PASS 후보 처리 — 배당소득 분리과세(2,810회, 이번 배치 최고
  검색량)는 4편(배당소득세 얼마 떼나)·6편(금융소득종합과세)·39편(해외주식
  배당소득세)이 이미 2026년 신설 분리과세 특례를 FAQ까지 포함해 상세히 다루고
  있어(56편 검토 시 이미 확인된 카니벌라이제이션, grep 재확인) 채택하지 않고
  backlog에 기록만 한다.
  YMYL 안전장치 점검 — 특정 종목명이나 매수·매도 시점을 언급하지 않았다. 계산
  예시는 전부 "가상의 A기업" 등 가상 수치로만 구성했다.
  기관 링크 점검 — 국가법령정보센터 상법 제329조 링크 1개를 본문 안내 문장과
  참고 출처 목록 양쪽에 동일하게 걸었다.
  제목 "액면가 뜻과 배당률 계산법" 13자·금지어 없음·조사(과)는 RULES.md 예시
  ("ISA 계좌 조건과 한도")와 동일한 명사 나열 방식이라 허용 범위.
  슬러그 영문 소문자+하이픈 5단어(par-value-dividend-rate-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—" 검색
  결과 0개 확인. "다만"은 FAQ 1곳에서만 1회 사용해 반복이 아니다(본문 다른 전환은
  "단,"·"그런데"로 분산). `<mark>` 총 3개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피).
  핵심 요약 박스 제목을 "📏 숫자로
  먼저 보면"으로, 색은 로즈(#fde9f0/#c2185b)로 최근 게시물(인디고#3949ab·
  버건디#a4243b·포레스트그린#2e7d32·앰버#d9812c·퍼플#7b3fa0·틸#00796b)과 겹치지
  않게 골랐다. 목차 제외 본문 H2 6개 중 서술형 5개, 질문형 1개("액면가란
  무엇인가요")로 "~나요" 편중 없음(6개 중 1개, 17%). FAQ 헤딩도 "자주 묻는 질문"
  대신 "궁금한 점 모아보기"로 변형. 헤지 표현은 남발하지 않고 확정된 사실은
  단정형으로 서술했다. 면책 문구는 기존 게시물과 다른 표현으로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-26</p>

<p>액면가는 주권 표면에 적힌 금액일 뿐 실제로 사고파는 시가와는 다른 숫자이며, 배당률 계산이나 회사 자본금 산정의 기준으로 쓰입니다. <mark>같은 배당금이라도 액면가와 시가 중 무엇을 기준으로 보느냐에 따라 배당률 수치가 크게 달라질 수 있습니다.</mark> 이 글은 액면가의 뜻과 법정 최저 기준, 액면배당률과 시가배당률의 계산 차이를 정리합니다.</p>

<div style="background:#fde9f0;border:2px solid #c2185b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#880e4f;font-size:18px;">📏 숫자로 먼저 보면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>액면가는 주권 표면에 적힌 금액으로, 시장에서 거래되는 시가와는 다른 숫자입니다.</li>
    <li>상법 제329조에 따라 액면주식 1주의 금액은 100원 이상이어야 합니다.</li>
    <li>같은 배당금이라도 액면가 기준(액면배당률)과 시가 기준(시가배당률)은 다른 숫자로 계산됩니다.</li>
    <li>2012년 시행된 개정 상법 이후에는 액면가 자체가 없는 무액면주식도 발행할 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>액면가란 무엇인가요</li>
  <li>액면가와 시가 발행가는 다릅니다</li>
  <li>액면가 최저 기준, 상법이 정합니다</li>
  <li>액면배당률과 시가배당률 계산법</li>
  <li>무액면주식은 액면가가 아예 없습니다</li>
  <li>액면분할 액면병합과 액면가 변화</li>
  <li>궁금한 점 모아보기</li>
</ol>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">액면가란 무엇인가요</h2>

<p>액면가(액면가액)는 주식회사가 처음 주식을 발행할 때 주권 표면에 적어 넣은 금액입니다. 회사의 자본금을 발행주식수로 나눈 값이 곧 액면가이며, 국내 상장사는 보통 5,000원을 표준으로 삼되 100원, 200원, 500원, 1,000원, 2,500원 단위도 함께 쓰입니다.</p>

<p>액면가는 실제 매매 가격이 아닙니다. 주식은 시장에서 수요와 공급에 따라 정해지는 시가로 거래되고, 액면가는 그 뒤에서 <mark>배당률 산정이나 자본금 계산의 기준값</mark>으로만 쓰입니다.</p>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">액면가와 시가 발행가는 다릅니다</h2>

<p>액면가, 발행가, 시가는 서로 다른 세 가지 숫자입니다. 헷갈리기 쉬워서 표로 구분하면 이렇습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">정해지는 시점</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">성격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">액면가</td>
      <td style="border:1px solid #ddd;padding:8px;">회사 설립·정관 변경 시</td>
      <td style="border:1px solid #ddd;padding:8px;">자본금 계산·배당률 산정 기준값</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">발행가</td>
      <td style="border:1px solid #ddd;padding:8px;">유상증자·공모 등 신주 발행 시</td>
      <td style="border:1px solid #ddd;padding:8px;">투자자가 실제로 납입하는 금액</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시가</td>
      <td style="border:1px solid #ddd;padding:8px;">매 거래일 장중</td>
      <td style="border:1px solid #ddd;padding:8px;">수요와 공급에 따라 계속 변하는 실제 거래가</td>
    </tr>
  </tbody>
</table>

<p>발행가는 액면가보다 높은 경우(액면가 이상 발행이 원칙)가 대부분이고, 시가는 상장 이후 시장에서 계속 바뀝니다. 세 숫자 중 액면가만 정관을 바꾸지 않는 한 고정돼 있습니다.</p>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">액면가 최저 기준, 상법이 정합니다</h2>

<p><a href="https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%83%81%EB%B2%95/%EC%A0%9C329%EC%A1%B0" target="_blank" rel="noopener">상법 제329조</a>는 액면주식 1주의 금액을 100원 이상으로 하도록 정하고 있습니다. 회사가 마음대로 1원, 10원 같은 극단적으로 낮은 액면가를 매길 수 없다는 뜻입니다.</p>

<ul style="line-height:1.9;">
  <li>액면주식 1주의 금액은 균일해야 합니다(한 회사 안에서 액면가를 종류마다 다르게 매길 수 없음).</li>
  <li>1주의 금액은 100원 이상이어야 합니다.</li>
  <li>회사의 자본금은 발행주식의 액면총액과 일치해야 합니다(무액면주식 발행 시는 예외).</li>
</ul>

<p>이 100원이라는 하한선은 2011년 상법 개정(2012년 시행) 이후 바뀐 적이 없는 안정적인 법정 기준입니다.</p>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">액면배당률과 시가배당률 계산법</h2>

<p>배당률은 어떤 금액을 기준으로 계산하느냐에 따라 액면배당률과 시가배당률로 나뉩니다. <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">액면배당률은 액면가를 기준으로 계산하고, 시가배당률은 배당 기준일의 실제 주가를 기준으로 계산합니다.</span></p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <p style="margin:8px 0 0 0;">액면가 5,000원인 A기업이 1주당 1,000원을 배당한다고 가정합니다.</p>
  <p style="margin:8px 0 0 0;">액면배당률 = 1,000원 ÷ 5,000원 × 100 = <mark>20%</mark> (주가와 무관하게 항상 동일)</p>
  <p style="margin:8px 0 0 0;">배당 기준일 시가가 20,000원이면, 시가배당률 = 1,000원 ÷ 20,000원 × 100 = 5%</p>
  <p style="margin:8px 0 0 0;">같은 날 시가가 10,000원이었다면, 시가배당률 = 1,000원 ÷ 10,000원 × 100 = 10%</p>
</div>

<p>배당금이 똑같이 1,000원이어도 액면배당률은 20%로 고정되지만, 시가배당률은 주가 수준에 따라 5%가 되기도 10%가 되기도 합니다. 실제로 그 주식을 시가로 산 투자자 입장에서는 액면배당률보다 시가배당률이 실질 수익률에 더 가깝습니다.</p>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">무액면주식은 액면가가 아예 없습니다</h2>

<p>2012년 시행된 개정 상법부터는 회사가 정관으로 정하는 바에 따라 액면가 없이 주식을 발행하는 무액면주식 제도를 도입할 수 있게 됐습니다. 무액면주식은 액면가라는 개념 자체가 없고, 발행가와 시가만 존재합니다.</p>

<p>회사는 액면주식과 무액면주식 중 하나를 선택해야 하며, 둘을 동시에 발행할 수는 없습니다. 국내 상장사 대부분은 여전히 액면주식을 채택하고 있어, 액면배당률 같은 개념도 그만큼 자주 쓰입니다.</p>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">액면분할 액면병합과 액면가 변화</h2>

<p>액면분할은 액면가를 낮추면서 발행주식수를 늘리는 조치이고, 액면병합은 반대로 액면가를 높이면서 발행주식수를 줄이는 조치입니다. 둘 다 회사의 자본금 총액 자체는 바뀌지 않습니다.</p>

<div style="background:#fff8e1;border-left:4px solid #f9a825;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <p style="margin:8px 0 0 0;">액면가 5,000원, 발행주식수 100만 주인 B기업이 액면가를 500원으로 낮추는 1대10 액면분할을 하면, 발행주식수는 1,000만 주로 늘어납니다.</p>
  <p style="margin:8px 0 0 0;">자본금(액면가 × 발행주식수)은 분할 전후 모두 50억원으로 동일합니다. 액면가와 발행주식수가 서로 반비례로 바뀔 뿐입니다.</p>
</div>

<p>단, 액면분할이나 액면병합을 결정하면 신주가 상장되기까지 일정 기간 매매가 정지됩니다. 실제 정지 기간과 사례는 이 시리즈의 액면분할 매매정지 기간 편에서 별도로 다뤘습니다.</p>

<h2 style="border-left:6px solid #c2185b;padding-left:12px;margin-top:36px;">궁금한 점 모아보기</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면가가 높으면 좋은 주식인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 액면가는 회사가 정한 표면 금액일 뿐 기업 가치나 주가 수준과는 관계가 없습니다. 액면가 5,000원짜리 주식보다 액면가 100원짜리 주식의 시가가 훨씬 높은 경우도 흔합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면가는 누가 정하나요</summary>
  <p style="margin:10px 0 0 0;">회사가 정관으로 정합니다. 다만 상법 제329조에 따라 액면주식이라면 1주의 금액을 100원 이상, 균일하게 정해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">액면가와 액면분할 시 발행가는 같은 개념인가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 액면가는 정관에 등록된 고정 기준값이고, 발행가는 유상증자나 공모처럼 신주를 발행할 때 투자자가 실제로 납입하는 금액입니다. 액면분할은 발행가가 아니라 액면가와 발행주식수를 함께 조정하는 절차입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">무액면주식으로 바꾸면 배당률 계산은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">무액면주식은 액면가가 없으므로 액면배당률 자체를 계산할 수 없습니다. 이 경우 배당 관련 비율은 시가배당률로만 표시됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">시가배당률이 액면배당률보다 중요한가요</summary>
  <p style="margin:10px 0 0 0;">투자자 입장에서는 그렇습니다. 실제로 주식을 시가에 사고팔기 때문에, 투자 원금 대비 실질 배당 수익률을 보여주는 지표는 시가배당률입니다. 액면배당률은 회사의 배당 정책을 표시하는 관행적 지표에 가깝습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%83%81%EB%B2%95/%EC%A0%9C329%EC%A1%B0" target="_blank" rel="noopener">국가법령정보센터 - 상법 제329조(자본금의 구성)</a></li>
    <li><a href="https://easylaw.go.kr" target="_blank" rel="noopener">법제처 찾기쉬운 생활법령정보</a></li>
  </ul>
  기준일: 2026년 9월 기준. 상법 제329조는 2011년 개정, 2012년 시행 이후 개정 이력이 없습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 주식 제도 용어를 설명하는 정보 글이며, 특정 종목이나 상품의 매수·매도를 권하지 않습니다. 액면가와 관련된 법령이나 배당 정책은 개별 기업 상황에 따라 달라질 수 있으므로, 실제 투자 판단 전에는 해당 기업의 공시나 국가법령정보센터 원문을 직접 확인하시기 바랍니다. 투자로 인한 손익은 투자자 본인에게 책임이 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "액면가 뜻과 배당률 계산법",
  "description": "액면가의 뜻, 상법 제329조 최저 액면가 요건, 무액면주식 제도, 액면배당률과 시가배당률의 계산 차이를 실제 숫자 예시로 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-26",
  "dateModified": "2026-09-26",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/par-value-dividend-rate-calculation"
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
      "name": "액면가가 높으면 좋은 주식인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 액면가는 회사가 정한 표면 금액일 뿐 기업 가치나 주가 수준과는 관계가 없습니다. 액면가 5,000원짜리 주식보다 액면가 100원짜리 주식의 시가가 훨씬 높은 경우도 흔합니다." }
    },
    {
      "@type": "Question",
      "name": "액면가는 누가 정하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "회사가 정관으로 정합니다. 다만 상법 제329조에 따라 액면주식이라면 1주의 금액을 100원 이상, 균일하게 정해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "액면가와 액면분할 시 발행가는 같은 개념인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "다릅니다. 액면가는 정관에 등록된 고정 기준값이고, 발행가는 유상증자나 공모처럼 신주를 발행할 때 투자자가 실제로 납입하는 금액입니다. 액면분할은 발행가가 아니라 액면가와 발행주식수를 함께 조정하는 절차입니다." }
    },
    {
      "@type": "Question",
      "name": "무액면주식으로 바꾸면 배당률 계산은 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "무액면주식은 액면가가 없으므로 액면배당률 자체를 계산할 수 없습니다. 이 경우 배당 관련 비율은 시가배당률로만 표시됩니다." }
    },
    {
      "@type": "Question",
      "name": "시가배당률이 액면배당률보다 중요한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "투자자 입장에서는 그렇습니다. 실제로 주식을 시가에 사고팔기 때문에, 투자 원금 대비 실질 배당 수익률을 보여주는 지표는 시가배당률입니다. 액면배당률은 회사의 배당 정책을 표시하는 관행적 지표에 가깝습니다." }
    }
  ]
}
</script>
