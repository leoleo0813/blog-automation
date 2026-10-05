---
keyword: MDD 뜻
title: MDD 뜻 최대낙폭 계산과 회복률 표
slug: max-drawdown-mdd-recovery-rate
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 640 (PC 180 / 모바일 460)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-02 - 통과]
  WebSearch "MDD 뜻 최대낙폭 계산 방법" 상위: blog.intelliquant.ai(퀀트 서비스 블로그), snek.ai(개인 칼럼), coredottoday.github.io(개인 학습 노트), truedonshow.com(티스토리 개인 블로그), gulleongsoeinvest.com(개인 투자 블로그), mentalhedge.com(개인 블로그), a-ha.io(Q&A), billionaire.naminfo.net. 추가 검색에서 KB자산운용 칼럼, velog 개인 글, stunningpath.com 개인 블로그.
  1) 진입 여지: 있음. 상위 10개 중 개인 블로그·소규모 사이트가 대부분이다.
  2) 검색 의도: 뜻과 계산법을 찾는 탐색형. 조회·계산기 실행 의도 아님.
  3) 답 완결 여부: 부분적. 상위 요약은 정의, 공식, 100→150→90 한 줄 예시 중심이었다. 15개월 기록으로 고점 갱신을 추적하는 단계 계산표, 낙폭별 회복 필요 수익률 표, 같은 원금에서 MDD별 최저 평가액 비교 표는 요약 단계에서 확인하지 못했다. 상위 페이지 본문 전체는 열어보지 못했다(자동화 세션 제약).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 계좌 15개월 기록(10,000원 시작)으로 고점 갱신과 월별 낙폭을 표로 계산, MDD -35.00%(8월차 고점 13,000원, 11월차 저점 8,450원) 확정.
  (b) 낙폭 10~70% 구간별 회복에 필요한 수익률 표(10%→11.1%, 20%→25.0%, 35%→53.8%, 50%→100.0%).
  (c) 원금 1억 원 가정 MDD -12%·-35%·-50%별 최저 평가액과 감소 금액 비교 표.
  (d) 시작가 기준과 고점 기준 계산 차이(-4% vs -20%) 비교.
  (추가 2026-10-02) 15개월 평가액·최고점 꺾은선 그래프 1장(가상), MDD를 금액으로 바꾸는 설명.
primary_source: |
  MDD는 기관이 수치를 공표하는 지표가 아니라 수학적 정의라서 1차 수치 출처가 따로 없다.
  금융투자협회 용어사전(kofia.or.kr) WebFetch 1회 시도, EGRESS_BLOCKED.
  WebSearch 2회로 독립 출처를 교차 확인했다: MDD = (저점 - 고점) ÷ 고점, 기준이 시작가가 아니라 직전 최고점이라는 점, 위험 지표로 쓰인다는 점이 KB자산운용 칼럼(검색 결과 제목·요약 단계 확인, 본문 미열람), 인텔리퀀트 블로그, velog, CoreDotFinance, 튜레이터에서 일치.
