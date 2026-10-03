---
keyword: 미국주식 거래시간
title: 미국주식 거래시간 한국시간, 11월 1일부터 바뀌는 시간
slug: us-stock-trading-hours-korea-time
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 20730 (backlog 실측, 주제 선정 v3 priority_queue 1순위)
gate1_pass: true (일반 주제 기준 월 500 이상)
serp_check: |
  [게이트2 v4 판정 2026-10-03 - 통과]
  2026-09-17 v3 판정에서는 상위 10개가 증권사 안내로 채워져 탈락했으나, 주제 선정 v3/게이트2 v4(월 5,000 이상은 정보이득이 있으면 통과)로 재판정.
  정보이득: (1) 서머타임 전후 한국시간 한 장 비교표(프리·정규·애프터·주간거래), (2) 남은 2026년 휴장·조기폐장의 한국시간 환산표, (3) 12월 6일 시작 미국 거래소 23x5 야간 세션의 한국시간 환산. 증권사 안내 페이지는 자사 서비스 시간 위주라 (2)(3)을 한 글에서 다루지 않음.
unique_asset: |
  (a) 서머타임 전후 4개 시간대 한국시간 비교표와 하루 막대 그림 1장.
  (b) 2026년 남은 휴장·조기폐장 한국시간 환산표(날짜 밀림 표시).
  (c) 12월 6일 야간 세션 한국시간 환산표(11:00~18:00, 정비 10:00~11:00).
primary_source: |
  NYSE 휴장 일정 PDF와 거래소 원문은 WebFetch 시도 없이 WebSearch 결과로 확인(이 세션 해외 일부 사이트 접근 제한).
  서머타임 2026-11-01 종료: 미주중앙일보(2026-10-02)·국내 블로그 다수 일치. 2027-03-14 시작은 3월 둘째 일요일 규칙으로 계산.
  정규장 9:30~16:00 ET, 프리 4:00~9:30, 애프터 16:00~20:00: 거래소 표준 시간, 다수 출처 일치.
  휴장 11/26, 조기폐장 11/27·12/24 13:00 ET, 12/25 휴장: Fidelity·finder·stockmarkethours·NYSE 발표 PDF 검색 요약 일치. 2027-01-01 휴장은 NYSE 2026~2028 발표 범위.
  주간거래 재개(2025년 11월~)와 해제 후 10:00~18:00: KB증권 안내·네이트 보도.
  12월 6일 23x5: WilmerHale(2026-09-29), Markets Media, Cboe FAQ, massive.com 일치. SEC 6월 26일 SIP 운영시간 연장 승인, 야간 세션 21:00~04:00 ET, 정비 20:00~21:00 ET.
기준일: 2026년 10월 3일 기준(증권사별 제공 시간은 각 증권사 안내 기준)
refresh_due: 2026-11-02
refresh_reason: "서머타임 종료 뒤 인트로·표의 '지금' 시제를 해제 기준으로 바꾸고, 12월 6일 야간 세션 국내 증권사 연결 공지 확인(다음 기한 2026-12-07)"
tags: 미국주식 거래시간, 미국주식 거래시간 한국시간, 서머타임 종료, 미국주식 프리마켓, 애프터마켓, 미국주식 주간거래, 미국증시 휴장일, 추수감사절 휴장, 미국 23시간 거래, 나스닥 야간거래
gate_pass: true
gate_pass_note: |
  게이트1 20,730회, 게이트2 v4 통과, 게이트3 비교표 3개·그림 1장, 게이트4 교차검증(공식 원문 직접 열람은 못 함).
  사람 확인 권장: 내 증권사 앱의 해외주식 거래시간 안내에서 주간거래 10:00~18:00(해제 후)만 한 번 대조. 12월 6일 일정이 바뀌면 해당 섹션 수정.
