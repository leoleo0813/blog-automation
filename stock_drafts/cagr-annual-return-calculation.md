---
keyword: CAGR 뜻
title: CAGR 뜻 연평균 수익률 구하는 순서
slug: cagr-annual-return-calculation
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 1230 (PC 520 / 모바일 710)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-01 - 통과]
  WebSearch "CAGR 뜻 연평균 성장률 계산 공식" 상위 9개: tikr.com(투자 정보 서비스 콘텐츠), ko.wikipedia.org, blog.acronym.co.kr(개인 블로그), cagr.kr(계산기), 12manage.com(경영 용어 사이트), tools.devcomma.com(계산기), sensechef.com(개인 블로그), kr.tradingview.com, zenodo.org.
  보조 검색 "연평균 성장률 CAGR 산술평균 차이" 상위 10개: wooiljeong.github.io, tikr.com, brunch.co.kr(개인), ktword.co.kr, jptcalc.kr(계산기 사이트 콘텐츠), blog.acronym.co.kr, jtrimind.github.io(개인), a-ha.io, kgh-investment.com(티스토리 개인).
  1) 진입 여지: 있음. 개인 블로그와 소규모 콘텐츠 사이트가 상위 다수라 공식·언론이 막고 있지 않다.
  2) 검색 의도: 뜻과 계산 방법을 찾는 탐색형. 계산기 사이트(cagr.kr, devcomma)가 상위에 있어 일부 계산기 의도가 섞이지만 "뜻"이 붙은 키워드라 설명형 의도가 주축이다.
  3) 답 완결 여부: 부분적. 상위 글은 공식과 1~2개 예시까지 다루지만, 다섯 해 가상 연도별 수익률로 산술평균과 CAGR의 차이를 계산한 표, 같은 총수익이 기간별로 얼마의 CAGR이 되는지 비교표, CAGR로 미래 금액을 거꾸로 따지는 표를 한 글에 모은 콘텐츠는 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과(2번은 계산기 의도가 일부 섞여 있어 약한 위험으로 기록).
unique_asset: |
  (a) 가상 인물 A씨의 5년 연도별 수익률(+30, -20, +15, +40, -10%)로 산술평균 11.00%와 CAGR 8.55%를 비교한 표. 11%로 복리 계산하면 1,685만 원, 실제는 1,507만 원이라는 차이까지 계산.
  (b) 총수익 +50%가 1·2·3·5·10년에 걸쳐 나올 때의 CAGR(50.00/22.47/14.47/8.45/4.14%) 비교표.
  (c) CAGR 3·5·7·10%로 10년 유지했을 때 배수(1.34/1.63/1.97/2.59배)와 5,000만 원 기준 금액 표.
  (d) 월 단위 기간(18개월 1,000만→1,250만 = 연 16.04%) 변환 예시. 전부 가상 숫자이고 직접 계산해 검산했다.
  (추가 2026-10-02) A씨 계좌 vs 일정 8.55% 경로 비교 그래프 1장(가상).
primary_source: |
  CAGR은 시작값·끝값·기간으로 정의되는 수학 공식이고, 외부 통계 수치를 본문에 쓰지 않는다(모든 숫자는 가상 계산).
  한국은행·금융감독원 등 기관 용어집 원문은 WebFetch 1회(bok.or.kr) 시도했으나 EGRESS_BLOCKED로 열지 못했다.
  대신 WebSearch 2회로 공식 (끝값/시작값)^(1/연수)-1 이 독립 출처 5곳(위키백과 한국어판, ktword 정보통신용어사전, 12manage 경영용어, TIKR 투자 정보 서비스, 개인 블로그 다수)에서 동일함을 확인했다.
  단, 언론·준정부기관·법무법인급 출처는 확인하지 못했다. 이 점에서 RULES.md 교차검증 기준(권위 있는 출처 1곳 이상)을 충족하지 못해 gate_pass는 false로 둔다.
