---
keyword: 비과세종합저축
title: 비과세종합저축 조건과 한도 2026
slug: tax-exempt-savings-limit-2026
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 4610 (PC 900 / 모바일 3710, 2026-09-24 실측, 제도 기준 100 이상 적용)
gate1_pass: true
serp_check: |
  [게이트2 v3 판정 2026-09-24 — 통과]
  WebSearch "비과세종합저축 가입조건 한도 이자소득세 2026" 상위 8개:
  kbthink.com(KB국민은행 공식, 세금가이드) x2 / insnews.co.kr(한국보험신문, 언론) /
  citibank.co.kr(한국씨티은행 공식) / happy-zone.co.kr(개인·소규모 콘텐츠) /
  suhyup-bank.com(수협은행 공식) / tpickshop.com(개인·소규모 콘텐츠) /
  lekkufinance.com(개인·소규모 콘텐츠). 후속 검색("한도 5천만원 가입기한
  2028년") 상위에는 standardchartered.co.kr(SC제일은행 공식) ·
  securities.miraeasset.com(미래에셋증권 공식) · kbsavings.com(KB저축은행 공식) ·
  incheonbank.com(인천저축은행 공식)도 추가로 나왔다.
  1) 진입 여지 — 있음. happy-zone.co.kr·tpickshop.com·lekkufinance.com 3곳이
     개인·소규모 콘텐츠로 상위권에 있다.
  2) 검색 의도 — "가입조건·한도"를 묻는 정보 탐색형이다. 조회·신청·계산기
     실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 아니다. 상위 결과 대부분이 은행 공식 상품 안내 위주라
     2026년 신설된 "기초연금 수급자" 가입 요건 변경을 구가입자·신가입자
     구분 없이 뭉뚱그려 쓰거나, 실제 절세 금액을 계산 예시로 보여주는 곳이
     드물다. 이 두 가지가 정보이득 포인트다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 계산 예시 — 한도 5천만원을 연 3.5% 금리 상품에 예치했다고 가정하면
      세전 이자는 175만원이다. 일반과세 상품이면 이자소득세 15.4%(269,500원)를
      떼지만, 비과세종합저축이면 세금 없이 175만원을 그대로 받는다. 상위
      결과 중 이 계산을 실제 숫자로 보여주는 곳은 찾지 못했다.
  (b) 비교표 — 2025년 12월 31일까지 가입한 경우와 2026년 1월 1일 이후
      가입한 경우, 고령자 가입 요건이 어떻게 달라지는지 표로 정리했다.
      "올해가 마지막 기회"라는 제목의 기사(브라보마이라이프)는 있었지만
      기존 가입자 혜택 유지 여부까지 표로 정리한 결과물은 상위에 없었다.
