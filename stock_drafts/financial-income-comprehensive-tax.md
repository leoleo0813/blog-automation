---
keyword: 금융소득 종합과세
title: 금융소득종합과세 2천만원 기준 확인법
slug: financial-income-comprehensive-tax
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 12270 (PC 2590 / 모바일 9680)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 재판정 2026-09-07: 통과]
  WebSearch "금융소득종합과세 2000만원 기준" 상위 7개:
  v.daum.net(동아일보 머니컨설팅, 언론) / m.joseilbo.com(조세일보, 언론) /
  help.3o3.co.kr(삼쩜삼 고객센터, 핀테크 서비스) / namu.wiki(백과) /
  incometax.calculate.co.kr(계산기 서비스) / hometax-go.kr 택스고(소규모 콘텐츠 사이트) x2
  1) 진입 여지: 있음. 택스고(hometax-go.kr)가 2개, 삼쩜삼 고객센터 1개로 소규모 콘텐츠가
     실제로 상위에 올라 있다. 오히려 국세청 공식 페이지는 이번 검색 상위에 없었다. SERP 안 잠김.
  2) 검색 의도: 정보 탐색("기준이 얼마고 넘으면 어떻게 되나"). 계산기가 1개 있으나 주 의도 아님.
  3) 답 완결 여부: 상위 3개가 언론 2 + 핀테크 고객센터 1로, 비교과세 공식이나 2천만원 이하
     예외(국외원천)까지 정확히 답하는 공식 페이지가 상위에 없다. 정보이득 여지 충분.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
  (참고: 2026-09-06 구 기준 판정에서는 "공식·언론·백과 5개 이상"으로 탈락 처리됐었다.
   구 기준이 세금 주제에서 모든 키워드를 거부하는 문제로 RULES.md 게이트2가 v3로 재조정됨.)
unique_asset: 이자+배당 합산 판단 절차(4단계) + "전액이 아니라 초과분에만 누진세율" 오해 해소 + 비교과세 산출세액 공식 ①②를 국세청 원문 그대로 제시(①과 ② 중 큰 금액) + 2,000만원 이하인데도 종합과세되는 예외(원천징수되지 않은 국외원천 이자·배당소득, 출자공동사업자 배당소득) + 세무서 자료와 금융회사 자료가 다를 때 금융회사 자료 기준으로 신고. 뒤의 두 가지는 상위 경쟁 콘텐츠가 대체로 다루지 않는 부분이라 이 글의 핵심 차별점.
primary_source: 국세청 국세상담센터 종합소득세 Q&A(금융소득), https://call.nts.go.kr/call/qna/selectQnaInfo.do?mi=1441&ctgId=CTG11775 . 사람이 직접 접속해 캡처를 제공(2026-09-07), 전문은 sources/nts-call-financial-income-qna.md 에 보존. 근거 조문 소득세법 제14조(종합과세 대상·예외)·제62조(비교과세). 보조로 sources/nts-overseas-stock-tax-2024.md(국세청 공식 책자 2024-05)의 2천만원 기준을 교차 확인. 자동화 세션에서는 nts.go.kr/easylaw.go.kr/law.go.kr이 EGRESS_BLOCKED라 사람 캡처로만 확보 가능(2026-09-06·09-07 두 세션 재현).
기준일: 2026-09-07 (국세청 국세상담센터 페이지 캡처일, 해당 페이지에는 별도 "OOOO년 O월 O일 기준" 문구가 표시되지 않고 근거 조문만 링크됨). 교차 확인에 쓴 국세청 책자는 2024-05 발간.
tags: 금융소득종합과세, 배당소득분리과세, 금융소득2천만원, 종합소득세, 이자소득세, 배당소득세, 비교과세, 금융소득세금, 주식초보, 세금신고, 2026세금
gate_pass: true
refresh_due: 2027-03-31
figure_plan: "2장. 1번 = 금융소득 3,000만원이 2,000만원 기준선 기준으로 14% 구간과 종합과세 구간으로 나뉘는 구조도, 2번 = 다른 소득 크기에 따라 금융소득 몫 세금이 420·430·542만원으로 달라지는 막대. 서로 다른 정보라 2장."
updated_note: "2026-10-07 갱신: 2026년 고배당 상장사 배당 분리과세(14~30%) 절 추가, 가상 계산 예시 표와 그림 2장, 주식 투자자 관점 H2, 내부 링크 3개, 첫 두 문장을 검색어에 맞게 교체. 구간별 분리과세 세율표는 원문 미확인이라 수록하지 않음(capture_guide 참조)."
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-07).
  게이트1: 네이버 키워드도구 실측 12,270회(PC 2,590 / 모바일 9,680): 시리즈 최대.
  게이트2: v3 기준으로 재판정해 통과(serp_check 참조). 구 기준에서는 탈락이었으나,
    구 기준이 세금 주제의 모든 키워드를 거부하는 문제가 확인돼 RULES.md 게이트2가
    2026-09-07 v3로 재조정됐다. 5편처럼 게이트 결과를 사람이 넘긴 human_override가 아니라,
    기준 자체를 고친 뒤 그 기준으로 정식 통과한 것이다.
  게이트3: 비교과세 공식 + 2천만원 이하 종합과세 예외(국외원천 이자·배당) + 신고 시
    금융회사 자료 기준. 뒤의 둘은 상위 경쟁 글들이 대체로 다루지 않는다.
  게이트4: 국세청 국세상담센터 원문 캡처(2026-09-07), 근거 조문 소득세법 제14조·제62조.
