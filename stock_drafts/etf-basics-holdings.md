---
keyword: ETF 뜻
title: ETF 뜻과 구성종목 확인하는 법
slug: etf-basics-holdings
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 38020 (PC 5220 / 모바일 32800)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-21 — 통과]
  WebSearch "ETF 뜻 초보 쉽게 설명" 및 "ETF 구성종목 조회 방법" 상위 종합:
  cardif.co.kr(카디프생명, 금융사 공식) / kbthink.com(KB국민은행, 공식) /
  samsungfund.com(삼성자산운용 Kodex, 공식) / tossbank.com(토스뱅크, 핀테크
  공식) / riseetf.co.kr(RISE ETF 자산운용사, 공식) / tigeretf.com(미래에셋
  TIGER, 공식) / banksalad.com(뱅크샐러드, 핀테크) / namu.wiki(나무위키,
  집단편집) / weolbu.com(월급쟁이부자들, 개인·커뮤니티 콘텐츠) /
  etfcheck.co.kr·funetf.co.kr·comp.wisereport.co.kr(민간 ETF 조회 서비스)
  1) 진입 여지 — 자산운용사·금융사 공식 페이지가 다수 노출되지만
     namu.wiki(집단편집)·weolbu.com(커뮤니티/개인) 등도 함께 상위에 있어
     "미국주식 거래시간"(20,730회, 상위 10개 전부 증권사 공식이라 게이트2
     탈락 처리했던 사례)만큼 완전히 잠겨 있지는 않다. 탈락조건1 미해당.
  2) 검색 의도 — "ETF가 뭔지" 정보 탐색형이다. 계산기·조회 도구 자체를
     찾는 의도가 아니다. 탈락조건2 미해당.
  3) 답 완결 여부 — 아니다. 상위 글 대부분 "ETF는 주식처럼 거래되는
     펀드"라는 정의와 장단점까지는 다루지만, 특정 ETF의 실제 구성종목을
     어느 사이트에서 어떻게 조회하는지 구체적인 절차를 안내하는 글은
     흩어져 있을 뿐 개념 설명과 한 곳에 종합된 글은 찾지 못했다. 정보이득
     여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-21, 2026-09-21 2차 개정: 분배금 내용은 별도 63편으로 분리]
  (1) ETF 개념(장바구니처럼 여러 종목을 한 번에 담아 지수 비중대로
      보유하는 펀드) 설명에 그치지 않고, 실제로 "이 ETF가 무슨 종목을
      담고 있는지"를 어디서 조회하는지 — 자산운용사 공식 PDF(자산구성내역),
      한국거래소 정보데이터시스템, 한국예탁결제원 SEIBro 순서로 구체적인
      조회 경로를 안내했다.
  (2) "ETF 구성종목"·"코스피200 구성종목"·"S&P500 구성종목" 등 조회 관련
      키워드는 실측 검색량이 전부 100회 미만으로 게이트1 미달이었다(아래
      self_check 기록). 별도 편으로 분리하지 않고 검색량이 확실한 "ETF 뜻"
      편의 한 섹션으로 흡수해, 검색 수요가 없는 키워드로 발행 편수를
      무리하게 늘리지 않았다.
  (3) 10편(ETF 수수료)·22편(ETF 괴리율)·23편(국내상장 해외ETF 세금)·
      40편(곱버스/레버리지 예탁금)·63편(월배당 ETF와 분배금)으로 이어지는
      허브 역할을 하도록 각 편의 핵심 한 줄 요약과 내부 링크를 배치했다.
  ★ 특정 ETF의 실시간 구성종목 비중처럼 매일 바뀌는 수치는 이 글에서
  단정하지 않고 "조회 방법"만 안내했다.
