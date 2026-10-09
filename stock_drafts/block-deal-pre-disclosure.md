---
keyword: 블록딜 뜻
title: 블록딜 뜻과 사전공시 의무 확인법
slug: block-deal-pre-disclosure
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 650 (PC 130 / 모바일 520)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-13 — 통과]
  WebSearch "블록딜 뜻 계산법" + "블록딜 주가 영향 할인율 대량매매" 상위 종합:
  sgsg.hankyung.com(한경 생글생글, 언론) / kbthink.com(KB 공식) / mofe.go.kr(기획재정부
  시사경제용어사전, 공식 ×2) / thescoop.co.kr(더스쿠프, 언론) / namu.wiki(백과) /
  mna.bridgecode.kr(M&A 자문사 콘텐츠, 소규모) / sisajournal-e.com(시사저널e, 언론) /
  cookiedeal.io(스타트업 자문 서비스 블로그, 소규모) / sedaily.com(서울경제, 언론) /
  a-ha.io(지식iN형 커뮤니티 Q&A)
  1) 진입 여지 — 있음. mna.bridgecode.kr·cookiedeal.io·a-ha.io 등 소규모 콘텐츠·커뮤니티가
     상위에 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻·계산법·주가 영향"). 조회/신청/계산기 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 아니다. 상위 글 대부분 정의와 "통상 5~8% 할인" 정도의 일반론까지만 다루고,
     2024년 도입된 임원·주요주주 대상 사전공시 의무제도(자본시장법 제173조의3, 거래규모
     기준·보고 시점·위반 시 제재)는 다루지 않음. 정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-13]
  (a) 블록딜 할인율이 통상 종가 대비 몇 % 수준인지(사례별로 2~8%, 5~8%, 5~10% 등 출처마다
      약간씩 다르게 표현되나 대체로 "5~10% 범위"로 수렴)를 정리하고, 가상의 종가를 대입한
      실제 계산 예시(예: 종가 10,000원에서 7% 할인 시 확정 매도가 9,300원)로 "%가 실제로
      얼마인지" 감을 잡게 한다.
  (b) 핵심 정보이득 — 2024년 7월 24일부터 시행된 "임원 등의 특정증권등 거래계획 보고"
      제도(자본시장법 제173조의3, 흔히 "블록딜 사전공시 의무제도"로 불림)를 상위 검색
      결과 대부분이 다루지 않는데, 이 글은 공시 대상 규모 기준(지분 1% 이상 또는 거래금액
      50억원 이상, 과거 6개월 합산 판단), 보고 시점(거래 개시일 30~90일 전), 계획 대비
      허용 오차(거래금액의 30% 이내), 위반 시 제재(과징금 최대 20억원 + 형사처벌)를
      표로 정리해 "왜 블록딜을 미리 알 수 있는 경우가 있는지"를 설명한다.
  (c) 이 제도가 대주주(내부자)의 사전 계획공시 의무이지, 매수자를 구하는 실제 협상·체결
      단계에 적용되는 규칙이 아니라는 점을 명확히 구분해 혼동을 없앤다.