capture_guide: |
  [2026-10-07 선택 보강] 고배당 상장사 배당 분리과세의 구간별 세율(언론 요약은 2천만원 이하 14% ~ 50억원 초과 30%로
  엇갈림 없이 보이나 기사 원문을 열지 못함)은 본문에 범위(14~30%)만 썼다. 구간표까지 넣으려면 국세청 또는
  기획재정부 보도자료 캡처가 필요하다: law.go.kr 에서 '조세특례제한법' 검색 → '고배당기업 배당소득 분리과세' 조문
  (2026년 신설) 캡처, 또는 기재부 '2025년 세제개편안' 보도자료. 안 하면 지금 본문 그대로 발행해도 된다.
  [해결됨 2026-09-07] 사람이 국세청 국세상담센터 금융소득 Q&A를 직접 캡처해 제공,
  비교과세 산출세액 공식(①② 중 큰 금액, 소득세법 제62조), 2천만원 이하인데도 종합과세되는
  예외(원천징수되지 않은 금융소득·출자공동사업자 배당소득, 소득세법 제14조), 신고 시 금융회사
  자료 기준 원칙을 모두 확보. 전문은 sources/nts-call-financial-income-qna.md 에 보존했고
  본문에 반영 완료. 게이트3·4 충족으로 전환.

  게이트2도 2026-09-07 해결됨: RULES.md 게이트2가 v3로 재조정된 뒤 그 기준으로 재판정해
  통과(serp_check 참조). 남은 사람 작업은 티스토리에 붙여넣어 발행하는 것뿐이다.

  [2026-09-07 추가 확보] 종합소득세 기본세율 구간표도 사람이 캡처해 제공,
  sources/nts-income-tax-rate.md 에 보존하고 본문에 표로 넣었다. 링크 안내만 하던 것을
  실제 표로 대체했다. 확인 과정에서 국세청이 게시한 최신 구간이 "2023~2025년 귀속"이고
  2026년 귀속 표는 아직 없다는 것도 확인해, 본문에 귀속연도를 명시했다.
  2022년 귀속까지 하위 두 구간 경계가 1,200만/4,600만원이었다가 2023년부터
  1,400만/5,000만원으로 오른 이력도 함께 넣었다(오래된 글과 갈리는 지점).
  배당가산액(Gross-up) 비율도 위 ① 공식에 등장하지만 본문에서 수치를 쓰지 않아 필수는 아니다.
