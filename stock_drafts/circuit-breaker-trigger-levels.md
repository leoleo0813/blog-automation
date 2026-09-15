---
keyword: 서킷브레이커 뜻
title: 서킷브레이커 뜻과 발동조건 3단계
slug: circuit-breaker-trigger-levels
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1680 (PC 300 / 모바일 1380)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-15 — 통과]
  WebSearch "서킷브레이커 뜻 발동 조건 코스피" 상위 종합:
  tossbank.com(토스뱅크, 대형 핀테크) / easylaw.go.kr(법제처 찾기쉬운 생활법령정보,
  공식) / ko.wikipedia.org(위키백과) / dndn.io(든든 블로그, 개인) /
  blog.blanclucy.co.kr·blanclucy.co.kr(개인 블로그, 동일 저자 2편 노출) /
  namu.wiki(나무위키) / brunch.co.kr(브런치, 개인) / mofe.go.kr(기획재정부
  시사경제용어사전, 공식) / dic.hankyung.com(한국경제, 언론) / newsis.com(뉴시스,
  언론) / kbthink.com(KB국민은행)
  1) 진입 여지 — 있음. dndn.io·blanclucy.co.kr(2편)·brunch.co.kr 등 개인/소규모
     콘텐츠가 상위권에 다수 노출. SERP 안 잠김.
  2) 검색 의도 — 정의+메커니즘 이해("왜, 언제 멈추나"). 홈택스형 조회·계산기 실행
     의도가 아니라 글로 답할 수 있는 정보 탐색.
  3) 답 완결 여부 — 아니다. 상위 글 대부분이 정의·3단계 조건·사이드카와의 차이까지는
     다루지만, 개별종목 단위인 VI(변동성완화장치)까지 포함한 3자 비교표를 갖춘 글은
     드물고, 2026년 코스피가 도입 이후 처음으로 이틀 연속 발동된 이례적 사례를 반영한
     글은 찾지 못했다. 정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-15]
  (a) 서킷브레이커 1·2·3단계 발동 조건과 조치를 표로 정리 — 각 단계의 하락률 기준,
      1분 지속 조건, 20분 정지·10분 단일가 재개(1·2단계) vs 즉시 장 종료(3단계)
      구분을 명확히 함.
  (b) VI(변동성완화장치)·사이드카·서킷브레이커 3자 비교표 — "개별 종목 vs 선물시장
      vs 시장 전체"라는 적용 대상 차이를 축으로 정리. 상위 검색 결과 대부분은
      서킷브레이커·사이드카 2자 비교에 그치고 VI까지 포함한 3자 비교는 드물다.
      사이드카의 코스피·코스닥별 세부 조건과 계산 예시는 25편(사이드카 뜻과 발동
      조건)으로 넘겨 중복을 피하고 링크만 건다.
  (c) 2026년 코스피가 제도 도입 이후 처음으로 7월 28~29일 이틀 연속 서킷브레이커가
      발동된 사례와, 7월 한 달 동안 서킷브레이커·사이드카가 하루도 발동되지 않은
      거래일이 사흘뿐이었다는 언론 보도를 날짜와 함께 인용 — 상위 검색 결과에 없는
      최신 시의성 확보.
  (d) 25편(사이드카 뜻)과 역할 분담 — 사이드카 세부 조건·계산 예시는 25편이 전담하고,
      이 글은 서킷브레이커 자체의 3단계 조건과 VI·사이드카와의 비교 축을 전담해
      카니벌라이제이션을 피한다.
primary_source: |
  1차 시도: 한국거래소 규정 페이지(regulation.krx.co.kr, 유가증권시장 매매거래중단제도)
  WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-15).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12)
  기준 적용 — 아래처럼 서로 무관한 출처가 3곳을 크게 넘고, 그중 다수가 정부기관·언론
  등급이며, 핵심 수치가 충돌 없이 일치해 교차검증으로 진행했다.
  ① 서킷브레이커 3단계 조건(8%/15%/20%, 1분 지속, 20분 정지+10분 단일가, 3단계
     즉시 종료, 1일1회, 개장5분후~장마감40분전): 기획재정부 시사경제용어사전
     (mofe.go.kr), 법제처 이지로우(easylaw.go.kr), 한국경제 경제용어사전
     (dic.hankyung.com), 토스뱅크 공식 아티클(tossbank.com) 4곳이 동일 수치로 일치.
  ② VI(변동성완화장치) 조건(동적 2~3%, 정적 10%, 2분 단일가+30초 냉각)과
     서킷브레이커·사이드카 3자 구분: 뉴시스(newsis.com, 언론)·kbthink.com(KB국민은행)
     2곳이 동일 서술로 일치, 25편 작성 시 확인한 다수 출처(헤럴드경제·서울경제 등)와도
     충돌 없음.
  ③ 2026년 이틀 연속 발동 사례(2026-07-28~29)는 MBC뉴스(imnews.imbc.com)와
     또 다른 언론 보도(daum 뉴스 링크)에서 "사상 처음 이틀 연속"이라는 동일 표현으로
     교차 확인. 7월 발동 빈도(하루도 안 걸린 날 사흘)는 파이낸셜뉴스(fnnews.com)
     보도. 연간 누적 발동 횟수는 보도 시점마다 계속 바뀌는 값이라 본문에 특정 숫자로
     단정하지 않고 "최신 수치는 거래소 공지·언론 보도로 확인" 안내로 갈음했다.
  KRX 규정 원문 전문을 직접 열람하지 못한 한계는 self_check에 투명 공개한다.