self_check: |
  [2026-10-03 gate_pass:true, 주제 선정 v3 첫 글]
  후보 경위: priority_queue 1순위(검색량 20,730, 11월 1일 서머타임 종료라는 4주 안 이슈).
  카니벌라이제이션: 49편 넥스트레이드(국내 거래시간)·80편 동시호가와 주제가 다름(미국장). 22·15·5편으로 내부 링크 3개.
  YMYL: 거래 시점 권유 없음. 증권사별 시간은 단정하지 않고 거래소 기준과 구분.
  첫 문장 유형: 사실 제시형(지금 시간 → 바뀌는 시간). 어투 B(해요체). 구조: 비교표 중심 + 이슈 섹션.
  투자자 섹션 소제목은 규칙 문구를 그대로 쓰지 않고 "시간대별로 주문이 다르게 체결되는 이유", 문단형(굵은 라벨 목록 아님).
  FAQ 5개(직전 123편 7개·124편 6개와 다름), 헤딩 "미국장 시간 Q&A 5개". mark 3개, em대시 0.
  그림 1장(한국시간 하루 막대), GitHub 원본 주소.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-03</p>

<p>미국주식 정규장은 지금 한국시간 밤 10시 30분에 열려 다음 날 새벽 5시에 닫혀요. 11월 1일(일) 미국 서머타임이 끝나면 모든 시간이 한 시간씩 늦어져서, 11월 2일(월) 밤부터는 밤 11시 30분~새벽 6시가 돼요. 12월 6일부터는 미국 거래소가 밤샘 거래를 시작할 예정이라, 한국 낮 시간에도 거래소 호가가 생겨요.</p>

<div style="background:#ecfeff;border:2px solid #0e7490;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#155e75;font-size:18px;">🕒 시계 맞추기 전에 볼 숫자</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>정규장 기준은 미국 동부시간 오전 9시 30분~오후 4시예요. 한국과는 서머타임 때 13시간, 해제 뒤 14시간 차이가 나요.</li>
    <li>서머타임 마지막 정규장은 미국 10월 30일(금), 한국시간 10월 30일 밤~31일 새벽이에요.</li>
    <li>11월 26일(목)은 추수감사절 휴장이고, 27일과 12월 24일은 미국시간 오후 1시에 일찍 끝나요.</li>
    <li>2027년 서머타임은 3월 14일(일)에 다시 시작해요.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">지금 시간과 11월 2일부터 시간 비교</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">서머타임 날짜와 한국시간 계산법</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2026년 남은 휴장일과 조기 폐장</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">12월 6일부터 미국 거래소 밤샘 거래 시작</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">시간대별로 주문이 다르게 체결되는 이유</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">미국장 시간 Q&amp;A 5개</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">지금 시간과 11월 2일부터 시간 비교</h2>

<p>11월 1일을 기준으로 미국 거래소의 모든 시간대가 한국시간으로 한 시간씩 뒤로 밀려요. 미국 현지 시각은 그대로이고, 미국 시계가 한 시간 늦춰지면서 한국과의 차이가 13시간에서 14시간으로 커지기 때문이에요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">구분</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">미국 동부시간</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">한국시간 ~10월 31일</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">한국시간 11월 2일~</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">프리마켓</td><td style="border:1px solid #ddd;padding:8px;">04:00~09:30</td><td style="border:1px solid #ddd;padding:8px;">17:00~22:30</td><td style="border:1px solid #ddd;padding:8px;">18:00~23:30</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;"><mark>정규장</mark></td><td style="border:1px solid #ddd;padding:8px;">09:30~16:00</td><td style="border:1px solid #ddd;padding:8px;">22:30~다음 날 05:00</td><td style="border:1px solid #ddd;padding:8px;">23:30~다음 날 06:00</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">애프터마켓</td><td style="border:1px solid #ddd;padding:8px;">16:00~20:00</td><td style="border:1px solid #ddd;padding:8px;">05:00~09:00</td><td style="border:1px solid #ddd;padding:8px;">06:00~10:00</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">주간거래(국내 증권사)</td><td style="border:1px solid #ddd;padding:8px;">20:00~04:00</td><td style="border:1px solid #ddd;padding:8px;">09:00~17:00</td><td style="border:1px solid #ddd;padding:8px;">10:00~18:00</td></tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/us-stock-trading-hours-korea-time-1.png" alt="미국주식 거래시간을 한국시간 하루 막대로 그린 그림. 서머타임 기간에는 주간거래 9시~17시, 프리마켓 17시~22시 30분, 정규장 22시 30분~다음 날 5시, 애프터 5시~9시이고, 11월 2일부터는 모두 1시간씩 늦어짐" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 미국 거래소 운영 시간을 한국시간으로 환산, 2026년 10월 기준</figcaption></figure>

