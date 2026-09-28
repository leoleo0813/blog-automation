---
keyword: 듀레이션 뜻
title: 듀레이션 뜻과 계산 방법
slug: duration-meaning-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1170 (PC 190 / 모바일 980)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-28 — 통과]
  WebSearch "듀레이션 뜻 채권 계산"·"워런트 신주인수권부사채 뜻 개념 정리"(비교
  검색) 상위 결과 종합: brunch.co.kr(개인 블로그) 2건, kbam.co.kr(중소형 자산운용사
  콘텐츠), quarterback.co.kr(자산운용사 블로그), fidelity.co.kr(해외 대형사 국문
  페이지), iprovest.com(교보증권 채권교실), bondweb.co.kr(민간 채권정보 사이트),
  jaenung.net(개인 재테크 블로그).
  1) 진입 여지 — 있음. brunch.co.kr 2건, jaenung.net 등 개인 콘텐츠가 상위 9개 중
     3개 이상을 차지한다.
  2) 검색 의도 — "뜻"과 "계산"을 함께 묻는 개념+계산 탐색형이다. 조회·계산기 실행이
     지배적 의도가 아니다(참고로 같은 세션에서 워런트 뜻을 먼저 검토했으나 그
     상위 결과는 한국은행·KDI 등 교육기관의 설명이 이미 상당히 완결적이라 정보이득
     확보가 어려워 보여 이번 편 후보에서 제외하고 듀레이션으로 전환했다).
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 듀레이션의 정의(평균 회수기간)와
     맥컬리 듀레이션 공식까지는 다루지만, 실제 숫자를 넣어 채권가격까지 끝까지
     계산한 글이나 만기별로 듀레이션이 몇 배 차이 나는지 비교표로 보여준 글은
     확인되지 않았다. 이 두 각도가 정보이득이다.
  → 탈락조건 1~3 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 액면 10,000원·표면금리 4%·만기수익률 5%인 3년 만기 이표채를 가정해 맥컬리
      듀레이션 공식을 현금흐름별로 실제 계산한다: 1년 차 400원·2년 차 400원·3년 차
      10,400원을 각각 할인해 채권가격 9,727.68원을 구하고, 이를 분모로 맥컬리
      듀레이션 2.88년, 수정듀레이션 2.75를 도출한다. 정의만 설명하고 끝나는 상위
      글들과 달리 끝까지 계산 과정을 보여준다.
  (b) 같은 표면금리·수익률 조건에서 만기만 1년/3년/10년으로 바꾼 세 채권의
      맥컬리 듀레이션·수정듀레이션·금리 1%p 상승 시 추정 가격변동률 비교표를
      직접 계산으로 만든다(1년물 -0.95% vs 10년물 -7.96%로 약 8.4배 차이) —
      "듀레이션이 길수록 민감하다"는 말을 구체적 배수로 보여주는 글은 상위
      결과에 없었다.
  (c) 무이표채(액면 10,000원·만기수익률 5%·5년) 예시로 듀레이션이 정확히 만기와
      같은 5.00년이 되는 이유를 계산으로 보여주고, 표면금리가 있는 채권과 대비해
      "표면금리가 낮을수록/없을수록 듀레이션이 길어진다"는 관계를 수치로 설명한다.
primary_source: |
  맥컬리 듀레이션·수정듀레이션 계산식(듀레이션 = Σ(t × 현금흐름의 현재가치) ÷
  채권가격, 수정듀레이션 = 맥컬리 듀레이션 ÷ (1+만기수익률))은 채권 가격결정의
  수학적 정의이며, 별도 기관 확인이 필요한 제도적 수치가 아니다(88편 PBR, 89편
  ROE, 90편 EPS, 93편 PER과 동일한 처리 방식 — 세율·한도처럼 매년 바뀌는 값이
  아니라 계산 공식 자체가 항등식이다). 본문 계산 예시는 전부 가상의 액면가·
  표면금리·수익률을 가정한 것으로 실제 특정 채권의 시세가 아니다.
  "듀레이션을 어디서 확인하는지"에 안내한 금융투자협회 채권정보센터
  (kofiabond.or.kr)는 WebSearch로 해당 사이트가 금융투자협회가 운영하는 채권
  정보 공식 창구임을 확인했으나, 자동화 세션에서 WebFetch를 1회 시도한 결과
  EGRESS_BLOCKED로 막혀 내부 화면 구성까지는 직접 확인하지 못했다(RULES.md에
  기록된 kofia.or.kr 계열 도메인의 알려진 접속 불안정과 같은 증상). 이 링크는
  세율·한도 같은 수치 주장이 아니라 "여기서 채권 정보를 찾아보라"는 안내용
  포인터이므로, RULES.md 「1차 출처가 막혔을 때」 기준상 교차검증이 필요한 대상은
  아니라고 판단했다.
