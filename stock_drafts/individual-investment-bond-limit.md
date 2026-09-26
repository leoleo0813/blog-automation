---
keyword: 개인투자용국채
title: 개인투자용국채 매입한도 분리과세
slug: individual-investment-bond-limit
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 7720 (PC 2270 / 모바일 5450)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
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
  [캡처로 완성]
  (a) 확정 반영: 5년·10년·20년 세 가지 만기 유형, 매월 청약, 최소 10만 원
      단위 매입, 판매대행기관(증권사) 앱을 통한 청약 절차를 단계별로 정리했다.
      상위 결과 대부분은 "장단점" 위주라 실제 청약 단계를 짚지 않는다.
  (b) 확정 반영: 일반 국채(장내 유통 국채)와의 차이 비교표 — 개인투자용국채는
      소유권 이전이 안 돼 만기 전 시장 매매가 불가능하고, 매입 1년이 지나야
      중도환매를 신청할 수 있으며 이 경우 가산금리·복리·분리과세 혜택이
      모두 빠진다는 점을 정리했다. 상위 글 중 이 차이를 표로 정리한 곳은
      드물다.
  (c) 사람 캡처로 확정(2026-09-26, 기획재정부 국채시장 공식 페이지
      ktb.moef.go.kr/personalInvGovBonds.do 원문 캡처): 연간 매입한도
      2억원(1인당, 최소 10만원부터), 분리과세 세율 14%(매입액 총 2억원까지).
      두 WebSearch 자료군 중 매입한도는 "2억원" 쪽이, 세율은 "14%" 쪽이
      맞았다 — 어느 한쪽 자료군이 통째로 맞은 게 아니라 수치별로 갈렸다는
      점을 투명하게 기록한다.
  (d) 캡처로 추가 확보한 세부 구조(상위 결과에 드문 정보): 표면금리는
      "전월 발행한 동일 연물 국고채 낙찰금리", 가산금리는 "시장상황 등
      고려 매월 결정·공표"라는 산정 방식 자체를 원문으로 확정. 만기 보유
      시 이 둘을 합쳐 연복리로 이자를 지급한다는 점, 상속·유증·강제집행
      외에는 소유권 이전이 불가하다는 점, 연간 국채 발행한도 등을 고려해
      12월은 개인투자용 국채가 미발행될 수 있다는 점도 원문에서 확인했다.
  (e) 확정된 수치로 세금 계산 예시 완성: 2억원을 5년 만기로 매입해 만기까지
      보유했다고 가정할 때, 분리과세(14%)와 금융소득종합과세 대상자의
      종합과세(가정 세율)를 비교하는 예시를 본문에 추가했다(가정 금리는
      명시적으로 "가정치"임을 밝히고, 실제 표면금리·가산금리는 매월
      변동한다는 점을 함께 안내).
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
  "14% 분리과세"(장단점 정리형 블로그 다수)로 나왔다.
  2026-09-26 사용자가 기획재정부 국채시장 공식 페이지
  (ktb.moef.go.kr/personalInvGovBonds.do) 원문을 직접 캡처해 확정했다:
  매입한도 2억원(1인당 연간), 분리과세 세율 14%(매입액 총 2억원까지).
  이로써 두 WebSearch 자료군 중 어느 한쪽도 전부 맞지 않았음을 확인했다
  — 매입한도는 "2억원" 자료군이, 세율은 "14%" 자료군이 맞았다.
  캡처 원본은 sources/user-capture-2026-09-26-individual-investment-bond-
  limit.webp에 보관.
