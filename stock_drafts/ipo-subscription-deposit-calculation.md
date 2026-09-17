---
keyword: 공모주 청약
title: 공모주 청약 증거금 계산 방법
slug: ipo-subscription-deposit-calculation
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 4900 (PC 1420 / 모바일 3480)
gate1_pass: true (일반 주제 기준 월 500 이상 필요 — 네이버 키워드도구 실측 4,900회로 이번 배치 최고 검색량)
serp_check: |
  [게이트2 v3 판정 2026-09-17 — 통과]
  WebSearch "공모주 청약 방법 증거금 계산 균등배정 비례배정 2026" 상위 종합:
  m.shinhansec.com(신한투자증권 공식) / news.jkn.co.kr(재경일보, 언론) /
  calctools.co.kr(개인 계산기 사이트) / easyzetec.com(개인/소규모 블로그, 43편에서도
  확인된 곳) / ipo.seosann.kr(개인 계산기 사이트) / trendmetriclab.com(개인/소규모
  블로그, 9편에서도 확인된 곳) / iprovest.com(교보증권 공식) / m.nhsec.com(NH투자증권
  공식) / keyzard.cc(개인 블로그)
  1) 진입 여지 — 있음. calctools.co.kr·easyzetec.com·ipo.seosann.kr·
     trendmetriclab.com·keyzard.cc 등 개인/소규모 콘텐츠·계산기 사이트가 상위 다수
     진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색+계산 의도가 섞여 있으나("증거금 얼마 필요한지, 배정이 어떻게
     되는지"), 계산기 실행 의도가 상위를 독점하지는 않는다. 재경일보·easyzetec.com·
     trendmetriclab.com 등 설명형 가이드 콘텐츠도 함께 상위권에 있어 조회·계산기 실행이
     지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 다수가 증거금 계산 공식(공모가×신청주수×증거금률)과
     균등/비례배정 기본 개념은 이미 다루고 있어 그 부분만으로는 정보이득이 약하다. 다만
     ① "균등배정도 신청자가 물량보다 많으면 전원이 1주씩 받는 게 아니라 추첨으로
     갈린다"는 실제 메커니즘, ② 2025-10-31 예고된 코스닥벤처펀드 우선배정 비율 확대
     (25%→30%, 2026-01-01 시행 예정)라는 최신 제도 변화를 함께 엮어 설명하는 글은
     상위 결과에서 확인하지 못했다. 정보이득 여지 있음.
  → 탈락조건 1·2 미해당, 탈락조건 3은 부분적으로 걸치나 위 두 가지 정보이득으로 통과
    가능하다고 판단.
unique_asset: |
  (1) 균등배정의 "동등한 배정 기회"가 실제로는 무엇을 뜻하는지 — 균등배정 신청자 수가
      균등배정 물량보다 많으면 전원이 1주씩 받는 게 아니라, 최소 청약증거금 이상을 낸
      신청자 중 추첨으로 갈려 누구는 1주, 누구는 0주를 받는다는 점. "청약만 하면 무조건
      1주는 받는다"는 흔한 오해를 바로잡는다.
  (2) 증거금 계산 예시(공모가 30,000원 × 200주 × 증거금률 50% = 3,000,000원)와 비례배정
      계산 예시(300주 신청, 경쟁률 1,000:1 → 300÷1,000=0.3, 소수점 버림으로 0주 배정)를
      함께 제시해 "증거금을 많이 넣어도 배정은 0주일 수 있다"는 실제 감각을 계산으로
      보여준다.
  (3) 2025-10-31 금융투자협회가 예고한 코스닥벤처펀드 등 정책펀드 우선배정 비율 확대
      (기존 25% → 30% 이상, 2026-01-01 이후 증권신고서 제출 코스닥 상장 예정기업부터
      적용, 2028-12-31까지 3년 한시)를 반영 — 대다수 기존 공모주 청약 가이드 콘텐츠가
      2025-10-31 이전에 작성돼 이 변화를 담지 못했다. 35편(IPO 뜻과 의무보유확약
      우선배정제도)은 IPO 전체 절차와 기관투자자 의무보유확약을 다루며 이 글에서 다루는
      "일반청약자의 증거금 계산·균등/비례배정 실제 메커니즘"은 다루지 않는다고 명시적으로
      기록돼 있어(해당 draft 132행) 카니벌라이제이션이 없다.
primary_source: |
  1차 시도: 금융투자협회 법규정보시스템 「증권 인수업무 등에 관한 규정」
  (https://law.kofia.or.kr/service/law/lawFullScreen.do?seq=140&historySeq=1728) WebFetch
  1회 시도 → EGRESS_BLOCKED(2026-09-17). 대조군으로 무관한 도메인(www.google.com) 1회
  추가 시도했으나 동일하게 EGRESS_BLOCKED로 확인돼 이번 세션의 전면 차단으로 판단했다
  (RULES.md 누적 기록 패턴과 일치, 그 이상 재시도하지 않음).
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로
  진행했다.
  - 균등배정 50% 이상·비례배정 공식(배정주수=신청주수÷경쟁률)·증거금 계산 공식(공모가×
    신청주수×증거금률)은 신한투자증권·NH투자증권·교보증권(iprovest.com)·삼성증권
    (samsungpop.com) 등 대형 증권사 공식 안내 페이지와 다이신증권 공지(money2.daishin.com)
    가 전부 동일한 수치로 일치했고, 이는 대형 증권사가 자사 계좌개설 고객에게 직접
    고지하는 내용이라 신뢰도가 높다. 원 근거는 금융투자협회 「증권 인수업무 등에 관한
    규정」(2020-11-30 개정, 2021년 시행)이다.
  - 코스닥벤처펀드 우선배정 비율 확대(25%→30%, 2026-01-01 시행 예정, 2028-12-31까지
    3년 한시)는 독립된 언론 7곳(파이낸셜뉴스·이데일리 마켓인·머니투데이·아시아경제·
    뉴스톱·리드경제·서울경제) 전부가 동일한 수치·시행일로 보도했고, 금융투자협회 공식
    보도자료(kofia.or.kr/brd/m_211/view.do?seq=223)와 금융위원회 보도자료
    (fsc.go.kr/no010101/85897)도 검색으로 확인돼 준정부기관 공식 발표 성격까지
    갖췄다. 독립 출처 3곳 기준을 크게 초과하고 핵심 수치 충돌이 전혀 없어 교차검증
    기준을 충족한다.
  - 세율·공제한도·과세표준처럼 과거 오류가 확인된 유형의 숫자(RULES.md 사례: 대주주
    기준 5배 차이, 코스피 세율 4배 차이)가 아니라 배정 절차·비율 규정이라 교차검증으로
    진행해도 되는 유형으로 판단했다.
기준일: 2026-09-17 (WebSearch 확인일)
tags: 공모주청약, 청약증거금, 균등배정, 비례배정, IPO청약, 공모주계산, 코스닥벤처펀드, 주식초보, 재테크초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-17).
  게이트1: 네이버 키워드도구 실측 4,900회(check-keywords.yml, 2026-09-17 — 일반 주제
  기준 500회 이상). 같은 배치에서 액면분할(1,980회)·권리락(1,000회)·배당기준일
  (1,090회)·미수거래(970회)·배당수익률(860회)도 게이트1 통과했으나 검색량이 가장 높은
  "공모주 청약"을 우선 채택하고 나머지는 backlog.verified에 다음 편 후보로 기록. 휴면주식
  찾는법(20회)·해외주식 증여세(20회)는 게이트1 미달. 이전 배치(변동성완화장치 뜻·RSU
  세금·거래정지 뜻·증거금률 뜻·미수거래 뜻·장외주식 거래 방법·우리사주조합 뜻·예탁결제원
  뜻)는 전부 20~420회로 게이트1 미달.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그·계산기 사이트 진입 여지
  있고, 균등배정 추첨 메커니즘과 2025-10-31 코스닥벤처펀드 우선배정 확대라는 최신
  변화를 함께 다루는 글이 상위 결과에 없어 정보이득 여지 있음.
  게이트3: 증거금·비례배정 계산 예시 2건 + 균등배정 추첨 메커니즘(오해 정정) + 최신
  규정 변화(2025-10-31 예고, 2026-01-01 시행) 반영으로 정보이득 확보.
  게이트4: law.kofia.or.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군(google.com)도
  차단돼 세션 전면 차단 확인 후 RULES.md 2026-09-12 기준에 따라 교차검증 진행 — 균등/
  비례배정·증거금 공식은 대형 증권사 공식 안내 다수 일치, 최신 규정 변화는 독립 언론
  7곳 + 금융투자협회·금융위원회 공식 보도자료까지 확인해 신뢰도 높음.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 4,900회(일반 주제 기준 500회 이상, 이번 배치
  최고 검색량).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은 균등배정
  추첨 메커니즘과 최신 규정 변화라는 두 정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 균등배정 추첨 메커니즘(오해 정정) + 증거금·비례배정 계산 예시 2건 +
  2025-10-31 코스닥벤처펀드 우선배정 확대(25%→30%) 최신 정보로 상위 결과가 다루지
  않는 각도를 확보했다.
  게이트4 — law.kofia.or.kr 직접 열람은 막혔고(대조군 google.com도 차단, 세션 전면
  차단), 균등/비례배정·증거금 공식은 대형 증권사 공식 안내 다수가 일치, 최신 규정
  변화는 독립 언론 7곳 + 금융투자협회·금융위원회 공식 보도자료로 교차검증해 진행했다.
  카니벌라이제이션 점검 — 35편(IPO 뜻과 의무보유확약 우선배정제도)은 IPO 전체 절차
  개념과 기관투자자 의무보유확약이 중심이고, 해당 draft 132행에 "공모주 청약 방법·
  균등배정·보호예수기간은 다루지 않았다"고 명시돼 있어 이 글의 증거금 계산·균등/비례
  배정 실제 메커니즘과 검색 의도가 겹치지 않는다. 본문에서 35편으로 내부 링크.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 금융투자협회·금융위원회 안내 문장과 하단
  참고 출처 목록 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에
  nofollow 미부착. 출처 URL은 WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "공모주 청약 증거금 계산 방법" 16자(공백 포함)·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 4단어(ipo-subscription-deposit-calculation). 인트로 문단
  최상단 배치. 표는 thead/tbody 시맨틱 사용. 기준일 명시. FAQ 6개와 JSON-LD 1:1 일치.
  종목·상품 추천 표현, 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 대형 증권사 공식 안내 다수 + 독립 언론
  7곳 + 금투협·금융위 공식 보도자료 교차검증으로 대체, 한계 투명 공개) → gate_pass:true.
  발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-17</p>

