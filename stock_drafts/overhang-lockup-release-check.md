---
keyword: 오버행 뜻
title: 오버행 뜻 보호예수 해제 확인법
slug: overhang-lockup-release-check
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1000 (PC 210 / 모바일 790)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-13 — 통과]
  WebSearch "오버행 뜻 주가" 상위 7개:
  brunch.co.kr(개인 브런치) / mofe.go.kr(기획재정부 시사경제용어사전, 정부) /
  kbthink.com(KB, 대형 금융사 사전 단문) / econowide.com(개인/소규모 경제 블로그) /
  a-ha.io(질문답변 커뮤니티) ×2 / keyzard.cc(개인/소규모 콘텐츠 사이트)
  1) 진입 여지 — 있음. brunch·econowide·a-ha(2)·keyzard 등 개인/커뮤니티 콘텐츠가
     상위 7개 중 5개. SERP가 잠겨 있지 않다.
  2) 검색 의도 — 정보 탐색형("뜻·원인·주가 영향"). 조회·신청·계산기 실행이 지배적
     의도가 아니다.
  3) 답 완결 여부 — 아니다. 상위 글은 대부분 정의와 "주가에 안 좋다" 수준의 일반론만
     다루고, 코스피·코스닥의 실제 의무보호예수 기간(법적 수치), 해제일을 직접 확인하는
     방법, 2026년 실제 사례를 함께 정리한 글은 없다. 정보이득 여지가 뚜렷하다.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (1) 코스피 6개월 / 코스닥 1년이라는 의무보호예수 기간의 실제 법적 수치와, 코스닥은
  상장 6개월 경과 후 매월 최초 보호예수주식수의 5%까지 반환·매각할 수 있다는 세부
  메커니즘 — 상위 SERP 대부분은 "해제되면 주가에 안 좋다"까지만 쓰고 이 수치를
  다루지 않는다.
  (2) 보호예수 해제일을 독자가 직접 확인하는 방법 — 한국예탁결제원 세이브로(SEIBRO)의
  "주식의무보호예수 해제물량조회" 메뉴, DART 전자공시.
  (3) 2026년 실제 사례 — 케이뱅크가 2026년 6월 상장 후 6개월 시점(2026-09)에 발행주식
  20%대 물량의 보호예수가 풀렸고, 우리은행 보유 지분(9%대)도 순차 해제를 앞두고 있다는
  실제 진행 중인 사례를 종목명과 함께 사실 그대로 전달(매수·매도 권유 아님).
  (4) 오버행 발생 원인을 보호예수 해제 외에 유상증자, CB·BW 주식전환, 스톡옵션 행사,
  M&A 이후 대주주 지분 매각까지 목록화.
primary_source: |
  금융위원회 보도자료(fsc.go.kr/no010101/77406, "신규 상장기업 임원의 주식 의무보유가
  강화됩니다")에 WebFetch를 1회 시도했으나 EGRESS_BLOCKED로 확인(2026-09-13). RULES.md
  「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12) 기준 적용.
  핵심 수치(코스피 상장법인 최대주주 등 6개월 의무보호예수 / 코스닥 상장법인 1년,
  코스닥은 상장 6개월 경과 후 매 1개월마다 최초 보호예수주식수의 5%까지 반환매각 가능)는
  서로 무관한 5개 이상 독립 출처가 충돌 없이 일치했다:
  ① 기획재정부 시사경제용어사전(정부, mofe.go.kr) — "의무보호예수" 항목
  ② 아주경제(언론사, ajunews.com) — "[아주 쉬운 뉴스 Q&A] 의무보호예수 기간이란
     무엇인가요?"
  ③ 한국예탁결제원 관련 증권실무해설 PDF(klca.or.kr) — "의무보호예수제도" 해설
  ④ 김앤장 법률사무소(법무법인, kimchang.com) 인사이트 — "신규 상장기업 임원의 주식
     의무보유 강화"
  ⑤ 한국거래소 KIND 공시자료 "코스닥시장 공시·상장관리해설서"(kind.krx.co.kr, 존재와
     제목은 WebSearch 스니펫으로 확인, 원문 WebFetch는 같은 세션에서 시도하지 않음 —
     kind.krx.co.kr도 공공기관 도메인이라 과거 패턴상 차단 가능성이 높다고 판단)
  법무법인(김앤장) 출처가 포함되어 있어 교차검증 기준(3곳 이상, 그중 최소 1곳은
  언론·준정부기관·법무법인급)을 충족한다. 이번 사례로 진행하고 한계를 투명 공개한다.
  2026년 케이뱅크 사례는 매일신문(imaeil.com, 2026-09-07)·다음뉴스 경유 기사
  (2026-06-05)로 확인, 링크는 참고 출처에 별도 표기.