기준일: 2026년 9월 기준 (계산 공식 자체는 시점에 무관한 수학적 정의)
tags: 듀레이션, 듀레이션 뜻, 채권 듀레이션, 맥컬리 듀레이션, 수정듀레이션, 채권투자, 금리민감도, 채권가격계산
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 1,170회(일반 주제 기준 500회 이상,
  2026-09-27 backlog 등록분 재확인). 게이트2 충족 — v3 기준 3개 탈락조건 모두
  미해당(개인 블로그 진입 여지 있음, 개념+계산 탐색형 의도, 끝까지 계산한 글·
  만기별 비교표 정보이득 미확보 확인). 게이트3 충족 — 3년 만기채 전체 계산 예시
  + 만기별(1/3/10년) 듀레이션 비교표 + 무이표채 대비 사례라는 정보이득. 게이트4
  충족 — 계산식은 수학적 항등식이라 기관 확인 불요, 안내 링크(kofiabond.or.kr)는
  존재 자체만 WebSearch로 확인했고 수치 주장이 아니므로 교차검증 대상이 아니다.
capture_guide: ""
self_check: |
  [2026-09-28 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  후보 선정 경위 — backlog.verified 중 "단순 순서 대기" 성격 항목을 검토했다.
  검색량이 가장 높았던 워런트 뜻(1,350회)을 먼저 WebSearch로 검토했으나 상위
  결과가 한국은행·KDI 등 교육기관의 설명으로 이미 상당히 완결적이어서(게이트2
  탈락조건 3번 위험) 정보이득 확보가 불확실하다고 판단해 보류하고, 다음으로
  검색량이 높은 듀레이션 뜻(1,170회)으로 전환했다. 워런트 뜻은 backlog.verified에
  그대로 남겨 다음 실행에서 게이트2 각도를 더 구체화한 뒤 재검토하도록 기록했다.
  카니벌라이제이션 점검 — stock_drafts/ 전체를 grep한 결과 "듀레이션"을 본문에서
  다룬 기존 편은 없었다. 37편(채권 세금)은 채권 이자소득 과세를 다루고 가격
  민감도는 다루지 않아 검색 의도가 겹치지 않는다.
  YMYL 안전장치 점검 — 특정 종목·채권 종목을 언급하지 않았고, 계산 예시는 전부
  가상의 액면가·금리 조건으로만 구성했다. 매수·매도 시점이나 목표가는 언급하지
  않았다.
  기관 링크 점검 — 금융투자협회 채권정보센터(kofiabond.or.kr) 링크 1개를 본문
  안내 문장과 참고 출처 목록에 동일하게 걸었다.
  제목 "듀레이션 뜻과 계산 방법" 12자·금지어 없음. 슬러그 영문 소문자+하이픈
  3단어(duration-meaning-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음. 첫 문장 유형: 수치충격형("금리가
  1%포인트만 움직여도... 여덟 배 넘게 벌어질 수 있습니다") — 최근 10편(PBR·ROE·
  EPS·사모펀드·VIX·PER 등)이 전부 "[키워드]는 ~입니다" 정의형으로 시작한 것과
  겹치지 않게 골랐다.
  글 구조 유형: 계산형(RULES.md 「글 구조 다양화」) — 목차 직후 첫 H2를 개념
  설명 없이 바로 계산 박스로 시작해 "결론부터 보여주고 원리는 나중에" 순서를
  적용했다. 최근 3편(사모펀드=개념형, VIX=개념형, PER=개념형)과 겹치지 않는다.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—" 검색
  결과 0개 확인. "다만"은 본문에 쓰지 않았고 전환어는 "그런데"·"반대로"·
  "단,"으로 분산했다. `mark` 태그 총 4개(3~5개 기준 충족). FAQ 6개(직전 4편이
  4~5개였던 것과 다르게 변화). 핵심 요약 박스 제목을 "⚖️ 듀레이션 이것부터
  확인"으로, 색은 인디고(#e8eaf6/#3949ab)로 최근 게시물(포레스트그린·머스터드·
  바이올렛·슬레이트네이비·틸)과 겹치지 않게 골랐다. 목차 제외 본문 H2 5개 중
  "~나요"로 끝나는 것은 1개(20%)로 편중 없음. FAQ 헤딩도 "자주 묻는 질문" 대신
  "빠뜨리기 쉬운 질문들"로 변형(최근 4편: 더 짚어두면 좋은 것들/헷갈리기 쉬운
  부분/궁금한 점 몇 가지 더/이런 질문도 자주 나옵니다와 겹치지 않음). 헤지
  표현("~것으로 알려져 있다" 등)은 쓰지 않고 확정된 계산 결과는 단정형으로
  서술했다. 면책 문구는 최근 4편과 다른 문장 순서·표현으로 새로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-28</p>

<p>금리가 1%포인트만 움직여도, 듀레이션이 짧은 채권과 긴 채권의 가격 변동폭은 여덟 배 넘게 벌어질 수 있습니다. 듀레이션은 채권 가격이 금리 변화에 얼마나 민감하게 반응하는지 보여주는 숫자입니다. 이 글에서는 실제 숫자로 듀레이션을 끝까지 계산하고, 만기별로 얼마나 차이 나는지 비교합니다.</p>

<div style="background:#e8eaf6;border:2px solid #3949ab;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#283593;font-size:18px;">⚖️ 듀레이션 이것부터 확인</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>듀레이션은 채권 가격이 금리 변화에 얼마나 민감한지 보여주는 숫자로, 단위는 '년'입니다.</li>
    <li>맥컬리 듀레이션을 (1+만기수익률)로 나누면 수정듀레이션이 되고, 여기에 금리 변동폭을 곱하면 가격 변동률을 추정할 수 있습니다.</li>
    <li>표면금리가 낮을수록, 만기가 길수록 듀레이션은 커집니다.</li>
    <li>이자 없이 할인 발행되는 무이표채는 듀레이션이 만기와 정확히 같습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>듀레이션 계산부터 먼저 보면</li>
  <li>듀레이션이 뜻하는 것</li>
  <li>표면금리가 듀레이션을 좌우하는 이유</li>
  <li>만기별 듀레이션 비교표</li>
  <li>듀레이션은 어디서 확인하나요</li>
  <li>빠뜨리기 쉬운 질문들</li>
</ol>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">듀레이션 계산부터 먼저 보면</h2>

<p>액면 10,000원, 표면금리 4%, 만기수익률 5%인 3년 만기 이표채를 예로 직접 계산해보겠습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 채권)</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>1년 차 현금흐름 400원을 5%로 할인 → 현재가치 380.95원</li>
    <li>2년 차 현금흐름 400원을 5%로 할인 → 현재가치 362.81원</li>
    <li>3년 차 현금흐름 10,400원(이자 400원+원금 10,000원)을 5%로 할인 → 현재가치 8,983.91원</li>
    <li>세 현재가치를 더한 채권가격 = 380.95 + 362.81 + 8,983.91 = 9,727.68원</li>
    <li>맥컬리 듀레이션 = (1×380.95 + 2×362.81 + 3×8,983.91) ÷ 9,727.68 = <mark>2.88년</mark></li>
    <li>수정듀레이션 = 2.88 ÷ (1+0.05) = 2.75</li>
  </ul>
  <p style="margin:10px 0 0 0;">수정듀레이션 2.75는 금리가 1%포인트 오르면 이 채권 가격이 대략 <mark>2.75% 하락</mark>한다고 추정할 수 있다는 뜻입니다.</p>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">듀레이션이 뜻하는 것</h2>