기준일: 2026-09-15 (WebSearch 확인일)
tags: 서킷브레이커, 서킷브레이커뜻, 서킷브레이커발동조건, 사이드카, 변동성완화장치, VI뜻, 코스피, 매매거래중단, 주식초보, 서킷브레이커차이
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-15).
  게이트1: check-keywords.yml 실측 1,680회(일반 기준 500 이상, 이 배치 중 유일한
  PASS — 나머지 7개 후보는 전부 20회로 FAIL, backlog.failed_gate1에 기록).
  게이트2: v3 기준 통과(serp_check 참조 — 개인/소규모 콘텐츠 다수 진입, VI까지
  포함한 3자 비교와 2026년 이례적 사례가 정보이득 여지).
  게이트3: 3단계 조건표 + VI·사이드카·서킷브레이커 3자 비교표 + 2026년 이틀 연속
  발동(사상 최초) 사례로 상위 검색 결과에 없는 정보이득 확보.
  게이트4: regulation.krx.co.kr 1회 WebFetch 시도 EGRESS_BLOCKED 확인 후, 정부기관
  2곳(기획재정부·법제처)·언론 3곳(한국경제·뉴시스·파이낸셜뉴스)·금융사 2곳(토스뱅크·KB)
  포함 다수 독립 출처 교차검증으로 진행. 한계는 self_check에 투명 공개.
self_check: |
  [2026-09-15 최종 판정]
  게이트1 충족 — check-keywords.yml 실측 1,680회(2026-09-15). 같은 배치의
  "넥스트레이드 수수료"(20)·"주식 대체출고 방법"(20)·"주식 대여 서비스
  이자소득"(20)·"명의신탁 주식 증여의제"(20)·"코스피 이전상장 요건"(20)·
  "대주주 양도소득세 판정기준일"(20)·"배당소득 원천징수영수증 발급방법"(20)은
  전부 FAIL로 backlog.failed_gate1에 기록.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 3단계 조건표 + VI·사이드카 3자 비교 + 2026년 이틀 연속 발동
  사례로 정보이득 확보. 사이드카 세부는 25편으로 넘겨 중복 없음.
  게이트4 — regulation.krx.co.kr 1회 WebFetch 시도 EGRESS_BLOCKED 확인(2026-09-15).
  RULES.md 2026-09-12 기준에 따라 정부기관 2곳(기획재정부·법제처)·언론 3곳(한국경제·
  뉴시스·파이낸셜뉴스)·금융사 2곳(토스뱅크·KB) 등 서로 무관한 다수 출처가 핵심
  수치(8%/15%/20%, 1분지속, 20분/10분/즉시종료, VI 2~3%/10%)에서 충돌 없이 일치해
  교차검증으로 진행했다. KRX 규정 원문 전문은 직접 열람하지 못한 한계가 있어, 본문에
  "정확한 최신 수치는 거래소 공지로 확인하라"는 안내를 덧붙였다. 2026년 누적 발동
  횟수는 보도 시점마다 계속 바뀌는 값이라 특정 숫자로 단정하지 않고 날짜가 명확한
  개별 사례(2026-07-28~29 이틀 연속 발동)와 "보도 시점 기준 사흘뿐" 식 출처·날짜
  명시 표현만 사용했다.
  카니벌라이제이션 점검 — 1~33편 어디에도 서킷브레이커·VI(변동성완화장치)를 정면으로
  다룬 편이 없다. 25편(사이드카 뜻)은 사이드카 자체의 세부 조건·계산 예시를 전담하므로,
  이 글은 서킷브레이커 3단계 조건과 VI·사이드카 비교 축만 담당해 역할이 겹치지 않는다.
  링크로 25편을 안내해 상호 보완 관계를 명시했다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 한국거래소를 안내하는 자리와
  하단 참고 출처 3곳 전부 target="_blank" rel="noopener"로 링크 처리. mofe.go.kr·
  easylaw.go.kr URL은 WebSearch 결과에서 직접 확인한 실제 URL만 사용, 지어낸 링크
  없음.
  제목 14자·금지어 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와 JSON-LD 1:1
  일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음(누적 발동
  횟수는 "최신 수치는 확인하라"로 단정 회피). 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) →
  gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-15</p>