<p>표의 프리마켓·애프터마켓은 미국 거래소 기준이라, 증권사마다 실제로 열어 주는 시간은 이보다 짧을 수 있어요. 주간거래는 국내 증권사가 미국 대체거래소(ATS)를 통해 제공하는 서비스예요. 2024년 대체거래소 장애로 체결된 거래가 일괄 취소된 뒤 1년 넘게 멈췄다가 2025년 11월부터 증권사별로 다시 열렸어요(<a href="https://www.kbsec.com/go.able?linkcd=s060901010000&amp;seq=10009104&amp;idt=20251022" target="_blank" rel="noopener">KB증권 주간거래 재개 안내</a>, <a href="https://news.nate.com/view/20250924n17646" target="_blank" rel="noopener">관련 보도</a>). 서머타임 해제 뒤 주간거래 시간이 10:00~18:00로 바뀌는 것도 같은 안내에 나와요.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">서머타임 날짜와 한국시간 계산법</h2>

<p>미국 서머타임은 3월 둘째 일요일에 시작해 11월 첫째 일요일에 끝나요. 2026년은 <mark>11월 1일(일) 새벽 2시(미국 현지)</mark>에 끝나고(<a href="https://www.koreadaily.com/article/20261002153320566" target="_blank" rel="noopener">미주중앙일보</a>), 같은 규칙으로 2027년은 3월 14일(일)에 다시 시작해요.</p>

<ul style="line-height:1.9;">
  <li>서머타임 기간: 한국시간 = 미국 동부시간 + 13시간</li>
  <li>서머타임 해제 기간: 한국시간 = 미국 동부시간 + 14시간</li>
  <li>예: 정규장 개장 9시 30분 + 14시간 = 한국시간 밤 11시 30분</li>
</ul>

<p>헷갈리기 쉬운 건 날짜예요. 미국 월요일 장은 한국 월요일 밤에 열려 화요일 새벽에 닫혀요. 그래서 미국 기준 10월 30일(금) 장이 서머타임의 마지막 장이고, 바뀐 시간은 한국시간 11월 2일(월) 밤 개장부터 적용돼요.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">2026년 남은 휴장일과 조기 폐장</h2>

<p>연말에는 미국 휴장일과 조기 폐장일이 몰려 있어요. 한국시간으로 바꾸면 날짜가 하루 밀리는 경우가 있어 표로 따로 정리했어요. 휴장·조기 폐장 일정은 <a href="https://s2.q4cdn.com/154085107/files/doc_news/NYSE-Group-Announces-2026-2027-and-2028-Holiday-and-Early-Closings-Calendar-2025.pdf" target="_blank" rel="noopener">NYSE의 2026~2028년 휴장 일정 발표</a>와 <a href="https://www.fidelity.com/learning-center/smart-money/stock-market-holidays" target="_blank" rel="noopener">피델리티 휴장일 안내</a>가 같아요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">미국 날짜</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">내용</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">한국시간으로는</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">11월 26일(목)</td><td style="border:1px solid #ddd;padding:8px;">추수감사절 휴장</td><td style="border:1px solid #ddd;padding:8px;">11월 26일 밤 정규장 없음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">11월 27일(금)</td><td style="border:1px solid #ddd;padding:8px;">오후 1시 조기 폐장</td><td style="border:1px solid #ddd;padding:8px;">11월 27일 밤 11시 30분 개장 → 28일(토) 새벽 3시 마감</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12월 24일(목)</td><td style="border:1px solid #ddd;padding:8px;">오후 1시 조기 폐장</td><td style="border:1px solid #ddd;padding:8px;">12월 24일 밤 11시 30분 개장 → 25일 새벽 3시 마감</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12월 25일(금)</td><td style="border:1px solid #ddd;padding:8px;">크리스마스 휴장</td><td style="border:1px solid #ddd;padding:8px;">12월 25일 밤 정규장 없음</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2027년 1월 1일(금)</td><td style="border:1px solid #ddd;padding:8px;">새해 첫날 휴장</td><td style="border:1px solid #ddd;padding:8px;">1월 1일 밤 정규장 없음</td></tr>
  </tbody>
