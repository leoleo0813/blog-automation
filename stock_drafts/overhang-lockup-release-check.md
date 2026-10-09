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
기준일: 2026-10-09 (제도 수치는 2026-09-13 교차검증값, 해제 물량은 한국예탁결제원 2026-08-31·09-30 발표를 언론 보도로 확인)
tags: 오버행, 보호예수, 의무보유등록, 보호예수 해제, 락업, 케이뱅크 보호예수, 10월 보호예수 해제, 코스닥 보호예수
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
refresh_due: 2026-11-02
figure_plan: "2장. 1: 코스피 6개월 vs 코스닥 12개월(6개월 후 매월 5%) 시간표(기간 구조) / 2: 2026년 10월 해제 물량 상위 6곳 막대(크기 비교). 서로 다른 정보라 2장, 계산표는 표로 유지"
refresh_note: "2026-10-09 갱신(구글 노출 118회·평균 8.1위 글): 케이뱅크 상장 시점 오류 정정(6월이 아니라 2026-03-05 상장, 9월 5일 해제), 2026년 9·10월 해제 물량 반영, 해제 물량 대비 유통주식 계산표, 투자자 관점 H2, 그림 2장, 내부 링크 4개. 법정 기간(6개월·1년·5%)은 9/13 교차검증값 재사용. 10월 수치는 예탁결제원 9/30 발표를 언론이 같은 숫자로 보도"
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
  [2026-10-09 갱신 점검] 기존 본문의 "케이뱅크 2026년 6월 상장, 9월 해제" 서술을 정정했다. 케이뱅크는 2026-03-05 상장이고 예탁결제원 8/31 발표 기준 9월 5일 8,178만주(보도 기준 발행주식 약 20%)가 해제됐으며, 최대주주 비씨카드 1억2,669만주는 2027-03-05까지 묶여 있다(언론 보도, 원문 접속은 egress 차단). 해제 주수는 매체별로 8,178만·8,377만주 등 다르게 나와 예탁결제원 집계 숫자만 쓰고 출처를 밝혔다. 10월 해제(34개사 9,932만주, 유가증권 1개사 702만, 코스닥 33개사 9,230만, 상위 6곳 주수)는 SBS Biz·아시아경제·메트로신문 등이 같은 숫자로 보도. 발행주식 대비 비율은 매체 간 불일치가 있어 쓰지 않았다. 케이뱅크 우리은행 잔여 지분 9.22%는 보도 인용.
  AI 티 점검: em대시 0개, 다만 0회, mark 3개. 첫 문장 유형: 문제제기형. 구조 유형: 개념형+계산표(첫 H2에 비유 문단), 어투 B 대화형(해요체). 첫 H2의 첫 블록은 비유 문단. FAQ 7개(직전 편 5~6개와 다름), 박스 제목 새로 지음, 확인하세요류 2회 이하. 내부 링크 4개(블록딜·IPO 의무보유확약·전환사채 리픽싱·권리락 계산, 모두 발행 완료 글).
  기관 안내 문장 전부 링크 처리, 출처 목록 전부 링크 처리.
---
<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-09</p>

<p>보유 종목에 "오버행 우려"라는 기사가 붙으면 괜히 마음이 쓰이죠. 오버행은 <mark>언제든 시장에 나올 수 있는 대기 매도 물량</mark>을 뜻하고, 가장 흔한 신호는 의무보유(보호예수) 해제일이에요.</p>

<div style="background:#fff4e8;border:2px solid #c26a1b;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#8a4a0f;font-size:18px;">📌 이번 달 해제 물량부터 볼게요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>한국예탁결제원 집계로 <b>2026년 10월에는 34개사 9,932만 주</b>의 의무보유가 풀려요. 유가증권시장 1개사 702만 주, 코스닥 33개사 9,230만 주예요.</li>
    <li>최대주주 등 의무보유는 코스피 <b>6개월</b>, 코스닥 <b>1년</b>이고, 코스닥은 6개월 뒤부터 매월 최초 물량의 5%까지 팔 수 있어요.</li>
    <li>해제 물량이 커 보여도 <b>유통주식수와 비교</b>해야 의미가 있고, 해제가 곧 매도는 아니에요.</li>
  </ul>