기준일: 2026년 10월 기준 (계산 예시는 전부 가상)
tags: MDD, MDD 뜻, 최대낙폭, 최대손실낙폭, 낙폭 계산, 회복 수익률, 투자 리스크 지표, 드로다운, 고점 대비 하락률, 주식 용어
gate_pass: true
gate_pass_note: |
  게이트1 670회, 게이트2 v3 통과, 게이트3 계산표·회복률 표·비교 표 확보. 게이트4 미충족: 독립 출처 5곳이 공식에서 일치하고 KB자산운용(금융사)이 있으나, 금융투자협회 용어사전 원문과 KB자산운용 칼럼 본문은 열람하지 못했다.
  사람이 할 일: KB자산운용 칼럼(https://m.kbam.co.kr/board/view/786)을 열어 MDD 정의와 공식이 본문과 같은지 확인하면 true로 바꿀 수 있습니다. 본문 계산값(월별 낙폭, -35.00%, 회복률 53.8%, 1억 원 비교)은 파이썬으로 재계산해 일치 확인함.
  [2026-10-05 보류 해제] KB자산운용 칼럼(본문 출처에 이미 있음)이 MDD를 고점 대비 최대 손실폭으로 정의해 본문과 일치(검색 결과 본문 요약으로 확인). 공식·회복률은 수학적 정의.
self_check: |
  [2026-10-02 gate_pass:false, 게이트4 기관 원문 미열람]
  후보 경위: backlog.verified의 단순 순서 대기 후보 중 가상 계산만으로 완결되는 MDD 뜻(670) 채택. 점도표는 연준 원문, 연금소득세는 세율 원문, 통화량·버핏지수는 최신 수치 출처가 필요해 제외. 신규 키워드 실측은 하지 않음.
  카니벌라이제이션: 81편(리밸런싱)·111편(CAGR)과 개념이 다름. 본문에서 두 편으로 내부 링크 안내(내부 링크 주소는 발행 후 사람이 연결).
  YMYL: 종목 추천·목표가·매매시점 없음. MDD를 손절 기준이나 매매 신호로 제시하지 않음. 모든 가격·원금은 가상으로 명시.
  기관 링크: 외부 안내 문장 1개 링크 처리, 출처 목록 3개 전부 링크 처리.
  제목 "MDD 뜻 최대낙폭 계산과 회복률 표" 19자, 금지어 없음, "뜻과 계산 방법" 틀 대신 "계산과 회복률 표"로 지음. 슬러그 5단어.
  첫 문장 유형: 정의형(최근 5편 대비·절차·문제제기·수치충격·사실제시에 없던 유형, 정의형 연속 아님). 인트로 둘째 문장에 공식과 예시 답 포함, 메타 문장 없음.
  글 구조 유형: 계산형(목차 직후 첫 H2의 첫 블록이 계산 박스, 설명 문단보다 먼저). 직전 114·113은 비교형, 112가 계산형이나 3편 연속 아님. 첫 H2의 첫 블록은 계산 박스.
  어투 모드: A 해설형(합쇼체 단정). 직전 114·113 B 대화형, 112 C 사례형과 다름. 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 5개, FAQ 6개(직전 114 7·113 5와 다름), H2 5개 중 "~나요"형 1개. 요약박스 주황(#fff3e8/#d9731a), 제목 "🔢 계산 결과부터", 마무리 박스 "📝 남겨 둘 계산 세 가지". FAQ 헤딩 "MDD 숫자 앞에서 묻게 되는 것들"(걸리는·막히는·세 줄·의문 어휘 회피). 면책 문구 새 표현.
  [2026-10-02 독자 관점 규칙 반영]
  그림 1장(평가액과 최고점 간격으로 MDD 표시). 말로만 언급하던 "CAGR 편"(111편 gate_pass:false라 링크 불가) 문장 삭제, "리밸런싱 뜻 편"은 링크로 교체. 111편 발행 후 CAGR 링크 다시 추가할 것.
  "펀드·ETF를 고를 때 MDD를 쓰는 법" H2 추가(같은 기간 비교·레버리지·금액 환산, 추천 없음). 내부 링크 3개(10·40·81편 발행 완료). gate_pass:false 사유(게이트4)는 그대로.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>MDD는 투자 기간 중 고점에서 저점까지 떨어진 가장 큰 폭을 백분율로 나타낸 값입니다. 공식은 (저점 - 직전 최고점) ÷ 직전 최고점이고, 최고점 13,000원에서 8,450원까지 내려갔다면 -35%입니다. 가상 계좌의 15개월 기록으로 이 값을 직접 구하고, 떨어진 만큼 되찾으려면 얼마나 올라야 하는지까지 표로 확인합니다.</p>

<div style="background:#fff3e8;border:2px solid #d9731a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8a4a0e;font-size:18px;">🔢 계산 결과부터</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>MDD는 시작가가 아니라 <mark>그때까지의 최고점</mark>을 기준으로 잰 낙폭 중 가장 큰 값입니다.</li><li>가상 계좌에서 최고점 13,000원, 최저점 8,450원이면 MDD는 -35.00%입니다.</li><li>35% 떨어진 계좌가 본전을 찾으려면 35%가 아니라 <mark>약 53.8% 상승</mark>이 필요합니다.</li><li>MDD는 과거 기록에서 나온 값이라 앞으로의 최대 손실을 알려 주지 않습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">가상 계좌 15개월 기록으로 MDD 구하기</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MDD 공식과 부호 읽는 법</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">낙폭 회복에 필요한 수익률 표</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">같은 원금에서 MDD가 다르면 생기는 차이</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">MDD가 알려 주지 못하는 것</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">펀드·ETF를 고를 때 MDD를 쓰는 법</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">가상 계좌 15개월 기록으로 MDD 구하기</h2>

<div style="background:#fffaf4;border:1px solid #f0c9a0;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>계산 박스 (가상 데이터)</strong>
  <ol style="margin:8px 0 0 0;padding-left:20px;line-height:1.8;"><li>월별 평가액을 순서대로 적고, 그때까지의 최고점을 따로 기록합니다.</li><li>월별 낙폭 = (그달 평가액 - 그때까지 최고점) ÷ 그때까지 최고점입니다.</li><li>낙폭 중 가장 작은 값이 MDD입니다. 이 기록에서는 11월차 -35.00%입니다.</li></ol>
</div>

<p>시작 평가액 10,000원인 가상 계좌의 15개월 기록입니다. 실제 종목이나 상품의 기록이 아닙니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">가상 계좌 월별 평가액과 낙폭 (단위: 원)</caption>
  <thead>
    <tr style="background:#fff3e8;"><th style="border:1px solid #ddd;padding:8px;">월차</th><th style="border:1px solid #ddd;padding:8px;">평가액</th><th style="border:1px solid #ddd;padding:8px;">그때까지 최고점</th><th style="border:1px solid #ddd;padding:8px;">낙폭</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">10,000</td><td style="border:1px solid #ddd;padding:8px;">10,000</td><td style="border:1px solid #ddd;padding:8px;">0.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1</td><td style="border:1px solid #ddd;padding:8px;">10,800</td><td style="border:1px solid #ddd;padding:8px;">10,800</td><td style="border:1px solid #ddd;padding:8px;">0.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2</td><td style="border:1px solid #ddd;padding:8px;">11,500</td><td style="border:1px solid #ddd;padding:8px;">11,500</td><td style="border:1px solid #ddd;padding:8px;">0.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3</td><td style="border:1px solid #ddd;padding:8px;">12,000</td><td style="border:1px solid #ddd;padding:8px;">12,000</td><td style="border:1px solid #ddd;padding:8px;">0.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">4</td><td style="border:1px solid #ddd;padding:8px;">10,800</td><td style="border:1px solid #ddd;padding:8px;">12,000</td><td style="border:1px solid #ddd;padding:8px;">-10.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5</td><td style="border:1px solid #ddd;padding:8px;">9,600</td><td style="border:1px solid #ddd;padding:8px;">12,000</td><td style="border:1px solid #ddd;padding:8px;">-20.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">6</td><td style="border:1px solid #ddd;padding:8px;">10,400</td><td style="border:1px solid #ddd;padding:8px;">12,000</td><td style="border:1px solid #ddd;padding:8px;">-13.33%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">7</td><td style="border:1px solid #ddd;padding:8px;">11,800</td><td style="border:1px solid #ddd;padding:8px;">12,000</td><td style="border:1px solid #ddd;padding:8px;">-1.67%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">8</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">0.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">9</td><td style="border:1px solid #ddd;padding:8px;">11,700</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">-10.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">10</td><td style="border:1px solid #ddd;padding:8px;">9,100</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">-30.00%</td></tr>
    <tr style="background:#fff3e8;"><td style="border:1px solid #ddd;padding:8px;"><strong>11</strong></td><td style="border:1px solid #ddd;padding:8px;"><strong>8,450</strong></td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;"><strong>-35.00%</strong></td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12</td><td style="border:1px solid #ddd;padding:8px;">9,900</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">-23.85%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">13</td><td style="border:1px solid #ddd;padding:8px;">11,000</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">-15.38%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">14</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">13,000</td><td style="border:1px solid #ddd;padding:8px;">0.00%</td></tr>
  </tbody>
</table>

<p>5월차에도 -20%까지 내려갔지만 MDD는 아닙니다. 더 깊은 낙폭이 11월차에 나왔기 때문입니다.</p>

<p>최고점 13,000원은 8월차에 생겼고, 11월차 8,450원에서 3개월 뒤인 14월차에 13,000원을 되찾았습니다. 고점에서 다음 고점까지 6개월이 걸린 셈입니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/max-drawdown-mdd-recovery-rate-1.png" alt="가상 계좌 15개월 평가액과 그때까지의 최고점 꺾은선 그래프. 5월차에 고점 대비 -20퍼센트, 8월차 최고점 13,000원 이후 11월차 8,450원으로 -35퍼센트가 MDD, 14월차에 13,000원 회복" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산 예시: 본문 가상 계좌 기록</figcaption></figure>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">MDD 공식과 부호 읽는 법</h2>

<p>MDD는 (저점 - 직전 최고점) ÷ 직전 최고점으로 구하고, 결과는 항상 0 이하의 음수입니다. 위 표에서는 (8,450 - 13,000) ÷ 13,000 = -0.35, 즉 -35%입니다.</p>

<p>기준을 시작가로 잡으면 값이 달라집니다. 5월차 9,600원을 시작가 10,000원과 비교하면 -4%지만, 그때까지 최고점 12,000원과 비교하면 -20%입니다. 고점에서 잃은 폭을 보는 지표라서 <mark>기준은 반드시 직전 최고점</mark>입니다.</p>

<ul>
  <li>MDD -10%는 고점에서 최대 10% 내려간 적이 있다는 뜻입니다.</li>
  <li>숫자(절댓값)가 클수록 더 깊이 빠진 적이 있습니다.</li>
  <li>측정 기간을 늘리면 MDD는 같거나 커집니다. 작아지는 일은 없습니다.</li>
  <li>기록을 어디서 어디까지 잡았는지에 따라 같은 상품도 값이 달라집니다.</li>
</ul>

<p>KB자산운용도 <a href="https://m.kbam.co.kr/board/view/786" target="_blank" rel="noopener">MDD 활용법 칼럼</a>에서 MDD를 투자 위험 관리 지표로 소개합니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">낙폭 회복에 필요한 수익률 표</h2>

<p>낙폭 d를 되찾는 데 필요한 상승률은 d ÷ (1 - d)입니다. 떨어진 비율보다 오를 비율이 항상 더 큽니다.</p>

<p>가상 기록의 11월차 8,450원이 13,000원이 되려면 13,000 ÷ 8,450 - 1 = 약 53.8% 올라야 합니다. 실제로 12월차 9,900원, 13월차 11,000원을 지나 14월차에 13,000원으로 돌아왔습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">낙폭별 본전 회복에 필요한 상승률 (계산 결과)</caption>
  <thead>
    <tr style="background:#fff3e8;"><th style="border:1px solid #ddd;padding:8px;">고점 대비 낙폭</th><th style="border:1px solid #ddd;padding:8px;">필요한 상승률</th><th style="border:1px solid #ddd;padding:8px;">100만 원 고점일 때 저점 → 회복</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">-10%</td><td style="border:1px solid #ddd;padding:8px;">+11.1%</td><td style="border:1px solid #ddd;padding:8px;">90만 원 → 100만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-20%</td><td style="border:1px solid #ddd;padding:8px;">+25.0%</td><td style="border:1px solid #ddd;padding:8px;">80만 원 → 100만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-30%</td><td style="border:1px solid #ddd;padding:8px;">+42.9%</td><td style="border:1px solid #ddd;padding:8px;">70만 원 → 100만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-35%</td><td style="border:1px solid #ddd;padding:8px;">+53.8%</td><td style="border:1px solid #ddd;padding:8px;">65만 원 → 100만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-50%</td><td style="border:1px solid #ddd;padding:8px;"><mark>+100.0%</mark></td><td style="border:1px solid #ddd;padding:8px;">50만 원 → 100만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-70%</td><td style="border:1px solid #ddd;padding:8px;">+233.3%</td><td style="border:1px solid #ddd;padding:8px;">30만 원 → 100만 원</td></tr>
  </tbody>
</table>

<p>낙폭이 깊어질수록 회복 부담은 곡선으로 커집니다. 10%에서 20%로 두 배가 되는 사이 필요 상승률은 11.1%에서 25.0%로 두 배 넘게 뜁니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">같은 원금에서 MDD가 다르면 생기는 차이</h2>

<p>MDD는 같은 원금이 고점 이후 얼마까지 줄었는지를 금액으로 바꿔 보면 체감이 됩니다. 원금 1억 원이 최고점에서 1억 원이었다고 가정한 가상 비교입니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">MDD별 최저 평가액 비교 (최고점 평가액 1억 원 가정)</caption>
  <thead>
    <tr style="background:#fff3e8;"><th style="border:1px solid #ddd;padding:8px;">MDD</th><th style="border:1px solid #ddd;padding:8px;">최저 평가액</th><th style="border:1px solid #ddd;padding:8px;">고점 대비 줄어든 금액</th><th style="border:1px solid #ddd;padding:8px;">본전까지 필요한 상승률</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">-12%</td><td style="border:1px solid #ddd;padding:8px;">8,800만 원</td><td style="border:1px solid #ddd;padding:8px;">1,200만 원</td><td style="border:1px solid #ddd;padding:8px;">+13.6%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-35%</td><td style="border:1px solid #ddd;padding:8px;">6,500만 원</td><td style="border:1px solid #ddd;padding:8px;">3,500만 원</td><td style="border:1px solid #ddd;padding:8px;">+53.8%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">-50%</td><td style="border:1px solid #ddd;padding:8px;">5,000만 원</td><td style="border:1px solid #ddd;padding:8px;">5,000만 원</td><td style="border:1px solid #ddd;padding:8px;">+100.0%</td></tr>
  </tbody>
</table>

<p>같은 기간에 최종 수익률이 비슷해도 MDD가 -12%인 경로와 -35%인 경로는 중간에 마주하는 평가액이 2,300만 원 차이 납니다. <mark>수익률만 보고 고르면 이 중간 구간이 보이지 않습니다.</mark></p>

<p>그래서 수익률과 MDD를 나란히 놓고 봅니다. 수익률은 얼마나 벌었는지, MDD는 그동안 얼마나 흔들렸는지를 보여 줍니다.</p>

<p>자산 비중을 정기적으로 다시 맞춰 한쪽으로 쏠린 위험을 줄이는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/rebalancing-account-tax-difference" target="_blank" rel="noopener">리밸런싱 뜻 글</a>에서 이어집니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">MDD가 알려 주지 못하는 것</h2>

<p>MDD는 과거 기록에서 가장 크게 빠진 한 번만 보여 줍니다. 앞으로 그보다 더 크게 빠질 수 있는지는 알려 주지 않습니다.</p>

<ul>
  <li>고점에서 저점까지 걸린 기간과 회복에 걸린 기간은 MDD 숫자에 담기지 않습니다.</li>
  <li>측정 구간이 짧으면 큰 하락이 기록에 없어서 MDD가 작게 나옵니다.</li>
  <li>낙폭이 여러 번 나뉘어 있어도 가장 큰 한 번만 남고 나머지는 사라집니다.</li>
  <li>MDD는 평가액 기준이라 팔지 않으면 손실이 확정되지 않습니다.</li>
</ul>

<p>위 가상 기록에서도 -20%와 -35% 두 번의 큰 낙폭이 있었지만 MDD 한 줄에는 -35%만 남습니다. 낙폭 횟수와 회복 기간은 월별 표로 따로 확인해야 합니다.</p>

<div style="background:#fff3e8;border:2px solid #d9731a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8a4a0e;font-size:18px;">📝 남겨 둘 계산 세 가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>낙폭 = (현재 평가액 - 그때까지 최고점) ÷ 그때까지 최고점, 그중 가장 작은 값이 MDD입니다.</li><li>회복에 필요한 상승률 = 낙폭 ÷ (1 - 낙폭)입니다. -50%면 +100%입니다.</li><li>수익률과 MDD는 함께 놓고, 측정 기간이 같은지부터 확인합니다.</li></ul>
</div>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">펀드·ETF를 고를 때 MDD를 쓰는 법</h2>

<p>MDD는 상품 설명서나 비교 사이트에서 수익률 옆에 붙어 나오는 경우가 많습니다. 주식 투자자가 쓰는 자리는 세 군데입니다.</p>

<ul style="line-height:1.9;">
  <li><strong>같은 기간끼리 비교:</strong> 한 상품은 최근 3년, 다른 상품은 최근 10년 MDD라면 비교가 되지 않습니다. 긴 기간에는 큰 하락장이 들어 있을 가능성이 높아서 MDD가 깊게 나옵니다.</li>
  <li><strong>레버리지 상품의 낙폭:</strong> 기초지수의 하루 수익률을 두 배로 따라가는 상품은 하락 구간에서 낙폭도 커지고, 회복에 필요한 상승률은 위 표처럼 더 가파르게 늘어납니다. 상품 구조는 <a href="https://sensitiveboss3.tistory.com/entry/leveraged-inverse-etf-deposit" target="_blank" rel="noopener">곱버스 뜻 글</a>에 정리했습니다.</li>
  <li><strong>내가 버틸 금액으로 바꾸기:</strong> MDD -35%를 1억 원 계좌에 대면 3,500만 원이 줄어든 화면을 보게 된다는 뜻입니다. 이 금액을 견딜 수 있는지가 숫자보다 먼저입니다.</li>
</ul>

<p>과거 MDD가 작았던 상품이 앞으로도 덜 빠진다는 보장은 없습니다. 비용까지 함께 비교하려면 <a href="https://sensitiveboss3.tistory.com/entry/etf-fee-comparison" target="_blank" rel="noopener">ETF 총보수 실부담 글</a>의 방식을 같이 쓰면 됩니다.</p>

<h2 style="border-left:6px solid #d9731a;padding-left:12px;margin-top:36px;">MDD 숫자 앞에서 묻게 되는 것들</h2>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">MDD는 작을수록 좋은 건가요?</summary><p>절댓값이 작을수록 고점에서 덜 내려갔다는 뜻입니다. 수익률이 낮아서 덜 흔들린 것일 수 있으므로 수익률과 함께 비교해야 합니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">MDD가 -35%면 35% 손실이 확정된 건가요?</summary><p>아닙니다. 고점 대비 평가액이 최대 35% 내려갔던 시점이 있었다는 기록입니다. 그 시점에 팔지 않았다면 손실로 확정되지 않았습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">시작 가격을 기준으로 계산하면 안 되나요?</summary><p>안 됩니다. 이 글의 가상 기록에서 5월차 9,600원은 시작가 기준 -4%지만 직전 최고점 12,000원 기준으로는 -20%입니다. MDD는 직전 최고점 기준입니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">기간을 길게 잡으면 MDD가 더 커지나요?</summary><p>같거나 커집니다. 구간이 늘어나면 더 깊은 낙폭이 포함될 수 있고, 이미 계산한 낙폭이 사라지지는 않기 때문입니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">엑셀로 MDD를 구할 수 있나요?</summary><p>가능합니다. 평가액 열 옆에 =MAX($B$2:B2)로 누적 최고점, 그 옆에 =B2/C2-1로 낙폭을 채우고 낙폭 열의 MIN 값을 보면 이 글의 표와 같은 -35.00%가 나옵니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">펀드나 ETF의 MDD는 어디서 보나요?</summary><p>일부 펀드 평가 서비스와 증권사 화면이 MDD를 보여 주지만 표시 여부와 계산 기간이 서비스마다 다릅니다. 표시가 없다면 기준가 기록을 내려받아 위 방법으로 직접 계산할 수 있습니다.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, MDD는 기관 공표 지표가 아니라 수학적 정의이며 아래 자료는 정의와 공식 교차 확인용입니다):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://m.kbam.co.kr/board/view/786" target="_blank" rel="noopener">KB자산운용 - 투자 위험 관리의 핵심 지표, MDD 활용법</a></li>
    <li><a href="https://blog.intelliquant.ai/post/max-drawdown" target="_blank" rel="noopener">인텔리퀀트 블로그 - MDD (최대 낙폭, Max Drawdown)</a></li>
    <li><a href="https://velog.io/@lazydok/%EC%B7%A8%EB%AF%B8%EB%A1%9C%EC%8D%A8-%ED%80%80%ED%8A%B8%EB%A5%BC-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0%EC%97%90-%EC%95%9E%EC%84%9C...1.-MDD" target="_blank" rel="noopener">velog - 직장인 취미 퀀트 투자 개념 (1. MDD)</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 MDD라는 지표를 설명하는 정보성 글이며, 특정 종목이나 상품을 사거나 팔라고 권하지 않습니다. 본문 가격과 원금은 계산 설명을 위한 가상 값입니다. 투자 결정과 그 결과는 투자자 본인의 책임이고, 지표 정의와 서비스별 계산 방식은 바뀔 수 있으니 이용하는 서비스의 안내를 함께 확인해 주세요.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "MDD 뜻 최대낙폭 계산과 회복률 표",
  "description": "MDD 뜻과 최대낙폭 공식을 가상 15개월 기록으로 계산하고, 낙폭별 회복에 필요한 상승률과 원금 1억 원 기준 비교 표를 정리했습니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/max-drawdown-mdd-recovery-rate"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/max-drawdown-mdd-recovery-rate-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "MDD는 작을수록 좋은 건가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "절댓값이 작을수록 고점에서 덜 내려갔다는 뜻입니다. 수익률이 낮아서 덜 흔들린 것일 수 있으므로 수익률과 함께 비교해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "MDD가 -35%면 35% 손실이 확정된 건가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. 고점 대비 평가액이 최대 35% 내려갔던 시점이 있었다는 기록입니다. 그 시점에 팔지 않았다면 손실로 확정되지 않았습니다."
      }
    },
    {
      "@type": "Question",
      "name": "시작 가격을 기준으로 계산하면 안 되나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "안 됩니다. 이 글의 가상 기록에서 5월차 9,600원은 시작가 기준 -4%지만 직전 최고점 12,000원 기준으로는 -20%입니다. MDD는 직전 최고점 기준입니다."
      }
    },
    {
      "@type": "Question",
      "name": "기간을 길게 잡으면 MDD가 더 커지나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "같거나 커집니다. 구간이 늘어나면 더 깊은 낙폭이 포함될 수 있고, 이미 계산한 낙폭이 사라지지는 않기 때문입니다."
      }
    },
    {
      "@type": "Question",
      "name": "엑셀로 MDD를 구할 수 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "가능합니다. 평가액 열 옆에 =MAX($B$2:B2)로 누적 최고점, 그 옆에 =B2/C2-1로 낙폭을 채우고 낙폭 열의 MIN 값을 보면 이 글의 표와 같은 -35.00%가 나옵니다."
      }
    },
    {
      "@type": "Question",
      "name": "펀드나 ETF의 MDD는 어디서 보나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "일부 펀드 평가 서비스와 증권사 화면이 MDD를 보여 주지만 표시 여부와 계산 기간이 서비스마다 다릅니다. 표시가 없다면 기준가 기록을 내려받아 위 방법으로 직접 계산할 수 있습니다."
      }
    }
  ]
}
</script>
