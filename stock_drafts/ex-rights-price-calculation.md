---
keyword: 권리락
title: 권리락 기준가 계산 방법
slug: ex-rights-price-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1000 (PC 310 / 모바일 690, 2026-09-17 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요 — 2026-09-17 배치 check-keywords.yml 실측, stock_beginner_series.json backlog.verified 기록)
serp_check: |
  [게이트2 v3 판정 2026-09-17 — 통과]
  WebSearch "권리락 뜻 2026" + "권리락 매매기준일 주가 조정" + "권리락일 확인방법 주식" 상위 종합:
  brunch.co.kr(개인 브런치) / infobaksa.com(개인/소규모 블로그, ×2) / eom.co.kr(개인
  콘텐츠 사이트) / orangeboard.co.kr(개인 콘텐츠 플랫폼) / stockplus.com(핀테크 콘텐츠) /
  m.cafe.daum.net(커뮤니티 카페) / kbthink.com(KB 금융 공식) / mofe.go.kr(기획재정부
  시사경제용어사전, 공식, ×2) / 아주경제·네이트뉴스(언론) / dbpia.co.kr·e-kjfs.org(학술논문)
  1) 진입 여지 — 있음. brunch.co.kr·infobaksa.com·eom.co.kr·orangeboard.co.kr·다음카페
     등 개인/소규모 콘텐츠가 다수 상위 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("권리락이 뭔지, 왜 주가가 떨어지는지, 어떻게 계산하는지").
     환율조회·계산기 실행처럼 도구 실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 대부분이 "권리락=신주인수권 상실"이라는 정의와 "주가가
     떨어진다"는 결과까지만 다루고, 실제 숫자를 대입한 기준가 계산 예시나 배당락과의
     조정방식 차이(현금배당은 거래소가 인위조정하지 않는다는 1998년 이후 규정)까지 다루는
     글은 상위 결과에서 확인하지 못했다. 정보이득 여지 뚜렷함.
  → 탈락조건 1·2 미해당, 탈락조건 3은 계산 예시·배당락 비교로 상쇄해 통과.
unique_asset: |
  (a) 유상증자·무상증자 각각의 이론권리락주가 공식을 실제 숫자(기준주가 10,000원 기준)를
      대입한 계산 예시 표로 구체화. 상위 글 대부분이 "공급이 늘어 주가가 떨어진다"는
      정성적 설명에 그치고, 공식에 숫자를 대입한 계산 과정을 보여주는 글은 확인하지 못했다.
  (b) 권리락(유·무상증자)과 배당락(현금배당)의 기준가 조정방식 차이 — 권리락은 한국거래소가
      공식을 적용해 기준가격 자체를 직접 조정하지만, 현금배당의 배당락은 1998년 7월
      "현금배당락조치" 폐지 이후 거래소가 기준가를 인위적으로 조정하지 않고 시장에서
      자율적으로 반영된다는 점(dbpia.co.kr 학술논문으로 확인). 두 개념을 같은 "가격이
      떨어지는 날"로 뭉뚱그리는 상위 글과 달리 조정 방식 자체가 다르다는 것을 비교표로
      정리했다.