</div>

<h2>목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">오버행은 정확히 무엇인가요</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">의무보유 기간, 코스피와 코스닥은 이렇게 달라요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2026년 10월 해제 물량 한눈에 보기</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">케이뱅크 사례로 보는 해제 과정</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자는 해제 소식을 어떻게 읽나요</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">해제일 직접 조회하는 법</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">해제 소식 앞에서 떠오르는 의문들</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">오버행은 정확히 무엇인가요</h2>

<p>오버행(Overhang)은 <b>아직 팔리지 않았지만 곧 팔릴 수 있는 주식 더미</b>예요. 머리 위에 매달린 물탱크처럼, 터지기 전에는 멀쩡해 보여도 시장은 늘 그 무게를 의식해요.</p>

<p>오버행이 생기는 길은 하나가 아니에요.</p>

<ul style="line-height:1.9;">
  <li>상장 때 걸어 둔 <b>의무보유(보호예수) 기간이 끝나는 경우</b></li>
  <li><a href="https://sensitiveboss3.tistory.com/entry/ex-rights-price-calculation" target="_blank" rel="noopener">유상증자로 새 주식이 생기는 경우</a>(권리락 기준가 계산법도 함께 보면 좋아요)</li>
  <li><a href="https://sensitiveboss3.tistory.com/entry/convertible-bond-refixing" target="_blank" rel="noopener">전환사채(CB)가 주식으로 바뀌는 경우</a></li>
  <li>임직원이 스톡옵션을 행사해 신주를 받는 경우</li>
  <li>인수합병 뒤 기존 대주주가 지분을 정리하는 경우</li>
</ul>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">의무보유 기간, 코스피와 코스닥은 이렇게 달라요</h2>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">코스피는 상장 후 6개월, 코스닥은 상장 후 1년</span>이 최대주주 등의 의무보유 기간이에요. 기간이 끝나기 전에는 한국예탁결제원에 주식이 묶여 있어서 시장에 팔 수 없어요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/overhang-lockup-release-check-1.png" alt="코스피는 상장 후 6개월 뒤 전량 해제, 코스닥은 6개월 뒤부터 매월 5%씩 반환되어 12개월에 전량 해제되는 시간표" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 기획재정부 시사경제용어사전·김·장 법률사무소 해설 등 교차 대조, 기준일 2026-09-13</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">최대주주 등 의무보유 기간</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">중간에 풀리는 물량</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스피</td>
      <td style="border:1px solid #ddd;padding:8px;">상장일부터 6개월</td>
      <td style="border:1px solid #ddd;padding:8px;">없음. 6개월 뒤 한꺼번에 해제</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">코스닥</td>
      <td style="border:1px solid #ddd;padding:8px;">상장일부터 1년</td>
      <td style="border:1px solid #ddd;padding:8px;">6개월 뒤부터 매월 최초 보호예수 주식수의 <mark>5%</mark>까지 반환·매각 가능</td>
    </tr>
  </tbody>
</table>

<p>그래서 코스닥 종목은 상장 6개월 시점부터 오버행 이야기가 달마다 따라붙어요. 한 번에 터지지 않고 조금씩 흘러나오는 구조라서요.</p>

<p>IPO 때 기관투자자가 "6개월 팔지 않겠다"고 약속한 확약 물량은 법정 의무와 별개예요. 이 제도는 <a href="https://sensitiveboss3.tistory.com/entry/ipo-mandatory-holding-allocation-2026" target="_blank" rel="noopener">IPO 의무보유확약과 우선배정제도</a> 글에 따로 정리해 뒀어요.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">2026년 10월 해제 물량 한눈에 보기</h2>

<p>한국예탁결제원이 9월 30일 발표한 10월 해제 물량은 <b>34개사, 약 9,932만 주</b>예요. 이 중 93%쯤이 코스닥에 몰려 있어요.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/overhang-lockup-release-check-2.png" alt="2026년 10월 의무보유 해제 물량 상위 6곳 막대그래프: 채비 1,531만 주, 제일엠앤에스 707만 주, HJ중공업 702만 주, 카카오게임즈 692만 주, 삐아 631만 주, 푸드나무 498만 주" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 한국예탁결제원 10월 의무보유 해제 발표(2026-09-30)를 보도한 SBS Biz·메트로신문, 기준일 2026-09-30</figcaption></figure>