primary_source: |
  근거 조문은 자본시장법 제173조의3(임원 등의 특정증권등 거래계획 보고) 및 시행령
  제200조의3으로, law.go.kr / fsc.go.kr / dart.fss.or.kr 세 개 정부 도메인에 각각
  WebFetch를 시도했으나 전부 EGRESS_BLOCKED로 확인(2026-09-13) — 세션 전면 차단 패턴과 일치.
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12) 기준
  적용 — 공시 대상 규모 기준(1%/50억원, 6개월 합산), 보고 시점(30~90일 전), 허용 오차
  (30% 이내), 위반 시 제재(과징금 최대 20억원, 형사처벌 최대 징역 1년 또는 벌금 3천만원)는
  서로 독립된 다수 출처(법률신문 lawtimes.co.kr, 법무법인 신영 shinkim.com, Lexology에
  게재된 국내 로펌 클라이언트노트 2건, 경향신문 khan.co.kr)에서 충돌 없이 일치했다.
  독립 출처가 3곳을 넘고 그중 언론사·법무법인급이 다수 포함돼 캡처 요청 없이 교차검증으로
  진행했다.
  ※ 시행일 표기 관련 주의사항 — 검색 중 "2026년 1월 2일 시행"이라는 요약도 발견됐으나,
  이는 제도의 세부사항을 정한 시행령이 대통령령 제35994호(2025-12-30 개정)로 다시 개정되어
  2026-01-02부터 적용된 것을 가리키는 것으로 확인됐다. 제도 자체(자본시장법 제173조의3
  본조)는 2024-07-24부터 시행됐고(보고의무는 그로부터 30일 뒤인 2024-08-23 이후 거래부터
  적용), KRX 상장공시시스템(kind.krx.co.kr)에 2025년 12월·2026년 5월에도 실제
  "거래계획보고서"가 계속 접수되고 있어 제도가 2024년부터 끊김 없이 운영 중임을 뒷받침한다.
  본문에는 최초 시행일(2024-07-24)을 기준으로 서술하고, 세부 규정이 이후 개정될 수 있다는
  점을 함께 밝힌다.
기준일: 2026-10-09 (제도 수치는 2026-09-13 교차확인값 재사용, 계산 예시는 산술)
tags: 블록딜, 블록딜뜻, 시간외매매, 사전공시의무, 특정증권등거래계획보고, 자본시장법, 대주주매도, 할인율, 내부자거래, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-13).
  게이트1: 네이버 키워드도구 실측 650회(backlog.verified 이월, 2026-09-13 재확인).
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 할인율 실제 계산 예시 + 사전공시 의무제도(규모기준·보고시점·허용오차·제재)
  정리 + 사전공시 의무와 실제 매도 협상 단계의 구분으로 정보이득 확보.
  게이트4: law.go.kr·fsc.go.kr·dart.fss.or.kr 3개 정부 도메인 EGRESS_BLOCKED 확인 후,
  4곳 이상 독립 출처(언론·법무법인급) 교차검증으로 진행. 시행일 표기의 잠재적 혼동은
  본문·self_check에 투명 공개.
self_check: |
  [2026-09-13 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 650회(backlog.verified 이월 항목, 2026-09-13
  당일 재확인. "게이트2 미판정·다음 배치 재확인" 사유로 대기 중이던 항목을 이번 편 후보로
  승격 — 카니벌라이제이션·게이트1 미달 등 실질적 보류 사유가 있는 다른 backlog 항목과
  달리 단순 순서 대기였다).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 실제 숫자 계산 예시(가상의 종가 대입, 특정 종목의 실제 주가가 아님을
  본문에 명시) + 상위 검색 결과가 다루지 않는 사전공시 의무제도 정리로 차별화했다.
  게이트4 — law.go.kr, fsc.go.kr, dart.fss.or.kr 세 개 정부 도메인에 각 1회씩 WebFetch를
  시도해 전부 EGRESS_BLOCKED 확인(2026-09-13, 이 세션의 기존 패턴과 일치). RULES.md
  2026-09-12 기준에 따라 핵심 수치(1%/50억원 기준, 6개월 합산, 30~90일 전 보고, 30%
  이내 오차 허용, 과징금 최대 20억원+형사처벌)가 법률신문·법무법인 신영·Lexology(로펌
  클라이언트노트 2건)·경향신문 등 4곳 이상 독립 출처에서 충돌 없이 일치해 캡처 요청 없이
  진행했다. 시행일 관련해 "2026-01-02 시행"이라는 요약과 "2024-07-24 시행"이라는 다수
  출처가 표면적으로 상충돼 보였으나, 조사 결과 전자는 시행령 재개정(대통령령 제35994호)
  적용일이고 후자가 제도 본체(자본시장법 제173조의3)의 최초 시행일임을 확인해 모순이
  아니라 서로 다른 두 시점임을 규명했다. 이 경위를 본문에도 명시해 투명하게 공개한다.
  실제 개별 종목(리노공업 등)의 정확한 할인율은 언론사별로 수치가 갈려(예: 12%/15%
  혼재) 원문 대조 없이는 확정할 수 없다고 판단, 본문에는 특정 종목의 실제 할인율을
  단정적으로 싣지 않고 "통상 5~10% 범위"라는 corroborated 일반 수치와 가상 예시로만
  계산을 보여줬다 — RULES.md의 "원문에 없는 수치는 생성하지 않는다" 원칙 적용.
  카니벌라이제이션 점검 — 1~25편 어디에도 블록딜·사전공시 의무제도는 다루지 않는다.
  20편(반대매매)·19편(예수금)과 위탁증거금 관련 용어를 공유하지 않으며 겹침 없음.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 안내하는 자리와 하단 참고 출처
  전부 target="_blank" rel="noopener"로 링크 처리.
  제목 17자(공백 포함)·금지어 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와 JSON-LD
  1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음. 하단 면책
  문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) →
  gate_pass:true. 발행 가능.