<p><mark>공모주 청약은 증권사 계좌에 청약증거금을 넣고 신청하면 균등배정과 비례배정 두 가지 방식으로 주식을 나눠 받는 절차입니다.</mark> 증거금을 많이 넣는다고 무조건 많이 받는 것도, 청약만 하면 반드시 1주를 받는 것도 아니라서 계산 방법과 배정 원리를 정확히 알아야 합니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>청약증거금 = <b>공모가 × 신청 주수 × 증거금률</b>(대부분 50%)로 계산합니다.</li>
    <li>배정 물량의 <b>50% 이상은 균등배정, 나머지는 비례배정</b>으로 나뉩니다. 균등배정도 신청자가 물량보다 많으면 <mark>추첨으로 갈려 0주를 받을 수도 있습니다.</mark></li>
    <li>비례배정 주수 = 신청 주수 ÷ 경쟁률(소수점 버림)이라, 증거금을 많이 넣어도 경쟁률이 높으면 배정이 0주가 될 수 있습니다.</li>
    <li>2026년 1월부터 코스닥 공모주는 코스닥벤처펀드 우선배정 비율이 25%에서 30%로 확대되는 규정이 적용됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>공모주 청약이 뭔가요</li>
  <li>청약 증거금은 어떻게 계산하나요</li>
  <li>균등배정과 비례배정은 어떻게 다른가요</li>
  <li>공모주 청약은 어떤 순서로 진행되나요</li>
  <li>최근 배정 규정이 바뀐다는데 무슨 내용인가요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">공모주 청약이 뭔가요</h2>

