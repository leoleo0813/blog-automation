---
keyword: 스태그플레이션
title: 스태그플레이션 판별 3지표와 1970년대 사례
slug: stagflation-three-indicators-1970s
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 5590 (PC 1210 / 모바일 4380)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-01 - 통과]
  WebSearch "스태그플레이션 뜻 1970년대 오일쇼크 물가상승률 실업률 미국 한국 사례" 상위 9개: ko.wikipedia.org(백과), sgsg.hankyung.com(언론), krihs.re.kr(국책연구기관 PDF), sisajournal.com(언론), naeiledu.co.kr(교육 소규모 사이트), economychosun.com(언론), nowdaylab.com(소규모 콘텐츠), arxiv.org(무관).
  1) 진입 여지: 있음. naeiledu.co.kr, nowdaylab.com 같은 소규모 콘텐츠 사이트가 상위에 있다.
  2) 검색 의도: 뜻과 사례를 찾는 탐색형. 조회·계산기 실행 의도 아님.
  3) 답 완결 여부: 부분적. 상위는 정의와 1970년대 서술 중심이고, 물가·성장률·실업률 3지표를 한 표로 놓고 "지금 상황을 직접 판별하는 순서"를 안내한 글은 검색 요약 단계에서 확인하지 못했다(본문 전체는 열지 못함).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 물가·성장률 조합 4분면 비교표(과열 / 스태그플레이션 / 골디락스 / 디플레이션형).
  (b) 한국·미국 1970~80년대 물가·실업률 연도별 표(ECOS·FRED 원자료로 채움).
  (c) 현재 상황을 직접 판별하는 3지표 확인 순서와 출처별 확인 위치.
primary_source: |
  연도별 수치는 전부 통계 원자료 파일(사용자 제공, 2026-10-05)로 확정했다. 검색 결과의 충돌(미국 1974 물가 11% 대 12%, 미국 1975 실업률 8.5% 대 9%)은 원자료로 해소됐다.
  - 한국 소비자물가 상승률 1973~1980: 한국은행 경제통계시스템(ECOS) 4.2.1 소비자물가지수 총지수(2020=100)로 전년 대비를 직접 계산. 당시 발표치(1973 3.5%, 1974 24.8%로 알려진 값)와 소수점 단위로 다르며 본문에 계산값임을 명시. sources/ecos-korea-cpi-1970-2025.md
  - 미국 소비자물가 상승률 연평균: FRED FPCPITOTLZGUSA(세계은행 원자료). sources/fred-us-cpi-inflation-1973-1982.md
  - 미국 실업률 연평균: FRED UNRATE(미국 노동통계국 원자료). 1973 4.9, 1974 5.6, 1975 8.5, 1979 5.9, 1980 7.2(%).
  - 지금 한국 3지표: ECOS 첫 화면(소비자물가 2.9% 2026.09, GDP 전기대비 0.6% 2026년 2분기)과 ECOS 8.6.2 경제활동인구 표로 계산한 실업률(2026년 8월 원계열 2.0%, 계절조정 2.7%). sources/ecos-korea-unemployment-2026-08.md
  - 정의·원인 설명: 국가기록원, 국토연구원, 위키백과, 한국경제가 서로 일치.
  한국 1970년대 경제성장률은 ECOS에서 조회되지 않아 표에서 제외.
기준일: 2026년 10월 기준 (연도별 수치는 한국은행 ECOS·FRED 원자료, 2026-10-05 확인)
tags: 스태그플레이션, 스태그플레이션 뜻, 스태그플레이션 사례, 1970년대 오일쇼크, 물가상승 경기침체, 경기침체 물가, 실업률 물가상승률, 거시경제 지표, 주식 용어, 경제 용어
gate_pass: true
gate_pass_note: |
  게이트1 5,590회, 게이트2 v3 통과, 게이트3 4분면 표와 연도별 물가·실업률 표와 지금 3지표 점검, 게이트4 통계 원자료로 확정(primary_source 참조).
  남은 주의: 한국 물가는 지수로 계산한 값이라 당시 발표치와 소수점 단위로 다를 수 있음(본문에 명시). 미국 값은 FRED 경유이며 원자료는 세계은행·미국 노동통계국.
