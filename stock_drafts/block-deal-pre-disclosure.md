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
기준일: 2026-09-13 (WebSearch 확인일)
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
---

<p>블록딜은 대주주가 <mark>장이 열리기 전이나 끝난 뒤 시간외거래로 대량의 주식을 한꺼번에 파는 것</mark>을 말합니다. 그런데 정작 몰랐던 사실은, 2024년부터는 이런 대량매도를 하기 전에 <mark>미리 공시해야 하는 의무</mark>가 생겼다는 점입니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>블록딜은 대주주가 시간외에 대량의 주식을 매수자와 미리 가격·수량을 정해 일괄 매도하는 거래로, 종가 대비 <b>통상 5~10% 정도 할인</b>된 가격에 이뤄집니다.</li>
    <li>2024년 7월 24일부터는 임원·주요주주가 <mark>지분 1% 이상 또는 거래금액 50억원 이상</mark>을 팔려면, 거래 개시일 <b>30~90일 전에</b> 거래계획을 미리 공시해야 합니다.</li>
    <li>계획을 어기고 몰래 팔거나 허위로 공시하면 <mark>과징금 최대 20억원</mark>과 형사처벌까지 받을 수 있습니다.</li>
    <li>다만 이 사전공시는 대주주(내부자)에게만 적용되는 의무이고, 매수자를 찾는 실제 협상·체결 절차 자체를 규제하는 것은 아닙니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>블록딜이란 무엇인가요</li>
  <li>블록딜 할인율은 어떻게 계산하나요</li>
  <li>블록딜을 하기 전에 왜 미리 공시해야 하나요</li>
  <li>사전공시 의무를 위반하면 어떻게 되나요</li>
  <li>블록딜 소식이 뜨면 주가는 어떻게 되나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">블록딜이란 무엇인가요</h2>

<p>블록딜(Block Deal)은 주식을 대량으로 보유한 매도자가 <b>사전에 매수자를 구해</b> 가격과 수량을 미리 정해두고, 장이 열리기 전이나 끝난 뒤 <mark>시간외매매로 한꺼번에 거래</mark>하는 방식입니다. 우리말로는 일괄매각이라고도 부릅니다.</p>

<p>일반 장중 거래로 대량의 물량을 팔면 매도 압력 자체가 주가를 크게 떨어뜨릴 수 있습니다. 블록딜은 이런 <mark>시장 충격을 피하기 위해</mark> 가격과 물량을 미리 정해두고 거래하는 방법입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">블록딜 할인율은 어떻게 계산하나요</h2>

<p>블록딜 가격은 보통 <mark>전일 또는 당일 종가를 기준으로 일정 비율 할인</mark>해서 정해집니다. 할인율은 거래 규모, 종목의 유동성, 매도자가 얼마나 급하게 팔아야 하는지에 따라 달라지며, 사례마다 2~8%, 5~8% 등으로 조금씩 다르게 보도되지만 대체로 <b>5~10% 범위</b>에 걸쳐 있습니다.</p>

<p>%로만 보면 감이 잘 안 오니, 예시로 계산해봅니다. 어떤 종목의 종가가 <b>10,000원</b>이고 할인율이 <b>7%</b>로 정해졌다면, 실제 블록딜 확정가는 <mark>10,000원 × (1-0.07) = 9,300원</mark>입니다. (이 10,000원은 계산을 보여주기 위한 예시 숫자이며 특정 종목의 실제 주가가 아닙니다.)</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>할인율이 너무 크면 오히려 신호가 될 수 있습니다</b>
  <p style="margin:8px 0 0 0;">할인율이 지나치게 높으면 "매도자가 그만큼 급하게 팔아야 할 사정이 있다"는 뜻으로 해석되기도 해, 해당 기업의 상황에 대한 의구심을 키울 수 있습니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">블록딜을 하기 전에 왜 미리 공시해야 하나요</h2>

