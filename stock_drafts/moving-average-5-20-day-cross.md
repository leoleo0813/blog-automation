---
keyword: 이동평균선
title: 이동평균선 5일 20일 계산과 크로스 보는 법
slug: moving-average-5-20-day-cross
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 1060 (PC 370 / 모바일 690)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-01 - 통과]
  WebSearch "이동평균선 뜻 5일 20일 골든크로스 데드크로스 계산 방법" 상위: economybloc.com(경제 용어 사이트), jaenung.net(소규모 콘텐츠 사이트), coinpick.com(차트 교육 사이트), 위키백과. 추가 검색에서 KB 금융용어사전, 한국투자증권 설명 페이지, 위키백과, treasurer.co.kr(소규모 사이트).
  1) 진입 여지: 있음. jaenung.net, coinpick, treasurer 등 소규모 콘텐츠 사이트가 상위에 있다.
  2) 검색 의도: 뜻과 보는 법을 찾는 탐색형. 조회·계산기 실행 의도 아님.
  3) 답 완결 여부: 부분적. 검색 요약은 정의와 기간별 용도, 크로스 개념 중심이었고, 가상 종가 25일치로 5일선·20일선을 표로 계산해 교차일을 찾는 과정과 "빠지는 값/들어오는 값" 증분 계산은 요약 단계에서 확인하지 못했다. 상위 페이지 본문 전체는 열어보지 못했다(자동화 세션 제약).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 가상 종가 25일치로 5일선(5일차 10,130원)·20일선(20일차 10,555원) 단계별 계산.
  (b) 21일차 20일선을 이전 평균 + (들어오는 값 - 빠지는 값) ÷ 20으로 구하는 증분 계산(10,585원).
  (c) 16~25일차 5일선·20일선 비교표와 23~24일차 데드크로스 확인.
  (d) 기간별 이평선 비교표, 흔한 오해 vs 실제 표.
  (추가 2026-10-02) 16~25일차 종가·5일선·20일선 꺾은선 그래프 1장(가상), 신호 지연 6거래일 계산.
primary_source: |
  이동평균선은 기관이 수치를 공표하는 지표가 아니라 수학적 정의라서 1차 수치 출처가 따로 없다.
  금융투자협회 증권 용어사전(kofia.or.kr) WebFetch 1회 시도, EGRESS_BLOCKED. 검색 결과에 해당 사전 페이지가 노출됐으나 본문은 열람하지 못했다.
  WebSearch 2회로 독립 출처를 교차 확인했다: 단순이동평균 = 기간 종가 합 ÷ 기간, 5/20/60/120일 관례, 골든·데드크로스 정의가 KB 금융용어사전, 한국투자증권, 이코노미블록, 위키백과에서 일치. SMA/EMA 구분도 이코노미블록·위키백과가 일치.
