---
keyword: 인적분할 뜻
title: 인적분할 뜻 신주배정 취득가액 계산법
slug: spinoff-share-allocation-guide
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 780 (PC 160 / 모바일 620)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-28 — 통과]
  WebSearch "인적분할 뜻 물적분할 차이 신주배정 비율" 상위 도메인:
  economist.co.kr(언론사, 2022년 기사) / korea.legal(신우법무사 wiki,
  소규모 법무사) / namu.wiki(나무위키) / narangdesign.com(한국벤처캐피탈협회
  2019년 뉴스레터, 구식) / mna.bridgecode.kr(M&A 전문 콘텐츠 사이트,
  소규모) / lgbr.co.kr(LG경영연구원 리포트).
  1) 진입 여지 — 있음. 법무사 wiki와 M&A 전문 소규모 콘텐츠 사이트가
     상위권에 있다.
  2) 검색 의도 — "뜻"을 묻는 개념 탐색형이라 조회·계산기 실행 의도가
     지배적이지 않다.
  3) 답 완결 여부 — 아니다. 상위 결과는 인적분할·물적분할의 구조적 차이
     (신주를 주주가 받는지 모회사가 받는지)까지만 다루고, 신주배정 비율을
     실제로 계산하는 예시, 취득가액 산정 공식, 2024년 12월 자사주 신주배정
     금지 개정은 다루지 않는다(경제지 기사는 2022년 작성으로 2024년 개정
     이전 시점).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
  카니벌라이제이션 점검 — 57편(물적분할 뜻과 인적분할 차이,
  spinoff-vs-carveout-difference)이 이미 인적분할·물적분할 비교표와 2022년
  9월 소수주주 3중 보호장치, 2024년 12월 이후 국회 논의 중인 신주 "우선배정"
  법안(20%안·15%안 등 미확정)을 다룬다. 이번 편이 다루는 2024-12-31 시행
  "자사주 신주배정 금지"(금융위 시행령 개정, 확정 시행)는 57편이 다룬
  국회 계류 법안과는 별개의 확정된 규정이라 겹치지 않는다. 본문에서는
  57편의 비교표를 반복하지 않고 정의만 1개 문단으로 짧게 짚은 뒤, 57편이
  다루지 않은 신주배정 계산 예시·취득가액 공식·자사주 금지 규정에 집중한다.
unique_asset: |
  (a) 인적분할 신주배정 비율 계산 예시 — 가상의 주주 지분 구성으로 인적분할
      전후 지분율이 그대로 유지됨을 실제 숫자로 보여준다.
  (b) 인적분할로 취득한 주식의 취득가액 산정 공식 — (총 취득가액 - 분할존속
      법인 주식 상당가액 + 의제배당금 등) / 분할신설법인 주식수. 소득세법
      시행령 제176조의2에 근거한 공식으로, 상위 정의형 글들은 다루지 않는다.
  (c) 2024년 12월 31일 시행된 자사주 신주배정 금지 규정("자사주 마법" 방지) —
      개정 배경과 시행일을 명시. 57편은 이를 "논의 중"으로만 다뤘으나 실제로는
      이미 확정 시행됐다는 점에서 정보가 최신화됨.
primary_source: |
  자사주 신주배정 금지 규정의 원 출처인 금융위원회 보도자료
  (fsc.go.kr/no010101/83702 추정 URL)에 WebFetch를 1회 시도했으나
  EGRESS_BLOCKED로 막혔다(2026-09-28). RULES.md 「1차 출처가 막혔을 때」
  기준에 따라 WebSearch로 독립 출처를 교차확인했다 — 대한민국 정책브리핑
  (korea.kr, 정부 공식 뉴스 채널)·한국경제·한국금융신문·뉴스1·조세일보
  (이상 언론사 4곳) 총 5곳이 전부 "2024년 12월 31일부터 상장법인 인적분할
  시 자사주 신주배정 금지"라는 핵심 사실과 시행일을 충돌 없이 보도했다.
  취득가액 계산 공식은 세정일보(언론사)와 CaseNote(국세청 해석사례 데이터
  베이스)가 동일한 공식을 인용하며 소득세법 시행령 제176조의2 제3항을
  근거로 명시해 교차확인했다(law.go.kr은 RULES.md 기준상 iframe 렌더링
  문제로 자동화 세션에서 직접 열람하지 않음). 세율·공제한도 구간처럼 과거
  오류가 발견된 유형의 숫자가 아니라 시행일이 명확한 제도 변경과 안정적인
  회계 공식이라 교차검증으로 진행했다.
