---
keyword: RSI 뜻
title: RSI 뜻과 14일 값 직접 구하기
slug: rsi-meaning-14day-calculation
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 1420 (PC 300 / 모바일 1120)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-01 - 통과]
  WebSearch "RSI 뜻 계산 방법 14일 평균 상승폭 하락폭 과매수 과매도" 상위 결과(일부 TradingView 스크립트 페이지 제외): brunch.co.kr 개인 글 2건, secondmin.co.kr(개인·소규모 사이트), m4markets.com·xs.com(해외 FX 브로커 콘텐츠), blog.okfngroup.com(금융사 블로그), economybloc.com(경제 용어 사이트).
  1) 진입 여지: 있음. 브런치 개인 글과 소규모 사이트가 상위에 있다.
  2) 검색 의도: 뜻과 계산 방법을 찾는 탐색형. 조회·계산기 실행 의도 아님.
  3) 답 완결 여부: 부분적. 검색 요약에서는 공식과 70/30 기준 설명이 중심이었고, 15일 일별 변동표로 와일더 평활 2일차까지 풀고 단순평균 방식 값(58.62)과 나란히 비교한 사례는 요약 단계에서 확인하지 못했다. 단 상위 페이지 본문 전체는 열어보지 못했다(자동화 세션 제약).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 종가 15일치 변동표와 14일 RSI 67.86 단계별 계산.
  (b) 15일차 와일더 방식 RSI 60.84와 단순평균 방식 58.62 비교표.
  (c) RSI 값이 말해 주는 것과 말해 주지 않는 것 표, 흔한 오해 vs 실제 표.
  (추가 2026-10-02) RSI 눈금 위 계산값 3개(67.86·60.84·58.62) 그림 1장(가상 종가).
primary_source: |
  RSI는 1978년 웰스 와일더가 소개한 지표이며 공식 기관이 숫자를 공표하는 지표가 아니라 1차 출처가 따로 없다. 와일더 원저는 열람하지 못했다.
  Investopedia WebFetch 1회 시도, 접속 불가. 이후 WebSearch 3회로 독립 출처를 교차 확인했다:
  - 공식 RSI = 100 - 100/(1+RS), RS = 평균 상승폭/평균 하락폭, 14일 기본값, 70/30 관례: 위키백과, 트레이딩뷰 도움말, 위키독스, 이코노미블록, 알파스퀘어가 일치.
  - 첫 14일 단순평균 후 (전일 평균×13+당일)/14로 이어 가는 와일더 평활: 위키백과, TC2000 도움말, 알파스퀘어가 일치.
  세율·한도가 아닌 수학적 정의이며 본문 가격은 전부 가상 값으로 명시했다.
기준일: 2026년 10월 기준 (계산 예시는 가상)
tags: RSI 뜻, RSI 계산법, 상대강도지수, RSI 14일, 와일더 RSI, 과매수 과매도, 기술적 지표, 보조지표, 주식 차트, 차트 보는 법
gate_pass: true
gate_pass_note: |
  게이트1 1,420회, 게이트2 v3 통과, 게이트3 계산표·비교표 확보. 게이트4 미충족: 독립 출처 5곳은 일치하지만 RULES.md 기준(언론·준정부·법무법인급 최소 1곳)에 맞는 기관·언론 출처가 없다(위키백과·트레이딩뷰·위키독스 등).
  사람이 할 일: 한국은행 경제금융용어 또는 금융투자협회·한국거래소 용어사전 등에서 RSI(상대강도지수) 정의 한 곳을 확인해 출처 목록에 추가하면 true로 바꿀 수 있습니다. 그리고 (1) 본문 계산 숫자(67.86 / 60.84 / 58.62)를 엑셀로 한 번 재계산하고, (2) 게이트2의 "답 완결 여부"가 요약 단계 판단이므로 상위 2~3개 글 본문이 15일 일별 계산표를 이미 싣고 있지 않은지 훑어보면 됩니다.
  [2026-10-05 보류 해제] 언론(디지털투데이) 용어 해설이 정의(일정 기간 오른 폭과 내린 폭 비교, 0~100, 14일·70/30 관례)와 일치해 기존 게이트4 기준(언론 1곳 이상) 충족. 계산 공식은 와일더 원식으로 수학적 정의.
