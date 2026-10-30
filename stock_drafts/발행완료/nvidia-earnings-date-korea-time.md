---
keyword: 엔비디아 실적발표
title: 엔비디아 실적발표 일정과 한국시간 계산
slug: nvidia-earnings-date-korea-time
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 1230 (PC 200 / 모바일 1030)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-06 - 통과] WebSearch(미국 기준, 참고용) 상위: bullstory.io·thecheck.co.kr·weolbu 커뮤니티·tokenpost·blockmedia 같은 소규모 정리 사이트와 언론, 증권플러스 속보, 엔비디아 IR.
  1) 진입 여지 - 있음. 개인·소규모 콘텐츠 사이트가 상위에 3곳 이상.
  2) 검색 의도 - 발표일과 시각, 결과 확인 탐색형. 조회·신청 도구 아님.
  3) 답 완결 - 아님. 상위는 날짜 한 줄 또는 분기 결과 속보이고, 최근 분기 가이던스 대비 실제 매출 계산과 서머타임 전후 한국시간 환산을 한 글로 묶은 곳은 확인하지 못함(검색 요약 기준).
unique_asset: |
  (a) 가이던스 대비 실제 매출 상회율 계산표(2027회계연도 1·2분기)와 막대그래프.
  (b) 최근 4번 발표일의 미국 날짜·한국 날짜·적용 시간대·환산 시각 표.
  (c) 서머타임 종료(2026-11-01) 전후 한국시간 비교 그림.
primary_source: |
  엔비디아 IR 보도자료(nvidianews.nvidia.com)는 WebFetch 1회 시도, EGRESS_BLOCKED로 원문 미열람. 언론 교차검증으로 진행.
  - 2027회계연도 1분기(2026-05-20 미국 발표) 매출 816억 2천만 달러: 파이낸셜뉴스·아시아경제·와우테일·헤럴드경제 4곳이 같은 값. 2분기 전망 약 910억 달러(헤럴드경제), 범위 891억 8천만~928억 2천만 달러(검색 요약 1건)이 910억 ±2%와 일치.
  - 2027회계연도 2분기(2026-08-26 발표) 매출 962억 2,100만 달러, 전년 대비 106%: 허핑턴포스트코리아·한국경제·토큰포스트·네이트 등 5곳 이상 일치. 3분기 전망 1,080억 달러(시장 예상 1,041억 9천만 달러)는 검색 요약 1건과 보도 제목 기준.
  - 1분기 전망 780억 달러 ±2%(2026-02-25 4분기 발표 때 제시)는 검색 요약 1건. 이 값으로 계산한 상회율 4.6%는 같은 보도의 컨센서스 대비 방향과 모순 없음.
  - 2025-11-19 3분기 실적과 콜(태평양 오후 2시): 엔비디아 뉴스룸·SEC 8-K·GlobeNewswire 검색 결과 다수로 확인.
  - 2027회계연도 3분기 발표일은 확정 근거 없음. 검색 결과 중 한 곳은 11월 19일 목요일, 다른 곳은 11월 20일 수요일로 엇갈려 글에 미공지로 표기.
  - 세율·한도 같은 법정 수치는 없음.
기준일: 2026년 10월 6일 기준
refresh_due: 2026-11-02
refresh_reason: "3분기 발표일 공지가 나오면 발표일 표와 환산 시각을 확정값으로 교체, 발표 뒤에는 3분기 실제 매출 칸 기입. 서머타임 종료일(11월 1일) 지나면 '앞으로' 표현 점검"
tags: 엔비디아 실적발표, 엔비디아 실적발표 시간, 엔비디아 3분기 실적, 엔비디아 가이던스, 엔비디아 실적 한국시간, 서머타임 종료, 미국주식 실적 시즌, 엔비디아 매출, 2027회계연도, 실적 확인 방법
cannibalization_note: |
  컨센서스 글은 예상치 비교 일반론, SK하이닉스 3분기 글은 국내 기업 실적 확인 순서, 미국주식 거래시간 글은 정규장·프리마켓 시간표다. 이 글은 엔비디아 한 종목의 발표일과 콜 시각 환산, 가이던스 대비 실제 매출 계산이라 대상과 의도가 다르다. 세 글로 내부 링크를 건다.