self_check: |
  [2026-09-07 사람 캡처 반영 후 재판정]
  게이트1 충족: 네이버 키워드도구 실측 12,270회(PC 2,590 / 모바일 9,680). 시리즈 최대.
  게이트2 충족: RULES.md 게이트2 v3(2026-09-07 재조정) 기준으로 재판정해 통과.
  판정 근거는 serp_check 참조(소규모 콘텐츠 3곳 상위 진입, SERP 안 잠김).
  게이트3 충족으로 전환: 캡처로 확보한 비교과세 공식(①② 중 큰 금액)을 국세청 표현 그대로
  제시하고, 상위 경쟁 콘텐츠가 대체로 빠뜨리는 두 가지를 추가했다: (a) 2,000만원 이하인데도
  종합과세되는 예외: 원천징수되지 않은 금융소득(국외원천 이자·배당)과 출자공동사업자 배당소득,
  (b) 세무서 자료와 금융회사 자료가 다를 때 금융회사 자료 기준으로 신고. (a)는 해외주식
  보유자에게 실질적 영향이 있어 5편(해외주식 양도세)과 자연스럽게 연결된다.
  게이트4 충족으로 전환: 국세청 국세상담센터 원문 캡처 확보(2026-09-07),
  sources/nts-call-financial-income-qna.md에 전문 보존. 근거 조문 소득세법 제14조·제62조.
  [2026-09-07 보강] 종합소득세 기본세율 구간표를 사람이 캡처해 제공해 본문에 표로 넣었다
  (sources/nts-income-tax-rate.md). 국세청 최신 게시 구간이 2023~2025년 귀속이고 2026년
  귀속 표는 아직 없다는 사실도 확인해 캡션에 명시했다: "2026년 세율"이라고 단정하지 않았다.
  keyword_class를 human-assisted/capture 그대로 유지: 실제로 사람 캡처가 있어야 완성됐다.
  제목 20자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와 JSON-LD 1:1 일치.
  @id를 티스토리 entry 패턴으로 지정. 종목·상품 추천/단정 표현 없음. 하단 고정 문구 포함.
  4편(배당소득세)과의 카니발라이제이션 점검: 4편은 원천징수 15.4%가 얼마인지가 중심,
  이 글은 합산 2천만원 판단과 비교과세가 중심이라 검색 의도가 다르다. 본문에서 4편으로 안내.
  기관 링크 점검(RULES.md 「기관 링크 필수」): 본문 기관 안내 문장 3곳(홈택스 신고 안내 2,
  국세청 세율표 안내 1) 전부 링크 처리, 하단 참고 출처 5개 전부 링크 처리. 모두
  target="_blank" rel="noopener"이며 정부·공공기관이라 nofollow는 붙이지 않았다.
  href 안의 &는 &amp;로 이스케이프했다.
  [2026-10-07 갱신 점검] AI 티 점검: em대시 0개, 다만 0회, mark 밀도 본문 9개(표 셀 포함). 첫 문장 유형: 정의+수치형.
  구조 유형: 계산형 보강(가상 계산표+그림 2장 추가). 확인하세요류 2회 이하, 내부 링크 3개(해외주식 배당소득세·
  배당소득세 얼마 떼나·채권 세금), 이 글로 오는 링크는 기존 글 9편 이상에 이미 있음. 분리과세 요건은 언론 3곳 요약이
  같은 숫자(배당성향 40%/25%+10%, 14~30%, 2026-01-01)로 일치해 통과, 구간별 세율은 원문 미확인이라 미수록.
  가상 계산 검증: ①A=280+624=904, ②A=420+474=894, ①B=280+1,606=1,886, ②B=420+1,344=1,764 (2023~2025 귀속 기본세율).
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 5편식 human_override가 아니라
  게이트2 기준 자체를 v3로 고친 뒤 정식 통과한 것이다. 발행 가능.
---