primary_source: |
  1차 시도: 한국거래소 업무규정(regulation.krx.co.kr) 기준가격 산출방법 페이지 WebFetch 1회
  시도 → EGRESS_BLOCKED(2026-09-17). 대조군으로 무관한 도메인(www.google.com)에도 1회
  추가 시도했으나 동일하게 EGRESS_BLOCKED로 확인돼 이번 세션의 전면 차단으로 판단했다
  (RULES.md 누적 기록 패턴과 일치, 그 이상 재시도하지 않음).
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다.
  - 이론권리락주가 공식(유상증자: [기준주가+(발행가×증자비율)]/(1+증자비율), 무상증자:
    기준주가/(1+증자비율))은 기획재정부 시사경제용어사전(mofe.go.kr, 정부기관), 한국증권
    학회지 논문(e-kjfs.org, 학술기관), 삼성증권 Compliance Note(samsungpop.com, 금융사
    리서치), 미래에셋증권 용어사전(securities.miraeasset.com), KB(kbthink.com), 오렌지보드
    (orangeboard.co.kr, 개인 콘텐츠) 등 6곳 이상에서 표현만 다를 뿐(주식수 기준 표기와
    비율 기준 표기는 수학적으로 동일) 충돌 없이 일치했다.
  - 현금배당 배당락 시 기준가 인위조정을 하지 않는다는 사실(1998년 7월 현금배당락조치
    폐지)은 DBpia 학술논문("현금배당락조치 폐지 이후 배당락일의 주가행태")으로 확인했다.
  - 위 수치는 세율·공제한도·과세표준처럼 이 프로젝트가 과거 오류를 잡아낸 유형의 숫자가
    아니라, 여러 독립 출처(정부·학술·금융사)가 동일한 산식으로 수렴하는 계산 공식이라
    교차검증으로 진행해도 되는 유형으로 판단했다. 특정 종목의 실제 기준가격 수치는
    본문에서 임의로 만들지 않고, 계산 예시는 가상의 기준주가(10,000원)를 명시해 예시임을
    분명히 했다.