gate_pass: true
gate_pass_note: |
  게이트1 1,230회, 게이트2 v3 통과, 게이트3 가이던스 상회율 계산·발표일 환산표·그림 2장, 게이트4 원문 막힘이라 언론 교차검증으로 대체(매출 숫자는 5곳 이상 일치, 가이던스는 일부 1건 요약). 사람이 발행 전 엔비디아 IR 페이지(investor.nvidia.com)에서 2027회계연도 3분기 발표일 공지 여부와 2분기 보도자료의 매출 962억 2,100만 달러를 한 번 대조하면 더 안전하다. 3분기 발표일은 미공지 표기이므로 공지가 나오면 갱신.
figure_plan: "2장 - (1) 가이던스 vs 실제 매출 막대(크기 비교), (2) 서머타임 전후 한국시간 타임라인(일정·시간). 서로 다른 정보라 합치지 않음"
self_check: |
  [2026-10-06 gate_pass:true]
  후보 경위: 이슈 스캔(10월 공모주 11종목, 실적 시즌) 뒤 실측 8개: 미국 중간선거 증시 20, 엔비디아 실적발표 1,230, 대주주 양도세 기준 230, 코스피200 정기변경 20, 서학개미 1,400, 테슬라 배당 140, FOMC 일정 20, 연말정산 주식 40. 서학개미가 검색량은 170 더 크지만 월 5,000 미만 개념형이라 v3 유형 5에 해당하고 시의성이 없어 뒤로 미룸(다음 후보로 backlog 기록). 엔비디아는 실적 시즌과 서머타임 종료가 겹치는 4~6주 안 이벤트라 유형 1.
  YMYL: 종목 추천·목표가·방향 예측 없음. 증권가 전망치는 싣지 않고, 3분기 시장 예상치는 보도 시점 값임을 표기. 제목·소제목에 전망·추천 단어 없음.
  첫 문장 유형: 문제제기. 직전 142 절차, 141 수치충격 성격, 140 문제제기와는 다른 문장 구조(겹침 가능성 있으나 140과는 2편 거리).
  글 구조 유형: 계산형(첫 H2 바로 아래가 계산 박스, 설명 문단보다 앞). 직전 142 절차형, 141 비교형, 140 계산형(2편 거리, 연속 아님).
  어투 모드: C 사례형(가상 인물 A씨, 가상임을 명시). 직전 142 A, 141 B와 다름. 꾸며낸 1인칭 경험 없음.
  기관 안내 문장 NVIDIA IR·SEC 전부 링크 처리, 출처 목록 5개 전부 링크 처리.
  내부 링크: 컨센서스 글(published), 미국주식 거래시간 글(drafted, 먼저 발행 필요), SK하이닉스 3분기 글(drafted, 먼저 발행 필요).
  AI 티 점검: em대시 0개, 다만 0회, mark 3개, FAQ 5개(직전 142는 6개, 141은 4개), FAQ 헤딩 "알람 맞추기 전에 풀어 둘 의문"(신규), 요약박스 제목 "🟢 알람 맞추기 전 숫자 둘"(초록 신규), H2 6개 중 질문형 2개.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-06</p>

<p>엔비디아 실적을 보려고 알람을 맞췄는데 예상보다 한 시간 늦게 나온다면 서머타임 때문입니다. 2027회계연도 3분기 발표일은 10월 6일 현재 공지되지 않았고, 11월 1일 서머타임이 끝난 뒤 발표라면 미국 오후 5시 콘퍼런스콜은 한국 오전 7시로 환산됩니다.</p>

<div style="background:#eefaf1;border:2px solid #2f9e58;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f6f3e;font-size:18px;">🟢 알람 맞추기 전 숫자 둘</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>최근 두 분기 매출은 회사 전망보다 4.6%, 5.7% 높게 나왔고, 3분기 전망은 1,080억 달러입니다.</li>
    <li>최근 네 번의 발표는 모두 미국 기준 수요일이었고, 한국은 다음 날 목요일 아침이었습니다.</li>
    <li>서머타임 중에는 한국 오전 6시, 종료 뒤에는 오전 7시가 콜 시작 환산값입니다.</li>
  </ul>
