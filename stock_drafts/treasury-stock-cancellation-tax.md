---
keyword: 자사주 소각
title: 자사주 소각 세금 누가 내나
slug: treasury-stock-cancellation-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 10340 (PC 3190 / 모바일 7150)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-18 — 통과]
  WebSearch "자사주 소각 뜻 세금 절차" + "자사주 소각 의제배당 세금 주가영향" + "자사주 의무소각
  상법 개정 2026" 상위 종합:
  help-me.kr(로펌 콘텐츠) / kbthink.com(KB 금융 공식, 사전형) / zuzu.network(스타트업 서비스,
  소규모) / namu.wiki(백과) / taxoffice.co.kr(세무법인, ×2) / gmg-tax.com(세무법인 기고) /
  m.news.nate.com(언론) / keyzard.cc(개인 블로그) / lawtimes.co.kr(법률신문, 법무법인 대륙아주·
  지평 기고 ×2) / moj.go.kr(법무부 공식 가이드) / pwc.com(PwC코리아 회계법인) / taxtimes.co.kr
  (한국세정신문) / shinkim.com(법무법인 신김 뉴스레터) / atlaw.kr(로펌 블로그) / casenote.kr(국세청
  유권해석·판례 데이터베이스, ×4) / watax.kr(개인·소규모 세무 콘텐츠) / blog.mstacc.com(회계법인
  블로그) / tuzaga.com(개인 세무사 블로그, 13편에서도 확인된 소규모 콘텐츠)
  1) 진입 여지 — 있음. zuzu.network·keyzard.cc·watax.kr·tuzaga.com·blog.mstacc.com 등
     개인/소규모 콘텐츠가 상위에 다수 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻이 뭔지, 세금이 있는지" 확인)이 지배적이다. 조회·계산기
     실행이 목적인 키워드가 아니다.
  3) 답 완결 여부 — 부분적. 상위 대부분이 "매각=법인세, 소각=의제배당"이라는 구조까지는
     설명하지만, ① 자사주를 팔지 않고 계속 들고 있는 일반 주주에게는 세금이 없다는 점을
     명확히 못박은 글, ② 2026-02-25 통과·2026-03-06 공포·즉시시행된 자사주 의무소각 상법
     개정(신규취득분 1년 내 소각, 기존보유분 6개월+1년 유예)을 세금 이슈와 엮어 설명한
     글, ③ 의제배당 원천징수 시기가 "소각 결정일"이라는 실무 포인트를 함께 갖춘 글은
     확인하지 못했다.
  → 탈락조건 1·2 미해당, 탈락조건 3은 위 3가지 정보이득으로 상쇄해 통과.
unique_asset: |
  "회사가 자사주를 소각하면 내 세금도 늘어나나" 하는 막연한 불안을 구조로 정리했다.
  - 자사주를 회사에 파는 것(매각)과 회사가 그 주식을 없애는 것(소각)은 별개 절차이고,
    세금이 붙는 지점도 다르다. 회사가 자사주를 제3자에게 되팔면 처분이익에 법인세,
    소각하면 소각대금을 받은 주주 본인에게 의제배당(배당소득세)이 발생한다.
  - 핵심 오해 해소: 자사주를 팔지 않고 계속 들고 있는 일반 주주는 지분율이 늘어나도
    아직 실현된 이익이 아니라서 그 자체로는 세금이 없다. 국세청 유권해석(casenote.kr
    수록)도 시가대로 매입해 소각한 경우 잔여 주주의 지분율 증가를 원칙적으로 의제배당으로
    보지 않는다고 밝히고 있다.
  - 2026-02-25 국회 통과, 2026-03-06 공포와 동시에 시행된 3차 상법 개정으로 자사주
    소각이 의무화됐다: 신규 취득분은 원칙적으로 취득 후 1년 내 소각, 기존 보유분은
    시행일로부터 6개월 준비기간을 거쳐 1년 이내(총 1년 6개월) 처분·소각을 결정해야
    한다. 상장·비상장·벤처기업 구분 없이 전체 회사에 적용되고, 외국인 지분제한 업종은
    3년 유예를 받는다.
  - 예외적으로 의제배당세가 발생하는 경우(회사가 특정 주주와 직접 협의해 비상장주식을
    사들여 소각하는 유상소각·이익소각)와, 상장주식을 시장에서 그냥 매도하는 것(7편에서
    확인한 소액주주 비과세)이 서로 다른 상황이라는 것을 표로 구분했다.