source_conflict_resolved: |
  매입한도: "2억원"(kbthink.com, PwC 삼일회계법인, 기획재정부 자료 인용
  스니펫) vs "1억원"(WebSearch 요약에 인용된 일부 장단점 정리형 콘텐츠).
  분리과세 세율: "15.4%"(kbthink.com, PwC) vs "14%"(같은 부류의 장단점
  정리형 콘텐츠). 2026-09-26 사용자가 기획재정부 국채시장 공식 페이지
  (ktb.moef.go.kr/personalInvGovBonds.do) 원문을 캡처해 확정: 매입한도는
  "2억원"이 맞고, 분리과세 세율은 "14%"가 맞다. 즉 두 자료군 모두
  절반씩만 맞았다 — "2억원·15.4%" 자료군은 한도는 맞혔지만 세율을
  틀렸고, "1억원·14%" 자료군은 세율은 맞혔지만 한도를 틀렸다. 이 사례는
  RULES.md가 강조하는 "출처가 그럴듯해 보여도 개별 수치는 따로
  검증해야 한다"는 원칙을 다시 확인시켜준다. 캡처 원본은 sources/에 보관.
기준일: 2026-09-26 (매입한도·분리과세 세율은 사용자 캡처 원문 기준, 그 외는
  2026-09-24 WebSearch 교차검증 기준)
tags: 개인투자용국채, 저축성국채, 국채투자, 분리과세, 매입한도, 국채금리, 주식초보, 절세, 채권투자
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-26, 캡처 반영). 게이트1 실측 7,840회,
  게이트2 v3 기준 통과, 청약 절차·만기 유형·일반 국채 비교는 WebSearch
  교차검증으로 확정, 매입한도(2억원)·분리과세 세율(14%)은 기획재정부
  국채시장 공식 페이지 원문 캡처로 확정했다. 확정 수치로 5년 만기 2억원
  세금 계산 예시를 완성했다.
self_check: |
  [2026-09-26 최종 판정 — 캡처 반영, gate_pass:true]
  게이트1 충족 — 네이버 키워드도구 실측 7,840회(일반 주제 기준 500 이상,
  이번 배치 중 최고 검색량).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당
  (serp_check 참조).
  게이트3 충족 — 청약 절차·만기 유형·일반 국채와의 차이에 더해, 확정된
  매입한도·세율로 5년 만기 2억원 세금 계산 예시(분리과세 vs 종합과세)를
  완성했다.
  게이트4 충족(캡처) — 1차 출처 WebFetch EGRESS_BLOCKED(대조군 google.com도
  차단 확인, 세션 전면 차단). 2차 교차검증에서 핵심 수치가 출처 간
  충돌했으나(source_conflict_resolved 참조), 2026-09-26 사용자가
  기획재정부 국채시장 공식 페이지 원문을 캡처해 매입한도 2억원·분리과세
  세율 14%로 확정했다. 두 WebSearch 자료군 모두 절반만 맞았다는 점을
  투명하게 기록했다.
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
  시맨틱. 매입한도·세율 모두 캡처 원문 수치로 확정해 "확인 중" 표기를
  전부 제거했다.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 발행 본문(YAML 제외)에서
  "—" 0개 확인(YAML의 "—"는 자동화 기록용 구분자라 본문 대상에서 제외).
  "다만"은 본문에서 1회만 사용(나머지 전환은 "단,"·"그런데"·"반면"으로 분산). 본문
  `<mark>` 총 5개(3~5개 기준 충족, 상한선 — 캡처 반영으로 4개에서 5개로
  늘어남). FAQ 5개(6개 고정 탈피). 핵심요약
  박스 제목을 "🔍 먼저 확인할 것"으로, 색상은 슬레이트블루 계열
  (#eef1fb/#3949ab)로 최근 게시물(테라코타·핑크·바이올렛·인디고·앰버·틸·
  그린·퍼플)과 겹치지 않게 골랐다. 목차 제외 본문 H2 6개 중 서술형
  4개("매입 방법과 만기 종류", "매입한도와 분리과세, 자료마다 다른 이유",
  "일반 국채와 다른 점", "원문에서 직접 확인하는 방법"), 질문형 2개
  ("개인투자용국채란 무엇인가요", "중도환매하면 어떻게 되나요")로 "~나요"
  편중 없음(전체 6개 중 2개, 33%).
  헤지 표현 남발 없음 — 수치 상충이 있었다는 경위를 본문에 정직하게
  남기고("자료마다 다른 이유" 문단), "~것으로 알려져 있다" 류 표현은
  쓰지 않음. 면책 문구는 기존 게시물과 다른 표현으로 작성.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-26</p>

