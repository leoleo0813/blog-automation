---
keyword: ISA 계좌 수수료
title: ISA 계좌 수수료 유형별 확인법
slug: isa-account-fee-check
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 160 (PC 50 / 모바일 110, 2026-09-23 실측, check-keywords.yml)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요 — "ISA" 포함 키워드)
serp_check: |
  [게이트2 v3 판정 2026-09-23 — 통과]
  WebSearch "ISA 계좌 수수료 신탁형 일임형 중개형 비교 2026" 상위 9개:
  brunch.co.kr(개인 콘텐츠 플랫폼) / securities.miraeasset.com(미래에셋증권, 공식) /
  obank.kbstar.com(KB국민은행, 공식) / welfarehello.com(개인·소규모 정책정보
  콘텐츠 사이트) / blog.onestopsamsungpop.co.kr(제3자 콘텐츠 블로그, 도메인이
  실제 삼성증권 공식 사이트가 아님 — 개인·소규모로 분류) / leehaninvest.com(개인
  재무상담 블로그) / exervital.com(개인·소규모 콘텐츠, 증권사 7곳 실측 비교표
  보유) / bileotools.com(개인·소규모 콘텐츠) / 위키백과(주제 무관, 검색 노이즈로
  제외)
  1) 진입 여지 — 있음. brunch·welfarehello·onestopsamsungpop 블로그·leehaninvest·
     exervital·bileotools까지 개인·소규모 콘텐츠가 9개 중 6개로 과반을 차지한다.
     이 시리즈에서 진입 여지가 넓은 축에 속한다.
  2) 검색 의도 — "ISA 유형별로 수수료가 어떻게 다른지" 정보 탐색형이다. 조회·신청·
     계산기 실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 아니다. 단, exervital.com이 이미 "증권사 7곳 수수료 비교"라는
     정적 표를 갖추고 있어 단순 표 나열만으로는 차별화가 약하다. 상위 글 대부분이
     신탁형·일임형·중개형의 수수료 "구조" 차이(무엇에 얼마가 붙는지)와 "본인 계좌의
     정확한 요율을 직접 확인하는 절차"를 함께 다루지는 않아, 그 지점에서 정보이득을
     확보한다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과(단, 정보이득 확보 난이도는 보통 이상).
unique_asset: |
  [부분 완성 — 금융사별 실측 비교표는 캡처 대기]
  (a) 확정 반영: ISA 3가지 유형(중개형·신탁형·일임형)이 수수료가 붙는 방식 자체가
      다르다는 구조를 정리했다. 중개형은 계좌 유지수수료가 없고 매매할 때만 위탁
      수수료가 붙는 반면, 신탁형은 신탁보수가, 일임형은 운용관리수수료가 보유
      기간 내내 자산에서 자동으로 빠져나간다. 이 구조 차이를 명확히 짚는 글은
      상위 결과 중 드물다.
  (b) 확정 반영: 신탁형 신탁보수(연 0.1~0.7%대)·일임형 운용관리수수료(연 0.1~0.6%대)의
      대략적 범위를 서로 다른 다수 출처로 교차확인했다. 다만 정확한 요율은
      금융사·상품마다 다르므로 범위로만 제시한다.
  (c) 캡처 대기: 실제 금융사별(증권사·은행 3~5곳) 신탁보수율·운용관리수수료율을
      한 표에 모은 실측 비교표. exervital.com은 중개형 매매수수료 중심으로 7곳을
      비교했지만, 신탁형·일임형까지 포함한 비교표는 확인하지 못했다 — 이 부분이
      캡처로 채워지면 뚜렷한 정보이득이 된다.
  (d) 확정 반영: 본인 계좌의 정확한 수수료를 스스로 확인하는 절차(금융투자협회
      ISA다모아 이용법)를 단계별로 안내했다. 상위 경쟁 글 대부분은 확인 도구
      자체를 소개하지 않는다.