<p>2024년 7월 24일부터 자본시장법 제173조의3에 따라 <mark>임원·주요주주(내부자)의 특정증권등 거래계획 사전공시 제도</mark>가 시행되고 있습니다. 이전에는 대주주가 예고 없이 블록딜을 진행해 일반 투자자가 뒤늦게 알고 손해를 보는 사례가 많았는데, 이를 막기 위해 도입된 제도입니다.</p>

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
      <td style="border:1px solid #ddd;padding:8px;">거래 개시일 <b>30일 이상 90일 이내</b> 전에 매매목적·가격·수량·거래기간 공시</td>
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

<p>이 제도의 세부 내용을 정한 시행령은 그 뒤로도 몇 차례 개정됐습니다. 가장 최근에는 대통령령 제35994호(2025-12-30 개정)가 2026-01-02부터 적용되고 있어, <mark>제도 자체는 2024년부터 계속 운영 중이지만 세부 규정은 계속 손질되고 있다</mark>는 점을 함께 알아두는 게 좋습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">사전공시 의무를 위반하면 어떻게 되나요</h2>

<p>거래계획을 아예 공시하지 않거나, 허위로 공시하거나, 공시한 계획을 이행하지 않으면 <mark>과징금 최대 20억원</mark>이 부과될 수 있습니다. 여기에 더해 형사처벌(최대 징역 1년 또는 벌금 3천만원)까지 받을 수 있어 처벌 수위가 낮지 않습니다.</p>

<p>부득이한 사유(사망, 회생·파산절차 개시, 공동관리절차 개시 등)가 생기면 이미 공시한 거래계획을 철회할 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">블록딜 소식이 뜨면 주가는 어떻게 되나요</h2>

<p>블록딜은 규모와 할인율, 매도 의도에 따라 정도는 다르지만 통상 <mark>주가에 단기 악재로 작용</mark>합니다. 대량의 매도 물량이 시장에 나왔다는 사실 자체가 투자심리에 부담을 주기 때문입니다.</p>