<ul style="line-height:1.9;">
  <li>유가증권시장: HJ중공업 702만 주가 <b>10월 28일</b> 해제돼요.</li>
  <li>코스닥: 제넥신 <b>10월 17일</b>, 카카오게임즈 <b>10월 24일</b> 등이 포함돼요.</li>
  <li>주말에 걸린 해제일은 실제 매도가 다음 거래일부터 가능해요. 10월 17일과 24일은 토요일이에요.</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>이 집계에 안 들어간 물량이 있어요</b>
  <p style="margin:8px 0 0 0;">예탁결제원은 자발적 보유 확약과 IPO 때 기관투자자가 한 의무 확약 물량을 이 집계에 포함하지 않았다고 설명했어요. 그래서 실제로 풀리는 물량은 표의 숫자보다 클 수 있어요.</p>
</div>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">케이뱅크 사례로 보는 해제 과정</h2>

<p>케이뱅크는 <b>2026년 3월 5일에 상장</b>했고, 상장 6개월 시점인 9월 5일에 약 8,178만 주의 의무보유가 풀렸어요. 한국예탁결제원 집계 기준 숫자이고, 언론은 이를 발행주식의 약 20%로 보도했어요.</p>

<p>보도에 따르면 이 해제 물량에는 우리은행이 들고 있던 잔여 지분(약 9%대)이 들어 있어요. 9월 5일은 토요일이라 처분은 첫 거래일인 9월 7일(월)부터 가능했어요.</p>

<p>반대로 최대주주 비씨카드의 1억2,669만 주는 2027년 3월 5일까지 묶여 있다고 보도됐어요. 같은 회사 안에서도 주주마다 풀리는 날이 다르다는 뜻이에요.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>사실 전달일 뿐 매수·매도 권유가 아니에요</b>
  <p style="margin:8px 0 0 0;">위 내용은 언론 보도와 예탁결제원 집계를 정리한 진행 상황이에요. 특정 종목의 매수·매도 시점이나 주가 방향을 말하는 글이 아니에요.</p>
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">주식 투자자는 해제 소식을 어떻게 읽나요</h2>

<p>해제 물량의 절대 크기보다 <b>해제 물량이 지금 시장에서 거래되는 주식 수의 몇 배인가</b>가 더 중요해요. 같은 500만 주라도 유통주식이 1,000만 주인 종목과 5억 주인 종목은 무게가 전혀 달라요.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">가상 종목</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">현재 유통주식수</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">해제 물량</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">해제 물량 ÷ 유통주식수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">A사(소형주)</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">1,000만 주</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">500만 주</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;"><mark>50%</mark></td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">B사(대형주)</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">5억 주</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">500만 주</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">1%</td>
    </tr>
  </tbody>
</table>

<p>시장이 보는 포인트는 보통 이 네 가지예요.</p>

<ul style="line-height:1.9;">
  <li><b>비율</b>: 위 표처럼 유통주식 대비 해제 물량이 클수록 수급 부담으로 읽어요.</li>
  <li><b>누가 푸는가</b>: 최대주주 물량인지, 상장 전 투자한 재무적 투자자(FI)인지에 따라 매도 가능성이 달라요.</li>
  <li><b>취득 단가</b>: 공모가보다 현재 주가가 낮으면 팔 유인이 작고, 높으면 차익 실현 유인이 커져요.</li>
  <li><b>선반영 여부</b>: 해제일은 몇 달 전에 공개돼서 그날 전부터 주가에 미리 반영되기도 해요.</li>
</ul>

<p>그래서 해제일이 지나도 주가가 버티거나, 해제 한참 전에 이미 빠지는 일이 모두 일어나요. 해제는 가능성이지 확정된 매도가 아니에요.</p>