<p>금융소득종합과세는 이자와 배당을 합쳐 연 2,000만원을 넘을 때, <mark>넘는 부분만</mark> 다른 소득과 합산해 세금을 다시 매기는 제도입니다. 2,000만원까지는 원천징수로 끝나고, 2026년부터는 요건을 갖춘 고배당 상장사의 배당이 분리과세 대상으로 빠집니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>이자소득과 배당소득을 1년간 합산해 <b>2,000만원을 넘는지</b>가 종합과세 여부를 가르는 기준입니다.</li>
    <li>2,000만원 이하는 원천징수 15.4%로 납세가 끝나고, <mark>초과분만</mark> 다른 소득과 합산해 종합소득세로 다시 계산됩니다.</li>
    <li>전액이 아니라 초과한 금액에만 누진세율이 적용되며, 세부담이 원천징수보다 줄어들지 않도록 하는 별도 계산 장치(비교과세)도 함께 적용됩니다.</li>
    <li>배우자의 금융소득은 합산되지 않고, <b>본인 명의 소득만</b> 계산 대상입니다.</li>
    <li>예외가 있습니다. <b>원천징수되지 않은 국외원천 이자·배당소득</b>은 2,000만원 이하라도 종합과세됩니다.</li>
    <li>2026년 1월 1일 이후 받는 배당부터는 <b>고배당 상장사 배당이 14~30% 분리과세</b>로 빠지는 길이 생겼습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">금융소득종합과세는 무엇인가요</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2,000만원 기준은 어떻게 계산하나요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2,000만원 넘으면 세금이 어떻게 달라지나요</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">세금은 두 방식 중 '큰 쪽'으로 정해집니다 (비교과세)</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">금융소득 3,000만원 가상 계산: 다른 소득에 따라 갈리는 세금</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2,000만원 이하인데도 종합과세되는 경우가 있습니다</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">신고할 때 어느 자료를 기준으로 하나요</a></li>
  <li><a href="#sec-8" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">배우자 소득도 합산되나요</a></li>
  <li><a href="#sec-9" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2026년부터 달라진 점: 고배당 상장사 배당 분리과세</a></li>
  <li><a href="#sec-10" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">주식 투자자에게 왜 중요한가: 배당주 보유자의 합산 점검</a></li>
  <li><a href="#sec-11" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">종합소득세 신고는 어떻게 하나요</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">금융소득종합과세는 무엇인가요</h2>

<p>금융소득종합과세는 <b>이자소득과 배당소득을 합친 금액이 연 2,000만원을 넘을 때</b> 적용되는 제도입니다. 예금·적금 이자, 채권 이자와 할인액, 주식 배당금, 펀드 분배금이 모두 합산 대상에 포함됩니다.</p>

<ul style="line-height:1.9;">
  <li><b>이자소득 예시:</b> 예금·적금 이자, 채권 이자, 저축성보험 차익 등</li>
  <li><b>배당소득 예시:</b> 국내외 주식 배당금, 펀드(집합투자기구) 분배금 등</li>
</ul>

<p style="font-size:13px;color:#888;">출처: <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 공식 책자 「2024년 해외주식과 세금(개인투자자용)」(2024년 5월 발간) · <a href="https://easylaw.go.kr" target="_blank" rel="noopener">법제처 찾기쉬운 생활법령정보</a>(2026-08-15 기준).</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2,000만원 기준은 어떻게 계산하나요</h2>

<p>본인의 금융소득만 아래 순서로 더해보면 종합과세 대상인지 바로 확인할 수 있습니다.</p>

<ol style="line-height:1.9;">
  <li>1년간 받은 예금·적금·채권 등 <b>이자소득</b>을 모두 더합니다.</li>
  <li>국내외 주식 배당금, 펀드 분배금 등 <b>배당소득</b>을 모두 더합니다.</li>
  <li>이자소득 합계와 배당소득 합계를 <b>더합니다.</b></li>
  <li>합계액이 <mark>2,000만원을 넘는지</mark> 확인합니다. 넘지 않으면 원천징수로 끝나고, 넘으면 초과분이 종합소득세 신고 대상이 됩니다.</li>
</ol>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>참고</b>
  <p style="margin:8px 0 0 0;">국내 상장주식을 팔아서 생긴 <b>양도차익</b>은 대주주가 아니면 애초에 과세 대상이 아니므로 이 2,000만원 합산에 포함되지 않습니다. 합산되는 것은 배당금과 이자뿐입니다.</p>
</div>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2,000만원 넘으면 세금이 어떻게 달라지나요</h2>

<p>2,000만원을 넘었다고 <mark>전체 금액에 누진세율이 붙는 것은 아닙니다.</mark> 2,000만원까지는 그대로 15.4% 원천징수로 계산되고, <b>넘는 부분만</b> 다른 소득(근로소득·사업소득 등)과 합산되어 종합소득세율로 다시 계산됩니다.</p>

<div style="background:#fff8e6;border-left:4px solid #e0a800;padding:14px 18px;margin:20px 0;">
  <b>정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>금융소득 2,000만원 이하분: 15.4% 원천징수로 납세 종결(분리과세)</li>
    <li>금융소득 2,000만원 초과분: 다른 종합소득과 합산해 종합소득세율(누진세율) 적용</li>
  </ul>
</div>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">세금은 두 방식 중 '큰 쪽'으로 정해집니다 (비교과세)</h2>