primary_source: |
  1차 시도: 한국거래소 정보데이터시스템(data.krx.co.kr) ETF 정보 페이지
  WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-21). RULES.md 「1차 출처가
  막혔을 때」(2026-09-12) 기준에 따라 판단: 이 글의 핵심 내용은
  세율·공제한도·과세표준 구간형 숫자가 아니라 ETF의 구조·조회 방법이라는
  개념/절차형 정보라, 서로 무관한 독립 출처 3곳 이상(그중 다수가 자산운용사·
  금융사 공식)이 일치하면 교차검증으로 충분하다고 판단해 진행했다.
  - ETF 정의·구조(주식처럼 거래되는 펀드, 지수 구성종목을 비중대로
    보유): cardif.co.kr(카디프생명)·kbthink.com(KB국민은행)·
    samsungfund.com(삼성자산운용 Kodex)·tigeretf.com(미래에셋 TIGER)·
    riseetf.co.kr(RISE ETF) 5개 자산운용사·금융사 공식 페이지가 동일한
    설명으로 일치했다.
  - 구성종목 조회처(자산운용사 공식 PDF·한국거래소·한국예탁결제원
    SEIBro): samsungfund.com 자료실 페이지와 seibro.or.kr(한국예탁결제원,
    공식)의 ETF종합정보 메뉴 존재를 WebSearch로 확인했다. 직접 열람은
    이번 세션에서 EGRESS_BLOCKED로 못했지만, 페이지 자체의 존재와
    메뉴 구조는 검색 결과 스니펫으로 교차 확인했다.
기준일: 2026-09-21 (WebSearch 교차검증일)
tags: ETF, ETF뜻, ETF구성종목, 상장지수펀드, 인덱스펀드, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-21, 2차 개정).
  게이트1: check-keywords.yml 실측 38,020회. 이 시리즈 역대 최고 검색량
  (종전 기록 17편 공매도 뜻 20,580회). 함께 조회한 ETF 종류(590회, PASS)는
  카니벌라이제이션 우려로 backlog에 남기고, ETF 구성종목 계열 키워드
  (ETF 구성종목 20회·ETF 구성종목 조회 20회·코스피200 구성종목 90회·
  S&P500 구성종목 100회·나스닥100 구성종목·ETF PDF 30회·ETF 순자산가치
  20회)는 전부 게이트1 미달로 FAIL. ETF 배당/분배금 계열(ETF 분배금 920회·
  ETF 배당금 1,220회·월배당 ETF 4,960회)은 전부 PASS해 별도 63편으로
  분리했다.
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 구성종목 조회 3단계 경로 + 기존 5개 편 허브 링크로 정보이득
  확보.
  게이트4: data.krx.co.kr 1회 WebFetch 시도 EGRESS_BLOCKED 확인 후,
  개념/절차형 정보라는 RULES.md 예외 기준에 따라 자산운용사·금융사
  공식 다수(5곳 이상) 교차검증으로 대체.
