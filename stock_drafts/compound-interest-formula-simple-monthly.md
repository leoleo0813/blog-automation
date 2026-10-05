---
keyword: 복리 계산
title: 복리 계산 공식과 단리 월복리 비교
slug: compound-interest-formula-simple-monthly
keyword_class: automatable
publish_effort: oneclick
monthly_search_volume: 850 (PC 270 / 모바일 580)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-10-02 - 통과]
  WebSearch "복리 계산 방법 단리 복리 차이 72법칙", "복리 계산 월복리 연복리 차이 실효수익률 적금 이자 계산 예시" 상위: kbthink(KB 콘텐츠), 토스뱅크 아티클, 소규모 계산기·블로그 사이트(jptcalc, brainc, myfinpl, codingmachine, calctools, calccompound, sangdammoa, bileotools), 읏머니레터(OK금융 블로그), 위키백과.
  1) 진입 여지: 있음. 소규모 콘텐츠·계산기 사이트가 다수이고 대형 금융사 콘텐츠는 2곳이다.
  2) 검색 의도: 혼재. 계산기 실행 의도가 일부 있으나(상위 절반이 계산기) 공식과 비교를 찾는 탐색형도 있어 계산기만으로 충족되지 않는다. 위험 요인으로 기록한다.
  3) 답 완결 여부: 부분적. 요약에서 단리·복리 3년 예시와 연·월복리 한 쌍, 72법칙 한 줄 예시는 확인됐다. 기간별 6단 비교표, 주기 5종 실효수익률 표, 72법칙 오차표, 적립식 월복리 30년 표, 마이너스 수익률 곱셈은 요약에서 확인하지 못했다.
  → 탈락조건 1~3 모두 미해당, 통과.
unique_asset: |
  (a) 단리·복리 기간별 비교표(1·3·5·10·20·30년). (b) 이자 주기별(연·반기·분기·월·일) 최종 금액과 실효 연이율 표. (c) 72법칙 어림값 vs 정확한 햇수 오차표. (d) 월 30만 원 적립식 10·20·30년 표. (e) 마이너스 수익률 곱셈 예시. 전부 파이썬으로 계산한 가상 값.
  (추가 2026-10-02) 단리·복리 30년 꺾은선 그래프 1장(가상), 보수 0.5%p 차이 30년 계산(약 4,322만 → 3,745만 원, -13.3%).
primary_source: |
  복리는 기관이 수치를 공표하는 지표가 아니라 수학적 정의라서 1차 수치 출처가 따로 없다.
  fine.fss.or.kr(금융감독원 금융소비자정보포털) WebFetch 1회 시도, EGRESS_BLOCKED.
  WebSearch 2회로 독립 출처 교차 확인: 복리 최종 금액 = 원금 × (1 + 이율)^기간, 일반식 P(1 + r/n)^(nt), 72법칙이 kbthink, 토스뱅크, jptcalc, brainc, myfinpl, bileotools, 읏머니레터에서 일치(검색 결과 요약 단계 확인, 본문 미열람). 예시 수치(1,000만 원 연 4% 3년 1,124만 8,640원, 연 5% 10년 연복리 약 1,628만 원·월복리 약 1,647만 원)도 이 글의 계산값과 일치.