<p>여기서 많이들 놓치는 장치가 있습니다. 종합과세 대상이 됐다고 해서 무조건 누진세율만 적용하는 게 아니라, <mark>두 가지 방식으로 각각 계산해보고 더 큰 금액을 납부세액으로 정합니다.</mark> 종합과세로 넘어갔는데 오히려 세금이 줄어드는 일이 생기지 않도록 만든 안전장치입니다.</p>

<p>국세청이 안내하는 산출세액 계산식은 다음과 같습니다.</p>

<div style="background:#fff8e6;border:2px solid #e0a800;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5c00;font-size:17px;">① 종합과세 방식으로 계산한 세액</strong>
  <p style="margin:8px 0 18px 0;line-height:1.9;">2천만원 × 14% <b>+</b> (2천만원 초과 금융소득 + 배당가산액 + 다른 종합소득금액 − 소득공제) × 기본세율</p>

  <strong style="color:#7a5c00;font-size:17px;">② 분리과세 방식으로 계산한 세액</strong>
  <p style="margin:8px 0 18px 0;line-height:1.9;">금융소득 × 원천징수세율 <b>+</b> (다른 종합소득금액 − 소득공제) × 기본세율</p>

  <p style="margin:0;padding-top:12px;border-top:1px dashed #e0a800;"><b>납부할 세액 = ①과 ② 중 큰 금액</b></p>
</div>

<div style="background:#f4f6f8;border-left:4px solid #8895a5;padding:12px 16px;margin:20px 0;font-size:14px;line-height:1.8;">
  위 식에서 <b>2천만원까지는 언제나 14%로 계산</b>된다는 점을 눈여겨보세요. 누진세율(기본세율)이 붙는 건 <b>2천만원을 넘은 부분부터</b>입니다. "2천만원을 1원이라도 넘으면 전체 금융소득에 높은 세율이 붙는다"는 이야기가 도는데, 계산식 자체가 그렇게 되어 있지 않습니다.
</div>

<p>식에 들어가는 <b>기본세율</b>은 종합소득세 누진세율입니다. 계산은 <mark>과세표준 × 세율 − 누진공제액</mark>으로 합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">과세표준</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세율</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">누진공제</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">1,400만원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">−</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">1,400만원 초과 5,000만원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">15%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">126만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">5,000만원 초과 8,800만원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">24%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">576만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">8,800만원 초과 1억 5,000만원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">35%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1,544만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">1억 5,000만원 초과 3억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">38%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1,994만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">3억원 초과 5억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">40%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">2,594만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">5억원 초과 10억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">42%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">3,594만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">10억원 초과</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">45%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6,594만원</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;"><b>2023~2025년 귀속 기준</b>입니다. 출처: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&amp;cntntsId=7667" target="_blank" rel="noopener">국세청 › 종합소득세 › 기본정보 › 세율</a>(2026-09-07 확인). 국세청이 게시한 가장 최신 구간이 2023~2025년 귀속분이며, 2026년 귀속 세율표는 아직 올라와 있지 않습니다. 신고 시점에는 해당 귀속연도 표가 올라와 있는지 같은 페이지에서 보면 됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>구간 경계가 바뀐 적이 있습니다</b>
  <p style="margin:8px 0 0 0;">2022년 귀속까지는 하위 두 구간 경계가 <b>1,200만원 / 4,600만원</b>이었고, 2023년 귀속부터 <b>1,400만원 / 5,000만원</b>으로 올라갔습니다. 오래된 글의 표에는 예전 경계가 그대로 남아 있을 수 있습니다.</p>
</div>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">금융소득 3,000만원 가상 계산: 다른 소득에 따라 갈리는 세금</h2>

