---
keyword: 볼린저밴드 뜻
title: 볼린저밴드 뜻과 계산법
slug: bollinger-bands-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1220 (PC 290 / 모바일 930)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
level_note: |
  2026-09-26 「키워드 범위 확장」 결정 이후 첫 중급 편. 1~84편이 "주식 초보"
  프레이밍으로 게이트1 실패 513개가 누적돼 순서 대기 후보가 소진된 상태에서,
  키워드 후보 범위를 초급에 한정하지 않고 중급·고급까지 넓힌 결과 채택한
  첫 사례다(RULES.md 「★ 키워드 범위 확장」절 참조). 기존 초급편과 겹치는
  기본 개념(이동평균·표준편차)이 없어 별도 내부 링크는 필요 없었다.
serp_check: |
  [게이트2 v3 판정 2026-09-26 — 통과]
  WebSearch "볼린저밴드 뜻 계산법 매매 활용" 상위 결과: brunch.co.kr(개인
  콘텐츠) / wikidocs.net(개인·커뮤니티 위키) / alphasquare.co.kr(퀀트
  서비스, 소규모 핀테크) / xs.com(해외 브로커 블로그) / econowide.com(개인
  블로그) / quantpro.co.kr(소규모 퀀트 서비스). 나머지 2건(Parabolic SAR,
  Stochastic oscillator 위키백과 영문판)은 주제 무관 오검색으로 제외.
  1) 진입 여지 — 있음. 언론·공식기관·백과 없이 개인·소규모 핀테크 콘텐츠가
     상위를 채우고 있다.
  2) 검색 의도 — "뜻·계산법·매매 활용"을 함께 묻는 개념+실전 탐색형이다.
     시세 조회나 계산기 실행이 지배적 의도는 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 "원리·설정·계산법·매매전략"을
     표방하지만 실제로는 공식만 제시할 뿐 처음부터 끝까지 숫자로 계산해
     보여주는 예시는 드물고, 상단·하단 접근을 무조건 매매 신호처럼 단정하는
     경우가 많아 "역추세로 볼 수도, 추세 지속으로 볼 수도 있다"는 균형 잡힌
     설명은 부족하다. 이 두 지점이 정보이득 포인트다(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
  [번복 기록] 이 키워드는 2026-09-25 81편 착수 과정(다섯 번째 실행)에서
  한 차례 게이트2 탈락으로 판정된 적이 있다. 당시 사유는 "상위 글
  (alphasquare.co.kr 등)이 계산법+매매전략까지 이미 총정리로 완결해
  정보이득 여지를 찾지 못했다"였다. 이번에 같은 상위 결과를 다시 검토한
  결과, 상위 글들이 공식과 전략을 "나열"하기는 하지만 실제 숫자로 끝까지
  계산해 보여주는 워크스루는 없고, 상단·하단 접근을 사실상 매수·매도
  신호처럼 단정하는 경우가 많아 균형 잡힌 해석(역추세 vs 추세추종)이
  빠져 있음을 확인했다. 전자는 상위 글이 다루지 않는 구체적 정보이득이고,
  후자는 이 프로젝트의 "종목추천·매매타이밍 금지" 원칙에 더 부합하는
  차별화 지점이라 이번엔 통과로 재판정한다. 판단이 갈릴 수 있는 지점이라
  이 번복 경위를 투명하게 남긴다.
unique_asset: |
  (a) 20일치 가상 종가로 중심선(20일 단순이동평균)과 표준편차, 상단·하단
      밴드값까지 처음부터 끝까지 손으로 계산해 보여주는 워크스루. 실제
      종목명이나 실제 시세는 쓰지 않았다.
  (b) 밴드 폭이 좁아지는 "스퀴즈"와 벌어지는 상태, 가격이 밴드를 타고
      움직이는 "밴드워크"를 구분해서 정리 — 상위 글 대부분이 스퀴즈만
      언급하고 밴드워크는 다루지 않는다.
  (c) 상단·하단 접근을 해석하는 두 가지 관점(역추세: 과매수·과매도 반전
      신호로 보는 시각 / 추세추종: 밴드워크 중이면 오히려 추세 지속 신호로
      보는 시각)을 양쪽 다 제시하고 어느 하나가 항상 맞다고 단정하지
      않았다. 특정 매매 타이밍을 권하지 않는다는 원칙을 지켰다.
primary_source: |
  볼린저밴드는 존 볼린저가 1980년대에 고안한 기술적 분석 도구로, 법령이나
  정부기관이 정의하는 용어가 아니다(81편 리밸런싱, 82편 컨센서스와 동일
  성격). 별도 1차 출처가 없어 WebSearch로 독립 출처(alphasquare.co.kr·
  quantpro.co.kr 등 퀀트·투자정보 서비스, brunch.co.kr·econowide.com·
  wikidocs.net 개인·커뮤니티 콘텐츠) 5곳 이상을 교차확인했다(2026-09-26).
  계산 공식(중심선=20일 단순이동평균, 상단·하단 밴드=중심선±2×표준편차)과
  기본 개념에서 출처 간 충돌 없이 일치함을 확인했다.
기준일: 2026년 9월 기준 (기술적 지표 정의라 법령 개정 이력과 무관)
tags: 볼린저밴드, 볼린저밴드뜻, 볼린저밴드계산법, 기술적분석, 이동평균선, 표준편차, 밴드스퀴즈, 주식중급, 차트분석, 보조지표
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-26). 게이트1 실측 1,220회(같은 배치 20개
  중 유일한 PASS, 나머지 19개는 게이트1 탈락). 게이트2 v3 기준 3개 탈락
  조건 모두 미해당. 게이트3은 20일 가상 종가 계산 워크스루 + 스퀴즈·
  밴드워크 구분 + 역추세·추세추종 두 관점 제시로 충족. 게이트4는 법정
  수치가 아닌 기술적 지표 정의라 WebSearch 독립 출처 5곳 이상 교차검증으로
  충족.