status: drafted
cannibalization_note: |
  1~49편 어디에도 자사주 소각(자기주식 소각)을 다룬 글이 없다. 7편(주식 양도소득세
  대주주 요건)은 상장주식을 시장에서 매도할 때의 대주주 판정이 중심이라 검색 의도가
  겹치지 않고, 소액주주 비과세 부분만 대비 설명으로 인용하며 내부 링크를 걸었다.
draft_path: stock_drafts/treasury-stock-cancellation-tax.md
primary_source: |
  1차 시도: 국세청(nts.go.kr) WebFetch 1회 → EGRESS_BLOCKED(2026-09-18). 추가로 법무부
  「자기주식 소각 의무화 관련 개정 상법 길라잡이」(moj.go.kr) PDF도 1회 시도했으나 동일하게
  EGRESS_BLOCKED로 확인돼 이번 세션 일반 차단 패턴과 일치한다고 판단, 반복 시도하지 않았다.
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다.
  - 2026-02-25 국회 본회의 통과, 2026-03-06 공포·즉시시행이라는 날짜와 신규취득분 1년 내
    소각·기존보유분 6개월+1년(총 1년6개월)·외국인지분제한기업 3년 유예라는 수치는 서로
    무관한 독립 출처 5곳 이상(법률신문 소재 법무법인 대륙아주·지평 기고 2건, PwC코리아,
    법무법인 신김 뉴스레터, 한국세정신문)이 충돌 없이 일치했다.
  - 소득세법 제17조가 "주식의 소각이나 자본의 감소로 주주가 취득하는 금전 등의 가액이
    그 주식 취득에 사용한 금액을 초과하는 금액"을 의제배당으로 규정한다는 점, 그 원천징수
    시기가 "주식의 소각을 결정한 날"이라는 점은 국가법령정보센터 조문 링크와 casenote.kr에
    수록된 국세청 유권해석(서면인터넷방문상담 다수 건)이 일치했다.
  - "매각은 법인세, 소각은 의제배당"이라는 과세 구조 차이는 세무 콘텐츠(watax.kr) 요약과
    casenote.kr 국세청 판례 인용이 서로 다른 사례에서 같은 결론을 반복해 일치했다.
  - "시가대로 매입해 소각하면 잔여 주주 지분율 증가는 원칙적으로 의제배당이 아니다"는
    점은 casenote.kr에 수록된 국세청 서면 질의회신(자기주식 소각으로 잔여주주 지분율
    증가 시 의제배당 여부) 원문 인용을 근거로 했다. 다만 비상장·특수관계자 간 거래처럼
    구체적 사실관계에 따라 예외가 있을 수 있다는 국세청 판단 기준 자체를 본문·주의문구에
    그대로 반영해, 일반화의 한계를 숨기지 않았다.
  - 상법 제341조(자기주식 취득, 재원규제)·제341조의2(특정목적 취득)는 국가법령정보센터
    조문 링크로 존재를 확인했으나 이번 개정으로 신설된 소각 의무 조항 자체의 정확한
    조번호(개정 조문)는 원문 미확보 상태다 - 이 한계를 self_check에 투명하게 남긴다.
  - 배당소득세율(원천징수 15.4%, 2천만원 초과 시 종합과세)은 신규 확인이 아니라 4편·6편
    (dividend-income-tax, financial-income-comprehensive-tax)에서 이미 국세청 원문·법제처
    자료로 확정한 수치를 그대로 재사용했다.
