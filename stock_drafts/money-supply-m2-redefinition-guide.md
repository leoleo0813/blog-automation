---
keyword: 통화량 뜻
title: 통화량 M2 뜻과 개편 후 달라진 점
slug: money-supply-m2-redefinition-guide
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 820 (PC 70 / 모바일 750)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-03 - 통과]
  WebSearch "통화량 M2 뜻 M1 차이 광의통화 증가율 주가" 상위 8개: brunch.co.kr 2개(개인), academy.gopax.co.kr(거래소 아카데미), eiec.kdi.re.kr(국책 교육), 위키백과, yellow.kr(지표 사이트·개인 블로그), rohw.co.kr(개인 블로그), goodreads 블로그 글.
  1) 진입 여지: 있음. brunch 개인 글 2개, rohw·yellow 같은 개인 블로그가 상위에 섞여 있다.
  2) 검색 의도: 뜻과 M1·M2 차이를 찾는 탐색형. 조회·계산기 아님.
  3) 답 완결 여부: 부분적. 상위는 M0~M3 정의와 M1·M2 구분 중심이고, 2025년 12월 한국은행 통계 개편(ETF 등 수익증권 제외, 8.7%에서 5.2%)과 최신 월 수치를 함께 풀어 준 글은 요약 단계에서 확인하지 못했다(본문 전체는 열지 못함).
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) M1 대 M2 구성 비교표와 개편 전후 비교표(수익증권 제외, 초대형 IB 발행어음 포함).
  (b) 2026년 7월 M2 현재 수치 표(4,225.6조 원, +12.7조 원 등)와 경제주체별 증감 막대 그림.
  (c) 보도에 나온 실제 수치로 한 전월 대비 증가율 검산(12.7 / 4,212.9 = 0.30%)과 증가율 계산식.
primary_source: |
  1차 출처인 한국은행 bok.or.kr WebFetch 1회 EGRESS_BLOCKED(2026-10-03). 뉴스 사이트 2곳(joseilbo, SBS Biz) WebFetch도 EGRESS_BLOCKED라 WebSearch 요약 단계 교차검증만 가능했다.
  교차검증: 2025년 12월 개편(수익증권 제외, 초대형 IB 발행어음 포함, 증가율 8.7%에서 5.2%, 총통화 409조 5천억 원 감소, 1년 병행 공표)은 한국경제·메트로서울·조세일보·네이트(연합 계열)가 충돌 없이 일치. 2026년 7월 수치(4,225.6조 원, +12.7조 원, +0.3%, 전년 동월 대비 +5.8%, 9개월 연속 증가, 2년 미만 정기예적금 +27.3조 원, 기업 +20.6조 원·가계 -11.6조 원)는 이투데이·글로벌이코노믹·포인트데일리·와이드경제·서플·네이트가 일치.
  다만 현재 값 유형의 숫자라 RULES 「독자 관점 점검」 4번에 따라 한국은행 보도자료 원문 대조 전에는 gate_pass를 true로 하지 않는다.