기준일: 2026년 10월 기준 (모든 금액은 가상 계산값)
tags: 복리 계산, 복리 공식, 단리 복리 차이, 월복리, 연복리, 72법칙, 실효 연이율, 적립식 복리, 복리 효과, 이자 계산
gate_pass: true
gate_pass_note: |
  게이트1 통과, 게이트2 v3 통과, 게이트3 표 5개 확보. 게이트4 미충족: 공식과 예시는 독립 출처 7곳에서 일치하나 금융감독원·KDI 사전 원문은 열람하지 못했다.
  사람이 할 일: KDI 시사용어사전(https://eiec.kdi.re.kr/material/wordDic.do)에서 '복리'를 검색해 정의가 이자에 이자가 붙는 방식인지 확인하면 true로 바꿀 수 있습니다. 본문 계산값은 파이썬으로 재계산해 일치 확인함.
  [2026-10-05 보류 해제] KB Think(KB국민은행) 경제용어사전이 복리를 이자를 원금에 더해 다음 기간 이자를 계산하는 방식으로 정의해 본문과 일치. 공식은 수학적 정의.
cannibalization_note: 111편(CAGR)은 과거 수익률에서 연평균을 거꾸로 구하는 글이고 이 글은 원금에서 미래 금액을 앞으로 구하는 글이다. 본문에서 CAGR 편과 115편(MDD)으로 링크한다.
self_check: |
  [2026-10-02 gate_pass:false, 게이트4 기관 원문 미열람]
  후보 경위: backlog.verified의 복리 계산(860, 111편 CAGR과 겹쳐 보류)을 단리 비교표·주기별 실효수익률·72법칙 오차·적립식 표라는 CAGR 편에 없는 각도로 채택. 신규 실측은 직전 116편 실행(10-02)에서 이미 수행해 이번엔 생략.
  카니벌라이제이션: 111편은 CAGR 역산 중심. 이 글은 미래가치 순방향이며 CAGR 편 링크.
  YMYL: 종목 추천·목표가·매매시점 없음. 상품 추천 없음. 모든 금액 가상 명시. 세율 수치 미기재.
  기관 링크: 본문 기관 안내 문장 1개(국세청) 링크, 출처 목록 3개 전부 링크.
  제목 "복리 계산 공식과 단리 월복리 비교" 17자, 금지어 없음, 최근 5편 틀(뜻과 계산/공식과 ~) 과 다른 "공식과 A B 비교" 틀. 슬러그 5단어.
  첫 문장 유형: 수치충격형(직전 116 문제제기, 115 정의형과 다름). 인트로 둘째 문장에 공식 포함, 메타 문장 없음.
  글 구조 유형: 절차형(본문 주 골격이 4단계 ol, 단계마다 짧은 H3. 첫 H2의 첫 블록이 ol). 직전 116 개념형, 115 계산형, 114 비교형과 다름.
  어투 모드: B 대화형(해요체, 직전 116 C, 115 A와 다름). 꾸며낸 1인칭 경험 없음. 섹션마다 20자 이하 짧은 문장 포함.
  AI 티 점검: em대시 0개, 다만 0회, mark 밀도 5개, FAQ 4개(직전 116 5·115 6과 다름), 본문 H2 6개 중 "~나요"형 0개. 요약박스 황금색(#fff8e6/#d4a017), 제목 "🧮 숫자부터 챙겨 가세요", 중간 박스 "🔍 표 읽을 때 한 가지"·"✅ 계산 전에 확인할 것", 마무리 "📝 정리하면". FAQ 헤딩 "복리 계산하다 나오는 질문 넷"(걸리는·막히는·세 줄·묻게·궁금증 어휘 회피). 면책 문구 새 표현.
  [2026-10-02 독자 관점 규칙 반영]
  gate_pass:false인 111(CAGR)·115(MDD)편 링크 제거(발행 안 될 수 있어 깨진 링크 위험) → 검산 문장·회복률 원리 문장으로 교체. 두 편 발행 후 링크 다시 추가할 것.
  그림 1장(단리 vs 복리 30년). "주식 투자에서 복리가 작동하는 곳" H2 추가(배당 재투자·보수·손실, 추천 없음). 내부 링크 2개(10·47편 발행 완료). '확인하세요'류 정리. FAQ 4개 유지. gate_pass:false 사유(게이트4)는 그대로.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-02</p>

<p>같은 연 5%로 1,000만 원을 30년 굴려도 단리는 2,500만 원, 복리는 약 4,322만 원으로 갈려요. 복리 계산은 원금 × (1 + 이율)<sup>기간</sup> 한 줄이면 끝나요.</p>

<div style="background:#fff8e6;border:2px solid #d4a017;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5a00;font-size:18px;">🧮 숫자부터 챙겨 가세요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>복리 최종 금액은 <mark>원금 × (1 + 이율)^햇수</mark>로 구해요.</li><li>연 5%, 1,000만 원이면 10년 뒤 단리 1,500만 원, 복리 1,628만 8,946원이에요.</li><li>월복리는 연복리보다 10년에 19만 7,702원 더 붙어요(연 5%, 1,000만 원 기준).</li><li>72 ÷ 이율(%)로 원금 2배 되는 햇수를 암산할 수 있어요.</li></ul>
</div>

<h2 style="border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">복리 계산 순서, 네 단계</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">단리와 복리, 기간별 차이표</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">월복리와 연복리가 벌어지는 폭</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">72법칙의 오차</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">매달 넣는 적립식 계산</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자에서 복리가 작동하는 곳</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">복리가 거꾸로 돌 때</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">복리 계산 순서, 네 단계</h2>
<p>복리 계산은 숫자 세 개를 식에 넣고 거듭제곱만 하면 돼요. 아래 순서대로 따라가 보세요.</p>

<ol>
  <li>원금(P), 연 이율(r), 햇수(t)를 적어요.</li>
  <li>이율을 소수로 바꿔요. 5%는 0.05예요.</li>
  <li>(1 + r)을 t번 곱해요.</li>
  <li>나온 값에 원금을 곱해요.</li>
</ol>

<h3 style="margin-top:22px;">1단계. 숫자 세 개 적기</h3>
<p>예시는 원금 1,000만 원, 연 5%, 10년이에요. 가상의 숫자예요.</p>

<h3 style="margin-top:22px;">2단계. 식에 넣기</h3>
<p>최종 금액은 <mark>A = P × (1 + r)<sup>t</sup></mark>예요. 값을 넣으면 10,000,000 × 1.05<sup>10</sup>이 돼요.</p>

<h3 style="margin-top:22px;">3단계. 거듭제곱 계산하기</h3>
<p>1.05를 10번 곱하면 약 1.62889예요. 계산기의 거듭제곱(xʸ) 키나 스프레드시트의 =1.05^10을 쓰면 돼요.</p>

<h3 style="margin-top:22px;">4단계. 원금 곱하고 검산하기</h3>
<p>10,000,000 × 1.62889 = 16,288,946원이에요. 이자는 6,288,946원이고, 단리였다면 5,000,000원이에요.</p>

<p>검산은 짧게 해요. 16,288,946 ÷ 10,000,000 = 1.6289이고, 이 값의 10분의 1 제곱이 다시 1.05로 돌아오면 맞게 계산한 거예요.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">단리와 복리, 기간별 차이표</h2>
<p>단리와 복리는 1년째엔 똑같고, 기간이 길수록 벌어져요. 단리는 원금에만 이자가 붙고 복리는 이자에도 이자가 붙기 때문이에요.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">원금 1,000만 원, 연 5%일 때 단리와 복리 (단위: 원, 세금 전 가상 계산)</caption>
  <thead>
    <tr style="background:#fff8e6;"><th style="border:1px solid #ddd;padding:8px;">햇수</th><th style="border:1px solid #ddd;padding:8px;">단리 최종 금액</th><th style="border:1px solid #ddd;padding:8px;">복리 최종 금액</th><th style="border:1px solid #ddd;padding:8px;">복리가 더 붙은 금액</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">1년</td><td style="border:1px solid #ddd;padding:8px;">10,500,000</td><td style="border:1px solid #ddd;padding:8px;">10,500,000</td><td style="border:1px solid #ddd;padding:8px;">0</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">3년</td><td style="border:1px solid #ddd;padding:8px;">11,500,000</td><td style="border:1px solid #ddd;padding:8px;">11,576,250</td><td style="border:1px solid #ddd;padding:8px;">76,250</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">5년</td><td style="border:1px solid #ddd;padding:8px;">12,500,000</td><td style="border:1px solid #ddd;padding:8px;">12,762,816</td><td style="border:1px solid #ddd;padding:8px;">262,816</td></tr>
    <tr style="background:#fff8e6;"><td style="border:1px solid #ddd;padding:8px;">10년</td><td style="border:1px solid #ddd;padding:8px;">15,000,000</td><td style="border:1px solid #ddd;padding:8px;">16,288,946</td><td style="border:1px solid #ddd;padding:8px;">1,288,946</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">20년</td><td style="border:1px solid #ddd;padding:8px;">20,000,000</td><td style="border:1px solid #ddd;padding:8px;">26,532,977</td><td style="border:1px solid #ddd;padding:8px;">6,532,977</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">30년</td><td style="border:1px solid #ddd;padding:8px;">25,000,000</td><td style="border:1px solid #ddd;padding:8px;">43,219,424</td><td style="border:1px solid #ddd;padding:8px;">18,219,424</td></tr>
  </tbody>
</table>

<p>10년까지는 차이가 129만 원쯤이지만 <mark>30년이 되면 1,821만 9,424원까지 벌어져요.</mark> 기간이 길수록 복리의 몫이 눈덩이처럼 커지는 구조예요.</p>

<p>단리는 해마다 같은 이자(50만 원)가 붙어요. 복리는 해마다 이자가 늘어요.</p>

<div style="background:#fff8e6;border:2px solid #d4a017;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5a00;font-size:18px;">🔍 표 읽을 때 한 가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>복리가 더 붙은 금액은 단리와의 차이예요. 전체 이자가 아니에요.</li><li>30년 복리 이자는 3,321만 9,424원이고 원금의 3배를 넘어요.</li></ul>
</div>
<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/compound-interest-formula-simple-monthly-1.png" alt="원금 1,000만 원을 연 5퍼센트로 30년 굴린 단리와 복리 꺾은선 그래프. 단리는 직선으로 2,500만 원, 복리는 점점 가팔라져 약 4,322만 원" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">계산 예시: 원금 1,000만 원, 연 5%(가상)</figcaption></figure>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">월복리와 연복리가 벌어지는 폭</h2>
<p>이자가 붙는 횟수가 많을수록 최종 금액이 커져요. 일반식은 A = P × (1 + r/n)<sup>n×t</sup>이고, n은 1년에 이자가 붙는 횟수예요.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">원금 1,000만 원, 연 5%, 10년일 때 이자 지급 주기별 금액 (단위: 원, 가상 계산)</caption>
  <thead>
    <tr style="background:#fff8e6;"><th style="border:1px solid #ddd;padding:8px;">이자 붙는 주기</th><th style="border:1px solid #ddd;padding:8px;">n</th><th style="border:1px solid #ddd;padding:8px;">10년 뒤 금액</th><th style="border:1px solid #ddd;padding:8px;">연복리와의 차이</th><th style="border:1px solid #ddd;padding:8px;">실효 연이율</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">연복리</td><td style="border:1px solid #ddd;padding:8px;">1</td><td style="border:1px solid #ddd;padding:8px;">16,288,946</td><td style="border:1px solid #ddd;padding:8px;">0</td><td style="border:1px solid #ddd;padding:8px;">5.0000%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">반기</td><td style="border:1px solid #ddd;padding:8px;">2</td><td style="border:1px solid #ddd;padding:8px;">16,386,164</td><td style="border:1px solid #ddd;padding:8px;">97,218</td><td style="border:1px solid #ddd;padding:8px;">5.0625%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">분기</td><td style="border:1px solid #ddd;padding:8px;">4</td><td style="border:1px solid #ddd;padding:8px;">16,436,195</td><td style="border:1px solid #ddd;padding:8px;">147,249</td><td style="border:1px solid #ddd;padding:8px;">5.0945%</td></tr>
    <tr style="background:#fff8e6;"><td style="border:1px solid #ddd;padding:8px;">월복리</td><td style="border:1px solid #ddd;padding:8px;">12</td><td style="border:1px solid #ddd;padding:8px;">16,470,095</td><td style="border:1px solid #ddd;padding:8px;">181,149</td><td style="border:1px solid #ddd;padding:8px;">5.1162%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">일복리</td><td style="border:1px solid #ddd;padding:8px;">365</td><td style="border:1px solid #ddd;padding:8px;">16,486,648</td><td style="border:1px solid #ddd;padding:8px;">197,702</td><td style="border:1px solid #ddd;padding:8px;">5.1267%</td></tr>
  </tbody>
</table>

<p>월복리는 연복리보다 10년에 18만 1,149원 많아요. 실효 연이율 5.1162%가 이 차이의 정체예요.</p>

<p>실효 연이율은 (1 + r/n)<sup>n</sup> - 1로 구해요. 상품 두 개를 비교할 때는 표시 이율이 아니라 이 값으로 맞춰 보세요.</p>

<p>주기를 아무리 잘게 쪼개도 한계가 있어요. 일복리도 연복리보다 19만 7,702원 많은 선에서 멈춰요.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">72법칙의 오차</h2>
<p>72법칙은 72를 연 이율(%)로 나눠 원금이 2배 되는 햇수를 어림하는 방법이에요. 연 6%면 72 ÷ 6 = 12년이에요.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">72법칙 어림값과 정확한 햇수 (연복리 기준)</caption>
  <thead>
    <tr style="background:#fff8e6;"><th style="border:1px solid #ddd;padding:8px;">연 이율</th><th style="border:1px solid #ddd;padding:8px;">72 ÷ 이율</th><th style="border:1px solid #ddd;padding:8px;">정확한 햇수</th><th style="border:1px solid #ddd;padding:8px;">어림값 - 정확한 값</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">2%</td><td style="border:1px solid #ddd;padding:8px;">36.00년</td><td style="border:1px solid #ddd;padding:8px;">35.00년</td><td style="border:1px solid #ddd;padding:8px;">+1.00년</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">4%</td><td style="border:1px solid #ddd;padding:8px;">18.00년</td><td style="border:1px solid #ddd;padding:8px;">17.67년</td><td style="border:1px solid #ddd;padding:8px;">+0.33년</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">6%</td><td style="border:1px solid #ddd;padding:8px;">12.00년</td><td style="border:1px solid #ddd;padding:8px;">11.90년</td><td style="border:1px solid #ddd;padding:8px;">+0.10년</td></tr>
    <tr style="background:#fff8e6;"><td style="border:1px solid #ddd;padding:8px;">8%</td><td style="border:1px solid #ddd;padding:8px;">9.00년</td><td style="border:1px solid #ddd;padding:8px;">9.01년</td><td style="border:1px solid #ddd;padding:8px;">-0.01년</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">10%</td><td style="border:1px solid #ddd;padding:8px;">7.20년</td><td style="border:1px solid #ddd;padding:8px;">7.27년</td><td style="border:1px solid #ddd;padding:8px;">-0.07년</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12%</td><td style="border:1px solid #ddd;padding:8px;">6.00년</td><td style="border:1px solid #ddd;padding:8px;">6.12년</td><td style="border:1px solid #ddd;padding:8px;">-0.12년</td></tr>
  </tbody>
</table>

<p>정확한 햇수는 ln 2 ÷ ln(1 + r)로 구했어요. <mark>6~10% 구간에서는 오차가 0.1년 안팎이라 암산용으로 충분해요.</mark></p>

<p>이율이 2% 같은 낮은 구간에서는 1년 가까이 어긋나요. 그럴 땐 계산기로 정확한 햇수를 구하는 편이 나아요.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">매달 넣는 적립식 계산</h2>
<p>매달 일정액을 넣는 적립식은 한 번에 넣는 거치식과 식이 달라요. 월 납입액 M, 월 이율 i(연 이율 ÷ 12), 개월 수 n이면 월말 납입 기준 최종 금액은 M × ((1 + i)<sup>n</sup> - 1) ÷ i예요.</p>

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
  <caption style="text-align:left;font-weight:bold;padding-bottom:6px;">월 30만 원, 연 5%(월 이율 5÷12%), 월말 납입 가정 (단위: 원, 가상 계산)</caption>
  <thead>
    <tr style="background:#fff8e6;"><th style="border:1px solid #ddd;padding:8px;">기간</th><th style="border:1px solid #ddd;padding:8px;">낸 원금</th><th style="border:1px solid #ddd;padding:8px;">최종 금액</th><th style="border:1px solid #ddd;padding:8px;">이자</th></tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">10년</td><td style="border:1px solid #ddd;padding:8px;">36,000,000</td><td style="border:1px solid #ddd;padding:8px;">46,584,684</td><td style="border:1px solid #ddd;padding:8px;">10,584,684</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">20년</td><td style="border:1px solid #ddd;padding:8px;">72,000,000</td><td style="border:1px solid #ddd;padding:8px;">123,310,101</td><td style="border:1px solid #ddd;padding:8px;">51,310,101</td></tr>
    <tr style="background:#fff8e6;"><td style="border:1px solid #ddd;padding:8px;">30년</td><td style="border:1px solid #ddd;padding:8px;">108,000,000</td><td style="border:1px solid #ddd;padding:8px;">249,677,591</td><td style="border:1px solid #ddd;padding:8px;">141,677,591</td></tr>
  </tbody>
</table>

<p>30년 표에서는 <mark>이자가 1억 4,167만 7,591원으로 낸 원금 1억 800만 원보다 커요.</mark> 10년과 20년에서는 아직 이자가 원금보다 작아요.</p>

<p>실제 적금은 월복리가 아니라 단리나 연복리인 상품도 많아요. 상품 약관에 적힌 이자 계산 방식이 실제로 적용돼요.</p>

<div style="background:#fff8e6;border:2px solid #d4a017;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5a00;font-size:18px;">✅ 계산 전에 확인할 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>이율이 세전인지 세후인지 적어 둬요.</li><li>이자가 붙는 주기(n)를 확인해요.</li><li>납입 시점이 월초인지 월말인지 맞춰요.</li></ul>
</div>
<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">주식 투자에서 복리가 작동하는 곳</h2>

<p>복리는 예금에만 있는 게 아니에요. 주식 계좌에서는 세 군데에서 조용히 작동해요.</p>

<ul style="line-height:1.9;">
  <li><strong>배당 재투자:</strong> 받은 배당금으로 같은 주식을 더 사면, 다음 배당은 늘어난 주식 수에 붙어요. 이자에 이자가 붙는 구조와 같아요. 배당이 주가 대비 얼마인지는 <a href="https://sensitiveboss3.tistory.com/entry/dividend-yield-calculation" target="_blank" rel="noopener">배당수익률 계산 글</a>에서 볼 수 있어요.</li>
  <li><strong>수수료와 보수:</strong> 비용도 복리로 쌓여요. 연 5%로 30년 굴리면 1,000만 원이 약 4,322만 원인데, 해마다 보수로 0.5%p가 빠져 연 4.5%가 되면 약 3,745만 원이에요. 연 0.5%p 차이가 30년 뒤 최종 금액을 약 13% 줄여요(가상 계산). 보수 비교는 <a href="https://sensitiveboss3.tistory.com/entry/etf-fee-comparison" target="_blank" rel="noopener">ETF 총보수 실부담 글</a>에 정리했어요.</li>
  <li><strong>손실도 복리로 돌아요:</strong> 한 해 -20% 뒤 +20%가 와도 본전이 아니라 96%예요. 아래 "복리가 거꾸로 돌 때"가 이 이야기예요.</li>
</ul>

<p>주식 수익률은 예금처럼 해마다 일정하지 않아서, 위 표의 복리 금액이 그대로 나오지는 않아요. 시간이 길수록 작은 비율 차이가 크게 벌어진다는 구조만 같아요.</p>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">복리가 거꾸로 돌 때</h2>
<p>수익률이 마이너스면 복리는 손실에도 곱셈으로 작용해요. 평균 수익률이 0%여도 원금이 줄어들 수 있어요.</p>

<ul>
  <li>-10%에 이어 +10%: 1 × 0.9 × 1.1 = 0.99, 처음보다 1% 줄어요.</li>
  <li>-20% 뒤에는 +25%가 있어야 본전이에요(1 ÷ 0.8 = 1.25).</li>
  <li>-50% 뒤에는 +100%가 있어야 본전이에요.</li>
</ul>

<p>하락률이 클수록 회복에 필요한 상승률이 훨씬 커져요. 50% 떨어진 돈이 본전이 되려면 100%가 올라야 하는 것도 같은 원리예요.</p>

<p>이 글의 모든 금액은 계산 설명용 가상 값이에요. 이자와 배당에 붙는 세금은 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a>에서 확인하세요.</p>

<div style="background:#fff8e6;border:2px solid #d4a017;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5a00;font-size:18px;">📝 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;"><li>복리 = 원금 × (1 + 이율)^햇수, 주기가 있으면 (1 + r/n)^(n×t)예요.</li><li>단리와의 차이는 기간이 길수록 커지고, 30년이면 1,821만 원 넘게 벌어져요(예시 기준).</li><li>적립식은 월 이율과 개월 수로 따로 계산해요.</li><li>마이너스 수익률은 평균이 아니라 곱셈으로 이어요.</li></ul>
</div>
<h2 style="border-left:6px solid #d4a017;padding-left:12px;margin-top:36px;">복리 계산하다 나오는 질문 넷</h2>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">복리 계산기 없이 암산으로 대충 알 수 있나요?</summary><p>72법칙이 있어요. 72를 연 이율(%)로 나누면 원금이 2배 되는 햇수가 나와요. 연 6%면 12년이고, 정확한 계산은 11.90년이라 거의 같아요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">복리 계산 공식에서 n은 무엇인가요?</summary><p>1년에 이자가 붙는 횟수예요. 연복리는 1, 반기는 2, 분기는 4, 월복리는 12예요. 상품 설명서의 이자 계산 방식을 보고 정해요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">수익률이 해마다 다르면 복리는 어떻게 계산하나요?</summary><p>해마다 (1 + 그해 수익률)을 차례로 곱해요. 예를 들어 -10%와 +10%면 0.9 × 1.1 = 0.99라서 처음보다 1% 줄어요. 평균 수익률로 곱하면 틀리니 CAGR 편의 방법으로 환산하세요.</p></details>
<details style="margin:10px 0;"><summary style="cursor:pointer;font-weight:bold;">표의 금액은 실제로 받는 돈과 같은가요?</summary><p>아니에요. 표는 세금과 수수료를 빼기 전 계산값이에요. 이자·배당에 붙는 세금은 상품과 계좌에 따라 달라서 국세청 안내를 따로 확인해야 해요.</p></details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (기준일 2026년 10월, 복리는 기관이 수치를 공표하는 지표가 아니라 수학적 정의이며 아래 자료는 공식 교차 확인용입니다):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://eiec.kdi.re.kr/material/wordDic.do" target="_blank" rel="noopener">KDI 경제교육·정보센터 - 시사용어사전</a></li>
    <li><a href="https://kbthink.com/saving-guide/simple-vs-compound.html" target="_blank" rel="noopener">KB Think - 단리, 복리 차이, 계산법 비교</a></li>
    <li><a href="https://www.tossbank.com/articles/simple-compound-interest" target="_blank" rel="noopener">토스뱅크 - 단리와 복리</a></li>
    <li><a href="https://kbthink.com/dictionary/view.html?dictId=KED-00015893" target="_blank" rel="noopener">KB Think 경제용어사전 복리</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#888;margin-top:16px;">이 글은 복리 계산 방법을 알려 드리는 정보성 글이에요. 특정 상품이나 종목을 사거나 팔라고 권하지 않으며, 본문의 금액은 전부 가상 계산값이에요. 투자 판단과 그 결과는 투자자 본인의 몫이고, 이율과 약관은 바뀔 수 있으니 가입 전 원문을 확인해 주세요.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "복리 계산 공식과 단리 월복리 비교",
  "description": "복리 계산 공식을 4단계로 풀고 단리와의 기간별 차이, 월복리와 연복리 차이, 72법칙 오차, 적립식 계산을 표로 정리했습니다.",
  "author": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "publisher": {
    "@type": "Person",
    "name": "센시티브보스"
  },
  "datePublished": "2026-10-02",
  "dateModified": "2026-10-02",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/compound-interest-formula-simple-monthly"
  },
  "image": "https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/compound-interest-formula-simple-monthly-1.png"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "복리 계산기 없이 암산으로 대충 알 수 있나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "72법칙이 있어요. 72를 연 이율(%)로 나누면 원금이 2배 되는 햇수가 나와요. 연 6%면 12년이고, 정확한 계산은 11.90년이라 거의 같아요."
      }
    },
    {
      "@type": "Question",
      "name": "복리 계산 공식에서 n은 무엇인가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1년에 이자가 붙는 횟수예요. 연복리는 1, 반기는 2, 분기는 4, 월복리는 12예요. 상품 설명서의 이자 계산 방식을 보고 정해요."
      }
    },
    {
      "@type": "Question",
      "name": "수익률이 해마다 다르면 복리는 어떻게 계산하나요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "해마다 (1 + 그해 수익률)을 차례로 곱해요. 예를 들어 -10%와 +10%면 0.9 × 1.1 = 0.99라서 처음보다 1% 줄어요. 평균 수익률로 곱하면 틀리니 CAGR 편의 방법으로 환산하세요."
      }
    },
    {
      "@type": "Question",
      "name": "표의 금액은 실제로 받는 돈과 같은가요?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아니에요. 표는 세금과 수수료를 빼기 전 계산값이에요. 이자·배당에 붙는 세금은 상품과 계좌에 따라 달라서 국세청 안내를 따로 확인해야 해요."
      }
    }
  ]
}
</script>