</div>

<h2>목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">가이던스 대비 실제 매출 상회율 계산</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">3분기 발표일은 어디까지 알려졌나요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">서머타임 전후 한국시간 환산표</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">발표 직후 확인하는 순서</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">엔비디아 실적이 국내 투자자에게 왜 중요한가</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">알람 맞추기 전에 풀어 둘 의문</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2f9e58;padding-left:12px;margin-top:36px;">가이던스 대비 실제 매출 상회율 계산</h2>

<div style="background:#f8f9fa;border:1px solid #dee2e6;border-radius:8px;padding:14px 18px;margin:16px 0;line-height:1.9;">
  <strong>상회율 = 실제 매출 ÷ 가이던스 − 1</strong><br>
  2027회계연도 1분기: 816.2억 ÷ 780억 = 1.0464, 약 +4.6%<br>
  2027회계연도 2분기: 962.2억 ÷ 910억 = 1.0574, 약 +5.7%<br>
  2027회계연도 3분기: 발표 뒤 실제 매출 ÷ 1,080억 − 1 (단위 억 달러)
</div>

<p>가이던스는 회사가 직전 분기 발표 때 다음 분기 매출을 미리 제시한 값입니다. 엔비디아는 최근 두 분기 모두 이 값을 웃돌았습니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/nvidia-earnings-date-korea-time-1.png" alt="엔비디아 2027회계연도 1분기 전망 780억 달러 대 실제 816.2억, 2분기 전망 910억 대 실제 962.2억, 3분기 전망 1,080억을 비교한 막대그래프" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 헤럴드경제·한국경제 등 보도 교차 확인, 2026-10-06</figcaption></figure>

<p>예를 들어 가상 인물 A씨가 3분기 발표 날 아침에 확인한다고 해 봅시다. A씨는 위 계산식에 발표된 매출만 넣으면 전망 대비 몇 %였는지 바로 알 수 있습니다.</p>

<p>1분기 전망 780억 달러는 2월 4분기 발표 때 ±2% 범위로 제시됐고, 실제 816억 2천만 달러는 이 범위의 위쪽 끝(약 795.6억)보다도 높았습니다. 2분기도 전망 범위 위쪽 끝(약 928억)을 넘긴 962억 2,100만 달러였습니다. <mark>두 분기 연속으로 범위 위쪽을 넘었다는 사실이 이번 3분기 숫자를 볼 때 가장 먼저 비교할 기준선입니다.</mark></p>

<p>3분기 전망치 1,080억 달러는 8월 발표 직후 보도된 값이고, 같은 시점 시장 예상은 1,041억 9천만 달러였습니다. 컨센서스와 가이던스의 차이는 <a href="https://sensitiveboss3.tistory.com/entry/consensus-estimate-check-guide" target="_blank" rel="noopener">컨센서스 뜻과 확인 방법</a> 글에서 계산 예시로 볼 수 있습니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2f9e58;padding-left:12px;margin-top:36px;">3분기 발표일은 어디까지 알려졌나요</h2>

