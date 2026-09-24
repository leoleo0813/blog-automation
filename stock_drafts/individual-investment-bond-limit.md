---
keyword: 개인투자용국채
title: 개인투자용국채 매입한도 분리과세
slug: individual-investment-bond-limit
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 7,840 (PC 2,340 / 모바일 5,500)
gate1_pass: true (일반 주제 기준 월 500 이상 필요 — check-keywords.yml 2026-09-24 실측)
serp_check: |
  [게이트2 v3 판정 2026-09-24 — 통과]
  WebSearch "개인투자용국채 장단점 후기 매입 방법" 상위 9개:
  banksalad.com(뱅크샐러드, 핀테크 미디어) / toss.im(토스피드, 대형 핀테크) /
  brunch.co.kr(개인 콘텐츠) / eiec.kdi.re.kr(KDI, 준정부 연구기관) /
  securities.miraeasset.com(미래에셋증권, 공식 판매대행기관) /
  ktb.moef.go.kr(기획재정부 국채시장, 정부 공식) / rainbowwater.kr(개인·소규모
  세금상식 블로그) / aiwoori.com(개인·소규모 블로그) / 위키백과(주제 무관, 검색
  노이즈로 제외)
  1) 진입 여지 — 있음. brunch·rainbowwater·aiwoori 3곳이 개인·소규모 콘텐츠로,
     9개 중 3분의 1을 차지한다.
  2) 검색 의도 — "장단점·매입 방법"을 묻는 정보 탐색형이다. 조회·신청·계산기
     실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 아니다. 오히려 상위 결과끼리 핵심 수치(매입한도 1억 vs
     2억원, 분리과세 세율 14% vs 15.4%)가 서로 달라 "무엇이 맞는 수치인지"
     자체가 아직 정리되지 않은 상태다(primary_source 참조). 이 혼란을 원문
     기준으로 정리하는 것 자체가 정보이득이 된다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [부분 완성 — 매입한도·분리과세 세율의 정확한 원문 수치는 캡처 대기]
  (a) 확정 반영: 5년·10년·20년 세 가지 만기 유형, 매월 청약, 최소 10만 원
      단위 매입, 판매대행기관(증권사) 앱을 통한 청약 절차를 단계별로 정리했다.
      상위 결과 대부분은 "장단점" 위주라 실제 청약 단계를 짚지 않는다.
  (b) 확정 반영: 일반 국채(장내 유통 국채)와의 차이 비교표 — 개인투자용국채는
      소유권 이전이 안 돼 만기 전 시장 매매가 불가능하고, 매입 1년이 지나야
      중도환매를 신청할 수 있으며 이 경우 가산금리·복리·분리과세 혜택이
      모두 빠진다는 점을 정리했다. 상위 글 중 이 차이를 표로 정리한 곳은
      드물다.
  (c) 캡처 대기: 이 글의 핵심이 될 수치 두 가지 — 연간 매입한도(1억원 vs
      2억원 중 어느 쪽이 맞는지)와 분리과세 세율(14% vs 15.4% 중 어느 쪽이
      맞는지)이 WebSearch 교차검증에서 자료마다 엇갈렸다. 원문(기획재정부
      국채시장 또는 조세특례제한법 조문) 확인 전까지는 어느 쪽도 단정하지
      않는다. 이 수치가 확정되면 "2억원을 5년 만기로 투자했을 때 분리과세
      적용 시와 종합과세 적용 시 세금 차이" 계산 예시를 추가해 정보이득을
      완성할 계획이다.