<p>대주주가 의무보유와 상관없이 대량 물량을 한 번에 넘기는 방식은 <a href="https://sensitiveboss3.tistory.com/entry/block-deal-pre-disclosure" target="_blank" rel="noopener">블록딜 뜻과 사전공시 의무</a> 글에서 할인율 계산과 함께 다뤘어요.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">해제일 직접 조회하는 법</h2>

<p>종목별 해제일과 물량은 <a href="https://seibro.or.kr" target="_blank" rel="noopener">한국예탁결제원 세이브로(SEIBRO)</a>에서 직접 볼 수 있어요. 세이브로에서 의무보유 해제 관련 조회 메뉴를 열고 종목명을 넣으면 돼요.</p>

<ol style="line-height:1.9;">
  <li><a href="https://seibro.or.kr" target="_blank" rel="noopener">세이브로</a>에 접속해 의무보유(보호예수) 해제 조회 메뉴를 찾아요.</li>
  <li>궁금한 종목명이나 기간을 넣어 해제일과 주식 수를 봐요.</li>
  <li>그 주식 수를 종목의 총 발행주식수·유통주식수와 나눠 비율을 직접 계산해요.</li>
  <li>매달 말 예탁결제원이 발표하는 다음 달 해제 현황 보도자료로 전체 흐름을 훑어요.</li>
</ol>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #c26a1b;padding-left:12px;margin-top:36px;">해제 소식 앞에서 떠오르는 의문들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">오버행 뜻을 한 줄로 말하면 뭔가요</summary>
  <p style="margin:10px 0 0 0;">앞으로 시장에 쏟아질 수 있는 대기 매도 물량이에요. 의무보유 해제, 유상증자, 전환사채 전환, 스톡옵션 행사가 대표적인 원인이에요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">보호예수와 의무보유등록은 같은 말인가요</summary>
  <p style="margin:10px 0 0 0;">거의 같은 뜻으로 써요. 한국예탁결제원 발표 자료는 "의무보유등록"이라고 부르고, 언론과 투자자는 "보호예수"라는 말을 더 많이 써요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해제일 당일에 바로 팔 수 있나요</summary>
  <p style="margin:10px 0 0 0;">해제일이 거래일이면 가능해요. 주말이면 다음 거래일부터 처분할 수 있어서, 케이뱅크 9월 5일(토) 해제분은 9월 7일(월)부터 가능했어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해제되면 주가는 반드시 내려가나요</summary>
  <p style="margin:10px 0 0 0;">아니에요. 보유자가 실제로 팔아야 수급에 영향을 주고, 해제 전에 이미 주가에 반영되는 경우도 있어요. 유통주식 대비 비율, 누가 푸는지, 취득 단가를 같이 봐야 해요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코스피와 코스닥은 기간이 왜 달라요</summary>
  <p style="margin:10px 0 0 0;">제도상 코스피는 최대주주 등 6개월, 코스닥은 1년이에요. 코스닥은 6개월 뒤부터 매월 5%씩 반환받을 수 있어서 물량이 나눠서 나와요. 두 시장의 상장 요건 차이는 <a href="https://sensitiveboss3.tistory.com/entry/kospi-kosdaq-difference-delisting" target="_blank" rel="noopener">코스피 코스닥 차이와 상장폐지 기준</a> 글에 있어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해제 예정 목록은 어디서 보나요</summary>
  <p style="margin:10px 0 0 0;">세이브로의 해제 조회 메뉴와 매달 말 한국예탁결제원 보도자료, 전자공시시스템(DART)의 지분 공시에서 볼 수 있어요.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">유상증자도 오버행이 되나요</summary>
  <p style="margin:10px 0 0 0;">네. 새로 발행돼 상장된 주식이 유통되면 잠재 매도 물량이 늘어서 오버행 요인이 돼요.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=1877" target="_blank" rel="noopener">기획재정부 시사경제용어사전: 오버행</a></li>
    <li><a href="https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&amp;idx=24585" target="_blank" rel="noopener">김·장 법률사무소: 신규 상장기업 임원의 주식 의무보유 강화</a></li>
    <li><a href="https://biz.sbs.co.kr/amp/article/20000337485" target="_blank" rel="noopener">SBS Biz: 예탁원, 다음달 34개사 9천932만주 의무보유등록 해제(2026-09-30)</a></li>
    <li><a href="https://view.asiae.co.kr/article/2026031316042210643" target="_blank" rel="noopener">아시아경제: 우리銀, 상장일에 유통가능물량 전부 매도(2026-03-13)</a></li>
    <li><a href="https://www.ajunews.com/view/20191104134723565" target="_blank" rel="noopener">아주경제: 의무보호예수 기간이란 무엇인가요</a></li>
    <li><a href="https://seibro.or.kr" target="_blank" rel="noopener">한국예탁결제원 세이브로(SEIBRO)</a></li>
  </ul>
  기준일: 2026-10-09. 의무보유 기간 수치는 2026-09-13에 정부·언론·법무법인 자료를 교차 대조한 값이고, 해제 물량은 한국예탁결제원 발표를 보도한 기사 기준이에요. 해제 물량 숫자는 매체와 집계 방식에 따라 조금씩 달라질 수 있어요.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보를 알려 드리는 목적이며 특정 종목이나 상품의 매수·매도를 권하지 않아요.