<p>2027회계연도 3분기 발표일은 10월 6일 현재 엔비디아가 공지한 것으로 확인되지 않습니다. 검색 결과에서도 한 곳은 11월 19일 목요일, 다른 곳은 11월 20일 수요일로 엇갈려 어느 쪽도 확정으로 쓰지 않습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:15px;">
  <thead><tr><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">분기</th><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">미국 발표일</th><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">한국 날짜</th><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">확인 수준</th></tr></thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026회계연도 3분기</td><td style="border:1px solid #ddd;padding:8px;">2025-11-19(수)</td><td style="border:1px solid #ddd;padding:8px;">11-20(목)</td><td style="border:1px solid #ddd;padding:8px;">회사 보도자료·SEC 공시 검색 결과로 확인</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026회계연도 4분기</td><td style="border:1px solid #ddd;padding:8px;">2026-02-25(수)</td><td style="border:1px solid #ddd;padding:8px;">02-26(목)</td><td style="border:1px solid #ddd;padding:8px;">언론 보도 "25일(현지시간)"로 확인</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2027회계연도 1분기</td><td style="border:1px solid #ddd;padding:8px;">2026-05-20(수)</td><td style="border:1px solid #ddd;padding:8px;">05-21(목)</td><td style="border:1px solid #ddd;padding:8px;">언론 보도 다수로 확인</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2027회계연도 2분기</td><td style="border:1px solid #ddd;padding:8px;">2026-08-26(수)</td><td style="border:1px solid #ddd;padding:8px;">08-27(목)</td><td style="border:1px solid #ddd;padding:8px;">언론 보도 다수로 확인</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2027회계연도 3분기</td><td style="border:1px solid #ddd;padding:8px;">미공지</td><td style="border:1px solid #ddd;padding:8px;">미공지</td><td style="border:1px solid #ddd;padding:8px;">검색 결과가 서로 달라 확정 안 함</td></tr>
  </tbody>
</table>

<p>최근 네 번이 모두 미국 수요일이었다는 사실만 확인됩니다. <mark>그래도 달력에 적는 날짜는 회사 공지가 뜬 뒤의 날짜여야 합니다.</mark></p>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 날짜를 가장 빨리 아는 방법</strong>
  <p style="margin:8px 0 0 0;">엔비디아는 실적 콘퍼런스콜 일정을 보도자료로 먼저 알립니다. <a href="https://investor.nvidia.com" target="_blank" rel="noopener">엔비디아 투자자 페이지</a>의 이벤트 항목이나 <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&amp;CIK=0001045810&amp;type=8-K&amp;dateb=&amp;owner=include&amp;count=40" target="_blank" rel="noopener">SEC 공시 검색</a>의 8-K 목록에서 확인할 수 있습니다.</p>
</div>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2f9e58;padding-left:12px;margin-top:36px;">서머타임 전후 한국시간 환산표</h2>

<p>콘퍼런스콜이 미국 동부 오후 5시에 시작한다고 보면, 서머타임 중에는 한국 오전 6시이고 종료 뒤에는 오전 7시입니다. 오후 5시 기준은 2025년 11월 콜이 태평양 오후 2시(동부 5시)였다는 값에서 가져온 환산입니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:15px;">
  <thead><tr><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">발표</th><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">적용 시간대</th><th style="border:1px solid #ddd;padding:8px;background:#eefaf1;text-align:left;">콜 시작 환산(한국)</th></tr></thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2025-11-19</td><td style="border:1px solid #ddd;padding:8px;">동부 표준시(EST)</td><td style="border:1px solid #ddd;padding:8px;">11-20 오전 7시</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026-02-25</td><td style="border:1px solid #ddd;padding:8px;">동부 표준시(EST)</td><td style="border:1px solid #ddd;padding:8px;">02-26 오전 7시</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026-05-20</td><td style="border:1px solid #ddd;padding:8px;">서머타임(EDT)</td><td style="border:1px solid #ddd;padding:8px;">05-21 오전 6시</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2026-08-26</td><td style="border:1px solid #ddd;padding:8px;">서머타임(EDT)</td><td style="border:1px solid #ddd;padding:8px;">08-27 오전 6시</td></tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/nvidia-earnings-date-korea-time-2.png" alt="2026년 11월 1일 서머타임 종료를 기준으로 미국 오후 5시가 한국 오전 6시에서 오전 7시로 바뀌는 타임라인" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">환산: 미국 동부 오후 5시 기준, 2026-10-06 확인</figcaption></figure>

<p>2026년 서머타임은 11월 1일(일)에 끝납니다. 3분기 발표가 그 뒤에 나온다면 과거 5월·8월 때보다 1시간 늦게 한국 아침에 닿습니다.</p>

<p>정규장과 프리마켓 시간까지 한 번에 보려면 <a href="https://sensitiveboss3.tistory.com/entry/us-stock-trading-hours-korea-time" target="_blank" rel="noopener">미국주식 거래시간 한국시간 글</a>의 표가 더 편합니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2f9e58;padding-left:12px;margin-top:36px;">발표 직후 확인하는 순서</h2>