기준일: 2026년 10월 기준 (계산 예시는 가상)
tags: 이동평균선, 이평선, 5일선 20일선, 골든크로스, 데드크로스, 단순이동평균, 지수이동평균, 이동평균선 계산, 기술적 지표, 주식 차트
gate_pass: false
gate_pass_note: |
  게이트1 1,090회, 게이트2 v3 통과, 게이트3 계산표·비교표 확보. 게이트4 미충족: 독립 출처 4곳은 일치하고 KB 금융용어사전·한국투자증권(금융사)이 있으나, 금융투자협회 용어사전 원문은 접속 차단으로 열람하지 못했다.
  사람이 할 일: 금융투자협회 증권 용어사전(https://kofia.or.kr/brd/m_117/view.do?seq=11&multi_itm_seq=0&itm_seq_1=0&itm_seq_2=0&page=1)에서 이동평균선 정의를 확인해 출처 목록에 넣으면 true로 바꿀 수 있습니다. 본문 계산값(10,130 / 10,555 / 10,585 / 23일차 10,630 / 24일차 10,550·10,640)은 파이썬으로 재계산해 일치 확인함.
self_check: |
  [2026-10-01 gate_pass:false, 게이트4 금융투자협회 원문 미열람]
  후보 경위: backlog.verified의 단순 순서 대기 후보 중 검색량이 가장 높은 이동평균선(1,090) 채택. 점도표(1,140)는 연준 원문 접속 점검 필요, 연금소득세는 세율 원문 필요라 제외. 신규 키워드 실측은 하지 않음.
  카니벌라이제이션: 볼린저밴드 편이 20일 이동평균을 중심선으로 언급(이동평균선 자체가 주제 아님). 내부 링크로 연결.
  YMYL: 종목 추천·목표가·매매시점 없음. 교차를 매매 신호로 제시하지 않고 후행·예측 아님을 본문·표·FAQ에 명시. 가격은 가상으로 명시.
  기관 링크: 외부 안내 문장 전부 링크 처리, 출처 목록 4개 전부 링크 처리. 금융투자협회 사전은 열람 불가라 본문에 넣지 않음.
  제목 "이동평균선 5일 20일 계산과 크로스 보는 법" 21자, 금지어 없음, 최근 5편의 "~뜻과 ~ 계산(법)" 틀을 피해 "계산과 ~ 보는 법"으로 지음. 슬러그 5단어.
  첫 문장 유형: 대비형(5일선은 날카롭게, 20일선은 느긋하게). 직전 113 절차형, 112 문제제기형, 111 수치충격형, 110 사실제시형과 겹치지 않음. 인트로 둘째 문장에 정의와 5일/20일 답 포함, 메타 문장 없음.
  글 구조 유형: 비교형(첫 H2 첫 블록이 기간별 이평선 비교표). 직전 112 계산형, 111 절차형, 110 시계열+계산형과 겹치지 않음.
  어투 모드: B 대화형(해요체 중심, 독자에게 묻는 문장 포함, 가상 인물 A씨는 예시 설명용). 꾸며낸 1인칭 경험 없음. 섹션마다 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 3개 이상 5개 이하, FAQ 7개(직전 112 6·111 4·110 5와 다름), H2 7개(목차 포함) 중 "~나요"형 0개(FAQ 질문 제외). 요약박스 청록(#e8f6f6/#1f8a8a), 제목 "👀 먼저 짚고 갈 숫자", 마무리 박스 "🧭 기억해 둘 것". FAQ 헤딩 "이평선 보면서 떠오르는 의문". 면책 문구 새 표현.
  [2026-10-02 독자 관점 규칙 반영]
  박스 제목 "헷갈리는" 제거. 그림 1장(교차 구간 꺾은선). "주식 투자자가 이평선을 쓰는 방식과 한계" H2 추가(추세·신호 지연·실적 미포함, 매매 지시 없음). 내부 링크 2개(85 볼린저밴드·93 PER, 발행 완료). FAQ 7개 유지. gate_pass:false 사유(게이트4)는 그대로.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>같은 종가로 그려도 5일선은 날카롭게 꺾이고 20일선은 느긋하게 따라옵니다. 이동평균선은 최근 며칠 종가를 더해 그 날짜 수로 나눈 값을 매일 이어 그린 선이고, 5일선은 5거래일, 20일선은 20거래일 평균이에요. 가상 종가 25일치로 두 선을 직접 계산해서 왜 모양이 다른지, 두 선이 만나는 지점은 어떻게 찾는지 따라가 볼게요.</p>

<div style="background:#e8f6f6;border:2px solid #1f8a8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#14595a;font-size:18px;">👀 먼저 짚고 갈 숫자</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>단순이동평균은 종가를 더해 기간으로 나눈 값입니다. 5일선이면 <mark>5개 합 ÷ 5</mark>예요.</li><li>가상 예시에서 20일선은 20일차에 <mark>10,555원</mark>이고, 하루 지나면 <mark>10,585원</mark>으로 30원 움직입니다.</li><li>같은 예시에서 5일선은 24일차에 10,550원으로 20일선 10,640원 아래로 내려가며 교차가 확인됩니다.</li><li>교차 신호는 이미 지난 가격의 평균끼리 비교한 결과라서, 앞날의 방향을 알려 주지 않습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>5일선, 20일선, 60일선 기간별 차이</li>
  <li>가상 종가로 5일선과 20일선 계산하기</li>
  <li>하루 지날 때 선이 움직이는 원리</li>
  <li>두 선이 만나는 지점 확인하는 순서</li>
  <li>단순 평균과 지수 평균의 차이</li>
  <li>이평선을 볼 때 흔한 오해</li>
  <li>주식 투자자가 이평선을 쓰는 방식과 한계</li>
  <li>이평선 보면서 떠오르는 의문</li>
</ol>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">5일선, 20일선, 60일선 기간별 차이</h2>
<p>기간이 짧을수록 선이 가격을 바짝 따라가고, 길수록 완만해집니다. 아래 표는 기간별로 관례처럼 쓰이는 이름과 성격이에요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">이평선</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">평균에 쓰는 거래일</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">관례적 이름</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">특징</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">5일선</td><td style="border:1px solid #ddd;padding:8px;">최근 5거래일</td><td style="border:1px solid #ddd;padding:8px;">초단기</td><td style="border:1px solid #ddd;padding:8px;">가격에 가장 민감하게 반응</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">20일선</td><td style="border:1px solid #ddd;padding:8px;">최근 20거래일</td><td style="border:1px solid #ddd;padding:8px;">단기</td><td style="border:1px solid #ddd;padding:8px;">약 한 달 흐름, 가장 많이 쓰는 기준선</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">60일선</td><td style="border:1px solid #ddd;padding:8px;">최근 60거래일</td><td style="border:1px solid #ddd;padding:8px;">중기</td><td style="border:1px solid #ddd;padding:8px;">약 석 달 흐름, 움직임이 완만</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">120일선</td><td style="border:1px solid #ddd;padding:8px;">최근 120거래일</td><td style="border:1px solid #ddd;padding:8px;">장기</td><td style="border:1px solid #ddd;padding:8px;">반년 흐름, 방향이 쉽게 안 바뀜</td></tr>
    </tbody>
</table>

<p>이 분류는 증권사 용어 설명과 투자 정보 사이트에서 공통으로 쓰는 관례입니다. 출처는 <a href="https://kbthink.com/dictionary/view.html?dictId=KED-00016769" target="_blank" rel="noopener">KB 금융용어사전 이동평균선</a>과 <a href="https://file.truefriend.com/Storage/navi/W2001_20.html" target="_blank" rel="noopener">한국투자증권 이동평균선 설명</a>에서 확인할 수 있어요.</p>

<p>볼린저밴드의 중심선이 바로 20일 이동평균입니다. 그 지표가 궁금하다면 <a href="https://sensitiveboss3.tistory.com/entry/bollinger-bands-calculation" target="_blank" rel="noopener">볼린저밴드 계산 편</a>을 같이 보세요.</p>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">가상 종가로 5일선과 20일선 계산하기</h2>
<p>A씨가 어떤 주식의 종가를 25일 동안 적었다고 해 볼게요. 아래 값은 설명용 가상 숫자이고 실제 종목 가격이 아닙니다.</p>

<p>5일선은 5일차부터 만들 수 있어요. 1~5일차 종가는 10,000, 10,100, 10,050, 10,200, 10,300원입니다.</p>

<ol style="line-height:1.9;">
  <li>5개를 모두 더하면 50,650원</li>
  <li>5로 나누면 <mark>10,130원</mark>이 5일차 5일선 값</li>
  <li>6일차는 2~6일차 종가 5개로 새로 평균을 냅니다</li>
</ol>

<p>20일선은 20일차에야 처음 나옵니다. 1~20일차 종가 20개의 합이 211,100원이라 20으로 나누면 10,555원이에요.</p>

<div style="background:#e8f6f6;border:2px solid #1f8a8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#14595a;font-size:18px;">📝 계산할 때 놓치기 쉬운 지점</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>평균에 쓰는 날짜 수가 모자라면 선이 아직 안 그려집니다. 20일선은 19일차까지 값이 없어요.</li><li>휴장일은 거래일에 들어가지 않으니, 달력 날짜가 아니라 장이 열린 날로 세어야 합니다.</li></ul>
</div>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">하루 지날 때 선이 움직이는 원리</h2>
<p>새 평균은 이전 평균에서 빠지는 값과 들어오는 값만 반영해 구할 수 있어요. 새 평균 = 이전 평균 + (들어오는 종가 - 빠지는 종가) ÷ 기간이라는 식입니다.</p>

<p>21일차를 예로 들어 볼까요? 21일차 종가는 10,600원이고, 20일선에서 빠지는 값은 1일차 종가 10,000원이에요.</p>

<ol style="line-height:1.9;">
  <li>들어오는 값 - 빠지는 값 = 10,600 - 10,000 = 600원</li>
  <li>600 ÷ 20 = 30원</li>
  <li>10,555 + 30 = <mark>10,585원</mark></li>
</ol>

<p>같은 600원 차이가 5일선에서는 5로 나뉘기 때문에 네 배 큰 120원으로 반영돼요. 5일선이 빠르고 20일선이 느린 이유가 이 나눗셈 하나입니다.</p>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">두 선이 만나는 지점 확인하는 순서</h2>
<p>5일선이 20일선을 아래에서 위로 넘으면 골든크로스, 위에서 아래로 넘으면 데드크로스라고 불러요. 두 선의 값 차이가 플러스에서 마이너스로 바뀌는 날을 찾으면 됩니다.</p>

<p>아래 표는 가상 종가의 16~25일차 구간입니다. 마지막 칸은 5일선에서 20일선을 뺀 값이에요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">일차</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">종가(가상)</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">5일선</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">20일선</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">5일선 - 20일선</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">16일차</td><td style="border:1px solid #ddd;padding:8px;">10,950원</td><td style="border:1px solid #ddd;padding:8px;">10,830원</td><td style="border:1px solid #ddd;padding:8px;">계산 전</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">17일차</td><td style="border:1px solid #ddd;padding:8px;">11,000원</td><td style="border:1px solid #ddd;padding:8px;">10,900원</td><td style="border:1px solid #ddd;padding:8px;">계산 전</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">18일차</td><td style="border:1px solid #ddd;padding:8px;">10,900원</td><td style="border:1px solid #ddd;padding:8px;">10,920원</td><td style="border:1px solid #ddd;padding:8px;">계산 전</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">19일차</td><td style="border:1px solid #ddd;padding:8px;">10,800원</td><td style="border:1px solid #ddd;padding:8px;">10,900원</td><td style="border:1px solid #ddd;padding:8px;">계산 전</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">20일차</td><td style="border:1px solid #ddd;padding:8px;">10,700원</td><td style="border:1px solid #ddd;padding:8px;">10,870원</td><td style="border:1px solid #ddd;padding:8px;">10,555원</td><td style="border:1px solid #ddd;padding:8px;">+315원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">21일차</td><td style="border:1px solid #ddd;padding:8px;">10,600원</td><td style="border:1px solid #ddd;padding:8px;">10,800원</td><td style="border:1px solid #ddd;padding:8px;">10,585원</td><td style="border:1px solid #ddd;padding:8px;">+215원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">22일차</td><td style="border:1px solid #ddd;padding:8px;">10,500원</td><td style="border:1px solid #ddd;padding:8px;">10,700원</td><td style="border:1px solid #ddd;padding:8px;">10,605원</td><td style="border:1px solid #ddd;padding:8px;">+95원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">23일차</td><td style="border:1px solid #ddd;padding:8px;">10,550원</td><td style="border:1px solid #ddd;padding:8px;">10,630원</td><td style="border:1px solid #ddd;padding:8px;">10,630원</td><td style="border:1px solid #ddd;padding:8px;">+0원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">24일차</td><td style="border:1px solid #ddd;padding:8px;">10,400원</td><td style="border:1px solid #ddd;padding:8px;">10,550원</td><td style="border:1px solid #ddd;padding:8px;">10,640원</td><td style="border:1px solid #ddd;padding:8px;">-90원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">25일차</td><td style="border:1px solid #ddd;padding:8px;">10,300원</td><td style="border:1px solid #ddd;padding:8px;">10,470원</td><td style="border:1px solid #ddd;padding:8px;">10,640원</td><td style="border:1px solid #ddd;padding:8px;">-170원</td></tr>
    </tbody>
</table>

<p>23일차에 두 선이 10,630원으로 같아지고, 24일차에는 5일선 10,550원이 20일선 10,640원 아래로 내려갑니다. 이 구간이 이 가상 예시의 데드크로스예요.</p>

<p>교차가 확인되는 시점은 가격이 정점(17일차 11,000원)을 지나고 한참 뒤인 23~24일차입니다. 평균은 지나간 값으로 만들어서 신호가 가격보다 늦게 나와요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/moving-average-5-20-day-cross-1.png" alt="16일차부터 25일차까지 가상 종가와 5일선, 20일선 꺾은선 그래프. 종가는 17일차 11,000원이 정점이고, 5일선이 내려와 23일차에 20일선과 10,630원에서 만난 뒤 아래로 내려감" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산 예시: 본문 가상 종가</figcaption></figure>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">단순 평균과 지수 평균의 차이</h2>
<p>이 글의 계산은 모두 단순이동평균(SMA)입니다. 지수이동평균(EMA)은 최근 값에 더 큰 비중을 주는 방식이에요.</p>

<ul style="line-height:1.9;">
  <li>SMA: 기간 안의 모든 종가를 같은 비중으로 평균</li>
  <li>EMA: 최근 종가일수록 비중이 큰 평균, 가격 변화에 더 빨리 반응</li>
  <li>같은 20일이라도 두 방식의 값은 다르게 나옵니다</li>
</ul>

<p>두 방식의 정의는 <a href="https://economybloc.com/article/37380/" target="_blank" rel="noopener">이코노미블록 이동평균선 설명</a>과 <a href="https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%8F%99%ED%8F%89%EA%B7%A0%EC%84%A0" target="_blank" rel="noopener">위키백과 이동평균선</a>에서도 같은 구분으로 나옵니다. 차트에서 이평선 값이 다르게 보이면 방식 항목이 SMA인지 EMA인지 먼저 보세요.</p>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">이평선을 볼 때 흔한 오해</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">흔한 오해</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">실제</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">골든크로스가 나오면 오른다</td><td style="border:1px solid #ddd;padding:8px;">두 평균의 위치 관계가 바뀌었다는 사실만 알려 줌. 이후 방향은 보장되지 않음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5일선이 20일선보다 정확하다</td><td style="border:1px solid #ddd;padding:8px;">빠를 뿐 정확한 건 아님. 잔 움직임에도 자주 흔들림</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">이평선은 미래 가격을 보여 준다</td><td style="border:1px solid #ddd;padding:8px;">과거 종가의 평균이라 후행 지표임</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">선이 가격에 닿으면 반드시 튕긴다</td><td style="border:1px solid #ddd;padding:8px;">가격이 선을 지나치는 경우도 많음. 규칙이 아니라 해석의 관례</td></tr>
    </tbody>
</table>

<div style="background:#e8f6f6;border:2px solid #1f8a8a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#14595a;font-size:18px;">🧭 기억해 둘 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>이평선은 종가를 더해 기간으로 나눈 값을 이은 선입니다.</li><li>기간이 짧을수록 빠르고, 길수록 완만합니다.</li><li>교차는 지나간 가격끼리의 비교라 신호가 늦고, 예측이 아닙니다.</li></ul>
</div>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">주식 투자자가 이평선을 쓰는 방식과 한계</h2>

<p>이평선은 차트를 처음 열면 가장 먼저 보이는 선이라, 쓰는 방식과 한계를 같이 알아 두는 편이 좋아요.</p>

<ul style="line-height:1.9;">
  <li><strong>추세 확인:</strong> 가격이 120일선 위에 오래 머무는지 아래에 머무는지로 반년 흐름을 한눈에 봅니다. 선의 기울기가 위인지 아래인지도 같이 봐요.</li>
  <li><strong>신호가 늦게 옵니다:</strong> 위 예시에서 종가 정점은 17일차였는데 두 선이 만난 건 23일차였어요. 6거래일 늦게 확인된 셈이고, 그 사이 종가는 11,000원에서 10,550원으로 내려와 있었습니다.</li>
  <li><strong>실적은 들어 있지 않아요:</strong> 이평선은 가격만으로 만든 선이라 회사가 돈을 얼마나 버는지는 담지 않습니다. 가격이 이익에 비해 어느 수준인지는 <a href="https://sensitiveboss3.tistory.com/entry/per-meaning-calculation" target="_blank" rel="noopener">PER 계산 글</a> 같은 가치 지표로 따로 봐요.</li>
</ul>

<p>골든크로스나 데드크로스 같은 이름이 붙어 있어도, 지나간 가격의 평균끼리 순서가 바뀌었다는 기록이에요. 이 신호만으로 매수나 매도를 정하는 건 일반적인 사용법이 아닙니다.</p>

<h2 style="border-left:6px solid #1f8a8a;padding-left:12px;margin-top:36px;">이평선 보면서 떠오르는 의문</h2>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">이동평균선은 종가로만 그리나요?</summary><p>대부분의 차트는 종가를 기본값으로 씁니다. 지표 설정에서 시가나 고가를 고르게 만든 서비스도 있으니, 쓰는 차트의 기본 설정을 먼저 확인해 보세요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">5일선이 20일선보다 먼저 움직이는 이유는 뭔가요?</summary><p>평균에 들어가는 날짜 수가 적기 때문입니다. 5일선은 하루 값이 5분의 1, 20일선은 20분의 1만 반영되어서 같은 하루 변화에도 5일선이 네 배 크게 반응합니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">골든크로스가 나오면 오른다는 뜻인가요?</summary><p>아닙니다. 골든크로스는 단기 평균이 장기 평균을 위로 넘었다는 사실만 알려 줍니다. 이미 오른 가격을 평균이 뒤따라온 결과일 수 있어서 앞으로의 방향을 보장하지 않습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">차트마다 이평선 값이 조금씩 다른 건 왜 그런가요?</summary><p>평균 방식(단순 또는 지수)과 기준 가격(종가 등), 거래일 수 처리가 서비스마다 다를 수 있기 때문입니다. 값이 어긋나면 지표 설정의 방식 항목부터 비교해 보세요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">종목마다 이평선 기간을 다르게 써도 되나요?</summary><p>정해진 정답은 없습니다. 5, 20, 60, 120일이 관례로 많이 쓰이지만 어떤 기간이 더 잘 맞는다고 확정할 근거는 없어서, 기간을 바꾸면 신호 시점도 함께 달라진다는 점만 알고 쓰면 됩니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">이동평균선 계산을 엑셀로 해 볼 수 있나요?</summary><p>가능합니다. 종가를 한 열에 적고 AVERAGE 함수로 최근 5칸, 20칸을 묶어 아래로 끌어 내리면 이 글의 표와 같은 값이 나옵니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">이평선만 보고 판단해도 괜찮을까요?</summary><p>이동평균선은 지나간 가격의 평균이라 후행 지표입니다. 거래량, 실적, 공시 같은 다른 정보와 따로 떼어 해석하면 오해하기 쉽고, 이 글도 매매 판단 기준을 제시하지 않습니다.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (2026년 10월 기준):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://kbthink.com/dictionary/view.html?dictId=KED-00016769" target="_blank" rel="noopener">KB 금융용어사전 - 이동평균선이란</a></li>
    <li><a href="https://file.truefriend.com/Storage/navi/W2001_20.html" target="_blank" rel="noopener">한국투자증권 - 이동평균선</a></li>
    <li><a href="https://economybloc.com/article/37380/" target="_blank" rel="noopener">이코노미블록 - 이동평균선(MA)이란</a></li>
    <li><a href="https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%8F%99%ED%8F%89%EA%B7%A0%EC%84%A0" target="_blank" rel="noopener">위키백과 - 이동평균선</a></li>
  </ul>
  <p>본문 계산 예시의 종가는 모두 설명용 가상 값입니다.</p>
</div>

<p style="font-size:13px;color:#888;">이 글은 지표의 계산 방법을 설명하는 정보 글이며, 특정 종목이나 상품을 사거나 팔라고 권하지 않습니다. 투자 결정과 그 결과는 투자자 본인의 몫이고, 서비스마다 지표 설정이 다를 수 있으니 사용하는 차트의 기준을 직접 확인해 주세요.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "이동평균선 5일 20일 계산과 크로스 보는 법",
  "description": "5일선과 20일선을 가상 종가 25일치로 직접 계산하고, 두 선이 만나는 골든크로스와 데드크로스를 확인하는 순서를 정리했습니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/moving-average-5-20-day-cross"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/moving-average-5-20-day-cross-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "이동평균선은 종가로만 그리나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "대부분의 차트는 종가를 기본값으로 씁니다. 지표 설정에서 시가나 고가를 고르게 만든 서비스도 있으니, 쓰는 차트의 기본 설정을 먼저 확인해 보세요."
      }
    },
    {
      "@type": "Question",
      "name": "5일선이 20일선보다 먼저 움직이는 이유는 뭔가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "평균에 들어가는 날짜 수가 적기 때문입니다. 5일선은 하루 값이 5분의 1, 20일선은 20분의 1만 반영되어서 같은 하루 변화에도 5일선이 네 배 크게 반응합니다."
      }
    },
    {
      "@type": "Question",
      "name": "골든크로스가 나오면 오른다는 뜻인가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. 골든크로스는 단기 평균이 장기 평균을 위로 넘었다는 사실만 알려 줍니다. 이미 오른 가격을 평균이 뒤따라온 결과일 수 있어서 앞으로의 방향을 보장하지 않습니다."
      }
    },
    {
      "@type": "Question",
      "name": "차트마다 이평선 값이 조금씩 다른 건 왜 그런가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "평균 방식(단순 또는 지수)과 기준 가격(종가 등), 거래일 수 처리가 서비스마다 다를 수 있기 때문입니다. 값이 어긋나면 지표 설정의 방식 항목부터 비교해 보세요."
      }
    },
    {
      "@type": "Question",
      "name": "종목마다 이평선 기간을 다르게 써도 되나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정해진 정답은 없습니다. 5, 20, 60, 120일이 관례로 많이 쓰이지만 어떤 기간이 더 잘 맞는다고 확정할 근거는 없어서, 기간을 바꾸면 신호 시점도 함께 달라진다는 점만 알고 쓰면 됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "이동평균선 계산을 엑셀로 해 볼 수 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "가능합니다. 종가를 한 열에 적고 AVERAGE 함수로 최근 5칸, 20칸을 묶어 아래로 끌어 내리면 이 글의 표와 같은 값이 나옵니다."
      }
    },
    {
      "@type": "Question",
      "name": "이평선만 보고 판단해도 괜찮을까요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이동평균선은 지나간 가격의 평균이라 후행 지표입니다. 거래량, 실적, 공시 같은 다른 정보와 따로 떼어 해석하면 오해하기 쉽고, 이 글도 매매 판단 기준을 제시하지 않습니다."
      }
    }
  ]
}
</script>