<p>공모주 청약은 새로 증시에 상장하는 기업이 일반투자자에게 파는 주식을 신청해서 받는 절차입니다. 증권사 계좌에 청약증거금을 넣고 원하는 수량을 신청하면, 그 증권사가 대표주관사로 참여한 공모에서 배정 결과에 따라 주식을 받습니다.</p>

<p>공모주가 상장 후 공모가보다 오르는 경우가 많다 보니 인기가 높지만, <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">신청한 수량을 그대로 받는 것이 아니라 증거금과 배정 방식에 따라 실제 받는 주식 수가 달라진다는 점</span>을 먼저 이해해야 합니다. IPO 전체 절차(주관사 선정부터 상장까지)와 기관투자자의 의무보유확약 제도는 <a href="https://sensitiveboss3.tistory.com/entry/ipo-mandatory-holding-allocation-2026" target="_blank" rel="noopener">이전 글(IPO 뜻과 의무보유확약 우선배정제도)</a>에서 다뤘습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">청약 증거금은 어떻게 계산하나요</h2>

<p><b>청약증거금은 공모가 × 신청 주수 × 증거금률로 계산합니다.</b> 증거금률은 증권사·종목에 따라 다를 수 있지만 대부분 50%를 적용합니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시</b>
  <p style="margin:8px 0 0 0;">공모가가 30,000원인 기업에 200주를 청약하고 증거금률이 50%라면, <b>30,000원 × 200주 × 50% = 3,000,000원</b>이 청약증거금으로 필요합니다.</p>
