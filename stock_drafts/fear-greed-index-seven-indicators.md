---
keyword: 공포탐욕지수
title: 공포탐욕지수 7개 지표와 점수 계산 구조
slug: fear-greed-index-seven-indicators
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 3520 (PC 870 / 모바일 2650, 2026-10-02 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-02 - 통과]
  WebSearch "공포탐욕지수 뜻 보는 법" 상위: kbthink.com 2건(KB금융 콘텐츠), danbinews.com(언론), coinglass.com·blockstreet.co.kr(가상자산 지수 서비스), uppity.co.kr(소규모 콘텐츠), dic.hankyung.com(용어사전), indexergo.com(지표 조회), frism.io(소규모 블로그).
  1) 진입 여지: 있음. uppity, frism 등 소규모 콘텐츠 사이트가 상위에 섞여 있다.
  2) 검색 의도: 뜻과 보는 법을 찾는 탐색형이 중심이나, 현재 점수 조회 의도가 일부 섞여 있다(coinglass, indexergo). 지배적이지는 않다.
  3) 답 완결 여부: 부분적. 상위 요약은 정의, 7개 지표 이름, 구간 해석 중심이었다. 일곱 점수를 평균하는 계산 예시, 평균이 같아도 구성이 다른 두 시장 비교, 구간 경계가 소개마다 다르다는 점의 비교표는 요약 단계에서 확인하지 못했다. 상위 페이지 본문 전체는 열어보지 못했다(자동화 세션 제약).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 일곱 점수(70·55·60·40·60·25·40) 평균 50.0 계산과 막대그래프 1장.
  (b) 같은 평균 50에서 구성이 다른 두 시장(갈림형 편차 45점 / 잠잠형 0점) 비교표, 지표 14점 변화가 종합 2점으로 나타나는 민감도 계산.
  (c) 일곱 지표 비교 대상·공포 신호·탐욕 신호 표, 20점 단위/25점 단위 구간표 비교.
primary_source: |
  1차 출처인 CNN Business 공포탐욕지수 페이지(cnn.com/markets/fear-and-greed) WebFetch 1회 EGRESS_BLOCKED.
  WebSearch 3회로 독립 출처를 교차 확인했다: 7개 지표 이름과 동일 가중 평균, 0~100 척도, 50 중립은 SoFi·NerdWallet·expobusiness·investingnews·macromicro 등 해외 소개 글과 KB Think·한경 용어사전·단비뉴스·KB자산운용 해설(검색 요약 단계 확인, 본문 미열람)에서 일치. 시장 모멘텀 125일 이동평균, 52주 신고가/신저가, 정크본드 금리 차, VIX, 주식 대비 국채 수익률도 일치. 구간 경계는 20점 단위(국내 해설)와 25점 단위(해외 소개)로 출처 간 상이해 본문에서 두 방식을 나란히 제시했다. 각 지표의 0~100점 환산 방식은 공개 자료에서 확인되지 않아 본문에 단정하지 않았다.
기준일: 2026년 10월 기준 (계산 예시는 전부 가상)
refresh_due: 2026-10-30
tags: 공포탐욕지수, 공포탐욕지수 뜻, CNN 공포탐욕지수, Fear and Greed Index, 투자심리지수, 시장 심리 지표, VIX, 풋콜비율, 정크본드, 미국 증시
gate_pass: false
gate_pass_note: |
  게이트1 3,520회, 게이트2 v3 통과, 게이트3 계산 예시·비교표 확보. 게이트4 미충족: CNN 원문 접속 불가이고 현재 수치 표(규칙: 지표 글은 현재 값 필수)를 채울 수 없다. 구조 설명은 독립 출처 다수가 일치해 교차검증 수준이다.
  사람이 할 일: capture_guide 참고. 현재 점수 캡처를 올려 주시면 본문 "현재 점수를 확인하는 곳" 표를 채우고 gate_pass를 true로 바꿀 수 있습니다.