primary_source: |
  1차 시도: 금융투자협회 ISA 비교공시 시스템 「ISA다모아」(isa.kofia.or.kr). 기존
  RULES.md 기록상 같은 금융투자협회 계열의 dis.kofia.or.kr이 WebSquare 기반 JS
  앱이라 자동화 렌더링으로는 수치가 보이지 않는다고 확인된 바 있어, isa.kofia.or.kr도
  같은 계열일 가능성이 높다고 판단해 대신 전국은행연합회 ISA 비교 페이지
  (portal.kfb.or.kr/compare/isa.php)에 WebFetch를 1회 시도했다 → EGRESS_BLOCKED
  (2026-09-23). 대조군으로 www.google.com도 같은 세션에서 WebFetch 1회 시도했으나
  동일하게 EGRESS_BLOCKED가 떨어져, 특정 도메인 문제가 아니라 이 세션의 전면 차단임을
  확인했다.
  RULES.md 「1차 출처가 막혔을 때」 기준에 따라 2차 출처 교차검증을 시도했다. 신탁형
  신탁보수·일임형 운용관리수수료의 "대략적 범위"(연 0.1~0.7%대, 연 0.1~0.6%대)는
  kbthink.com(KB국민은행 공식 콘텐츠) 복수 페이지와 asiatop.co.kr(개인·소규모 콘텐츠)
  등에서 겹치는 범위로 확인됐다. 그러나 정확한 소수점 단위 요율은 자료마다 다르게
  나왔다(예: 신탁형 "연 0.20%" vs "연 0.1~0.7%", 일임형 "연 0.10~0.50%" vs
  "연 0.2~0.6%"). 이는 세율처럼 단일 정답이 있는 숫자가 아니라 금융사·상품별로
  실제 요율이 다르기 때문에 생기는 자연스러운 편차이며, 그래서 본문에는 대략적
  범위만 쓰고 "정확한 요율은 금융사·상품마다 다르다"는 점을 명시했다. 금융사별
  구체적인 실측값(비교표의 핵심)은 원문(ISA다모아) 접근 없이는 확정할 수 없어
  capture_guide로 전환한다.
기준일: 2026-09-23 (WebSearch 교차검증일 — 금융사별 실측값은 사람 캡처 대기)
tags: ISA계좌, ISA수수료, 신탁형ISA, 일임형ISA, 중개형ISA, 신탁보수, 운용관리수수료, 주식초보, 절세계좌
gate_pass: false
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 160회(PC 50/모바일 110, 세부·제도 기준
  100 이상). 같은 배치에서 함께 확인한 연금계좌 인출순서(20)·상장리츠 공모청약
  방법(20)·외국인 순매수 확인방법(20)·연금저축 이월신청(20)·배당소득세 원천징수
  시기(20)는 전부 FAIL로 backlog.failed_gate1에 기록했다.
  게이트2 충족 — v3 기준 통과(serp_check 참조). 개인·소규모 콘텐츠가 상위 과반을
  차지해 진입 여지는 있으나, exervital.com이 이미 유사한 비교표를 갖추고 있어
  정보이득 확보 난이도는 보통 이상이다.
  게이트3 부분 충족 — 수수료 유형별 구조 차이, 대략적 요율 범위, 직접 확인 절차는
  확정해 반영했다. 다만 이 글의 핵심이 되어야 할 "금융사별 실제 요율 비교표"는
  아직 만들 수 없다.
  게이트4 미충족 — 1차 출처(ISA다모아)는 JS 앱으로 추정돼 시도하지 않았고, 대안
  출처(은행연합회)는 WebFetch가 EGRESS_BLOCKED로 막혔다(대조군 google.com도 차단
  확인, 세션 전면 차단). 2차 출처 교차검증은 "대략적 범위"까지만 수렴했고 금융사별
  정확한 소수점 요율은 자료마다 달라 확정하지 못했다. RULES.md의 human-assisted
  분류(증권사 수수료·환전 우대율·ETF 총보수와 같은 유형)에 정확히 해당해 캡처로
  전환한다.