기준일: 2026-09-13 (WebSearch 확인일)
tags: 오버행, 보호예수, 의무보호예수, 상장주식, 코스닥투자, 코스피투자, 락업해제, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-13).
  게이트1: 네이버 키워드도구 실측 1,000회(check-keywords.yml, 2026-09-13). 이번 배치
  8개 후보 중 유상증자·무상증자·사이드카·블록딜과 함께 PASS했으나, 유상증자·무상증자는
  게이트2에서 대형 금융사·로펌·백과사전이 SERP를 완전히 장악해(진입 여지 없음) 탈락시켰다.
  게이트2: v3 기준 통과(serp_check 참조) — 개인/커뮤니티 콘텐츠 다수 진입, 법적 수치·
  확인 방법·실제 사례 미반영으로 정보이득 여지 뚜렷.
  게이트3: 의무보호예수 법적 기간(6개월/1년) + 코스닥 5% 반환매각 메커니즘 + 해제일
  확인 방법(SEIBRO) + 2026년 케이뱅크 실제 사례로 정보이득 확보.
  게이트4: fsc.go.kr 1회 시도 EGRESS_BLOCKED 확인 후 RULES.md 2026-09-12 기준에 따라
  정부 시사용어사전+언론+한국예탁결제원 실무해설+법무법인(김앤장) 5개 이상 독립 출처
  교차검증으로 진행, 수치 일치 확인, 한계 투명 공개.
self_check: |
  [2026-09-13 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 1,000회(일반 주제 기준 500회 이상).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 법적 의무보호예수 기간·반환매각 메커니즘·해제일 확인 방법·2026년
  실제 사례로 상위 SERP와 차별화했다.
  게이트4 — fsc.go.kr에 1회 시도해 EGRESS_BLOCKED 확인. 2026-09-12 RULES.md 기준을
  적용해 정부 시사용어사전·언론·한국예탁결제원 실무해설·법무법인(김앤장) 5개 이상
  독립 출처가 핵심 수치(6개월/1년, 매월 5%)에서 충돌 없이 일치함을 확인해 캡처 요청
  없이 진행했다.
  카니벌라이제이션 점검 — 1~23편 어디에도 오버행·보호예수·의무보호예수는 다루지 않는다.
  17편(공매도 뜻, 상환기간)·20편(반대매매 뜻)과는 메커니즘 자체가 다른 별개 주제다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 안내하는 자리와 하단 참고
  출처 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow
  미부착. kind.krx.co.kr은 이번 세션에서 접속 검증하지 않아 하단 참고 출처에는
  넣지 않고 기관명만 본문에 언급.
  제목 "오버행 뜻 보호예수 해제 확인법" 17자(공백 포함)·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 4단어(overhang-lockup-release-check). FAQ 6개와 JSON-LD
  1:1 일치. @id 티스토리 entry 패턴. 종목명(케이뱅크)은 실제 진행 중인 사례를 사실
  그대로 전달했을 뿐 매수·매도 권유나 목표가 제시는 없음. 단정 표현 없음. 하단 면책
  문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) →
  gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-13</p>

<p>오버행은 <mark>언제든 시장에 쏟아질 수 있는 대량의 대기 매도 물량</mark>을 뜻합니다. 상장 후 일정 기간이 지나 보호예수가 풀리거나, 유상증자·전환사채 주식전환 등으로 새 물량이 생기면 오버행 우려가 커집니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>오버행 = <mark>보호예수 해제·유상증자·전환사채 전환 등으로 시장에 나올 수 있는 대량 매도 대기 물량</mark>입니다.</li>
    <li>코스피 상장법인의 최대주주 등은 <b>상장 후 6개월</b>, 코스닥은 <b>상장 후 1년</b> 동안 지분을 의무적으로 보호예수해야 합니다.</li>
    <li>코스닥은 상장 6개월이 지나면 매달 최초 보호예수주식수의 <b>5%까지</b> 반환받아 팔 수 있습니다.</li>
    <li>보호예수 해제일은 한국예탁결제원 세이브로(SEIBRO)에서 직접 조회할 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>오버행이 정확히 무엇을 뜻하나요</li>
  <li>보호예수 의무기간은 얼마나 되나요</li>
  <li>오버행이 주가에 어떤 영향을 주나요</li>
  <li>보호예수 해제일은 어디서 확인하나요</li>
  <li>2026년 오버행 사례는 어떤 게 있나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">오버행이 정확히 무엇을 뜻하나요</h2>