</table>

<p>조기 폐장일에는 정규장이 3시간 30분만 열려요. 평소처럼 새벽 6시까지 열린다고 생각하고 주문을 미뤄 두면 장이 이미 끝나 있을 수 있어요.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">12월 6일부터 미국 거래소 밤샘 거래 시작</h2>

<p>올해 미국 주식시장의 가장 큰 변화는 거래소 밤샘 거래예요. 미국 증권거래위원회(SEC)가 시세 정보를 모아 뿌리는 시스템(SIP)의 운영 시간 연장을 승인했고, <mark>2026년 12월 6일(일) 미국 동부시간 밤 9시</mark>부터 평일 23시간 거래 체제가 시작될 예정이에요(<a href="https://www.wilmerhale.com/en/insights/client-alerts/20260929-23x5-trading-comes-to-us-exchanges-what-firms-should-know-before-launch" target="_blank" rel="noopener">WilmerHale 분석</a>, <a href="https://www.marketsmedia.com/nasdaq-aims-to-debut-23-5-trading-on-6-december-2026/" target="_blank" rel="noopener">Markets Media 보도</a>).</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">항목</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">미국 동부시간</th><th style="border:1px solid #ddd;padding:8px;background:#f0f0f0;">한국시간(서머타임 해제 기준)</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">새 야간 세션</td><td style="border:1px solid #ddd;padding:8px;">21:00~다음 날 04:00</td><td style="border:1px solid #ddd;padding:8px;">11:00~18:00</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">시스템 정비로 멈추는 시간</td><td style="border:1px solid #ddd;padding:8px;">20:00~21:00</td><td style="border:1px solid #ddd;padding:8px;">10:00~11:00</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">첫 거래 시작</td><td style="border:1px solid #ddd;padding:8px;">12월 6일(일) 21:00</td><td style="border:1px solid #ddd;padding:8px;">12월 7일(월) 11:00</td></tr>
  </tbody>
</table>

<p>SEC가 조건부로 승인한 거래소는 나스닥, NYSE Arca, Cboe EDGX, 24X, MEMX 다섯 곳이고, Cboe는 시세 시스템이 열리는 첫날부터 모든 종목을 야간 세션에 올리겠다고 밝혔어요(<a href="https://www.cboe.com/document/tech-spec/content/technical-specifications/cboe-u.s.-equities-overnight-trading-faq" target="_blank" rel="noopener">Cboe 야간 거래 FAQ</a>). 다만 국내 증권사가 이 세션을 언제, 어떤 방식으로 연결할지는 아직 정해지지 않았어요. 증권사 공지가 나오면 이 글을 갱신할게요.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">시간대별로 주문이 다르게 체결되는 이유</h2>

<p>같은 종목이라도 몇 시에 주문하느냐에 따라 체결 가격이 꽤 달라질 수 있어요. 정규장 밖의 프리마켓, 애프터마켓, 주간거래는 참여자가 적어서 사려는 값과 팔려는 값의 간격이 넓고, 작은 주문에도 가격이 크게 움직여요.</p>

<p>미국 기업 실적은 대부분 정규장 시작 전이나 끝난 뒤에 나와요. 그래서 실적 발표 날에는 한국시간 아침의 애프터마켓이나 저녁의 프리마켓에서 가격이 먼저 크게 움직이는 일이 많아요. 주간거래는 2024년 사례처럼 대체거래소 사정으로 체결이 취소될 수 있다는 점도 함께 알아 두면 좋아요.</p>