기준일: 2026-09-17 (WebSearch 확인일)
tags: 권리락, 유상증자, 무상증자, 기준가격, 배당락, 신주배정, 주식초보, 재테크초보, 권리락계산법
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-17).
  게이트1: 네이버 키워드도구 실측 1,000회(2026-09-17 배치, backlog.verified 기록 — 일반
  주제 기준 500회 이상). 같은 배치에서 "단순 순서 대기"로 분류된 항목(권리락 1,000회,
  배당수익률 860회) 중 최고 검색량이라 이번 편으로 채택했다. 배당기준일(1,090회)·
  미수거래(970회)는 검색량은 더 높지만 각각 16편·21편과 카니벌라이제이션 점검이
  선행돼야 하는 항목이라 이번 편 후보에서 제외했다.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그 진입 여지 있고, 실제 계산
  예시·배당락과의 조정방식 차이를 다루는 글이 상위 결과에 없어 정보이득 여지 있음.
  게이트3: 실제 숫자를 대입한 계산 예시(유상증자·무상증자 각 1건) + 배당락과의 조정방식
  차이(1998년 현금배당락조치 폐지 근거)로 정보이득 확보.
  게이트4: regulation.krx.co.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군(google.com)도
  차단돼 세션 전면 차단 확인 후 RULES.md 2026-09-12 기준에 따라 교차검증 진행 — 계산
  공식은 정부·학술·대형금융사 등 6곳 이상이 동일하게 수렴, 배당락 비교 근거는 학술논문으로
  확인.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 1,000회(일반 주제 기준 500회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은 계산 예시·
  배당락 비교 정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 실제 숫자를 대입한 이론권리락주가 계산 예시(유상증자·무상증자)와 배당락
  조정방식 차이로 상위 결과가 다루지 않는 각도를 확보했다.
  게이트4 — regulation.krx.co.kr 직접 열람은 막혔고(대조군 google.com도 차단, 세션 전면
  차단), 계산 공식은 정부·학술·대형금융사 등 6곳 이상 독립 출처로 교차검증, 배당락 비교
  사실은 학술논문(DBpia)으로 확인해 진행했다. 본문의 계산 예시는 가상의 기준주가를 명시해
  실제 종목 수치처럼 오인되지 않게 했다.
  카니벌라이제이션 점검 — 16편(배당락일 매수 마감일 계산법)은 배당 관련 배당기준일·
  배당락일 매수 타이밍을 다루고, 이번 편은 유상증자·무상증자로 인한 권리락 기준가 계산을
  다뤄 검색 의도와 핵심 내용이 겹치지 않는다(4번째 H2에서 오히려 두 개념의 차이를 명시적
  으로 비교해 상호 참조가 되도록 했다). 1~45편 어디에도 권리락 기준가 계산 공식을 다룬
  글은 없다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 한국거래소 KIND 안내 문장과 하단 참고
  출처 목록 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow
  미부착. 출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "권리락 기준가 계산 방법" 12자(공백 포함)·금지어 없음·조사·접속사 없음. 슬러그
  영문 소문자+하이픈 4단어(ex-rights-price-calculation). 인트로 문단 최상단 배치. 표는
  thead/tbody 시맨틱 사용. 기준일 명시. FAQ 6개와 JSON-LD 1:1 일치. 종목·상품 추천
  표현, 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 정부·학술·대형금융사 등 6곳 이상 교차검증으로
  대체, 한계는 본문·출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-17</p>

<p><mark>유상증자나 무상증자를 결정한 종목은 그 다음 날부터 주가가 정해진 계산식대로 인위적으로 낮아지는데, 이를 권리락이라고 합니다.</mark> 왜 떨어지는지, 실제로 얼마나 떨어지는지를 계산 공식과 숫자 예시로 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>권리락은 <b>유상증자·무상증자로 신주를 받을 권리가 사라지는 것</b>을 뜻합니다.</li>
    <li>한국거래소가 <mark>정해진 공식으로 기준가격을 직접 낮춰</mark> 형평성을 맞춥니다.</li>
    <li>무상증자 1:1이면 <b>주가가 이론상 절반</b>이 됩니다(기준주가 ÷ 2).</li>
    <li>현금배당의 배당락은 권리락과 달리 <b>거래소가 기준가를 인위조정하지 않습니다.</b></li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>권리락이 뭔가요</li>
  <li>권리락일에는 왜 주가가 인위적으로 떨어지나요</li>
  <li>권리락 기준가는 어떻게 계산하나요</li>
  <li>권리락과 배당락은 뭐가 다른가요</li>
  <li>내가 가진 종목의 권리락 기준가는 어디서 확인하나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">권리락이 뭔가요</h2>

<p>권리락(權利落)은 회사가 유상증자나 무상증자를 할 때, 신주를 배정받을 자격이 있는 기준일이 지나 그 권리가 사라진 상태로 주식이 거래되는 것을 말합니다. 기준일까지 주식을 보유해야 신주를 받을 수 있고, 그다음 날부터는 같은 주식을 사도 신주를 받지 못합니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">권리락일이 되면 한국거래소가 신주인수권의 가치만큼 그 종목의 기준가격을 직접 낮춰서 거래를 시작시킵니다.</span> 즉 전날 종가에서 그냥 시작하는 게 아니라, 계산식으로 산출한 조정된 가격에서 하루를 시작하는 것입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">권리락일에는 왜 주가가 인위적으로 떨어지나요</h2>

<p>유상증자든 무상증자든 발행주식수가 늘어나면 회사 전체의 가치는 그대로인데 주식 수만 늘어나는 셈입니다. <b>신주를 받을 권리가 있던 기존 주주와, 권리락 이후에 산 새 주주 사이의 형평성을 맞추기 위해</b> 거래소가 기준가격을 낮춰서 조정합니다.</p>

<p>조정하지 않으면 권리락 전날 주식을 판 사람은 신주 가치만큼 손해를 보고, 권리락 이후 산 사람은 상대적으로 비싸게 사는 셈이 되기 때문입니다. <mark>이 조정은 회사의 실적이나 가치가 나빠져서가 아니라, 순전히 주식 수가 늘어나는 데 따른 산술적 조정</mark>입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">권리락 기준가는 어떻게 계산하나요</h2>

<p>계산식은 유상증자와 무상증자가 다릅니다. 유상증자는 신주를 발행가에 사는 조건이 붙어 있어 발행가를 반영하고, 무상증자는 주주가 돈을 내지 않고 받으므로 증자비율만 반영합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산식</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">예시 값</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">계산 결과</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">유상증자</td>
      <td style="border:1px solid #ddd;padding:8px;">[기준주가+(발행가×증자비율)] ÷ (1+증자비율)</td>
      <td style="border:1px solid #ddd;padding:8px;">기준주가 10,000원 / 발행가 8,000원 / 증자비율 20%</td>
      <td style="border:1px solid #ddd;padding:8px;">(10,000+1,600)÷1.2 ≈ <mark>9,667원</mark></td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">무상증자</td>
      <td style="border:1px solid #ddd;padding:8px;">기준주가 ÷ (1+증자비율)</td>
      <td style="border:1px solid #ddd;padding:8px;">기준주가 10,000원 / 증자비율 100%(1:1)</td>
      <td style="border:1px solid #ddd;padding:8px;">10,000÷2 = <mark>5,000원</mark></td>
    </tr>
  </tbody>
</table>

<p>위 숫자는 계산 과정을 보여주기 위한 예시일 뿐, 실제 종목의 기준주가·발행가·증자비율이 아닙니다. 실제로는 이렇게 산출된 값을 <b>호가가격단위에 맞춰 반올림·조정</b>한 값이 그날 시초가의 기준이 됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>증자비율이 클수록 조정 폭도 커집니다</b>
  <p style="margin:8px 0 0 0;">무상증자 1:1(증자비율 100%)이면 이론상 주가가 절반이 되고, 2:1(증자비율 200%)이면 3분의 1로 낮아집니다. 회사가치가 줄어든 게 아니라 주식 수만 늘어난 것이므로, 보유 주식 수도 그만큼 늘어나 평가금액 총합은 이론상 동일합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">권리락과 배당락은 뭐가 다른가요</h2>

<p>둘 다 "기준일 다음 날 주가가 떨어진다"는 결과만 보면 비슷해 보이지만, <b>거래소가 기준가를 조정하는지 여부</b>가 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">권리락</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">배당락(현금배당)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">발생 원인</td>
      <td style="border:1px solid #ddd;padding:8px;">유상증자·무상증자로 신주인수권 상실</td>
      <td style="border:1px solid #ddd;padding:8px;">배당기준일 경과로 배당받을 권리 상실</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기준가 조정</td>
      <td style="border:1px solid #ddd;padding:8px;">거래소가 공식으로 기준가격을 직접 조정</td>
      <td style="border:1px solid #ddd;padding:8px;">1998년 7월 이후 인위적 조정 없음(시장 자율 반영)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">거래정지</td>
      <td style="border:1px solid #ddd;padding:8px;">없음(가격만 조정)</td>
      <td style="border:1px solid #ddd;padding:8px;">없음(가격만 반영)</td>
    </tr>
  </tbody>
</table>

<p>즉 권리락은 한국거래소가 계산식을 적용해 그날 시초가의 기준을 직접 낮추는 반면, 배당락은 별도의 공식 없이 시장에서 배당금 가치만큼 자연스럽게 가격이 반영되는 것에 가깝습니다. 배당기준일·배당락일 매수 타이밍을 계산하는 방법은 배당락일 매수 마감일 계산법에서 따로 다루고 있으니 함께 참고하면 좋습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">내가 가진 종목의 권리락 기준가는 어디서 확인하나요</h2>

<p>계산식으로 대략을 가늠할 수는 있지만, 실제 조정된 기준가격은 종목마다 <a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 KIND(상장공시시스템)</a>에 회사별로 "권리락 기준가격 안내" 공시가 올라옵니다. 종목명으로 검색하면 해당 종목의 실제 조정 기준가를 확인할 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">KIND</a> 접속 후 상단 검색창에 보유 종목명 입력</li>
  <li>공시 목록에서 "권리락 기준가격 안내" 항목 확인</li>
  <li>공시 원문에서 증자 비율·발행가·조정 후 기준가격 확인</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">권리락이란 정확히 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">유상증자나 무상증자를 할 때 신주를 배정받을 자격이 있는 기준일이 지나 그 권리가 사라진 상태로 주식이 거래되는 것을 말합니다. 그날부터 한국거래소가 기준가격을 인위적으로 낮춥니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">권리락일에는 주가가 왜 떨어지나요</summary>
  <p style="margin:10px 0 0 0;">신주를 받을 권리가 있던 기존 주주와 권리락 이후 산 새 주주 사이의 형평성을 맞추기 위해, 신주인수권 가치만큼 거래소가 기준가격을 낮추기 때문입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">권리락 기준가는 어떻게 계산하나요</summary>
  <p style="margin:10px 0 0 0;">유상증자는 [기준주가+(발행가×증자비율)]÷(1+증자비율), 무상증자는 기준주가÷(1+증자비율)로 계산합니다. 무상증자 1:1이면 이론상 주가가 절반이 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">권리락과 배당락은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">권리락은 거래소가 공식으로 기준가격을 직접 조정하지만, 현금배당의 배당락은 1998년 7월 이후 거래소가 인위적으로 조정하지 않고 시장에서 자율적으로 가격에 반영됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">권리락이 발생해도 매매정지가 되나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 유상증자·무상증자로 인한 권리락은 기준가격만 조정될 뿐 매매정지는 발생하지 않습니다. 신주권 교체를 위해 거래 자체가 멈추는 액면분할과는 다릅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">내 종목의 실제 권리락 기준가는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">한국거래소 KIND(상장공시시스템)에서 종목명으로 검색하면 "권리락 기준가격 안내" 공시로 실제 조정된 기준가격을 확인할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 KIND(상장공시시스템)</a> - 종목별 권리락 기준가격 안내 공시(자동화 세션에서는 접속이 막혀 직접 확인하지 못함)</li>
    <li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=602" target="_blank" rel="noopener">기획재정부 시사경제용어사전 - 권리락</a></li>
    <li><a href="https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11729858" target="_blank" rel="noopener">DBpia - 현금배당락조치 폐지 이후 배당락일의 주가행태</a></li>
  </ul>
  기준일: 2026-09-17(WebSearch 확인일). 한국거래소 업무규정 원문은 이번 세션 WebFetch가
  차단돼 직접 열람하지 못했고, 이론권리락주가 공식은 정부·학술·대형금융사 등 독립 출처
  6곳 이상의 교차검증으로, 배당락과의 조정방식 차이는 학술논문으로 확인했습니다.
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
  "headline": "권리락 기준가 계산 방법",
  "description": "권리락이 왜 발생하는지, 유상증자·무상증자 기준가격을 실제로 계산하는 방법과 배당락과의 차이를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-17",
  "dateModified": "2026-09-17",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/ex-rights-price-calculation"
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
      "name": "권리락이란 정확히 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "유상증자나 무상증자를 할 때 신주를 배정받을 자격이 있는 기준일이 지나 그 권리가 사라진 상태로 주식이 거래되는 것을 말합니다. 그날부터 한국거래소가 기준가격을 인위적으로 낮춥니다." }
    },
    {
      "@type": "Question",
      "name": "권리락일에는 주가가 왜 떨어지나요",
      "acceptedAnswer": { "@type": "Answer", "text": "신주를 받을 권리가 있던 기존 주주와 권리락 이후 산 새 주주 사이의 형평성을 맞추기 위해, 신주인수권 가치만큼 거래소가 기준가격을 낮추기 때문입니다." }
    },
    {
      "@type": "Question",
      "name": "권리락 기준가는 어떻게 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "유상증자는 [기준주가+(발행가×증자비율)]÷(1+증자비율), 무상증자는 기준주가÷(1+증자비율)로 계산합니다. 무상증자 1:1이면 이론상 주가가 절반이 됩니다." }
    },
    {
      "@type": "Question",
      "name": "권리락과 배당락은 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "권리락은 거래소가 공식으로 기준가격을 직접 조정하지만, 현금배당의 배당락은 1998년 7월 이후 거래소가 인위적으로 조정하지 않고 시장에서 자율적으로 가격에 반영됩니다." }
    },
    {
      "@type": "Question",
      "name": "권리락이 발생해도 매매정지가 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 유상증자·무상증자로 인한 권리락은 기준가격만 조정될 뿐 매매정지는 발생하지 않습니다. 신주권 교체를 위해 거래 자체가 멈추는 액면분할과는 다릅니다." }
    },
    {
      "@type": "Question",
      "name": "내 종목의 실제 권리락 기준가는 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "한국거래소 KIND(상장공시시스템)에서 종목명으로 검색하면 \"권리락 기준가격 안내\" 공시로 실제 조정된 기준가격을 확인할 수 있습니다." }
    }
  ]
}
</script>