<p>다만 사전공시 제도 덕분에 지분 1% 또는 거래금액 50억원이 넘는 내부자 거래는 최소 30일 전부터 공시된 내용을 확인할 수 있게 됐습니다. 관심 있는 종목이 있다면 갑작스러운 소식보다는, 사전공시 여부를 미리 챙겨보는 습관이 도움이 됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">블록딜이 뭔가요</summary>
  <p style="margin:10px 0 0 0;">대주주가 매수자를 미리 구해 가격과 수량을 정해두고, 장 시작 전이나 끝난 뒤 시간외매매로 대량의 주식을 한꺼번에 파는 거래입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">블록딜 할인율은 보통 몇 %인가요</summary>
  <p style="margin:10px 0 0 0;">사례마다 다르지만 대체로 종가 대비 5~10% 범위에서 할인된 가격으로 거래됩니다. 유동성이 낮거나 매각 규모가 클수록 할인율이 더 커질 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">왜 블록딜을 미리 공시해야 하나요</summary>
  <p style="margin:10px 0 0 0;">2024년 7월 24일 시행된 자본시장법 제173조의3에 따라, 임원·주요주주가 예고 없이 대량매도해 일반 투자자가 피해를 보는 것을 막기 위해 사전공시 의무가 도입됐습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">사전공시 대상 규모 기준은 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">지분 1% 이상 또는 거래금액 50억원 이상을 거래하는 경우이며, 과거 6개월간 거래수량·거래금액을 합산해 판단합니다. 거래 개시일 30~90일 전에 공시해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">사전공시를 위반하면 어떤 처벌을 받나요</summary>
  <p style="margin:10px 0 0 0;">미공시, 허위공시, 계획 미이행 시 과징금 최대 20억원이 부과될 수 있고, 형사처벌(최대 징역 1년 또는 벌금 3천만원)까지 받을 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">블록딜 소식이 뜨면 제가 가진 주식에 영향이 있나요</summary>
  <p style="margin:10px 0 0 0;">보유 종목에 블록딜 소식이 나오면 대량 매도 물량 부담으로 단기적으로 주가가 하락하는 경우가 많습니다. 다만 사전공시 제도 덕분에 일정 규모 이상 거래는 최소 30일 전부터 공시 내용을 확인할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.law.go.kr/LSW//lsSideInfoP.do?lsiSeq=279823&amp;joNo=0173&amp;joBrNo=00&amp;docCls=jo&amp;urlMode=lsScJoRltInfoR" target="_blank" rel="noopener">국가법령정보센터: 자본시장법 제173조의3(특정증권등 거래계획 보고)</a></li>
    <li><a href="https://dart.fss.or.kr/info/main.do?menu=340" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART): 기업공시 길라잡이: 임원 등의 특정증권등 거래계획 보고</a></li>
    <li><a href="https://www.lawtimes.co.kr/news/articleView.html?idxno=199134" target="_blank" rel="noopener">법률신문: 상장회사 임원 및 주요주주의 내부자거래 사전공시의무 관련 자본시장법 하위법령 개정안 해설</a></li>
    <li>기준일: 2026-09-13(WebSearch 확인일, 법률신문·법무법인·경향신문 등 독립 출처 4곳 이상 교차 확인)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 판단과 그 결과에 대한 책임은 본인에게 있습니다. 사전공시 의무제도의 세부 규정은 시행령 개정에 따라 계속 바뀔 수 있으므로, 최신 내용은 국가법령정보센터나 금융감독원 전자공시시스템에서 반드시 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "블록딜 뜻과 사전공시 의무 확인법",
  "description": "블록딜의 뜻과 할인율 계산 방법, 2024년부터 시행 중인 임원·주요주주 사전공시 의무제도의 대상 규모·보고 시점·위반 시 제재를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-09-13",
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
    {
      "@type": "Question",
      "name": "블록딜이 뭔가요",
      "acceptedAnswer": { "@type": "Answer", "text": "대주주가 매수자를 미리 구해 가격과 수량을 정해두고, 장 시작 전이나 끝난 뒤 시간외매매로 대량의 주식을 한꺼번에 파는 거래입니다." }
    },
    {
      "@type": "Question",
      "name": "블록딜 할인율은 보통 몇 %인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "사례마다 다르지만 대체로 종가 대비 5~10% 범위에서 할인된 가격으로 거래됩니다. 유동성이 낮거나 매각 규모가 클수록 할인율이 더 커질 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "왜 블록딜을 미리 공시해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2024년 7월 24일 시행된 자본시장법 제173조의3에 따라, 임원·주요주주가 예고 없이 대량매도해 일반 투자자가 피해를 보는 것을 막기 위해 사전공시 의무가 도입됐습니다." }
    },
    {
      "@type": "Question",
      "name": "사전공시 대상 규모 기준은 얼마인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "지분 1% 이상 또는 거래금액 50억원 이상을 거래하는 경우이며, 과거 6개월간 거래수량·거래금액을 합산해 판단합니다. 거래 개시일 30~90일 전에 공시해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "사전공시를 위반하면 어떤 처벌을 받나요",
      "acceptedAnswer": { "@type": "Answer", "text": "미공시, 허위공시, 계획 미이행 시 과징금 최대 20억원이 부과될 수 있고, 형사처벌(최대 징역 1년 또는 벌금 3천만원)까지 받을 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "블록딜 소식이 뜨면 제가 가진 주식에 영향이 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "보유 종목에 블록딜 소식이 나오면 대량 매도 물량 부담으로 단기적으로 주가가 하락하는 경우가 많습니다. 다만 사전공시 제도 덕분에 일정 규모 이상 거래는 최소 30일 전부터 공시 내용을 확인할 수 있습니다." }
    }
  ]
}
</script>