<p><mark>서킷브레이커는 주가지수가 8% 이상 급락하면 모든 종목의 거래를 20분간 강제로 멈추는 시장 안전장치입니다.</mark> 코스피는 2026년 들어 유독 자주 발동돼 사상 처음 이틀 연속 걸리기도 했습니다. 이 글은 정확한 발동 조건 3단계와, 헷갈리기 쉬운 사이드카·VI와의 차이를 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>서킷브레이커는 지수가 전일 대비 <b>8%·15%·20% 이상</b> 하락하면 단계별로 발동되는 <b>시장 전체</b> 거래정지 제도입니다.</li>
    <li><mark>1·2단계는 20분간 매매가 멈추고, 3단계가 뜨면 그날 장이 즉시 끝납니다.</mark></li>
    <li>개별 종목이 급변할 때 걸리는 <b>VI</b>, 선물시장 충격을 막는 <b>사이드카</b>와는 적용 대상과 조건이 다릅니다.</li>
    <li>2026년 코스피는 서킷브레이커가 이례적으로 자주 발동돼 <b>사상 처음 이틀 연속</b> 걸리는 기록도 남겼습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>서킷브레이커란 무엇인가요</li>
  <li>코스피 서킷브레이커는 언제 발동되나요</li>
  <li>서킷브레이커와 사이드카·VI는 어떻게 다른가요</li>
  <li>서킷브레이커가 발동되면 어떻게 되나요</li>
  <li>2026년 서킷브레이커는 왜 이렇게 자주 발동됐나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">서킷브레이커란 무엇인가요</h2>

<p>서킷브레이커(매매거래중단제도)는 <mark>주가지수가 급락할 때 시장 전체의 매매를 일시적으로 멈추는 제도</mark>입니다. 전기 회로에 과부하가 걸리면 차단기가 내려가듯, 투자자들에게 냉정하게 생각할 시간을 강제로 주기 위한 장치입니다.</p>

<p>한국거래소는 1998년부터 이 제도를 운영하고 있으며, 하락 폭에 따라 <b>1단계·2단계·3단계</b> 순서로 발동됩니다. 코스피와 코스닥 시장에 각각 독립적으로 적용됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">코스피 서킷브레이커는 언제 발동되나요</h2>

<p>발동 기준은 <b>전일 종가 대비 지수 하락률이 일정 수준을 1분 이상 유지</b>하는지로 판단합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">단계</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">발동 조건</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">조치</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">1단계</td>
      <td style="border:1px solid #ddd;padding:8px;">전일 종가 대비 8% 이상 하락 상태 1분 지속</td>
      <td style="border:1px solid #ddd;padding:8px;">전 종목 매매 20분 정지 → 10분간 단일가매매로 재개</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2단계</td>
      <td style="border:1px solid #ddd;padding:8px;">전일 종가 대비 15% 이상 하락(1단계 대비 1%p 추가 하락) 상태 1분 지속</td>
      <td style="border:1px solid #ddd;padding:8px;">전 종목 매매 20분 정지 → 10분간 단일가매매로 재개</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">3단계</td>
      <td style="border:1px solid #ddd;padding:8px;">전일 종가 대비 20% 이상 하락(2단계 대비 1%p 추가 하락) 상태 1분 지속</td>
      <td style="border:1px solid #ddd;padding:8px;">그날 장 즉시 종료</td>
    </tr>
  </tbody>
</table>

<p><mark>1·2단계는 하루에 한 번만 발동</mark>할 수 있고, 장이 열린 뒤 5분이 지난 시점부터 장 마감 40분 전까지만 발동됩니다. 발동 중에는 새 주문을 넣을 수 없고, 이미 낸 주문을 취소하는 것만 가능합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">서킷브레이커와 사이드카·VI는 어떻게 다른가요</h2>