<p>금융소득이 3,000만원이어도 <mark>다른 소득이 클수록 금융소득에 붙는 세금이 커집니다.</mark> 아래는 예금 이자만 3,000만원을 받은 가상의 사람 두 명을 비교한 계산입니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/financial-income-comprehensive-tax-1.png" alt="금융소득 3,000만원 중 2,000만원은 14% 원천징수 구간, 넘는 1,000만원은 종합과세 구간으로 나뉘는 구조도" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 소득세법 제14조·제62조, 국세청 국세상담센터(2026-09-07 확인). 3,000만원은 계산용 가정값</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">항목(만원)</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">A: 다른 소득 4,000만원</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">B: 다른 소득 8,000만원</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">① 종합과세 방식: 2,000×14%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">280</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">280</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">① 초과 1,000+다른 소득에 기본세율</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5,000×15%−126=624</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">9,000×35%−1,544=1,606</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">① 합계</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><b>904</b></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><b>1,886</b></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">② 분리과세 방식: 3,000×14%+다른 소득 세금</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">420+474=894</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">420+1,344=1,764</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">납부세액(①과 ② 중 큰 쪽)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><b>904</b></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><b>1,886</b></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">다른 소득만 있을 때 세금</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">474</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1,344</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">금융소득에 붙은 세금</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>430</mark></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>542</mark></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">원천징수 420 대비 추가 납부</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">+10</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">+122</td></tr>
  </tbody>
</table>

<p>A는 넘는 1,000만원이 15% 구간에서 계산돼 추가 납부가 10만원에 그칩니다. B는 같은 1,000만원이 24~35% 구간에 걸쳐 추가 납부가 122만원으로 커집니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/financial-income-comprehensive-tax-2.png" alt="금융소득 3,000만원의 소득세: 원천징수만 420만원, 다른 소득 4,000만원이면 430만원, 8,000만원이면 542만원" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 위 표의 가상 계산, 2023~2025년 귀속 기본세율(국세청). 지방소득세 제외</figcaption></figure>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>계산 전제</b>
  <p style="margin:8px 0 0 0;">이자소득만 있다고 가정해 배당가산액은 0으로 두었고, 다른 소득은 공제를 뺀 과세표준 기준입니다. 이자소득 원천징수세율은 14%로 보았고 지방소득세(소득세의 10%)는 뺐습니다. 실제 신고에서는 이미 낸 원천징수세액(420만원)을 기납부세액으로 빼고 차액만 냅니다.</p>
</div>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2,000만원 이하인데도 종합과세되는 경우가 있습니다</h2>

<p>기준선만 외우면 놓치는 예외가 있습니다. 국세청은 <mark>다음 두 가지는 금융소득이 2,000만원 이하라도 종합과세한다</mark>고 안내합니다.</p>

<ul style="line-height:1.9;">
  <li><b>원천징수되지 않은 금융소득</b>: 대표적인 예가 <b>국외원천 이자·배당소득</b>입니다. 국내 금융회사를 거치지 않아 원천징수가 이뤄지지 않았다면 금액이 작아도 신고 대상입니다.</li>
  <li><b>출자공동사업자의 배당소득</b></li>
</ul>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:12px 16px;margin:20px 0;line-height:1.8;">
  <b>해외 주식·해외 예금을 갖고 있다면 특히 주의할 자리입니다.</b> "2,000만원도 안 되는데 뭘" 하고 넘기기 쉬운 자리인데, 원천징수가 안 된 국외원천 소득은 금액과 무관하게 종합과세 대상입니다. 증권사가 원천징수를 대행했는지 여부부터 확인하는 게 순서입니다.
</div>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고할 때 어느 자료를 기준으로 하나요</h2>

<p>세무서에서 받은 금융자료와 금융회사에서 받은 자료의 숫자가 다를 때가 있습니다. 국세청은 <mark>금융회사에서 제공받은 자료를 기준으로 신고</mark>하라고 안내합니다. 금융회사가 이자·배당소득지급명세서를 제출하지 않았거나 중복·오류 자료를 제출한 경우, 세무서가 제공한 자료가 사실과 다를 수 있기 때문입니다.</p>

<h2 id="sec-8" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배우자 소득도 합산되나요</h2>

<p>아닙니다. 금융소득종합과세는 <mark>본인 명의의 소득만 합산</mark>합니다. 배우자나 다른 가족 명의의 예금·주식에서 나온 이자·배당소득은 본인의 2,000만원 기준에 포함되지 않습니다.</p>

<h2 id="sec-9" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2026년부터 달라진 점: 고배당 상장사 배당 분리과세</h2>