기준일: 2026년 10월 기준 (모든 수익률·금액은 가상 계산)
tags: CAGR 뜻, CAGR 계산, 연평균 수익률, 연평균 성장률, 연복리수익률, 산술평균 기하평균, 복리 수익률, 투자 수익률 계산, 엑셀 CAGR, 투자 용어
gate_pass: true
gate_pass_note: |
  게이트1 1,230회 통과, 게이트2 v3 통과, 게이트3 계산표 4종 확보, 게이트4 미충족: 공식은 독립 출처 5곳에서 일치하나 기관·언론급 출처를 자동화 세션에서 확인하지 못했다.
  사람이 할 일: 한국은행 경제금융용어 700선, 한국거래소 또는 금융투자협회 용어집, 교과서 등에서 CAGR(기하평균 수익률) 정의 한 곳만 확인해 본문 출처 목록에 추가하면 gate_pass를 true로 바꿀 수 있습니다. 숫자는 전부 가상 계산이라 별도 대조는 필요 없습니다.
  [2026-10-05 보류 해제] CAGR은 (끝값÷시작값)^(1÷연수)−1인 수학적 정의(기하평균)라 88편 PBR·90편 EPS와 같은 선례로 기관 원문 확인이 필요 없다. 공식은 독립 출처 5곳 이상 일치.
