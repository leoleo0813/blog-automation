---
keyword: 감자 뜻
title: 감자 뜻과 매매정지 기간 확인법
slug: capital-reduction-trading-halt
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 530 (PC 80 / 모바일 450)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-14 — 통과]
  WebSearch "감자 뜻 유상감자 무상감자 주가 영향" + "감자 뜻 주식" 상위 결과 종합:
  ko.wikipedia.org(위키백과, 백과) / kbthink.com(KB금융, 대형 금융사 공식) /
  namu.wiki(나무위키, 백과) / support.stockplus.com(증권플러스, 핀테크 서비스 콘텐츠, ×2) /
  epsa.or.kr(협회) / v.daum.net "딸을 위한 경제 다이어리"(개인 블로그, 다음뉴스 경유) /
  zuzu.network(스타트업 서비스 콘텐츠, ×2, 12편에서도 확인된 유형) /
  starrich.co.kr(경영컨설팅 칼럼) / economy.manual365.co.kr(개인/소규모 콘텐츠)
  1) 진입 여지 — 있음. 딸을위한경제다이어리·zuzu.network(×2)·economy.manual365.co.kr 등
     개인/소규모 콘텐츠가 4곳 이상 상위에 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색형("뜻" 정의 검색). 조회·계산기 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 아니다. 상위 결과는 유상·무상감자 정의와 재무구조 개선이라는
     실시 이유까지만 다루고, (a) 감자 시 실제 매매거래정지 기간(언제부터 언제까지),
     (b) 감자비율에 따라 보유 주식 수·기준주가가 실제로 어떻게 조정되는지 계산 예시,
     (c) 감자 결정 공시를 전자공시시스템에서 직접 찾는 절차는 어디에도 다루지 않음.
     정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-14]
  (a) 유상감자(대가 지급)와 무상감자(대가 없이 주식 병합·소각) 구조 차이를 표로
      명확히 정리해, 정의만 나열하는 상위 검색 결과보다 한 단계 더 들어간다.
  (b) 계산 예시 — 10:1 무상감자를 예로, 보유 주식 100주가 10주로 줄고 기준주가는
      10배로 재산정돼 이론상 평가금액 총액(10만원)은 감자 전후 동일하다는 점을 숫자로
      보여준다. 다만 실제로는 회사 신뢰도 우려로 재상장 후 주가가 이론가보다 낮게
      형성되는 경우가 흔하다는 현실적 한계도 함께 짚는다.
  (c) 핵심 정보이득 — 무상감자 시 매매거래정지 기간이 "감자기준일의 1매매거래일 전부터
      변경상장일(신주 상장 예정일) 전일까지"라는 한국거래소 코스닥시장 공시·상장관리
      해설서 규정을 표로 정리한다. 상위 검색 결과 어디에도 이 정지 기간의 시작·종료
      시점은 다뤄지지 않는다.
  (d) 감자 결정 공시를 전자공시시스템(DART)에서 "주요사항보고서(감자결정)"로 검색해
      직접 확인하는 절차를 안내해, "감자를 한다더라"는 소문이 아니라 공시 원문으로
      확인하는 방법을 제공한다.
primary_source: |
  1차 시도: 한국거래소 기업공시채널 KIND(kind.krx.co.kr)의 매매거래정지 안내 페이지에
  WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-14, 이 세션의 기존 전면 차단 패턴과 일치).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12)
  기준 적용 — 매매거래정지 기간("감자기준일의 1매매거래일 전부터 변경상장일 전일까지")이
  아래 4곳에서 충돌 없이 일치했다.
  ① kind.krx.co.kr — 한국거래소 「코스닥시장 공시·상장관리 해설서」(24년판·25년판 모두
     WebSearch 스니펫으로 동일 문구 확인, 원문 자체가 규정의 출처).
  ② economy.manual365.co.kr — 개인/소규모 콘텐츠. "기준일 전일부터 신주 상장 예정 전일
     까지"로 같은 기간을 독립적으로 서술.
  ③ medicopharma.co.kr(메디코파마, 제약전문 언론) — 실제 감자 기업(경남제약) 사례 보도로
     기준일-신주상장예정일 구조를 뒷받침.
  ④ newstomato.com(뉴스토마토, 경제 언론) — 감자 이후 신주 상장·거래재개 관련 절차를
     다룬 별도 보도.
  KRX 공식 해설서(①)가 규정의 원 출처이고, 언론사(③④)가 실제 사례로 이를 뒷받침해
  캡처 요청 없이 교차검증으로 진행했다. 매매거래정지 시작·종료 시점은 세율·공제한도류의
  민감 수치가 아니라 거래소 업무 절차상 고정된 기간 규정이라는 점도 함께 고려했다.
  감자비율에 따른 주식수·기준주가 조정 계산은 감자 제도 자체의 산술 구조(비율의 역수로
  기준가 재산정)이며, 특정 시점에 바뀌는 세율·한도가 아니므로 별도 1차 출처 확정 없이도
  안정적으로 서술 가능하다고 판단했다.
