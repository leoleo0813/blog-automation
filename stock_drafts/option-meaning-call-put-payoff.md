---
keyword: 옵션 뜻
title: 옵션 뜻 콜옵션 풋옵션 손익 구조
slug: option-meaning-call-put-payoff
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 1720 (PC 160 / 모바일 1560, 2026-10-02 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-02 - 통과]
  WebSearch "옵션 뜻 콜옵션 풋옵션 프리미엄 손익 구조 초보" 상위: tossbank.com(은행 공식 콘텐츠), kbthink.com(KB손해보험), mofe.go.kr(기획재정부 시사경제용어사전), cmegroup.com(거래소 교육), m4markets.com(해외 브로커 콘텐츠), namu.wiki(백과), it.dategom.com(소규모 IT 블로그).
  1) 진입 여지: 있음. dategom 같은 소규모 블로그와 브로커 콘텐츠 사이트가 상위에 있다.
  2) 검색 의도: 뜻과 손익 구조를 찾는 탐색형. 조회·계산기 실행 의도 아님.
  3) 답 완결 여부: 부분적. 상위 요약은 정의와 행사가격 100만 원 콜옵션 한 줄 예시 중심이다. 네 포지션을 한 표에 놓은 손익분기·최대 손익 비교, 만기 지수별 손익표, 포인트를 원화로 바꾼 값은 요약 단계에서 확인하지 못했다. 상위 페이지 본문 전체는 열어보지 못했다(자동화 세션 egress 제한).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 콜 매수·콜 매도·풋 매수·풋 매도 네 포지션 비교표(최대 이익·최대 손실·손익분기).
  (b) 행사가격 300, 프리미엄 3.00 가상 조건의 만기 지수별(280~320) 손익표와 원화 환산표.
  (c) 내가격·등가격·외가격 내재가치 구분표, 옵션과 선물 비교표.
primary_source: |
  한국거래소 open.krx.co.kr WebFetch 1회 시도, EGRESS_BLOCKED.
  WebSearch 2회로 교차확인했다. 콜옵션=살 권리, 풋옵션=팔 권리, 매수자 최대 손실=프리미엄, 매도자 손실 확대 구조가 기획재정부 시사경제용어사전, KB손해보험 KB Think, 토스뱅크에서 일치(검색 결과 제목·요약 단계 확인, 본문 미열람).
  코스피200 옵션 거래승수 25만 원과 현금결제는 한국투자증권·KB증권·신한투자증권·유진투자증권 상품 안내의 검색 요약에서 일치했다. 세율·공제 한도형 수치는 없고 거래소 상품 규격 두 가지(승수, 결제방식)만 외부 수치다. 본문 손익표는 전부 가상 조건에서 직접 계산한 값이다.