<p>듀레이션은 채권에 투자한 돈을 평균적으로 몇 년 만에 돌려받는지를 현금흐름별 비중으로 가중평균한 값입니다. 만기가 원금 전액을 돌려받는 마지막 시점이라면, 듀레이션은 이자와 원금을 포함한 모든 현금흐름의 회수 시점을 가중평균한 시점입니다.</p>

<p>그래서 이표(이자)를 주는 채권은 듀레이션이 항상 만기보다 짧습니다. 만기 전에도 이자를 통해 돈의 일부가 먼저 돌아오기 때문입니다.</p>

<ul style="line-height:1.9;">
  <li>듀레이션의 단위는 '년'입니다.</li>
  <li>듀레이션이 클수록 금리 변화에 따른 채권가격 변동폭이 커집니다.</li>
  <li>실제 투자 판단에는 맥컬리 듀레이션보다 가격 변동률 추정에 바로 쓰는 수정듀레이션이 더 자주 쓰입니다.</li>
</ul>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">표면금리가 듀레이션을 좌우하는 이유</h2>

<p>표면금리가 높을수록 만기 전에 받는 이자 비중이 커져서, 가중평균 회수 시점이 앞으로 당겨집니다. 반대로 표면금리가 낮거나 아예 없으면 현금흐름이 만기 시점 하나에 몰리게 됩니다.</p>