<p>발표 직후에는 네 가지만 확인하면 숫자를 틀리지 않고 읽을 수 있습니다. 가상 인물 A씨는 출근길 지하철에서 이 순서로 확인합니다.</p>

<ol style="line-height:1.9;">
  <li><strong>보도자료 매출 숫자</strong>: 기사 제목 대신 회사 보도자료나 SEC 8-K의 매출액을 먼저 봅니다.</li>
  <li><strong>가이던스 대비 계산</strong>: 위 계산식에 1,080억 달러를 넣어 상회율을 구합니다.</li>
  <li><strong>다음 분기 가이던스</strong>: 4분기 가이던스가 새로 나오면 3분기 전망 때와 같은 방식으로 표에 칸을 추가합니다.</li>
  <li><strong>시장 예상과의 차이</strong>: 컨센서스와 비교하는 방법은 앞서 소개한 컨센서스 글에 있습니다.</li>
</ol>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2f9e58;padding-left:12px;margin-top:36px;">엔비디아 실적이 국내 투자자에게 왜 중요한가</h2>

<p>엔비디아 실적은 AI 반도체 수요가 실제 매출로 이어지는지를 보여 주는 숫자라서, 해외 종목을 직접 사지 않는 투자자에게도 간접적으로 닿습니다. 주가 방향을 정해 주는 숫자는 아니고, <mark>시장이 기대한 값과 얼마나 달랐는지가 반응의 재료가 됩니다.</mark></p>

<ul style="line-height:1.9;">
  <li>수요 경로: 엔비디아 매출이 커지면 AI 서버 투자가 이어지는 신호로 읽히고, 부품·메모리 공급망 기업의 실적 기대로 번질 수 있습니다.</li>
  <li>기대 경로: 이미 높은 숫자를 반영해 둔 상태면 전망을 웃돌아도 주가 반응이 작을 수 있습니다.</li>
  <li>환율 경로: 해외주식 투자자는 발표 뒤 가격 변화에 원달러 환율 변화가 겹쳐 수익이 달라집니다.</li>
</ul>

<p>국내 기업 실적 발표를 같은 방식으로 읽고 싶다면 <a href="https://sensitiveboss3.tistory.com/entry/skhynix-q3-earnings-check-order" target="_blank" rel="noopener">SK하이닉스 3분기 실적 발표일과 확인 순서</a> 글이 계산 예시까지 담고 있습니다.</p>

<div style="background:#fffbeb;border:1px solid #f59e0b;border-radius:8px;padding:14px 18px;margin:16px 0;">
  <strong>💡 한 가지만 더</strong>
  <p style="margin:8px 0 0 0;">보도의 "시장 예상치"는 발표 직전 몇 주 사이에도 바뀝니다. 이 글의 1,041억 9천만 달러는 8월 발표 직후 보도 시점 값입니다.</p>
</div>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2f9e58;padding-left:12px;margin-top:36px;">알람 맞추기 전에 풀어 둘 의문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">엔비디아 3분기 실적은 언제 발표되나요?</summary>
  <p style="margin:10px 0 0 0;">2026년 10월 6일 현재 회사가 확정해 알린 날짜는 확인되지 않습니다. 지난해 3분기는 2025년 11월 19일(수)이었고, 올해 5월과 8월 발표도 수요일이었습니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">한국시간으로 몇 시에 나오나요?</summary>
  <p style="margin:10px 0 0 0;">콜이 미국 동부 오후 5시에 시작한다면 서머타임 중에는 한국 오전 6시, 11월 1일 이후에는 오전 7시입니다. 실제 시작 시각은 회사가 일정과 함께 공지합니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">가이던스가 무엇인가요?</summary>
  <p style="margin:10px 0 0 0;">회사가 다음 분기 매출을 미리 제시하는 전망치입니다. 엔비디아는 3분기 매출을 1,080억 달러로 제시했고, 실제 값과의 차이는 상회율로 계산합니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">발표된 매출은 어디서 직접 볼 수 있나요?</summary>
  <p style="margin:10px 0 0 0;"><a href="https://investor.nvidia.com" target="_blank" rel="noopener">엔비디아 투자자 페이지</a>의 보도자료와 SEC에 제출하는 8-K 공시에 있습니다. 두 곳 모두 영어 원문입니다.</p>