<p>한국 증시에 상장된 미국 지수 ETF는 한국 장 시간(오전 9시~오후 3시 30분)에 거래돼요. 미국 장이 닫혀 있는 동안의 가격은 추정치라서 실제 가치와 벌어지는 괴리율이 생길 수 있고, 이 내용은 <a href="https://sensitiveboss3.tistory.com/entry/etf-divergence-rate-2026" target="_blank" rel="noopener">ETF 괴리율 글</a>에 정리했어요. 미국 주식을 팔 때의 세금은 <a href="https://sensitiveboss3.tistory.com/entry/us-stock-tax" target="_blank" rel="noopener">미국주식 세금 글</a>과 <a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing" target="_blank" rel="noopener">해외주식 양도소득세 신고 글</a>에서 이어서 볼 수 있어요.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #0e7490;padding-left:12px;margin-top:36px;">미국장 시간 Q&amp;A 5개</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">서머타임이 끝나면 미국 장은 한국시간 몇 시에 열리나요</summary>
  <p style="margin:10px 0 0 0;">11월 2일(월) 밤 11시 30분에 열려 다음 날 새벽 6시에 닫혀요. 이 시간은 2027년 3월 14일 서머타임이 다시 시작될 때까지 이어지고, 그 뒤에는 밤 10시 30분~새벽 5시로 돌아가요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증권사 앱의 프리마켓 시간이 표와 다른 이유는 뭔가요</summary>
  <p style="margin:10px 0 0 0;">표는 미국 거래소 기준이에요. 증권사마다 연결한 시장과 제공 시간이 달라서 프리마켓을 거래소보다 늦게 열거나 애프터마켓을 일찍 닫는 곳이 있어요. 내 증권사 앱의 해외주식 거래시간 안내가 실제로 주문할 수 있는 시간이에요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">추수감사절에는 한국시간으로 언제 쉬나요</summary>
  <p style="margin:10px 0 0 0;">미국 11월 26일(목)이 휴장이라 한국시간 11월 26일 밤에는 정규장이 열리지 않아요. 다음 날 27일은 미국시간 오후 1시에 일찍 끝나서 한국시간 11월 28일(토) 새벽 3시에 마감돼요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주간거래와 12월 6일부터 시작되는 밤샘 거래는 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">달라요. 주간거래는 국내 증권사가 미국 대체거래소(ATS)를 통해 한국 낮 시간에 열어 주는 서비스예요. 12월 6일부터는 나스닥 같은 정식 거래소가 미국 밤 시간에 직접 거래를 받는 것이라, 국내 증권사가 이 세션을 어떻게 연결할지는 따로 공지가 나와야 알 수 있어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주말에도 미국주식을 사고팔 수 있나요</summary>
  <p style="margin:10px 0 0 0;">정규 거래소는 주말에 쉬어요. 한국시간 토요일 아침 10시(서머타임 해제 기준)까지는 미국 금요일 애프터마켓이 이어지고, 12월 6일 이후에도 새 주가 시작되는 시점은 미국 일요일 밤 9시, 한국시간 월요일 오전 11시예요.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://s2.q4cdn.com/154085107/files/doc_news/NYSE-Group-Announces-2026-2027-and-2028-Holiday-and-Early-Closings-Calendar-2025.pdf" target="_blank" rel="noopener">NYSE Group 2026·2027·2028 휴장 및 조기 폐장 일정</a></li>
    <li><a href="https://www.fidelity.com/learning-center/smart-money/stock-market-holidays" target="_blank" rel="noopener">Fidelity Stock market holidays 2026</a></li>
    <li><a href="https://www.koreadaily.com/article/20261002153320566" target="_blank" rel="noopener">미주중앙일보 서머타임 11월 1일 종료 보도(2026-10-02)</a></li>
    <li><a href="https://www.kbsec.com/go.able?linkcd=s060901010000&amp;seq=10009104&amp;idt=20251022" target="_blank" rel="noopener">KB증권 미국주식 주간거래 재개 안내</a></li>
    <li><a href="https://news.nate.com/view/20250924n17646" target="_blank" rel="noopener">미국 주식 주간거래 재개 보도(2025-09-24)</a></li>
    <li><a href="https://www.wilmerhale.com/en/insights/client-alerts/20260929-23x5-trading-comes-to-us-exchanges-what-firms-should-know-before-launch" target="_blank" rel="noopener">WilmerHale 23x5 Trading Comes to US Exchanges(2026-09-29)</a></li>
    <li><a href="https://www.marketsmedia.com/nasdaq-aims-to-debut-23-5-trading-on-6-december-2026/" target="_blank" rel="noopener">Markets Media Nasdaq Aims to Debut 23/5 Trading on 6 December 2026</a></li>
    <li><a href="https://www.cboe.com/document/tech-spec/content/technical-specifications/cboe-u.s.-equities-overnight-trading-faq" target="_blank" rel="noopener">Cboe U.S. Equities Overnight Trading FAQ</a></li>
  </ul>
  기준일: 2026년 10월 3일. 증권사별 프리·애프터·주간거래 제공 시간은 각 증권사 안내가 기준입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