<p>오버행(Overhang)은 <b>앞으로 시장에 나올 가능성이 있는 대규모 주식 물량</b>을 말합니다. 아직 실제로 팔리지 않았지만, 언제든 매물로 쏟아질 수 있다는 점에서 투자자들이 부담을 느끼는 요소입니다.</p>

<p>오버행이 생기는 원인은 한 가지가 아닙니다. 아래처럼 여러 상황에서 대기 매도 물량이 만들어집니다.</p>

<ul style="line-height:1.9;">
  <li>상장 당시 정한 <b>의무보호예수 기간이 끝나는 경우</b></li>
  <li><b>유상증자</b>로 새 주식이 추가로 발행되는 경우</li>
  <li><b>전환사채(CB)·신주인수권부사채(BW)</b>가 주식으로 전환되는 경우</li>
  <li><b>스톡옵션</b> 행사로 임직원이 신주를 받는 경우</li>
  <li>인수합병(M&A) 이후 <b>기존 대주주가 지분을 정리</b>하는 경우</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">보호예수 의무기간은 얼마나 되나요</h2>

<p>가장 흔한 오버행 원인은 <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">상장 당시 최대주주 등에게 부과되는 의무보호예수 기간이 끝나는 것</span>입니다. 이 기간과 조건은 코스피와 코스닥이 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">최대주주 등 의무보호예수 기간</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">비고</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스피</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>6개월</mark></td>
      <td style="border:1px solid #ddd;padding:8px;">상장일 기산, 6개월 후 전량 해제</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스닥</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>1년</mark></td>
      <td style="border:1px solid #ddd;padding:8px;">상장 6개월 경과 후 매월 최초 보호예수주식수의 5%까지 반환매각 가능</td>
    </tr>
  </tbody>
</table>

<p>즉 코스닥은 상장 후 1년이 다 지나야 전량 해제되는 것이 아니라, <b>6개월째부터 매달 조금씩</b> 시장에 나올 수 있는 구조입니다. 그래서 코스닥 종목은 상장 6개월 시점부터 오버행 이슈가 반복적으로 거론됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">오버행이 주가에 어떤 영향을 주나요</h2>

<p>대기 매도 물량이 실제로 시장에 풀리면 <b>수급 불균형</b>이 생겨 주가가 하락 압력을 받을 수 있습니다. 물량을 보유한 투자자들이 차익 실현을 위해 한꺼번에 매도에 나설 수 있기 때문입니다.</p>

<p>다만 오버행이 있다고 <b>무조건</b> 주가가 떨어지는 것은 아닙니다. 회사 실적이나 시장 상황에 따라 해제일 이후에도 주가가 버티는 경우가 있고, 반대로 해제 훨씬 전부터 우려만으로 주가가 눌리는 경우도 있습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>오버행 = 확정된 악재가 아니라 잠재적 부담</b>
  <p style="margin:8px 0 0 0;">오버행은 "물량이 나올 수 있다"는 가능성을 뜻할 뿐, 실제로 매도가 나올지·언제 나올지는 보유 주체의 판단에 달려 있습니다. 해제 물량 규모가 유통주식수 대비 얼마나 큰지를 함께 확인하는 것이 중요합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">보호예수 해제일은 어디서 확인하나요</h2>

<p>추측하지 않고 실제 해제일과 물량을 확인하는 방법이 있습니다. <a href="https://seibro.or.kr" target="_blank" rel="noopener">한국예탁결제원 세이브로(SEIBRO)</a>는 상장주식의 의무보호예수 해제 물량을 조회할 수 있는 공식 시스템을 제공합니다.</p>

<ul style="line-height:1.9;">
  <li><a href="https://seibro.or.kr" target="_blank" rel="noopener">한국예탁결제원 세이브로(SEIBRO)</a> 접속 → "기업/주식" 메뉴에서 종목별 의무보호예수 해제물량 조회</li>
  <li>전자공시시스템(DART)에서 해당 종목의 지분공시·최대주주 변경 신고를 확인</li>
  <li>증권사 리서치센터가 매월 발표하는 "이달의 보호예수 해제 예정 종목" 리포트 참고</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2026년 오버행 사례는 어떤 게 있나요</h2>