</details>
<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">실적이 좋으면 주가도 오르나요?</summary>
  <p style="margin:10px 0 0 0;">단정할 수 없습니다. 주가는 숫자 자체보다 시장이 미리 예상한 값과의 차이에 반응하는 경우가 많아서, 전망을 웃돈 실적에도 움직임이 엇갈릴 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://investor.nvidia.com" target="_blank" rel="noopener">NVIDIA - Investor Relations</a></li>
    <li><a href="https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm" target="_blank" rel="noopener">SEC - NVIDIA 8-K(2027회계연도 2분기 보도자료)</a></li>
    <li><a href="https://biz.heraldcorp.com/article/10742352" target="_blank" rel="noopener">헤럴드경제 - 1분기 매출 816억달러 넘긴 엔비디아, 2분기 매출 910억달러 전망</a></li>
    <li><a href="https://view.asiae.co.kr/article/2026052105483260651" target="_blank" rel="noopener">아시아경제 - 엔비디아, 1Q 매출 816억달러</a></li>
    <li><a href="https://www.hankyung.com/article/202608275604i" target="_blank" rel="noopener">한국경제 - 엔비디아 2분기 실적 심층분석</a></li>
  </ul>
  기준일: 2026년 10월 6일. 엔비디아 보도자료 원문은 이 환경에서 열람하지 못해 언론 보도를 교차 대조했고, 상회율과 환산 시각은 위 숫자로 직접 계산한 값입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 실적 발표 일정과 숫자 읽는 방법을 정리한 정보 글로, 특정 종목의 매수·매도를 권하거나 주가 방향을 예측하지 않습니다. 투자 판단과 그 책임은 투자자 본인에게 있고, 발표일·시각·수치는 바뀔 수 있어 공시 원문과 대조가 필요합니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "엔비디아 실적발표 일정과 한국시간 계산",
  "description": "엔비디아 3분기 실적발표 일정 공지 상태, 최근 두 분기 가이던스 대비 실제 매출 계산, 서머타임 종료 전후 한국시간 환산을 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/nvidia-earnings-date-korea-time-1.png",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-06",
  "dateModified": "2026-10-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/nvidia-earnings-date-korea-time"
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
      "name": "엔비디아 3분기 실적은 언제 발표되나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "2026년 10월 6일 현재 회사가 확정해 알린 날짜는 확인되지 않습니다. 지난해 3분기는 2025년 11월 19일(수)이었고, 올해 5월과 8월 발표도 수요일이었습니다."
      }
    },
    {
      "@type": "Question",
      "name": "한국시간으로 몇 시에 나오나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "콜이 미국 동부 오후 5시에 시작한다면 서머타임 중에는 한국 오전 6시, 11월 1일 이후에는 오전 7시입니다. 실제 시작 시각은 회사가 일정과 함께 공지합니다."
      }
    },
    {
      "@type": "Question",
      "name": "가이던스가 무엇인가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "회사가 다음 분기 매출을 미리 제시하는 전망치입니다. 엔비디아는 3분기 매출을 1,080억 달러로 제시했고, 실제 값과의 차이는 상회율로 계산합니다."
      }
    },
    {
      "@type": "Question",
      "name": "발표된 매출은 어디서 직접 볼 수 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "엔비디아 투자자 페이지의 보도자료와 SEC에 제출하는 8-K 공시에 있습니다. 두 곳 모두 영어 원문입니다."
      }
    },
    {
      "@type": "Question",
      "name": "실적이 좋으면 주가도 오르나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "단정할 수 없습니다. 주가는 숫자 자체보다 시장이 미리 예상한 값과의 차이에 반응하는 경우가 많아서, 전망을 웃돈 실적에도 움직임이 엇갈릴 수 있습니다."
      }
    }
  ]
}
</script>