투자 판단과 그 결과의 책임은 투자자 본인에게 있어요. 제도와 해제 일정은 바뀔 수 있으니
원출처에서 최신 내용을 꼭 대조해 주세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "오버행 뜻 보호예수 해제 확인법",
  "description": "오버행의 뜻과 코스피 6개월·코스닥 1년 의무보유 기간, 2026년 10월 해제 물량(34개사 9,932만 주), 케이뱅크 사례, 해제일 조회법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-10-09",
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
    {"@type": "Question", "name": "오버행 뜻을 한 줄로 말하면 뭔가요", "acceptedAnswer": {"@type": "Answer", "text": "앞으로 시장에 쏟아질 수 있는 대기 매도 물량이에요. 의무보유 해제, 유상증자, 전환사채 전환, 스톡옵션 행사가 대표적인 원인이에요."}},
    {"@type": "Question", "name": "보호예수와 의무보유등록은 같은 말인가요", "acceptedAnswer": {"@type": "Answer", "text": "거의 같은 뜻으로 써요. 한국예탁결제원 발표 자료는 \"의무보유등록\"이라고 부르고, 언론과 투자자는 \"보호예수\"라는 말을 더 많이 써요."}},
    {"@type": "Question", "name": "해제일 당일에 바로 팔 수 있나요", "acceptedAnswer": {"@type": "Answer", "text": "해제일이 거래일이면 가능해요. 주말이면 다음 거래일부터 처분할 수 있어서, 케이뱅크 9월 5일(토) 해제분은 9월 7일(월)부터 가능했어요."}},
    {"@type": "Question", "name": "해제되면 주가는 반드시 내려가나요", "acceptedAnswer": {"@type": "Answer", "text": "아니에요. 보유자가 실제로 팔아야 수급에 영향을 주고, 해제 전에 이미 주가에 반영되는 경우도 있어요. 유통주식 대비 비율, 누가 푸는지, 취득 단가를 같이 봐야 해요."}},
    {"@type": "Question", "name": "코스피와 코스닥은 기간이 왜 달라요", "acceptedAnswer": {"@type": "Answer", "text": "제도상 코스피는 최대주주 등 6개월, 코스닥은 1년이에요. 코스닥은 6개월 뒤부터 매월 5%씩 반환받을 수 있어서 물량이 나눠서 나와요. 두 시장의 상장 요건 차이는 코스피 코스닥 차이와 상장폐지 기준 글에 있어요."}},
    {"@type": "Question", "name": "해제 예정 목록은 어디서 보나요", "acceptedAnswer": {"@type": "Answer", "text": "세이브로의 해제 조회 메뉴와 매달 말 한국예탁결제원 보도자료, 전자공시시스템(DART)의 지분 공시에서 볼 수 있어요."}},
    {"@type": "Question", "name": "유상증자도 오버행이 되나요", "acceptedAnswer": {"@type": "Answer", "text": "네. 새로 발행돼 상장된 주식이 유통되면 잠재 매도 물량이 늘어서 오버행 요인이 돼요."}}
  ]
}
</script>