primary_source: |
  1차 시도: 국세청 "비과세되는 주요 금융소득" 페이지
  (https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=10602&cntntsId=7910)에
  WebFetch를 1회 시도 → EGRESS_BLOCKED(2026-09-24). RULES.md 「1차 출처가
  막혔을 때」 기준에 따라 2차 출처 교차검증으로 전환했다.
  기본 수치(저축원금 기준 전 금융기관 합산 5천만원 한도, 이자·배당소득세
  15.4% 전액 비과세)는 kbthink.com(KB국민은행)·citibank.co.kr(한국씨티은행)·
  standardchartered.co.kr(SC제일은행)·suhyup-bank.com(수협은행)·
  securities.miraeasset.com(미래에셋증권)·kbsavings.com(KB저축은행)·
  incheonbank.com(인천저축은행) 등 7곳 이상 제도권 금융기관 공식 페이지에서
  충돌 없이 일치했다.
  2026년 신설 가입 요건(만 65세 이상이면서 「기초연금법」상 기초연금
  수급대상자로 한정, 2026-01-01 이후 가입분부터 적용)은 브라보마이라이프
  (bravo.etoday.co.kr, 이투데이 계열 언론사) · 한국보험신문(insnews.co.kr) ·
  일간NTN(intn.co.kr, "2025 핵심 개정 세법 총정리 - 국회 본회의 의결
  2025.12.2.") 세 개 독립 언론사와, 공무원연금공단(POBA, 준정부기관)의
  가입요건 변경 안내 공지(poba.or.kr)까지 네 곳에서 시행일·요건이 충돌
  없이 일치했다. 근거 법령(조세특례제한법 제88조의2)의 국가법령정보센터
  조문 링크(law.go.kr)도 확인했으나, RULES.md 지침에 따라 law.go.kr은
  자동화 세션에서 WebFetch를 시도하지 않았다(렌더링해도 본문 없음이 기존
  확인 사항).
  종합: 독립 출처 4곳 이상(언론 3 + 준정부기관 1)이 핵심 수치(시행일·
  가입요건·기존가입자 보호조항)에서 충돌 없이 일치했고, 법 개정이라는
  검증 가능한 사실관계이므로 RULES.md의 교차검증 진행 기준을 충족한다고
  판단해 gate4를 충족으로 처리한다. 원문 직접 대조는 사람이 law.go.kr에서
  한 번 더 확인하면 더 확실하다.
기준일: 2026-09-24 (WebSearch 교차검증일 기준. 법 시행일은 2026-01-01)
tags: 비과세종합저축, 이자소득세, 비과세한도, 고령자저축, 기초연금, 절세상품, 조세특례제한법, 주식초보, 저축세금
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 4,610회(제도 기준 100 이상, 같은
  배치에서 함께 확인한 해외주식 상속세(20)·계좌이동제도(20)·배당소득세
  환급 방법(20)·주식 매매명세서 발급(20)·청약증거금대출(20)·배당소득세
  원천징수영수증(20)·주식 양도소득세 필요경비(20)는 전부 FAIL).
  게이트2 충족 — v3 기준 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 계산 예시(비과세 시 세후 이자 175만원 vs 일반과세 시
  1,480,500원)와 2025년/2026년 가입요건 비교표 확보.
  게이트4 충족 — 1차 출처 WebFetch는 EGRESS_BLOCKED로 막혔으나, 독립
  출처 4곳 이상(언론 3 + 준정부기관 1, 제도권 금융기관 7곳 추가)이 핵심
  수치에서 충돌 없이 일치해 RULES.md의 교차검증 진행 기준을 충족했다.
capture_guide: ""
self_check: |
  [2026-09-24 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — 기존 78편 중 "비과세종합저축"을 다룬 편 없음
  (grep 0건). 6편(금융소득 종합과세)·4편(배당소득세)은 일반 금융소득
  과세를 다루지만 비과세종합저축이라는 특정 저축상품 특례는 언급하지
  않아(grep 0건) 겹치지 않는다.
  기관 링크 점검 — 본문에서 국세청·국가법령정보센터로 안내하는 문장과
  하단 참고 출처 전부 target="_blank" rel="noopener"로 링크 처리했다.
  정부 기관 링크는 nofollow 미부착.
  제목 "비과세종합저축 조건과 한도 2026" 19자·금지어 없음·조사/접속사
  없음(제도 패턴 "{제도명} 조건과 한도"에 연도만 추가). 슬러그 영문
  소문자+하이픈 5단어(tax-exempt-savings-limit-2026).
  인트로 문단 최상단 배치, "안녕하세요" 없음. 비교표 1개 thead/tbody
  시맨틱.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서
  "—" 0개 확인. "다만"은 본문에서 0회(전환은 "단,"·"그런데"·"반면"·
  "그런데도"로 분산). `<mark>` 총 3개(3~5개 기준 충족). FAQ 5개(6개
  고정 탈피). 핵심요약 박스 제목을 "🗂 먼저 짚고 갈 것"으로, 색상은
  버건디 계열(#fdf1f1/#a4243b)로 최근 게시물(테라코타 #c2540e·틸
  #0f9b8e·슬레이트블루 #3949ab)과 겹치지 않게 골랐다. 목차 제외 본문
  H2 5개 중 서술형 3개("가입할 수 있는 사람과 저축 한도", "2026년
  가입자부터 달라지는 조건", "가입 전 놓치기 쉬운 점"), 질문형
  2개("비과세종합저축이란 무엇인가요", "비과세 혜택, 얼마나 차이
  날까요")로 "~나요" 편중 없음(5개 중 2개, 40%). FAQ 헤딩도 "자주 묻는
  질문" 대신 "많이 묻는 질문들"로 변형.
  헤지 표현 남발 없음 — 확정된 수치는 단정해서 쓰고, 교차검증으로
  확인했다는 사실만 출처 문단에 한 번 명시했다. 면책 문구는 기존
  게시물과 다른 표현으로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-24</p>

<p>비과세종합저축은 <mark>일정 자격을 갖춘 사람이 원금 5천만원까지 저축하면 이자·배당소득세를 한 푼도 내지 않는 제도</mark>입니다. 2026년 1월 1일부터 가입 대상 조건이 좁아졌기 때문에, 기존에 알고 있던 조건만 믿고 있으면 정작 가입이 안 되는 경우가 생길 수 있습니다. 이 글에서는 달라진 조건과 한도, 실제 절세 금액을 계산 예시로 정리합니다.</p>

<div style="background:#fdf1f1;border:2px solid #a4243b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a1a2b;font-size:18px;">🗂 먼저 짚고 갈 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>저축 원금 기준 전 금융기관 합산 1인당 5천만원까지 이자·배당소득세가 전액 면제됩니다.</li>
    <li>2026년 1월 1일 이후 신규 가입분부터는 고령자 가입 조건이 "만 65세 이상"에서 "만 65세 이상이면서 기초연금 수급 대상자"로 좁아졌습니다.</li>
    <li>2025년 안에 가입하면 기존 조건으로 가입할 수 있고, 이미 가입한 상품은 만기까지 혜택이 그대로 유지됩니다.</li>
    <li>장애인, 국가유공자 등 고령자 외 가입 대상 요건에는 변화가 없습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>비과세종합저축이란 무엇인가요</li>
  <li>가입할 수 있는 사람과 저축 한도</li>
  <li>2026년 가입자부터 달라지는 조건</li>
  <li>비과세 혜택, 얼마나 차이 날까요</li>
  <li>가입 전 놓치기 쉬운 점</li>
  <li>많이 묻는 질문들</li>
</ol>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">비과세종합저축이란 무엇인가요</h2>

<p>조세특례제한법 제88조의2에 근거한 저축 상품으로, 은행·증권사 등에서 정한 요건을 갖춘 사람이 가입하면 그 저축에서 나오는 이자소득과 배당소득에 소득세를 매기지 않습니다.</p>

<p>일반 예금이나 펀드는 이자·배당소득에 15.4%(소득세 14% + 지방소득세 1.4%)를 원천징수하지만, 비과세종합저축은 이 세금이 통째로 빠집니다. 예금, 적금, 펀드, 채권 등 대부분의 금융상품에 이 특례를 적용할 수 있습니다.</p>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">가입할 수 있는 사람과 저축 한도</h2>

<p><mark>저축 원금 기준으로 전 금융기관을 합산해 1인당 5천만원까지</mark> 비과세 혜택을 받을 수 있습니다. 한 은행에서 5천만원을 채웠다면 다른 은행에서는 추가로 가입할 수 없습니다.</p>

<ul style="line-height:1.9;">
  <li>만 65세 이상 고령자(2026년부터 조건 변경, 아래 항목 참조)</li>
  <li>장애인복지법상 장애인</li>
  <li>독립유공자와 그 유족·가족</li>
  <li>국가유공자 중 상이자</li>
  <li>기초생활수급자</li>
  <li>5·18민주화운동 부상자</li>
  <li>고엽제후유의증 환자</li>
  <li>특수임무유공자와 그 유족·가족</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>용어 정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>저축원금</b>: 이자·배당을 뺀, 실제로 넣은 원금만 계산한 금액.</li>
    <li><b>기초연금</b>: 만 65세 이상 중 소득·재산이 적은 하위 약 70%에게 지급되는 국가 연금.</li>
    <li><b>원천징수</b>: 금융기관이 이자를 지급할 때 세금을 미리 떼고 나머지만 주는 방식.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">2026년 가입자부터 달라지는 조건</h2>

<p>2025년 세제개편안에 이 제도의 개정 내용이 담겼고, 2025년 12월 2일 국회 본회의에서 의결됐습니다. 핵심은 고령자 가입 조건이 좁아졌다는 점입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">2025년 12월 31일까지 가입</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">2026년 1월 1일 이후 가입</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">고령자 가입 조건</td>
      <td style="border:1px solid #ddd;padding:8px;">만 65세 이상 거주자면 소득과 무관하게 가입 가능</td>
      <td style="border:1px solid #ddd;padding:8px;">만 65세 이상이면서 기초연금 수급 대상자만 가입 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">장애인·국가유공자 등</td>
      <td style="border:1px solid #ddd;padding:8px;">동일</td>
      <td style="border:1px solid #ddd;padding:8px;">변경 없음</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">저축 한도</td>
      <td style="border:1px solid #ddd;padding:8px;">전 금융기관 합산 5천만원</td>
      <td style="border:1px solid #ddd;padding:8px;">동일</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기존 가입자</td>
      <td style="border:1px solid #ddd;padding:8px;">해당 없음</td>
      <td style="border:1px solid #ddd;padding:8px;">만기까지 기존 조건의 비과세 혜택 유지</td>
    </tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;margin-top:6px;">소득과 재산이 적은 고령층에게 세제 혜택을 집중하려는 취지의 개편이라고 언론에 보도됐습니다. 조문 원문은 <a href="https://www.law.go.kr/lsLawLinkInfo.do?chrClsCd=010202&amp;lsJoLnkSeq=1017631657" target="_blank" rel="noopener">국가법령정보센터 조세특례제한법 제88조의2</a>에서 확인할 수 있습니다.</p>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">비과세 혜택, 얼마나 차이 날까요</h2>

<p>한도인 5천만원을 연 3.5% 금리 상품에 1년 동안 예치했다고 가정해봅니다. 세전 이자는 5천만원 × 3.5% = 175만원입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">일반과세 상품</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">비과세종합저축</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">세전 이자</td>
      <td style="border:1px solid #ddd;padding:8px;">1,750,000원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,750,000원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">이자소득세(15.4%)</td>
      <td style="border:1px solid #ddd;padding:8px;">269,500원</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>0원</mark></td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">세후 실수령 이자</td>
      <td style="border:1px solid #ddd;padding:8px;">1,480,500원</td>
      <td style="border:1px solid #ddd;padding:8px;">1,750,000원</td>
    </tr>
  </tbody>
</table>

<p>같은 상품, 같은 금리라도 비과세종합저축으로 가입하면 269,500원을 더 받습니다. 금리가 높거나 한도를 꽉 채울수록 절세 금액은 더 커집니다.</p>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">가입 전 놓치기 쉬운 점</h2>

<p>한도는 개별 상품이 아니라 사람 기준입니다. 여러 은행에 나눠 가입해도 저축원금 합계가 5천만원을 넘으면 초과분은 비과세 혜택을 받지 못합니다.</p>

<ul style="line-height:1.9;">
  <li>가입 전 다른 금융기관에서 이미 가입한 비과세종합저축 잔액이 있는지 먼저 확인해야 합니다.</li>
  <li>만 65세 이상으로 가입하려면 본인이 기초연금 수급 대상자인지부터 확인이 필요합니다.</li>
  <li>이 제도 자체의 가입 기한은 2028년 12월 31일까지이지만, 고령자 가입 조건은 이미 2026년 1월 1일부터 바뀌었으므로 두 날짜를 혼동하지 않아야 합니다.</li>
</ul>

<p>본인이 가입 대상에 해당하는지 정확히 확인하려면 <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=10602&amp;cntntsId=7910" target="_blank" rel="noopener">국세청 비과세 금융소득 안내</a> 페이지나 가입하려는 은행·증권사 창구에서 직접 확인하는 편이 정확합니다.</p>

<h2 style="border-left:6px solid #a4243b;padding-left:12px;margin-top:36px;">많이 묻는 질문들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비과세종합저축은 아무나 가입할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 만 65세 이상(2026년부터는 기초연금 수급 대상자로 한정), 장애인, 국가유공자, 기초생활수급자 등 법으로 정한 대상만 가입할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">이미 가입한 사람은 2026년부터 혜택이 사라지나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 법 개정 전에 가입한 상품은 만기까지 기존 조건의 비과세 혜택이 그대로 유지됩니다. 새로 바뀐 조건은 2026년 1월 1일 이후 신규 가입자에게만 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">한도 5천만원은 상품 하나당 기준인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 사람 기준입니다. 전 금융기관에 가입한 비과세종합저축 저축원금을 모두 합쳐서 5천만원까지만 비과세 혜택을 받을 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">기초연금 수급 대상자인지는 어떻게 확인하나요</summary>
  <p style="margin:10px 0 0 0;">소득과 재산을 합산한 소득인정액이 일정 기준 이하인 만 65세 이상 고령자 중 약 70%가 기초연금을 받습니다. 본인의 수급 여부는 가까운 주민센터나 국민연금공단에 문의해 확인할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">적금이나 펀드로도 가입할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">네, 예금·적금뿐 아니라 펀드·채권 등 대부분의 금융상품을 비과세종합저축 형태로 가입할 수 있습니다. 취급 여부는 가입하려는 금융기관에 따라 다를 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr/lsLawLinkInfo.do?chrClsCd=010202&amp;lsJoLnkSeq=1017631657" target="_blank" rel="noopener">국가법령정보센터 - 조세특례제한법 제88조의2(비과세종합저축)</a></li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=10602&amp;cntntsId=7910" target="_blank" rel="noopener">국세청 - 비과세되는 주요 금융소득</a></li>
    <li>기준일: 2026-09-24(WebSearch 교차검증일). 가입 요건 변경 시행일은 2026-01-01.</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 비과세종합저축이라는 제도를 소개하는 정보 글로, 특정 금융상품 가입을 권하지 않습니다. 가입 대상·한도·세율은 법 개정이나 금융기관 정책에 따라 달라질 수 있으므로 가입 전 국세청이나 해당 금융기관의 최신 공지를 직접 확인하시기 바랍니다. 저축·투자 결정과 그 결과에 대한 책임은 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "비과세종합저축 조건과 한도 2026",
  "description": "비과세종합저축의 가입 대상과 5천만원 한도, 2026년부터 달라지는 고령자 가입 조건, 이자소득세 비과세 계산 예시를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-24",
  "dateModified": "2026-09-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/tax-exempt-savings-limit-2026"
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
      "name": "비과세종합저축은 아무나 가입할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 만 65세 이상(2026년부터는 기초연금 수급 대상자로 한정), 장애인, 국가유공자, 기초생활수급자 등 법으로 정한 대상만 가입할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "이미 가입한 사람은 2026년부터 혜택이 사라지나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 법 개정 전에 가입한 상품은 만기까지 기존 조건의 비과세 혜택이 그대로 유지됩니다. 새로 바뀐 조건은 2026년 1월 1일 이후 신규 가입자에게만 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "한도 5천만원은 상품 하나당 기준인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 사람 기준입니다. 전 금융기관에 가입한 비과세종합저축 저축원금을 모두 합쳐서 5천만원까지만 비과세 혜택을 받을 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "기초연금 수급 대상자인지는 어떻게 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "소득과 재산을 합산한 소득인정액이 일정 기준 이하인 만 65세 이상 고령자 중 약 70%가 기초연금을 받습니다. 본인의 수급 여부는 가까운 주민센터나 국민연금공단에 문의해 확인할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "적금이나 펀드로도 가입할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네, 예금·적금뿐 아니라 펀드·채권 등 대부분의 금융상품을 비과세종합저축 형태로 가입할 수 있습니다. 취급 여부는 가입하려는 금융기관에 따라 다를 수 있습니다." }
    }
  ]
}
</script>