<p>세 가지 모두 주가 급변 시 매매를 일시적으로 조정하는 안전장치지만, <b>적용 대상과 강도</b>가 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">적용 대상</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">발동 조건</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">조치</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">VI(변동성완화장치)</td>
      <td style="border:1px solid #ddd;padding:8px;">개별 종목</td>
      <td style="border:1px solid #ddd;padding:8px;">동적: 직전 체결가 대비 2~3%↑↓ / 정적: 전일 종가 대비 10%↑↓</td>
      <td style="border:1px solid #ddd;padding:8px;">2분간 단일가매매 전환 후 30초 냉각</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">사이드카</td>
      <td style="border:1px solid #ddd;padding:8px;">코스피200·코스닥150 선물시장</td>
      <td style="border:1px solid #ddd;padding:8px;">선물가격 기준가 대비 코스피 5%, 코스닥 6%(+지수 3%) 이상 등락 1분 지속</td>
      <td style="border:1px solid #ddd;padding:8px;">프로그램매매 호가 효력 5분간 정지</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">서킷브레이커</td>
      <td style="border:1px solid #ddd;padding:8px;">시장 전체(전 종목)</td>
      <td style="border:1px solid #ddd;padding:8px;">지수가 전일 대비 8%·15%·20% 이상 하락 1분 지속</td>
      <td style="border:1px solid #ddd;padding:8px;">20분 정지(1·2단계) 또는 즉시 장 종료(3단계)</td>
    </tr>
  </tbody>
</table>

<p>즉 <mark>VI는 종목 하나, 사이드카는 선물시장 충격의 파급, 서킷브레이커는 시장 전체를 대상으로 한다</mark>는 점이 가장 큰 차이입니다. 사이드카의 코스피·코스닥별 세부 조건과 실제 숫자 계산 예시는 <a href="https://sensitiveboss3.tistory.com/entry/stock-sidecar-trigger-condition" target="_blank" rel="noopener">사이드카 뜻과 발동 조건</a> 글에서 더 자세히 다뤘습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">서킷브레이커가 발동되면 어떻게 되나요</h2>

<p>1·2단계가 발동되면 코스피·코스닥은 물론 관련 선물·옵션 시장까지 <b>20분간 모든 매매가 멈춥니다</b>(채권시장 제외). 이 시간 동안 이미 낸 주문을 취소하는 것은 가능하지만, 새로운 매수·매도 주문은 접수되지 않습니다.</p>

<p>20분이 지나면 곧바로 정상 매매로 돌아가는 게 아니라, <b>10분간 단일가매매</b>로 가격을 조정한 뒤 재개됩니다. 3단계가 발동되면 이런 절차 없이 그날 거래소 매매 자체가 그대로 끝납니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>주의할 점</b>
  <p style="margin:8px 0 0 0;">서킷브레이커가 풀렸다고 해서 하락이 끝났다는 뜻은 아닙니다. 20분의 냉각 시간을 준 것일 뿐, 재개 이후 지수가 다시 급락하면 다음 단계가 이어서 발동될 수 있습니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2026년 서킷브레이커는 왜 이렇게 자주 발동됐나요</h2>

<p>2026년 코스피는 <mark>제도 도입 이후 서킷브레이커가 가장 잦았던 해</mark>로 꼽힙니다. 3월에는 미국-이란 전쟁 여파로 코스피·코스닥이 동반 8%대로 급락하며 발동됐고, 7월에는 반도체주 투매 등으로 발동이 잇따랐습니다.</p>

<p>특히 <b>2026년 7월 28일과 29일, 코스피는 제도 도입 이후 처음으로 이틀 연속 서킷브레이커가 발동</b>되는 기록을 남겼습니다. 여러 언론은 7월 한 달 동안 서킷브레이커나 사이드카가 하루도 발동되지 않은 거래일이 사흘뿐이었다고 전했습니다.</p>

