---
keyword: 이월과세
title: 이월과세 적용 기간과 계산 방법
slug: carryover-taxation-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 420 (PC 150 / 모바일 270)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-25 — 통과]
  WebSearch "이월과세" 상위 9개: taxnet.co.kr(세무 전문 매체 칼럼) /
  findsemusa.com(개인·소규모 세무 정보 플랫폼) / kci.go.kr(학술논문 포털,
  준정부) / call.nts.go.kr(국세청 Q&A, 공식) / kin.eduwill.net(공인중개사
  수험 커뮤니티, 개인 게시판) / intn.co.kr(일간NTN, 언론사) /
  taxoffice.co.kr(세림세무법인, 소규모 세무법인 콘텐츠, ×2) /
  ksmac.or.kr(세무 관련 협회 성격, 준정부).
  1) 진입 여지 — 있음. findsemusa.com·kin.eduwill.net·taxoffice.co.kr까지
     개인·소규모 콘텐츠가 다수 상위권에 있다.
  2) 검색 의도 — 제도 자체를 묻는 개념+절차 탐색형이다. 조회·계산기 실행
     페이지는 상위에 없다.
  3) 답 완결 여부 — 아니다. 상위 결과는 거의 전부 부동산 증여 후 재양도
     사례(10년 규정) 중심이고, 2025년 세법 개정으로 주식이 새로 이월과세
     대상에 포함되면서 기간이 1년으로 별도 적용된다는 점, 그리고 국내
     상장주식 소액주주는 애초에 양도소득세 비과세라 이월과세와 무관하다는
     구분까지 계산 예시와 함께 다룬 글은 찾지 못했다. 이 각도가 정보이득
     포인트다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 원 단위 계산 예시 — 아버지가 2천만원에 산 비상장주식을 아들에게
      증여(증여 당시 시가 8천만원)하고, 아들이 8개월 만에 9천만원에 매도한
      가상 사례로 "이월과세 적용 시 양도차익 7천만원" vs "1년을 넘겨
      팔았다면 양도차익 1천만원"을 나란히 계산해 6천만원 차이를 보여준다.
      상위 검색 결과 중 주식을 소재로 한 계산 예시는 찾지 못했다.
  (b) 부동산(10년) vs 주식(1년) 비교표 — 같은 이월과세 규정인데도 자산
      종류에 따라 적용 기간이 다르다는 점을 표로 정리했다. 상위 결과는
      대부분 부동산 사례만 다뤄 이 대비가 없다.
  (c) "국내 상장주식 소액주주는 대부분 무관하다"는 명확화 — 상위 글들이
      "주식도 해당된다"고만 언급해 소액 개인 투자자에게 불필요한 불안을
      줄 수 있는데, 국내 상장주식을 장내에서 거래하는 소액주주는 애초에
      양도소득세 비과세 대상이라 이월과세를 적용할 세금 자체가 없다는
      점을 한국경제·국세청 출처로 확인해 명시했다.
primary_source: |
  law.go.kr(소득세법 제97조의2 조문 원문)·nts.go.kr에 WebFetch를 각 1회
  시도했으나 둘 다 EGRESS_BLOCKED로 막혔고, 민간 도메인(intn.co.kr,
  heumtax.com)도 같은 세션에서 막혀 이번 세션은 WebFetch가 전면 차단된
  상태로 판단했다(대조군 확인 포함, 상세 기록 sources/
  carryover-taxation-stock-cross-verification.md).
  RULES.md 「1차 출처가 막혔을 때」 기준에 따라 WebSearch로 독립 출처
  8곳 이상을 교차확인했다: 언론사 2곳(일간NTN·한국경제), 법무법인 2곳
  (신영·김앤장), 회계법인 1곳(삼일PwC), 세무법인 콘텐츠 2곳(흠택스·
  세림세무법인), 대형 금융사(KB증권) 콘텐츠 2편. 핵심 수치 — 2025-01-01
  이후 증여분부터 주식(상장·비상장·해외주식)이 이월과세 대상에 신설
  편입, 적용 기간은 증여일로부터 1년 이내 양도, 배우자·직계존비속 증여자가
  매도 전 사망하면 이월과세 배제 — 가 출처 간 충돌 없이 일치했다. 단순
  사전적 정의가 아니라 2025년 세법 개정이라는 검증 가능한 사실관계이고,
  RULES.md가 예시로 든 16·17·18편(제도 변경·기간 수치)과 같은 성격이라
  판단해 교차검증으로 진행했다. 소득세법 제97조의2 조문 원문 자체는
  이번에도 확보하지 못해, 사람이 law.go.kr에서 직접 확인하면 더 확실하다.