<p>이 관계를 무이표채(이자를 전혀 주지 않고 할인된 가격에 발행되는 채권)로 확인해보겠습니다. 액면 10,000원, 만기수익률 5%, 만기 5년인 무이표채는 현금흐름이 만기 시점 한 번뿐이라 듀레이션이 <mark>정확히 5.00년</mark>, 만기와 똑같이 계산됩니다.</p>

<ul style="line-height:1.9;">
  <li>이표채: 이자가 만기 전에도 여러 번 들어와 듀레이션이 만기보다 짧다.</li>
  <li>무이표채: 현금흐름이 만기 한 번뿐이라 듀레이션이 만기와 같다.</li>
  <li>같은 만기라도 표면금리가 낮은 채권일수록 듀레이션이 더 길고, 금리 변화에 더 민감하다.</li>
</ul>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">만기별 듀레이션 비교표</h2>

<p>표면금리 4%, 만기수익률 5%인 조건을 그대로 두고 만기만 1년, 3년, 10년으로 바꿔 계산하면 아래와 같습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;">
  <thead>
    <tr>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">만기</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">채권가격</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">맥컬리 듀레이션</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">수정듀레이션</th>
      <th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">금리 1%p 상승 시 추정 가격변동</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">1년</td>
      <td style="border:1px solid #ddd;padding:8px;">9,904.76원</td>
      <td style="border:1px solid #ddd;padding:8px;">1.00년</td>
      <td style="border:1px solid #ddd;padding:8px;">0.95</td>
      <td style="border:1px solid #ddd;padding:8px;">-0.95%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">3년</td>
      <td style="border:1px solid #ddd;padding:8px;">9,727.68원</td>
      <td style="border:1px solid #ddd;padding:8px;">2.88년</td>
      <td style="border:1px solid #ddd;padding:8px;">2.75</td>
      <td style="border:1px solid #ddd;padding:8px;">-2.75%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">10년</td>
      <td style="border:1px solid #ddd;padding:8px;">9,227.83원</td>
      <td style="border:1px solid #ddd;padding:8px;">8.36년</td>
      <td style="border:1px solid #ddd;padding:8px;">7.96</td>
      <td style="border:1px solid #ddd;padding:8px;">-7.96%</td>
    </tr>
  </tbody>
</table>

<p>10년 만기 채권의 수정듀레이션(7.96)은 1년 만기 채권(0.95)의 <mark>8배가 넘습니다</mark>. 같은 금리 변동에도 만기가 긴 채권일수록 가격이 훨씬 크게 흔들린다는 뜻입니다.</p>

<div style="background:#eef2f7;border:2px solid #5c6bc0;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#283593;font-size:16px;">💡 실전에서 기억할 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>금리 인상이 예상되면 듀레이션이 짧은 채권(잔존만기가 짧은 채권)이 가격 방어에 유리합니다.</li>
    <li>같은 만기라면 표면금리가 높은 채권일수록 듀레이션이 짧아 상대적으로 덜 흔들립니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">듀레이션은 어디서 확인하나요</h2>

