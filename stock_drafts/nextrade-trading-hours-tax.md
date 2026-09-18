---
keyword: 넥스트레이드
title: 넥스트레이드 뜻과 거래시간 세금 차이
slug: nextrade-trading-hours-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 12020 (PC 3830 / 모바일 8190, 2026-09-18 실측)
gate1_pass: true (일반 주제 기준 월 500 이상, 시리즈 내 최고 수준의 검색량)
serp_check: |
  [게이트2 v3 판정 2026-09-18 — 통과]
  WebSearch "넥스트레이드"(단독) + "넥스트레이드 뜻 거래시간 수수료" + "넥스트레이드 스마트주문라우팅
  SOR 체결가격 세금" + "넥스트레이드 상장종목 수 확대" 상위 종합:
  thevc.kr(스타트업 정보 매체, 소규모) / nextrade.co.kr(넥스트레이드 공식, ×2) /
  bnkfn.co.kr(BNK투자증권 공식) / securities.miraeasset.com(미래에셋증권 공식) /
  shinhangroup.com(신한금융그룹 콘텐츠) / kbcapital.co.kr(KB캐피탈 공식) /
  youtube.com(개인 크리에이터 영상) / namu.wiki(백과) / iprovest.com(소규모 IT업체 안내) /
  myasset.com(유안타증권 공식, ×2) / open.shinhansec.com(신한투자증권 공식) /
  daolsecurities.com(다올투자증권 공식) / kiwoom PDF(키움증권 공식) /
  moneyinsight1000.com(개인·소규모 블로그) / mettafriend.com(개인 블로그) /
  asiae.co.kr·fntimes.com·news.nate.com·zum뉴스(언론사 다수)
  1) 진입 여지 — 얇지만 있음. thevc.kr(소규모 전문매체), 개인 유튜브 크리에이터,
     moneyinsight1000.com·mettafriend.com 같은 개인 블로그가 상위에 실제로 진입해
     "하나도 없음"에는 해당하지 않는다. 다만 증권사 공식 콘텐츠 비중이 높은 편이라
     경쟁이 센 키워드로 분류한다.
  2) 검색 의도 — 정보 탐색형(뜻·거래시간·세금 확인)이 지배적이다. 조회·계산기 실행이
     목적인 키워드가 아니다.
  3) 답 완결 여부 — 부분적. 상위 결과 대부분이 "거래시간이 늘어난다", "수수료가
     싸다"는 개념 소개에 그치고, ① 정확한 대상 종목 수(700개, 코스피375/코스닥325)와
     분기별 변경 여부 ② 세금이 KRX와 동일한지 ③ "수수료가 싸다"는 것이 증권사가 내는
     도매 수수료이지 투자자의 위탁수수료가 아니라는 구분 ④ 프리·애프터마켓은 지정가만
     가능하다는 실무 제약을 한 곳에서 엮어 설명하는 글은 확인하지 못했다.
  → 탈락조건 1·2 미해당, 탈락조건 3은 위 4가지 정보이득으로 상쇄해 통과.
unique_asset: |
  "거래시간이 길어졌다"는 소개에 그치지 않고 실전에서 헷갈리는 지점을 계산·비교로 정리했다.
  - 프리마켓(08:00~08:50)·정규시장(09:00:30~15:20)·애프터마켓(15:30~20:00) 3구간과
    그 사이 두 번의 휴장 구간(08:50~09:00:30, 15:20~15:30)을 표로 정리하고, 프리·
    애프터마켓은 지정가만 가능하다는 KRX 시간외거래와 다른 제약을 명시했다.
  - "넥스트레이드가 수수료 20~40% 싸다"는 정보는 사실이지만 증권사가 거래소에 내는
    도매 수수료 이야기이지 투자자의 위탁수수료가 자동으로 낮아진다는 뜻이 아니라는
    오해를 바로잡았다.
  - 증권거래세는 체결 시장과 무관하게 KRX와 완전히 동일한 세율(코스피 0.20%, 코스닥
    0.20%, 코넥스 0.10%)이 적용된다는 것을 9편에서 확정한 법령 수치로 재확인하고,
    2025년 3월 개장 초기 있었던 세액 산정 오차 보도 사례도 투명하게 소개했다.
  - 2026년 1분기 기준 거래대상이 700개 종목(코스피200·코스닥150 지수 구성종목
    350개 + 시가총액 상위 비지수 종목 350개)으로 한정되고 분기마다 재조정된다는
    구체적 숫자를 제시해, "내 종목도 되겠지"라는 막연한 가정을 바로잡았다.