기준일: 2026년 9월 기준 (2025-01-01 이후 증여분부터 시행 중인 규정)
tags: 이월과세, 이월과세뜻, 주식증여세, 증여주식양도소득세, 소득세법97조의2, 비상장주식증여, 해외주식증여, 양도소득세이월과세, 주식초보, 세금정보
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 420회(세부·제도 기준 100 이상).
  게이트2 충족 — v3 기준 3개 탈락 조건 모두 미해당, 주식 특화 각도로
  정보이득 확보. 게이트3 충족 — 계산 예시·비교표·소액주주 무관 명확화
  3종. 게이트4 충족 — law.go.kr·nts.go.kr WebFetch 1회 시도 후 세션
  전면 차단 확인, WebSearch 8개 이상 독립 출처(언론사·법무법인·회계법인
  포함) 교차검증으로 근거 확보, 충돌 없음.
capture_guide: ""
self_check: |
  [2026-09-25 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — stock_drafts/*.md 82개 전체를 grep, "이월과세"
  또는 "97조의2"를 다룬 기존 편 없음 확인. 11편(주식 증여세)은 증여세
  계산 자체(평가기준일·공제한도)만 다루고 증여 후 재양도 시 양도소득세
  특례는 다루지 않아 겹치지 않는다.
  이번 배치에서 함께 확인한 신규 후보(기관 순매수 확인 방법 20회·코스피
  선물 뜻 140회·ETF 총보수 순보수 차이 20회·증권사 예탁금 이용료율
  20회·코스피 코스닥 시가총액 순위 확인 방법 20회·주식 매매수수료
  부가가치세 20회·배당소득세 지방소득세 계산법 20회)는 전부 게이트1(세부
  기준 월100/일반 기준 월500) 미달로 탈락 — backlog.failed_gate1에 기록.
  YMYL 안전장치 점검 — 특정 종목·상품을 추천하지 않았다. 계산 예시는
  "가상의 부모-자녀" 관계로 실제 인물·회사명을 쓰지 않았다. 매도 시점을
  앞당기거나 늦추라는 지시 없이 "이월과세가 적용되는 요건"만 사실대로
  서술했고, 절세 전략처럼 읽히지 않도록 6번째 H2를 "예외 요건"으로
  제목을 잡았다.
  기관 링크 점검 — 국세청 링크(nts.go.kr 주식등 양도소득세 페이지, RULES.md
  표 등재분) 1회, 법제처/국가법령정보센터 링크(law.go.kr) 1회를 본문
  안내 문장 자리에 배치, 하단 참고 출처 목록도 전부 링크 처리.
  제목 "이월과세 적용 기간과 계산 방법" 17자·금지어 없음·조사/접속사 없음.
  슬러그 영문 소문자+하이픈 3단어(carryover-taxation-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—"
  0개 확인. "다만"은 0회, 전환은 "그런데"·"단,"·"반대로"로 분산. `<mark>`
  총 4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심 요약 박스 제목을
  "⏳ 핵심만 짚으면"으로, 색은 퍼플(#f5eefc/#7b3fa0)로 최근 게시물(틸
  #00796b·슬레이트블루#3949ab·버건디#a4243b·포레스트그린#2e7d32·앰버
  #d9812c)과 겹치지 않게 골랐다. 목차 제외 본문 H2 6개 중 서술형 4개,
  질문형 2개("주식도 이월과세 대상에 포함되나요"·"부동산 이월과세와
  무엇이 다른가요")로 "~나요" 편중 없음(6개 중 2개, 33%). FAQ 헤딩도
  "자주 묻는 질문" 대신 "헷갈리는 부분 정리"로 변형. 헤지 표현은 남발
  없이 확정된 사실은 단정문으로 썼다. 면책 문구는 기존 게시물과 다른
  표현으로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-25</p>

<p>이월과세는 배우자나 부모·자녀에게 증여받은 주식을 짧은 기간 안에 팔면, 증여받은 사람이 아니라 <mark>원래 증여해 준 사람이 산 가격</mark>을 기준으로 양도소득세를 계산하는 특례입니다. 2025년부터 이 규정에 주식이 새로 포함됐는데, 부동산과 적용 기간이 달라 헷갈리기 쉽습니다. 이 글은 이월과세의 적용 기간과 실제 계산 방법을 정리합니다.</p>

<div style="background:#f5eefc;border:2px solid #7b3fa0;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4a1a6b;font-size:18px;">⏳ 핵심만 짚으면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>2025년 1월 1일 이후 증여받은 주식부터, 증여일로부터 1년 이내 팔면 이월과세가 적용됩니다.</li>
    <li>이월과세가 적용되면 증여받은 사람의 취득가액이 아니라 증여자의 원래 취득가액으로 양도차익을 계산합니다.</li>
    <li>부동산 등은 기존부터 10년 기준이 적용되며, 주식만 1년이라는 점이 다릅니다.</li>
    <li>국내 상장주식을 장내에서 거래하는 소액주주는 애초에 양도소득세가 없어 대부분 해당하지 않습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>이월과세의 기본 개념</li>
  <li>주식도 이월과세 대상에 포함되나요</li>
  <li>적용 기간 1년의 기산일 계산법</li>
  <li>실제 계산 예시로 보는 이월과세</li>
  <li>부동산 이월과세와 무엇이 다른가요</li>
  <li>이월과세가 적용되지 않는 경우</li>
  <li>헷갈리는 부분 정리</li>
</ol>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">이월과세의 기본 개념</h2>

<p>이월과세(소득세법 제97조의2)는 배우자나 직계존비속(부모·자녀·조부모 등)에게 자산을 증여받은 사람이 그 자산을 짧은 기간 안에 팔면, 증여받은 날의 가격이 아니라 <mark>증여해 준 사람이 원래 그 자산을 산 가격</mark>을 취득가액으로 삼아 양도소득세를 계산하는 제도입니다.</p>

<p>증여세는 증여받을 때 이미 별도로 계산해 납부합니다. 이월과세는 그 이후 자산을 팔 때 양도소득세를 어떤 가격 기준으로 계산할지를 정하는 특례일 뿐, 증여세 자체를 늘리거나 다시 매기는 규정이 아닙니다.</p>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">주식도 이월과세 대상에 포함되나요</h2>

<p>포함됩니다. 2025년 세법 개정 전까지는 부동산과 일부 회원권 등에만 이월과세가 적용됐고, 주식은 별도의 부당행위계산부인 규정으로 다뤘습니다. 2025년 1월 1일 이후 증여받은 분부터는 상장주식, 비상장주식, 해외주식이 모두 이월과세 적용 대상에 새로 들어왔습니다.</p>

<p>취득가액뿐 아니라 취득시기도 증여자가 원래 그 주식을 산 시점을 기준으로 계산합니다. 증여받은 날짜가 아니라 증여자의 보유 이력을 그대로 이어받는다는 뜻입니다.</p>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">적용 기간 1년의 기산일 계산법</h2>

<p>기산일은 주식을 증여받은 날(수증일)입니다. 그날로부터 1년이 되는 날까지 팔면 이월과세가 적용되고, 그 날짜를 넘겨 팔면 적용되지 않습니다.</p>

<ul style="line-height:1.9;">
  <li>2025년 3월 15일에 증여받았다면, 2026년 3월 15일까지 매도 시 이월과세 대상입니다.</li>
  <li>2026년 3월 16일 이후에 매도하면 이월과세 대상에서 제외됩니다.</li>
  <li>증여받은 날 이후 매도까지 걸린 실제 날짜 수로 따지며, 반대로 1년을 며칠이라도 넘기면 적용되지 않습니다.</li>
</ul>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">실제 계산 예시로 보는 이월과세</h2>

<p>가상의 사례로 계산 방식을 비교해 보겠습니다. 아버지가 5년 전 2천만원에 산 비상장주식을 2025년 3월 아들에게 증여했고, 증여 당시 시가는 8천만원이었습니다(증여세는 이 금액을 기준으로 별도 계산). 아들이 8개월 만인 2025년 11월 9천만원에 매도했다고 가정합니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례, 1년 이내 매도 → 이월과세 적용)</b>
  <p style="margin:8px 0 0 0;">양도가액 9천만원 − 필요경비(아버지의 취득가액) 2천만원 = 양도차익 <mark>7천만원</mark></p>
  <b style="display:block;margin-top:12px;">만약 같은 가격에 1년을 넘겨 팔았다면 (이월과세 미적용)</b>
  <p style="margin:8px 0 0 0;">양도가액 9천만원 − 필요경비(아들의 취득가액, 증여 당시 가액) 8천만원 = 양도차익 <mark>1천만원</mark></p>
</div>

<p>같은 매도가격이라도 양도차익이 7천만원과 1천만원으로 6천만원 차이가 납니다. 과세표준이 커지면 적용 세율 구간도 함께 올라갈 수 있어, 실제 세금 차이는 이보다 더 벌어질 수 있습니다. 구체적인 세율 구간은 이 시리즈의 다른 주식 양도소득세 관련 글을 참고하시기 바랍니다.</p>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">부동산 이월과세와 무엇이 다른가요</h2>

<p>같은 이월과세 규정이라도 자산 종류에 따라 적용 기간이 다릅니다. 아래 표로 비교합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">부동산·회원권 등</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">주식(상장·비상장·해외)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">적용 기간</td>
      <td style="border:1px solid #ddd;padding:8px;">증여일로부터 10년 이내 양도</td>
      <td style="border:1px solid #ddd;padding:8px;">증여일로부터 1년 이내 양도</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시행 시기</td>
      <td style="border:1px solid #ddd;padding:8px;">기존부터 적용 중인 규정</td>
      <td style="border:1px solid #ddd;padding:8px;">2025년 1월 1일 이후 증여분부터</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">적용 대상 증여자</td>
      <td style="border:1px solid #ddd;padding:8px;">배우자, 직계존비속</td>
      <td style="border:1px solid #ddd;padding:8px;">배우자, 직계존비속</td>
    </tr>
  </tbody>
</table>

<p>반대로 말하면, 부동산은 10년이라는 기간만 생각하고 주식도 똑같이 여유가 있다고 오해하기 쉽습니다. 주식은 기간이 훨씬 짧다는 점을 따로 기억해야 합니다.</p>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">이월과세가 적용되지 않는 경우</h2>

<p>아래 요건에 해당하면 이월과세가 적용되지 않거나, 애초에 적용할 세금 자체가 없습니다.</p>

<ul style="line-height:1.9;">
  <li>증여받은 날로부터 1년을 넘겨 매도하는 경우: 증여받은 사람 본인의 취득가액(증여 당시 가액)을 기준으로 계산합니다.</li>
  <li>매도 전에 증여자인 배우자나 직계존비속이 사망한 경우: 이월과세를 적용하지 않고, 증여 당시 가액을 그대로 취득가액으로 인정합니다.</li>
  <li>국내 상장주식을 장내에서 거래하는 소액주주인 경우: 애초에 양도소득세 과세 대상이 아니므로, 이월과세를 적용할 세금 자체가 없습니다. <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&amp;mi=12274" target="_blank" rel="noopener">국세청 주식등 양도소득세 안내</a>에서 본인이 대주주인지, 장외거래인지부터 확인하는 편이 정확합니다.</li>
</ul>

<h2 style="border-left:6px solid #7b3fa0;padding-left:12px;margin-top:36px;">헷갈리는 부분 정리</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">이월과세를 적용받으면 증여세도 다시 내야 하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 증여세는 증여받을 때 이미 별도로 계산해 납부합니다. 이월과세는 나중에 그 주식을 팔 때 양도소득세를 어떤 가격 기준으로 계산할지 정하는 특례일 뿐입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">1년이 지난 뒤에 팔면 전혀 신경 쓰지 않아도 되나요</summary>
  <p style="margin:10px 0 0 0;">그렇습니다. 증여받은 날로부터 1년을 초과해 보유한 뒤 매도하면 이월과세가 적용되지 않고, 증여받은 사람 본인의 취득가액인 증여 당시 가액을 기준으로 양도소득세를 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비상장주식이나 해외주식도 이월과세 대상인가요</summary>
  <p style="margin:10px 0 0 0;">네. 2025년 1월 1일 이후 증여받은 분부터 상장주식, 비상장주식, 해외주식이 모두 이월과세 적용 대상에 포함됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내 상장주식을 조금 보유한 개인도 이월과세를 걱정해야 하나요</summary>
  <p style="margin:10px 0 0 0;">대부분은 아닙니다. 국내 상장주식을 장내에서 거래하는 소액주주는 애초에 양도소득세 과세 대상이 아니므로, 이월과세를 적용할 세금 자체가 없습니다. 대주주에 해당하거나 장외거래·비상장·해외주식인 경우에만 실제로 문제 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증여자가 매도 전에 사망하면 이월과세는 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">매도 전에 증여자인 배우자나 직계존비속이 사망한 경우에는 이월과세를 적용하지 않고, 증여 당시의 가액을 그대로 취득가액으로 인정합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a>: 소득세법 제97조의2(양도소득의 필요경비 계산 특례)</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&amp;mi=12274" target="_blank" rel="noopener">국세청 - 주식등 양도소득세(세액계산요령)</a></li>
    <li>2025년 세법 개정에 따른 주식 이월과세 신설 편입 내용은 언론 보도(일간NTN)와 법무법인·회계법인 공개 자료를 교차확인해 정리했습니다(상세 기록은 저장소 sources/ 참고).</li>
  </ul>
  <p style="margin:8px 0 0 0;">기준일: 2026년 9월 기준. 2025년 1월 1일 이후 증여받은 분부터 시행 중인 규정입니다.</p>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 세금 제도를 설명하는 정보 글이며, 특정 종목이나 상품의 매수·매도를 권하지 않습니다. 증여·매도 시점을 포함한 투자 판단과 그 결과는 본인 책임이며, 개별 상황에 따라 계산이 달라질 수 있으니 실제 신고 전에는 세무 전문가나 국세청 원문으로 다시 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "이월과세 적용 기간과 계산 방법",
  "description": "2025년부터 주식도 포함된 이월과세(소득세법 97조의2)의 적용 기간, 부동산과의 차이, 원 단위 계산 예시와 예외 요건을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-25",
  "dateModified": "2026-09-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/carryover-taxation-calculation"
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
      "name": "이월과세를 적용받으면 증여세도 다시 내야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 증여세는 증여받을 때 이미 별도로 계산해 납부합니다. 이월과세는 나중에 그 주식을 팔 때 양도소득세를 어떤 가격 기준으로 계산할지 정하는 특례일 뿐입니다." }
    },
    {
      "@type": "Question",
      "name": "1년이 지난 뒤에 팔면 전혀 신경 쓰지 않아도 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "그렇습니다. 증여받은 날로부터 1년을 초과해 보유한 뒤 매도하면 이월과세가 적용되지 않고, 증여받은 사람 본인의 취득가액인 증여 당시 가액을 기준으로 양도소득세를 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "비상장주식이나 해외주식도 이월과세 대상인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 2025년 1월 1일 이후 증여받은 분부터 상장주식, 비상장주식, 해외주식이 모두 이월과세 적용 대상에 포함됩니다." }
    },
    {
      "@type": "Question",
      "name": "국내 상장주식을 조금 보유한 개인도 이월과세를 걱정해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "대부분은 아닙니다. 국내 상장주식을 장내에서 거래하는 소액주주는 애초에 양도소득세 과세 대상이 아니므로, 이월과세를 적용할 세금 자체가 없습니다. 대주주에 해당하거나 장외거래·비상장·해외주식인 경우에만 실제로 문제 됩니다." }
    },
    {
      "@type": "Question",
      "name": "증여자가 매도 전에 사망하면 이월과세는 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "매도 전에 증여자인 배우자나 직계존비속이 사망한 경우에는 이월과세를 적용하지 않고, 증여 당시의 가액을 그대로 취득가액으로 인정합니다." }
    }
  ]
}
</script>