기준일: 2026-09-18 (WebSearch 확인일)
tags: 자사주소각, 자기주식소각, 의제배당, 상법개정, 배당소득세, 주식초보, 재테크초보, 자사주매입
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-18).
  게이트1: 네이버 키워드도구 실측 10,340회 — 이번 배치 후보(변동성완화장치 300 FAIL /
  스팩 3,500 PASS / 전환사채 2,780 PASS / 유상감자 세금 20 FAIL / 실질주주 20 FAIL /
  자사주 소각 10,340 PASS / 신용거래융자 이자율 20 FAIL / 대차거래 530 PASS) 중
  카니벌라이제이션 없이 가장 검색량이 높아 채택. 스팩·전환사채·대차거래는 backlog에 PASS
  후보로 기록.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 세무 콘텐츠 진입 확인, 정보이득
  3가지(잔여주주 비과세 명문화·2026 의무소각 제도·원천징수 시기)로 탈락조건3 상쇄.
  게이트3: 매각/소각 과세구조 비교표 + 잔여주주 비과세 근거 + 의무소각 시행일정표 +
  일반 시장매도(소액주주 비과세)와의 구분표로 정보이득 확보.
  게이트4: nts.go.kr·moj.go.kr 각 1회 시도 EGRESS_BLOCKED 확인 후 RULES.md 2026-09-12
  기준에 따라 교차검증 진행 — 상법개정 일정은 법무법인·회계법인·세정전문매체 5곳 이상,
  의제배당 법리는 소득세법 제17조 조문+국세청 유권해석(casenote.kr)으로 확인. 개정 상법의
  정확한 신설 조번호는 원문 미확보로 self_check·본문에 한계를 투명 공개.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 10,340회(일반 주제 기준 500회 이상, 이번 배치
  최고 검색량).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은 3가지
  정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 매각/소각 과세구조 비교표, 잔여주주 비과세 근거, 2026 의무소각 시행
  일정표, 일반 시장매도(소액주주 비과세)와 유상소각(의제배당)의 구분표까지 상위 결과가
  한 곳에 모아두지 않은 정보를 엮었다.
  게이트4 — nts.go.kr·moj.go.kr 직접 열람은 막혔고(각 1회 시도 후 중단), 상법개정 일정은
  법무법인·회계법인·세정전문매체 5곳 이상, 의제배당 법리는 소득세법 제17조 조문과 국세청
  유권해석(casenote.kr)으로 교차검증했다. 개정 상법의 정확한 신설 조번호(예: 제343조
  개정 여부)는 원문을 확보하지 못해 본문에서 조번호를 특정하지 않고 "3차 상법 개정"으로만
  표기했다 - 이는 숨기지 않고 참고 출처 문구에도 명시했다.
  카니벌라이제이션 점검 — 1~49편 어디에도 자사주 소각을 다룬 글이 없다. 7편(주식
  양도소득세 대주주 요건)은 시장 매도 시 대주주 판정이 중심이라 검색 의도가 겹치지
  않으며, 소액주주 비과세 부분만 대비 설명으로 인용하고 재도출하지 않았다.
  기관 링크 점검 — 국가법령정보센터·법률신문·casenote.kr 링크 전부 target="_blank"
  rel="noopener" 처리, 정부·언론 링크에 nofollow 미부착(상업 제휴 링크가 아니므로).
  출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "자사주 소각 세금 누가 내나" 13자·금지어 없음. 슬러그 영문 소문자+하이픈
  4단어(treasury-stock-cancellation-tax). 인트로 문단 최상단 배치. 표는 thead/tbody
  시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1 일치. 종목·상품 추천 표현, 단정
  표현("반드시","무조건","확실히","보장") 없음. 하단 면책 문구 포함(표준 블록과 다르게
  새로 작성).
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문에서 "—" 검색 결과 0개 확인.
  "다만"은 본문에 0회 사용(전환어는 "단," 1회, "그런데" 2회로 분산). `<mark>` 총 3개
  (3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을 "✅ 오늘 확인할 3가지"로,
  색상도 그린 계열(#eefbf3/#16a34a)로 바꿔 기존 파란색·앰버 패턴을 반복하지 않았다. FAQ
  헤딩도 "이것도 궁금하셨나요"로 변경. 목차 제외 H2 6개(FAQ 헤딩 포함) 중 "~나요"류로
  끝난 것은 2개뿐("자사주 소각이 뭔가요", FAQ 헤딩) 이고 나머지 4개는 서술형이라 절반
  이상 서술형 기준을 충족한다. 헤지 표현("~것으로 알려져 있다" 등) 남발 없음, 단 국세청
  판단이 사안별로
  갈릴 수 있는 부분은 실제로 단정할 수 없으므로 그 한계 자체를 본문에 명시했다(헤지가
  아니라 사실 반영).
  종합 판정: 4개 게이트 전부 충족(게이트4는 법무법인·회계법인·세정매체+국세청 유권해석
  교차검증으로 대체, 한계는 출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-18</p>

<p>회사가 자사주를 소각해도 <mark>계속 주식을 들고 있는 일반 주주에게는 원칙적으로 세금이 붙지 않습니다.</mark> 세금이 발생하는 쪽은 회사에 주식을 직접 팔아 소각대금을 받은 주주이거나, 처분 방식에 따라 회사(법인) 자신입니다. 매각과 소각의 과세 구조 차이, 2026년부터 의무화된 소각 제도까지 정리했습니다.</p>

<div style="background:#eefbf3;border:2px solid #16a34a;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#14532d;font-size:18px;">✅ 오늘 확인할 3가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>자사주를 <b>제3자에게 되팔면 법인세</b>, <b>소각하면 소각대금을 받은 주주에게 배당소득세</b>가 붙습니다.</li>
    <li>주식을 계속 보유한 일반 주주는 지분율이 늘어나도 <mark>과세 대상이 아닙니다.</mark></li>
    <li>2026년 3월 상법 개정으로 자사주는 <b>원칙적으로 1년 안에 소각</b>해야 합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>자사주 소각이 뭔가요</li>
  <li>자사주를 팔면 회사에, 소각하면 주주에게 세금이 붙습니다</li>
  <li>계속 보유한 주주는 세금을 내지 않습니다</li>
  <li>2026년부터 자사주 소각이 의무입니다</li>
  <li>예외적으로 의제배당세가 발생하는 경우</li>
  <li>이것도 궁금하셨나요</li>
</ol>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">자사주 소각이 뭔가요</h2>

<p>자사주 소각은 회사가 사들여 보유하고 있던 자기 회사 주식을 완전히 없애는 절차입니다. 시중에 풀린 주식 수 자체가 줄어드는 효과가 있습니다.</p>

<p>자사주를 사는 것(매입)과 없애는 것(소각)은 서로 다른 단계입니다. 회사는 시장에서 자사주를 사들인 뒤 계속 보유할 수도, 임직원 보상용으로 쓸 수도, 소각할 수도 있습니다. 세금 문제는 이 중 "처분" 단계, 즉 매각하느냐 소각하느냐에서 갈립니다.</p>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">자사주를 팔면 회사에, 소각하면 주주에게 세금이 붙습니다</h2>

<p>회사가 갖고 있던 자사주를 제3자에게 되팔면, 취득가보다 비싸게 팔아 남은 이익에 법인세가 붙습니다. 회사(법인) 입장의 세금입니다.</p>

<p>반면 회사가 특정 주주로부터 직접 주식을 사들여 소각하면 이야기가 다릅니다. 소득세법 제17조는 주식 소각이나 자본감소로 주주가 받는 돈이 그 주식을 취득할 때 쓴 금액보다 많으면, 그 차액을 <b>배당으로 간주</b>한다고 규정합니다. 이를 의제배당이라 부르고, 이때 세금을 내는 사람은 회사가 아니라 소각대금을 받은 그 주주 본인입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">처분 방식</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">과세 대상</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">세목</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">제3자에게 매각</td>
      <td style="border:1px solid #ddd;padding:8px;">회사(법인)</td>
      <td style="border:1px solid #ddd;padding:8px;">법인세</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">특정 주주로부터 매입 후 소각</td>
      <td style="border:1px solid #ddd;padding:8px;">소각대금을 받은 그 주주</td>
      <td style="border:1px solid #ddd;padding:8px;">배당소득세(의제배당)</td>
    </tr>
  </tbody>
</table>

<p>의제배당의 원천징수 시기는 실제로 돈이 오간 날이 아니라 <b>주식의 소각을 결정한 날</b>입니다. 세율은 배당소득세와 동일하게 원천징수 15.4%이고, 다른 금융소득과 합쳐 연 2,000만원을 넘으면 종합과세 대상이 됩니다.</p>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">계속 보유한 주주는 세금을 내지 않습니다</h2>

<p>여기서 가장 많이 헷갈리는 부분이 남습니다. 자사주가 소각되면 시중 주식 수가 줄어 남은 주주의 지분율은 자연히 올라갑니다. 그런데 이 지분율 상승 자체에는 세금이 붙지 않습니다.</p>

<p>국세청 유권해석도 회사가 자사주를 시가대로 매입해 소각한 경우, 잔여 주주의 지분율이 늘어난 것을 원칙적으로 의제배당으로 보지 않는다고 밝히고 있습니다. 아직 주식을 팔지 않아 이익이 실현되지 않았기 때문입니다.</p>

<ul style="line-height:1.9;">
  <li>지분율이 늘어난 것만으로는 과세 대상 거래 자체가 없습니다.</li>
  <li>그 늘어난 지분을 나중에 실제로 매도할 때는 그 시점의 일반적인 양도소득세 규정(7편 참고)이 적용됩니다.</li>
  <li>단, 시가와 동떨어진 가격에 매입했거나 특수관계자 간 거래처럼 구체적 사정이 있으면 국세청이 개별적으로 다르게 판단할 수 있습니다.</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>내가 보유한 종목이 자사주를 소각한다는 공시가 떴다면</b>
  <p style="margin:8px 0 0 0;">그 자체로 개인 주주가 세금 신고를 해야 하는 일은 생기지 않습니다. 회사에 직접 주식을 팔아 소각대금을 받은 경우가 아니라면, 시장에서 계속 주식을 들고 있는 이상 이번 소각으로 발생하는 세금은 없습니다.</p>
</div>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">2026년부터 자사주 소각이 의무입니다</h2>

<p>2026년 2월 25일 국회 본회의를 통과하고 같은 해 3월 6일 공포와 동시에 시행된 3차 상법 개정으로, 자사주는 원칙적으로 취득 후 <mark>1년 안에 소각</mark>해야 합니다. 임직원 보상 등 활용 목적이 있으면 매년 주주총회 승인을 받아 예외적으로 보유할 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">대상</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">소각 기한</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시행일 이후 신규 취득분</td>
      <td style="border:1px solid #ddd;padding:8px;">취득 후 원칙적으로 1년 이내</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시행일 이전 기존 보유분</td>
      <td style="border:1px solid #ddd;padding:8px;">6개월 준비기간 + 1년(총 1년 6개월) 이내 처분·소각 결정</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">외국인 지분제한 업종</td>
      <td style="border:1px solid #ddd;padding:8px;">소각으로 제한 비율 초과 시 3년 이내 처분 허용</td>
    </tr>
  </tbody>
</table>

<p>상장회사뿐 아니라 비상장회사, 벤처기업까지 예외 없이 적용됩니다. 그동안 자사주를 지분 방어나 우호지분 확보 수단으로 오래 들고 있던 회사들은 이제 보유·처분 계획서를 만들어 매년 주주총회 승인을 받거나, 정해진 기한 안에 실제로 소각해야 합니다.</p>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">예외적으로 의제배당세가 발생하는 경우</h2>

<p>일반 소액주주가 시장에서 상장주식을 그냥 팔 때와, 회사가 특정 주주와 직접 협의해 주식을 사들여 소각하는 것(유상소각·이익소각)은 완전히 다른 상황입니다. 그런데 뉴스에서 "자사주 소각 세금 폭탄"이라는 표현이 나오는 것도 대부분 이 후자, 즉 회사와 직접 거래하는 특정 주주(주로 지주회사나 대주주)에게 해당하는 이야기입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">상황</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">세금 처리</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">일반 상장주식을 시장에서 매도</td>
      <td style="border:1px solid #ddd;padding:8px;">소액주주는 양도소득세 비과세(7편 참고)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">회사와 직접 협의해 주식을 팔고 그 주식이 소각됨</td>
      <td style="border:1px solid #ddd;padding:8px;">받은 돈이 취득가를 넘는 부분에 의제배당(배당소득세)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">그 자사주가 소각되며 지분율만 늘어난 일반 주주</td>
      <td style="border:1px solid #ddd;padding:8px;">원칙적으로 과세 없음</td>
    </tr>
  </tbody>
</table>

<p>결국 핵심은 "누가 회사로부터 실제로 돈을 받았는가"입니다. 돈을 받은 사람에게만 그 차액에 대한 세금 문제가 생기고, 그렇지 않은 주주에게는 소각 자체가 별도의 세금 이벤트가 아닙니다.</p>

<h2 style="border-left:6px solid #16a34a;padding-left:12px;margin-top:36px;">이것도 궁금하셨나요</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">내가 보유한 회사가 자사주를 소각하면 저도 세금을 내야 하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 회사에 직접 주식을 팔아 소각대금을 받은 것이 아니라면, 계속 보유한 주주에게는 이번 소각으로 발생하는 세금이 없습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">자사주 매각과 소각은 세금이 왜 다른가요</summary>
  <p style="margin:10px 0 0 0;">매각은 회사가 주식을 되파는 것이라 처분이익에 법인세가 붙고, 소각은 회사에 주식을 판 주주가 받는 돈에 의제배당(배당소득세)이 붙습니다. 세금을 내는 주체 자체가 다릅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">2026년 상법 개정으로 무엇이 바뀌었나요</summary>
  <p style="margin:10px 0 0 0;">자사주를 원칙적으로 취득 후 1년 안에 소각해야 하는 의무가 생겼습니다. 기존 보유분은 6개월 준비기간을 포함해 1년 6개월 안에 처분이나 소각을 결정해야 하고, 상장·비상장·벤처기업 모두 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">의제배당세는 언제를 기준으로 원천징수하나요</summary>
  <p style="margin:10px 0 0 0;">실제로 돈이 오간 날이 아니라 주식의 소각을 결정한 날을 기준으로 원천징수합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">"자사주 소각 세금 폭탄" 뉴스는 누구 이야기인가요</summary>
  <p style="margin:10px 0 0 0;">주로 회사와 직접 거래해 주식을 넘기는 지주회사나 대주주처럼 특정 주주에 관한 이야기입니다. 시장에서 주식을 사고파는 일반 소액주주와는 상황이 다릅니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 소득세법 제17조(배당소득, 의제배당) 조문</li>
    <li><a href="https://www.moj.go.kr/bbs/moj/182/491790/download.do" target="_blank" rel="noopener">법무부</a> - 자기주식 소각 의무화 관련 개정 「상법」 길라잡이(2026.3.11.)</li>
    <li><a href="https://www.lawtimes.co.kr/news/articleView.html?idxno=217118" target="_blank" rel="noopener">법률신문(법무법인 대륙아주)</a> - 2026년 개정 상법의 자기주식 의무 소각 제도 해설</li>
  </ul>
  기준일: 2026-09-18(WebSearch 확인일). 국세청·법무부 원문 페이지는 이번 세션 WebFetch가
  모두 막혀 직접 열람하지 못했고, 상법 개정 시행 일정은 법무법인·회계법인·세정전문매체
  5곳 이상이 일치하는 것으로, 의제배당 법리는 소득세법 조문과 국세청 유권해석(casenote.kr
  수록)으로 교차검증했습니다. 개정으로 신설된 조문의 정확한 조번호는 원문을 확보하지
  못해 표기하지 않았습니다. 배당소득세율은 4편·6편에서 이미 확정한 수치를 재사용했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 자사주 소각과 관련된 세금 구조를 이해하는 데 도움을 드리려는 정보 제공용
글입니다. 특정 종목이나 상품의 매수매도를 권하지 않으며, 투자 판단과 그 결과는
투자자 본인의 책임입니다. 세율과 관련 법령은 이후 바뀔 수 있으니 실제 적용 전에는
원출처에서 다시 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "자사주 소각 세금 누가 내나",
  "description": "자사주를 매각할 때와 소각할 때 세금이 어떻게 다른지, 계속 보유한 주주는 왜 세금이 없는지, 2026년 의무화된 자사주 소각 상법 개정 내용을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-18",
  "dateModified": "2026-09-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/treasury-stock-cancellation-tax"
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
      "name": "내가 보유한 회사가 자사주를 소각하면 저도 세금을 내야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 회사에 직접 주식을 팔아 소각대금을 받은 것이 아니라면, 계속 보유한 주주에게는 이번 소각으로 발생하는 세금이 없습니다." }
    },
    {
      "@type": "Question",
      "name": "자사주 매각과 소각은 세금이 왜 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "매각은 회사가 주식을 되파는 것이라 처분이익에 법인세가 붙고, 소각은 회사에 주식을 판 주주가 받는 돈에 의제배당(배당소득세)이 붙습니다. 세금을 내는 주체 자체가 다릅니다." }
    },
    {
      "@type": "Question",
      "name": "2026년 상법 개정으로 무엇이 바뀌었나요",
      "acceptedAnswer": { "@type": "Answer", "text": "자사주를 원칙적으로 취득 후 1년 안에 소각해야 하는 의무가 생겼습니다. 기존 보유분은 6개월 준비기간을 포함해 1년 6개월 안에 처분이나 소각을 결정해야 하고, 상장·비상장·벤처기업 모두 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "의제배당세는 언제를 기준으로 원천징수하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "실제로 돈이 오간 날이 아니라 주식의 소각을 결정한 날을 기준으로 원천징수합니다." }
    },
    {
      "@type": "Question",
      "name": "\"자사주 소각 세금 폭탄\" 뉴스는 누구 이야기인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "주로 회사와 직접 거래해 주식을 넘기는 지주회사나 대주주처럼 특정 주주에 관한 이야기입니다. 시장에서 주식을 사고파는 일반 소액주주와는 상황이 다릅니다." }
    }
  ]
}
</script>