primary_source: |
  1차 시도: 넥스트레이드 공식 사이트(nextrade.co.kr/transactionSys/content.do) WebFetch
  1회 시도 → EGRESS_BLOCKED(2026-09-18). 추가로 신한투자증권 NXT 안내 페이지
  (open.shinhansec.com)도 1회 시도했으나 동일하게 EGRESS_BLOCKED로 확인돼 이번 세션의
  일반적 차단 패턴과 일치한다고 판단, 그 이상 반복 시도하지 않았다.
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로
  진행했다.
  - 거래시간 구간(프리 08:00~08:50/정규 09:00:30~15:20/애프터 15:30~20:00)과 휴장
    구간, 지정가 전용 여부는 서로 무관한 독립 출처 5곳 이상(유안타증권·신한투자증권·
    키움증권·미래에셋증권 공식 안내자료, 개인 블로그 mettafriend.com)이 충돌 없이
    일치했다.
  - SOR(스마트주문라우팅)이 시장 미지정 시 자동으로 유리한 시장에 배분한다는 점,
    매매체결수수료가 KRX보다 20~40% 낮다는 점은 유안타증권 최선집행기준 설명서(공식
    금융소비자보호 심사필 문서)와 신한투자증권 공식 안내가 일치했다.
  - 2026년 1분기 대상종목 700개(코스피375/코스닥325, 지수 350+비지수 350) 확대는
    아시아경제·한국금융신문·네이트뉴스 등 언론사 3곳 이상이 동일 수치로 보도해
    교차검증됐다.
  - 2025년 3월 개장 초기 증권거래세 산정 오차 사례는 zum뉴스 보도를 근거로 했고,
    "투자자 피해 없음"이라는 결론까지 함께 보도된 내용을 그대로 반영했다.
  - 증권거래세 세율(코스피 0.20%/코스닥 0.20%/코넥스 0.10%) 자체는 신규 확인이 아니라
    9편(증권거래세 세율 2026, securities-transaction-tax-rate)에서 이미 법령 원문
    (농어촌특별세법·증권거래세법 시행령)으로 확정한 수치를 그대로 재사용했다.
  - 위 항목들은 세율·공제한도처럼 이 프로젝트가 과거 오류를 잡아낸 유형의 숫자가
    아니라 제도 운영 현황에 대한 사실관계이고, 다수 독립 출처(언론사 포함)가 충돌 없이
    일치해 교차검증으로 진행해도 되는 유형으로 판단했다.