미국 주식시장 운영 시간을 한국시간으로 정리한 정보 글이며, 특정 종목의 매수·매도나 거래 시점을 권하지 않습니다. 거래소 일정과 증권사 서비스는 공지에 따라 바뀔 수 있습니다. 투자 판단과 결과의 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "미국주식 거래시간 한국시간, 11월 1일부터 바뀌는 시간",
  "description": "미국주식 프리마켓·정규장·애프터마켓·주간거래를 한국시간으로 정리하고, 11월 1일 서머타임 종료로 바뀌는 시간과 남은 휴장일, 12월 6일 시작되는 미국 거래소 밤샘 거래까지 정리했습니다.",
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/us-stock-trading-hours-korea-time-1.png",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/us-stock-trading-hours-korea-time"
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
      "name": "서머타임이 끝나면 미국 장은 한국시간 몇 시에 열리나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "11월 2일(월) 밤 11시 30분에 열려 다음 날 새벽 6시에 닫혀요. 이 시간은 2027년 3월 14일 서머타임이 다시 시작될 때까지 이어지고, 그 뒤에는 밤 10시 30분~새벽 5시로 돌아가요."
      }
    },
    {
      "@type": "Question",
      "name": "증권사 앱의 프리마켓 시간이 표와 다른 이유는 뭔가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "표는 미국 거래소 기준이에요. 증권사마다 연결한 시장과 제공 시간이 달라서 프리마켓을 거래소보다 늦게 열거나 애프터마켓을 일찍 닫는 곳이 있어요. 내 증권사 앱의 해외주식 거래시간 안내가 실제로 주문할 수 있는 시간이에요."
      }
    },
    {
      "@type": "Question",
      "name": "추수감사절에는 한국시간으로 언제 쉬나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "미국 11월 26일(목)이 휴장이라 한국시간 11월 26일 밤에는 정규장이 열리지 않아요. 다음 날 27일은 미국시간 오후 1시에 일찍 끝나서 한국시간 11월 28일(토) 새벽 3시에 마감돼요."
      }
    },
    {
      "@type": "Question",
      "name": "주간거래와 12월 6일부터 시작되는 밤샘 거래는 같은 건가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "달라요. 주간거래는 국내 증권사가 미국 대체거래소(ATS)를 통해 한국 낮 시간에 열어 주는 서비스예요. 12월 6일부터는 나스닥 같은 정식 거래소가 미국 밤 시간에 직접 거래를 받는 것이라, 국내 증권사가 이 세션을 어떻게 연결할지는 따로 공지가 나와야 알 수 있어요."
      }
    },
    {
      "@type": "Question",
      "name": "주말에도 미국주식을 사고팔 수 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정규 거래소는 주말에 쉬어요. 한국시간 토요일 아침 10시(서머타임 해제 기준)까지는 미국 금요일 애프터마켓이 이어지고, 12월 6일 이후에도 새 주가 시작되는 시점은 미국 일요일 밤 9시, 한국시간 월요일 오전 11시예요."
      }
    }
  ]
}
</script>
