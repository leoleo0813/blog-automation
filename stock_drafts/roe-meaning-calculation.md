---
keyword: ROE 뜻
title: ROE 뜻과 계산 방법
slug: roe-meaning-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 930 (PC 250 / 모바일 680, 2026-09-27 실측)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-27 — 통과]
  WebSearch "ROE 뜻 계산 방법 듀폰분해 자기자본이익률" 상위 결과 종합: truefriend.com
  (한국투자증권 공식)/ko.wikipedia.org·namu.wiki(백과)/stockplus.com(핀테크)/
  plainratio.com·infonararo.info-nararo.com·fnwiki.org·econowide.com·
  ecodemy.cafe24.com(개인·소규모 콘텐츠 다수).
  1) 진입 여지 — 있음. plainratio·infonararo·fnwiki·econowide·ecodemy 등 개인·
     소규모 콘텐츠가 상위 9개 중 5개를 차지한다.
  2) 검색 의도 — "뜻"과 "계산법"을 묻는 개념 탐색형이다. 조회·계산기 실행이
     지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 ROE 정의·계산식(당기순이익÷자기자본)
     까지는 다루지만, 검색 결과 자체가 "듀폰분해에 대한 구체적인 정보는 포함되지
     않았다"고 확인될 만큼 듀폰 3단계 분해나 코리아 밸류업 지수의 ROE 활용 기준을
     다룬 글은 확인되지 않았다. 이 두 각도가 정보이득이다.
  → 탈락조건 1~3 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) ROE = 당기순이익 ÷ 자기자본 계산 공식과 가상 숫자 예시(자기자본 1,000억 원,
      당기순이익 200억 원 → ROE 20%)를 직접 계산으로 보여준다.
  (b) 듀폰 분해(ROE = 순이익률 × 총자산회전율 × 재무레버리지)를 같은 가상 기업의
      숫자로 실제 도출해, ROE를 한 줄 공식으로만 설명하는 상위 글들과 차별화한다.
      매출 4,000억 원·총자산 2,000억 원인 가상 기업으로 순이익률 5% × 총자산회전율
      2회 × 재무레버리지 2배 = 20%가 직접 계산과 일치함을 보인다.
  (c) 코리아 밸류업 지수가 종목 선정 5단계 스크리닝에서 최근 2년 평균 ROE를
      산업군별 순위비율로 반영한다는, 2026년 현재도 유효한 제도적 활용 사례 —
      상위 검색결과에는 이 연결 지점을 다룬 글이 없었다.
  (d) ROE가 높다고 무조건 좋은 회사가 아닌 이유(부채로 자기자본을 줄여 만든
      ROE) 판별 체크리스트 — 듀폰 분해로 재무레버리지 항을 분리해서 보여준다.
  (e) 업종별로 ROE 수준이 다르다는 점과, 실제 업종별 수치는 한국거래소
      정보데이터시스템에서 확인하도록 안내(자동화 세션은 접속 차단으로 직접 확인
      못함 — 88편 PBR 편과 동일한 처리 방식).
primary_source: |
  ROE 계산 공식과 듀폰 분해식(ROE = 당기순이익/자기자본 = (당기순이익/매출액) ×
  (매출액/총자산) × (총자산/자기자본))은 재무비율의 수학적 항등식으로, 별도의
  기관 확인이 필요한 수치가 아니라 정의상 항상 성립하는 계산이다(88편 PBR=PER×ROE
  관계식과 동일한 처리).
  코리아 밸류업 지수의 ROE 활용 부분은 자동화 세션에서 한국거래소 www.krx.co.kr에
  WebFetch를 1회 시도했으나 EGRESS_BLOCKED로 막혔다. RULES.md 「1차 출처가 막혔을
  때」 기준에 따라 WebSearch로 독립 출처 교차검증을 진행했다. 코리아 밸류업 지수가
  시가총액 상위 400위 이내, 최근 2년 연속 적자가 아닌 기업, 최근 2년 연속 배당
  또는 자사주 소각 기업, PBR 순위 상위 50% 이내 기업을 걸러낸 뒤 최근 2년 평균
  ROE 기준으로 산업군별 순위비율 상위 100종목을 선정한다는 사실은 한국경제
  (hankyung.com)·이투데이(etoday.co.kr)·서울경제(sedaily.com)·MTN뉴스
  (news.mtn.co.kr)·인더스트리뉴스(industrynews.co.kr) 등 5곳 이상 독립 언론이
  핵심 수치에서 충돌 없이 일치했다. 지수 자체는 2024년 9월 24일 한국거래소가
  처음 발표한 완결된 사실이며, 세율·공제한도처럼 매년 바뀌는 유형이 아니므로
  다수 독립 언론 교차검증으로 진행해도 안전하다고 판단했다. 지수 구성 종목의
  평균 PBR·PER·ROE 등 구체 수치는 단일 저자 콘텐츠에서만 확인돼 교차검증 기준을
  충족하지 못해 본문에 넣지 않았다.