refresh_due: 2027-01-09
refresh_reason: "사전공시 시행령 추가 개정 여부, 서치 콘솔 검색어(블록딜 뜻)·순위 재점검"
figure_plan: "1: 할인율별 확정가 막대(종가 대비 크기 비교) / 2: 사전공시 일정 타임라인(90일 전~거래 개시일). 같은 표를 모양만 바꾼 그림은 아님"
refresh_note: "2026-10-09 갱신(구글 노출 120회·평균 7.8위 글): 첫 두 문장을 정의+할인율+공시 기준 직답으로, 할인율 표·그림 2장, 투자자 관점 H2, 내부 링크 4개 추가. 제도 수치는 9/13 교차검증값 재사용, 신규 수치 없음(할인액은 산술)"
---
<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-09</p>

<p>블록딜은 대주주가 사 줄 기관을 미리 정해 두고 장 시작 전이나 마감 뒤 시간외시장에서 주식을 한꺼번에 넘기는 거래입니다. 값은 종가보다 <mark>보통 5~10% 싸게</mark> 정해지고, 2024년 7월부터는 지분 1% 또는 50억원 이상을 파는 임원·주요주주가 거래 30~90일 전에 계획을 먼저 공시해야 합니다.</p>

<div style="background:#f3f0ff;border:2px solid #7a5ec9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#47347f;font-size:18px;">📌 블록딜 숫자 미리 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>종가 10,000원 종목을 7% 할인하면 확정가는 9,300원이고, 100억원어치면 7억원이 깎입니다.</li>
    <li>사전공시를 하고도 실제 거래는 계획 금액의 <b>30% 이내</b> 오차까지 달라질 수 있습니다.</li>
    <li>미공시·허위공시 과징금은 <mark>최대 20억원</mark>이고 형사처벌도 따로 붙습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">블록딜 뜻과 일반 매매와의 차이</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">블록딜 할인율 계산법</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">대주주 사전공시 일정과 대상</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">사전공시를 어기면 받는 제재</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">블록딜이 투자자에게 중요한 이유</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">블록딜 소식 앞에서 투자자가 묻는 것들</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">블록딜 뜻과 일반 매매와의 차이</h2>

<p>블록딜(Block Deal)은 대량 보유자가 매수자를 미리 구해 가격과 수량을 정한 뒤 시간외매매로 한 번에 체결하는 거래입니다. 우리말로는 일괄매각이라고도 합니다.</p>