capture_guide: |
  (1) 왜 필요한가 — ISA 계좌 수수료는 신탁형(신탁보수)·일임형(운용관리수수료)이
  금융사·상품마다 실제 요율이 다릅니다. WebSearch로는 "신탁형 연 0.1~0.7%대",
  "일임형 연 0.1~0.6%대" 같은 대략적 범위만 확인되고, 특정 금융사 몇 곳의 정확한
  요율을 나란히 비교한 표는 원문 없이는 만들 수 없습니다. 이 표가 이 글의 핵심
  정보이득이라 캡처 없이는 발행할 수 없습니다.
  (2) 확인할 곳(우선순위):
  1순위. 금융투자협회 ISA다모아 https://isa.kofia.or.kr 접속 → "신탁형 상품비교"
  메뉴에서 주요 은행·증권사 3~5곳을 선택해 신탁보수율이 표로 뜨는 화면을 캡처,
  이어서 "일임형 상품비교" 메뉴에서 같은 방식으로 운용관리수수료율 화면을 캡처
  2순위. 전국은행연합회 ISA 비교공시 https://portal.kfb.or.kr/compare/isa.php
  접속 → 은행별 ISA 수수료(신탁보수율)가 보이는 화면 캡처
  3순위. 평소 이용하는 증권사 ISA 상품안내 페이지(예: 미래에셋증권
  https://securities.miraeasset.com/hks/hks4659/n02.do , 그 외 이용 중인 증권사)에서
  중개형 매매수수료 또는 신탁형·일임형 수수료 안내 문구·표를 캡처
  (3) 캡처가 끝나면 — 스크린샷을 대화에 올려주시고, 어느 금융사·어느 유형(신탁형/
  일임형/중개형)의 수수료인지, 조회 기준일자도 함께 알려주시면 본문 비교표에
  반영해 gate_pass를 재판정하겠습니다.
self_check: |
  [2026-09-23 판정 — gate_pass:false로 저장]
  게이트1 충족 — 네이버 키워드도구 실측 160회(세부·제도 기준 100 이상).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check
  참조). 다만 exervital.com이라는 직접 경쟁 콘텐츠가 있어 정보이득 확보가 더
  까다롭다는 점을 게이트3 판단에 반영했다.
  게이트3 부분 충족 — 유형별 수수료 구조 차이, 대략적 요율 범위, 직접 확인 절차
  세 가지는 확정 반영했다. 금융사별 실측 비교표(핵심 정보이득)는 캡처 대기.
  게이트4 미충족 — ISA다모아는 dis.kofia.or.kr과 같은 계열의 JS 앱으로 추정해
  시도하지 않았고, 대안인 은행연합회 페이지는 WebFetch 1회 시도 후 EGRESS_BLOCKED
  확인(대조군 google.com도 차단되어 세션 전면 차단 판단). 2차 교차검증은 범위까지만
  수렴하고 금융사별 정확한 요율은 확정하지 못해 human-assisted 캡처로 전환.
  카니벌라이제이션 점검 — 1편(증권사 수수료 비교)은 매매 위탁수수료(거래마다 발생)를
  다루고, 이 글은 ISA 계좌 자체의 보유 기간 수수료(신탁보수·운용관리수수료)를
  다뤄 대상이 다르다. 본문에서 1편으로 내부 링크해 구분을 명시했다. 3편(ISA 계좌
  한도와 비과세 혜택)·67편(ISA 중도해지)·71편(ISA 계좌 이전 방법)·75편(IRP ISA
  차이)은 전부 grep 확인 결과 수수료·보수 관련 서술이 없어(0건) 겹침 없음.
  기관 링크 점검 — 본문에서 금융투자협회·미래에셋증권으로 안내하는 문장과 하단
  참고 출처 전부 target="_blank" rel="noopener"로 링크 처리. 정부·준정부 성격의
  금융투자협회 링크는 nofollow 미부착.
  제목 "ISA 계좌 수수료 유형별 확인법" 16자·금지어 없음·조사/접속사 없음. 슬러그
  영문 소문자+하이픈 4단어(isa-account-fee-check). 인트로 문단 최상단 배치,
  "안녕하세요" 없음. 표 2개 모두 thead/tbody 시맨틱. 비교표 값이 아직 없는 구간은
  "확인 중"으로 표기하고 수치를 지어내지 않았다.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 발행 본문(YAML 제외)에서 "—"
  0개 확인(YAML 메타데이터의 "—"는 자동화 기록용 구분자라 본문 대상에서 제외).
  "다만"은 본문에서 0회(전부 "단,"·"그런데"·"반면"으로 분산). 본문 `<mark>` 총
  3개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을 "🧾 미리
  정리하면"으로, 색상은 테라코타
  계열(#fff4ec/#c2540e)로 최근 게시물(핑크·바이올렛·인디고·앰버·틸·그린·퍼플)과
  겹치지 않게 골랐다. 목차 제외 본문 H2 6개 중 서술형 4개("신탁형·일임형 수수료
  구조", "금융사별 ISA 수수료 비교표", "내 계좌 수수료 직접 확인하는 방법",
  "수수료를 낮추는 방법"), 질문형 2개("ISA 계좌도 수수료를 따로 내야 하나요",
  "중개형 ISA는 수수료가 다른가요")로 "~나요" 편중 없음(전체 6개 중 2개, 33%).
  헤지 표현 남발 없음 — 정확한 요율이 금융사마다 다르다는 점은 정직하게 명시하고
  반복하지 않음. 면책 문구는 기존 게시물과 다른 표현으로 작성.
  종합 판정: 게이트1·2 충족, 게이트3 부분 충족, 게이트4 미충족(핵심 비교표 캡처
  대기) → gate_pass:false. 사람 캡처 대기 상태로 저장.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-23</p>

<p>ISA 계좌는 <mark>유형(중개형·신탁형·일임형)에 따라 수수료가 붙는 방식 자체가 다릅니다.</mark> 어떤 유형은 계좌 유지 비용이 아예 없고, 어떤 유형은 보유하는 동안 자산에서 매년 일정 비율이 자동으로 빠져나갑니다.</p>

<div style="background:#fff4ec;border:2px solid #c2540e;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#9a3f0a;font-size:18px;">🧾 미리 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>중개형</b>은 계좌 유지수수료가 없고, 매매할 때 위탁수수료만 붙습니다.</li>
    <li><b>신탁형</b>은 보유 기간 내내 <b>신탁보수</b>가, <b>일임형</b>은 <b>운용관리수수료</b>가 자산에서 자동으로 빠져나갑니다.</li>
    <li>정확한 요율은 금융사·상품마다 달라 <b>직접 조회</b>해야 정확히 알 수 있습니다.</li>
    <li>이 글의 금융사별 실측 비교표는 원문 조회 화면 캡처가 확보되는 대로 채워집니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ISA 계좌도 수수료를 따로 내야 하나요</li>
  <li>신탁형·일임형 수수료 구조</li>
  <li>중개형 ISA는 수수료가 다른가요</li>
  <li>금융사별 ISA 수수료 비교표</li>
  <li>내 계좌 수수료 직접 확인하는 방법</li>
  <li>수수료를 낮추는 방법</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">ISA 계좌도 수수료를 따로 내야 하나요</h2>

<p>네, 유형에 따라 다릅니다. ISA는 가입할 때 중개형·신탁형·일임형 중 하나를 고르는데, 이 선택이 수수료 구조 자체를 바꿉니다.</p>

<p>중개형은 국내 상장주식을 직접 사고팔 수 있는 유일한 유형으로, 계좌를 유지하는 데 드는 별도 비용이 없습니다. 반면 신탁형과 일임형은 은행이나 증권사가 자산을 대신 굴려주는 구조라, 보유하는 동안 정해진 비율의 보수가 계속 빠져나갑니다.</p>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">신탁형·일임형 수수료 구조</h2>

<p>신탁형은 예금·펀드 위주로 운용되며 <b>신탁보수</b>가 붙습니다. 일임형은 전문가가 포트폴리오를 대신 운용해주는 대가로 <b>운용관리수수료</b>가 붙습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>용어 정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>신탁보수</b>: 신탁형 ISA에서 편입 자산을 관리하는 대가로 연 단위로 부과되는 보수.</li>
    <li><b>운용관리수수료</b>: 일임형 ISA에서 전문가가 포트폴리오를 운용해주는 대가로 부과되는 수수료.</li>
    <li><b>위탁수수료</b>: 중개형 ISA에서 주식·ETF 등을 매매할 때마다 발생하는 거래 수수료.</li>
  </ul>
</div>

<p>여러 출처를 교차확인한 결과, <mark>신탁형 신탁보수는 대략 연 0.1~0.7%대, 일임형 운용관리수수료는 대략 연 0.1~0.6%대</mark> 범위에서 금융사·상품별로 다르게 매겨지고 있었습니다. 자료마다 나온 숫자의 소수점 단위까지는 서로 달라, 이 글에서는 범위로만 제시합니다.</p>

<p style="font-size:13px;color:#888;margin-top:6px;">단, 이 범위는 세율처럼 정해진 하나의 답이 아니라 금융사·상품마다 실제로 다르게 매기는 값입니다. 본인이 가입한(또는 가입할) 금융사의 정확한 요율은 아래 「내 계좌 수수료 직접 확인하는 방법」에서 확인하는 편이 정확합니다.</p>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">중개형 ISA는 수수료가 다른가요</h2>

<p>네, 다릅니다. 중개형은 계좌를 갖고 있다는 이유만으로 빠져나가는 돈이 없습니다.</p>

<ul style="line-height:1.9;">
  <li>매매하지 않고 그대로 두면 수수료가 발생하지 않습니다.</li>
  <li>주식·ETF를 사고팔 때만 <b>위탁수수료</b>가 붙습니다.</li>
  <li>위탁수수료율은 증권사마다 다르며, 이 부분은 별도로 정리한 <a href="https://sensitiveboss3.tistory.com/entry/broker-fee-comparison-2026" target="_blank" rel="noopener">증권사 수수료 비교 글</a>에서 자세히 다뤘습니다.</li>
</ul>

<p>그런데 국내 상장주식을 직접 사고팔 수 있는 유형은 중개형뿐입니다. 신탁형·일임형은 펀드·예금 등 편입 가능한 상품이 정해져 있어 매매수수료라는 개념 자체가 다르게 적용됩니다.</p>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">금융사별 ISA 수수료 비교표</h2>

<div style="background:#fdf3e3;border-left:4px solid #c98a1f;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>금융사별 정확한 요율은 원문 확인 중입니다</b>
  <p style="margin:8px 0 0 0;">금융투자협회 ISA다모아, 전국은행연합회 ISA 비교공시 등 1차 출처 조회 화면 캡처가 확보되는 대로 아래 표를 실제 수치로 채워 갱신하겠습니다. 확인 전까지는 수치를 지어내지 않습니다.</p>
</div>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">금융사</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">유형</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">신탁보수 / 운용관리수수료</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">신탁형</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">일임형</td>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">확인 중</td>
      <td style="border:1px solid #ddd;padding:8px;">중개형</td>
      <td style="border:1px solid #ddd;padding:8px;">계좌 유지수수료 없음(매매 시 위탁수수료만)</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">내 계좌 수수료 직접 확인하는 방법</h2>

<p><mark>가장 정확한 방법은 금융투자협회가 운영하는 ISA다모아에서 직접 조회하는 것</mark>입니다. 상품 안내 페이지에는 대표 요율만 크게 적혀 있는 경우가 많아, 비교공시 화면에서 확인하는 편이 확실합니다.</p>

<ol style="line-height:1.9;">
  <li><a href="https://isa.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 ISA다모아</a>에 접속합니다.</li>
  <li>가입한(또는 가입할) 유형이 신탁형이면 <b>신탁형 상품비교</b>, 일임형이면 <b>일임형 상품비교</b> 메뉴로 들어갑니다.</li>
  <li>비교하려는 금융사를 선택해 조회합니다.</li>
  <li>신탁보수율 또는 운용관리수수료율이 금융사별로 나열된 화면을 확인합니다.</li>
</ol>

<p>중개형이라면 이용 중인 증권사의 위탁수수료율을 앱이나 홈페이지의 수수료 안내 메뉴에서 바로 확인할 수 있습니다.</p>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">수수료를 낮추는 방법</h2>

<p>비용만 생각하면 <b>중개형이 상대적으로 유리</b>합니다. 매매하지 않는 기간에는 아무 비용도 발생하지 않기 때문입니다.</p>

<ul style="line-height:1.9;">
  <li>주식·ETF를 직접 고르고 관리할 여유가 있다면 중개형을 고려할 만합니다.</li>
  <li>전문가에게 맡기고 싶다면 일임형·신탁형을 선택하되, 가입 전에 요율을 비교해봅니다.</li>
  <li>이미 가입한 계좌라도 만기 전 다른 금융사로 <a href="https://sensitiveboss3.tistory.com/entry/isa-account-transfer-guide" target="_blank" rel="noopener">계좌 이전</a>이 가능하니, 요율 차이가 크다면 이전을 검토할 수 있습니다.</li>
</ul>

<p>단, 수수료만으로 금융사를 정하면 안 됩니다. 편입 가능한 상품 구성이나 운용 성과도 함께 봐야 전체 그림이 맞습니다.</p>

<h2 style="border-left:6px solid #c2540e;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">중개형 ISA는 정말 수수료가 하나도 없나요</summary>
  <p style="margin:10px 0 0 0;">계좌를 유지하는 비용은 없습니다. 단, 주식·ETF를 매매할 때는 증권사별 위탁수수료가 발생합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신탁보수와 운용관리수수료는 언제 빠져나가나요</summary>
  <p style="margin:10px 0 0 0;">거래와 상관없이 보유하는 동안 정해진 비율만큼 자산에서 정기적으로 차감됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">수수료가 가장 싼 유형은 어디인가요</summary>
  <p style="margin:10px 0 0 0;">보유 비용만 보면 중개형이 상대적으로 낮은 편입니다. 단, 정확한 요율은 금융사·상품마다 다르므로 ISA다모아에서 직접 비교해보는 것이 정확합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">가입 후에도 유형을 바꿀 수 있나요</summary>
  <p style="margin:10px 0 0 0;">유형 간 전환은 제한적입니다. 다른 금융사로 계좌를 이전하는 방법은 가능하니, 이전 절차를 정리한 별도 글을 참고하는 편이 좋습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증권사 매매수수료와 ISA 신탁보수는 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 매매수수료는 사고팔 때만 발생하고, 신탁보수·운용관리수수료는 거래 여부와 상관없이 보유 기간 동안 계속 발생합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://isa.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 ISA다모아</a>: 신탁형·일임형 상품비교 (금융사별 실측값은 조회 화면 캡처 후 반영 예정)</li>
    <li><a href="https://securities.miraeasset.com/hks/hks4659/n02.do" target="_blank" rel="noopener">미래에셋증권 ISA 제도안내</a>: 가입자격 및 종류</li>
    <li>기준일: 2026-09-23(WebSearch 교차검증일, 금융사별 실측값은 캡처 확보일로 갱신 예정)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 내용은 정보 제공용이며 특정 금융사나 상품 가입을 권유하지 않습니다. 수수료·보수율은 금융사와 시점에 따라 달라지므로, 가입 전 해당 금융사의 최신 안내를 직접 확인하시기 바랍니다. 투자 결과에 대한 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ISA 계좌 수수료 유형별 확인법",
  "description": "ISA 계좌의 중개형·신탁형·일임형 수수료 구조 차이와 대략적인 요율 범위, 금융투자협회 ISA다모아에서 본인 계좌의 정확한 수수료를 직접 확인하는 방법을 정리합니다. (금융사별 실측값은 조회 화면 캡처 후 확정)",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-23",
  "dateModified": "2026-09-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/isa-account-fee-check"
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
      "name": "중개형 ISA는 정말 수수료가 하나도 없나요",
      "acceptedAnswer": { "@type": "Answer", "text": "계좌를 유지하는 비용은 없습니다. 단, 주식·ETF를 매매할 때는 증권사별 위탁수수료가 발생합니다." }
    },
    {
      "@type": "Question",
      "name": "신탁보수와 운용관리수수료는 언제 빠져나가나요",
      "acceptedAnswer": { "@type": "Answer", "text": "거래와 상관없이 보유하는 동안 정해진 비율만큼 자산에서 정기적으로 차감됩니다." }
    },
    {
      "@type": "Question",
      "name": "수수료가 가장 싼 유형은 어디인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "보유 비용만 보면 중개형이 상대적으로 낮은 편입니다. 단, 정확한 요율은 금융사·상품마다 다르므로 ISA다모아에서 직접 비교해보는 것이 정확합니다." }
    },
    {
      "@type": "Question",
      "name": "가입 후에도 유형을 바꿀 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "유형 간 전환은 제한적입니다. 다른 금융사로 계좌를 이전하는 방법은 가능하니, 이전 절차를 정리한 별도 글을 참고하는 편이 좋습니다." }
    },
    {
      "@type": "Question",
      "name": "증권사 매매수수료와 ISA 신탁보수는 같은 건가요",
      "acceptedAnswer": { "@type": "Answer", "text": "다릅니다. 매매수수료는 사고팔 때만 발생하고, 신탁보수·운용관리수수료는 거래 여부와 상관없이 보유 기간 동안 계속 발생합니다." }
    }
  ]
}
</script>