primary_source: |
  1차 시도: 기획재정부 국채시장 개인투자용국채 안내 페이지
  (https://ktb.moef.go.kr/personalInvGovBonds.do)에 WebFetch를 1회 시도 →
  EGRESS_BLOCKED(2026-09-24). 대조군으로 같은 세션에서 www.google.com도
  WebFetch 1회 시도했으나 동일하게 EGRESS_BLOCKED가 떨어져, 특정 도메인
  문제가 아니라 이 세션의 전면 차단임을 확인했다.
  RULES.md 「1차 출처가 막혔을 때」 기준에 따라 2차 출처 교차검증을 시도했다.
  개인투자용국채의 기본 성격(2024년 6월 최초 발행, 개인만 매입 가능한 저축성
  국채, 5·10·20년 만기, 매월 청약)은 kbthink.com(KB국민은행 공식)·
  eiec.kdi.re.kr(KDI, 준정부)·securities.miraeasset.com(미래에셋증권 공식)·
  toss.im(토스피드) 등 4곳 이상에서 충돌 없이 일치해 확정 반영했다.
  그러나 핵심 수치인 (1) 연간 매입한도와 (2) 분리과세 세율은 자료마다
  달랐다 — 한 검색 결과 묶음에서는 "1인당 매입한도 2억원, 분리과세 15.4%"
  (kbthink.com, PwC 삼일회계법인 인사이트, 기획재정부 자료 인용 스니펫)로
  나왔고, 다른 검색 결과 묶음에서는 "최소 10만 원, 연간 최대 1억원"이며
  "14% 분리과세"(장단점 정리형 블로그 다수)로 나왔다. 이는 세율·한도
  숫자에서 자료 간 실제 충돌이 확인된 경우로, RULES.md가 과거 대주주 기준
  5배 차이 사례를 근거로 "2차 보도의 근사치보다 원문 확정이 특히
  중요하다"고 명시한 유형에 정확히 해당한다. source_conflict로 기록하고
  본문에 두 수치를 함께 쓰지 않으며, gate4는 미충족으로 둔다.
source_conflict: |
  매입한도: "2억원"(kbthink.com, PwC 삼일PwC 인사이트, 기획재정부 보도자료
  인용 스니펫) vs "1억원"(WebSearch 요약에 인용된 일부 장단점 정리형
  콘텐츠). 분리과세 세율: "15.4%"(kbthink.com, PwC) vs "14%"(같은 부류의
  장단점 정리형 콘텐츠). 판단: 기획재정부 원문과 회계법인(PwC) 자료가
  가리키는 "2억원·15.4%" 쪽이 더 신뢰도 높아 보이나, 사람이 원문(1순위
  ktb.moef.go.kr 또는 조세특례제한법 제91조의16 조문)에서 최종 확정하기
  전까지 본문에 어느 수치도 확정해 쓰지 않는다.
기준일: 2026-09-24 (WebSearch 교차검증일 — 매입한도·분리과세 세율은 원문
  확인 후 확정 예정)
tags: 개인투자용국채, 저축성국채, 국채투자, 분리과세, 매입한도, 국채금리, 주식초보, 절세, 채권투자
gate_pass: false
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 7,840회(PC 2,340/모바일 5,500,
  일반 주제 기준 500 이상). 같은 배치에서 함께 확인한 다트 뜻(70)·호가창
  뜻(30)·배당가산율(20)·성장주 가치주 뜻(20)·왝더도그 뜻(20)은 FAIL,
  우량주 뜻(1,210)·테마주 뜻(830)은 PASS했으나 검색량이 개인투자용국채보다
  낮아 backlog로 넘겼다(사전형 개념이라 정보이득 확보 난이도도 더 높음).
  게이트2 충족 — v3 기준 통과(serp_check 참조).
  게이트3 부분 충족 — 청약 절차, 일반 국채와의 차이 비교표는 확정했다.
  다만 이 글의 핵심 수치(매입한도·분리과세 세율)가 자료마다 충돌해 아직
  정보이득의 핵심(계산 예시)을 완성하지 못했다.
  게이트4 미충족 — 1차 출처 WebFetch가 EGRESS_BLOCKED로 막혔고(대조군
  google.com도 차단 확인), 2차 교차검증에서도 핵심 수치가 출처 간에
  충돌해(source_conflict 참조) 확정할 수 없었다. RULES.md의 세율·한도
  숫자 캡처 우선 원칙에 따라 human-assisted로 전환한다.
capture_guide: |
  (1) 왜 필요한가 — 이 글의 핵심 수치인 연간 매입한도와 분리과세 세율이
  검색 결과마다 다릅니다. 한쪽은 "2억원·15.4%"를, 다른 쪽은 "1억원·14%"를
  말하고 있어 원문 확인 없이는 어느 쪽도 쓸 수 없습니다. 이 프로젝트가
  과거 비슷한 유형의 숫자에서 자료 간 5배 차이 오류를 잡아낸 적이 있어
  더욱 신중하게 접근합니다.
  (2) 확인할 곳(우선순위):
  1순위. 기획재정부 국채시장 개인투자용국채 안내
  https://ktb.moef.go.kr/personalInvGovBonds.do 접속 → 페이지 안에서
  "매입한도"와 "분리과세"(또는 "세제혜택") 관련 문단이 보이는 화면을 캡처.
  발행계획 페이지 https://ktb.moef.go.kr/perIsuPlan.do 도 함께 확인하면
  좋습니다.
  2순위. 국세법령정보시스템(taxlaw.nts.go.kr)이나 국가법령정보센터
  (law.go.kr)에서 "조세특례제한법 제91조의16"(개인투자용 국채등에 대한
  과세특례)을 검색해 조문에 나온 매입한도·세율·보유기간 요건 화면을 캡처.
  3순위. 미래에셋증권 개인투자용국채 안내
  https://securities.miraeasset.com/hks/hks4046/n01.do 에서 매입한도·
  세제혜택 안내 문구가 보이는 화면을 캡처(판매대행기관 공식 안내라 참고
  가치는 있으나 2순위 법령 원문보다는 우선순위가 낮습니다).
  (3) 캡처가 끝나면 — 스크린샷을 대화에 올려주시고, 확인하신 매입한도
  (1억원/2억원 중 실제 값)와 분리과세 세율(14%/15.4% 중 실제 값), 조회
  기준일자를 함께 알려주시면 본문 표와 세금 계산 예시에 반영해 gate_pass를
  재판정하겠습니다.
self_check: |
  [2026-09-24 판정 — gate_pass:false로 저장]
  게이트1 충족 — 네이버 키워드도구 실측 7,840회(일반 주제 기준 500 이상,
  이번 배치 중 최고 검색량).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당
  (serp_check 참조).
  게이트3 부분 충족 — 청약 절차·만기 유형·일반 국채와의 차이는 확정
  반영했다. 핵심 정보이득이 될 매입한도·분리과세 세율 계산 예시는 캡처
  대기.
  게이트4 미충족 — 1차 출처 WebFetch EGRESS_BLOCKED(대조군 google.com도
  차단 확인, 세션 전면 차단). 2차 교차검증에서 핵심 수치가 출처 간 충돌
  (source_conflict)해 human-assisted 캡처로 전환.
  카니벌라이제이션 점검 — 기존 77편 중 "개인투자용국채"를 다룬 편 없음
  (grep 0건). 37편(채권 세금)은 일반 회사채·국채 이자소득세를 다루지만
  개인투자용국채의 분리과세 특례는 별도 제도라 겹치지 않는다(본문에서
  37편으로 내부 링크해 구분을 명시).
  기관 링크 점검 — 본문에서 기획재정부·미래에셋증권으로 안내하는 문장과
  하단 참고 출처 전부 target="_blank" rel="noopener"로 링크 처리. 정부
  기관 링크는 nofollow 미부착.
  제목 "개인투자용국채 매입한도 분리과세" 17자·금지어 없음·조사/접속사
  없음. 슬러그 영문 소문자+하이픈 4단어(individual-investment-bond-limit).
  인트로 문단 최상단 배치, "안녕하세요" 없음. 비교표 1개 thead/tbody
  시맨틱. 확정 못한 수치는 "확인 중"으로 표기하고 지어내지 않았다.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 발행 본문(YAML 제외)에서
  "—" 0개 확인(YAML의 "—"는 자동화 기록용 구분자라 본문 대상에서 제외).
  "다만"은 본문에서 1회만 사용(나머지 전환은 "단,"·"그런데"·"반면"으로 분산). 본문
  `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약
  박스 제목을 "🔍 먼저 확인할 것"으로, 색상은 슬레이트블루 계열
  (#eef1fb/#3949ab)로 최근 게시물(테라코타·핑크·바이올렛·인디고·앰버·틸·
  그린·퍼플)과 겹치지 않게 골랐다. 목차 제외 본문 H2 6개 중 서술형
  4개("매입 방법과 만기 종류", "매입한도와 분리과세, 자료마다 다른 이유",
  "일반 국채와 다른 점", "원문에서 직접 확인하는 방법"), 질문형 2개
  ("개인투자용국채란 무엇인가요", "중도환매하면 어떻게 되나요")로 "~나요"
  편중 없음(전체 6개 중 2개, 33%).
  헤지 표현 남발 없음 — 수치가 확정되지 않았다는 사실 자체를 정직하게
  명시하고 반복하지 않음("~것으로 알려져 있다" 류 표현 미사용). 면책
  문구는 기존 게시물과 다른 표현으로 작성.
  종합 판정: 게이트1·2 충족, 게이트3 부분 충족, 게이트4 미충족(핵심
  수치 캡처 대기) → gate_pass:false. 사람 캡처 대기 상태로 저장.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-24</p>

<p>개인투자용국채는 <mark>개인만 살 수 있는 저축성 국채</mark>로, 만기까지 들고 있으면 이자소득에 분리과세 혜택이 붙는 상품입니다. 다만 매입한도와 세율을 다루는 글마다 숫자가 조금씩 달라, 이 글에서는 확실한 부분과 아직 원문 확인이 더 필요한 부분을 나눠 정리합니다.</p>

<div style="background:#eef1fb;border:2px solid #3949ab;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1a237e;font-size:18px;">🔍 먼저 확인할 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>개인투자용국채는 5년·10년·20년 만기 중 골라 매월 청약으로 매입합니다.</li>
    <li>만기까지 보유해야 가산금리·복리·분리과세 혜택을 모두 받습니다.</li>
    <li>연간 매입한도와 분리과세 세율은 검색 결과마다 다르게 나와, 이 글에서는 원문 확인 전까지 단정하지 않습니다.</li>
    <li>일반 국채와 달리 만기 전에는 시장에서 사고팔 수 없습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>개인투자용국채란 무엇인가요</li>
  <li>매입 방법과 만기 종류</li>
  <li>매입한도와 분리과세, 자료마다 다른 이유</li>
  <li>일반 국채와 다른 점</li>
  <li>중도환매하면 어떻게 되나요</li>
  <li>원문에서 직접 확인하는 방법</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">개인투자용국채란 무엇인가요</h2>

<p>2024년 6월 처음 발행된 저축성 국채로, 매입 자격이 개인으로 한정됩니다. 기관이나 법인은 살 수 없고, 개인이 소액 단위로 안정적인 장기 자산을 모으도록 설계된 상품입니다.</p>

<p>일반 국채는 증권사 계좌를 통해 장내에서 누구나 사고팔 수 있지만, 개인투자용국채는 전용 계좌를 만들어 청약해야 하고 발행 후에는 시장에서 거래되지 않습니다.</p>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">매입 방법과 만기 종류</h2>

<p>만기는 5년·10년·20년 세 종류로 나뉘고, <mark>매월 정해진 기간에 청약 방식으로 모집</mark>합니다. 최소 매입 금액은 10만 원이며 10만 원 단위로 금액을 늘릴 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>판매대행기관(증권사)의 앱이나 지점에서 전용 계좌를 개설합니다.</li>
  <li>청약 기간에 원하는 만기와 금액을 정해 신청합니다.</li>
  <li>경쟁률이 높으면 한도 내에서 배정되며, 초과 청약분은 환불됩니다.</li>
  <li>이자 지급 방식은 만기에 원금과 이자를 한 번에 받는 복리형과, 매년 이자를 받다가 만기에 추가 이자를 받는 방식으로 나뉩니다.</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>용어 정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>판매대행기관</b>: 정부를 대신해 개인투자용국채 청약을 접수하는 증권사.</li>
    <li><b>분리과세</b>: 이자소득을 다른 소득과 합치지 않고 정해진 세율로만 떼는 과세 방식.</li>
    <li><b>가산금리</b>: 만기까지 보유했을 때 표면금리에 추가로 얹어주는 금리.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">매입한도와 분리과세, 자료마다 다른 이유</h2>

<p>이 부분이 가장 헷갈립니다. 검색해보면 <b>연간 매입한도를 2억 원이라고 쓴 자료</b>와 <b>1억 원이라고 쓴 자료</b>가 동시에 나옵니다. 분리과세 세율도 <b>15.4%</b>라는 자료와 <b>14%</b>라는 자료가 섞여 있습니다.</p>

<p>여러 출처를 교차확인한 결과, 국민은행 자료·회계법인(PwC) 자료·기획재정부 발간자료를 인용한 자료는 "2억 원·15.4%" 쪽을 가리켰습니다. 반면 일부 장단점 정리형 콘텐츠는 "1억 원·14%"로 적고 있었습니다.</p>

<p style="font-size:13px;color:#888;margin-top:6px;">두 세트 중 어느 쪽이 최신 기준인지 이 글에서는 단정하지 않습니다. 기획재정부 국채시장 페이지나 조세특례제한법 조문에서 원문을 확인하는 대로 정확한 수치와 계산 예시로 이 부분을 채우겠습니다.</p>

<div style="background:#fff8e1;border-left:4px solid #f9a825;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>매입한도·분리과세 세율은 원문 확인 중입니다</b>
  <p style="margin:8px 0 0 0;">확인되는 대로 아래 내용을 정확한 수치로 갱신하고, "2억 원을 5년 만기로 투자했을 때 분리과세 적용 시 세금이 얼마나 줄어드는지" 계산 예시도 추가하겠습니다.</p>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">일반 국채와 다른 점</h2>

<p>가장 큰 차이는 <mark>만기 전에 시장에서 팔 수 있는지 여부</mark>입니다. 일반 국채(장내 국채)는 증권사 계좌로 언제든 사고팔 수 있지만, 개인투자용국채는 소유권 자체를 다른 사람에게 넘길 수 없습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">일반 국채(장내)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">개인투자용국채</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매입 자격</td>
      <td style="border:1px solid #ddd;padding:8px;">개인·기관 모두 가능</td>
      <td style="border:1px solid #ddd;padding:8px;">개인만 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">중도 매매</td>
      <td style="border:1px solid #ddd;padding:8px;">증권사 계좌로 언제든 가능</td>
      <td style="border:1px solid #ddd;padding:8px;">불가능(소유권 이전 불가)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">중도환매</td>
      <td style="border:1px solid #ddd;padding:8px;">해당 없음(매도로 대체)</td>
      <td style="border:1px solid #ddd;padding:8px;">매입 1년 후부터 신청 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">분리과세 혜택</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">만기 보유 시에만 적용(확인 중인 한도까지)</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">중도환매하면 어떻게 되나요</h2>

<p>매입 후 1년이 지나면 중도환매를 신청할 수 있습니다. 그런데 이 경우 가산금리·복리 효과·분리과세 혜택이 전부 빠지고 원금과 기본 이자만 돌려받는 구조입니다.</p>

<ul style="line-height:1.9;">
  <li>급하게 현금이 필요할 가능성이 있다면 처음부터 만기가 짧은 5년물을 고려할 수 있습니다.</li>
  <li>중도환매 신청 절차와 한도는 판매대행기관(증권사)마다 안내가 다를 수 있어 가입 전 확인이 필요합니다.</li>
  <li>만기까지 보유할 자신이 없다면 일반 국채나 예금 등 다른 상품과 비교해보는 편이 낫습니다.</li>
</ul>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">원문에서 직접 확인하는 방법</h2>

<p>정확한 매입한도와 세율을 지금 바로 확인하고 싶다면 <mark>기획재정부 국채시장 사이트에서 직접 확인</mark>하는 것이 가장 정확합니다.</p>

<ol style="line-height:1.9;">
  <li><a href="https://ktb.moef.go.kr/personalInvGovBonds.do" target="_blank" rel="noopener">기획재정부 국채시장 - 개인투자용 국채</a> 페이지에 접속합니다.</li>
  <li>매입한도·분리과세 관련 안내 문단을 확인합니다.</li>
  <li>이용 중인 증권사의 <a href="https://securities.miraeasset.com/hks/hks4046/n01.do" target="_blank" rel="noopener">개인투자용국채 안내 페이지</a>에서도 동일한 수치가 나오는지 함께 대조합니다.</li>
</ol>

<p>채권 이자소득세 전반에 대해서는 별도로 정리한 <a href="https://sensitiveboss3.tistory.com/entry/bond-tax-guide" target="_blank" rel="noopener">채권 세금 글</a>도 참고할 만합니다. 단, 개인투자용국채의 분리과세 특례는 일반 채권 과세와는 별도 제도라는 점을 구분해서 봐야 합니다.</p>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">개인투자용국채는 누구나 살 수 있나요</summary>
  <p style="margin:10px 0 0 0;">개인만 매입할 수 있습니다. 법인이나 기관은 매입 대상이 아닙니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">만기 전에 팔고 싶으면 어떻게 하나요</summary>
  <p style="margin:10px 0 0 0;">시장에 내다 팔 수는 없고, 매입 1년 후부터 중도환매를 신청할 수 있습니다. 이때는 가산금리·복리·분리과세 혜택이 빠집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">연간 매입한도는 정확히 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">자료마다 1억 원과 2억 원으로 다르게 나와 있어 이 글에서는 아직 단정하지 않습니다. 기획재정부 국채시장 페이지에서 원문을 확인하는 대로 갱신하겠습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">일반 국채를 사는 것과 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">가장 큰 차이는 중도 매매 가능 여부입니다. 일반 국채는 증권사 계좌로 언제든 사고팔 수 있지만, 개인투자용국채는 소유권을 넘길 수 없어 만기까지 들고 있거나 중도환매를 신청해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">최소 얼마부터 투자할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">10만 원부터 10만 원 단위로 매입할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://ktb.moef.go.kr/personalInvGovBonds.do" target="_blank" rel="noopener">기획재정부 국채시장 - 개인투자용 국채</a>: 매입한도·분리과세 원문 확인용 (정확한 수치는 캡처 확보 후 반영 예정)</li>
    <li><a href="https://securities.miraeasset.com/hks/hks4046/n01.do" target="_blank" rel="noopener">미래에셋증권 개인투자용국채 안내</a>: 청약 절차 및 상품 안내</li>
    <li>기준일: 2026-09-24(WebSearch 교차검증일, 핵심 수치는 캡처 확보일로 갱신 예정)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 개인투자용국채라는 상품의 구조를 설명할 뿐, 매수를 권하는 글이 아닙니다. 매입한도·세율·발행 조건은 시점에 따라 바뀔 수 있으므로 가입 전에 반드시 기획재정부나 판매대행기관의 최신 공지를 직접 확인하시기 바랍니다. 투자로 인한 손익은 투자자 본인의 책임입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "개인투자용국채 매입한도 분리과세",
  "description": "개인투자용국채의 매입 방법과 만기 종류, 일반 국채와의 차이, 중도환매 조건을 정리합니다. 매입한도와 분리과세 세율은 자료마다 수치가 달라 원문 확인 후 계산 예시와 함께 확정할 예정입니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-24",
  "dateModified": "2026-09-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/individual-investment-bond-limit"
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
      "name": "개인투자용국채는 누구나 살 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "개인만 매입할 수 있습니다. 법인이나 기관은 매입 대상이 아닙니다." }
    },
    {
      "@type": "Question",
      "name": "만기 전에 팔고 싶으면 어떻게 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "시장에 내다 팔 수는 없고, 매입 1년 후부터 중도환매를 신청할 수 있습니다. 이때는 가산금리·복리·분리과세 혜택이 빠집니다." }
    },
    {
      "@type": "Question",
      "name": "연간 매입한도는 정확히 얼마인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "자료마다 1억 원과 2억 원으로 다르게 나와 있어 이 글에서는 아직 단정하지 않습니다. 기획재정부 국채시장 페이지에서 원문을 확인하는 대로 갱신하겠습니다." }
    },
    {
      "@type": "Question",
      "name": "일반 국채를 사는 것과 뭐가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "가장 큰 차이는 중도 매매 가능 여부입니다. 일반 국채는 증권사 계좌로 언제든 사고팔 수 있지만, 개인투자용국채는 소유권을 넘길 수 없어 만기까지 들고 있거나 중도환매를 신청해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "최소 얼마부터 투자할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "10만 원부터 10만 원 단위로 매입할 수 있습니다." }
    }
  ]
}
</script>