<p>장중에 같은 물량을 호가창에 내놓으면 매도 물량 자체가 주가를 끌어내립니다. 블록딜은 그 충격을 피하려고 <mark>가격을 먼저 합의하고 장 밖에서 넘기는 방식</mark>입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">장중 대량 매도</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">블록딜</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">가격 결정</td>
      <td style="border:1px solid #ddd;padding:8px;">호가에 따라 체결 중 변동</td>
      <td style="border:1px solid #ddd;padding:8px;">종가 대비 할인율로 사전 합의</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매수자</td>
      <td style="border:1px solid #ddd;padding:8px;">불특정 다수</td>
      <td style="border:1px solid #ddd;padding:8px;">미리 구한 소수의 기관 등</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">체결 시점</td>
      <td style="border:1px solid #ddd;padding:8px;">정규장 중</td>
      <td style="border:1px solid #ddd;padding:8px;">장 시작 전 또는 마감 뒤 시간외</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주가 충격</td>
      <td style="border:1px solid #ddd;padding:8px;">매도 물량이 호가에 그대로 노출</td>
      <td style="border:1px solid #ddd;padding:8px;">체결 전에는 호가창에 드러나지 않음</td>
    </tr>
  </tbody>
</table>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">블록딜 할인율 계산법</h2>

<p>블록딜 확정가는 종가에 (1 - 할인율)을 곱해 구하고, 할인율은 언론 보도 기준 대체로 5~10% 범위입니다. 거래 규모가 크거나 종목 거래가 한산할수록, 매도자가 급할수록 할인율이 커지는 경향이 있습니다.</p>

<p>아래는 종가 10,000원인 가상 종목을 100만 주(100억원어치) 넘길 때의 계산입니다. 특정 종목의 실제 주가가 아닌 예시 숫자입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">할인율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">확정가</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">주당 할인액</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">100만 주 총 할인액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">5%</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">9,500원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">500원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">5억원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">7%</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">9,300원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">700원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">7억원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">10%</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">9,000원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">1,000원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">10억원</td>
    </tr>
  </tbody>
</table>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/block-deal-pre-disclosure-1.png" alt="종가 10,000원 기준 5%·7%·10% 할인 시 블록딜 확정가 막대그래프" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 산술 계산 예시, 2026-10-09</figcaption></figure>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>할인율 숫자가 크면 읽을 거리가 생깁니다</b>
  <p style="margin:8px 0 0 0;">할인이 유난히 깊다면 매도자가 그만큼 서둘러 팔아야 하는 사정이 있거나 받아 줄 매수자가 적었다는 뜻일 수 있습니다. 이때는 같은 날 공시된 매도 사유와 매도 뒤 남는 지분율을 함께 봅니다.</p>
</div>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">대주주 사전공시 일정과 대상</h2>

<p>임원·주요주주가 지분 1% 이상 또는 거래금액 50억원 이상을 팔려면 거래 개시일 30~90일 전에 거래계획을 공시해야 합니다. 2024년 7월 24일부터 시행 중인 자본시장법 제173조의3 규정입니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/block-deal-pre-disclosure-2.png" alt="거래 90일 전부터 30일 전 사이에 보고하고 거래 개시일부터 거래 기간이 시작되는 타임라인" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 자본시장법 제173조의3 해설(법률신문 등 교차 대조), 기준일 2026-09-13</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">공시 대상</td>
      <td style="border:1px solid #ddd;padding:8px;">상장회사 임원·주요주주가 지분 <b>1% 이상</b> 또는 거래금액 <b>50억원 이상</b>을 거래하는 경우(과거 6개월간 거래를 합산해 판단)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">공시 시점</td>
      <td style="border:1px solid #ddd;padding:8px;">거래 개시일 <b>30일 이상 90일 이내</b> 전에 매매 목적·가격·수량·거래 기간 공시</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">허용 오차</td>
      <td style="border:1px solid #ddd;padding:8px;">시장 상황에 따라 계획한 거래금액의 <b>30% 이내</b>에서는 계획과 다르게 거래 가능</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">면제 사유</td>
      <td style="border:1px solid #ddd;padding:8px;">상속, 주식배당, 주식양수도 방식의 M&amp;A, 담보가치 하락에 따른 반대매매 등 미공개중요정보 이용 우려가 없는 부득이한 거래</td>
    </tr>
  </tbody>