capture_guide: ""
self_check: |
  [2026-10-01 gate_pass:false, 게이트4 1차 출처 접속 불가 + 2차 출처 수치 충돌, capture 전환]
  후보 경위: check-keywords 8개(스태그플레이션 5,590 PASS, 경기침체 1,130 PASS, 점도표 1,140 PASS, 이동평균선 1,090 PASS, MDD 뜻 670 PASS, 배당성향 570 PASS, 이격도 480 FAIL, 양적완화 20 FAIL) 중 최고 검색량 채택. 다음 편 후보는 backlog에 기록.
  카니벌라이제이션: stock_drafts에서 "스태그플레이션"은 currency-hedge-cost-meaning.md와 dollar-index-meaning-currency-weights.md에 각 1회 스치듯 언급될 뿐 주제가 아니다. 소비자물가지수·GDP·기준금리 편으로는 내부 링크로 연결(난이도는 지표 해설 다음 단계인 "조합 해석").
  YMYL: 종목 추천·목표가·매매시점 없음. "스태그플레이션이면 무엇을 사라" 같은 투자 판단은 쓰지 않고 판별 방법과 역사적 배경만 서술.
  기관 링크: 외부 안내 문장 전부 링크, 출처 목록 4개 전부 링크. ecos.bok.or.kr, kostat.go.kr 같은 기관 대표 주소는 RULES.md 표에 없으나 기관 공식 도메인이며 지어낸 하위 경로는 쓰지 않음.
  제목 "스태그플레이션 판별 3지표와 1970년대 사례" 23자, 금지어 없음, "~뜻과 ~ 계산" 틀 회피. 슬러그 4단어 영문 소문자.
  첫 문장 유형: 절차형(뉴스에서 우려라는 말이 나오면 세 숫자부터 확인). 직전 RSI 문제제기형, CAGR 수치충격형, 기준금리 사실제시형과 다름.
  글 구조 유형: 비교형(첫 H2가 물가·성장률 4분면 비교표로 시작, 목차는 H2 5개라 생략하지 않고 유지). 직전 RSI 계산형, CAGR 절차형, 기준금리 시계열형과 겹치지 않음. 첫 H2의 첫 블록은 표.
  어투 모드: B 대화형(해요체, 독자에게 묻는 문장 3개). 직전 RSI·CAGR의 C 사례형과 다름. 꾸며낸 1인칭 경험 없음.
  AI 티 점검: em대시 0개, 접속어 '다만' 본문 0회, mark 밀도 4개(본문 실제 개수 위 4곳), FAQ 5개(직전 RSI 6·CAGR 4와 다름), H2 5개 중 "~나요"형 1개. 요약박스 청록(#e9f6f5/#2a8c8a), 제목 "🧭 핵심 체크 포인트", 마무리 박스 "🔎 확인 순서 다시 보기". FAQ 헤딩 "뉴스 보다가 떠오르는 의문". 면책 문구 새 표현.
  [2026-10-02 독자 관점 규칙 반영]
  인트로 메타 문장("이 글에서는~") 삭제 → 지금 숫자로 본 결론. 그림 1장(4분면 개념도). "지금 한국의 3지표" H2 신설(물가 9월 2.9%·성장 2분기 0.6%는 100·108편 검증 수치, 실업률은 출처 충돌로 캡처 요청 추가).
  "주식 투자자에게 스태그플레이션이 무서운 이유" H2 추가. FAQ "어떤 자산이 유리한가요" 답을 회피형에서 경로 설명으로 교체(추천 없음). 내부 링크 4개(100·107·108 발행 완료, 110 발행 예정).
refresh_due: 2026-11-05
refresh_reason: "10월 소비자물가(11월 초 발표) 반영해 지금 3지표 표 갱신"
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>뉴스에서 스태그플레이션 우려라는 말이 나오면 먼저 물가상승률, 경제성장률, 실업률 세 숫자부터 확인하면 돼요. 스태그플레이션은 경기가 가라앉는데도 물가가 계속 오르는 상태를 말해요. 2026년 지금 숫자로 보면 한국은 물가가 2%대 후반이고 성장률은 플러스라서, 성장이 멈춘 칸에는 들어가 있지 않아요.</p>

<div style="background:#e9f6f5;border:2px solid #2a8c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6360;font-size:18px;">🧭 핵심 체크 포인트</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>스태그플레이션은 <mark>물가는 오르고 성장은 멈추거나 뒷걸음질</mark>치는 조합입니다.</li><li>물가 하나만 높다고 스태그플레이션이 아니고, 성장률과 실업률을 함께 봐야 합니다.</li><li>1970년대 오일쇼크가 대표 사례이고, 지금 한국의 세 숫자는 본문 표에 따로 정리했어요.</li></ul>
</div>

<h2 style="border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">물가와 성장률 조합으로 보는 네 가지 경기 상황</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">스태그플레이션이 생기는 원인</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">1970년대 오일쇼크 때는 어땠을까요</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">지금 상황을 직접 판별하는 3지표 확인 순서</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">지금 한국의 3지표는 어디쯤일까요</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">스태그플레이션 뉴스를 읽을 때 놓치기 쉬운 점</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 스태그플레이션이 무서운 이유</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">물가와 성장률 조합으로 보는 네 가지 경기 상황</h2>
<p>물가가 오르는지 내리는지, 성장이 늘어나는지 줄어드는지를 겹치면 경기 상황은 네 가지로 나뉘어요. 스태그플레이션은 그중 물가 상승과 성장 둔화가 겹친 칸이에요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">성장 늘어남</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">성장 멈춤·감소</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">물가 오름</td><td style="border:1px solid #ddd;padding:8px;">경기 과열형 (수요가 공급을 앞지르는 상황)</td><td style="border:1px solid #ddd;padding:8px;"><mark>스태그플레이션</mark> (불황 속 물가 상승)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">물가 안정·하락</td><td style="border:1px solid #ddd;padding:8px;">골디락스형 (성장하면서 물가도 안정)</td><td style="border:1px solid #ddd;padding:8px;">디플레이션형 (불황과 물가 하락)</td></tr>
  </tbody>
</table>

<p>같은 물가 상승이라도 성장이 함께 늘면 과열이고, 성장이 꺼지면 스태그플레이션이에요. 그래서 물가 숫자 하나만 보고 판단하면 안 돼요.</p>

<p>물가가 어떻게 계산되는지 궁금하다면 <a href="https://sensitiveboss3.tistory.com/entry/consumer-price-index-calculation-guide" target="_blank" rel="noopener">소비자물가지수 계산 가이드</a>를, 성장률의 명목·실질 차이는 <a href="https://sensitiveboss3.tistory.com/entry/gdp-meaning-nominal-real-calculation" target="_blank" rel="noopener">GDP 뜻과 명목·실질 계산</a>을 먼저 보고 오면 이해가 빨라요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/stagflation-three-indicators-1970s-1.png" alt="물가와 성장률로 나눈 4분면 그림. 물가 오름과 성장 멈춤은 스태그플레이션, 물가 오름과 성장 늘어남은 경기 과열형, 물가 안정과 성장 늘어남은 골디락스형, 물가 안정과 성장 멈춤은 디플레이션형" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">개념도: 물가와 성장 조합 4분면</figcaption></figure>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">스태그플레이션이 생기는 원인</h2>
<p>가장 대표적인 원인은 <mark>원유 같은 원자재 가격이 갑자기 오르는 공급 충격</mark>이에요. 생산 비용이 올라 물가는 뛰는데 기업은 생산을 줄이니 성장은 꺾이고 일자리도 줄어요.</p>

<p>스태그플레이션이라는 말은 침체를 뜻하는 스태그네이션(stagnation)과 물가 상승을 뜻하는 인플레이션(inflation)을 합친 단어예요. 정의는 <a href="https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9C%EA%B7%B8%ED%94%8C%EB%A0%88%EC%9D%B4%EC%85%98" target="_blank" rel="noopener">위키백과 스태그플레이션</a>에도 같은 구성으로 나와요.</p>

<ul style="line-height:1.9;">
  <li>원자재 가격 급등: 생산 비용이 올라 기업이 가격을 올리고 생산은 줄입니다.</li>
  <li>대외 의존이 큰 경제 구조: 수입 가격 충격이 국내 물가와 경기에 바로 번집니다.</li>
  <li>정책의 딜레마: 금리를 올리면 물가는 잡히지만 경기가 더 눌리고, 내리면 경기는 살아도 물가가 더 오를 수 있어요.</li>
</ul>

<div style="background:#e9f6f5;border:2px solid #2a8c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6360;font-size:16px;">💡 금리가 왜 딜레마가 될까요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>기준금리는 보통 물가가 오르면 올리고 경기가 나쁘면 내립니다.</li><li>두 상황이 동시에 오면 어느 쪽을 우선할지 정해야 해서 정책이 어려워집니다.</li></ul>
</div>

<p>기준금리가 움직이는 방식은 <a href="https://sensitiveboss3.tistory.com/entry/base-rate-meaning-interest-calc" target="_blank" rel="noopener">기준금리 뜻과 이자 계산</a> 편에 정리해 두었어요.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">1970년대 오일쇼크 때는 어땠을까요</h2>
<p>1970년대 두 차례 오일쇼크가 스태그플레이션의 대표 사례로 꼽혀요. 1974년에는 주요 선진국이 두 자릿수 물가 상승과 성장 둔화를 함께 겪었어요.</p>

<p>한국도 해외 의존도가 높은 경제 구조라서 1차 석유파동 때 불황 속 물가 상승을 겪었고, 2차 석유파동에서도 반복됐어요. 이 흐름은 <a href="https://theme.archives.go.kr/next/koreaOfRecord/gasoline.do" target="_blank" rel="noopener">국가기록원 기록으로 만나는 대한민국 석유파동</a>에 정리돼 있어요.</p>

<p>아래 표는 연도별 물가와 실업률을 한 줄씩 놓고 보기 위한 표예요. 한국 물가는 한국은행 경제통계시스템의 소비자물가지수(2020=100)로 전년 대비 상승률을 직접 계산했고, 당시 발표치와 소수점 단위로 다를 수 있어요. 미국 물가는 세계은행 소비자물가 상승률(연평균), 미국 실업률은 연평균이에요(FRED 수록).</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">연도</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">한국 물가상승률(소비자물가)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">미국 물가상승률</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">미국 실업률</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">1973년</td><td style="border:1px solid #ddd;padding:8px;">3.2%</td><td style="border:1px solid #ddd;padding:8px;">6.2%</td><td style="border:1px solid #ddd;padding:8px;">4.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1974년</td><td style="border:1px solid #ddd;padding:8px;">24.3%</td><td style="border:1px solid #ddd;padding:8px;">11.1%</td><td style="border:1px solid #ddd;padding:8px;">5.6%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1975년</td><td style="border:1px solid #ddd;padding:8px;">25.2%</td><td style="border:1px solid #ddd;padding:8px;">9.1%</td><td style="border:1px solid #ddd;padding:8px;">8.5%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1979년</td><td style="border:1px solid #ddd;padding:8px;">18.3%</td><td style="border:1px solid #ddd;padding:8px;">11.3%</td><td style="border:1px solid #ddd;padding:8px;">5.9%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1980년</td><td style="border:1px solid #ddd;padding:8px;">28.7%</td><td style="border:1px solid #ddd;padding:8px;">13.5%</td><td style="border:1px solid #ddd;padding:8px;">7.2%</td></tr>
  </tbody>
</table>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">지금 상황을 직접 판별하는 3지표 확인 순서</h2>
<p>스태그플레이션 여부는 <mark>뉴스 헤드라인이 아니라 공식 통계 세 가지</mark>로 확인할 수 있어요. 아래 순서대로 보면 5분이면 충분해요.</p>

<ol style="line-height:1.9;">
  <li>물가상승률: <a href="https://kostat.go.kr" target="_blank" rel="noopener">통계청</a>이 발표하는 소비자물가 상승률을 전년 동월 대비로 봅니다.</li>
  <li>경제성장률: <a href="https://ecos.bok.or.kr" target="_blank" rel="noopener">한국은행 경제통계시스템</a>에서 분기 GDP 성장률이 연속으로 낮아지는지 봅니다.</li>
  <li>실업률: 통계청 경제활동인구조사의 실업률이 올라가는지 봅니다.</li>
  <li>세 숫자를 위 4분면 표에 놓고 물가 상승과 성장 둔화가 겹치는지 확인합니다.</li>
</ol>

<div style="background:#e9f6f5;border:2px solid #2a8c8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1d6360;font-size:16px;">🔎 확인 순서 다시 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>물가만 보지 말고 성장률과 실업률까지 세 숫자를 함께 봅니다.</li><li>한 달 수치보다 몇 달 이어지는 흐름을 봅니다.</li><li>판별은 현재 상황을 이해하는 용도이고, 매매 신호가 아닙니다.</li></ul>
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">지금 한국의 3지표는 어디쯤일까요</h2>

<p>판별 순서를 지금 숫자에 그대로 적용해 볼게요. 물가는 2%대 후반, 성장률은 플러스여서 4분면에서 스태그플레이션 칸과는 거리가 있어요. 다만 한 분기 숫자만으로 정하지 않고 몇 달 흐름을 이어서 봐요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">지표</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">최근 값</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">기준 시점·발표</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">소비자물가 상승률</td><td style="border:1px solid #ddd;padding:8px;">2.9% (전년 동월 대비)</td><td style="border:1px solid #ddd;padding:8px;">2026년 9월, 국가데이터처</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">실질 GDP 성장률</td><td style="border:1px solid #ddd;padding:8px;">0.6% (전기 대비)</td><td style="border:1px solid #ddd;padding:8px;">2026년 2분기 잠정치, 한국은행</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">실업률</td><td style="border:1px solid #ddd;padding:8px;">2.0% (원계열) / 2.7% (계절조정)</td><td style="border:1px solid #ddd;padding:8px;">2026년 8월, 국가데이터처 경제활동인구조사(한국은행 ECOS 수록)</td></tr>
  </tbody>
</table>

<p>물가 숫자는 <a href="https://sensitiveboss3.tistory.com/entry/consumer-price-index-calculation-guide" target="_blank" rel="noopener">소비자물가지수 계산 방법 글</a>의 최근 물가 표, 성장률은 <a href="https://sensitiveboss3.tistory.com/entry/gdp-meaning-nominal-real-calculation" target="_blank" rel="noopener">GDP 뜻과 명목·실질 계산 글</a>의 2분기 숫자와 같아요. 실업률은 원계열 2.0%, 계절조정 2.7%로 집계 방식에 따라 값이 달라요. 계절 요인을 지운 계절조정치가 달마다 흐름을 비교하기에 알맞아서 두 값을 함께 적었어요.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">스태그플레이션 뉴스를 읽을 때 놓치기 쉬운 점</h2>
<p>우려라는 말이 붙은 기사와 실제 스태그플레이션은 다른 이야기예요. 우려 기사는 가능성을 말하고, 판별은 확정된 통계로만 할 수 있어요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">흔한 오해</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">실제</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">물가가 오르면 스태그플레이션이다</td><td style="border:1px solid #ddd;padding:8px;">성장이 함께 늘면 경기 과열이에요. 성장 둔화가 겹쳐야 해당돼요.</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">경기가 나쁘면 스태그플레이션이다</td><td style="border:1px solid #ddd;padding:8px;">물가가 안정이거나 내리면 디플레이션형에 가까워요.</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1970년대와 똑같이 반복된다</td><td style="border:1px solid #ddd;padding:8px;">원인과 경제 구조가 달라서 같은 모양으로 오지 않을 수 있어요.</td></tr>
  </tbody>
</table>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">주식 투자자에게 스태그플레이션이 무서운 이유</h2>

<p>주식시장이 스태그플레이션이라는 단어에 예민한 건, 주가를 받치는 두 기둥이 동시에 흔들리기 때문이에요.</p>

<ul style="line-height:1.9;">
  <li><strong>이익이 줄어요:</strong> 원자재 값이 올라 원가는 늘었는데 경기가 식어 판매는 줄면, 기업 마진이 양쪽에서 눌려요. 원가 상승이 어디서 먼저 보이는지는 <a href="https://sensitiveboss3.tistory.com/entry/producer-price-index-cpi-difference" target="_blank" rel="noopener">생산자물가지수 글</a>에서 볼 수 있어요.</li>
  <li><strong>금리가 도와주지 못해요:</strong> 보통 경기가 나쁘면 금리를 내려 주가를 받치지만, 물가가 높으면 금리를 내리기 어려워요. 할인율 부담이 그대로 남는 거예요.</li>
  <li><strong>업종마다 다르게 맞아요:</strong> 원가를 판매가에 넘길 힘이 있는 기업과 없는 기업의 차이가 평소보다 크게 벌어져요.</li>
</ul>

<p>그래서 기사에서 이 단어를 보면, 결론보다 세 숫자가 실제로 어느 칸에 있는지부터 보는 게 순서예요.</p>

<h2 style="border-left:6px solid #2a8c8a;padding-left:12px;margin-top:36px;">뉴스 보다가 떠오르는 의문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">스태그플레이션과 경기침체는 같은 말인가요</summary>
  <p style="margin:10px 0 0 0;">같지 않습니다. 경기침체는 성장이 줄어드는 상태이고, 스태그플레이션은 거기에 물가 상승이 함께 있는 경우입니다. 침체 중에 물가가 내리면 스태그플레이션이 아닙니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">물가상승률이 몇 퍼센트를 넘어야 스태그플레이션인가요</summary>
  <p style="margin:10px 0 0 0;">정해진 숫자 기준은 없습니다. 물가 상승과 성장 둔화, 일자리 악화가 함께 나타나는지를 종합해서 판단합니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">스태그플레이션이 오면 금리는 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">정해진 방향은 없습니다. 물가를 잡으려면 금리를 올리고 경기를 살리려면 내려야 해서 상황마다 중앙은행의 선택이 달라집니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">한국도 스태그플레이션을 겪은 적이 있나요</summary>
  <p style="margin:10px 0 0 0;">1970년대 1차와 2차 석유파동 때 불황 속 물가 상승을 겪은 것으로 기록돼 있습니다. 해외 의존도가 높은 경제 구조가 영향을 줬다는 설명이 국가기록원 자료에 나옵니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">스태그플레이션 때 어떤 자산이 유리한가요</summary>
  <p style="margin:10px 0 0 0;">정해진 답은 없어요. 원가를 판매가에 넘길 수 있는지, 빚이 많아 금리에 민감한지에 따라 같은 시기에도 결과가 갈렸어요. 이 글은 특정 자산이나 종목을 권하지 않아요.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (2026년 10월 확인):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://theme.archives.go.kr/next/koreaOfRecord/gasoline.do" target="_blank" rel="noopener">국가기록원 기록으로 만나는 대한민국 석유파동</a></li>
    <li><a href="https://www.krihs.re.kr/data/en_brief/Brief_190.pdf" target="_blank" rel="noopener">국토연구원 스태그플레이션과 주택시장</a></li>
    <li><a href="https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9C%EA%B7%B8%ED%94%8C%EB%A0%88%EC%9D%B4%EC%85%98" target="_blank" rel="noopener">위키백과 스태그플레이션</a></li>
    <li><a href="https://ecos.bok.or.kr" target="_blank" rel="noopener">한국은행 경제통계시스템(ECOS) 소비자물가지수·경제활동인구</a></li>
    <li><a href="https://fred.stlouisfed.org/series/UNRATE" target="_blank" rel="noopener">FRED 미국 실업률(UNRATE)과 소비자물가 상승률</a></li>
    <li><a href="https://sgsg.hankyung.com/article/2025020799981" target="_blank" rel="noopener">한국경제 경제야 놀자 스태그플레이션 딜레마</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;">이 글은 경제 용어를 설명하는 정보 글이며 특정 종목이나 금융상품을 사고팔라는 권유가 아닙니다. 투자 결정과 그 결과는 투자자 본인이 책임지며, 통계 수치는 발표 기관 자료가 기준입니다.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "스태그플레이션 판별 3지표와 1970년대 사례",
  "description": "스태그플레이션이 무엇인지, 물가와 성장률 조합 4분면, 원인, 1970년대 오일쇼크 사례, 물가·성장률·실업률로 직접 판별하는 순서를 정리했습니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/stagflation-three-indicators-1970s"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/stagflation-three-indicators-1970s-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "스태그플레이션과 경기침체는 같은 말인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "같지 않습니다. 경기침체는 성장이 줄어드는 상태이고, 스태그플레이션은 거기에 물가 상승이 함께 있는 경우입니다. 침체 중에 물가가 내리면 스태그플레이션이 아닙니다."
      }
    },
    {
      "@type": "Question",
      "name": "물가상승률이 몇 퍼센트를 넘어야 스태그플레이션인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 숫자 기준은 없습니다. 물가 상승과 성장 둔화, 일자리 악화가 함께 나타나는지를 종합해서 판단합니다."
      }
    },
    {
      "@type": "Question",
      "name": "스태그플레이션이 오면 금리는 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 방향은 없습니다. 물가를 잡으려면 금리를 올리고 경기를 살리려면 내려야 해서 상황마다 중앙은행의 선택이 달라집니다."
      }
    },
    {
      "@type": "Question",
      "name": "한국도 스태그플레이션을 겪은 적이 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1970년대 1차와 2차 석유파동 때 불황 속 물가 상승을 겪은 것으로 기록돼 있습니다. 해외 의존도가 높은 경제 구조가 영향을 줬다는 설명이 국가기록원 자료에 나옵니다."
      }
    },
    {
      "@type": "Question",
      "name": "스태그플레이션 때 어떤 자산이 유리한가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 답은 없어요. 원가를 판매가에 넘길 수 있는지, 빚이 많아 금리에 민감한지에 따라 같은 시기에도 결과가 갈렸어요. 이 글은 특정 자산이나 종목을 권하지 않아요."
      }
    }
  ]
}
</script>