</div>

<p>증거금을 낼 때는 신청 주수의 절반만 실제 현금으로 내는 셈이지만, <mark>배정이 확정되기 전까지는 신청 주수 전체를 기준으로 증거금을 미리 준비해야 합니다.</mark> 최종 배정 결과에 따라 배정받지 못한 만큼의 증거금은 환불됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">균등배정과 비례배정은 어떻게 다른가요</h2>

<p>일반청약자에게 배정되는 물량은 <b>50% 이상이 균등배정, 나머지가 비례배정</b>으로 운영됩니다. 이 비율은 금융투자협회의 <a href="https://law.kofia.or.kr/service/law/lawFullScreen.do?seq=140&amp;historySeq=1728" target="_blank" rel="noopener">「증권 인수업무 등에 관한 규정」</a>에 근거합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">배정 방식</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">배정 주수 계산</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">균등배정 (50% 이상)</td>
      <td style="border:1px solid #ddd;padding:8px;">최소 청약증거금 이상을 낸 모든 신청자에게 동등한 배정 기회 부여</td>
      <td style="border:1px solid #ddd;padding:8px;">신청자 수가 물량보다 많으면 추첨</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">비례배정 (나머지)</td>
      <td style="border:1px solid #ddd;padding:8px;">신청 주수가 많을수록 배정 확률·수량 증가</td>
      <td style="border:1px solid #ddd;padding:8px;">신청 주수 ÷ 경쟁률 (소수점 버림)</td>
    </tr>
  </tbody>
</table>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">균등배정은 "청약만 하면 무조건 1주는 받는다"는 뜻이 아닙니다.</span> 균등배정 물량보다 최소 증거금 이상을 낸 신청자 수가 많으면, 그 초과분만큼은 추첨으로 갈려 누구는 1주를 받고 누구는 0주를 받습니다. "동등한 배정 기회"는 동일한 확률을 의미하는 것이지 동일한 수량을 보장하는 것이 아닙니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>비례배정 계산 예시</b>
  <p style="margin:8px 0 0 0;">300주를 신청했는데 경쟁률이 1,000:1이라면, 배정 주수는 <b>300 ÷ 1,000 = 0.3</b>이고 소수점은 버리므로 실제 배정은 <b>0주</b>입니다. 경쟁률이 높은 인기 공모주일수록 증거금을 많이 넣어도 비례배정에서는 한 주도 못 받는 경우가 흔합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">공모주 청약은 어떤 순서로 진행되나요</h2>