기준일: 2026년 9월 기준 (코리아 밸류업 지수 선정 기준은 2026년 9월 시점 공개 자료 기준)
tags: ROE, ROE뜻, 자기자본이익률, ROE계산법, 듀폰분해, PBR, PER, 밸류업지수, 재무레버리지, 주식투자지표
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 930회(일반 주제 기준 500회 이상). 게이트2
  충족 — v3 기준 3개 탈락조건 모두 미해당(개인·소규모 콘텐츠 다수 진입, 개념
  탐색형 의도, 듀폰 분해·밸류업 지수 연결이라는 정보이득 미확보 확인). 게이트3
  충족 — ROE 계산 예시 + 듀폰 3단계 분해 도출 + 코리아 밸류업 지수 ROE 활용
  기준이라는 정보이득. 게이트4 충족 — 계산식은 수학적 항등식이라 기관 확인
  불요, 밸류업 지수 부분은 원문 WebFetch 1회 시도 후 차단을 확인하고 5곳 이상
  독립 언론이 충돌 없이 일치하는 사실만 교차검증으로 확보했다.
capture_guide: ""
self_check: |
  [2026-09-27 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  카니벌라이제이션 점검 — stock_drafts/ 전체를 grep한 결과 ROE를 실제 본문
  주제로 다룬 기존 편은 없었다(bollinger-bands-calculation.md와
  derivatives-capital-gains-tax-calculation.md는 게이트1 검색량 조사 로그에
  "ROE 뜻 계산법"이 후보 키워드로만 언급됐을 뿐 본문 내용은 없음). 88편(PBR 뜻과
  계산 방법)은 PBR=PER×ROE 관계식 안에서 ROE를 한 문장으로만 설명해, 이 글의
  듀폰 분해·밸류업 지수 연결과 검색 의도가 겹치지 않는다.
  YMYL 안전장치 점검 — 특정 종목의 매수·매도 시점이나 목표가를 언급하지 않았다.
  계산 예시는 전부 가상의 수치로만 구성했고, 코리아 밸류업 지수는 이미 발표된
  제도의 선정 기준을 사실 그대로 전달하는 용도로만 썼다.
  기관 링크 점검 — 한국거래소 정보데이터시스템(data.krx.co.kr) 링크 1개와 언론
  보도 링크 1개를 참고 출처 목록에 걸었다.
  제목 "ROE 뜻과 계산 방법" 11자·금지어 없음·조사 최소화.
  슬러그 영문 소문자+하이픈 3단어(roe-meaning-calculation).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—" 검색
  결과 0개 확인. "다만"은 FAQ 1곳에서만 썼고, 본문 전환은 "단,"·"반대로"·"그런데"로
  분산했다. `mark` 태그 총 4개(3~5개 기준 충족). FAQ 6개(직전 88편이 5개였던 것과
  다르게 변화). 핵심 요약 박스 제목을 "🔍 미리 보는 핵심"으로, 색은 포레스트그린
  (#eaf5ec/#2e7d32)으로 최근 게시물(테라코타#c0562f·슬레이트#455a64·브라운
  #8d6e63 등)과 겹치지 않게 골랐다. 목차 제외 본문 H2 6개 중 서술형 4개, 질문형
  2개("ROE가 높으면 무조건 좋은 회사인가요", "ROE는 어디서 확인하나요")로 "~나요"
  편중 없음(6개 중 2개, 33%). FAQ 헤딩도 "자주 묻는 질문" 대신 "더 알아두면
  좋은 것들"로 변형. 헤지 표현("~것으로 알려져 있다" 등)은 쓰지 않고 확정된
  사실은 단정형으로 서술했다. 면책 문구는 88편과 다른 표현으로 새로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-27</p>

<p>ROE는 회사가 주주의 돈(자기자본)으로 얼마나 이익을 냈는지 보여주는 지표입니다. 계산식 자체는 나눗셈 한 번으로 끝나지만, 그 안을 순이익률·자산회전율·재무레버리지 세 조각으로 쪼개 보면 같은 ROE라도 성격이 완전히 다를 수 있습니다. 이 글은 ROE 계산 공식과 듀폰 분해, 코리아 밸류업 지수가 ROE를 어떻게 쓰는지를 정리합니다.</p>

<div style="background:#eaf5ec;border:2px solid #2e7d32;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#1b4d27;font-size:18px;">🔍 미리 보는 핵심</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>ROE는 당기순이익 ÷ 자기자본으로 계산하며, 자기자본을 얼마나 효율적으로 굴렸는지를 보여줍니다.</li>
    <li>같은 ROE도 듀폰 분해로 쪼개면 이익률이 좋아서인지 빚을 많이 써서인지 구분됩니다.</li>
    <li>업종마다 평균 ROE 수준이 달라 단순 비교는 오해를 부를 수 있습니다.</li>
    <li>코리아 밸류업 지수는 종목을 고를 때 최근 2년 평균 ROE를 산업군별로 줄 세워 반영합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ROE 뜻과 계산 공식</li>
  <li>ROE가 높으면 무조건 좋은 회사인가요</li>
  <li>듀폰 분해로 ROE 뜯어보기</li>
  <li>업종별로 ROE 수준이 다릅니다</li>
  <li>코리아 밸류업 지수와 ROE</li>
  <li>ROE는 어디서 확인하나요</li>
  <li>더 알아두면 좋은 것들</li>
</ol>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">ROE 뜻과 계산 공식</h2>

<p>ROE(Return On Equity, 자기자본이익률)는 <mark>회사가 주주의 자본을 이용해 1년 동안 얼마를 벌었는지 비율로 나타낸 지표</mark>입니다. 계산식은 ROE = 당기순이익 ÷ 자기자본 × 100(%)입니다.</p>

<p>예를 들어 자기자본이 1,000억 원이고 당기순이익이 200억 원인 회사라면, ROE는 200 ÷ 1,000 × 100 = 20%가 됩니다. 이 회사는 주주가 맡긴 자본 1,000억 원으로 한 해 동안 200억 원의 이익을 냈다는 뜻입니다.</p>

<ul style="line-height:1.9;">
  <li>자기자본(자본총계) = 자산총계 - 부채총계</li>
  <li>ROE 20% = 자기자본 대비 20%만큼의 이익을 냈다는 뜻</li>
  <li>ROE가 시중 예금·채권 금리보다 낮으면 굳이 그 회사에 자본을 맡길 이유가 약해집니다</li>
</ul>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">ROE가 높으면 무조건 좋은 회사인가요</h2>

<p>아닙니다. ROE가 높다고 반드시 좋은 회사는 아닙니다. 이익을 잘 내서 ROE가 높은 경우도 있지만, 빚을 늘려 자기자본 비중을 줄이는 방식으로도 ROE 숫자는 똑같이 올라갑니다.</p>

<p>자기자본이 작을수록 같은 순이익이라도 나누는 분모가 작아지므로 ROE는 커집니다. 그런데 그 자기자본이 작아진 이유가 부채를 많이 끌어썼기 때문이라면, 겉보기 ROE는 높아도 재무 위험은 함께 커진 상태일 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>ROE 상승이 이익 개선 때문인지, 부채 증가로 자기자본이 줄어서인지 확인합니다.</li>
  <li>부채비율을 함께 확인해 레버리지 수준을 봅니다.</li>
  <li>최근 몇 년간 ROE 추세가 꾸준한지, 특정 해만 튄 것은 아닌지 봅니다.</li>
</ul>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">듀폰 분해로 ROE 뜯어보기</h2>

<p><mark>듀폰 분해는 ROE를 순이익률 × 총자산회전율 × 재무레버리지, 세 항목의 곱으로 나누는 방법</mark>입니다. 이렇게 나누면 ROE가 어디에서 나왔는지 원인을 구분할 수 있습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <p style="margin:8px 0 0 0;">가상의 E기업은 매출액 4,000억 원, 당기순이익 200억 원, 총자산 2,000억 원, 자기자본 1,000억 원이라고 가정합니다.</p>
  <p style="margin:8px 0 0 0;">순이익률 = 당기순이익 ÷ 매출액 = 200 ÷ 4,000 = 5%</p>
  <p style="margin:8px 0 0 0;">총자산회전율 = 매출액 ÷ 총자산 = 4,000 ÷ 2,000 = 2회</p>
  <p style="margin:8px 0 0 0;">재무레버리지 = 총자산 ÷ 자기자본 = 2,000 ÷ 1,000 = 2배</p>
  <p style="margin:8px 0 0 0;">듀폰 분해 ROE = 5% × 2 × 2 = <mark>20%</mark>로, 앞서 직접 계산한 200 ÷ 1,000 = 20%와 정확히 같습니다.</p>
</div>

<p>이 가상 사례에서 재무레버리지를 3배로 바꾸면 자기자본이 더 작아지면서 ROE는 30%까지 뛰어오릅니다. 순이익률과 매출은 그대로인데 빚만 늘려도 ROE 숫자가 커질 수 있다는 뜻입니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">업종별로 ROE 수준이 다릅니다</h2>

<p>업종 특성에 따라 평균 ROE는 크게 갈립니다. 은행·보험처럼 원래 부채(예금·보험부채) 비중이 큰 업종은 재무레버리지가 높아 ROE도 높게 나오는 구조이고, 설비 투자가 많은 제조업은 자기자본 비중이 상대적으로 커 ROE가 낮게 나오는 경우가 흔합니다.</p>

<p>그런데 은행업의 높은 레버리지는 업종 자체의 사업 구조 때문이지 경영을 잘해서만은 아닙니다. 그래서 서로 다른 업종의 ROE를 그대로 비교하면 오해가 생기기 쉽습니다. 같은 업종 안에서 비교하거나, <a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a>의 업종별 투자지표를 참고하는 편이 정확합니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">코리아 밸류업 지수와 ROE</h2>

<p>한국거래소가 2024년 9월 24일 처음 발표한 <mark>코리아 밸류업 지수는 종목 선정 과정에서 최근 2년 평균 ROE를 산업군별 순위비율로 반영</mark>합니다.</p>

<p>구체적으로는 시가총액 상위 400위 이내, 최근 2년 연속 적자가 아닌 기업, 최근 2년 연속 배당 또는 자사주 소각을 실시한 기업, PBR 순위가 상위 50% 이내인 기업을 먼저 거른 뒤, 그 안에서 최근 2년 평균 ROE 기준으로 산업군별 순위비율 상위 기업 100종목을 골라 구성합니다.</p>

<ul style="line-height:1.9;">
  <li>ROE는 단독 기준이 아니라 수익성·주주환원·시장평가 지표 중 하나로 쓰입니다.</li>
  <li>업종별로 따로 순위를 매기기 때문에 은행업과 제조업의 ROE를 직접 비교하지 않습니다.</li>
  <li>지수 편입 자체가 특정 종목의 매수 추천을 뜻하지는 않습니다.</li>
</ul>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">ROE는 어디서 확인하나요</h2>

<p>종목별·업종별 ROE는 <a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템</a>의 투자지표 메뉴에서 무료로 조회할 수 있습니다. 증권사 MTS의 종목 상세 화면이나 재무제표 메뉴에도 대부분 ROE가 함께 표시됩니다.</p>

<h2 style="border-left:6px solid #2e7d32;padding-left:12px;margin-top:36px;">더 알아두면 좋은 것들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ROE와 ROA는 무엇이 다른가요</summary>
  <p style="margin:10px 0 0 0;">ROE는 자기자본 대비 이익을, ROA는 총자산(자기자본+부채) 대비 이익을 봅니다. 부채를 많이 쓰는 회사는 ROE가 ROA보다 크게 벌어집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ROE가 마이너스면 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">당기순손실이 났다는 뜻입니다. 자기자본으로 나누는 분자(순이익) 자체가 음수이므로 ROE도 음수로 표시됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">듀폰 분해를 꼭 직접 계산해야 하나요</summary>
  <p style="margin:10px 0 0 0;">직접 계산하지 않아도 됩니다. 다만 순이익률·총자산회전율·재무레버리지 세 항목을 확인하면 ROE가 어디서 나왔는지 감을 잡을 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ROE는 분기마다 바뀌나요</summary>
  <p style="margin:10px 0 0 0;">네. 당기순이익과 자기자본이 분기·반기 실적 발표마다 갱신되므로 ROE도 그때마다 다시 계산됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코리아 밸류업 지수에 들어가면 주가가 오르나요</summary>
  <p style="margin:10px 0 0 0;">지수 편입 자체가 주가 상승을 보장하지는 않습니다. 수익성·주주환원 기준을 충족한 기업이라는 참고 정보로만 활용하는 편이 안전합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">PBR·PER과 ROE를 같이 봐야 하나요</summary>
  <p style="margin:10px 0 0 0;">네. PBR은 PER과 ROE를 곱한 값(PBR=PER×ROE)이라 세 지표가 서로 연결돼 있어, ROE 하나만으로 판단하기보다 함께 보는 편이 안전합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://data.krx.co.kr" target="_blank" rel="noopener">한국거래소 정보데이터시스템 - 투자지표</a></li>
    <li><a href="https://www.hankyung.com/article/2024092439946" target="_blank" rel="noopener">한국경제 - 코리아 밸류업 지수 선정 기준(주주환원·ROE) 보도</a></li>
  </ul>
  기준일: 2026년 9월 기준. 코리아 밸류업 지수 선정 기준은 2026년 9월 시점 공개 자료를 반영했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 ROE라는 투자지표를 계산하고 해석하는 방법을 설명하는 정보 글로, 특정 종목의 매수나 매도를 권하지 않습니다. 계산에 쓰인 숫자는 이해를 돕기 위해 만든 가상의 사례이며 실제 기업의 재무 수치가 아닙니다. 제도나 지수 구성 기준은 향후 바뀔 수 있으므로 투자 전 최신 공시로 다시 확인하시길 권합니다. 투자로 인한 결과는 투자자 본인이 책임집니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ROE 뜻과 계산 방법",
  "description": "ROE(자기자본이익률)의 뜻과 계산 공식, 순이익률·총자산회전율·재무레버리지로 나누는 듀폰 분해, 업종별 ROE 차이, 코리아 밸류업 지수의 ROE 활용 기준을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-27",
  "dateModified": "2026-09-27",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/roe-meaning-calculation"
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
      "name": "ROE와 ROA는 무엇이 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "ROE는 자기자본 대비 이익을, ROA는 총자산(자기자본+부채) 대비 이익을 봅니다. 부채를 많이 쓰는 회사는 ROE가 ROA보다 크게 벌어집니다." }
    },
    {
      "@type": "Question",
      "name": "ROE가 마이너스면 무슨 뜻인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "당기순손실이 났다는 뜻입니다. 자기자본으로 나누는 분자(순이익) 자체가 음수이므로 ROE도 음수로 표시됩니다." }
    },
    {
      "@type": "Question",
      "name": "듀폰 분해를 꼭 직접 계산해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "직접 계산하지 않아도 됩니다. 다만 순이익률·총자산회전율·재무레버리지 세 항목을 확인하면 ROE가 어디서 나왔는지 감을 잡을 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "ROE는 분기마다 바뀌나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 당기순이익과 자기자본이 분기·반기 실적 발표마다 갱신되므로 ROE도 그때마다 다시 계산됩니다." }
    },
    {
      "@type": "Question",
      "name": "코리아 밸류업 지수에 들어가면 주가가 오르나요",
      "acceptedAnswer": { "@type": "Answer", "text": "지수 편입 자체가 주가 상승을 보장하지는 않습니다. 수익성·주주환원 기준을 충족한 기업이라는 참고 정보로만 활용하는 편이 안전합니다." }
    },
    {
      "@type": "Question",
      "name": "PBR·PER과 ROE를 같이 봐야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. PBR은 PER과 ROE를 곱한 값(PBR=PER×ROE)이라 세 지표가 서로 연결돼 있어, ROE 하나만으로 판단하기보다 함께 보는 편이 안전합니다." }
    }
  ]
}
</script>