<p>정확한 연간 누적 발동 횟수는 시점마다 계속 바뀌므로, 최신 수치는 <a href="https://www.krx.co.kr" target="_blank" rel="noopener">한국거래소</a> 공지나 언론 보도로 확인하는 게 정확합니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 다시 한 번 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>서킷브레이커는 지수가 8%·15%·20% 이상 하락하면 단계별로 시장 전체 매매를 멈추는 제도입니다.</li>
    <li>VI는 개별 종목, 사이드카는 선물시장, 서킷브레이커는 시장 전체를 대상으로 한다는 점이 다릅니다.</li>
    <li>2026년 코스피는 이례적으로 자주 발동돼 사상 처음 이틀 연속 걸리는 기록도 남겼습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">서킷브레이커가 발동되면 주식을 살 수 없나요</summary>
  <p style="margin:10px 0 0 0;">새로운 매수·매도 주문은 낼 수 없지만, 이미 낸 주문을 취소하는 것은 가능합니다. 20분 정지 후에는 10분간 단일가매매를 거쳐 재개됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">서킷브레이커는 하루에 여러 번 발동될 수 있나요</summary>
  <p style="margin:10px 0 0 0;">1단계와 2단계는 각각 하루에 한 번만 발동됩니다. 다만 하락 폭이 커지면 1단계에 이어 2단계, 3단계까지 순서대로 넘어갈 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">서킷브레이커와 사이드카는 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 서킷브레이커는 지수 급락 시 시장 전체 매매를 멈추는 제도이고, 사이드카는 선물시장 급변이 현물시장으로 번지는 것을 막기 위해 프로그램매매 호가만 일시 정지하는 제도입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">VI(변동성완화장치)와는 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">VI는 개별 종목의 가격이 갑자기 크게 움직일 때 그 종목만 2분간 단일가매매로 전환하는 장치입니다. 서킷브레이커처럼 시장 전체를 멈추지는 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">3단계 서킷브레이커가 발동되면 다음 날 거래는 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">3단계는 그날 하루의 매매만 즉시 종료시킬 뿐, 다음 거래일은 평소대로 정상 개장합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코스닥에도 서킷브레이커가 있나요</summary>
  <p style="margin:10px 0 0 0;">있습니다. 코스닥 지수도 코스피와 동일한 8%·15%·20% 기준으로, 코스피와 별도로 서킷브레이커가 발동됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://regulation.krx.co.kr/contents/RGL/03/03010402/RGL03010402.jsp" target="_blank" rel="noopener">한국거래소 - 주식시장의 매매거래중단제도(Circuit Breakers) 규정</a></li>
    <li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=1427" target="_blank" rel="noopener">기획재정부 - 시사경제용어사전 「서킷브레이커」</a></li>
    <li><a href="https://www.easylaw.go.kr/CSP/CnpClsMainBtr.laf?popMenu=ov&amp;csmSeq=1701&amp;ccfNo=3&amp;cciNo=1&amp;cnpClsNo=1" target="_blank" rel="noopener">법제처 찾기쉬운 생활법령정보 - 매매거래중단·정지 및 시장경보제도</a></li>
    <li>기준일: 2026-09-15 (WebSearch 확인일)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를
권유하지 않습니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "서킷브레이커 뜻과 발동조건 3단계",
  "description": "서킷브레이커의 뜻과 1·2·3단계 발동 조건, 사이드카·VI(변동성완화장치)와의 차이, 2026년 코스피가 사상 처음 이틀 연속 발동된 사례까지 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-15",
  "dateModified": "2026-09-15",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/circuit-breaker-trigger-levels"
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
      "name": "서킷브레이커가 발동되면 주식을 살 수 없나요",
      "acceptedAnswer": { "@type": "Answer", "text": "새로운 매수·매도 주문은 낼 수 없지만, 이미 낸 주문을 취소하는 것은 가능합니다. 20분 정지 후에는 10분간 단일가매매를 거쳐 재개됩니다." }
    },
    {
      "@type": "Question",
      "name": "서킷브레이커는 하루에 여러 번 발동될 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "1단계와 2단계는 각각 하루에 한 번만 발동됩니다. 다만 하락 폭이 커지면 1단계에 이어 2단계, 3단계까지 순서대로 넘어갈 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "서킷브레이커와 사이드카는 같은 건가요",
      "acceptedAnswer": { "@type": "Answer", "text": "다릅니다. 서킷브레이커는 지수 급락 시 시장 전체 매매를 멈추는 제도이고, 사이드카는 선물시장 급변이 현물시장으로 번지는 것을 막기 위해 프로그램매매 호가만 일시 정지하는 제도입니다." }
    },
    {
      "@type": "Question",
      "name": "VI(변동성완화장치)와는 뭐가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "VI는 개별 종목의 가격이 갑자기 크게 움직일 때 그 종목만 2분간 단일가매매로 전환하는 장치입니다. 서킷브레이커처럼 시장 전체를 멈추지는 않습니다." }
    },
    {
      "@type": "Question",
      "name": "3단계 서킷브레이커가 발동되면 다음 날 거래는 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "3단계는 그날 하루의 매매만 즉시 종료시킬 뿐, 다음 거래일은 평소대로 정상 개장합니다." }
    },
    {
      "@type": "Question",
      "name": "코스닥에도 서킷브레이커가 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "있습니다. 코스닥 지수도 코스피와 동일한 8%·15%·20% 기준으로, 코스피와 별도로 서킷브레이커가 발동됩니다." }
    }
  ]
}
</script>