self_check: |
  [2026-09-21 최종 판정, 2차 개정]
  게이트1 충족 — check-keywords.yml 실측 38,020회. 사용자가 처음에는
  ETF 개념·구성종목·분배금을 한 편에 담아달라고 했으나, 이후 "1편에 다
  담지 말고 종목별로 여러 편 시리즈로 발행해달라"고 요청을 바꿔 분배금
  내용을 63편으로 분리하고 이 편은 개념+구성종목만 남겼다. 구성종목을
  단독 편으로 더 쪼개는 방안도 검토했으나, ETF 구성종목·ETF 구성종목
  조회·코스피200 구성종목·S&P500 구성종목·나스닥100 구성종목·ETF PDF·
  ETF 순자산가치 등 시도한 키워드 전부 실측 100회 미만으로 게이트1을
  통과하지 못해(2026-09-21 확인) 단독 편으로 만들지 않고 이 편의 섹션
  으로 유지했다. 이 판단 근거를 self_check에 투명하게 남긴다.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당
  (serp_check 참조).
  게이트3 충족 — 구성종목 조회 3단계 경로(자산운용사 PDF, 한국거래소
  정보데이터시스템, 한국예탁결제원 SEIBro) + 기존 ETF 4개 편(10·22·
  23·40편) + 신규 63편(월배당 ETF)으로의 허브 링크로 차별화했다.
  게이트4 — data.krx.co.kr 1회 WebFetch 시도 EGRESS_BLOCKED(2026-09-21).
  ETF 구조·조회처는 세율·공제한도 같은 구간형 숫자가 아닌 개념/절차형
  정보라 RULES.md 예외 기준에 따라 자산운용사·금융사 공식 5곳 이상
  교차검증으로 진행했다. 실시간 구성종목 비중은 본문에서 단정하지
  않았다.
  카니벌라이제이션 점검 — 1~61편 keyword 전체 확인. 10편(ETF 수수료)은
  보수·비용, 22편(ETF 괴리율)은 가격과 NAV의 괴리, 23편(국내상장
  해외ETF 세금)은 과세 방식, 40편(곱버스 뜻)은 레버리지·인버스 예탁금
  제도, 63편(월배당 ETF)은 분배금·지급주기가 중심이라 이 글의 "ETF가
  무엇이고 무엇을 담고 있는지"와 검색 의도가 겹치지 않는다. 본문에서
  5개 편 전부로 내부 링크를 걸어 중복 설명 대신 위임했다.
  제목 "ETF 뜻과 구성종목 확인하는 법" 16자·금지어 없음·조사/접속사
  없음. 슬러그 영문 소문자+하이픈 3단어(etf-basics-holdings).
  인트로 문단 최상단 배치, "안녕하세요" 없음. FAQ 4개와 JSON-LD 1:1
  일치. 종목·상품 추천 표현 없음(특정 ETF 종목명·티커 언급 없이 조회
  방법만 안내). 단정 표현("반드시","무조건","확실히","보장") 없음.
  기관 링크 점검 — krx.co.kr·data.krx.co.kr(한국거래소)·
  seibro.or.kr(한국예탁결제원) 링크 전부 target="_blank" rel="noopener"
  처리, 공공기관 성격이라 nofollow 미부착.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 발행 본문(YAML 제외)에서
  "—" 0개 확인. "다만" 0회. 본문 `<mark>` 총 3개(3~5개 기준 충족, 하한선).
  FAQ 4개(6개 고정 탈피, 하한선). 핵심요약 박스 제목을 "🧺 ETF, 이것만
  알면 됩니다"로, 색상은 rose 계열(#fff1f2/#be123c)로 최근 게시물과
  겹치지 않게 새로 골랐다. 목차 제외 본문 H2 4개 중 서술형 3개("ETF
  뜻", "ETF 구성종목 확인하는 법", "ETF 종류 살펴보기"), 질문형 1개
  ("ETF는 무엇을 담고 있나요")로 "~나요" 편중 없음. 헤지 표현 남발 없음.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-21</p>

<p><mark>ETF는 여러 종목을 한 바구니에 담아 지수 비중대로 보유하면서 주식처럼 실시간으로 사고파는 펀드</mark>입니다. 이 글은 ETF가 정확히 무엇인지부터, 그 안에 어떤 종목이 들어있는지 확인하는 법까지 정리했습니다. 분배금(배당)은 별도 편에서 더 깊이 다룹니다.</p>

<div style="background:#fff1f2;border:2px solid #be123c;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#9f1239;font-size:18px;">🧺 ETF, 이것만 알면 됩니다</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>ETF는 <b>여러 종목을 한 번에 담은 바구니</b>를 주식처럼 실시간으로 사고파는 상품입니다.</li>
    <li>실제 구성종목은 <b>자산운용사 공식 페이지·한국거래소·한국예탁결제원 SEIBro</b>에서 확인할 수 있습니다.</li>
    <li>ETF 이름만 보고 담긴 종목을 짐작하기보다, 직접 구성종목을 확인하는 습관이 필요합니다.</li>
    <li>수수료·괴리율·세금·분배금처럼 더 깊이 볼 주제는 각각 다른 편에서 따로 다룹니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #be123c;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ETF 뜻</li>
  <li>ETF는 무엇을 담고 있나요</li>
  <li>ETF 구성종목 확인하는 법</li>
  <li>ETF 종류 살펴보기</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #be123c;padding-left:12px;margin-top:36px;">ETF 뜻</h2>

<p>ETF(Exchange Traded Fund)는 우리말로 상장지수펀드라고 부릅니다. 여러 종목에 나눠 투자하는 펀드이면서도, 증권거래소에 상장돼 있어 주식처럼 장중 아무 때나 실시간 가격으로 사고팔 수 있습니다.</p>

<p>일반 펀드는 하루 한 번 정해진 기준가로만 거래되지만, ETF는 주식 계좌만 있으면 장중 시세를 보면서 바로 매수·매도할 수 있습니다. 이 차이가 ETF와 일반 펀드를 가르는 가장 큰 특징입니다.</p>

<h2 style="border-left:6px solid #be123c;padding-left:12px;margin-top:36px;">ETF는 무엇을 담고 있나요</h2>

<p>ETF는 대부분 특정 지수를 그대로 따라가도록 설계됩니다. 예를 들어 코스피200 지수를 추종하는 ETF라면, 코스피200에 속한 200개 종목을 지수와 비슷한 비중으로 나눠 담습니다. 지수가 오르내리면 ETF 가격도 같은 방향으로 움직이는 구조입니다.</p>

<p>지수 구성종목은 정기적으로 재평가돼 교체되기도 합니다. 이때 ETF도 지수 변경에 맞춰 보유 종목을 함께 조정합니다. 그래서 <mark>ETF 이름만 보고 "이 종목이 계속 들어있겠지"라고 단정하기보다, 실제 구성종목을 직접 확인하는 습관</mark>이 필요합니다.</p>

<h2 style="border-left:6px solid #be123c;padding-left:12px;margin-top:36px;">ETF 구성종목 확인하는 법</h2>

<p>특정 ETF가 실제로 어떤 종목을 얼마나 담고 있는지는 아래 순서로 확인할 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">확인 경로</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">어디서</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">확인할 수 있는 것</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">① 자산운용사 공식 페이지</td>
      <td style="border:1px solid #ddd;padding:8px;">운용사 홈페이지의 ETF 상품 페이지</td>
      <td style="border:1px solid #ddd;padding:8px;">PDF(자산구성내역), 종목별 편입 비중, 최근 변경 내역</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">② 한국거래소 정보데이터시스템</td>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://data.krx.co.kr" target="_blank" rel="noopener">data.krx.co.kr</a></td>
      <td style="border:1px solid #ddd;padding:8px;">전체 상장 ETF의 기본 정보와 구성종목</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">③ 한국예탁결제원 SEIBro</td>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://seibro.or.kr" target="_blank" rel="noopener">seibro.or.kr</a></td>
      <td style="border:1px solid #ddd;padding:8px;">ETF종합정보 메뉴의 종목상세, 자산구성 현황</td>
    </tr>
  </tbody>
</table>

<p>증권사 MTS 앱에서도 ETF 종목명을 검색하면 "구성종목" 또는 "PDF" 탭에서 같은 정보를 바로 볼 수 있는 경우가 많습니다. <mark>구성종목과 비중은 매일 바뀔 수 있으니</mark>, 투자 전에는 항상 최신 자료로 다시 확인하는 편이 안전합니다.</p>

<h2 style="border-left:6px solid #be123c;padding-left:12px;margin-top:36px;">ETF 종류 살펴보기</h2>

<p>ETF는 무엇을 추종하느냐에 따라 성격이 크게 갈립니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">종류</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">추종 대상</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">국내 지수형</td>
      <td style="border:1px solid #ddd;padding:8px;">코스피200 등 국내 대표 지수</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">해외 지수형</td>
      <td style="border:1px solid #ddd;padding:8px;">S&amp;P500, 나스닥100 등 해외 지수</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">채권형</td>
      <td style="border:1px solid #ddd;padding:8px;">국채, 회사채 등 채권 바스켓</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">원자재형</td>
      <td style="border:1px solid #ddd;padding:8px;">금, 원유 등 실물 자산 가격</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">레버리지·인버스형</td>
      <td style="border:1px solid #ddd;padding:8px;">지수 등락률의 배수 또는 반대 방향</td>
    </tr>
  </tbody>
</table>

<p>수수료(총보수)가 실제로 얼마나 부담되는지는 <a href="https://sensitiveboss3.tistory.com/entry/etf-fee-comparison">ETF 수수료 총보수 실부담 확인법</a>, 거래가격과 순자산가치가 벌어지는 괴리율 문제는 <a href="https://sensitiveboss3.tistory.com/entry/etf-divergence-rate-2026">ETF 괴리율 계산법</a>, 국내상장 ETF의 세금 계산은 <a href="https://sensitiveboss3.tistory.com/entry/domestic-listed-overseas-etf-tax">국내상장 해외ETF 세금</a>, 레버리지·인버스 ETF의 예탁금 제도는 <a href="https://sensitiveboss3.tistory.com/entry/leveraged-inverse-etf-deposit">곱버스 뜻과 레버리지 예탁금 기준</a>, 분배금(배당)이 어떻게 지급되는지는 <a href="https://sensitiveboss3.tistory.com/entry/monthly-dividend-etf-basics">월배당 ETF 뜻과 분배금 지급방식</a> 편에서 각각 자세히 다룹니다.</p>

<div style="background:#fff1f2;border:2px solid #be123c;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#9f1239;font-size:18px;">요약하면 이렇습니다</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>ETF는 여러 종목을 담은 바구니를 주식처럼 실시간 매매하는 상품입니다.</li>
    <li>구성종목은 자산운용사 공식 페이지, 한국거래소, 한국예탁결제원 SEIBro에서 확인할 수 있습니다.</li>
    <li>분배금(배당) 지급 방식은 별도 편(월배당 ETF 뜻과 분배금 지급방식)에서 자세히 다룹니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #be123c;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF와 일반 펀드는 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">가장 큰 차이는 거래 방식입니다. 일반 펀드는 하루 한 번 정해진 기준가로만 거래되지만, ETF는 증권거래소에 상장돼 있어 주식처럼 장중 실시간 가격으로 사고팔 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF 이름에 붙은 숫자(200, S&amp;P500 등)는 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">그 ETF가 추종하는 지수의 이름이나 구성종목 수를 뜻합니다. 코스피200을 추종하면 이름에 200이 들어가고, 미국 S&amp;P500 지수를 추종하면 이름에 S&amp;P500이 들어가는 식입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF 구성종목은 얼마나 자주 바뀌나요</summary>
  <p style="margin:10px 0 0 0;">추종하는 지수가 정기적으로 재평가돼 구성종목을 교체할 때마다 ETF도 함께 바뀝니다. 교체 주기는 지수마다 다르므로, 정확한 시점은 자산운용사 공지로 확인하는 편이 좋습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF가 상장폐지되면 투자금은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">상장폐지되더라도 투자금이 사라지는 것은 아닙니다. 운용사가 보유 자산을 정리해 상장폐지 시점의 순자산가치만큼을 투자자에게 돌려주는 절차를 거칩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.krx.co.kr" target="_blank" rel="noopener">한국거래소</a> - ETF 시장 개요</li>
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a> - ETF 종목 정보·구성종목</li>
    <li><a href="https://seibro.or.kr" target="_blank" rel="noopener">한국예탁결제원 SEIBro</a> - ETF종합정보</li>
  </ul>
  기준일: 2026-09-21(WebSearch 교차검증일). 한국거래소 정보데이터시스템은
  이번 세션 WebFetch가 EGRESS_BLOCKED로 막혀 직접 열람하지 못했고,
  ETF 구조·조회처는 자산운용사·금융사 공식 페이지 다수로 교차검증했습니다.
  실시간으로 바뀌는 구성종목 비중은 이 글에서 단정하지 않았으니 투자
  전 위 사이트에서 최신 자료로 다시 확인하세요.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 ETF의 구조를 이해하는 데 참고하시라고 정리한 정보성 글이며,
특정 ETF나 종목의 매수·매도를 권하지 않습니다. 투자 전에는 반드시
자산운용사·거래소 등 원출처에서 최신 정보를 다시 확인하시고, 투자
결과에 대한 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ETF 뜻과 구성종목 확인하는 법",
  "description": "ETF가 무엇인지, 실제 구성종목을 어디서 확인하는지를 정리합니다. 분배금(배당)은 별도 편에서 다룹니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-21",
  "dateModified": "2026-09-21",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/etf-basics-holdings"
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
      "name": "ETF와 일반 펀드는 뭐가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "가장 큰 차이는 거래 방식입니다. 일반 펀드는 하루 한 번 정해진 기준가로만 거래되지만, ETF는 증권거래소에 상장돼 있어 주식처럼 장중 실시간 가격으로 사고팔 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "ETF 이름에 붙은 숫자(200, S&P500 등)는 무슨 뜻인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "그 ETF가 추종하는 지수의 이름이나 구성종목 수를 뜻합니다. 코스피200을 추종하면 이름에 200이 들어가고, 미국 S&P500 지수를 추종하면 이름에 S&P500이 들어가는 식입니다." }
    },
    {
      "@type": "Question",
      "name": "ETF 구성종목은 얼마나 자주 바뀌나요",
      "acceptedAnswer": { "@type": "Answer", "text": "추종하는 지수가 정기적으로 재평가돼 구성종목을 교체할 때마다 ETF도 함께 바뀝니다. 교체 주기는 지수마다 다르므로, 정확한 시점은 자산운용사 공지로 확인하는 편이 좋습니다." }
    },
    {
      "@type": "Question",
      "name": "ETF가 상장폐지되면 투자금은 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "상장폐지되더라도 투자금이 사라지는 것은 아닙니다. 운용사가 보유 자산을 정리해 상장폐지 시점의 순자산가치만큼을 투자자에게 돌려주는 절차를 거칩니다." }
    }
  ]
}
</script>