기준일: 2026-09-18 (WebSearch 확인일)
tags: 넥스트레이드, NXT, 대체거래소, 주식거래시간, 스마트주문라우팅, 증권거래세, 주식초보, 재테크초보, ATS
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-18).
  게이트1: 네이버 키워드도구 실측 12,020회 — 이번 배치 후보(ISA 중도해지 530 / 퇴직소득세
  5,030 / 양도소득세 가산세 200 / 넥스트레이드 12,020) 중 카니벌라이제이션 없이 가장
  검색량이 높아 채택. 나머지 PASS 후보는 backlog에 기록.
  게이트2: v3 기준 통과(serp_check 참조) — 증권사 공식 콘텐츠 비중이 높아 경쟁이 센
  편이지만 개인·소규모 콘텐츠 진입이 있고, 정보이득 4가지(대상종목 수·세금 동일 여부·
  수수료 주체 구분·지정가 제약)로 상쇄.
  게이트3: 거래시간 3구간 표 + 대상종목 700개 구성 + 세금 비교표 + 수수료 오해 정정으로
  정보이득 확보.
  게이트4: nextrade.co.kr·신한투자증권 페이지 WebFetch 각 1회 시도 EGRESS_BLOCKED 확인 후
  RULES.md 2026-09-12 기준에 따라 교차검증 진행 — 거래시간·SOR·수수료는 4개 증권사 공식
  자료로, 대상종목 수는 언론사 3곳 이상으로 교차검증. 세율 자체는 9편 기확정 수치 재사용.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 12,020회(일반 주제 기준 500회 이상, 시리즈 내
  최고 수준).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은 4가지
  정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 거래시간 3구간·휴장구간 표, 세금 비교표, 대상종목 700개 구성 수치,
  "수수료가 싸다"는 통념의 정정까지 상위 결과가 다루지 않는 각도를 확보했다.
  게이트4 — nextrade.co.kr·신한투자증권 안내 페이지 직접 열람은 막혔고(각 1회 시도 후
  중단), 거래시간·SOR·수수료는 증권사 공식자료 4곳 이상, 대상종목 수는 언론사 3곳
  이상으로 교차검증했다. 세율 자체는 9편에서 이미 확정한 법령 수치를 재사용했다.
  카니벌라이제이션 점검 — 1~48편 어디에도 넥스트레이드(대체거래소·NXT)를 다룬 글이
  없다. 9편(증권거래세 세율 2026)은 세율 산정 근거가 중심이라 이 글과 검색 의도가
  겹치지 않으며, 세율 부분만 내부 링크로 연결하고 본문에서 재도출하지 않았다.
  기관 링크 점검 — 넥스트레이드 공식 사이트 안내 문장과 하단 참고 출처 목록 전부
  target="_blank" rel="noopener"로 링크 처리, 언론사 링크에도 nofollow 미부착(상업
  제휴 링크가 아니므로). 출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "넥스트레이드 뜻과 거래시간 세금 차이" 15자(공백 제외)·금지어 없음. 슬러그 영문
  소문자+하이픈 4단어(nextrade-trading-hours-tax). 인트로 문단 최상단 배치. 표는
  thead/tbody 시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1 일치. 종목·상품 추천 표현,
  단정 표현("반드시","무조건","확실히","보장") 없음. 하단 면책 문구 포함(문구는 표준
  블록과 다르게 새로 작성).
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문에서 "—" 검색 결과 0개 확인.
  "다만"은 본문에 0회(전환어는 "단," 1회만 사용해 반복 자체를 피했다). `<mark>` 총 4개
  (3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을 "🔑 미리 보는 핵심 3가지"로,
  색상도 앰버 계열(#fff4e6/#f5a623)로 바꿔 기존 "📌 핵심만 먼저 보기"+파란색 패턴을
  반복하지 않았다. FAQ 헤딩도 "궁금한 점 살펴보기"로 변경. H2 5개 중 "~나요"로 끝난
  것은 1개뿐(나머지는 서술형). 헤지 표현("~것으로 알려져 있다" 등) 남발 없음, 확정
  사실은 단정형으로 서술.
  종합 판정: 4개 게이트 전부 충족(게이트4는 증권사 공식자료+언론사 교차검증으로 대체,
  한계는 출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-18</p>

<p>넥스트레이드(NXT)는 한국거래소 말고도 주식을 사고팔 수 있는 또 다른 시장으로, 2025년 3월 출범한 국내 최초의 대체거래소입니다. <mark>거래시간이 길어지고 수수료 구조도 달라졌지만, 세금까지 달라지는 것은 아닙니다.</mark> 거래시간, 체결가격, 세금까지 무엇이 같고 무엇이 다른지 정리했습니다.</p>

<div style="background:#fff4e6;border:2px solid #f5a623;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7c4a03;font-size:18px;">🔑 미리 보는 핵심 3가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>거래시간은 <b>프리마켓 08:00~08:50, 정규시장 09:00:30~15:20, 애프터마켓 15:30~20:00</b>로 나뉩니다.</li>
    <li>시장을 따로 지정하지 않으면 증권사 시스템(SOR)이 <b>더 유리한 곳으로 자동 주문</b>합니다.</li>
    <li>증권거래세는 <mark>한국거래소와 완전히 동일한 세율</mark>이 적용됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>넥스트레이드가 뭔가요</li>
  <li>거래시간은 세 구간으로 나뉩니다</li>
  <li>체결가격이 다르게 나오는 이유</li>
  <li>세금은 KRX와 똑같이 적용됩니다</li>
  <li>넥스트레이드 이용 시 확인할 점</li>
  <li>궁금한 점 살펴보기</li>
</ol>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">넥스트레이드가 뭔가요</h2>

<p>넥스트레이드는 한국거래소(KRX)에 상장된 주식을 별도의 시장에서 사고팔 수 있게 해주는 대체거래소(ATS)입니다. 한국금융투자협회와 코스콤, 주요 증권사 등 34개사가 공동 출자해 만들었고 2025년 3월 4일 영업을 시작했습니다.</p>

<p>KRX와 완전히 다른 거래소가 하나 더 생겼다기보다는, <b>같은 주식을 두 시장 중 어디서 체결할지 고를 수 있게 됐다</b>고 이해하면 됩니다. 상장이나 상장폐지 같은 결정은 여전히 KRX가 담당합니다.</p>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">거래시간은 세 구간으로 나뉩니다</h2>

<p>KRX는 오전 9시부터 오후 3시 30분까지만 열리지만, 넥스트레이드는 오전 8시부터 밤 8시까지로 거래 시간이 늘어납니다. 단, 하루 종일 쉬지 않고 거래되는 것은 아닙니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구간</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시간</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">주문 방식</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">프리마켓</td>
      <td style="border:1px solid #ddd;padding:8px;">08:00~08:50</td>
      <td style="border:1px solid #ddd;padding:8px;">지정가만 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">정규(메인)시장</td>
      <td style="border:1px solid #ddd;padding:8px;">09:00:30~15:20</td>
      <td style="border:1px solid #ddd;padding:8px;">시장가·지정가 모두 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">애프터마켓</td>
      <td style="border:1px solid #ddd;padding:8px;">15:30~20:00</td>
      <td style="border:1px solid #ddd;padding:8px;">지정가만 가능</td>
    </tr>
  </tbody>
</table>

<p>08:50부터 09:00:30까지, 15:20부터 15:30까지는 <mark>넥스트레이드에서 매매 자체가 이뤄지지 않는</mark> 휴장 구간입니다. 정규시장이 아닌 프리마켓과 애프터마켓에서는 시장가 주문이 막혀 있다는 점도 KRX 시간외거래와 다른 부분입니다.</p>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">체결가격이 다르게 나오는 이유</h2>

<p>같은 종목이라도 그 순간 KRX와 넥스트레이드의 호가창은 따로 움직입니다. 두 시장에 걸린 주문량이 다르기 때문에 체결 가격이 서로 달라질 수 있습니다.</p>

<p>투자자가 시장을 직접 고르지 않으면, 증권사의 스마트주문라우팅(SOR)이 그 순간 더 유리한 가격의 시장으로 주문을 자동으로 보냅니다. 이 배분 기준을 최선집행기준이라 부르고, 증권사마다 세부 기준이 조금씩 다릅니다.</p>

<ul style="line-height:1.9;">
  <li>정규시장 시간에는 두 시장 모두 거래량이 있어 가격 차이가 크지 않은 편입니다.</li>
  <li>프리마켓과 애프터마켓은 참여자가 적어 <b>같은 시간 KRX 시간외거래보다 가격이 크게 움직일 수 있습니다.</b></li>
  <li>SOR을 쓰더라도 체결을 100% 보장하지는 않으므로, 지정가 주문은 원하는 가격을 직접 넣어야 합니다.</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>수수료가 항상 싸지는 건 아닙니다</b>
  <p style="margin:8px 0 0 0;">넥스트레이드가 증권사에 부과하는 매매체결수수료는 KRX보다 20~40% 낮지만, 이는 증권사가 거래소에 내는 도매 수수료입니다. 투자자가 실제로 내는 위탁수수료는 각 증권사가 별도로 정하므로, 넥스트레이드에서 체결됐다고 자동으로 저렴해지는 것은 아닙니다.</p>
</div>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">세금은 KRX와 똑같이 적용됩니다</h2>

<p>매도할 때 내는 증권거래세는 어느 시장에서 체결됐는지와 관계없이 동일한 세율로 부과됩니다. 코스피 상장주식은 0.20%(증권거래세 0.05%+농어촌특별세 0.15%), 코스닥은 0.20%, 코넥스는 0.10%입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시장</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">합산 세율(KRX·NXT 동일)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스피</td>
      <td style="border:1px solid #ddd;padding:8px;">0.20%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스닥</td>
      <td style="border:1px solid #ddd;padding:8px;">0.20%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코넥스</td>
      <td style="border:1px solid #ddd;padding:8px;">0.10%</td>
    </tr>
  </tbody>
</table>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>세율 계산 근거가 궁금하다면</b>
  <p style="margin:8px 0 0 0;">코스피·코스닥·코넥스 세율이 이렇게 정해진 법적 근거와 연도별 변화는 <a href="https://sensitiveboss3.tistory.com/entry/securities-transaction-tax-rate" target="_blank" rel="noopener">이전 글(증권거래세 세율 2026)</a>에서 법령 원문으로 확인했습니다.</p>
</div>

<p>2025년 3월 개장 초기에는 예탁결제원이 세액을 산정하는 과정에서 같은 투자자·종목·가격의 체결 내역을 합산 처리하다 금액이 미세하게 어긋난 사례가 언론에 보도된 적이 있습니다. 당시 투자자에게 실제 피해는 없었던 것으로 확인됐고, 세율 자체가 달라진 것도 아니었습니다.</p>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">넥스트레이드 이용 시 확인할 점</h2>

<p>넥스트레이드를 쓰기 위해 새 계좌를 만들거나 별도로 신청할 필요는 없습니다. 기존 증권사 계좌에서 시장을 지정하지 않고 주문하면 자동으로 SOR이 작동합니다.</p>

<ul style="line-height:1.9;">
  <li>증권사 앱(MTS)에 처음 로그인할 때 최선집행기준설명서 확인 안내가 뜨는 경우가 많습니다.</li>
  <li>모든 상장주식이 대상은 아닙니다. 2026년 1분기 기준 대상 종목은 <b>700개(코스피 375개, 코스닥 325개)</b>로, 코스피200·코스닥150 지수 구성종목 350개와 시가총액 상위 비지수 종목 350개(각 시장 175개씩)로 채워져 있습니다.</li>
  <li>대상 종목은 분기마다 다시 정해지므로, 지난 분기에 거래됐던 종목이 이번 분기엔 빠질 수 있습니다.</li>
</ul>

<p><mark>내가 가진 종목이 넥스트레이드 대상인지는 증권사 앱의 종목 상세 화면이나 <a href="https://www.nextrade.co.kr/" target="_blank" rel="noopener">넥스트레이드 홈페이지</a>에서 확인할 수 있습니다.</mark> 대상이 아니면 이전처럼 KRX에서만 체결됩니다.</p>

<h2 style="border-left:6px solid #f5a623;padding-left:12px;margin-top:36px;">궁금한 점 살펴보기</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">넥스트레이드에서 체결되면 세금이 더 싸지나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 증권거래세는 KRX와 넥스트레이드 모두 동일한 세율(코스피·코스닥 0.20%, 코넥스 0.10%)이 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">프리마켓이나 애프터마켓에서도 시장가 주문이 되나요</summary>
  <p style="margin:10px 0 0 0;">안 됩니다. 프리마켓(08:00~08:50)과 애프터마켓(15:30~20:00)은 지정가 주문만 가능하고, 시장가 주문은 정규시장(09:00:30~15:20)에서만 낼 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">내 종목이 넥스트레이드 대상인지 어떻게 확인하나요</summary>
  <p style="margin:10px 0 0 0;">증권사 앱의 종목 상세 화면이나 넥스트레이드 홈페이지에서 확인할 수 있습니다. 2026년 1분기 기준 대상은 700개 종목으로 한정돼 있고 분기마다 바뀝니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">넥스트레이드를 이용하려면 계좌를 새로 만들어야 하나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 기존 증권사 계좌 그대로 이용할 수 있고, 시장을 따로 지정하지 않으면 SOR이 자동으로 유리한 시장에 주문을 배분합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">체결 시장을 KRX나 넥스트레이드 중에서 직접 고를 수 있나요</summary>
  <p style="margin:10px 0 0 0;">증권사 앱에서 시장을 직접 지정할 수 있습니다. 지정하지 않으면 SOR이 그 순간 더 유리한 시장으로 자동 배분합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nextrade.co.kr/" target="_blank" rel="noopener">넥스트레이드(NXT)</a> - 공식 소개 페이지</li>
    <li><a href="https://www.fntimes.com/html/view.php?ud=202607101558479863179ad43907_18" target="_blank" rel="noopener">한국금융신문</a> - 넥스트레이드 거래종목 확대 보도</li>
    <li><a href="https://sensitiveboss3.tistory.com/entry/securities-transaction-tax-rate" target="_blank" rel="noopener">증권거래세 세율 2026(이전 글)</a> - 세율 법령 원문 근거</li>
  </ul>
  기준일: 2026-09-18(WebSearch 확인일). 넥스트레이드 공식 사이트(nextrade.co.kr)와 신한투자증권
  안내 페이지는 이번 세션 WebFetch가 모두 막혀 직접 열람하지 못했고, 거래시간·대상종목 수·
  세금 적용 방식은 증권사 공식 자료와 언론 보도 등 독립 출처 5곳 이상이 일치하는 것으로
  교차검증했습니다. 증권거래세 세율은 9편에서 법령 원문으로 이미 확정한 수치를 재사용했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 넥스트레이드라는 거래 방식을 이해하는 데 도움을 드리려는 정보 제공용 글입니다.
특정 종목이나 상품의 매수매도를 권하지 않으며, 투자 판단과 그 결과는 투자자 본인의
책임입니다. 거래 제도와 세율은 이후 바뀔 수 있으니 최신 내용은 원출처에서 다시
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "넥스트레이드 뜻과 거래시간 세금 차이",
  "description": "넥스트레이드(NXT)의 거래시간 3구간, 체결가격이 KRX와 달라지는 이유(SOR), 증권거래세가 동일하게 적용되는지, 대상 종목 700개 구성을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-18",
  "dateModified": "2026-09-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/nextrade-trading-hours-tax"
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
      "name": "넥스트레이드에서 체결되면 세금이 더 싸지나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 증권거래세는 KRX와 넥스트레이드 모두 동일한 세율(코스피·코스닥 0.20%, 코넥스 0.10%)이 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "프리마켓이나 애프터마켓에서도 시장가 주문이 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "안 됩니다. 프리마켓(08:00~08:50)과 애프터마켓(15:30~20:00)은 지정가 주문만 가능하고, 시장가 주문은 정규시장(09:00:30~15:20)에서만 낼 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "내 종목이 넥스트레이드 대상인지 어떻게 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권사 앱의 종목 상세 화면이나 넥스트레이드 홈페이지에서 확인할 수 있습니다. 2026년 1분기 기준 대상은 700개 종목으로 한정돼 있고 분기마다 바뀝니다." }
    },
    {
      "@type": "Question",
      "name": "넥스트레이드를 이용하려면 계좌를 새로 만들어야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 기존 증권사 계좌 그대로 이용할 수 있고, 시장을 따로 지정하지 않으면 SOR이 자동으로 유리한 시장에 주문을 배분합니다." }
    },
    {
      "@type": "Question",
      "name": "체결 시장을 KRX나 넥스트레이드 중에서 직접 고를 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권사 앱에서 시장을 직접 지정할 수 있습니다. 지정하지 않으면 SOR이 그 순간 더 유리한 시장으로 자동 배분합니다." }
    }
  ]
}
</script>