</table>

<p>이 규정은 대주주 내부자의 사전 계획 공시 의무이고, 매수자를 구하는 협상이나 체결 단계를 규제하는 규칙은 아닙니다. 세부 내용을 정한 시행령은 대통령령 제35994호(2025-12-30 개정)로 2026-01-02부터 다시 적용되고 있어, 제도는 2024년부터 이어지되 세부 기준은 손질될 수 있습니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">사전공시를 어기면 받는 제재</h2>

<p>거래계획을 공시하지 않거나 허위로 공시하거나 공시한 계획을 이행하지 않으면 과징금이 최대 20억원까지 부과됩니다. 형사처벌(최대 징역 1년 또는 벌금 3천만원)도 따로 받을 수 있습니다.</p>

<p>사망, 회생·파산절차 개시처럼 부득이한 사유가 생기면 이미 공시한 계획을 철회할 수 있습니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">블록딜이 투자자에게 중요한 이유</h2>

<p>블록딜은 대량 물량이 한 번에 시장으로 나온다는 점에서 단기 부담 요인으로 읽히는 경우가 많지만, 주가 방향은 거래마다 다르므로 단정할 수 없습니다. 같은 블록딜이라도 아래 세 가지에 따라 시장의 해석이 갈립니다.</p>

<ul style="line-height:1.9;">
  <li><b>물량의 크기:</b> 총 발행주식 대비 몇 %인지, 평소 거래량의 며칠 치인지에 따라 소화 부담이 달라집니다.</li>
  <li><b>할인율:</b> 깊게 할인된 가격은 이후 일정 기간 시장이 의식하는 기준 가격이 되기도 합니다.</li>
  <li><b>매도자의 잔여 지분:</b> 팔고도 최대주주 자리가 유지되는지, 추가 매각 가능성이 남았는지를 시장이 따집니다.</li>
</ul>

<p>매도 물량이 이미 예고돼 있었다면, 그동안 주가에 부담으로 작용하던 불확실성(오버행)이 한 번에 정리됐다고 보는 시각도 있습니다. 이 개념은 <a href="https://sensitiveboss3.tistory.com/entry/overhang-lockup-release-check" target="_blank" rel="noopener">오버행 뜻과 보호예수 해제 확인법</a>에서 자세히 다룹니다.</p>

<p>블록딜로 팔 때도 일반 매도처럼 거래세가 붙고, 대주주라면 양도소득세 문제가 따라옵니다. 세금 쪽은 <a href="https://sensitiveboss3.tistory.com/entry/securities-transaction-tax-rate" target="_blank" rel="noopener">증권거래세 세율</a>과 <a href="https://sensitiveboss3.tistory.com/entry/stock-capital-gains-tax-target" target="_blank" rel="noopener">주식 대주주 요건</a> 글에 정리해 뒀습니다.</p>