<p>공모주 청약은 대체로 아래 순서로 진행됩니다.</p>

<ol style="line-height:1.9;">
  <li><b>청약 가능 증권사 계좌 개설</b> — 공모마다 대표주관사·인수단으로 참여하는 증권사가 다르므로 청약 전에 확인이 필요합니다.</li>
  <li><b>청약 일정 확인</b> — 수요예측을 거쳐 공모가가 확정된 뒤 일반청약일(보통 2영업일)이 공지됩니다.</li>
  <li><b>청약 신청 및 증거금 납입</b> — 균등배정과 비례배정 중 원하는 신청 주수를 정해 증거금을 납입합니다.</li>
  <li><b>배정 결과 확인</b> — 청약 마감 후 균등배정(추첨 포함)과 비례배정 결과가 각각 발표됩니다.</li>
  <li><b>환불금 입금 및 상장</b> — 배정받지 못한 증거금은 환불일에 계좌로 자동 입금되고, 배정받은 주식은 상장일부터 거래할 수 있습니다.</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">최근 배정 규정이 바뀐다는데 무슨 내용인가요</h2>

<p><mark>2026년 1월 1일 이후 증권신고서를 제출하는 코스닥 상장 예정기업은 공모주의 30% 이상을 코스닥벤처펀드에 우선 배정해야 합니다.</mark> 기존 25%에서 확대된 것으로, <a href="https://www.kofia.or.kr/brd/m_211/view.do?seq=223" target="_blank" rel="noopener">금융투자협회</a>가 2025년 10월 31일 관련 규정 개정을 예고했고 같은 내용을 <a href="https://www.fsc.go.kr/no010101/85897" target="_blank" rel="noopener">금융위원회</a>도 보도자료로 확인했습니다.</p>