<p>개인투자용국채는 <mark>개인만 살 수 있는 저축성 국채</mark>로, 만기까지 들고 있으면 이자소득에 분리과세 혜택이 붙는 상품입니다. 연간 매입한도는 2억원, 분리과세 세율은 14%로 기획재정부 원문을 통해 확인했습니다.</p>

<div style="background:#eef1fb;border:2px solid #3949ab;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1a237e;font-size:18px;">🔍 먼저 확인할 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>개인투자용국채는 5년·10년·20년 만기 중 골라 매월 청약으로 매입합니다.</li>
    <li>만기까지 보유해야 가산금리·복리·분리과세 혜택을 모두 받습니다.</li>
    <li>연간 매입한도는 <b>1인당 2억원</b>, 만기까지 보유 시 분리과세 세율은 <b>14%</b>입니다.</li>
    <li>일반 국채와 달리 만기 전에는 시장에서 사고팔 수 없습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>개인투자용국채란 무엇인가요</li>
  <li>매입 방법과 만기 종류</li>
  <li>매입한도와 분리과세, 정확한 수치</li>
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

<p>표면금리는 전월 발행한 동일 연물 국고채 낙찰금리를 그대로 따르고, 여기에 가산금리를 더해 최종 금리가 정해집니다. 가산금리는 시장 상황 등을 고려해 매월 새로 결정·공표되므로, 이번 달과 다음 달 청약분의 금리가 다를 수 있습니다. 만기까지 보유하면 이 표면금리와 가산금리를 합쳐 연복리로 이자가 붙습니다. 연간 국채 발행한도 등을 고려해 12월에는 개인투자용국채가 발행되지 않을 수도 있습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>용어 정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>판매대행기관</b>: 정부를 대신해 개인투자용국채 청약을 접수하는 증권사.</li>
    <li><b>분리과세</b>: 이자소득을 다른 소득과 합치지 않고 정해진 세율로만 떼는 과세 방식.</li>
    <li><b>표면금리</b>: 전월 발행한 동일 연물 국고채 낙찰금리를 그대로 적용하는 기본 금리.</li>
    <li><b>가산금리</b>: 표면금리에 추가로 얹어주는 금리로, 시장 상황을 고려해 매월 결정·공표된다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #3949ab;padding-left:12px;margin-top:36px;">매입한도와 분리과세, 정확한 수치</h2>

<p>검색해보면 연간 매입한도를 <b>2억 원</b>이라고 쓴 자료와 <b>1억 원</b>이라고 쓴 자료가 동시에 나오고, 분리과세 세율도 <b>15.4%</b>라는 자료와 <b>14%</b>라는 자료가 섞여 있습니다. 기획재정부 국채시장 공식 페이지 원문을 직접 확인한 결과, <mark>매입한도는 1인당 연간 2억 원, 분리과세 세율은 14%</mark>가 맞습니다.</p>

<p style="font-size:13px;color:#888;margin-top:6px;">흥미로운 점은 어느 한쪽 자료가 통째로 맞은 게 아니라는 것입니다. "2억 원·15.4%"라고 쓴 자료는 한도는 맞혔지만 세율을 틀렸고, "1억 원·14%"라고 쓴 자료는 세율은 맞혔지만 한도를 틀렸습니다. 숫자를 인용할 때는 출처가 그럴듯해 보여도 수치 하나하나를 따로 확인해야 한다는 걸 보여주는 사례입니다.</p>