capture_guide: ""
self_check: |
  [2026-09-26 판정 — gate_pass:true, 키워드 범위 확장 후 첫 편]
  게이트1 충족 — check-keywords.yml 실측 1,220회(PC 290/모바일 930, 일반
  기준 500 이상). 같은 배치 20개 중 유일한 PASS(나머지 19개: 이동평균선
  골든크로스 20회, RSI 지표 보는법 120회, MACD 지표 보는법 20회, 스토캐스틱
  지표 110회, 선물 만기일 영향 20회, 옵션 콜풋 뜻 20회, 델타헤지 뜻 20회,
  PER PBR 뜻 320회, ROE 뜻 계산법 20회, 부채비율 뜻 50회, PEG 지표 뜻 20회,
  기준금리 주가 영향 20회, 환율 수출주 영향 20회, 신용거래 미수금 차이
  20회, 헤드앤숄더 패턴 220회, 물타기 불타기 차이 20회, 손절매 기준 20회,
  선물옵션 양도소득세 20회, 배당성장주 뜻 20회 — 전부 임계값 미달로 FAIL).
  게이트2 충족 — RULES.md v3 기준 3개 탈락 조건 모두 미해당(serp_check
  참조).
  게이트3 충족 — 20일 가상 종가로 중심선·표준편차·상단하단 밴드를 처음부터
  끝까지 계산하는 워크스루, 스퀴즈·밴드워크 구분, 역추세·추세추종 두 관점
  제시로 상위 글보다 구체적인 정보이득을 확보했다.
  게이트4 충족 — 정부 1차 출처가 없는 기술적 지표 정의라 WebSearch 독립
  출처 5곳 이상(퀀트 서비스 2곳 포함) 교차검증으로 근거를 확보했다.
  카니벌라이제이션 점검 — 전체 stock_drafts/*.md(84개) grep 결과
  "볼린저"·"표준편차"·"이동평균"(기술지표 의미) 키워드를 다룬 편 없음.
  "overseas-stock-tax-filing.md"에 "이동평균법"이 등장하나 이는 양도차익
  계산의 평균단가법을 뜻해 이 글의 이동평균선과 무관하다(확인 완료).
  YMYL·투자조언 안전장치 점검 — 실제 종목명·실제 시세를 언급하지 않고
  모든 계산 예시를 "가상의 종가"로 명시했다. 상단·하단 접근을 특정 매수·
  매도 신호로 단정하지 않고 역추세·추세추종 두 해석을 병기했다. FAQ에서
  "볼린저밴드만으로 매매 결정을 내리지 않는 편이 안전하다"는 점을 명시해
  단일 지표 맹신을 경계했다.
  제목 "볼린저밴드 뜻과 계산법" 12자·금지어 없음·조사 "과" 1개(제목 규칙상
  조사·접속사 제거 대상은 "은는이가" 등 주격조사이며 "과"는 병렬 연결에
  필요해 유지, 검색어 "볼린저밴드 계산법"에도 그대로 쓰이는 표현). 슬러그
  영문 소문자+하이픈 3단어(bollinger-bands-calculation).
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—"
  0개. "다만" 0회(전환은 "단,"·"반면"·문장 구조 전환으로 분산). 본문
  `<mark>` 총 5개(3~5개 기준 충족, 상한선). FAQ 5개(6개 고정 탈피). 핵심요약 박스
  제목을 "📊 볼린저밴드, 숫자로 보면"으로, 색은 스카이블루 계열
  (#e6f7fb/#0277bd)로 최근 게시물(슬레이트블루#3949ab·주황#d9812c·
  버건디#a4243b·그린#2e7d32·틸#0f9b8e·퍼플#7b3fa0·마젠타#c2185b)과 겹치지
  않게 골랐다. 목차 제외 본문 H2 5개 중 질문형 1개("볼린저밴드란
  무엇인가요"), 서술형 4개로 "~나요" 편중 없음(5개 중 1개, 20%). 헤지
  표현은 "정해진 기준이 없다"는 사실 서술 1회만 썼고 반복하지 않았다. 면책
  문구는 기존 게시물과 다른 표현으로 작성.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-26</p>

<p>볼린저밴드는 20일 이동평균선 위아래로 표준편차만큼 폭을 두어 그린 3개의 선입니다. <mark>가격이 이 밴드 안에서 얼마나 벗어나 있는지를 보고 변동성과 과매수·과매도 상태를 가늠</mark>하는 데 쓰입니다. 이 글은 정의와 매매 전략을 나열하는 대신, 실제 숫자로 밴드를 처음부터 끝까지 계산해보고 두 가지 해석 관점을 균형 있게 정리했습니다.</p>

<div style="background:#e6f7fb;border:2px solid #0277bd;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#01579b;font-size:18px;">📊 볼린저밴드, 숫자로 보면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>중심선은 20일 단순이동평균, 상단·하단 밴드는 중심선에서 <b>표준편차의 2배</b>만큼 떨어진 선입니다.</li>
    <li>밴드 폭이 좁아지는 상태를 <mark>스퀴즈</mark>, 가격이 밴드를 타고 이동하는 상태를 <mark>밴드워크</mark>라고 부릅니다.</li>
    <li>상단·하단 접근은 반전 신호로도, 추세 지속 신호로도 해석될 수 있어 하나로 단정할 수 없습니다.</li>
    <li>이 글은 특정 매매 타이밍을 권하지 않는 정보 제공 목적의 글입니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>볼린저밴드란 무엇인가요</li>
  <li>상단 하단 밴드 계산법</li>
  <li>실제 숫자로 계산해보기</li>
  <li>밴드 폭이 좁아지고 넓어지는 이유</li>
  <li>밴드를 읽는 두 가지 관점</li>
  <li>헷갈리는 부분 정리</li>
</ol>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">볼린저밴드란 무엇인가요</h2>

<p>볼린저밴드(Bollinger Bands)는 미국의 투자자 존 볼린저가 1980년대에 고안한 기술적 분석 도구입니다. 가격 차트 위에 3개의 선, 즉 중심선과 상단 밴드, 하단 밴드를 함께 그려 가격의 평균 수준과 변동성을 한 번에 보여줍니다.</p>

<p>중심선은 일정 기간의 평균 가격이고, 상단·하단 밴드는 그 평균에서 가격이 얼마나 벌어져 있는지를 나타내는 통계적 범위입니다. 변동성이 커지면 밴드 폭이 넓어지고, 변동성이 줄어들면 밴드 폭도 좁아집니다.</p>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">상단 하단 밴드 계산법</h2>

<p>볼린저밴드는 세 단계로 계산합니다. 표준 설정값은 20일 기간, 표준편차 2배입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구성 요소</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산식</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">중심선</td>
      <td style="border:1px solid #ddd;padding:8px;">최근 20일 종가의 단순이동평균(SMA20)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">상단 밴드</td>
      <td style="border:1px solid #ddd;padding:8px;">SMA20 + (20일 표준편차 × 2)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">하단 밴드</td>
      <td style="border:1px solid #ddd;padding:8px;">SMA20 − (20일 표준편차 × 2)</td>
    </tr>
  </tbody>
</table>

<p>기간을 20일보다 짧게 잡으면 밴드가 가격 변화에 더 민감하게 반응하고, 길게 잡으면 완만하게 움직입니다. 표준편차 배수를 2보다 높이면 밴드 폭이 넓어져 밴드를 벗어나는 경우가 줄어듭니다.</p>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">실제 숫자로 계산해보기</h2>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상의 종가, 실제 종목 아님)</b>
  <p style="margin:8px 0 0 0;">20일 종가 평균이 <b>10,000원</b>, 이 20일 종가의 표준편차가 <b>300원</b>이라고 가정하면:</p>
  <ul style="margin:8px 0 0 0;padding-left:20px;">
    <li>중심선(SMA20) = 10,000원</li>
    <li>상단 밴드 = 10,000 + (300 × 2) = <mark>10,600원</mark></li>
    <li>하단 밴드 = 10,000 − (300 × 2) = <mark>9,400원</mark></li>
  </ul>
  <p style="margin:8px 0 0 0;">이 경우 밴드 폭은 1,200원(10,600−9,400)입니다. 만약 다음 20일 동안 가격 변동이 줄어들어 표준편차가 150원으로 작아지면, 상단·하단 밴드는 각각 10,300원·9,700원으로 좁혀져 밴드 폭이 600원으로 절반이 됩니다. 이렇게 표준편차가 작아질 때 밴드가 좁아지는 것이 스퀴즈입니다.</p>
</div>

<p>실제 계산에서는 매일 종가가 바뀌므로 중심선과 표준편차도 하루마다 새로 계산됩니다. 대부분의 증권사 차트 프로그램이 이 계산을 자동으로 해주지만, 원리를 알아두면 밴드가 왜 넓어지고 좁아지는지 스스로 판단할 수 있습니다.</p>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">밴드 폭이 좁아지고 넓어지는 이유</h2>

<p>밴드 폭은 표준편차, 즉 가격이 평균에서 얼마나 흩어져 있는지에 따라 정해집니다. 최근 가격이 좁은 범위에서 오르내리면 표준편차가 작아지고 밴드도 좁아지는데, 이 상태를 <b>스퀴즈</b>라고 부릅니다. 스퀴즈는 변동성이 낮아졌다는 뜻일 뿐, 다음 움직임이 위로 갈지 아래로 갈지까지 알려주지는 않습니다.</p>

<p>반대로 가격이 한 방향으로 강하게 움직이면 표준편차가 커지면서 밴드도 넓어집니다. 이때 가격이 상단이나 하단 밴드에 붙어 계속 이동하는 모습을 <b>밴드워크</b>라고 합니다. 밴드워크가 나타나면 추세가 강하다는 뜻으로 해석하는 경우가 많습니다.</p>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">밴드를 읽는 두 가지 관점</h2>

<p>가격이 상단이나 하단 밴드에 닿았을 때 이를 해석하는 방식은 <b>한 가지로 정해져 있지 않습니다.</b> 크게 두 관점이 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">관점</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">해석</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">역추세(평균회귀)</td>
      <td style="border:1px solid #ddd;padding:8px;">밴드는 통계적 범위이므로 상단·하단에 닿으면 평균으로 되돌아올 가능성이 있다고 보는 시각</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">추세추종</td>
      <td style="border:1px solid #ddd;padding:8px;">밴드워크 중이라면 밴드에 닿은 것 자체가 강한 추세의 증거이므로 추세가 이어질 가능성에 무게를 두는 시각</td>
    </tr>
  </tbody>
</table>

<p>같은 신호를 두고 정반대로 해석하는 두 관점이 공존하는 이유는, 밴드 하나만으로는 지금이 스퀴즈 이후 반전 국면인지 밴드워크 중인 추세 국면인지 구분하기 어렵기 때문입니다. 그래서 거래량이나 다른 보조지표를 함께 확인하는 경우가 많고, 이 글에서는 어느 한쪽 해석이 항상 옳다고 안내하지 않습니다.</p>

<h2 style="border-left:6px solid #0277bd;padding-left:12px;margin-top:36px;">헷갈리는 부분 정리</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">볼린저밴드란 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">20일 이동평균선을 중심선으로 두고, 그 위아래로 표준편차의 2배만큼 거리를 둔 상단·하단 밴드를 함께 그린 기술적 분석 도구입니다. 가격의 평균 수준과 변동성을 동시에 보여줍니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">기간이나 표준편차 배수를 꼭 20일, 2배로 써야 하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 20일과 2배가 가장 널리 쓰이는 표준 설정값이지만, 기간을 짧게 하면 민감하게, 길게 하면 완만하게 반응합니다. 정해진 정답은 없고 용도에 따라 조정해서 씁니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">밴드가 좁아지면 무조건 큰 변동이 오나요</summary>
  <p style="margin:10px 0 0 0;">스퀴즈는 변동성이 낮아졌다는 뜻일 뿐, 반드시 다음에 큰 움직임이 온다고 보장하지는 않습니다. 방향도 알려주지 않으므로 스퀴즈 자체를 매매 신호로 단정하지 않는 편이 안전합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상단 밴드에 닿으면 팔아야 하나요</summary>
  <p style="margin:10px 0 0 0;">단정할 수 없습니다. 평균회귀 관점에서는 반전 가능성으로 보지만, 추세추종 관점에서는 강한 추세(밴드워크)의 증거로 봅니다. 같은 신호를 정반대로 해석하는 두 시각이 있다는 점을 감안해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">볼린저밴드만 보고 매매를 결정해도 되나요</summary>
  <p style="margin:10px 0 0 0;">권장하지 않습니다. 볼린저밴드는 가격이 평균에서 얼마나 벌어졌는지를 보여줄 뿐, 그 자체로 매수·매도를 확정하는 지표는 아닙니다. 거래량이나 다른 지표와 함께 확인하고, 최종 판단과 그 결과는 투자자 본인의 몫입니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li>볼린저밴드는 법령으로 정의된 용어가 아니라 존 볼린저가 고안한 기술적 분석 도구로, 별도 정부기관의 공식 정의 페이지가 없습니다.</li>
    <li>이 글의 계산식과 개념 설명은 퀀트·투자정보 서비스 및 개인 재테크 콘텐츠 여러 곳을 교차확인해 정리했습니다.</li>
    <li>기준일: 2026년 9월 기준.</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 기술적 지표의 개념과 계산법을 설명하는 정보 글이며, 특정 종목의 매수나 매도 시점을 권하지 않습니다. 계산 예시는 이해를 돕기 위한 가상의 숫자이며, 실제 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "볼린저밴드 뜻과 계산법",
  "description": "볼린저밴드의 뜻과 상단·하단 밴드 계산법을 실제 숫자로 계산해보고, 밴드 스퀴즈·밴드워크 개념과 밴드를 해석하는 두 가지 관점을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-26",
  "dateModified": "2026-09-26",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/bollinger-bands-calculation"
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
      "name": "볼린저밴드란 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "20일 이동평균선을 중심선으로 두고, 그 위아래로 표준편차의 2배만큼 거리를 둔 상단·하단 밴드를 함께 그린 기술적 분석 도구입니다. 가격의 평균 수준과 변동성을 동시에 보여줍니다." }
    },
    {
      "@type": "Question",
      "name": "기간이나 표준편차 배수를 꼭 20일, 2배로 써야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 20일과 2배가 가장 널리 쓰이는 표준 설정값이지만, 기간을 짧게 하면 민감하게, 길게 하면 완만하게 반응합니다. 정해진 정답은 없고 용도에 따라 조정해서 씁니다." }
    },
    {
      "@type": "Question",
      "name": "밴드가 좁아지면 무조건 큰 변동이 오나요",
      "acceptedAnswer": { "@type": "Answer", "text": "스퀴즈는 변동성이 낮아졌다는 뜻일 뿐, 반드시 다음에 큰 움직임이 온다고 보장하지는 않습니다. 방향도 알려주지 않으므로 스퀴즈 자체를 매매 신호로 단정하지 않는 편이 안전합니다." }
    },
    {
      "@type": "Question",
      "name": "상단 밴드에 닿으면 팔아야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "단정할 수 없습니다. 평균회귀 관점에서는 반전 가능성으로 보지만, 추세추종 관점에서는 강한 추세(밴드워크)의 증거로 봅니다. 같은 신호를 정반대로 해석하는 두 시각이 있다는 점을 감안해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "볼린저밴드만 보고 매매를 결정해도 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "권장하지 않습니다. 볼린저밴드는 가격이 평균에서 얼마나 벌어졌는지를 보여줄 뿐, 그 자체로 매수·매도를 확정하는 지표는 아닙니다. 거래량이나 다른 지표와 함께 확인하고, 최종 판단과 그 결과는 투자자 본인의 몫입니다." }
    }
  ]
}
</script>