기준일: 2026년 9월 기준 (2024년 12월 31일 시행된 자사주 신주배정 금지 규정이 현재까지 유효함을 교차확인)
tags: 인적분할, 물적분할, 신주배정, 자사주, 기업분할, 취득가액, 양도소득세, 주식초보
gate_pass: true
gate_pass_note: |
  게이트1 충족 — 네이버 키워드도구 실측 840회(2026-09-27, backlog.verified
  재사용, 일반 주제 기준 500회 이상 충족). 게이트2 충족 — v3 기준 3개 탈락
  조건 모두 미해당, 법무사·M&A 전문 소규모 콘텐츠가 진입 여지로 존재하며
  57편과 카니벌라이제이션 없음을 확인. 게이트3 충족 — 신주배정 비율 계산
  예시 + 취득가액 산정 공식 + 2024년 자사주 신주배정 금지 규정(57편 대비
  최신화된 정보). 게이트4 충족 — 금융위 원문은 EGRESS_BLOCKED로 막혔으나
  정책브리핑·언론 4곳이 시행일에서 충돌 없이 일치했고, 취득가액 공식은
  언론·국세청 해석사례 데이터베이스가 동일 공식·근거 조문을 인용해 교차
  검증으로 확정.
capture_guide: ""
self_check: |
  [2026-09-28 판정 — gate_pass:true]
  게이트1~4 전부 충족(gate_pass_note 참조).
  후보 선정 과정 — backlog.verified 중 "단순 순서 대기"로 명시된 항목(인적
  분할 뜻 840회, 증여세 연부연납 780회, 유보율 뜻 530회) 중 검색량이 가장
  높은 인적분할 뜻을 채택. 새 키워드 브레인스토밍·check-keywords.yml 워크
  플로 재실행은 생략(이미 검증된 대기 후보가 있었음).
  카니벌라이제이션 점검 — 57편(물적분할 뜻과 인적분할 차이)과의 중복 여부를
  serp_check에 상세 기록. 본문에서 57편이 다룬 비교표·소수주주 보호장치
  타임라인을 반복하지 않고 새 각도(신주배정 계산·취득가액 공식·자사주
  금지 확정)에 집중해 차별화했다.
  YMYL 안전장치 점검 — 특정 종목·기업명을 언급하지 않았다. 계산 예시는
  "가상의 주주"로 명시했다. 매수·매도 권유나 목표가 제시 없이 제도와 세금
  계산 방식만 설명했다.
  기관 링크 점검 — 참고 출처 3개 전부 링크 처리(정책브리핑·국세청·법제처).
  본문 내 기관 안내 문장(국세청 언급)도 링크 처리.
  제목 "인적분할 뜻 신주배정 취득가액 계산법" 20자·금지어 없음·조사/접속사
  없음(핵심어 "인적분할 뜻"이 맨 앞).
  슬러그 영문 소문자+하이픈 4단어(spinoff-share-allocation-guide).
  인트로 문단 최상단 배치, "안녕하세요" 없음.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서 "—"
  검색 결과 0개 확인. "다만"은 한 번도 쓰지 않았고 전환은 "그런데"·"단,"·
  "반면에"로 분산했다. `<mark>` 총 3개(3~5개 기준 충족). FAQ 5개(6개 고정
  탈피). 핵심 요약 박스 제목을 "🔍 인적분할, 이 4가지만 짚어두세요"로, 색은
  버건디(#fbe9ea/#8e2436)로 최근 게시물(스카이블루#1565c0·인디고#3949ab·
  바이올렛#673ab7·슬레이트네이비#2c3e50)과 겹치지 않게 골랐다. 목차 제외
  본문 H2 5개 중 서술형 3개, 질문형 2개("인적분할하면 신주는 어떻게
  배정되나요" 등)로 "~나요" 편중 없음(5개 중 2개, 40%). FAQ 헤딩도 "자주
  묻는 질문" 대신 "헷갈리기 쉬운 부분 정리"로 변형. 헤지 표현은 남발하지
  않았고 확정된 사실은 단정형("~입니다")으로 썼다. 면책 문구는 기존
  게시물과 다른 표현으로 작성.
  종합 판정: 게이트1~4 전부 충족 → gate_pass:true.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-28</p>

<p>인적분할은 회사를 나눌 때 기존 주주가 지분율 그대로 신설회사 주식을 직접 받는 방식이며, 물적분할과 달리 모회사가 신설회사 지분을 독차지하지 않습니다. 이 글은 인적분할의 뜻, 신주배정 비율 계산 방식, 취득가액 산정 공식, 2024년 말 바뀐 자사주 신주배정 규정을 정리합니다.</p>

<div style="background:#fbe9ea;border:2px solid #8e2436;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#6b1a29;font-size:18px;">🔍 인적분할, 이 4가지만 짚어두세요</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>인적분할은 신설회사 주식을 기존 주주가 지분율대로 직접 받는 방식입니다.</li>
    <li>신주는 원칙적으로 분할 전 지분율 그대로 배정됩니다.</li>
    <li>취득가액은 총 취득가액에서 존속법인 몫을 뺀 뒤 신설법인 주식 수로 나눠 계산합니다.</li>
    <li>2024년 12월 31일부터 인적분할 시 자사주에는 신주를 배정할 수 없습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">인적분할 뜻과 물적분할 차이</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">인적분할하면 신주는 어떻게 배정되나요</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">인적분할 주식 취득가액 계산법</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">인적분할 주식 세금 내는 시점</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">2024년 자사주 신주배정 금지 규정</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">헷갈리기 쉬운 부분 정리</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">인적분할 뜻과 물적분할 차이</h2>

<p>인적분할은 회사를 둘로 나누면서 신설회사 주식을 기존 주주에게 보유 지분율대로 직접 배정하는 방식입니다. 분할 전 회사와 분할 후 두 회사의 주주 구성이 동일하게 유지되는 "형제 회사" 구조가 됩니다.</p>

<p>물적분할은 이와 달리 신설회사 주식 전부를 모회사가 갖습니다. 주주 입장에서는 신설회사 주식을 직접 받지 못하고, 모회사를 통해 간접적으로만 지분을 보유하게 됩니다. 두 방식의 지배구조·소수주주 보호 장치에 대한 자세한 비교는 이미 <a href="https://sensitiveboss3.tistory.com/entry/spinoff-vs-carveout-difference" target="_blank" rel="noopener">물적분할 뜻과 인적분할 차이</a> 글에서 다뤘으므로, 이 글에서는 인적분할 자체의 신주배정과 세금 계산에 집중합니다.</p>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">인적분할하면 신주는 어떻게 배정되나요</h2>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">인적분할의 신주는 원칙적으로 분할 전 보유 지분율 그대로 배정됩니다.</span> 상법상 인적분할이 성립하려면 분할대가 전액이 주식이어야 하고, 그 주식이 기존 지분 비율에 따라 배정돼야 합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">주주</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">분할 전 A회사 지분율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">분할 후 A회사(존속) 지분율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">분할 후 B회사(신설) 지분율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">갑</td>
      <td style="border:1px solid #ddd;padding:8px;">60%</td>
      <td style="border:1px solid #ddd;padding:8px;">60%</td>
      <td style="border:1px solid #ddd;padding:8px;">60%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">을</td>
      <td style="border:1px solid #ddd;padding:8px;">25%</td>
      <td style="border:1px solid #ddd;padding:8px;">25%</td>
      <td style="border:1px solid #ddd;padding:8px;">25%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">병</td>
      <td style="border:1px solid #ddd;padding:8px;">15%</td>
      <td style="border:1px solid #ddd;padding:8px;">15%</td>
      <td style="border:1px solid #ddd;padding:8px;">15%</td>
    </tr>
  </tbody>
</table>

<p>위 표처럼 가상의 주주 갑·을·병이 분할 전 A회사에서 각각 60%, 25%, 15%를 보유했다면, 인적분할로 신설된 B회사에서도 같은 비율의 주식을 받습니다. 분할비율(존속회사와 신설회사에 배분되는 순자산 비율)에 따라 각 회사의 주식 수 자체는 달라지지만, 갑·을·병 사이의 상대적 지분율은 두 회사 모두 동일하게 유지됩니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">인적분할 주식 취득가액 계산법</h2>

<p>인적분할로 받은 신설법인 주식을 나중에 팔 때 양도차익을 계산하려면 취득가액을 알아야 합니다. <mark>1주당 취득가액은 (총 취득가액 - 분할존속법인 주식 상당가액 + 의제배당금 등) ÷ 분할신설법인 주식 수로 계산</mark>합니다. 소득세법 시행령 제176조의2 제3항에 근거한 공식입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (가상 사례)</b>
  <p style="margin:8px 0 0 0;">가상의 주주 C씨가 분할 전 A회사 주식을 1,000만원에 취득했고, 분할 후 존속법인(A) 주식 상당가액이 600만원, 신설법인(B) 주식 수가 100주라고 가정합니다. 의제배당금이 없다면 B회사 주식의 총 취득가액은 1,000만원 - 600만원 = 400만원이고, 1주당 취득가액은 400만원 ÷ 100주 = 4만원이 됩니다.</p>
</div>

<p>총 취득가액 중 일부가 불분명하면 매매사례가액이나 환산가액으로 대신 계산합니다. 정확한 금액은 거래 증권사의 매매내역서나 국세청 홈택스에서 확인하는 것이 안전합니다.</p>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">인적분할 주식 세금 내는 시점</h2>

<p>적격분할 요건(사업목적, 지분 비율 유지, 사업 계속 등)을 갖추면 분할 시점에는 세금이 과세되지 않고 이연됩니다. 실제로 세금을 내는 시점은 주주가 보유한 신설법인 주식을 팔 때입니다.</p>

<ul style="line-height:1.9;">
  <li>적격분할: 분할 시점 과세 없음, 주식 양도 시 양도소득세로 정산</li>
  <li>비적격분할: 분할 시점에 주주에게 의제배당으로 과세될 수 있음</li>
  <li>사후관리 요건(분할 후 2~3년 이내 사업 폐지·지분 처분 등) 위반 시 과세이연 취소</li>
</ul>

<p><mark>국내 상장주식은 대주주가 아니면 양도소득세 대상이 아닙니다.</mark> 따라서 일반 소액주주가 인적분할로 받은 상장주식을 파는 경우 대부분 양도소득세를 신경 쓸 필요가 없습니다. 대주주 기준이나 양도소득세 계산 방식은 <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&amp;mi=12274" target="_blank" rel="noopener">국세청 주식등 양도소득세 안내</a>에서 직접 확인할 수 있습니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">2024년 자사주 신주배정 금지 규정</h2>

<p><mark>2024년 12월 31일부터 상장법인이 인적분할할 때 회사가 보유한 자기주식(자사주)에는 신주를 배정할 수 없게 됐습니다.</mark> 금융위원회가 자본시장법 시행령을 개정해 시행한 규정입니다.</p>

<p>그동안에는 자사주에도 신주를 배정하는 관행이 있었고, 이 신주를 대주주가 확보해 지배력만 높이는 이른바 "자사주 마법"이라는 비판이 있었습니다. 개정 이후에는 자사주 몫만큼 신주 발행 자체가 줄어 대주주 지배력 강화 효과가 사라집니다.</p>

<p>이 개정은 인적분할뿐 아니라 상장법인 간 합병에서 소멸법인이 보유한 자사주에도 동일하게 적용됩니다. 반면 물적분할은 애초에 모회사가 신주 전부를 받는 구조라 이 규정의 직접적인 영향을 받지 않습니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #8e2436;padding-left:12px;margin-top:36px;">헷갈리기 쉬운 부분 정리</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">인적분할과 물적분할 중 세금 부담이 더 큰 쪽이 있나요</summary>
  <p style="margin:10px 0 0 0;">적격분할 요건을 갖추면 두 방식 모두 분할 시점에는 과세가 이연됩니다. 세금 부담의 차이는 분할 방식 자체보다 이후 주식을 언제, 어떻게 처분하느냐에 따라 달라집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">인적분할 신주는 언제 계좌에 들어오나요</summary>
  <p style="margin:10px 0 0 0;">분할신설법인의 재상장일에 기존 주식 대신(또는 함께) 신주가 계좌에 입고됩니다. 정확한 일정은 분할을 발표한 회사의 공시를 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">자사주 신주배정 금지가 소액주주에게 어떤 의미가 있나요</summary>
  <p style="margin:10px 0 0 0;">자사주에 배정됐을 신주가 발행되지 않는 만큼 전체 발행주식 수 증가가 줄어들어, 대주주 지분 쏠림이 완화되는 효과가 있습니다. 개별 종목의 주가에 미치는 영향은 회사별 상황에 따라 다르므로 일률적으로 말하기는 어렵습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">취득가액을 못 찾으면 어떻게 하나요</summary>
  <p style="margin:10px 0 0 0;">거래 증권사에 매매내역서를 요청하거나 국세청 홈택스에서 취득 당시 거래 내역을 조회할 수 있습니다. 그래도 불분명하면 매매사례가액이나 환산가액으로 대신 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비적격분할인지는 어떻게 확인하나요</summary>
  <p style="margin:10px 0 0 0;">분할 공시나 사업보고서에서 회사가 적격분할 요건 충족 여부를 밝히는 경우가 많습니다. 확실하지 않으면 회사 IR 담당 부서나 세무 전문가에게 확인하는 것이 정확합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.korea.kr/news/policyNewsView.do?newsId=148937841" target="_blank" rel="noopener">대한민국 정책브리핑 - 인적분할 시 신주배정 금지 관련 자본시장법 시행령 개정</a> (금융위 원문은 자동화 세션에서 접속 차단, 정책브리핑으로 교차확인)</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&amp;mi=12274" target="_blank" rel="noopener">국세청 - 주식등 양도소득세 안내</a></li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터 - 소득세법 시행령 제176조의2(취득가액 산정 근거)</a></li>
  </ul>
  기준일: 2026년 9월 기준.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 인적분할 제도를 설명하는 정보 글이며, 특정 종목의 매수나 매도를 권하지 않습니다. 세율과 취득가액 계산 방식은 개별 사안과 법령 개정에 따라 달라질 수 있으니, 실제 신고 전에는 반드시 국세청이나 세무 전문가를 통해 다시 확인하시기 바랍니다. 투자 판단에 따른 결과는 투자자 본인의 책임입니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "인적분할 뜻 신주배정 취득가액 계산법",
  "description": "인적분할의 뜻과 물적분할 차이, 신주배정 비율 계산 예시, 취득가액 산정 공식, 2024년 12월 시행된 자사주 신주배정 금지 규정까지 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-28",
  "dateModified": "2026-09-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/spinoff-share-allocation-guide"
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
      "name": "인적분할과 물적분할 중 세금 부담이 더 큰 쪽이 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "적격분할 요건을 갖추면 두 방식 모두 분할 시점에는 과세가 이연됩니다. 세금 부담의 차이는 분할 방식 자체보다 이후 주식을 언제, 어떻게 처분하느냐에 따라 달라집니다." }
    },
    {
      "@type": "Question",
      "name": "인적분할 신주는 언제 계좌에 들어오나요",
      "acceptedAnswer": { "@type": "Answer", "text": "분할신설법인의 재상장일에 기존 주식 대신(또는 함께) 신주가 계좌에 입고됩니다. 정확한 일정은 분할을 발표한 회사의 공시를 확인해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "자사주 신주배정 금지가 소액주주에게 어떤 의미가 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "자사주에 배정됐을 신주가 발행되지 않는 만큼 전체 발행주식 수 증가가 줄어들어, 대주주 지분 쏠림이 완화되는 효과가 있습니다. 개별 종목의 주가에 미치는 영향은 회사별 상황에 따라 다르므로 일률적으로 말하기는 어렵습니다." }
    },
    {
      "@type": "Question",
      "name": "취득가액을 못 찾으면 어떻게 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "거래 증권사에 매매내역서를 요청하거나 국세청 홈택스에서 취득 당시 거래 내역을 조회할 수 있습니다. 그래도 불분명하면 매매사례가액이나 환산가액으로 대신 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "비적격분할인지는 어떻게 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "분할 공시나 사업보고서에서 회사가 적격분할 요건 충족 여부를 밝히는 경우가 많습니다. 확실하지 않으면 회사 IR 담당 부서나 세무 전문가에게 확인하는 것이 정확합니다." }
    }
  ]
}
</script>