기준일: 2026년 10월 기준 (수치는 2026년 7월 통계, 한국은행 2026년 9월 15일 발표)
refresh_due: 2026-10-16
capture_guide: |
  (1) 왜 필요한가: 이 글의 현재 수치 표(M2 4,225.6조 원, 전월 대비 +12.7조 원·+0.3%, 전년 동월 대비 +5.8%)와 개편 내용(수익증권 제외, 409조 5천억 원 감소, 병행 공표 기간)을 한국은행 원문으로 확인하지 못했습니다. 보도 6곳 이상이 일치하지만, 4,225.6조 원이 개편 후(신) M2 기준이라는 점과 병행 공표의 정확한 기간은 원문으로 한 번 확정해야 합니다.
  (2) 시도할 사이트(우선순위):
    1순위 한국은행 홈페이지(https://www.bok.or.kr) 접속 → 상단 메뉴 '통계' 또는 '보도자료' → 검색창에 "2026년 7월 통화 및 유동성" 입력 → 9월 15일자 보도자료 첫 페이지(M2 평잔, 증가액, 전년동월대비 증가율 표)가 보이게 캡처.
    2순위 한국은행 경제통계시스템 ECOS(https://ecos.bok.or.kr) 접속 → 통계검색에서 "M2(광의통화, 계절조정계열, 평잔)" 검색 → 2026년 7월 값이 보이는 화면 캡처.
    3순위 2025년 12월 개편 안내 보도자료: 한국은행 홈페이지에서 "통화 및 유동성 통계 개편" 검색 → 개편 전후 M2 증가율(8.7%, 5.2%)과 병행 공표 기간이 적힌 부분 캡처.
  (3) 캡처 후: 스크린샷을 대화에 올려주세요. 표 값을 원문대로 확정한 뒤 gate_pass를 true로 바꾸고 refresh_due 다음 항목(8월 통계, 10월 15일 발표 예정)도 반영하겠습니다.
tags: 통화량, 통화량 뜻, M2, 광의통화, M1 협의통화, 통화 및 유동성, 한국은행 통계 개편, 수익증권 제외, M2 증가율, 주식 용어
gate_pass: false
gate_pass_note: |
  게이트1·2·3 충족. 게이트4는 교차검증으로 진행했지만 현재 수치(2026년 7월 M2)가 한국은행 원문 미확인이라 gate_pass:false. 발행 전 사람이 할 일: capture_guide 1순위 화면(7월 통화 및 유동성 보도자료)을 캡처해 올려주세요. 값이 일치하면 gate_pass를 true로 바꾸면 됩니다. 8월 통계가 10월 15일 발표 예정이라 그 전에 발행하면 refresh_due(10월 16일)에 바로 갱신 대상이 됩니다.
self_check: |
  후보 경위: backlog.verified의 단순 순서 대기 후보 중 디플레이션 뜻(900회)을 먼저 검토했으나 게이트2에서 한국은행·KDI·기획재정부·위키·KB·토스뱅크·나무위키 등 사전형 SERP로 채워져 탈락조건 1·3에 해당해 backlog에 기록. 다음 후보 통화량 뜻(830회)을 채택. 버핏지수 뜻(640회)은 시가총액·GDP 최신 수치 출처가 없어 이번 편에서 제외.
  YMYL: 종목 추천·목표가·매매시점 없음. M2 증감으로 주가 방향을 단정하지 않고 경로와 한계를 적음.
  제목 "통화량 M2 뜻과 개편 후 달라진 점" 17자, 금지어 없음, "뜻과 계산 방법" 틀 아님. 슬러그 5단어, -meaning-calculation 접미사 아님.
  첫 문장 유형: 수치충격형(직전 121 정의, 120 문제제기, 119 절차, 118 대비와 다름). 인트로 둘째 문장에 답(M2의 정의) 포함, 메타 문장 없음.
  글 구조 유형: 개념형(첫 H2 안에 가상 직장인 A씨의 돈이 M1과 M2를 오가는 사례 문단 1개). 직전 121 절차형, 120 비교형, 119 계산형과 다름.
  어투 모드: C 사례형(가상 인물 A씨, 가상임을 명시, 합쇼체). 직전 121 A, 120 B와 다름. 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  현재 수치 표: 최신 값·기준 시점·발표 기관(링크)·다음 발표 예정일 포함. 보도 기준 수치임을 표 아래에 명시.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 3개, FAQ 5개(직전 121 6·120 4와 다름), H2 5개 중 "~나요"형 1개. 요약박스 녹색(#eef8ee/#3a9a4a), 제목 "🌱 숫자를 읽기 전에 알아 둘 것", 중간 박스 "💡 ETF가 빠지면 달라지는 점", 마무리 박스 "📝 마무리 메모". FAQ 헤딩 "M2 숫자를 읽다 남는 궁금증". 면책 문구 새 표현.
  기관 링크: 안내 문장·출처 목록 전부 링크 처리(한국은행, ECOS, KDI, 보도). 내부 링크 4개(108 GDP, 100 소비자물가지수, 106 테이퍼링, 61 ETF). 모두 published. 그림 1장(경제주체별 M2 증감 막대).
  발행 글 갱신(refresh): lint_draft --due에 92·98·105편이 현재 수치 부재로 기한 도달. 지표 현재 값의 1차 출처(한국은행·시카고옵션거래소·한국거래소 등) 접속이 불가해 수치를 지어낼 수 없으므로 이번 실행에서는 갱신하지 않고 다음 실행으로 넘김.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-03</p>

<p>2025년 말 한국은행이 통계를 개편하면서 M2 증가율이 개편 전 8.7%에서 개편 후 5.2%로 3.5%포인트 내려앉았습니다. <mark>통화량 M2는 현금과 요구불예금에 2년 미만 예적금, CD, RP 같은 상품을 더한 광의통화</mark>이고, 개편 뒤에는 ETF 등 수익증권이 빠졌습니다.</p>

<div style="background:#eef8ee;border:2px solid #3a9a4a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f6b2c;font-size:18px;">🌱 숫자를 읽기 전에 알아 둘 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>M1은 바로 꺼내 쓰는 돈이고, M2는 거기에 만기 2년 미만의 예적금과 시장형 상품을 더한 범위입니다.</li><li>개편으로 총통화 규모가 409조 5천억 원 줄었고, 개편 후 1년간 새 M2와 옛 M2를 함께 공표합니다.</li><li>2026년 7월 M2는 보도 기준 4,225.6조 원이고, 늘린 쪽은 기업, 줄어든 쪽은 가계였습니다.</li></ul>
</div>

<h2>목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">통화량 M1과 M2는 무엇이 다른가</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2025년 말 개편으로 M2에서 빠진 것과 들어온 것</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2026년 7월 M2 현재 수치</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">M2 증가율 계산법</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 왜 중요한가</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #3a9a4a;padding-left:12px;margin-top:36px;">통화량 M1과 M2는 무엇이 다른가</h2>

<p>월급 300만 원을 받은 직장인 A씨(가상 인물)로 따라가 볼게요. 월급이 통장에 들어와 현금처럼 쓸 수 있는 동안에는 M1에 잡힙니다.</p>

<p>A씨가 그중 1,000만 원을 1년 만기 정기예금에 넣으면 M1에서는 빠지지만 M2에는 그대로 남습니다. 만기가 2년을 넘는 상품으로 옮기면 M2에서도 빠집니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">M1과 M2 구성 비교 (기준일 2026년 10월)</caption>
  <thead>
    <tr style="background:#eef8ee;"><th style="border:1px solid #ddd;padding:8px;">구분</th><th style="border:1px solid #ddd;padding:8px;">부르는 이름</th><th style="border:1px solid #ddd;padding:8px;">들어 있는 것</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">M1</td><td style="border:1px solid #ddd;padding:8px;">협의통화</td><td style="border:1px solid #ddd;padding:8px;">현금, 요구불예금, 수시입출식 저축성예금</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">M2</td><td style="border:1px solid #ddd;padding:8px;">광의통화</td><td style="border:1px solid #ddd;padding:8px;">M1 + 만기 2년 미만 정기예적금, 시장형 상품(CD·RP·표지어음), 금융채, 금전신탁 등</td></tr>
  </tbody>
</table>

<p>뉴스에서 특별한 설명 없이 시중 통화량이라고 하면 대부분 M2를 가리킵니다. 한국은행이 통화 및 유동성 통계로 매달 발표하는 숫자도 M2가 중심이에요.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #3a9a4a;padding-left:12px;margin-top:36px;">2025년 말 개편으로 M2에서 빠진 것과 들어온 것</h2>

<p><mark>개편의 핵심은 ETF 등 수익증권을 M2에서 뺀 것</mark>입니다. 한국은행은 IMF 통화금융통계 매뉴얼 개정을 반영했다고 밝혔고, 초대형 IB 발행어음은 새로 포함했습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">M2 개편 전후 비교 (2025년 12월 발표 보도 기준)</caption>
  <thead>
    <tr style="background:#eef8ee;"><th style="border:1px solid #ddd;padding:8px;">항목</th><th style="border:1px solid #ddd;padding:8px;">개편 전</th><th style="border:1px solid #ddd;padding:8px;">개편 후</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">수익증권(ETF·펀드 등)</td><td style="border:1px solid #ddd;padding:8px;">M2에 포함</td><td style="border:1px solid #ddd;padding:8px;">M2에서 제외</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">초대형 IB 발행어음</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">M2에 새로 포함</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">M2 증가율</td><td style="border:1px solid #ddd;padding:8px;">8.7%</td><td style="border:1px solid #ddd;padding:8px;">5.2% (3.5%포인트 하락)</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">총통화 규모</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">409조 5천억 원 감소</td></tr>
  </tbody>
</table>

<p>같은 돈이라도 어디에 담겨 있느냐에 따라 M2에 잡히기도, 빠지기도 하는 거죠. A씨가 정기예금 1,000만 원을 해지해 ETF를 사면, 개편 전에는 M2 안에서 자리만 옮겼지만 개편 후에는 M2에서 줄어든 것으로 잡힙니다.</p>

<p>한국은행은 혼선을 줄이려고 개편 후 1년간 새 M2와 옛 M2 총액을 함께 공표한다고 밝혔습니다. 두 숫자가 섞이면 증가율 비교가 어긋나므로 어느 기준인지부터 봐야 해요. 이 글의 4,225.6조 원은 보도에서 개편 후 기준으로 소개된 값입니다.</p>

<div style="background:#eef8ee;border:2px solid #3a9a4a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f6b2c;font-size:18px;">💡 ETF가 빠지면 달라지는 점</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>예금에서 ETF·펀드로 돈이 옮겨 가면 새 M2는 줄어드는 쪽으로 움직입니다.</li><li>ETF가 무엇인지 먼저 알고 싶다면 <a href="https://sensitiveboss3.tistory.com/entry/etf-basics-holdings" target="_blank" rel="noopener">ETF 뜻과 구성 종목 보는 법</a> 글부터 읽어 보세요.</li></ul>
</div>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #3a9a4a;padding-left:12px;margin-top:36px;">2026년 7월 M2 현재 수치</h2>

<p>2026년 7월 M2 평균 잔액은 4,225.6조 원으로, 전월보다 12.7조 원(0.3%) 늘어 9개월 연속 증가했습니다. 아래 수치는 한국은행이 2026년 9월 15일 발표한 내용을 전한 보도를 교차해 정리한 값입니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">M2(광의통화, 계절조정 평잔) 최신 수치 (보도 기준 2026년 10월 3일)</caption>
  <thead>
    <tr style="background:#eef8ee;"><th style="border:1px solid #ddd;padding:8px;">항목</th><th style="border:1px solid #ddd;padding:8px;">값</th><th style="border:1px solid #ddd;padding:8px;">기준 시점</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">M2 평균 잔액</td><td style="border:1px solid #ddd;padding:8px;">4,225.6조 원</td><td style="border:1px solid #ddd;padding:8px;">2026년 7월</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">전월 대비 증가</td><td style="border:1px solid #ddd;padding:8px;">+12.7조 원 (+0.3%)</td><td style="border:1px solid #ddd;padding:8px;">2026년 7월</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">전년 동월 대비</td><td style="border:1px solid #ddd;padding:8px;">+5.8%</td><td style="border:1px solid #ddd;padding:8px;">2026년 7월</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2년 미만 정기예적금</td><td style="border:1px solid #ddd;padding:8px;">+27.3조 원 (2022년 12월 이후 최대 증가)</td><td style="border:1px solid #ddd;padding:8px;">2026년 7월</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">옛 M2(수익증권 포함)</td><td style="border:1px solid #ddd;padding:8px;">전월 대비 0.8% 감소</td><td style="border:1px solid #ddd;padding:8px;">2026년 7월</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">발표 기관</td><td style="border:1px solid #ddd;padding:8px;"><a href="https://www.bok.or.kr" target="_blank" rel="noopener">한국은행</a> 통화 및 유동성 (통계는 <a href="https://ecos.bok.or.kr" target="_blank" rel="noopener">ECOS</a>)</td><td style="border:1px solid #ddd;padding:8px;">2026년 9월 15일 발표</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">다음 발표(8월 통계)</td><td style="border:1px solid #ddd;padding:8px;">2026년 10월 15일 예정 (경제지표 일정 서비스 기준)</td><td style="border:1px solid #ddd;padding:8px;">-</td></tr>
  </tbody>
</table>

<p>위 값은 보도 6곳 이상이 일치한 내용이고, 한국은행 원문 대조는 아직 거치지 않았습니다. 발표가 나오면 이 표를 새 값으로 바꿀 거예요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/money-supply-m2-redefinition-guide-1.png" alt="2026년 7월 경제주체별 M2 증감 막대 그림. 비금융 기업 20.6조 원 증가, 기타 부문 6.3조 원 증가, 기타 금융기관 5.7조 원 감소, 가계·비영리단체 11.6조 원 감소" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 한국은행 2026년 7월 통화 및 유동성 보도 내용, 2026년 9월 15일 발표</figcaption></figure>

<p><mark>기업은 20.6조 원 늘었고 가계·비영리단체는 11.6조 원 줄었습니다.</mark> 반도체 수출이 좋은 기업의 여유 자금이 예적금으로 들어온 반면, 가계는 수시입출식 예금이 크게 줄었다고 보도됐어요.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #3a9a4a;padding-left:12px;margin-top:36px;">M2 증가율 계산법</h2>

<p>증가율은 (비교 시점 값 - 기준 시점 값) ÷ 기준 시점 값 x 100으로 구합니다. 7월 수치로 직접 검산해 볼게요.</p>

<ol>
  <li>7월 M2 4,225.6조 원에서 증가액 12.7조 원을 빼면 6월은 4,212.9조 원입니다.</li>
  <li>12.7 ÷ 4,212.9 = 0.0030이라 약 0.30%입니다.</li>
  <li>보도된 전월 대비 0.3%와 같은 값이에요.</li>
</ol>

<p>전월 대비 0.3%를 12개월로 곱하면 약 3.6%가 되어 전년 동월 대비 5.8%와는 다릅니다. 두 숫자는 비교 기준이 달라서 섞어 읽으면 안 돼요. 복리로 이어 붙이는 계산은 <a href="https://sensitiveboss3.tistory.com/entry/gdp-meaning-nominal-real-calculation" target="_blank" rel="noopener">GDP 뜻과 명목 실질 계산</a> 글의 성장률 설명과 같은 방식입니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #3a9a4a;padding-left:12px;margin-top:36px;">주식 투자자에게 왜 중요한가</h2>

<p>M2는 시중에 돌 수 있는 돈의 양을 보여 줘서, 시장이 금리와 유동성을 가늠하는 배경으로 자주 쓰입니다. 시장이 이 숫자를 받아들이는 경로는 보통 이렇게 설명돼요.</p>

<ul>
  <li>M2 증가세가 빨라짐 → 물가 부담이 커질 수 있다는 기대 → 금리 인하 기대가 약해짐</li>
  <li>M2 증가세가 둔해짐 → 시중 자금이 마른다는 해석 → 위험자산 선호가 줄 수 있다는 해석</li>
  <li>돈의 양이 늘어도 기업 예금으로 쌓이면 주식 매수로 바로 이어지지 않을 수 있음</li>
</ul>

<p>A씨처럼 가계 쪽 수시입출식 예금이 줄어든 것은 자금이 다른 곳으로 옮겨 갔을 수 있다는 신호로 읽는 해석이 있습니다. 하지만 그 돈이 주식으로 갔는지, 대출 상환으로 갔는지는 M2만으로 알 수 없어요.</p>

<p>개편 후 M2에서는 ETF 자금이 빠지기 때문에, 증시로 자금이 이동하면 새 M2가 줄어드는 쪽으로 보일 수 있습니다. 물가와 같이 봐야 해서 <a href="https://sensitiveboss3.tistory.com/entry/consumer-price-index-calculation-guide" target="_blank" rel="noopener">소비자물가지수 계산 글</a>을, 중앙은행이 돈을 거두는 방식은 <a href="https://sensitiveboss3.tistory.com/entry/tapering-meaning-qe-schedule" target="_blank" rel="noopener">테이퍼링 뜻과 양적완화 축소 일정</a> 글을 같이 보면 좋습니다.</p>

<div style="background:#eef8ee;border:2px solid #3a9a4a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f6b2c;font-size:18px;">📝 마무리 메모</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>M2 숫자를 볼 때는 개편 후 기준인지 옛 기준인지부터 가려 읽습니다.</li><li>전월 대비와 전년 동월 대비는 서로 다른 기준이라 한 문장에 섞지 않습니다.</li><li>M2 증감만으로 주가 방향을 말할 수 없고, 금리와 물가를 함께 봅니다.</li></ul>
</div>

<h2 style="border-left:6px solid #3a9a4a;padding-left:12px;margin-top:36px;">M2 숫자를 읽다 남는 궁금증</h2>

<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">M1과 M2 중 어느 쪽을 시중 통화량으로 보나요?</summary><p>M2를 시중 통화량으로 부르는 경우가 대부분입니다. M1은 바로 쓸 수 있는 돈만 담아 범위가 좁습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">개편 후 M2에서 ETF가 빠진 이유는 무엇인가요?</summary><p>IMF 통화금융통계 매뉴얼 개정을 반영해 국제 기준에 맞춘 것이라고 한국은행이 밝혔습니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">M2 증가율이 8.7%에서 5.2%로 줄었으면 돈이 사라진 건가요?</summary><p>아닙니다. 계산 범위에서 수익증권을 빼서 숫자가 달라진 것이고, 실제 돈이 사라진 것은 아닙니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">M2가 늘면 주가도 오르나요?</summary><p>같은 방향으로 움직인다고 단정할 수 없습니다. 늘어난 돈이 기업 예금에 머물 수도 있고, 물가와 금리 기대에 따라 해석이 갈립니다.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">M2 최신 숫자는 어디에서 볼 수 있나요?</summary><p><a href="https://ecos.bok.or.kr" target="_blank" rel="noopener">한국은행 경제통계시스템 ECOS</a>에서 M2 계열을 검색하면 월별 값이 나옵니다. 매월 중순 <a href="https://www.bok.or.kr" target="_blank" rel="noopener">한국은행</a> 통화 및 유동성 보도자료가 같이 나와요.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, 아래 자료를 교차해 정리했습니다):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.bok.or.kr" target="_blank" rel="noopener">한국은행 - 통화 및 유동성 보도자료</a></li>
    <li><a href="https://ecos.bok.or.kr" target="_blank" rel="noopener">한국은행 경제통계시스템 ECOS - M2 통계</a></li>
    <li><a href="https://eiec.kdi.re.kr/policy/materialView.do?num=285416" target="_blank" rel="noopener">KDI 경제교육·정보센터 - 2026년 6월 통화 및 유동성</a></li>
    <li><a href="https://www.hankyung.com/amp/2025123034211" target="_blank" rel="noopener">한국경제 - 한은, 통화량 통계에서 ETF 제외</a></li>
    <li><a href="https://www.etoday.co.kr/news/view/2625597" target="_blank" rel="noopener">이투데이 - 7월 시중에 풀린 돈, 9개월째 증가</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 통화량 통계를 풀어 설명하는 정보성 글입니다. 특정 종목이나 상품의 매수·매도를 권하지 않고, 투자 판단과 그 결과의 책임은 투자자 본인에게 있습니다. 본문의 A씨는 설명을 위한 가상 인물이며, 통계 수치는 이후 발표로 바뀔 수 있습니다.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "통화량 M2 뜻과 개편 후 달라진 점",
  "description": "통화량 M2와 M1의 차이, 2025년 말 한국은행 통계 개편으로 ETF 등 수익증권이 빠진 내용, 2026년 7월 M2 4,225.6조 원 수치와 증가율 계산법을 정리했습니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-03",
  "dateModified": "2026-10-03",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/money-supply-m2-redefinition-guide"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/money-supply-m2-redefinition-guide-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "M1과 M2 중 어느 쪽을 시중 통화량으로 보나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "M2를 시중 통화량으로 부르는 경우가 대부분입니다. M1은 바로 쓸 수 있는 돈만 담아 범위가 좁습니다."
      }
    },
    {
      "@type": "Question",
      "name": "개편 후 M2에서 ETF가 빠진 이유는 무엇인가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IMF 통화금융통계 매뉴얼 개정을 반영해 국제 기준에 맞춘 것이라고 한국은행이 밝혔습니다."
      }
    },
    {
      "@type": "Question",
      "name": "M2 증가율이 8.7%에서 5.2%로 줄었으면 돈이 사라진 건가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. 계산 범위에서 수익증권을 빼서 숫자가 달라진 것이고, 실제 돈이 사라진 것은 아닙니다."
      }
    },
    {
      "@type": "Question",
      "name": "M2가 늘면 주가도 오르나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "같은 방향으로 움직인다고 단정할 수 없습니다. 늘어난 돈이 기업 예금에 머물 수도 있고, 물가와 금리 기대에 따라 해석이 갈립니다."
      }
    },
    {
      "@type": "Question",
      "name": "M2 최신 숫자는 어디에서 볼 수 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "한국은행 경제통계시스템 ECOS에서 M2 계열을 검색하면 월별 값이 나옵니다. 매월 중순 한국은행 통화 및 유동성 보도자료가 같이 나와요."
      }
    }
  ]
}
</script>