<p>개별 채권의 듀레이션은 증권사 HTS·MTS의 채권 상세 화면에서 대부분 함께 표시됩니다. 채권 종목 자체를 찾아보려면 <a href="https://www.kofiabond.or.kr/" target="_blank" rel="noopener">금융투자협회 채권정보센터</a>에서 종목별 수익률과 만기 정보를 조회할 수 있습니다.</p>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">빠뜨리기 쉬운 질문들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">듀레이션이 길면 무조건 위험한 채권인가요</summary>
  <p style="margin:10px 0 0 0;">위험하다기보다 금리 변화에 민감하다는 뜻입니다. 금리가 내리는 국면에서는 듀레이션이 긴 채권이 오히려 가격이 더 크게 오릅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">표면금리가 높을수록 듀레이션이 짧아지는 이유는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">만기 전에 받는 이자 비중이 커져서 가중평균 회수 시점이 앞으로 당겨지기 때문입니다. 이자가 많을수록 원금을 기다리지 않고도 먼저 돌려받는 돈이 많아집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">무이표채는 왜 듀레이션이 만기와 똑같은가요</summary>
  <p style="margin:10px 0 0 0;">현금흐름이 만기 시점 단 한 번뿐이라 가중평균을 낼 대상이 그 시점 하나뿐이기 때문입니다. 그래서 듀레이션 계산 결과가 만기와 정확히 일치합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">맥컬리 듀레이션과 수정듀레이션은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">맥컬리 듀레이션은 평균 회수 시점(년)을, 수정듀레이션은 그 값을 (1+만기수익률)로 나눠 금리 변동에 따른 가격 변동률 추정에 바로 쓸 수 있게 바꾼 값입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">채권 듀레이션은 어디서 확인할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">증권사 HTS·MTS의 채권 상세 화면이나 금융투자협회 채권정보센터에서 종목별로 확인할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">만기가 같아도 듀레이션이 다른 채권이 있나요</summary>
  <p style="margin:10px 0 0 0;">네. 만기가 같아도 표면금리가 다르면 듀레이션이 달라집니다. 표면금리가 낮은 채권일수록 만기가 같아도 듀레이션은 더 깁니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.kofiabond.or.kr/" target="_blank" rel="noopener">금융투자협회 채권정보센터</a></li>
  </ul>
  기준일: 2026년 9월 기준. 듀레이션 계산식 자체는 시점과 무관한 수학적 정의이며, 본문의 채권가격·듀레이션 수치는 이해를 돕기 위해 가정한 예시입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
계산에 쓰인 액면가·표면금리·수익률은 이해를 돕기 위해 만든 가상의 조건이며 실제 특정 채권의 시세가 아닙니다. 이 글은 듀레이션 개념과 계산법을 설명하는 정보 글로, 특정 채권이나 종목의 매수·매도를 권하지 않습니다. 실제 투자 전에는 해당 채권의 최신 수익률과 잔존만기를 직접 확인하시고, 투자 결과에 대한 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "듀레이션 뜻과 계산 방법",
  "description": "채권 듀레이션의 뜻과 맥컬리 듀레이션·수정듀레이션 계산법을 실제 숫자 예시로 정리하고, 만기별 듀레이션 차이를 비교표로 보여줍니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-28",
  "dateModified": "2026-09-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/duration-meaning-calculation"
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
      "name": "듀레이션이 길면 무조건 위험한 채권인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "위험하다기보다 금리 변화에 민감하다는 뜻입니다. 금리가 내리는 국면에서는 듀레이션이 긴 채권이 오히려 가격이 더 크게 오릅니다." }
    },
    {
      "@type": "Question",
      "name": "표면금리가 높을수록 듀레이션이 짧아지는 이유는 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "만기 전에 받는 이자 비중이 커져서 가중평균 회수 시점이 앞으로 당겨지기 때문입니다. 이자가 많을수록 원금을 기다리지 않고도 먼저 돌려받는 돈이 많아집니다." }
    },
    {
      "@type": "Question",
      "name": "무이표채는 왜 듀레이션이 만기와 똑같은가요",
      "acceptedAnswer": { "@type": "Answer", "text": "현금흐름이 만기 시점 단 한 번뿐이라 가중평균을 낼 대상이 그 시점 하나뿐이기 때문입니다. 그래서 듀레이션 계산 결과가 만기와 정확히 일치합니다." }
    },
    {
      "@type": "Question",
      "name": "맥컬리 듀레이션과 수정듀레이션은 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "맥컬리 듀레이션은 평균 회수 시점(년)을, 수정듀레이션은 그 값을 (1+만기수익률)로 나눠 금리 변동에 따른 가격 변동률 추정에 바로 쓸 수 있게 바꾼 값입니다." }
    },
    {
      "@type": "Question",
      "name": "채권 듀레이션은 어디서 확인할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권사 HTS·MTS의 채권 상세 화면이나 금융투자협회 채권정보센터에서 종목별로 확인할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "만기가 같아도 듀레이션이 다른 채권이 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 만기가 같아도 표면금리가 다르면 듀레이션이 달라집니다. 표면금리가 낮은 채권일수록 만기가 같아도 듀레이션은 더 깁니다." }
    }
  ]
}
</script>