<div style="background:#eef6f0;border-left:4px solid #2e7d32;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>2억원을 5년 만기로 투자하면 세금이 얼마나 다를까(가정 예시)</b>
  <p style="margin:8px 0 0 0;">표면금리와 가산금리는 매월 바뀌므로, 이해를 돕기 위해 연 3.5%(가정치)로 5년간 이자 총 3,500만원이 발생했다고 가정해 보겠습니다.</p>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>분리과세 적용(만기까지 보유): 3,500만원 × 14% = <b>세금 490만원</b></li>
    <li>금융소득종합과세 대상자가 다른 소득과 합산 과세될 경우(예: 종합소득세 최고세율 구간 45% 가정): 3,500만원 × 45% = <b>세금 1,575만원</b></li>
  </ul>
  <p style="margin:8px 0 0 0;">실제 표면금리·가산금리는 청약 시점마다 다르고, 종합과세 여부와 세율도 개인의 다른 소득 수준에 따라 달라지므로 이 예시는 구조를 보여주기 위한 가정치입니다.</p>
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
      <td style="border:1px solid #ddd;padding:8px;">불가능(상속·유증·강제집행 외 소유권 이전 불가)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">중도환매</td>
      <td style="border:1px solid #ddd;padding:8px;">해당 없음(매도로 대체)</td>
      <td style="border:1px solid #ddd;padding:8px;">매입 1년 후부터 신청 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">분리과세 혜택</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">만기 보유 시에만 적용(매입액 총 2억원까지, 세율 14%)</td>
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

<p>이 글의 매입한도(2억원)·분리과세 세율(14%)은 <mark>기획재정부 국채시장 사이트 원문</mark>으로 확인한 수치입니다. 다만 가산금리는 매월 바뀌고 제도 자체도 개정될 수 있으므로, 청약 직전에는 아래 페이지에서 그 시점 기준으로 다시 확인하는 편이 안전합니다.</p>

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
  <p style="margin:10px 0 0 0;">1인당 연간 2억 원입니다. 최소 10만 원부터 10만 원 단위로 매입할 수 있고, 만기까지 보유하면 매입액 총 2억 원까지 이자소득에 14% 분리과세가 적용됩니다.</p>
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
    <li><a href="https://ktb.moef.go.kr/personalInvGovBonds.do" target="_blank" rel="noopener">기획재정부 국채시장 - 개인투자용 국채</a>: 매입한도·분리과세 원문(사용자 캡처, 2026-09-26)</li>
    <li><a href="https://securities.miraeasset.com/hks/hks4046/n01.do" target="_blank" rel="noopener">미래에셋증권 개인투자용국채 안내</a>: 청약 절차 및 상품 안내</li>
    <li>기준일: 매입한도·분리과세 세율은 2026-09-26(사용자 캡처 원문 기준), 그 외 항목은 2026-09-24 WebSearch 교차검증 기준</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 개인투자용국채라는 상품의 구조를 설명할 뿐, 매수를 권하는 글이 아닙니다. 표면금리·가산금리는 매월 바뀌고 매입한도·세율 등 제도 자체도 개정될 수 있으므로 가입 전에 반드시 기획재정부나 판매대행기관의 최신 공지를 직접 확인하시기 바랍니다. 투자로 인한 손익은 투자자 본인의 책임입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "개인투자용국채 매입한도 분리과세",
  "description": "개인투자용국채의 매입 방법과 만기 종류, 일반 국채와의 차이, 중도환매 조건을 정리합니다. 연간 매입한도 2억원, 분리과세 세율 14%를 기획재정부 원문으로 확인하고 세금 계산 예시를 담았습니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-24",
  "dateModified": "2026-09-26",
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
      "acceptedAnswer": { "@type": "Answer", "text": "1인당 연간 2억 원입니다. 최소 10만 원부터 10만 원 단위로 매입할 수 있고, 만기까지 보유하면 매입액 총 2억 원까지 이자소득에 14% 분리과세가 적용됩니다." }
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