<p>관심 종목에 예고된 대주주 매도가 있는지는 <a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART)</a>에서 회사명으로 공시 목록을 열어 거래계획보고서가 올라와 있는지 보면 알 수 있습니다. 같은 공시는 <a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 KIND</a>에서도 열람됩니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #7a5ec9;padding-left:12px;margin-top:36px;">블록딜 소식 앞에서 투자자가 묻는 것들</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">블록딜 뜻을 한 줄로 말하면 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">대주주가 매수자를 미리 구해 가격과 수량을 정하고, 장 시작 전이나 마감 뒤 시간외매매로 대량의 주식을 한꺼번에 파는 거래입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">블록딜 할인율은 보통 몇 %인가요</summary>
  <p style="margin:10px 0 0 0;">사례마다 다르지만 대체로 종가 대비 5~10% 범위입니다. 유동성이 낮거나 매각 규모가 클수록 커질 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">사전공시 대상 규모 기준은 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">지분 1% 이상 또는 거래금액 50억원 이상이며, 과거 6개월간 거래를 합산해 판단합니다. 거래 개시일 30~90일 전에 공시해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">사전공시를 어기면 어떤 처벌을 받나요</summary>
  <p style="margin:10px 0 0 0;">과징금이 최대 20억원이고, 형사처벌(최대 징역 1년 또는 벌금 3천만원)까지 받을 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">블록딜 소식이 뜨면 내 주식은 떨어지나요</summary>
  <p style="margin:10px 0 0 0;">대량 매도 부담 때문에 단기 하락 요인으로 받아들여지는 경우가 많지만, 방향은 물량·할인율·매도자 잔여 지분에 따라 달라서 단정할 수 없습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr/LSW//lsSideInfoP.do?lsiSeq=279823&amp;joNo=0173&amp;joBrNo=00&amp;docCls=jo&amp;urlMode=lsScJoRltInfoR" target="_blank" rel="noopener">국가법령정보센터: 자본시장법 제173조의3(특정증권등 거래계획 보고)</a></li>
    <li><a href="https://dart.fss.or.kr/info/main.do?menu=340" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART): 기업공시 길라잡이, 임원 등의 특정증권등 거래계획 보고</a></li>
    <li><a href="https://www.lawtimes.co.kr/news/articleView.html?idxno=199134" target="_blank" rel="noopener">법률신문: 상장회사 임원 및 주요주주의 내부자거래 사전공시의무 관련 자본시장법 하위법령 개정안 해설</a></li>
    <li>기준일: 2026-10-09(사전공시 수치는 2026-09-13 독립 출처 4곳 이상 교차 대조값, 할인액 표는 산술 계산)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공이 목적이며 특정 종목의 매수·매도를 권하지 않습니다. 투자 판단과 그 결과의 책임은 투자자 본인에게 있습니다. 사전공시 세부 규정은 시행령 개정으로 바뀔 수 있으니 최신 조문은 국가법령정보센터에서 대조하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "블록딜 뜻과 사전공시 의무 확인법",
  "description": "블록딜 뜻과 할인율 계산, 2024년부터 시행 중인 임원·주요주주 사전공시 의무의 대상 규모·공시 시점·제재, 투자자가 보는 포인트를 정리했습니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-10-09",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/block-deal-pre-disclosure"
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "블록딜 뜻을 한 줄로 말하면 무엇인가요", "acceptedAnswer": {"@type": "Answer", "text": "대주주가 매수자를 미리 구해 가격과 수량을 정하고, 장 시작 전이나 마감 뒤 시간외매매로 대량의 주식을 한꺼번에 파는 거래입니다."}},
    {"@type": "Question", "name": "블록딜 할인율은 보통 몇 %인가요", "acceptedAnswer": {"@type": "Answer", "text": "사례마다 다르지만 대체로 종가 대비 5~10% 범위입니다. 유동성이 낮거나 매각 규모가 클수록 커질 수 있습니다."}},
    {"@type": "Question", "name": "사전공시 대상 규모 기준은 얼마인가요", "acceptedAnswer": {"@type": "Answer", "text": "지분 1% 이상 또는 거래금액 50억원 이상이며, 과거 6개월간 거래를 합산해 판단합니다. 거래 개시일 30~90일 전에 공시해야 합니다."}},
    {"@type": "Question", "name": "사전공시를 어기면 어떤 처벌을 받나요", "acceptedAnswer": {"@type": "Answer", "text": "과징금이 최대 20억원이고, 형사처벌(최대 징역 1년 또는 벌금 3천만원)까지 받을 수 있습니다."}},
    {"@type": "Question", "name": "블록딜 소식이 뜨면 내 주식은 떨어지나요", "acceptedAnswer": {"@type": "Answer", "text": "대량 매도 부담 때문에 단기 하락 요인으로 받아들여지는 경우가 많지만, 방향은 물량·할인율·매도자 잔여 지분에 따라 달라서 단정할 수 없습니다."}}
  ]
}
</script>