<p>이 규정은 <b>코스닥 공모주에만 적용</b>되며, 2028년 12월 31일까지 3년간 한시적으로 시행됩니다. 코스닥벤처펀드 우선배정은 기관투자자 배정 물량 안에서 이뤄지는 절차라, 이 글에서 다룬 일반청약자의 균등배정 50% 이상·비례배정 규정 자체가 바뀌는 것은 아닙니다. 다만 코스닥 공모주에 청약할 계획이라면 알아두면 좋은 최신 변화입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공모주 청약이란 정확히 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">새로 증시에 상장하는 기업의 주식을 증권사 계좌에 청약증거금을 넣고 신청해서, 균등배정과 비례배정 결과에 따라 배정받는 절차입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">청약 증거금은 어떻게 계산하나요</summary>
  <p style="margin:10px 0 0 0;">공모가 × 신청 주수 × 증거금률로 계산합니다. 증거금률은 대부분 50%라서, 공모가 30,000원에 200주를 신청하면 3,000,000원이 필요합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">균등배정과 비례배정은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">균등배정은 최소 증거금 이상을 낸 모든 신청자에게 동등한 배정 기회(물량이 부족하면 추첨)를 주고, 비례배정은 신청 주수를 경쟁률로 나눈 만큼(소수점 버림) 배정합니다. 배정 물량의 50% 이상이 균등배정입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">균등배정을 신청하면 무조건 1주는 받나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 균등배정 신청자 수가 균등배정 물량보다 많으면 초과분은 추첨으로 갈려 0주를 받는 신청자도 생깁니다. "동등한 배정 기회"는 동일한 확률을 뜻하지 수량 보장을 뜻하지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">청약 증거금은 언제 돌려받나요</summary>
  <p style="margin:10px 0 0 0;">배정 결과가 확정된 뒤, 배정받은 주식 금액을 뺀 나머지 증거금이 환불일에 증권사 계좌로 자동 입금됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코스닥벤처펀드 우선배정 확대는 개인 청약자와 무슨 관계가 있나요</summary>
  <p style="margin:10px 0 0 0;">2026년 1월부터 코스닥 공모주의 코스닥벤처펀드 우선배정 비율이 25%에서 30%로 확대됩니다. 이는 기관투자자 배정 물량 안에서 이뤄지는 절차라 일반청약자의 균등배정 50% 이상·비례배정 규정 자체를 바꾸지는 않지만, 코스닥 공모주 청약을 계획한다면 알아두면 좋은 최신 변화입니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://law.kofia.or.kr/service/law/lawFullScreen.do?seq=140&amp;historySeq=1728" target="_blank" rel="noopener">금융투자협회 법규정보시스템</a> - 증권 인수업무 등에 관한 규정(균등·비례배정 근거, 자동화 세션에서는 접속이 막혀 직접 확인하지 못함)</li>
    <li><a href="https://www.kofia.or.kr/brd/m_211/view.do?seq=223" target="_blank" rel="noopener">금융투자협회 보도자료</a> - 코스닥벤처펀드(벤처기업투자신탁) 공모주 우선배정확대 등 예고(2025-10-31)</li>
    <li><a href="https://www.fsc.go.kr/no010101/85897" target="_blank" rel="noopener">금융위원회 보도자료</a> - 코스닥벤처펀드 우선배정 확대 관련</li>
  </ul>
  기준일: 2026-09-17(WebSearch 확인일). 금융투자협회 법규정보시스템 원문은 이번 세션
  WebFetch가 차단돼 직접 열람하지 못했고, 대형 증권사(신한투자증권·NH투자증권·
  교보증권·삼성증권) 공식 안내가 동일한 계산 공식과 배정 비율을 고지하는 것으로
  교차검증했습니다. 코스닥벤처펀드 우선배정 확대는 독립 언론 7곳과 금융투자협회·
  금융위원회 공식 보도자료로 확인했습니다.
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
  "headline": "공모주 청약 증거금 계산 방법",
  "description": "공모주 청약증거금 계산 공식, 균등배정과 비례배정의 차이와 실제 계산 예시, 청약 절차, 2026년 코스닥벤처펀드 우선배정 확대 규정을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-17",
  "dateModified": "2026-09-17",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/ipo-subscription-deposit-calculation"
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
      "name": "공모주 청약이란 정확히 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "새로 증시에 상장하는 기업의 주식을 증권사 계좌에 청약증거금을 넣고 신청해서, 균등배정과 비례배정 결과에 따라 배정받는 절차입니다." }
    },
    {
      "@type": "Question",
      "name": "청약 증거금은 어떻게 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "공모가 × 신청 주수 × 증거금률로 계산합니다. 증거금률은 대부분 50%라서, 공모가 30,000원에 200주를 신청하면 3,000,000원이 필요합니다." }
    },
    {
      "@type": "Question",
      "name": "균등배정과 비례배정은 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "균등배정은 최소 증거금 이상을 낸 모든 신청자에게 동등한 배정 기회(물량이 부족하면 추첨)를 주고, 비례배정은 신청 주수를 경쟁률로 나눈 만큼(소수점 버림) 배정합니다. 배정 물량의 50% 이상이 균등배정입니다." }
    },
    {
      "@type": "Question",
      "name": "균등배정을 신청하면 무조건 1주는 받나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 균등배정 신청자 수가 균등배정 물량보다 많으면 초과분은 추첨으로 갈려 0주를 받는 신청자도 생깁니다. \"동등한 배정 기회\"는 동일한 확률을 뜻하지 수량 보장을 뜻하지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "청약 증거금은 언제 돌려받나요",
      "acceptedAnswer": { "@type": "Answer", "text": "배정 결과가 확정된 뒤, 배정받은 주식 금액을 뺀 나머지 증거금이 환불일에 증권사 계좌로 자동 입금됩니다." }
    },
    {
      "@type": "Question",
      "name": "코스닥벤처펀드 우선배정 확대는 개인 청약자와 무슨 관계가 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2026년 1월부터 코스닥 공모주의 코스닥벤처펀드 우선배정 비율이 25%에서 30%로 확대됩니다. 이는 기관투자자 배정 물량 안에서 이뤄지는 절차라 일반청약자의 균등배정 50% 이상·비례배정 규정 자체를 바꾸지는 않지만, 코스닥 공모주 청약을 계획한다면 알아두면 좋은 최신 변화입니다." }
    }
  ]
}
</script>