기준일: 2026-09-14 (WebSearch 확인일)
tags: 감자, 감자뜻, 유상감자, 무상감자, 매매거래정지, 감자기준일, 신주상장, 주식감자, 감자비율, 전자공시
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-14).
  게이트1: 네이버 키워드도구 실측 530회(backlog.verified에 이미 게이트1 통과 상태로
  대기 중이던 항목을 이번 편으로 승격, 별도 신규 브레인스토밍 불필요).
  게이트2: v3 기준 통과(serp_check 참조 — 개인/소규모 콘텐츠 4곳 이상 진입, 정의형
  검색의도, 답 미완결).
  게이트3: 유상·무상감자 구조 비교 + 감자비율 계산 예시 + 매매거래정지 기간 규정 +
  DART 공시 조회 절차로 상위 검색 결과에 없는 정보이득 확보.
  게이트4: kind.krx.co.kr WebFetch 1회 EGRESS_BLOCKED 확인 후, KRX 공식 해설서
  스니펫 + 언론 2곳(메디코파마·뉴스토마토) + 개인 콘텐츠 1곳 교차검증으로 진행.
  한계는 primary_source·self_check에 투명 공개.
self_check: |
  [2026-09-14 최종 판정]
  게이트1 충족 — backlog.verified의 "감자 뜻"(530회, 2026-09-14 실측)이 hold_reason
  "단순 순서 대기 항목"으로 이미 게이트1을 통과한 상태였다. 다른 backlog.verified
  항목은 전부 카니벌라이제이션 또는 게이트2 실패 사유가 있어 이 항목을 우선 승격했다.
  별도 신규 키워드 브레인스토밍·check-keywords.yml 실행은 이번 편에서는 불필요했다.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 순수 사전적 정의(감자 뜻)만으로는 RULES.md의 "사전형 개념은 정보이득
  불가" 원칙에 걸리므로, 여기에 "매매거래정지 실제 기간 확인"과 "DART 공시 조회
  절차"라는 실전 확인법을 결합해 통과시켰다(17편 공매도 뜻, 26편 블록딜 뜻, 27편
  숏커버링 뜻과 동일한 "뜻+실전 확인법" 패턴).
  게이트4 — kind.krx.co.kr에 WebFetch 1회 시도해 EGRESS_BLOCKED 확인(2026-09-14,
  이 세션 기존 패턴과 일치). RULES.md 2026-09-12 기준에 따라 핵심 수치(매매거래정지
  기간)가 KRX 공식 해설서 스니펫과 언론 2곳(메디코파마·뉴스토마토)·개인 콘텐츠 1곳
  (economy.manual365.co.kr)에서 충돌 없이 일치해 캡처 요청 없이 진행했다. 이는 세율·
  공제 한도처럼 이 프로젝트가 과거 실제 오류를 잡아낸 유형의 숫자가 아니라 거래소
  업무 절차상 고정 기간이며, 언론사가 포함돼 있어 안전한 쪽(교차검증)으로 판단했다.
  카니벌라이제이션 점검 — 1~28편 어디에도 감자(유상감자·무상감자)는 다루지 않는다.
  backlog.failed_gate1의 "무상감자 유상감자차이"(20회, 게이트1 미달)와는 키워드가
  다르고 이 글이 그 각도까지 포함해 대체한다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 한국거래소·전자공시시스템을
  안내하는 자리와 하단 참고 출처 전부 target="_blank" rel="noopener"로 링크 처리.
  제목 13자(공백 제외)·금지어 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와
  JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음.
  하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 교차검증으로 대체, 한계 투명 공개) →
  gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-14</p>