capture_guide: |
  (1) 왜 필요한가: 지표 글에는 현재 수치 표가 필수인데, 자동화 세션에서 CNN 페이지가 차단돼 현재 점수·등급·기준 시점을 얻지 못했습니다. 구간 이름도 CNN 표기 기준으로 확정하고 싶습니다.
  (2) 방법 1순위: https://www.cnn.com/markets/fear-and-greed 접속, 화면 맨 위의 게이지(현재 점수와 등급 문구)와 그 아래 "Fear &amp; Greed Over Time" 또는 이전 시점 값이 나온 부분이 한 화면에 보이게 캡처. 2순위: 같은 페이지의 일곱 지표 설명 영역(각 지표 이름과 Fear/Greed 라벨)을 캡처.
  (3) 캡처 후 "스크린샷을 대화에 올려주세요". 올려 주시면 현재 수치 표와 구간 설명을 CNN 표기에 맞춰 수정합니다.
self_check: |
  [2026-10-02 gate_pass:false, 현재 수치 표 미기입 + 1차 출처 미열람]
  후보 경위: backlog.verified에 단순 순서 대기 후보 없음. 신규 8개 실측: 공포탐욕지수 3,520 PASS / 빅테크 뜻 1,570 PASS / 인덱스펀드 뜻 1,560 PASS / 금리인상 주식 350·분할매수 뜻 140·스윙 투자 뜻 80·롱숏 전략 뜻 20·배당귀족주 뜻 20 FAIL. 최고 검색량인 공포탐욕지수 채택. 나머지 PASS 2개는 다음 편 후보로 backlog.verified 기록.
  카니벌라이제이션: 92편(VIX)은 일곱 지표 중 하나만 다루고 공포탐욕지수 단어는 기존 초안 전체에서 0건(grep). 본문에서 92·105·98편으로 내부 링크(전부 발행 완료).
  YMYL: 종목 추천·목표가·매매시점 없음. 극단 구간을 매수·매도 신호로 제시하지 않고 방향 단정 대신 단정할 수 없는 이유(지표 구조)와 함께 볼 지표를 적었다.
  제목 "공포탐욕지수 7개 지표와 점수 계산 구조" 20자, 금지어 없음, "뜻과 계산 방법" 틀 대신 "7개 지표와 점수 계산 구조". 슬러그 5단어.
  첫 문장 유형: 절차형(직전 118 대비형, 117 수치충격형, 116 문제제기형, 115 정의형과 다름). 인트로 둘째 문장에 척도(0~100, 50 중립) 답 포함, 메타 문장 없음.
  글 구조 유형: 계산형(목차 직후 첫 H2의 첫 블록이 계산 박스, 설명 문단보다 먼저). 직전 118 비교형, 117 절차형, 116 개념형, 115 계산형이라 연속 아님.
  어투 모드: C 사례형(가상 인물 B씨, 가상임을 명시, 합쇼체). 직전 118 A, 117 B와 다름. 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 2회, mark 밀도 3개, FAQ 5개(직전 118 6·117 4와 다름), 본문 H2 6개 중 "~나요"형 1개. 요약박스 청록(#eaf7f6/#2a9d8f), 제목 "🧭 점수를 읽기 전에", 마무리 박스 "✅ 챙겨 둘 읽기 순서". FAQ 헤딩 "공포탐욕지수 얘기에 따라붙는 의문들". 면책 문구 새 표현.
  기관 링크: 외부 안내 문장·출처 목록 CNN·KB Think·한경 용어사전 전부 링크 처리. 내부 링크 3개. 그림 1장(가상 일곱 점수 막대그래프).
  발행 글 갱신(refresh): lint_draft --due에 92·98·105편이 현재 수치 부재로 기한 도달. 현재 값을 1차 출처로 확인할 수 없어 이번 실행에서는 갱신하지 않음.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>공포탐욕지수를 읽으려면 이 숫자가 일곱 개 점수의 평균이라는 것부터 알아야 합니다. CNN이 공개하는 0~100점 지표로, 0에 가까울수록 극단적 공포, 100에 가까울수록 극단적 탐욕, 50은 중립으로 봅니다.</p>

<div style="background:#eaf7f6;border:2px solid #2a9d8f;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#17615a;font-size:18px;">🧭 점수를 읽기 전에</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>종합 점수는 시장 모멘텀, 주가 강도, 주가 폭, 풋·콜 옵션, 정크본드 수요, 시장 변동성, 안전자산 수요 일곱 가지의 <mark>동일 가중 평균</mark>입니다.</li><li>지표 하나가 14점 움직이면 종합 점수는 2점 움직입니다.</li><li>평균이 같은 50이어도 일곱 점수가 섞여 있는지, 모두 50 근처인지는 전혀 다른 상황입니다.</li><li>이 지수는 미국 시장 기준이라 코스피나 코인 공포탐욕지수와 다른 지표입니다.</li></ul>
</div>

<h2 style="border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">종합 점수는 일곱 점수의 평균입니다</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">일곱 지표가 각각 재는 것</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">점수 구간은 어디서 끊어 읽나요</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 왜 중요한가</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">VIX와의 차이와 이 지수의 한계</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">현재 점수를 확인하는 곳</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">종합 점수는 일곱 점수의 평균입니다</h2>

<div style="background:#f5fbfa;border:1px solid #9fd6d0;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>계산 박스 (가상 데이터)</strong>
  <ol style="margin:8px 0 0 0;padding-left:20px;line-height:1.8;"><li>일곱 지표를 각각 0~100점으로 바꿉니다. 이 예시의 점수는 70, 55, 60, 40, 60, 25, 40입니다.</li><li>일곱 점수를 모두 더하면 350입니다.</li><li>350 ÷ 7 = 50.0이 종합 점수이고, 50이라 중립으로 읽습니다.</li></ol>
</div>

<p>직장인 B씨(가상 인물)가 종합 점수 50을 보고 "오늘 시장은 평온하네"라고 생각했다고 해 보겠습니다. 그런데 점수를 풀어 보면 평온과는 거리가 멉니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/fear-greed-index-seven-indicators-1.png" alt="가상 예시 막대그래프. 시장 모멘텀 70, 주가 강도 55, 주가 폭 60, 풋·콜 옵션 40, 정크본드 수요 60, 시장 변동성 25, 안전자산 수요 40이고 평균은 350을 7로 나눈 50.0" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">설명용 가상 수치. 실제 지수 값이 아닙니다.</figcaption></figure>

<p>주가 흐름 쪽 지표는 탐욕 방향이고, 변동성은 25점으로 공포 쪽에 가깝습니다. 평균은 이 차이를 지워 버립니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">같은 종합 점수 50, 다른 두 시장 (가상)</caption>
  <thead>
    <tr style="background:#eaf7f6;"><th style="border:1px solid #ddd;padding:8px;">구분</th><th style="border:1px solid #ddd;padding:8px;">일곱 점수</th><th style="border:1px solid #ddd;padding:8px;">평균</th><th style="border:1px solid #ddd;padding:8px;">최고점과 최저점의 차</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">시장 갈림형</td><td style="border:1px solid #ddd;padding:8px;">70 · 55 · 60 · 40 · 60 · 25 · 40</td><td style="border:1px solid #ddd;padding:8px;">50.0</td><td style="border:1px solid #ddd;padding:8px;">45점 (70과 25)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">시장 잠잠형</td><td style="border:1px solid #ddd;padding:8px;">50 · 50 · 50 · 50 · 50 · 50 · 50</td><td style="border:1px solid #ddd;padding:8px;">50.0</td><td style="border:1px solid #ddd;padding:8px;">0점</td></tr>
  </tbody>
</table>

<p>일곱 지표의 비중이 같다는 점은 계산을 단순하게 만듭니다. 변동성 점수가 25에서 39로 14점 오르면 합계가 364가 되어 364 ÷ 7 = 52.0, 종합 점수는 2점 오를 뿐입니다.</p>

<p>다만 각 지표를 0~100점으로 환산하는 세부 방식은 공개 자료에서 확인되지 않습니다. 그래서 이 글의 점수는 구조를 설명하기 위한 값이고 CNN의 실제 환산값이 아닙니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">일곱 지표가 각각 재는 것</h2>

<p>일곱 지표는 주가 흐름, 옵션 시장, 채권 시장 세 곳에서 가져옵니다. 표에서 공포 쪽과 탐욕 쪽 신호가 무엇인지 나란히 봅니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">공포탐욕지수 일곱 지표 (CNN 공개 설명을 교차 확인한 요약)</caption>
  <thead>
    <tr style="background:#eaf7f6;"><th style="border:1px solid #ddd;padding:8px;">지표</th><th style="border:1px solid #ddd;padding:8px;">무엇을 비교하나</th><th style="border:1px solid #ddd;padding:8px;">공포 쪽 신호</th><th style="border:1px solid #ddd;padding:8px;">탐욕 쪽 신호</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">시장 모멘텀</td><td style="border:1px solid #ddd;padding:8px;">S&amp;P500 지수와 125일 이동평균</td><td style="border:1px solid #ddd;padding:8px;">지수가 평균보다 아래</td><td style="border:1px solid #ddd;padding:8px;">지수가 평균보다 위</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">주가 강도</td><td style="border:1px solid #ddd;padding:8px;">52주 신고가 종목 수와 신저가 종목 수</td><td style="border:1px solid #ddd;padding:8px;">신저가 종목이 더 많음</td><td style="border:1px solid #ddd;padding:8px;">신고가 종목이 더 많음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">주가 폭</td><td style="border:1px solid #ddd;padding:8px;">상승 종목 거래량과 하락 종목 거래량</td><td style="border:1px solid #ddd;padding:8px;">하락 종목 거래량이 우세</td><td style="border:1px solid #ddd;padding:8px;">상승 종목 거래량이 우세</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">풋·콜 옵션</td><td style="border:1px solid #ddd;padding:8px;">하락 베팅인 풋과 상승 베팅인 콜의 비율</td><td style="border:1px solid #ddd;padding:8px;">풋 비중이 높음</td><td style="border:1px solid #ddd;padding:8px;">콜 비중이 높음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">정크본드 수요</td><td style="border:1px solid #ddd;padding:8px;">투자등급 채권과 정크본드의 금리 차</td><td style="border:1px solid #ddd;padding:8px;">금리 차가 벌어짐</td><td style="border:1px solid #ddd;padding:8px;">금리 차가 좁아짐</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">시장 변동성</td><td style="border:1px solid #ddd;padding:8px;">VIX 지수</td><td style="border:1px solid #ddd;padding:8px;">VIX가 높음</td><td style="border:1px solid #ddd;padding:8px;">VIX가 낮음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">안전자산 수요</td><td style="border:1px solid #ddd;padding:8px;">주식 수익률과 국채 수익률</td><td style="border:1px solid #ddd;padding:8px;">국채가 더 나은 성과</td><td style="border:1px solid #ddd;padding:8px;">주식이 더 나은 성과</td></tr>
  </tbody>
</table>

<p>표 위쪽 세 지표(모멘텀·강도·폭)는 주가 자체에서 계산됩니다. 그래서 주가가 크게 움직이는 날에는 세 점수가 함께 움직이기 쉽습니다.</p>

<ul>
  <li>시장 변동성에 쓰이는 VIX는 <a href="https://sensitiveboss3.tistory.com/entry/vix-index-meaning-calculation" target="_blank" rel="noopener">VIX 지수 글</a>에서 계산 구조까지 풀어 두었습니다.</li>
  <li>안전자산 수요와 정크본드 수요는 국채·회사채 금리와 이어지므로 <a href="https://sensitiveboss3.tistory.com/entry/government-bond-yield-meaning" target="_blank" rel="noopener">국채금리 글</a>이 배경 설명이 됩니다.</li>
</ul>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">점수 구간은 어디서 끊어 읽나요</h2>

<p>50이 중립이라는 점만 모든 소개 자료가 같고, 중간 구간의 경계는 소개마다 다릅니다. 국내 해설 중에는 20점 단위 다섯 구간으로 설명하는 곳이 있고, 해외 소개 글에는 25점 단위 네 구간이 흔합니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">구간 구분의 두 가지 소개 방식</caption>
  <thead>
    <tr style="background:#eaf7f6;"><th style="border:1px solid #ddd;padding:8px;">점수</th><th style="border:1px solid #ddd;padding:8px;">20점 단위로 설명하는 경우</th><th style="border:1px solid #ddd;padding:8px;">25점 단위로 설명하는 경우</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">0~19</td><td style="border:1px solid #ddd;padding:8px;">매우 공포</td><td style="border:1px solid #ddd;padding:8px;">극단적 공포 (0~24)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">20~24</td><td style="border:1px solid #ddd;padding:8px;">공포</td><td style="border:1px solid #ddd;padding:8px;">극단적 공포</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">25~39</td><td style="border:1px solid #ddd;padding:8px;">공포</td><td style="border:1px solid #ddd;padding:8px;">공포 (25~49)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">40~49</td><td style="border:1px solid #ddd;padding:8px;">중립</td><td style="border:1px solid #ddd;padding:8px;">공포</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">50~59</td><td style="border:1px solid #ddd;padding:8px;">중립</td><td style="border:1px solid #ddd;padding:8px;">탐욕 (50~74)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">60~74</td><td style="border:1px solid #ddd;padding:8px;">탐욕</td><td style="border:1px solid #ddd;padding:8px;">탐욕</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">75~79</td><td style="border:1px solid #ddd;padding:8px;">탐욕</td><td style="border:1px solid #ddd;padding:8px;">극단적 탐욕 (75~100)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">80~100</td><td style="border:1px solid #ddd;padding:8px;">매우 탐욕</td><td style="border:1px solid #ddd;padding:8px;">극단적 탐욕</td></tr>
  </tbody>
</table>

<p>같은 점수가 어떤 설명에서는 중립이고 다른 설명에서는 공포입니다. 점수를 인용할 때는 <mark>어느 구간표를 쓴 해설인지</mark>를 함께 보는 편이 정확합니다. 등급 이름은 <a href="https://www.cnn.com/markets/fear-and-greed" target="_blank" rel="noopener">CNN 공포탐욕지수 페이지</a>에 표시된 것을 기준으로 삼으면 됩니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">주식 투자자에게 왜 중요한가</h2>

<p>이 지수는 시장 분위기를 한 숫자로 압축해 보여 주는 보조 지표라서, 지금 시장이 어느 쪽으로 쏠려 있는지 가늠하는 데 쓰입니다. 주가가 이미 많이 오른 탐욕 구간에서는 작은 악재에도 흔들릴 여지가 크다고 보는 시각이 있고, 극단적 공포 구간은 팔 사람이 상당히 팔고 난 뒤라고 보는 시각이 있습니다.</p>

<p>일곱 지표가 주식 시장에 닿는 경로는 대략 이렇습니다.</p>

<ul>
  <li>변동성이 오르면 위험 한도를 줄이려는 투자자가 늘어 주식 매도 압력이 커질 수 있습니다.</li>
  <li>정크본드 금리 차가 벌어지면 신용도가 낮은 기업의 자금 조달 비용이 올라 경기에 민감한 업종의 실적 우려로 이어질 수 있습니다.</li>
  <li>국채를 찾는 수요가 늘면 국채 가격이 오르고 금리는 내려, 성장주 할인율 부담이 줄어드는 쪽과 경기 둔화를 읽는 쪽이 엇갈립니다.</li>
</ul>

<p>다만 극단 구간이 곧 반등이나 하락을 뜻한다고 단정할 수는 없습니다. <mark>점수는 분위기를 보여 줄 뿐 다음 방향을 알려 주지 않기</mark> 때문입니다.</p>

<ul>
  <li>일곱 지표 중 세 개가 주가 자체에서 나오므로, 주가가 내리는 동안은 공포 점수가 자연스럽게 낮아집니다.</li>
  <li>공포 구간이 길게 이어진 시기도 있어서 낮은 점수가 바닥의 증거는 아닙니다.</li>
  <li>함께 볼 만한 것은 VIX 수준, 국채금리 방향, 달러 흐름입니다. 달러 쪽은 <a href="https://sensitiveboss3.tistory.com/entry/dollar-index-meaning-currency-weights" target="_blank" rel="noopener">달러인덱스 글</a>이 이어집니다.</li>
</ul>

<div style="background:#f5fbfa;border:1px solid #9fd6d0;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>📎 읽을 때 기억할 점</strong>
  <p style="margin:8px 0 0 0;">이 점수에는 특정 종목의 사고팔 시점이 담겨 있지 않습니다. 매매 판단과 그 결과는 투자자 본인의 몫입니다.</p>
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">VIX와의 차이와 이 지수의 한계</h2>

<p>VIX는 공포탐욕지수를 이루는 일곱 지표 중 하나입니다. 공포탐욕지수는 VIX에 주가 흐름, 옵션, 채권 지표를 더해 종합한 값입니다.</p>

<ul>
  <li>VIX는 옵션 가격에서 나온 기대 변동성 하나만 봅니다.</li>
  <li>공포탐욕지수는 VIX를 포함해 서로 다른 시장의 신호 일곱 가지를 평균냅니다.</li>
  <li>그래서 VIX가 낮아도 다른 지표가 나쁘면 종합 점수는 중립 근처로 내려옵니다.</li>
</ul>

<p>이 지수에는 분명한 한계도 있습니다.</p>

<ul>
  <li>미국 시장 기준입니다. S&amp;P500과 뉴욕증권거래소 데이터를 쓰므로 한국 시장에 그대로 옮기기 어렵습니다.</li>
  <li>평균이라서 지표 사이의 엇갈림이 가려집니다.</li>
  <li>환산 방식이 일부 비공개라 직접 재현할 수 없습니다.</li>
  <li>매일 바뀌는 숫자라 하루 변화에 의미를 부여하기 어렵습니다.</li>
</ul>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">현재 점수를 확인하는 곳</h2>

<p>현재 점수와 등급은 <a href="https://www.cnn.com/markets/fear-and-greed" target="_blank" rel="noopener">CNN Business의 Fear &amp; Greed Index 페이지</a>에서 볼 수 있고, 미국 시장 거래일에 맞춰 갱신됩니다. 아래 표는 이 글을 게시할 때 그 페이지의 값을 옮겨 적는 자리입니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">공포탐욕지수 현재 수치</caption>
  <thead>
    <tr style="background:#eaf7f6;"><th style="border:1px solid #ddd;padding:8px;">항목</th><th style="border:1px solid #ddd;padding:8px;">값</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">현재 점수 (0~100)</td><td style="border:1px solid #ddd;padding:8px;">게시 전 기입</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">등급 표기</td><td style="border:1px solid #ddd;padding:8px;">게시 전 기입</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">기준 시점</td><td style="border:1px solid #ddd;padding:8px;">게시 전 기입 (미국 동부시간)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">발표처</td><td style="border:1px solid #ddd;padding:8px;">CNN Business</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">다음 갱신</td><td style="border:1px solid #ddd;padding:8px;">미국 시장 다음 거래일</td></tr>
  </tbody>
</table>

<div style="background:#eaf7f6;border:2px solid #2a9d8f;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#17615a;font-size:18px;">✅ 챙겨 둘 읽기 순서</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>종합 점수를 본 다음, 일곱 지표 중 어느 쪽이 점수를 끌어올리고 내리는지 분해해서 봅니다.</li><li>구간 이름은 CNN 페이지의 표기를 따르고, 다른 해설과 경계가 다를 수 있음을 염두에 둡니다.</li><li>극단 구간이어도 방향 신호로 쓰지 않고 분위기 확인용으로만 씁니다.</li></ul>
</div>

<h2 style="border-left:6px solid #2a9d8f;padding-left:12px;margin-top:36px;">공포탐욕지수 얘기에 따라붙는 의문들</h2>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">점수가 높을수록 좋은 건가요?</summary><p>좋고 나쁨을 나타내는 점수가 아닙니다. 0에 가까우면 시장 분위기가 극단적 공포 쪽, 100에 가까우면 극단적 탐욕 쪽이라는 상태 설명일 뿐입니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">점수가 50이면 시장이 안정적인 건가요?</summary><p>그렇게 단정할 수 없습니다. 이 글의 가상 예시처럼 높은 점수와 낮은 점수가 섞여 평균만 50이 될 수 있어서, 일곱 지표를 따로 봐야 합니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">극단적 공포 구간이면 주가가 오르나요?</summary><p>오른다고 말할 수 없습니다. 공포 구간에서 반등한 때도 있고 공포가 더 깊어진 때도 있어서, 점수는 지금의 분위기를 보여 줄 뿐 다음 방향을 알려 주지 않습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">일곱 지표를 직접 계산해서 CNN 점수를 만들 수 있나요?</summary><p>똑같이 재현하기는 어렵습니다. 지표별 원자료는 찾을 수 있어도 0~100점으로 바꾸는 세부 방식이 공개 자료에서 확인되지 않기 때문입니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">코스피나 코인에도 같은 공포탐욕지수가 있나요?</summary><p>이름은 같아도 별개의 지수입니다. 코스피용과 가상자산용 공포탐욕지수는 각각 다른 구성과 산출 방식을 쓰고, 이 글에서 다룬 것은 미국 주식시장 기준의 CNN 지수입니다.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, 일곱 지표 구성과 동일 가중 방식은 아래 자료를 교차해 정리했습니다):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.cnn.com/markets/fear-and-greed" target="_blank" rel="noopener">CNN Business - Fear &amp; Greed Index</a></li>
    <li><a href="https://kbthink.com/us-economy/fear-and-greed-index.html" target="_blank" rel="noopener">KB Think - 공포 탐욕 지수</a></li>
    <li><a href="https://dic.hankyung.com/economy/view/?seq=15903" target="_blank" rel="noopener">한경 용어사전 - 공포탐욕지수</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 공포탐욕지수의 구조를 설명하는 정보성 글이며, 특정 종목이나 상품을 사고팔라고 권하지 않습니다. 본문의 점수와 평균은 구조 설명을 위한 가상 값입니다. 투자 판단과 그 결과는 투자자 본인에게 있고, 지수의 구성과 구간 표기는 제공처 사정에 따라 바뀔 수 있습니다.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "공포탐욕지수 7개 지표와 점수 계산 구조",
  "description": "공포탐욕지수가 일곱 지표의 동일 가중 평균으로 만들어지는 구조를 가상 예시로 계산하고, 지표별 의미와 구간 해석의 차이, 한계를 정리했습니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/fear-greed-index-seven-indicators"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/fear-greed-index-seven-indicators-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "점수가 높을수록 좋은 건가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "좋고 나쁨을 나타내는 점수가 아닙니다. 0에 가까우면 시장 분위기가 극단적 공포 쪽, 100에 가까우면 극단적 탐욕 쪽이라는 상태 설명일 뿐입니다."
      }
    },
    {
      "@type": "Question",
      "name": "점수가 50이면 시장이 안정적인 건가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "그렇게 단정할 수 없습니다. 이 글의 가상 예시처럼 높은 점수와 낮은 점수가 섞여 평균만 50이 될 수 있어서, 일곱 지표를 따로 봐야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "극단적 공포 구간이면 주가가 오르나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "오른다고 말할 수 없습니다. 공포 구간에서 반등한 때도 있고 공포가 더 깊어진 때도 있어서, 점수는 지금의 분위기를 보여 줄 뿐 다음 방향을 알려 주지 않습니다."
      }
    },
    {
      "@type": "Question",
      "name": "일곱 지표를 직접 계산해서 CNN 점수를 만들 수 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "똑같이 재현하기는 어렵습니다. 지표별 원자료는 찾을 수 있어도 0~100점으로 바꾸는 세부 방식이 공개 자료에서 확인되지 않기 때문입니다."
      }
    },
    {
      "@type": "Question",
      "name": "코스피나 코인에도 같은 공포탐욕지수가 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이름은 같아도 별개의 지수입니다. 코스피용과 가상자산용 공포탐욕지수는 각각 다른 구성과 산출 방식을 쓰고, 이 글에서 다룬 것은 미국 주식시장 기준의 CNN 지수입니다."
      }
    }
  ]
}
</script>