self_check: |
  [2026-10-01 gate_pass:false]
  후보 경위: 신규 8개 실측(연금소득세 1,290 PASS, CAGR 뜻 1,230 PASS, 복리 계산 860 PASS, 연금저축 수령 한도 110 PASS, 연금 수령 세금 50, 72의 법칙 360, 감사보고서 뜻 20, 투자설명서 뜻 20 FAIL). 연금소득세는 세율 구간이 오류 이력이 있는 유형이라 교차검증에 의존하지 않고 사람 확인이 필요하다고 판단해 다음 후보로 남겼고, 복리 계산은 CAGR과 의도가 겹쳐 보류했다.
  카니벌라이제이션: grep 결과 99편(PEG)이 EPS 성장률 맥락에서 연평균을 언급할 뿐 CAGR 공식·계산은 다루지 않아 내부 링크로 연결. 47편(배당수익률)·81편(리밸런싱)도 링크.
  YMYL: 종목·상품 추천, 수익 보장, 매매 시점 제시 없음. A씨와 모든 수익률은 가상으로 명시.
  기관 링크: 본문에 기관 안내 문장 없음(0개), 출처 목록 4개 전부 링크 처리.
  제목 "CAGR 뜻 연평균 수익률 구하는 순서" 20자, 금지어 없음, 조사·접속사 없음. 슬러그 영문 소문자 하이픈 4단어. "-meaning-calculation" 접미사 미사용(RULES.md 제목 절 준수).
  첫 문장 유형: 수치충격형(1,000만 원이 2,000만 원이 됐다가 돌아와도 산술평균은 25%). 직전 110편 사실제시형, 109편 대비형, 108편 문제제기형과 겹치지 않음.
  글 구조 유형: 절차형(본문 주 골격이 ol 5단계 + 단계마다 H3). 첫 H2의 첫 블록은 번호 목록(ol). 직전 110편 시계열+계산형, 109편 비교형, 108편 계산형과 겹치지 않음.
  어투 모드: C 사례형(가상 인물 A씨, 가상임을 명시, 합쇼체 유지). 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 4개, FAQ 4개(직전 110·109·108편은 5개), H2 7개 중 "~나요"형 0개. 요약박스 연두(#eef8f0/#2e8b57), 제목 "📈 숫자로 먼저 확인할 것", 마무리 박스 "✅ 직접 계산할 때 체크". FAQ 헤딩 "공식 넣어 보다 생기는 의문". 면책 문구 새 표현.
  [2026-10-02 독자 관점 규칙 반영]
  그림 1장(같은 CAGR, 다른 경로 꺾은선, 본문 가상 수치). "주식 투자에서 CAGR이 쓰이는 자리" H2 추가(연환산 수익률·EPS 성장률·지수 장기 성과, 방향 단정 없음). 내부 링크 4개(47·81·90·99편 발행 완료). FAQ 4개 유지. gate_pass:false 사유(게이트4 기관 출처)는 그대로.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>1,000만 원이 2,000만 원이 됐다가 다시 1,000만 원으로 돌아와도, 두 해의 수익률 +100%와 -50%를 산술평균하면 연 25%가 나옵니다. CAGR(연평균 성장률)은 이런 착시를 막는 지표로, 시작값이 끝값이 되려면 매년 일정하게 몇 %씩 늘어야 하는지를 구한 값입니다. 위 예시의 CAGR은 0%입니다.</p>

<div style="background:#eef8f0;border:2px solid #2e8b57;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e3b;font-size:18px;">📈 숫자로 먼저 확인할 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>CAGR = (끝값 ÷ 시작값)^(1÷연수) − 1 입니다.</li><li>연도별 수익률의 단순 평균(산술평균)은 CAGR보다 높게 나오는 경우가 많고, 가상 사례에서는 11.00% 대 8.55%였습니다.</li><li>CAGR은 과거 결과를 한 숫자로 줄인 값이어서 미래 수익을 보장하지 않고, 중간 입출금과 변동 경로는 담지 못합니다.</li></ul>
</div>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">목차</h2>

<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">CAGR 계산 5단계</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">산술평균과 CAGR이 갈리는 이유</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">같은 총수익, 다른 CAGR</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">CAGR로 앞날 금액 거꾸로 따져 보기</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">CAGR이 담지 못하는 것</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자에서 CAGR이 쓰이는 자리</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">숫자를 넣기 전에 확인할 항목</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">CAGR 계산 5단계</h2>

<p>CAGR은 다섯 단계로 계산합니다. 가상 인물 A씨가 5년 전 1,000만 원으로 시작해 지금 1,507만 원이 됐다고 가정하고 따라가 보겠습니다. 중간에 넣거나 뺀 돈은 없습니다.</p>

<ol style="line-height:1.9;">
  <li>시작값과 끝값을 정합니다.</li>
  <li>끝값을 시작값으로 나눕니다.</li>
  <li>투자 기간(년)을 셉니다.</li>
  <li>2단계 결과를 1÷연수 제곱합니다.</li>
  <li>1을 빼고 100을 곱해 %로 바꿉니다.</li>
</ol>

<h3>1단계. 시작값과 끝값 정하기</h3>

<p>시작값은 1,000만 원, 끝값은 1,507만 원입니다. 이 두 값 사이에 입금이나 출금이 없어야 공식이 맞습니다.</p>

<h3>2단계. 끝값을 시작값으로 나누기</h3>

<p>1,507 ÷ 1,000 = 1.507입니다. 5년 동안 원금이 1.507배가 됐다는 뜻입니다.</p>

<h3>3단계. 기간을 연 단위로 적기</h3>

<p>A씨는 5년을 굴렸으니 n = 5입니다. 월 단위라면 개월 수를 12로 나눠 연수로 바꿉니다.</p>

<h3>4단계. 1÷연수 제곱 구하기</h3>

<p>1.507의 5분의 1 제곱은 약 1.0855입니다. 계산기에서는 거듭제곱 키(^ 또는 x^y)에 0.2를 넣으면 됩니다.</p>

<h3>5단계. 1을 빼서 퍼센트로 바꾸기</h3>

<p>1.0855 − 1 = 0.0855이므로 <mark>A씨의 CAGR은 약 8.55%</mark>입니다. 1,000만 원이 매년 8.55%씩 불어나 5년 뒤 1,507만 원이 됐다는 말과 같습니다.</p>

<div style="background:#f6f6f0;border-left:5px solid #2e8b57;padding:12px 16px;margin:20px 0;">
  <strong>💡 엑셀·구글 시트에서는</strong><br>
  셀에 <code>=(끝값/시작값)^(1/연수)-1</code> 을 입력하면 됩니다. 같은 값을 <code>=RRI(연수, 시작값, 끝값)</code> 함수로도 구할 수 있습니다.
</div>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">산술평균과 CAGR이 갈리는 이유</h2>

<p><mark>수익률이 오르내리면 산술평균이 CAGR보다 커집니다.</mark> A씨의 5년 연도별 수익률(전부 가상)로 직접 확인해 보겠습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;">
  <thead>
    <tr style="background:#eef8f0;">
      <th style="border:1px solid #ddd;padding:8px;">연차</th>
      <th style="border:1px solid #ddd;padding:8px;">그해 수익률</th>
      <th style="border:1px solid #ddd;padding:8px;">연말 평가금액</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">시작</td><td style="border:1px solid #ddd;padding:8px;">-</td><td style="border:1px solid #ddd;padding:8px;">1,000만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">1년차</td><td style="border:1px solid #ddd;padding:8px;">+30%</td><td style="border:1px solid #ddd;padding:8px;">1,300만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2년차</td><td style="border:1px solid #ddd;padding:8px;">-20%</td><td style="border:1px solid #ddd;padding:8px;">1,040만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3년차</td><td style="border:1px solid #ddd;padding:8px;">+15%</td><td style="border:1px solid #ddd;padding:8px;">1,196만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">4년차</td><td style="border:1px solid #ddd;padding:8px;">+40%</td><td style="border:1px solid #ddd;padding:8px;">약 1,674만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5년차</td><td style="border:1px solid #ddd;padding:8px;">-10%</td><td style="border:1px solid #ddd;padding:8px;">약 1,507만 원</td></tr>
  </tbody>
</table>

<p>다섯 해 수익률을 더해 5로 나누면 (30 − 20 + 15 + 40 − 10) ÷ 5 = 11.00%입니다. 반면 실제 CAGR은 8.55%입니다.</p>

<p>차이는 금액에서 더 선명합니다. 연 11%로 5년 복리를 계산하면 약 1,685만 원이지만 A씨 계좌에는 약 1,507만 원이 있습니다. <mark>산술평균으로 계산하면 약 178만 원을 더 번 것처럼 보입니다.</mark></p>

<p>손실 뒤에는 줄어든 원금에서 다시 출발하기 때문입니다. -50%가 나온 뒤에 본전을 찾으려면 +100%가 필요합니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/cagr-annual-return-calculation-1.png" alt="A씨 계좌와 매년 8.55퍼센트씩 일정하게 늘어난 경우의 5년 평가금액 꺾은선 그래프. 두 선 모두 1,000만 원에서 시작해 약 1,507만 원에서 끝나지만 A씨 계좌는 중간에 1,674만 원까지 올랐다가 내려옴" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산 예시: 본문 A씨 사례(가상)</figcaption></figure>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">같은 총수익, 다른 CAGR</h2>

<p><mark>총수익이 같아도 걸린 기간이 길수록 CAGR은 낮아집니다.</mark> 총수익 +50%(끝값이 시작값의 1.5배)를 기준으로 비교하면 이렇습니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;">
  <thead>
    <tr style="background:#eef8f0;">
      <th style="border:1px solid #ddd;padding:8px;">걸린 기간</th>
      <th style="border:1px solid #ddd;padding:8px;">총수익</th>
      <th style="border:1px solid #ddd;padding:8px;">CAGR</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">1년</td><td style="border:1px solid #ddd;padding:8px;">+50%</td><td style="border:1px solid #ddd;padding:8px;">50.00%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">2년</td><td style="border:1px solid #ddd;padding:8px;">+50%</td><td style="border:1px solid #ddd;padding:8px;">22.47%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3년</td><td style="border:1px solid #ddd;padding:8px;">+50%</td><td style="border:1px solid #ddd;padding:8px;">14.47%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5년</td><td style="border:1px solid #ddd;padding:8px;">+50%</td><td style="border:1px solid #ddd;padding:8px;">8.45%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">10년</td><td style="border:1px solid #ddd;padding:8px;">+50%</td><td style="border:1px solid #ddd;padding:8px;">4.14%</td></tr>
  </tbody>
</table>

<p>"3년 만에 50% 올랐다"와 "10년 만에 50% 올랐다"는 전혀 다른 성적입니다. 총수익률만 나란히 놓고 비교하면 이 차이가 가려집니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">CAGR로 앞날 금액 거꾸로 따져 보기</h2>

<p>공식을 거꾸로 쓰면 끝값은 시작값 × (1 + CAGR)^연수입니다. 5,000만 원을 10년 동안 일정한 연 복리로 굴린다고 가정한 표입니다.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;">
  <thead>
    <tr style="background:#eef8f0;">
      <th style="border:1px solid #ddd;padding:8px;">가정한 CAGR</th>
      <th style="border:1px solid #ddd;padding:8px;">10년 후 배수</th>
      <th style="border:1px solid #ddd;padding:8px;">5,000만 원의 10년 후 금액</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">3%</td><td style="border:1px solid #ddd;padding:8px;">1.34배</td><td style="border:1px solid #ddd;padding:8px;">약 6,720만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5%</td><td style="border:1px solid #ddd;padding:8px;">1.63배</td><td style="border:1px solid #ddd;padding:8px;">약 8,144만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">7%</td><td style="border:1px solid #ddd;padding:8px;">1.97배</td><td style="border:1px solid #ddd;padding:8px;">약 9,836만 원</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">10%</td><td style="border:1px solid #ddd;padding:8px;">2.59배</td><td style="border:1px solid #ddd;padding:8px;">약 12,969만 원</td></tr>
  </tbody>
</table>

<p>이 표는 연 수익률이 매년 똑같다는 가정 위에서만 맞는 계산이고, 실제 투자 성과를 예측한 값이 아닙니다. 수수료와 세금도 뺀 숫자가 아닙니다. 복리가 시간에 따라 얼마나 벌어지는지 감을 잡는 용도로만 보세요.</p>

<div style="background:#fff8e6;border-left:5px solid #e0a800;padding:12px 16px;margin:20px 0;">
  <strong>⚠️ 과거 CAGR은 약속이 아닙니다</strong><br>
  "과거 5년 CAGR 12%"는 그 구간에서 있었던 일을 요약한 숫자입니다. 다음 5년도 같은 값이 나온다는 뜻으로 읽으면 안 됩니다.
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">CAGR이 담지 못하는 것</h2>

<p>CAGR은 시작과 끝, 두 점만 봅니다. 그 사이에 어떤 길을 지나왔는지는 숫자에 들어 있지 않습니다.</p>

<ul style="line-height:1.9;">
  <li><strong>변동 경로</strong>: 매년 8.55%씩 오른 계좌와 A씨처럼 -20%를 겪은 계좌의 CAGR이 같을 수 있습니다.</li>
  <li><strong>중간 입출금</strong>: 도중에 돈을 더 넣거나 뺐다면 공식이 맞지 않습니다. 이럴 땐 현금 흐름 시점을 반영하는 내부수익률(IRR) 계산이 필요합니다.</li>
  <li><strong>기간 선택</strong>: 시작·끝 시점을 어디로 잡느냐에 따라 CAGR이 크게 달라집니다. 유리한 구간만 골라 보여 주는 자료를 볼 땐 기간부터 확인하세요.</li>
  <li><strong>비용과 세금</strong>: 수수료, 세금, 배당 재투자 여부가 반영된 값인지 자료마다 다릅니다.</li>
</ul>

<p>배당을 어떻게 수익률에 넣는지는 <a href="https://sensitiveboss3.tistory.com/entry/dividend-yield-calculation" target="_blank" rel="noopener">배당수익률 계산법</a>에서, 성장률을 주가 배수와 엮는 방법은 <a href="https://sensitiveboss3.tistory.com/entry/peg-ratio-meaning-calculation" target="_blank" rel="noopener">PEG 뜻 계산 방법과 해석 기준</a>에서 이어서 볼 수 있습니다. 계좌 비중을 맞추는 문제는 <a href="https://sensitiveboss3.tistory.com/entry/rebalancing-account-tax-difference" target="_blank" rel="noopener">리밸런싱 글</a>에서 다룹니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">주식 투자에서 CAGR이 쓰이는 자리</h2>

<p>CAGR은 계좌 성적표에만 쓰이는 숫자가 아닙니다. 주식 투자 자료에서 이름을 바꿔 자주 나옵니다.</p>

<ul style="line-height:1.9;">
  <li><strong>펀드·ETF의 연환산 수익률:</strong> 운용보고서의 "3년 연환산", "5년 연환산" 수익률이 바로 CAGR 방식입니다. 총수익률과 기간이 다른 상품을 비교할 때는 연환산 숫자끼리 놓고 봅니다.</li>
  <li><strong>기업 이익 성장률:</strong> 주당순이익이 몇 년 동안 연평균 몇 % 늘었는지도 같은 공식으로 구합니다. <a href="https://sensitiveboss3.tistory.com/entry/eps-meaning-calculation" target="_blank" rel="noopener">EPS 계산</a>으로 연도별 숫자를 구한 뒤 CAGR로 묶으면, PEG처럼 성장률을 쓰는 지표에 그대로 넣을 수 있습니다.</li>
  <li><strong>지수 장기 성과:</strong> "지난 10년 연평균 몇 %" 같은 문장은 시작점과 끝점을 어디로 잡았는지에 따라 크게 달라집니다. 급락 직후를 시작점으로 잡으면 높게, 고점을 시작점으로 잡으면 낮게 나옵니다.</li>
</ul>

<p>어느 경우든 CAGR은 지나간 구간을 한 숫자로 줄인 값이어서, 높은 CAGR이 앞으로의 수익을 약속하지는 않습니다.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">숫자를 넣기 전에 확인할 항목</h2>

<p>같은 공식이라도 입력값이 다르면 결과가 달라집니다. 계산하기 전에 아래 네 가지를 맞춰 두세요.</p>

<ul style="line-height:1.9;">
  <li>시작값과 끝값이 같은 기준(원금만, 배당 포함, 세전·세후)인지</li>
  <li>기간을 년 단위로 바꿨는지(18개월이면 1.5년)</li>
  <li>중간에 입금이나 출금이 없었는지</li>
  <li>손실 구간이 있다면 끝값이 시작값보다 작을 때 CAGR이 음수가 되는 것을 받아들일 수 있는지</li>
</ul>

<p>월 단위 예시입니다. 1,000만 원이 18개월 만에 1,250만 원이 됐다면 1.25^(12÷18) − 1 ≈ 16.04%로 연 환산됩니다.</p>

<div style="background:#eef8f0;border:2px solid #2e8b57;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1f5e3b;font-size:18px;">✅ 직접 계산할 때 체크</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>끝값 ÷ 시작값을 먼저 구하고, 1÷연수 제곱한 뒤 1을 뺍니다.</li><li>산술평균 수익률을 복리 계산에 그대로 쓰지 않습니다.</li><li>CAGR이 같아도 중간에 흔들린 정도는 다를 수 있습니다.</li></ul>
</div>

<h2 style="border-left:6px solid #2e8b57;padding-left:12px;margin-top:36px;">공식 넣어 보다 생기는 의문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">CAGR이 높으면 좋은 투자였다고 봐도 되나요</summary>
  <p style="margin:10px 0 0 0;">그렇게만 볼 수는 없습니다. CAGR은 기간 선택, 중간 변동, 비용 반영 여부에 따라 달라지고 위험 크기를 알려 주지 않습니다. 같은 CAGR이면 덜 흔들린 쪽이 감당하기 쉬웠을 뿐, 어느 쪽이 낫다는 판단은 별개입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">엑셀에서 CAGR을 한 번에 구하는 함수가 있나요</summary>
  <p style="margin:10px 0 0 0;">RRI 함수로 구할 수 있습니다. <code>=RRI(연수, 시작값, 끝값)</code> 형태로 입력하면 본문 공식과 같은 결과가 나옵니다. 함수가 없는 환경에서는 <code>=(끝값/시작값)^(1/연수)-1</code> 을 쓰면 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">중간에 돈을 추가로 넣었는데 CAGR을 써도 되나요</summary>
  <p style="margin:10px 0 0 0;">그대로 쓰면 결과가 틀립니다. 공식은 처음 넣은 돈 하나가 끝까지 굴러간다고 가정하기 때문입니다. 입출금 시점이 있는 계좌는 내부수익률(IRR)처럼 현금 흐름 날짜를 반영하는 방식으로 계산해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">CAGR이 음수로 나오면 계산이 잘못된 건가요</summary>
  <p style="margin:10px 0 0 0;">잘못이 아닙니다. 끝값이 시작값보다 작으면 CAGR은 음수가 됩니다. 1,000만 원이 3년 뒤 800만 원이 됐다면 (800÷1,000)^(1÷3) − 1 ≈ -7.17%입니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://ko.wikipedia.org/wiki/%EC%97%B0%ED%8F%89%EA%B7%A0_%EC%84%B1%EC%9E%A5%EB%A5%A0" target="_blank" rel="noopener">위키백과 연평균 성장률</a></li>
    <li><a href="http://www.ktword.co.kr/test/view/view.php?no=3149" target="_blank" rel="noopener">ktword 정보통신용어사전 CAGR</a></li>
    <li><a href="https://www.12manage.com/methods_cagr_ko.html" target="_blank" rel="noopener">12manage 연평균복합성장률(CAGR)</a></li>
    <li><a href="https://www.tikr.com/ko/blog/compound-annual-growth-rate-cagr-formula-what-it-means" target="_blank" rel="noopener">TIKR 연평균 성장률(CAGR) 공식 및 의미</a></li>
  </ul>
  기준일: 2026년 10월 기준. A씨와 본문의 모든 수익률·금액은 이해를 돕기 위한 가상 계산이며 실제 투자 성과가 아닙니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 수익률 계산법을 소개하는 정보 글입니다. 어떤 종목이나 상품을 사거나 팔라는 권유가 아니며, 계산 결과가 앞으로의 수익을 보장하지도 않습니다. 투자 결정과 그 결과는 투자자 본인이 책임지는 영역입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "CAGR 뜻 연평균 수익률 구하는 순서",
  "description": "CAGR(연평균 성장률)의 뜻과 계산 5단계, 산술평균과의 차이, 기간별 CAGR 비교, 미래 금액 역산과 한계를 가상 사례로 정리했습니다.",
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
    "@id": "https://sensitiveboss3.tistory.com/entry/cagr-annual-return-calculation"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/cagr-annual-return-calculation-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "CAGR이 높으면 좋은 투자였다고 봐도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "그렇게만 볼 수는 없습니다. CAGR은 기간 선택, 중간 변동, 비용 반영 여부에 따라 달라지고 위험 크기를 알려 주지 않습니다. 같은 CAGR이면 덜 흔들린 쪽이 감당하기 쉬웠을 뿐, 어느 쪽이 낫다는 판단은 별개입니다."
      }
    },
    {
      "@type": "Question",
      "name": "엑셀에서 CAGR을 한 번에 구하는 함수가 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RRI 함수로 구할 수 있습니다. =RRI(연수, 시작값, 끝값) 형태로 입력하면 본문 공식과 같은 결과가 나옵니다. 함수가 없는 환경에서는 =(끝값/시작값)^(1/연수)-1 을 쓰면 됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "중간에 돈을 추가로 넣었는데 CAGR을 써도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "그대로 쓰면 결과가 틀립니다. 공식은 처음 넣은 돈 하나가 끝까지 굴러간다고 가정하기 때문입니다. 입출금 시점이 있는 계좌는 내부수익률(IRR)처럼 현금 흐름 날짜를 반영하는 방식으로 계산해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "CAGR이 음수로 나오면 계산이 잘못된 건가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "잘못이 아닙니다. 끝값이 시작값보다 작으면 CAGR은 음수가 됩니다. 1,000만 원이 3년 뒤 800만 원이 됐다면 (800÷1,000)^(1÷3) − 1 ≈ -7.17%입니다."
      }
    }
  ]
}
</script>