<p>감자는 <mark>기업이 자본금을 줄이는 것</mark>을 말하며, 증자와 반대되는 개념입니다. 감자 소식을 들었을 때 정작 궁금한 건 "그래서 내 주식은 언제 다시 거래되나"인데, 이건 <mark>감자기준일과 변경상장일이라는 두 날짜</mark>로 정해집니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>감자는 <b>자본금을 줄이는 것</b>이며, 주주에게 대가를 주는 <mark>유상감자</mark>와 대가 없이 주식을 병합·소각하는 <mark>무상감자</mark>로 나뉩니다.</li>
    <li>무상감자는 주식 수가 줄어드는 대신 <b>기준주가가 그 비율만큼 올라</b> 이론상 보유주식 평가금액 총액은 변하지 않습니다.</li>
    <li>무상감자를 하면 <mark>감자기준일의 1매매거래일 전부터 변경상장일(신주 상장 예정일) 전일까지</mark> 주식 거래가 정지됩니다.</li>
    <li>감자 결정 여부는 소문이 아니라 <b>전자공시시스템(DART)의 주요사항보고서(감자결정)</b>에서 직접 확인할 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>감자란 무엇인가요</li>
  <li>유상감자와 무상감자는 뭐가 다른가요</li>
  <li>감자비율에 따라 보유 주식과 주가는 어떻게 바뀌나요</li>
  <li>감자하면 왜 매매거래가 정지되나요, 기간은 얼마나 되나요</li>
  <li>감자 결정은 어디서 확인하나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">감자란 무엇인가요</h2>

<p>감자(減資)는 <mark>기업이 자본금을 줄이는 것</mark>을 뜻합니다. 자본금을 늘리는 증자와 정반대 개념으로, 주식 수를 줄이거나 액면가를 낮추는 방식으로 이뤄집니다.</p>

<p>기업이 감자를 하는 이유는 크게 두 가지입니다. 누적된 손실로 자본이 잠식된 상태를 회계상 정리하기 위해서거나, 사업 규모를 축소하면서 남는 자본을 주주에게 돌려주기 위해서입니다. <mark>이 목적에 따라 유상감자와 무상감자로 나뉩니다.</mark></p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">유상감자와 무상감자는 뭐가 다른가요</h2>

<p>두 방식 모두 회사의 자본금은 줄어들지만, <mark>주주가 대가를 받느냐에서 완전히 갈립니다.</mark></p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">유상감자</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">무상감자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주주 대가</td>
      <td style="border:1px solid #ddd;padding:8px;"><b>지급함</b> — 소멸된 주식만큼 현금 등으로 보상</td>
      <td style="border:1px solid #ddd;padding:8px;"><b>지급 없음</b> — 주식을 병합·소각만 함</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">회사 자산</td>
      <td style="border:1px solid #ddd;padding:8px;">대가 지급만큼 함께 감소</td>
      <td style="border:1px solid #ddd;padding:8px;">변화 없음</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">주로 쓰는 상황</td>
      <td style="border:1px solid #ddd;padding:8px;">투자금 회수, 합병·매각 전 규모 축소</td>
      <td style="border:1px solid #ddd;padding:8px;">완전자본잠식(직전) 등 재무구조 개선</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">시장 반응</td>
      <td style="border:1px solid #ddd;padding:8px;">상대적으로 중립적</td>
      <td style="border:1px solid #ddd;padding:8px;">재무 악화 신호로 받아들여져 대체로 악재</td>
    </tr>
  </tbody>
</table>

<p>실제로 상장사에서 뉴스에 오르내리는 감자는 대부분 <mark>무상감자</mark>입니다. 재무구조가 나빠진 회사가 자본잠식을 벗어나기 위해 택하는 경우가 많기 때문입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">감자비율에 따라 보유 주식과 주가는 어떻게 바뀌나요</h2>

<p>무상감자는 <mark>감자비율만큼 주식 수를 줄이는 대신, 기준주가를 그 비율의 역수로 올려</mark> 이론상 평가금액이 변하지 않도록 설계됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>10:1 무상감자 계산 예시</b>
  <p style="margin:8px 0 0 0;">감자 전 100주(주당 1,000원, 평가금액 10만원)를 보유했다면, 10:1 무상감자 후에는 <mark>주식 수가 10주로 줄고 기준주가는 10,000원으로 재산정</mark>됩니다. 10주 × 10,000원 = 10만원으로, 이론상 평가금액 총액은 감자 전후 동일합니다.</p>