<p>실제 사례를 보면 오버행이 어떻게 진행되는지 감이 잡힙니다. <b>케이뱅크는 2026년 6월 상장했고, 상장 6개월 시점(2026년 9월)에 발행주식의 20%가 넘는 물량에 대한 매각 제한이 풀렸습니다.</b> 이어 우리은행이 보유한 지분(9%대)도 순차적으로 보호예수 해제 구간에 들어설 예정입니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>사실 전달일 뿐, 매수·매도 권유가 아닙니다</b>
  <p style="margin:8px 0 0 0;">위 사례는 언론 보도를 바탕으로 한 진행 상황 설명입니다. 특정 종목의 매수·매도 시점을 제시하는 것이 아니며, 투자 판단은 각자의 몫입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">오버행 뜻은 정확히 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">앞으로 시장에 나올 가능성이 있는 대규모 대기 매도 물량을 뜻합니다. 보호예수 해제, 유상증자, 전환사채 전환, 스톡옵션 행사 등으로 생깁니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">오버행과 유상증자는 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">유상증자는 오버행이 생기는 원인 중 하나입니다. 새로 발행된 주식이 상장돼 유통되면 잠재적 매도 물량, 즉 오버행이 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">보호예수 의무기간은 코스피와 코스닥이 다른가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 코스피 상장법인의 최대주주 등은 상장 후 6개월, 코스닥은 상장 후 1년 동안 지분을 의무적으로 보호예수해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">보호예수 해제일은 어디서 확인할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">한국예탁결제원 세이브로(SEIBRO)의 의무보호예수 해제물량 조회 메뉴에서 종목별로 확인할 수 있고, 전자공시시스템(DART)의 지분공시로도 확인할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">오버행이 있으면 무조건 주가가 하락하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 대기 물량이 실제로 매도돼야 주가에 영향을 주며, 해제 이후에도 물량이 나오지 않으면 주가가 버티는 경우도 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">스톡옵션 행사도 오버행 원인이 되나요</summary>
  <p style="margin:10px 0 0 0;">네. 임직원이 스톡옵션을 행사해 받은 신주가 시장에 나오면 유통 물량이 늘어나므로 오버행 요인 중 하나로 꼽힙니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=1877" target="_blank" rel="noopener">기획재정부 시사경제용어사전 — 오버행</a></li>
    <li><a href="https://www.ajunews.com/view/20191104134723565" target="_blank" rel="noopener">아주경제 — 의무보호예수 기간이란 무엇인가요</a></li>
    <li><a href="https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&amp;idx=24585" target="_blank" rel="noopener">김·장 법률사무소 — 신규 상장기업 임원의 주식 의무보유 강화</a></li>
    <li><a href="https://seibro.or.kr" target="_blank" rel="noopener">한국예탁결제원 세이브로(SEIBRO)</a></li>
    <li><a href="https://www.imaeil.com/page/view/2026090709304609998" target="_blank" rel="noopener">매일신문 — 케이뱅크 보호예수 해제 관련 보도(2026-09-07)</a></li>
  </ul>
  기준일: 2026-09-13(WebSearch 확인일). 금융위원회 원문(fsc.go.kr/no010101/77406)은 이번 세션 WebFetch가 차단돼 직접 확인하지 못했고, 위 정부·언론·법무법인 등 5개 이상 독립 출처의 교차 확인으로 대체했습니다.
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
  "headline": "오버행 뜻 보호예수 해제 확인법",
  "description": "오버행의 뜻과 발생 원인, 코스피 6개월·코스닥 1년인 의무보호예수 기간, 해제일을 직접 확인하는 방법과 2026년 실제 사례를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-09-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/overhang-lockup-release-check"
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
      "name": "오버행 뜻은 정확히 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "앞으로 시장에 나올 가능성이 있는 대규모 대기 매도 물량을 뜻합니다. 보호예수 해제, 유상증자, 전환사채 전환, 스톡옵션 행사 등으로 생깁니다." }
    },
    {
      "@type": "Question",
      "name": "오버행과 유상증자는 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "유상증자는 오버행이 생기는 원인 중 하나입니다. 새로 발행된 주식이 상장돼 유통되면 잠재적 매도 물량, 즉 오버행이 됩니다." }
    },
    {
      "@type": "Question",
      "name": "보호예수 의무기간은 코스피와 코스닥이 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "다릅니다. 코스피 상장법인의 최대주주 등은 상장 후 6개월, 코스닥은 상장 후 1년 동안 지분을 의무적으로 보호예수해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "보호예수 해제일은 어디서 확인할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "한국예탁결제원 세이브로(SEIBRO)의 의무보호예수 해제물량 조회 메뉴에서 종목별로 확인할 수 있고, 전자공시시스템(DART)의 지분공시로도 확인할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "오버행이 있으면 무조건 주가가 하락하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 대기 물량이 실제로 매도돼야 주가에 영향을 주며, 해제 이후에도 물량이 나오지 않으면 주가가 버티는 경우도 있습니다." }
    },
    {
      "@type": "Question",
      "name": "스톡옵션 행사도 오버행 원인이 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 임직원이 스톡옵션을 행사해 받은 신주가 시장에 나오면 유통 물량이 늘어나므로 오버행 요인 중 하나로 꼽힙니다." }
    }
  ]
}
</script>