기준일: 2026년 10월 기준 (손익 계산 예시는 전부 가상)
tags: 옵션, 옵션 뜻, 콜옵션, 풋옵션, 프리미엄, 행사가격, 코스피200 옵션, 옵션 손익, 옵션 매수 매도, 파생상품
gate_pass: true
gate_pass_note: |
  게이트1 1,720회, 게이트2 v3 통과, 게이트3 가상 조건 손익표, 게이트4는 정부 용어사전과 증권사 4곳 교차확인(원문 직접 열람은 실패). 사람 확인 권장: 발행 전 KRX 코스피200 옵션 상품명세(https://www.krx.co.kr/contents/OPN/01/01040202/OPN01040202.jsp)에서 거래승수 25만 원과 현금결제를 한 번 대조해 주세요. 불일치하면 gate_pass를 false로 바꾸세요.
self_check: |
  [2026-10-02 gate_pass:true, 게이트4 교차검증]
  후보 경위: 신규 8개 실측 결과 선물옵션 만기일 7,030·레버리지 ETF 뜻 6,490·스톡옵션 뜻 2,110·옵션 뜻 1,720 PASS, 신용융자 이자·평단가 계산·시간외거래·샤프지수 FAIL. 만기일은 60편 네마녀의 날, 레버리지 ETF는 40편 곱버스와 레버리지 인버스 ETF 예탁금 편, 스톡옵션은 stock-option-tax 편과 겹쳐 보류하고 전용 편이 없는 옵션 뜻을 채택.
  카니벌라이제이션: 커버드콜 ETF 세금·네마녀의 날 편은 옵션을 배경으로만 언급. 이 글은 옵션 손익 구조 자체가 주제이고 두 편을 본문에서 이름으로 안내(내부 링크 주소는 발행 후 사람이 연결). 초급 개념에서 한 단계 올라간 파생상품 기초.
  YMYL: 종목 추천·목표가·매매시점 없음. 옵션 거래를 권하지 않고 매도 위험을 명시. 모든 행사가격·프리미엄 가상 표기.
  기관 링크: 본문 기관 안내 문장 2개(KRX, 기재부 용어사전) 링크 처리, 출처 목록 7개 전부 링크 처리.
  제목 "옵션 뜻 콜옵션 풋옵션 손익 구조" 16자, 금지어 없음, 최근 5편의 "뜻과 계산"·"공식과" 틀과 다른 "A B 손익 구조" 틀. 슬러그 5단어.
  첫 문장 유형: 대비형(직전 117 수치충격, 116 문제제기와 다름). 인트로 둘째 문장에 정의 포함, 메타 문장 없음.
  글 구조 유형: 비교형(목차 직후 첫 H2의 첫 블록이 네 포지션 비교표). 직전 117 절차형, 116 개념형, 115 계산형과 다름.
  어투 모드: A 해설형(합쇼체 단정). 직전 117 B, 116 C와 다름. 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 4개, FAQ 6개(직전 117 4·116 5와 다름), H2 6개 중 "~나요"형 0개. 요약박스 보라(#f3eefc/#7a4fc4), 제목 "🔮 방향부터 구분하기", 중간 박스 "📎 손익표 읽기 체크", FAQ 헤딩 "표를 읽고 나서 남는 의문 풀이".
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>콜옵션과 풋옵션은 이름만 비슷할 뿐 돈이 벌리는 방향이 정반대입니다. 옵션은 정해 둔 가격(행사가격)으로 사거나 팔 수 있는 권리이고, 그 권리를 사는 값이 프리미엄입니다.</p>

<div style="background:#f3eefc;border:2px solid #7a4fc4;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4b2c85;font-size:18px;">🔮 방향부터 구분하기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>콜옵션은 <mark>살 수 있는 권리</mark>, 풋옵션은 <mark>팔 수 있는 권리</mark>입니다.</li><li>매수자는 프리미엄만큼만 잃고, 매도자는 프리미엄만 받는 대신 손실이 크게 열려 있습니다.</li><li>가상 조건(행사가격 300, 프리미엄 3.00)에서 손익분기는 콜 303, 풋 297입니다.</li><li>코스피200 옵션은 1포인트가 25만 원이라 3.00포인트 프리미엄은 75만 원입니다.</li></ul>
</div>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;"><li>콜옵션과 풋옵션 네 가지 포지션 비교</li><li>만기 손익 계산법</li><li>프리미엄이 정해지는 방식</li><li>옵션과 선물의 차이</li><li>매도 포지션의 위험 구조</li><li>코스피200 옵션의 실제 규격</li></ol>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">콜옵션과 풋옵션 네 가지 포지션 비교</h2>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">네 가지 포지션 한눈에 비교 (가상 조건: 행사가격 300, 프리미엄 3.00포인트, 만기 손익 기준)</caption>
  <thead>
    <tr style="background:#f3eefc;"><th style="border:1px solid #ddd;padding:8px;">포지션</th><th style="border:1px solid #ddd;padding:8px;">프리미엄</th><th style="border:1px solid #ddd;padding:8px;">이익이 나는 방향</th><th style="border:1px solid #ddd;padding:8px;">최대 이익</th><th style="border:1px solid #ddd;padding:8px;">최대 손실</th><th style="border:1px solid #ddd;padding:8px;">손익분기 지수</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">콜옵션 매수</td><td style="border:1px solid #ddd;padding:8px;">지급 (3.00)</td><td style="border:1px solid #ddd;padding:8px;">지수 상승</td><td style="border:1px solid #ddd;padding:8px;">이론상 무제한</td><td style="border:1px solid #ddd;padding:8px;">프리미엄 3.00</td><td style="border:1px solid #ddd;padding:8px;">303</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">콜옵션 매도</td><td style="border:1px solid #ddd;padding:8px;">수령 (3.00)</td><td style="border:1px solid #ddd;padding:8px;">지수 하락 또는 제자리</td><td style="border:1px solid #ddd;padding:8px;">프리미엄 3.00</td><td style="border:1px solid #ddd;padding:8px;">이론상 무제한</td><td style="border:1px solid #ddd;padding:8px;">303</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">풋옵션 매수</td><td style="border:1px solid #ddd;padding:8px;">지급 (3.00)</td><td style="border:1px solid #ddd;padding:8px;">지수 하락</td><td style="border:1px solid #ddd;padding:8px;">297 (지수가 0이 될 때)</td><td style="border:1px solid #ddd;padding:8px;">프리미엄 3.00</td><td style="border:1px solid #ddd;padding:8px;">297</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">풋옵션 매도</td><td style="border:1px solid #ddd;padding:8px;">수령 (3.00)</td><td style="border:1px solid #ddd;padding:8px;">지수 상승 또는 제자리</td><td style="border:1px solid #ddd;padding:8px;">프리미엄 3.00</td><td style="border:1px solid #ddd;padding:8px;">297 (지수가 0이 될 때)</td><td style="border:1px solid #ddd;padding:8px;">297</td></tr>
  </tbody>
</table>

<p>옵션의 손익은 사는 쪽과 파는 쪽, 콜과 풋의 조합 네 가지로 갈립니다. 같은 프리미엄 3.00이 한쪽에서는 비용이고 반대쪽에서는 수입입니다.</p>

<p>콜 매수와 풋 매수는 최대 손실이 프리미엄으로 막혀 있습니다. 콜 매도와 풋 매도는 최대 이익이 프리미엄으로 막혀 있습니다. <mark>이익이 한정된 쪽은 손실이 크게 열려 있고, 손실이 한정된 쪽은 이익이 열려 있습니다.</mark></p>

<p>이 표의 숫자는 전부 계산 설명을 위해 만든 가상 값입니다. 실제 거래되는 옵션의 행사가격과 프리미엄이 아닙니다.</p>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">만기 손익 계산법</h2>

<div style="background:#faf7fe;border:1px solid #d6c6ef;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>계산 순서 (콜 매수 기준)</strong>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.8;"><li>내재가치 = 만기 지수 - 행사가격, 단 0보다 작으면 0입니다.</li><li>손익 = 내재가치 - 처음 낸 프리미엄입니다.</li><li>풋 매수는 내재가치를 행사가격 - 만기 지수로 바꿔 같은 순서로 계산합니다.</li><li>매도 포지션의 손익은 매수 포지션 손익의 부호를 뒤집은 값입니다.</li></ul>
</div>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">만기 때 지수별 손익 (단위: 포인트, 가상 조건: 행사가격 300, 프리미엄 3.00)</caption>
  <thead>
    <tr style="background:#f3eefc;"><th style="border:1px solid #ddd;padding:8px;">만기 지수</th><th style="border:1px solid #ddd;padding:8px;">콜 매수</th><th style="border:1px solid #ddd;padding:8px;">콜 매도</th><th style="border:1px solid #ddd;padding:8px;">풋 매수</th><th style="border:1px solid #ddd;padding:8px;">풋 매도</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">280</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td><td style="border:1px solid #ddd;padding:8px;">+17</td><td style="border:1px solid #ddd;padding:8px;">-17</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">290</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td><td style="border:1px solid #ddd;padding:8px;">+7</td><td style="border:1px solid #ddd;padding:8px;">-7</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">297</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr style="background:#f3eefc;"><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">303</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">310</td><td style="border:1px solid #ddd;padding:8px;">+7</td><td style="border:1px solid #ddd;padding:8px;">-7</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">320</td><td style="border:1px solid #ddd;padding:8px;">+17</td><td style="border:1px solid #ddd;padding:8px;">-17</td><td style="border:1px solid #ddd;padding:8px;">-3</td><td style="border:1px solid #ddd;padding:8px;">+3</td></tr>
  </tbody>
</table>

<p>만기 지수 300에서는 콜과 풋 모두 내재가치가 0이라 매수자는 프리미엄 3.00을 그대로 잃습니다. 303에서 콜 매수가 본전이 되고, 297에서 풋 매수가 본전이 됩니다.</p>

<p>표를 보면 매수자의 손실은 -3으로 바닥이 막혀 있습니다. 반면 콜 매수 이익은 320에서 +17, 풋 매수 이익은 280에서 +17로 지수가 더 움직일수록 계속 커집니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">같은 조건을 원화로 바꾼 값 (1포인트 = 25만 원 곱셈, 수수료와 세금 제외)</caption>
  <thead>
    <tr style="background:#f3eefc;"><th style="border:1px solid #ddd;padding:8px;">만기 지수</th><th style="border:1px solid #ddd;padding:8px;">콜 매수</th><th style="border:1px solid #ddd;padding:8px;">콜 매도</th><th style="border:1px solid #ddd;padding:8px;">풋 매수</th><th style="border:1px solid #ddd;padding:8px;">풋 매도</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">290</td><td style="border:1px solid #ddd;padding:8px;">-75만 원</td><td style="border:1px solid #ddd;padding:8px;">+75만 원</td><td style="border:1px solid #ddd;padding:8px;">+175만 원</td><td style="border:1px solid #ddd;padding:8px;">-175만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">303</td><td style="border:1px solid #ddd;padding:8px;">0원</td><td style="border:1px solid #ddd;padding:8px;">0원</td><td style="border:1px solid #ddd;padding:8px;">-75만 원</td><td style="border:1px solid #ddd;padding:8px;">+75만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">320</td><td style="border:1px solid #ddd;padding:8px;">+425만 원</td><td style="border:1px solid #ddd;padding:8px;">-425만 원</td><td style="border:1px solid #ddd;padding:8px;">-75만 원</td><td style="border:1px solid #ddd;padding:8px;">+75만 원</td></tr>
  </tbody>
</table>

<p>원화로 바꾸면 만기 지수 290에서 풋 매수는 175만 원 이익, 320에서 콜 매수는 425만 원 이익입니다. 같은 지수에서 매도자는 정확히 그만큼 손실입니다. 옵션은 한쪽의 이익이 곧 반대쪽의 손실인 구조입니다.</p>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">프리미엄이 정해지는 방식</h2>

<p>프리미엄은 내재가치와 시간가치를 더한 값입니다. 내재가치는 지금 당장 행사하면 생기는 이익이고, 시간가치는 만기까지 남은 시간 동안 지수가 유리하게 움직일 가능성에 매기는 값입니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">행사가격 300 기준 내재가치 구분 (가상 지수)</caption>
  <thead>
    <tr style="background:#f3eefc;"><th style="border:1px solid #ddd;padding:8px;">현재 지수</th><th style="border:1px solid #ddd;padding:8px;">콜옵션 상태</th><th style="border:1px solid #ddd;padding:8px;">풋옵션 상태</th><th style="border:1px solid #ddd;padding:8px;">콜 내재가치</th><th style="border:1px solid #ddd;padding:8px;">풋 내재가치</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">310</td><td style="border:1px solid #ddd;padding:8px;">내가격(ITM)</td><td style="border:1px solid #ddd;padding:8px;">외가격(OTM)</td><td style="border:1px solid #ddd;padding:8px;">10포인트</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">등가격(ATM)</td><td style="border:1px solid #ddd;padding:8px;">등가격(ATM)</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">290</td><td style="border:1px solid #ddd;padding:8px;">외가격(OTM)</td><td style="border:1px solid #ddd;padding:8px;">내가격(ITM)</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">10포인트</td></tr>
  </tbody>
</table>

<p>지수가 310이면 행사가격 300 콜옵션은 10포인트의 내재가치를 가진 내가격 상태입니다. 같은 지수에서 풋옵션은 내재가치가 0이라 프리미엄이 전부 시간가치입니다.</p>

<p>시간가치는 만기가 다가올수록 줄어듭니다. 이 글의 3.00 프리미엄이 만기 지수 300에서 전부 사라지는 것도 같은 이유입니다. 프리미엄이 시장에서 어떤 값으로 형성되는지는 거래소 시세에서 직접 확인합니다. 콜옵션의 정의는 <a href="https://mofe.go.kr/sisa/dictionary/detail?idx=2583" target="_blank" rel="noopener">기획재정부 시사경제용어사전 - 콜옵션</a>에서도 같은 구조로 설명합니다.</p>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">옵션과 선물의 차이</h2>

<p>선물은 만기에 사고팔 의무이고 옵션은 사고팔 권리입니다. 권리를 가진 매수자만 행사 여부를 고를 수 있습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">옵션과 선물 비교</caption>
  <thead>
    <tr style="background:#f3eefc;"><th style="border:1px solid #ddd;padding:8px;">구분</th><th style="border:1px solid #ddd;padding:8px;">선물</th><th style="border:1px solid #ddd;padding:8px;">옵션</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">매수자의 권리와 의무</td><td style="border:1px solid #ddd;padding:8px;">만기에 사고팔 의무</td><td style="border:1px solid #ddd;padding:8px;">사고팔 권리, 의무는 없음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">처음 내는 돈</td><td style="border:1px solid #ddd;padding:8px;">증거금</td><td style="border:1px solid #ddd;padding:8px;">프리미엄(매수자) 또는 증거금(매도자)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">매수자의 최대 손실</td><td style="border:1px solid #ddd;padding:8px;">지수 변동에 따라 커질 수 있음</td><td style="border:1px solid #ddd;padding:8px;">지급한 프리미엄</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">손익 모양</td><td style="border:1px solid #ddd;padding:8px;">지수와 직선으로 움직임</td><td style="border:1px solid #ddd;padding:8px;">꺾인 선: 한쪽은 막히고 한쪽은 열림</td></tr>
  </tbody>
</table>

<p>선물은 지수와 손익이 직선으로 움직여 오를 때와 내릴 때 같은 속도로 벌거나 잃습니다. 옵션은 프리미엄 지점에서 꺾이기 때문에 손익 그래프가 꺾인 선 모양입니다. 앞서 다룬 <strong>네마녀의 날 뜻</strong> 편의 선물옵션 동시만기는 이 두 상품의 만기가 같은 날 겹치는 날입니다.</p>

<div style="background:#fbf8ff;border:2px solid #a98bd9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4b2c85;font-size:18px;">📎 손익표 읽기 체크</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>내가 매수자인지 매도자인지부터 확인합니다. 같은 표에서 부호가 정반대입니다.</li><li>손익분기는 콜이면 행사가격 + 프리미엄, 풋이면 행사가격 - 프리미엄입니다.</li><li>프리미엄은 <mark>1포인트당 곱하는 승수</mark>를 곱해야 실제 금액이 됩니다.</li></ul>
</div>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">매도 포지션의 위험 구조</h2>

<p>매도자의 이익은 처음 받은 프리미엄이 상한입니다. 이 글의 가상 조건에서는 3.00포인트, 25만 원 곱셈으로 75만 원입니다.</p>

<p>반대로 콜 매도는 지수가 오를수록 손실이 이론상 끝없이 커지고, 풋 매도는 지수가 내려갈수록 손실이 커져 지수가 0이 되는 극단에서 297포인트에 이릅니다. 손실 가능 금액이 프리미엄보다 훨씬 크므로 매도자는 거래소와 증권사가 정한 증거금을 맡겨야 합니다.</p>

<ul><li>프리미엄을 받는다고 손실이 막히는 것은 아닙니다.</li><li>증거금 금액은 상품과 시점에 따라 바뀌므로 이용하는 증권사 안내에서 확인합니다.</li><li>개인이 파생상품을 거래하려면 증권사가 정한 가입 요건이 있을 수 있어 사전에 확인해야 합니다.</li></ul>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">코스피200 옵션의 실제 규격</h2>

<p>코스피200 옵션의 거래승수는 25만 원이라 옵션 가격 1포인트가 25만 원입니다. 최종 결제는 현금으로 이뤄집니다. 한국투자증권, KB증권, 신한투자증권의 상품 안내가 같은 규격을 설명합니다. 거래소 원문은 <a href="https://www.krx.co.kr/contents/OPN/01/01040202/OPN01040202.jsp" target="_blank" rel="noopener">한국거래소(KRX)</a> 상품 안내에서 확인합니다.</p>

<ul><li>예시: 프리미엄 3.00포인트 × 25만 원 = 75만 원</li><li>예시: 프리미엄 0.50포인트 × 25만 원 = 12만 5천 원</li><li>현금결제라 만기에 실제 주식을 주고받지 않고 손익만 계산해 정산합니다.</li></ul>

<p>상품 규격과 승수는 거래소 공지로 바뀔 수 있습니다. 이 글의 계산은 개념 설명용이고, 실제 거래 전에는 현재 상품명세를 다시 확인해야 합니다.</p>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">표를 읽고 나서 남는 의문 풀이</h2>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">옵션을 사면 최대 얼마까지 잃을 수 있나요?</summary><p>매수자의 최대 손실은 지급한 프리미엄입니다. 이 글의 가상 조건에서는 3.00포인트, 25만 원 곱셈으로 75만 원입니다.</p></details>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">콜옵션은 지수가 오르기만 하면 이익인가요?</summary><p>아닙니다. 지수가 행사가격 300을 넘어도 프리미엄 3.00을 갚는 303을 넘어야 이익이 납니다. 301이나 302에서 끝나면 권리를 행사해도 손실입니다.</p></details>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">만기 전에 옵션을 팔 수 있나요?</summary><p>프리미엄은 만기 전에도 시세가 움직이므로 반대 거래로 정리할 수 있습니다. 이 글의 표는 만기까지 들고 갔을 때의 손익이라 중간 시세와는 다릅니다.</p></details>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">프리미엄 0.5포인트는 원화로 얼마인가요?</summary><p>지수옵션이 코스피200 옵션 규격(거래승수 25만 원)이라면 0.5 × 25만 = 12만 5천 원입니다. 상품마다 승수가 다르니 거래하는 상품의 규격을 먼저 확인하세요.</p></details>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">매도는 프리미엄을 먼저 받으니 더 유리하지 않나요?</summary><p>받는 돈은 프리미엄이 상한입니다. 반면 콜 매도의 손실은 이론상 끝이 없고, 풋 매도의 손실도 지수가 크게 내려갈수록 커집니다. 이익은 작게 한정되고 손실은 크게 열려 있는 구조입니다.</p></details>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">커버드콜 ETF는 옵션과 무슨 관계인가요?</summary><p>커버드콜 ETF는 보유 자산에 콜옵션 매도를 결합해 프리미엄 수입을 노리는 구조입니다. 이 글의 콜 매도 행(상한이 막힌 이익)이 그 원리의 핵심이고, 세금은 <strong>커버드콜 ETF 세금</strong> 편에서 따로 다뤘습니다.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, 한국거래소 원문은 자동 열람이 막혀 증권사 상품 안내와 공공기관 용어사전으로 교차 확인):
  <ul style="margin:6px 0 0 0;padding-left:20px;"><li><a href="https://www.krx.co.kr/contents/OPN/01/01040202/OPN01040202.jsp" target="_blank" rel="noopener">한국거래소(KRX)</a> - 코스피200 옵션 상품 안내</li><li><a href="https://truefriend.com/main/bond/domestic/_static/TF03bd010100.jsp" target="_blank" rel="noopener">한국투자증권 주가지수선물옵션 상품소개</a></li><li><a href="https://www.kbsec.com/go.able?linkcd=s07040020P201" target="_blank" rel="noopener">KB증권 주가지수선물/옵션</a></li><li><a href="https://www.shinhansec.com/siw/trading/etc-market/market_index_tab5/contents.do" target="_blank" rel="noopener">신한투자증권 주가지수상품 거래안내</a></li><li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=2583" target="_blank" rel="noopener">기획재정부 시사경제용어사전 - 콜옵션</a></li><li><a href="https://kbthink.com/main/asset-management/wealth-manage-tip/kbthink-original/202411/calloption,putoption.html" target="_blank" rel="noopener">KB손해보험 KB Think - 콜옵션 풋옵션 개념과 차이</a></li><li><a href="https://www.tossbank.com/articles/calloption" target="_blank" rel="noopener">토스뱅크 - 콜옵션</a></li></ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 옵션의 구조를 설명하는 정보성 글입니다. 특정 상품의 거래나 매매 시점을 권하지 않고, 본문의 행사가격과 프리미엄은 모두 가상 값입니다. 파생상품은 원금을 넘는 손실이 날 수 있으며 투자 판단과 결과는 투자자 본인에게 있으니, 규격과 증거금은 거래 전에 증권사와 거래소 안내로 다시 확인해 주세요.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "옵션 뜻 콜옵션 풋옵션 손익 구조",
      "description": "옵션 뜻과 콜옵션 풋옵션의 차이를 가상 조건으로 네 가지 포지션의 만기 손익표로 계산하고, 프리미엄 구성과 코스피200 옵션 규격까지 정리했습니다.",
      "author": {
        "@type": "Person",
        "name": "센시티브보스"
      },
      "publisher": {
        "@type": "Person",
        "name": "센시티브보스"
      },
      "datePublished": "2026-10-02",
      "dateModified": "2026-10-02",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://sensitiveboss3.tistory.com/entry/option-meaning-call-put-payoff"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "옵션을 사면 최대 얼마까지 잃을 수 있나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "매수자의 최대 손실은 지급한 프리미엄입니다. 이 글의 가상 조건에서는 3.00포인트, 25만 원 곱셈으로 75만 원입니다."
          }
        },
        {
          "@type": "Question",
          "name": "콜옵션은 지수가 오르기만 하면 이익인가요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "아닙니다. 지수가 행사가격 300을 넘어도 프리미엄 3.00을 갚는 303을 넘어야 이익이 납니다. 301이나 302에서 끝나면 권리를 행사해도 손실입니다."
          }
        },
        {
          "@type": "Question",
          "name": "만기 전에 옵션을 팔 수 있나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "프리미엄은 만기 전에도 시세가 움직이므로 반대 거래로 정리할 수 있습니다. 이 글의 표는 만기까지 들고 갔을 때의 손익이라 중간 시세와는 다릅니다."
          }
        },
        {
          "@type": "Question",
          "name": "프리미엄 0.5포인트는 원화로 얼마인가요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "지수옵션이 코스피200 옵션 규격(거래승수 25만 원)이라면 0.5 × 25만 = 12만 5천 원입니다. 상품마다 승수가 다르니 거래하는 상품의 규격을 먼저 확인하세요."
          }
        },
        {
          "@type": "Question",
          "name": "매도는 프리미엄을 먼저 받으니 더 유리하지 않나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "받는 돈은 프리미엄이 상한입니다. 반면 콜 매도의 손실은 이론상 끝이 없고, 풋 매도의 손실도 지수가 크게 내려갈수록 커집니다. 이익은 작게 한정되고 손실은 크게 열려 있는 구조입니다."
          }
        },
        {
          "@type": "Question",
          "name": "커버드콜 ETF는 옵션과 무슨 관계인가요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "커버드콜 ETF는 보유 자산에 콜옵션 매도를 결합해 프리미엄 수입을 노리는 구조입니다. 이 글의 콜 매도 행(상한이 막힌 이익)이 그 원리의 핵심이고, 세금은 커버드콜 ETF 세금 편에서 따로 다뤘습니다."
          }
        }
      ]
    }
  ]
}
</script>