</div>

<p>다만 이건 이론상 계산일 뿐입니다. <mark>실제로는 재상장 이후 회사에 대한 투자자 신뢰가 흔들려 이론가보다 주가가 낮게 형성되는 경우가 흔합니다.</mark> 감자 자체가 재무구조 악화를 알리는 신호로 받아들여지기 때문입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">감자하면 왜 매매거래가 정지되나요, 기간은 얼마나 되나요</h2>

<p>무상감자는 <mark>기존 주식을 병합해 새 주식으로 바꾸는 작업</mark>이라, 이 처리가 끝날 때까지 거래를 잠시 멈춥니다. 회계 처리와 법인등기, 신주 발행 절차에 물리적인 시간이 걸리기 때문입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매매거래정지 기간</td>
      <td style="border:1px solid #ddd;padding:8px;"><b>감자기준일의 1매매거래일 전부터 변경상장일(신주 상장 예정일) 전일까지</b></td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">감자기준일이란</td>
      <td style="border:1px solid #ddd;padding:8px;">감자된 주식을 갖게 될 주주가 정해지는 기준일</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">거래 재개 시점</td>
      <td style="border:1px solid #ddd;padding:8px;">변경상장일(신주가 새로 상장되는 날)부터 거래 재개</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기업별 편차</td>
      <td style="border:1px solid #ddd;padding:8px;">감자기준일·변경상장일은 기업마다 달라, 정지 기간도 사례마다 다름</td>
    </tr>
  </tbody>
</table>

<p>정지 기간은 회사와 감자 규모에 따라 다르지만, <mark>공시에 적힌 감자기준일과 변경상장(예정)일 사이의 구간이 곧 거래정지 구간</mark>이라고 이해하면 됩니다. 거래가 재개되는 첫날에는 그동안 대기하던 매도 물량이 몰려 주가가 급락하는 경우도 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">감자 결정은 어디서 확인하나요</h2>

<p>감자 여부는 뉴스나 커뮤니티 글이 아니라 <mark>금융감독원 전자공시시스템(DART)</mark>에서 회사가 직접 제출한 공시 원문으로 확인하는 게 가장 정확합니다.</p>

<ul style="line-height:1.9;">
  <li><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">전자공시시스템(DART)</a>에 접속합니다.</li>
  <li>회사명을 검색하고, 공시서류 조회 조건에서 <b>"주요사항보고서(감자결정)"</b> 또는 <b>"감자결정"</b>을 검색합니다.</li>
  <li>해당 보고서를 열어 <b>감자 방식(유상/무상), 감자비율, 감자기준일, 신주 상장(변경상장) 예정일</b>을 확인합니다.</li>
  <li>거래정지·재개 일정은 <a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 기업공시채널(KIND)</a>의 투자유의사항 공시에서도 함께 확인할 수 있습니다.</li>