self_check: |
  [2026-10-01 gate_pass:false, 게이트4 기관 출처 부족]
  후보 경위: check-keywords 8개(RSI 뜻 1,420 PASS, MACD 뜻 130, 부채비율 뜻 70, 영업이익률 뜻 20, 잉여현금흐름 뜻 40, 장단기 금리차 490, 버핏지수 640 PASS, 신용잔고 뜻 30) 중 최고 검색량 RSI 뜻 채택. 버핏지수 640은 다음 편 후보.
  카니벌라이제이션: stock_drafts에서 RSI 단어는 볼린저밴드 편 메모와 파생상품 편 메모에만 등장(본문 주제 아님). 볼린저밴드 편과는 내부 링크로 연결, 계산 대상이 달라 겹치지 않음.
  YMYL: 종목 추천·목표가·매매시점 없음. 70/30을 매도·매수 신호로 쓰지 않고 "예측이 아님"을 표로 명시. 계산 가격은 가상으로 명시.
  기관 링크: 외부 안내 문장 전부 링크, 출처 목록 5개 전부 링크. 단 공공기관 출처는 없음.
  제목 "RSI 뜻과 14일 값 직접 구하기" 17자, 금지어 없음, 최근 5편(GDP 뜻과 ... 계산 / 환율 뜻과 ... 계산법 / 기준금리 뜻과 ... 계산법)의 "~뜻과 ~ 계산(법)" 틀을 피해 "직접 구하기"로 바꿈. 슬러그 rsi-meaning-14day-calculation 4단어(-meaning-calculation 접미사 아님).
  첫 문장 유형: 문제제기형(차트 숫자가 어디서 나왔는지 따라가 본 적이 있나요). 직전 편들과 겹치지 않게 선택.
  글 구조 유형: 계산형(목차 직후 첫 H2가 15일 변동표와 단계 계산, 개념 설명보다 먼저). 직전 CAGR는 절차형, GDP는 계산형이나 환율·기준금리가 사이에 있어 3편 연속 아님.
  어투 모드: C 사례형(가상 인물 A씨의 가상 종가를 끝까지 따라감, 가상임을 명시). 1인칭 경험담 없음.
  AI 티 점검: em대시 0개, 다만 0회(본문), mark 밀도 4개, FAQ 6개(직전 CAGR 4·기준금리 5·환율 5와 다름), H2 7개(목차 포함) 중 "~나요"형 0개(FAQ 질문 제외). 요약박스 보라(#f3edfc/#7a4fc4), 제목 "🧮 이 글의 계산 결과 요약". FAQ 헤딩 "RSI 확인하다 궁금해지는 점"(걸리는·막히는·세 줄 어휘 회피). 면책 문구 새 표현.
  [2026-10-02 독자 관점 규칙 반영]
  그림 1장(RSI 눈금·관례 구간·계산값). "RSI가 투자 판단에 쓸모 있는 순간과 아닌 순간" H2 추가(매매 지시 없음). 내부 링크 2개(85 볼린저밴드·62 데드캣 바운스, 발행 완료). FAQ 6개 유지. gate_pass:false 사유(게이트4 기관 출처)는 그대로.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>차트 아래에 붙은 RSI 숫자 67.9가 어디서 나온 값인지 따라가 본 적이 있나요? RSI는 최근 14일 동안 오른 폭과 내린 폭을 비교해 0에서 100 사이로 바꾼 값입니다. 가상 종가 15일치로 14일 RSI를 직접 구하고, 하루가 더 지났을 때 값이 어떻게 바뀌는지까지 한 줄씩 따라가 봅니다.</p>

<div style="background:#f3edfc;border:2px solid #7a4fc4;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4a2d86;font-size:18px;">🧮 이 글의 계산 결과 요약</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>RSI는 100 - 100 ÷ (1 + RS)이고, RS는 평균 상승폭 ÷ 평균 하락폭입니다.</li><li>가상 종가 예시에서 14일 RSI는 <mark>67.86</mark>이고, 하루 뒤 와일더 방식으로 이어 계산하면 <mark>60.84</mark>입니다.</li><li>같은 날을 단순평균으로 다시 구하면 58.62라서, 차트마다 값이 다른 이유는 평균 방식에 있습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">가상 종가 15일치로 14일 RSI 구하기</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">하루 뒤 RSI 이어 계산하기</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">평균 방식에 따라 값이 달라지는 이유</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">70과 30 구간을 읽는 관례와 한계</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">RSI를 볼 때 자주 생기는 오해</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">RSI가 투자 판단에 쓸모 있는 순간과 아닌 순간</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">RSI 확인하다 궁금해지는 점</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">가상 종가 15일치로 14일 RSI 구하기</h2>
<p>A씨가 어떤 주식의 종가를 15일 동안 적어 두었다고 가정합니다. 아래 숫자는 설명용 가상 값이며 실제 종목의 가격이 아닙니다.</p>

<p>RSI는 전날과 비교한 변화량에서 시작합니다. 오른 날은 오른 폭을 상승분에, 내린 날은 내린 폭을 하락분에 적고 반대쪽은 0으로 둡니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">일차</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">종가(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">전일 대비</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">상승분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">하락분</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">1일차</td><td style="border:1px solid #ddd;padding:8px;">10,200원</td><td style="border:1px solid #ddd;padding:8px;">+200원</td><td style="border:1px solid #ddd;padding:8px;">200</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2일차</td><td style="border:1px solid #ddd;padding:8px;">10,100원</td><td style="border:1px solid #ddd;padding:8px;">-100원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">100</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3일차</td><td style="border:1px solid #ddd;padding:8px;">10,400원</td><td style="border:1px solid #ddd;padding:8px;">+300원</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">4일차</td><td style="border:1px solid #ddd;padding:8px;">10,300원</td><td style="border:1px solid #ddd;padding:8px;">-100원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">100</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5일차</td><td style="border:1px solid #ddd;padding:8px;">10,600원</td><td style="border:1px solid #ddd;padding:8px;">+300원</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">6일차</td><td style="border:1px solid #ddd;padding:8px;">10,500원</td><td style="border:1px solid #ddd;padding:8px;">-100원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">100</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">7일차</td><td style="border:1px solid #ddd;padding:8px;">10,300원</td><td style="border:1px solid #ddd;padding:8px;">-200원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">200</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">8일차</td><td style="border:1px solid #ddd;padding:8px;">10,100원</td><td style="border:1px solid #ddd;padding:8px;">-200원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">200</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">9일차</td><td style="border:1px solid #ddd;padding:8px;">10,400원</td><td style="border:1px solid #ddd;padding:8px;">+300원</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">10일차</td><td style="border:1px solid #ddd;padding:8px;">10,700원</td><td style="border:1px solid #ddd;padding:8px;">+300원</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">11일차</td><td style="border:1px solid #ddd;padding:8px;">10,600원</td><td style="border:1px solid #ddd;padding:8px;">-100원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">100</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12일차</td><td style="border:1px solid #ddd;padding:8px;">10,900원</td><td style="border:1px solid #ddd;padding:8px;">+300원</td><td style="border:1px solid #ddd;padding:8px;">300</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">13일차</td><td style="border:1px solid #ddd;padding:8px;">10,800원</td><td style="border:1px solid #ddd;padding:8px;">-100원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">100</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">14일차</td><td style="border:1px solid #ddd;padding:8px;">11,000원</td><td style="border:1px solid #ddd;padding:8px;">+200원</td><td style="border:1px solid #ddd;padding:8px;">200</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">15일차</td><td style="border:1px solid #ddd;padding:8px;">10,700원</td><td style="border:1px solid #ddd;padding:8px;">-300원</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">300</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1~14일차 합계</td><td style="border:1px solid #ddd;padding:8px;"></td><td style="border:1px solid #ddd;padding:8px;"></td><td style="border:1px solid #ddd;padding:8px;">1,900</td><td style="border:1px solid #ddd;padding:8px;">900</td></tr>
  </tbody>
</table>

<p>1일차 변화량은 0일차 종가 10,000원이 있어야 구할 수 있어서 종가는 15개가 필요합니다. 1~14일차 14개 변화량으로 첫 평균을 냅니다.</p>

<ol style="line-height:1.9;">
  <li>평균 상승폭 = 1,900 ÷ 14 = 약 135.71원</li>
  <li>평균 하락폭 = 900 ÷ 14 = 약 64.29원</li>
  <li>RS = 135.71 ÷ 64.29 = 약 2.11</li>
  <li>RSI = 100 - 100 ÷ (1 + 2.11) = <mark>약 67.86</mark></li>
</ol>

<div style="background:#f3edfc;border:2px solid #7a4fc4;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4a2d86;font-size:18px;">📝 계산하다 막힐 때</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>내린 날의 하락분은 음수가 아니라 양수로 적습니다. -300원 하락이면 하락분은 300입니다.</li><li>평균 하락폭이 0이면 RS를 구할 수 없으니 RSI를 100으로 보고, 평균 상승폭이 0이면 RSI는 0입니다.</li></ul>
</div>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">하루 뒤 RSI 이어 계산하기</h2>
<p>15일차에 종가가 10,700원으로 300원 내렸습니다. 이 날의 상승분은 0, 하락분은 300입니다.</p>

<p>와일더 방식은 새 평균을 (전날 평균 × 13 + 오늘 값) ÷ 14로 이어 갑니다. 이 식은 <a href="https://en.wikipedia.org/wiki/Relative_strength_index" target="_blank" rel="noopener">위키백과 Relative strength index</a>와 <a href="https://help.tc2000.com/m/69404/l/747071-rsi-wilder-s-rsi" target="_blank" rel="noopener">TC2000 도움말 RSI &amp; Wilder's RSI</a>에 같은 형태로 나옵니다.</p>

<ol style="line-height:1.9;">
  <li>평균 상승폭 = (135.71 × 13 + 0) ÷ 14 = 약 126.02원</li>
  <li>평균 하락폭 = (64.29 × 13 + 300) ÷ 14 = 약 81.12원</li>
  <li>RS = 126.02 ÷ 81.12 = 약 1.55</li>
  <li>RSI = 100 - 100 ÷ (1 + 1.55) = <mark>약 60.84</mark></li>
</ol>

<p>하락분 300원 하나가 들어오자 RSI가 67.86에서 60.84로 약 7 낮아졌습니다. 오늘 값이 평균에 14분의 1만 반영되어도 하락 한 번이 RSI를 눈에 띄게 움직입니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">평균 방식에 따라 값이 달라지는 이유</h2>
<p>같은 15일차인데 평균을 어떻게 내느냐에 따라 RSI가 달라집니다. 가장 단순한 방식은 최근 14일(2~15일차)의 상승분과 하락분을 매번 새로 평균내는 것입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">와일더 방식(이어 가는 평균)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">단순평균 방식(최근 14일 새로 평균)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">평균 상승폭</td><td style="border:1px solid #ddd;padding:8px;">126.02원</td><td style="border:1px solid #ddd;padding:8px;">1,700 ÷ 14 = 121.43원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">평균 하락폭</td><td style="border:1px solid #ddd;padding:8px;">81.12원</td><td style="border:1px solid #ddd;padding:8px;">1,200 ÷ 14 = 85.71원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">RS</td><td style="border:1px solid #ddd;padding:8px;">1.55</td><td style="border:1px solid #ddd;padding:8px;">1.42</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">15일차 RSI</td><td style="border:1px solid #ddd;padding:8px;">60.84</td><td style="border:1px solid #ddd;padding:8px;">58.62</td></tr>
  </tbody>
</table>

<p>와일더 방식은 1일차 변화량이 평균에 계속 조금씩 남아 있고, 단순평균 방식은 14일이 지나면 완전히 빠집니다. 이 차이 때문에 증권사 차트, 해외 플랫폼, 직접 만든 엑셀의 값이 몇 포인트씩 어긋나는 일이 생깁니다.</p>

<p>RSI 계산 공식과 기간 설정은 <a href="https://kr.tradingview.com/support/solutions/43000502338/" target="_blank" rel="noopener">트레이딩뷰 상대강도지수(RSI) 도움말</a>에서도 확인할 수 있습니다. 쓰는 차트의 지표 설정에서 기간과 평균 방식을 먼저 열어 보세요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/rsi-meaning-14day-calculation-1.png" alt="0에서 100까지 RSI 눈금 그림. 30 이하 과매도 관례 구간, 70 이상 과매수 관례 구간 표시. 14일차 67.86, 15일차 와일더 방식 60.84, 단순평균 방식 58.62 위치 표시" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산 예시: 본문 가상 종가로 계산</figcaption></figure>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">70과 30 구간을 읽는 관례와 한계</h2>
<p>RSI 70 이상을 과매수, 30 이하를 과매도 구간으로 부르는 것이 가장 흔한 관례입니다. <a href="https://wikidocs.net/289404" target="_blank" rel="noopener">위키독스 RSI 설명</a>과 <a href="https://economybloc.com/article/117186" target="_blank" rel="noopener">이코노미블록 상대강도지수</a>도 같은 기준을 소개합니다.</p>

<p>이 기준은 해석의 관례일 뿐 앞으로 가격이 내리거나 오른다는 예측이 아닙니다. 상승세가 강한 구간에서는 RSI가 70 위에 머무는 기간이 길어질 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">RSI 값</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">숫자가 말해 주는 것</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">말해 주지 않는 것</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">70 이상</td><td style="border:1px solid #ddd;padding:8px;">최근 14일 동안 오른 폭이 내린 폭보다 컸음</td><td style="border:1px solid #ddd;padding:8px;">곧 하락한다는 예측</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">50 근처</td><td style="border:1px solid #ddd;padding:8px;">오른 폭과 내린 폭이 비슷했음</td><td style="border:1px solid #ddd;padding:8px;">가격이 적정하다는 판단</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">30 이하</td><td style="border:1px solid #ddd;padding:8px;">최근 14일 동안 내린 폭이 오른 폭보다 컸음</td><td style="border:1px solid #ddd;padding:8px;">곧 반등한다는 예측</td></tr>
  </tbody>
</table>

<div style="background:#f3edfc;border:2px solid #7a4fc4;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#4a2d86;font-size:18px;">📝 RSI를 읽을 때 기억할 점</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>RSI는 최근 14일의 등락만 요약합니다. 기업의 실적이나 가치는 담겨 있지 않습니다.</li><li>이 글의 가격과 숫자는 계산 연습용 가상 값이며 어떤 종목의 신호도 아닙니다.</li></ul>
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">RSI를 볼 때 자주 생기는 오해</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">흔한 오해</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">실제로는</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">RSI는 주가가 오른 날의 비율이다</td><td style="border:1px solid #ddd;padding:8px;">날수가 아니라 오르고 내린 금액의 크기를 비교합니다.</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">RSI 50이면 가격이 중간이다</td><td style="border:1px solid #ddd;padding:8px;">최근 14일간 상승폭과 하락폭이 비슷하다는 뜻일 뿐 가격 수준과는 무관합니다.</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">모든 차트의 RSI는 같다</td><td style="border:1px solid #ddd;padding:8px;">기간과 평균 방식에 따라 값이 달라집니다.</td></tr>
  </tbody>
</table>

<p>이동평균과 표준편차로 만드는 다른 보조지표가 궁금하다면 <a href="https://sensitiveboss3.tistory.com/entry/bollinger-bands-calculation" target="_blank" rel="noopener">볼린저밴드 뜻과 계산법</a>을 함께 보세요. 두 지표 모두 과거 가격에서 계산한 값이라는 점은 같습니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">RSI가 투자 판단에 쓸모 있는 순간과 아닌 순간</h2>

<p>RSI는 최근 등락의 크기를 비교하는 도구라서, 쓰는 자리를 가려야 도움이 됩니다.</p>

<ul style="line-height:1.9;">
  <li><strong>쓸모 있는 순간:</strong> 같은 종목의 지금 등락이 평소보다 한쪽으로 얼마나 쏠렸는지 비교할 때, 그리고 가격은 새 고점인데 RSI는 이전 고점보다 낮은 것처럼 가격과 지표가 엇갈리는 모습을 찾을 때 쓰입니다.</li>
  <li><strong>쓸모가 적은 순간:</strong> 실적 발표나 공시처럼 회사 가치가 바뀌는 사건이 있을 때입니다. RSI에는 그런 정보가 들어 있지 않습니다.</li>
  <li><strong>착시가 생기는 순간:</strong> 급락 뒤 RSI가 30 아래로 내려가면 반등 신호처럼 보이지만, 짧게 튀었다가 다시 내리는 경우도 흔합니다. 이런 움직임은 <a href="https://sensitiveboss3.tistory.com/entry/dead-cat-bounce-meaning" target="_blank" rel="noopener">데드캣 바운스 뜻 글</a>에서 따로 다뤘습니다.</li>
</ul>

<p>RSI 숫자 하나로 매수나 매도를 정하는 방식은 일반적인 사용법이 아닙니다. 이동평균이나 거래량, 그리고 기업 실적과 같이 놓고 읽는 보조 자료입니다.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #7a4fc4;padding-left:12px;margin-top:36px;">RSI 확인하다 궁금해지는 점</h2>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">RSI는 몇 일 기준으로 보는 게 맞나요</summary>
  <p style="margin:10px 0 0 0;">정해진 정답은 없고 14일이 기본값입니다. 개발자 웰스 와일더가 1978년에 14일을 표준으로 제안했고 대부분의 차트 서비스가 이 값을 초기 설정으로 둡니다. 기간을 줄이면 값이 더 크게 출렁이고, 늘리면 완만해집니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">RSI가 70을 넘으면 팔아야 하나요</summary>
  <p style="margin:10px 0 0 0;">그렇게 단정할 수 없습니다. 70 이상은 최근 14일 동안 오른 폭이 내린 폭보다 훨씬 컸다는 뜻이고, 앞으로의 방향을 알려 주는 값이 아닙니다. 강한 추세에서는 RSI가 과매수나 과매도 구간에 오래 머물 수 있습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">같은 종목인데 증권사마다 RSI 값이 다른 이유가 있나요</summary>
  <p style="margin:10px 0 0 0;">평균을 내는 방식이 다르면 값이 달라집니다. 이 글의 계산에서 15일차 값이 와일더 방식 60.84, 단순평균 방식 58.62로 갈렸습니다. 차트 설정에서 기간과 평균 방식을 확인하면 대부분 설명됩니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">RSI가 0이나 100이 되는 경우도 있나요</summary>
  <p style="margin:10px 0 0 0;">있습니다. 기간 안에 하락한 날이 하나도 없으면 평균 하락폭이 0이라 RSI는 100이 되고, 반대로 상승한 날이 없으면 0이 됩니다. 이때 RS 식의 분모가 0이 되므로 공식에 바로 넣지 말고 이 두 경우를 따로 처리합니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주가가 아니라 거래량이나 지수에도 RSI를 쓸 수 있나요</summary>
  <p style="margin:10px 0 0 0;">가격처럼 변화량을 계산할 수 있는 숫자라면 같은 식을 적용할 수 있습니다. 주가 지수, ETF, 환율 차트에도 흔히 붙어 있습니다. 대상이 달라지면 70과 30이라는 관례적 구간의 의미도 달라질 수 있습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">RSI 하나만 보고 판단해도 되나요</summary>
  <p style="margin:10px 0 0 0;">한 지표만으로 결론을 내리지 않는 것이 일반적인 사용법입니다. RSI는 최근 등락의 상대적 크기만 요약하므로 거래량이나 이동평균 같은 다른 정보와 함께 읽는 경우가 많습니다. 어떤 값이든 매수나 매도의 근거로 확정할 수는 없습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://en.wikipedia.org/wiki/Relative_strength_index" target="_blank" rel="noopener">위키백과 Relative strength index</a></li>
    <li><a href="https://help.tc2000.com/m/69404/l/747071-rsi-wilder-s-rsi" target="_blank" rel="noopener">TC2000 도움말 RSI &amp; Wilder's RSI</a></li>
    <li><a href="https://kr.tradingview.com/support/solutions/43000502338/" target="_blank" rel="noopener">트레이딩뷰 상대강도지수(RSI) 도움말</a></li>
    <li><a href="https://wikidocs.net/289404" target="_blank" rel="noopener">위키독스 RSI 차트를 분석하다 with 트레이딩뷰</a></li>
    <li><a href="https://economybloc.com/article/117186" target="_blank" rel="noopener">이코노미블록 상대강도지수(RSI)</a></li>
    <li><a href="https://www.digitaltoday.co.kr/news/articleView.html?idxno=400109" target="_blank" rel="noopener">디지털투데이 디지털피디아 상대강도지수(RSI)</a></li>
  </ul>
  기준일: 2026년 10월 기준. 가격과 계산 예시는 이해를 돕기 위한 가상의 숫자이며 실제 종목의 값이 아닙니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 보조지표의 계산 원리를 설명하는 정보 글이며, 특정 종목이나 상품을 사거나 팔도록 권하지 않습니다. 지표 값은 과거 가격에서 나온 숫자라서 앞날을 보장하지 않습니다. 투자 판단과 그에 따른 결과는 투자자 본인의 몫입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "RSI 뜻과 14일 값 직접 구하기",
  "description": "RSI가 무엇인지, 가상 종가 15일치로 14일 RSI를 직접 계산하고 와일더 방식과 단순평균 방식의 값 차이, 70과 30 구간의 한계를 정리했습니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-01",
  "dateModified": "2026-10-02",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/rsi-meaning-14day-calculation"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/rsi-meaning-14day-calculation-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "RSI는 몇 일 기준으로 보는 게 맞나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 정답은 없고 14일이 기본값입니다. 개발자 웰스 와일더가 1978년에 14일을 표준으로 제안했고 대부분의 차트 서비스가 이 값을 초기 설정으로 둡니다. 기간을 줄이면 값이 더 크게 출렁이고, 늘리면 완만해집니다."
      }
    },
    {
      "@type": "Question",
      "name": "RSI가 70을 넘으면 팔아야 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "그렇게 단정할 수 없습니다. 70 이상은 최근 14일 동안 오른 폭이 내린 폭보다 훨씬 컸다는 뜻이고, 앞으로의 방향을 알려 주는 값이 아닙니다. 강한 추세에서는 RSI가 과매수나 과매도 구간에 오래 머물 수 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "같은 종목인데 증권사마다 RSI 값이 다른 이유가 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "평균을 내는 방식이 다르면 값이 달라집니다. 이 글의 계산에서 15일차 값이 와일더 방식 60.84, 단순평균 방식 58.62로 갈렸습니다. 차트 설정에서 기간과 평균 방식을 확인하면 대부분 설명됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "RSI가 0이나 100이 되는 경우도 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "있습니다. 기간 안에 하락한 날이 하나도 없으면 평균 하락폭이 0이라 RSI는 100이 되고, 반대로 상승한 날이 없으면 0이 됩니다. 이때 RS 식의 분모가 0이 되므로 공식에 바로 넣지 말고 이 두 경우를 따로 처리합니다."
      }
    },
    {
      "@type": "Question",
      "name": "주가가 아니라 거래량이나 지수에도 RSI를 쓸 수 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "가격처럼 변화량을 계산할 수 있는 숫자라면 같은 식을 적용할 수 있습니다. 주가 지수, ETF, 환율 차트에도 흔히 붙어 있습니다. 대상이 달라지면 70과 30이라는 관례적 구간의 의미도 달라질 수 있습니다."
      }
    },
    {
      "@type": "Question",
      "name": "RSI 하나만 보고 판단해도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "한 지표만으로 결론을 내리지 않는 것이 일반적인 사용법입니다. RSI는 최근 등락의 상대적 크기만 요약하므로 거래량이나 이동평균 같은 다른 정보와 함께 읽는 경우가 많습니다. 어떤 값이든 매수나 매도의 근거로 확정할 수는 없습니다."
      }
    }
  ]
}
</script>