<p>2026년 1월 1일 이후 지급받는 배당부터, 요건을 갖춘 고배당 상장사의 배당소득은 <mark>종합소득에 합산하지 않고 14~30% 세율로 분리과세</mark>합니다. 이자와 합친 금융소득이 2,000만원을 넘어도 이 배당은 위 비교과세 계산에서 빠진다는 뜻입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">내용</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">적용 시작</td><td style="border:1px solid #ccd;padding:10px;">2026년 1월 1일 이후 지급받는 배당</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">대상 기업</td><td style="border:1px solid #ccd;padding:10px;">배당성향 40% 이상, 또는 배당성향 25% 이상이면서 전년보다 배당 10% 이상 증가한 상장사</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">세율 범위</td><td style="border:1px solid #ccd;padding:10px;">14~30%(지방소득세 별도), 배당소득이 클수록 높은 세율</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">과세 방식</td><td style="border:1px solid #ccd;padding:10px;">종합소득에 합산하지 않고 분리과세로 종결</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">출처: <a href="https://www.ytn.co.kr/_ln/0102_202512311356310272" target="_blank" rel="noopener">YTN, '최고 30%' 고배당 기업 배당소득 분리과세 도입</a>(2025-12-31) · <a href="https://www.newsis.com/view/NISX20260115_0003478692" target="_blank" rel="noopener">뉴시스, 고배당기업 현금배당 늘리면 세금 깎아준다[세법시행령]</a>(2026-01-15). 2026년 10월 기준 언론 보도로 정리했고, 구간별 세율은 이 글에 싣지 않았습니다.</p>

<p>배당성향은 순이익 중 배당으로 나간 비율입니다. 어느 종목이 요건에 드는지는 회사별 공시를 봐야 하므로 이 글에서 종목을 짚지 않습니다.</p>

<h2 id="sec-10" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">주식 투자자에게 왜 중요한가: 배당주 보유자의 합산 점검</h2>

<p>배당을 많이 받는 투자자는 <mark>배당이 이자와 합쳐 2,000만원선에 닿는 순간</mark> 세금 구조가 달라집니다. 배당주 비중이 큰 계좌일수록 이 기준선이 가까워집니다.</p>

<ul style="line-height:1.9;">
  <li>배당만 받아도 연 2,000만원이면 한 종목 배당이 아니라 모든 계좌의 이자·배당 합계로 따집니다.</li>
  <li>예금 이자가 많은 사람은 같은 배당이라도 기준선을 더 빨리 넘습니다.</li>
  <li>해외주식 배당은 국내 증권사가 원천징수한 경우와 아닌 경우의 신고 방식이 달라집니다. 원천징수 세율은 <a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-dividend-tax" target="_blank" rel="noopener">해외주식 배당소득세</a> 글에 있습니다.</li>
  <li>국내 배당의 기본 원천징수 15.4%는 <a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax" target="_blank" rel="noopener">배당소득세 얼마 떼나</a> 글에서 계산해 두었습니다.</li>
</ul>

<p>채권 이자나 이자부 상품이 많은 경우는 <a href="https://sensitiveboss3.tistory.com/entry/bond-tax-guide" target="_blank" rel="noopener">채권 세금</a> 글의 원천징수 방식까지 합쳐 따져야 합니다. 분리과세 대상 배당이 늘어도 이자소득은 그대로 합산 대상이라는 점이 갈림길입니다.</p>

<h2 id="sec-11" style="scroll-margin-top:72px;border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">종합소득세 신고는 어떻게 하나요</h2>

<p>금융소득이 2,000만원을 넘은 해가 있다면, <b>다음 해 5월 1일부터 31일까지</b> <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>에서 종합소득세 확정신고를 해야 합니다.</p>

<ol style="line-height:1.9;">
  <li>증권사·은행에서 발급하는 이자·배당소득 지급명세서를 확인합니다.</li>
  <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스(hometax.go.kr)</a>에 로그인해 <b>종합소득세 신고</b> 메뉴로 들어갑니다.</li>
  <li>금융소득 2,000만원 초과분과 다른 종합소득(근로·사업소득 등)을 함께 입력합니다.</li>
  <li>계산된 세액을 확인하고 신고서를 제출한 뒤 납부합니다.</li>