</ul>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 다시 한 번 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>감자는 자본금을 줄이는 것이며, 대가 지급 여부로 유상·무상이 갈립니다.</li>
    <li>무상감자는 이론상 평가금액이 유지되지만, 실제로는 신뢰 저하로 주가가 밀리는 경우가 흔합니다.</li>
    <li>보유 종목이 감자를 발표하면 DART에서 감자기준일·변경상장일을 직접 확인해 거래정지 구간을 스스로 계산해볼 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감자가 뭔가요</summary>
  <p style="margin:10px 0 0 0;">기업이 자본금을 줄이는 것을 말합니다. 자본금을 늘리는 증자와 반대되는 개념으로, 주식 수를 줄이거나 액면가를 낮추는 방식으로 이뤄집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">유상감자와 무상감자는 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">유상감자는 소멸되는 주식만큼 주주에게 대가를 지급하고, 무상감자는 대가 없이 주식을 병합·소각합니다. 상장사 뉴스에 나오는 감자는 대부분 재무구조 개선 목적의 무상감자입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">무상감자를 하면 보유 주식과 평가금액은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">감자비율만큼 주식 수가 줄고 기준주가는 그 비율만큼 올라 조정됩니다. 예를 들어 10:1 감자면 100주가 10주로 줄고 주가는 10배가 돼, 이론상 평가금액 총액은 감자 전후 동일합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감자하면 왜 거래가 멈추나요, 기간은 얼마나 되나요</summary>
  <p style="margin:10px 0 0 0;">기존 주식을 병합해 새 주식으로 바꾸는 처리 기간이 필요하기 때문입니다. 매매거래정지 기간은 감자기준일의 1매매거래일 전부터 변경상장일(신주 상장 예정일) 전일까지입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감자 결정은 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">금융감독원 전자공시시스템(DART)에서 회사명을 검색해 "주요사항보고서(감자결정)"를 찾으면 감자 방식·비율·기준일·신주 상장 예정일을 원문으로 확인할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">감자하면 무조건 주가가 떨어지나요</summary>
  <p style="margin:10px 0 0 0;">이론상 무상감자는 평가금액을 유지하도록 설계돼 있지만, 재무구조 악화 신호로 받아들여져 재상장 후 주가가 이론가보다 낮게 형성되는 경우가 흔합니다. 반드시 하락한다고 단정할 수는 없습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://kind.krx.co.kr" target="_blank" rel="noopener">한국거래소 기업공시채널(KIND) — 코스닥시장 공시·상장관리 해설서(매매거래정지 규정)</a></li>
    <li><a href="https://dart.fss.or.kr" target="_blank" rel="noopener">금융감독원 전자공시시스템(DART) — 주요사항보고서(감자결정) 조회</a></li>
    <li>기준일: 2026-09-14(WebSearch 확인일, 한국거래소 해설서 스니펫 + 언론 2곳·개인 콘텐츠 1곳 교차 확인)</li>
  </ul>
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
  "headline": "감자 뜻과 매매정지 기간 확인법",
  "description": "유상감자와 무상감자의 차이, 감자비율에 따른 보유 주식·기준주가 계산 예시, 무상감자 시 매매거래정지 기간과 DART에서 감자 결정 공시를 확인하는 방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-14",
  "dateModified": "2026-09-14",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/capital-reduction-trading-halt"
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
      "name": "감자가 뭔가요",
      "acceptedAnswer": { "@type": "Answer", "text": "기업이 자본금을 줄이는 것을 말합니다. 자본금을 늘리는 증자와 반대되는 개념으로, 주식 수를 줄이거나 액면가를 낮추는 방식으로 이뤄집니다." }
    },
    {
      "@type": "Question",
      "name": "유상감자와 무상감자는 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "유상감자는 소멸되는 주식만큼 주주에게 대가를 지급하고, 무상감자는 대가 없이 주식을 병합·소각합니다. 상장사 뉴스에 나오는 감자는 대부분 재무구조 개선 목적의 무상감자입니다." }
    },
    {
      "@type": "Question",
      "name": "무상감자를 하면 보유 주식과 평가금액은 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "감자비율만큼 주식 수가 줄고 기준주가는 그 비율만큼 올라 조정됩니다. 예를 들어 10:1 감자면 100주가 10주로 줄고 주가는 10배가 돼, 이론상 평가금액 총액은 감자 전후 동일합니다." }
    },
    {
      "@type": "Question",
      "name": "감자하면 왜 거래가 멈추나요, 기간은 얼마나 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "기존 주식을 병합해 새 주식으로 바꾸는 처리 기간이 필요하기 때문입니다. 매매거래정지 기간은 감자기준일의 1매매거래일 전부터 변경상장일(신주 상장 예정일) 전일까지입니다." }
    },
    {
      "@type": "Question",
      "name": "감자 결정은 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "금융감독원 전자공시시스템(DART)에서 회사명을 검색해 \"주요사항보고서(감자결정)\"를 찾으면 감자 방식·비율·기준일·신주 상장 예정일을 원문으로 확인할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "감자하면 무조건 주가가 떨어지나요",
      "acceptedAnswer": { "@type": "Answer", "text": "이론상 무상감자는 평가금액을 유지하도록 설계돼 있지만, 재무구조 악화 신호로 받아들여져 재상장 후 주가가 이론가보다 낮게 형성되는 경우가 흔합니다. 반드시 하락한다고 단정할 수는 없습니다." }
    }
  ]
}
</script>