</ol>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>이자소득+배당소득이 연 2,000만원을 넘는지가 종합과세 여부를 가르는 기준입니다.</li>
    <li>전액이 아니라 <b>초과한 부분만</b> 다른 소득과 합산해 종합소득세율로 재계산됩니다.</li>
    <li>세부담이 원천징수보다 줄지 않도록 비교과세 장치가 함께 적용되며, 신고는 다음 해 5월입니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금융소득종합과세 2,000만원 기준은 무엇을 합산하나요</summary>
  <p style="margin:10px 0 0 0;">1년간 받은 이자소득과 배당소득을 모두 더한 금액입니다. 국내 상장주식 양도차익(대주주 제외)은 포함되지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금융소득이 2,000만원 이하면 신고 안 해도 되나요</summary>
  <p style="margin:10px 0 0 0;">네. 15.4% 원천징수로 납세 의무가 끝나 별도로 종합소득세를 신고할 필요가 없습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">2,000만원을 넘으면 전체 금액에 누진세율이 붙나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 2,000만원까지는 그대로 15.4% 원천징수로 계산되고, 넘는 부분만 다른 소득과 합산해 종합소득세율이 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배우자 소득도 합쳐지나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 금융소득종합과세는 본인 명의의 소득만 합산하며, 배우자나 가족 명의 소득은 포함되지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내 상장주식 배당도 포함되나요</summary>
  <p style="margin:10px 0 0 0;">네. 국내외 상장주식 배당금과 펀드 분배금 모두 배당소득으로 합산 대상에 포함됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">종합소득세 신고는 언제 하나요</summary>
  <p style="margin:10px 0 0 0;">금융소득이 2,000만원을 넘은 해의 다음 해 5월 1일부터 31일까지 홈택스에서 확정신고합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li>국세청 국세상담센터: 금융소득 종합과세 제도, 비교과세 산출세액 계산(소득세법 제62조), 2,000만원 이하 종합과세 예외(소득세법 제14조), 신고 시 기준 자료 (<a href="https://call.nts.go.kr/call/qna/selectQnaInfo.do?mi=1441&amp;ctgId=CTG11775" target="_blank" rel="noopener">call.nts.go.kr</a>, 2026-09-07 확인)</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&amp;cntntsId=7667" target="_blank" rel="noopener">국세청: 종합소득세 세율</a> (과세표준 구간별 세율·누진공제, 2023~2025년 귀속 기준, 2026-09-07 확인)</li>
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 공식 책자 「2024년 해외주식과 세금(개인투자자용)」: 금융소득종합과세 2,000만원 기준 (2024년 5월 발간)</li>
    <li><a href="https://easylaw.go.kr" target="_blank" rel="noopener">법제처 찾기쉬운 생활법령정보</a>: 배당소득세 원천징수 15.4% (2026-08-15 기준)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>: 종합소득세 확정신고</li>
    <li>기준일: 2026-09-07 (국세청 국세상담센터 확인일)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를 권유하지 않습니다.
투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·기준금액은 법 개정에 따라 변경될 수 있으므로 반드시 원출처에서 최신 내용을 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "금융소득종합과세 2,000만원 기준은 무엇을 합산하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1년간 받은 이자소득과 배당소득을 모두 더한 금액입니다. 국내 상장주식 양도차익(대주주 제외)은 포함되지 않습니다."
      }
    },
    {
      "@type": "Question",
      "name": "금융소득이 2,000만원 이하면 신고 안 해도 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네. 15.4% 원천징수로 납세 의무가 끝나 별도로 종합소득세를 신고할 필요가 없습니다."
      }
    },
    {
      "@type": "Question",
      "name": "2,000만원을 넘으면 전체 금액에 누진세율이 붙나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아니요. 2,000만원까지는 그대로 15.4% 원천징수로 계산되고, 넘는 부분만 다른 소득과 합산해 종합소득세율이 적용됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "배우자 소득도 합쳐지나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아니요. 금융소득종합과세는 본인 명의의 소득만 합산하며, 배우자나 가족 명의 소득은 포함되지 않습니다."
      }
    },
    {
      "@type": "Question",
      "name": "국내 상장주식 배당도 포함되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네. 국내외 상장주식 배당금과 펀드 분배금 모두 배당소득으로 합산 대상에 포함됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "종합소득세 신고는 언제 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "금융소득이 2,000만원을 넘은 해의 다음 해 5월 1일부터 31일까지 홈택스에서 확정신고합니다."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "금융소득종합과세 2천만원 기준 확인법",
  "description": "금융소득 2,000만원 넘으면 넘는 부분만 종합과세. 비교과세 공식, 3,000만원 가상 계산, 2026년 고배당 분리과세 요건을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-06",
  "dateModified": "2026-10-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/financial-income-comprehensive-tax"
  }
}
</script>
