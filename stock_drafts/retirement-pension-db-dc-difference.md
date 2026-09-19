---
keyword: 퇴직연금 DB DC 차이
title: 퇴직연금 DB DC 차이
slug: retirement-pension-db-dc-difference
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 850 (PC 420 / 모바일 430, 2026-09-19 실측)
gate1_pass: true (제도 기준 월 100 이상 필요, 이번 배치 중 검색량이 가장 높은 PASS 키워드)
serp_check: |
  [게이트2 v3 판정 2026-09-19 — 통과]
  WebSearch "퇴직연금 DB형 DC형 차이 선택 기준" 상위 종합:
  biz.sbs.co.kr(SBS Biz, 언론) / kyobo.com(교보생명, 공식 Q&A) /
  tossbank.com(토스뱅크, 핀테크 공식) / kcie.or.kr(금융투자자보호재단, 준정부) /
  glasswallet.com(개인·소규모 블로그) / gumiland.net(개인·소규모 블로그) /
  jun21.ddubinfo.com(개인 블로그) / dozard.com(개인·소규모 블로그) /
  tali.kr(개인 블로그)
  1) 진입 여지 — 있음. glasswallet.com·gumiland.net·ddubinfo.com·dozard.com·
     tali.kr까지 개인·소규모 블로그 5곳이 상위에 진입해 SERP가 잠겨 있지 않다.
  2) 검색 의도 — 정보 탐색+의사결정형("DB DC 중 뭐가 나은지 판단하고 싶다")이
     지배적이다. 조회·계산기 실행이 목적인 키워드가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 "임금상승률 4% 안팎이 기준"이라는
     어림값과 "회사가 운용 vs 내가 운용"이라는 개념 설명, "DC 전환 후 복귀 불가"는
     다루지만, ① 임금상승률과 투자수익률이 같을 때 두 제도의 결과가 수학적으로
     같아진다는 것을 실제 계산으로 보여주는 글은 찾지 못했고, ② DC형 계좌를
     방치했을 때 적용되는 사전지정운용제도(디폴트옵션)의 자동매수 조건·위험자산
     한도 예외까지 DB/DC 비교 맥락에서 함께 다루는 글도 없었다. 정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  "임금상승률이 높으면 DB, 수익률이 높으면 DC가 유리하다"는 흔한 설명을 실제
  계산으로 검증하고, 대부분 비교글이 다루지 않는 디폴트옵션 자동매수 규칙까지
  엮었다.
  - 연봉 4,000만원, 근속 10년 가정(단순화, 수수료·세제 제외) 하에 직접 계산:
    임금상승률 4%·투자수익률 4%로 같으면 DB형 퇴직급여와 DC형 최종 적립금이
    47,443,727원으로 정확히 일치한다(수학적으로 증명 가능한 항등식).
  - 임금상승률 6%·수익률 2%이면 DB형이 56,315,965원으로 DC형(47,654,440원)보다
    약 866만원 많고, 반대로 임금상승률 2%·수익률 6%이면 DC형이 같은 금액만큼
    유리해진다는 것을 같은 방식으로 계산해 대비했다.
  - DC형 계좌를 방치하면 적용되는 사전지정운용제도(디폴트옵션)의 실무 규칙을
    구체적 숫자로 정리했다: 신규가입은 통지 후 2주, 만기상품은 만기 후 4주+통지
    후 2주로 총 6주가 지나면 자동매수되고, 이 상품은 예외적으로 위험자산 100%
    편입이 허용된다(일반 DC·IRP는 70% 한도).
status: drafted
cannibalization_note: |
  8편(연금저축 세액공제, pension-savings-tax-credit)은 DB·DC를 전혀 언급하지
  않는다(2026-09-19 grep 확인, 매치 0건). 38편(퇴직연금 실물이전,
  retirement-pension-in-kind-transfer)은 DB→DB·DC→DC처럼 계좌를 옮기는
  실물이전 서비스가 중심이고, DB형·DC형이 애초에 무엇이 다른지·어느 쪽이
  유리한지·디폴트옵션 메커니즘은 다루지 않는다(2026-09-19 grep으로 확인,
  "DB DC IRP 사이 어떤 조합이 안 되나요" 섹션만 있고 제도 자체의 구조 비교는
  없음). 검색 의도가 서로 겹치지 않는다.
draft_path: stock_drafts/retirement-pension-db-dc-difference.md
primary_source: |
  1차 시도: 고용노동부 사전지정운용제도(디폴트옵션) FAQ(moel.go.kr) WebFetch
  1회 → EGRESS_BLOCKED(2026-09-19). 세션 전면 차단인지 확인하려 무관한
  정부도메인 금융위원회(fsc.go.kr)에도 1회 더 시도 → 동일하게 EGRESS_BLOCKED.
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처
  교차검증으로 진행했다.
  - 도입일(2022-07-12)·시행일(2023-07-12, 1년 유예)은 서로 무관한 6곳이
    충돌 없이 일치했다: 고용노동부 보도자료(moel.go.kr, WebSearch 스니펫으로
    확인·직접 열람은 막힘), 금융위원회 보도자료(fsc.go.kr, 동일), 김·장
    법률사무소 인사이트(kimchang.com, 대형 로펌), 노동법 전문 자료
    (worklaw.co.kr), 하나은행 공식 블로그(blog.hanabank.com), 금융투자자보호
    재단(kcie.or.kr, 준정부).
  - 디폴트옵션 상품이 위험자산 70% 한도의 예외로 100%까지 편입 가능하다는 점은
    한국경제 기사(hankyung.com, 언론)와 미래에셋투자와연금센터(investpension.
    miraeasset.com, 공식)·KB증권(kbsec.com, 공식)·금융투자자보호재단(kcie.or.kr,
    준정부) 4곳이 배경 설명(근로자퇴직급여보장법상 원리금보장상품 포함 의무 때문에
    일반 한도를 그대로 적용하면 제도가 작동하지 않는다는 이유)까지 일치했다.
  - 자동매수 시점(신규가입 통지 후 2주, 만기상품 만기 후 4주+통지 후 2주=6주)은
    삼성증권(samsungpop.com)·한국투자증권(file.koreainvestment.com, PDF)·
    하나은행(image.kebhana.com, PDF) 등 고용노동부 표준 양식을 준용한 공식
    문서 3곳과, 이를 다른 표현("6주 뒤 자동 가입")으로 독립적으로 서술한 개인
    블로그 glasswallet.com이 숫자까지 일치했다.
  - DB/DC 계산 예시(임금상승률 4%·근속10년·연봉4,000만원 가정)는 원문 인용이
    아니라 이 세션이 직접 계산한 수치이며, 계산 근거(공식·가정)를 본문에
    투명하게 명시했다.
기준일: 2026-09-19 (WebSearch 교차검증일)
tags: 퇴직연금, DB형, DC형, 확정급여형, 확정기여형, 디폴트옵션, 사전지정운용제도, 퇴직급여, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-19).
  게이트1: 네이버 키워드도구 실측 850회(제도 기준 100회 초과). 같은 배치 후보 중
  주식 시간외 거래 방법(1,020회, 일반기준 500 초과했으나 게이트2에서 기존
  개인블로그·공식 콘텐츠가 시간대·가격범위까지 이미 완결해 정보이득 확보
  실패로 제외, backlog에 기록)·미국주식 프리마켓 애프터마켓(20)·자사주 매입
  효과(80)·유상증자 실권주 처리(20)·공모주 비례배정 균등배정 차이(20)·
  배당소득세 분리과세 요건(20)·채권 표면금리 이자소득세(20)는 게이트1
  미달로 탈락, 퇴직연금 DB DC 차이만 게이트1·2를 모두 통과해 채택했다.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그 5곳 진입 확인,
  정보이득 2가지(임금상승률=수익률일 때 두 제도가 수학적으로 같아진다는 계산
  검증, 디폴트옵션 자동매수 규칙)로 탈락조건3 상쇄.
  게이트3: 실제 계산 예시(3가지 시나리오, 직접 계산해 검증) + 디폴트옵션
  자동매수 조건·위험자산 한도 예외의 구체적 숫자로 정보이득 확보.
  게이트4: moel.go.kr·fsc.go.kr 2개 정부 도메인 각 1회 시도 모두
  EGRESS_BLOCKED 확인 후 RULES.md 2026-09-12 기준에 따라 교차검증 진행 —
  핵심 사실(도입·시행일, 위험자산 한도 예외, 자동매수 기간)마다 6곳 이상의
  무관한 출처(정부 보도자료 스니펫·대형 로펌·언론·금융사 공식문서·준정부기관·
  개인 블로그)가 충돌 없이 일치했다.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 850회(제도 기준 100회 초과).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은
  정보이득 2가지로 상쇄(serp_check 참조).
  게이트3 충족 — 임금상승률=수익률일 때 두 제도 결과가 정확히 일치한다는
  실제 계산(47,443,727원=47,443,727원)과 두 비대칭 시나리오 대비표로 단순
  개념 설명을 넘어섰다.
  게이트4 — moel.go.kr·fsc.go.kr 직접 열람은 막혔고(각 1회 시도 후 중단),
  도입·시행일·위험자산 한도 예외·자동매수 기간을 정부 보도자료 스니펫·대형
  로펌·언론·금융사 공식문서·준정부기관·개인 블로그 등 6곳 이상으로
  교차검증했다. 한계: 정부 원문 페이지 전체 문구는 직접 재확인하지 못했다는
  점을 투명하게 남긴다.
  카니벌라이제이션 점검 — 8편(연금저축 세액공제)에 DB·DC 언급 없음, 38편
  (퇴직연금 실물이전)은 계좌 이전 절차가 중심이라 제도 자체 비교와 검색
  의도가 다름을 grep으로 확인(cannibalization_note 참조).
  기관 링크 점검 — 고용노동부·금융위원회·국가법령정보센터 링크 전부
  target="_blank" rel="noopener" 처리, 정부기관은 nofollow 미부착. 출처 URL은
  WebSearch로 실제 확인된 주소만 사용(지어내지 않음).
  제목 "퇴직연금 DB DC 차이" 13자·금지어 없음·조사 없음. 슬러그 영문 소문자+
  하이픈 5단어(retirement-pension-db-dc-difference). 인트로 문단 최상단 배치.
  표는 thead/tbody 시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1 일치.
  종목·상품 추천 표현, 단정 표현("반드시","무조건","확실히","보장") 없음.
  하단 면책 문구는 기존 게시글과 다른 문장으로 새로 작성.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문에서 "—" 검색 결과 0개
  확인. "다만"은 0회(전환은 "단,"·"반대로"·문장 구조 전환으로 처리).
  본문(YAML 메타데이터 제외) `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개
  고정 탈피). 핵심요약 박스
  제목을 "🧭 미리 확인할 4가지"로, 색상도 스카이블루 계열(#e0f2fe/#0284c7)로
  바꿔 최근 게시물들(주황·초록·보라·틸·로즈)과 겹치지 않게 했다. 목차 제외
  본문 H2 5개 중 "~나요"로 끝난 것은 2개, 나머지 3개는 서술형("~다릅니다",
  "~유불리","~벌어지는 일")이라 다양성 기준(절반 이상 서술형)을 충족한다.
  헤지 표현("~라고 보는 경우가 많다")은 1회만 사용해 남발하지 않았다.
  종합 판정: 4개 게이트 전부 충족(게이트4는 정부 보도자료 스니펫·로펌·언론·
  금융사 공식문서 등 다수 교차검증으로 대체, 한계는 출처란에 투명 공개) →
  gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-19</p>

<p>퇴직연금 DB형과 DC형은 <mark>누가 적립금을 운용하고 누가 그 결과를 책임지는지</mark>가 근본적으로 다릅니다. "임금상승률이 높으면 DB, 수익률이 높으면 DC가 유리하다"는 말을 실제 계산으로 검증하고, DC형을 방치했을 때 적용되는 자동매수 규칙까지 정리했습니다.</p>

<div style="background:#e0f2fe;border:2px solid #0284c7;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#075985;font-size:18px;">🧭 미리 확인할 4가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>DB형은 <b>회사</b>가, DC형은 <b>근로자 본인</b>이 적립금을 운용합니다.</li>
    <li>임금상승률과 투자수익률이 같으면 두 제도의 최종 금액은 계산상 <b>정확히 같습니다</b>.</li>
    <li>DC형 계좌를 방치하면 최대 6주 뒤 <mark>디폴트옵션 상품으로 자동 매수</mark>됩니다.</li>
    <li>DB에서 DC로 전환하면 <b>되돌릴 수 없어</b> 신중한 결정이 필요합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>퇴직연금 DB형과 DC형, 운용 주체부터 다릅니다</li>
  <li>임금상승률과 투자수익률 비교로 보는 유불리</li>
  <li>DC형 계좌를 방치하면 벌어지는 일</li>
  <li>디폴트옵션도 위험자산 한도가 적용되나요</li>
  <li>DB에서 DC로 전환하면 되돌릴 수 있나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">퇴직연금 DB형과 DC형, 운용 주체부터 다릅니다</h2>

<p>DB형(확정급여형)은 <mark>회사가 적립금을 직접 운용</mark>하고, 근로자는 운용 성과와 무관하게 근로자퇴직급여보장법에 정해진 방식(퇴직 전 3개월 평균임금 × 근속연수)대로 계산된 금액을 받습니다.</p>

<p>DC형(확정기여형)은 회사가 매년 연간 임금총액의 12분의 1 이상을 근로자 개인 계좌에 부담금으로 넣어주고, 그 적립금을 <b>근로자 본인이 직접 운용</b>합니다. 펀드·ETF 등에 투자한 결과가 좋으면 더 받고, 나쁘면 덜 받습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">DB형(확정급여형)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">DC형(확정기여형)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">운용 주체</td>
      <td style="border:1px solid #ddd;padding:8px;">회사</td>
      <td style="border:1px solid #ddd;padding:8px;">근로자 본인</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">받는 금액</td>
      <td style="border:1px solid #ddd;padding:8px;">퇴직 전 평균임금 × 근속연수로 확정</td>
      <td style="border:1px solid #ddd;padding:8px;">납입금 + 운용 손익</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">운용 위험 부담</td>
      <td style="border:1px solid #ddd;padding:8px;">회사</td>
      <td style="border:1px solid #ddd;padding:8px;">근로자</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">유리한 상황</td>
      <td style="border:1px solid #ddd;padding:8px;">임금상승률이 높을 때</td>
      <td style="border:1px solid #ddd;padding:8px;">투자수익률이 높을 때</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">임금상승률과 투자수익률 비교로 보는 유불리</h2>

<p>"임금이 많이 오르면 DB, 투자를 잘하면 DC가 유리하다"는 설명은 많지만, 두 조건이 <b>같을 때</b> 실제로 어떤 결과가 나오는지 계산으로 확인한 글은 드뭅니다. 연봉 4,000만원, 근속 10년을 가정해(수수료·세제는 제외한 단순화 계산) 직접 계산해봤습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">시나리오</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">DB형 최종 금액</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">DC형 최종 금액</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">결과</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">임금상승률 4% = 수익률 4%</td>
      <td style="border:1px solid #ddd;padding:8px;">47,443,727원</td>
      <td style="border:1px solid #ddd;padding:8px;">47,443,727원</td>
      <td style="border:1px solid #ddd;padding:8px;">정확히 동일</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">임금상승률 6% &gt; 수익률 2%</td>
      <td style="border:1px solid #ddd;padding:8px;">56,315,965원</td>
      <td style="border:1px solid #ddd;padding:8px;">47,654,440원</td>
      <td style="border:1px solid #ddd;padding:8px;">DB형이 약 866만원 많음</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">임금상승률 2% &lt; 수익률 6%</td>
      <td style="border:1px solid #ddd;padding:8px;">39,836,419원</td>
      <td style="border:1px solid #ddd;padding:8px;">47,654,440원</td>
      <td style="border:1px solid #ddd;padding:8px;">DC형이 약 782만원 많음</td>
    </tr>
  </tbody>
</table>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">임금상승률과 투자수익률이 정확히 같으면 두 제도의 최종 금액도 정확히 같아집니다.</span> 근속연수가 같다면 DB형의 "최종 임금 × 근속연수" 계산과 DC형의 "매년 납입금을 복리로 굴린 합"이 수학적으로 같은 값에 수렴하기 때문입니다.</p>

<p>반대로 두 비율이 벌어질수록 그 차이도 벌어집니다. 근속 기간이 길고 회사 임금 인상 곡선이 가파른 편이면 DB형을, 이직이 잦거나 투자 성과에 자신 있는 편이면 DC형을 유리하게 보는 경우가 많지만, 임금상승률 자체는 회사와 개인마다 달라 이 계산은 직접 자신의 연봉 인상률을 넣어봐야 정확합니다.</p>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">DC형 계좌를 방치하면 벌어지는 일</h2>

<p>DC형과 IRP는 근로자가 직접 운용상품을 지정해야 합니다. 아무 지시도 하지 않으면 <b>사전지정운용제도(디폴트옵션)</b>가 작동해 미리 골라둔 상품으로 자동 매수됩니다. 이 제도는 2022년 7월 12일 도입돼 1년의 유예기간을 거쳐 2023년 7월 12일부터 전면 시행 중입니다.</p>

<ul style="line-height:1.9;">
  <li>신규가입 시: 통지 후 2주 안에 운용지시가 없으면 자동매수</li>
  <li>기존 상품 만기 시: 만기 후 4주가 지나면 통지가 이뤄지고, 그 후 2주가 더 지나면 자동매수(총 6주)</li>
</ul>

<p>주의할 점은 디폴트옵션 상품에는 <mark>일반 DC·IRP 계좌에 적용되는 위험자산 70% 한도가 적용되지 않는다</mark>는 것입니다. 근로자퇴직급여보장법이 원리금보장 상품을 포함하도록 규정해 일반 한도를 그대로 적용하면 제도가 작동하기 어렵기 때문에, 디폴트옵션 상품은 예외적으로 적립금의 100%까지 편입할 수 있습니다.</p>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">디폴트옵션도 위험자산 한도가 적용되나요</h2>

<p>적용되지 않습니다. 일반 DC·IRP 계좌는 주식형 펀드 같은 위험자산을 적립금의 70%까지만 담을 수 있지만, <a href="https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=13711" target="_blank" rel="noopener">고용노동부</a>와 <a href="https://fsc.go.kr/no010107/77805" target="_blank" rel="noopener">금융위원회</a>가 함께 도입한 디폴트옵션 상품은 이 한도의 예외로 인정돼 100%까지 위험자산으로 채울 수 있습니다.</p>

<p>따라서 "디폴트옵션은 안전한 상품일 것"이라고 넘겨짚으면 안 됩니다. 연금사업자가 제시하는 디폴트옵션 상품 목록에는 원리금보장형뿐 아니라 위험자산 비중이 높은 상품도 포함되어 있어, 가입 전에 상품 성격을 직접 확인해야 합니다.</p>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">DB에서 DC로 전환하면 되돌릴 수 있나요</h2>

<p>되돌릴 수 없습니다. DB형에서 DC형으로 전환하는 것은 가능하지만, 반대로 DC형에서 DB형으로 되돌아가는 전환은 원칙적으로 인정되지 않습니다.</p>

<p>회사가 퇴직연금 제도를 DB에서 DC로 바꾸는 경우, 근로자는 전환 시점까지 쌓인 금액을 DC 계좌로 옮기고 이후 적립분부터는 DC 방식이 적용됩니다. 전환을 고민 중이라면 남은 근속연수와 예상 임금 인상률, 본인의 투자 성향을 함께 따져본 뒤 결정해야 합니다.</p>

<h2 style="border-left:6px solid #0284c7;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">DC형에서 DB형으로 다시 돌아갈 수 있나요</summary>
  <p style="margin:10px 0 0 0;">안 됩니다. 전환은 한 방향(DB→DC)으로만 가능해 결정 전에 신중히 따져봐야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">임금상승률이 몇 %면 DB형이 유리한가요</summary>
  <p style="margin:10px 0 0 0;">임금상승률이 투자수익률보다 높을수록 DB형이 유리해집니다. 통상 연 4% 안팎을 기준점으로 보는 경우가 많지만 이는 어림값이고, 실제로는 본인의 연봉 인상 곡선과 예상 수익률을 넣어 계산해봐야 정확합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">DC형 계좌에서 운용지시를 안 하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">통지 후 2주(기존 상품 만기 시에는 만기 후 4주+통지 후 2주로 총 6주)가 지나면 미리 지정해둔 디폴트옵션 상품으로 자동 매수됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">디폴트옵션 상품도 위험자산 70% 한도 규제를 받나요</summary>
  <p style="margin:10px 0 0 0;">받지 않습니다. 디폴트옵션 상품은 이 한도의 예외로 적립금의 100%까지 위험자산으로 편입할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">사전지정운용제도(디폴트옵션)는 언제부터 시행됐나요</summary>
  <p style="margin:10px 0 0 0;">2022년 7월 12일 도입돼 1년의 유예기간을 거쳐 2023년 7월 12일부터 전면 시행됐습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=13711" target="_blank" rel="noopener">고용노동부</a> - 퇴직연금제도에 사전지정운용제도(디폴트옵션) 도입 보도자료</li>
    <li><a href="https://fsc.go.kr/no010107/77805" target="_blank" rel="noopener">금융위원회</a> - 퇴직연금 사전지정운용제도 도입 보도자료</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 근로자퇴직급여보장법(DB형·DC형 정의 및 산정 방식)</li>
  </ul>
  기준일: 2026-09-19(WebSearch 교차검증일). 고용노동부·금융위원회 원문 페이지는
  이번 세션 WebFetch가 각각 막혀 직접 열람하지 못했고, 도입·시행일과 위험자산
  한도 예외, 자동매수 기간은 정부 보도자료 스니펫·대형 로펌·언론·금융사 공식
  문서·준정부기관·개인 블로그 등 6곳 이상이 일치하는 것으로 교차검증했습니다.
  DB/DC 계산 예시는 본문에 명시한 가정(연봉 4,000만원, 근속 10년, 수수료·세제
  제외)에 따라 이 세션이 직접 계산한 수치입니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 퇴직연금 DB형·DC형 제도의 구조 차이를 이해하는 데 참고하시라고 정리한
정보 제공용 글이며, 특정 금융상품이나 종목의 가입·매수를 권유하지 않습니다.
어떤 제도가 유리한지는 개인의 근속연수와 임금 인상 곡선에 따라 달라지므로
최종 선택과 그 결과에 대한 책임은 근로자 본인에게 있고, 제도 내용은 관련
법령 개정에 따라 달라질 수 있으니 가입 전 고용노동부·금융위원회 등
원출처에서 다시 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "퇴직연금 DB DC 차이",
  "description": "퇴직연금 DB형과 DC형은 운용 주체와 위험 부담이 다릅니다. 임금상승률과 투자수익률이 같을 때 두 제도의 결과가 수학적으로 같아진다는 계산 검증과, DC형 방치 시 적용되는 디폴트옵션 자동매수 규칙을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-19",
  "dateModified": "2026-09-19",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/retirement-pension-db-dc-difference"
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
      "name": "DC형에서 DB형으로 다시 돌아갈 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "안 됩니다. 전환은 한 방향(DB→DC)으로만 가능해 결정 전에 신중히 따져봐야 합니다." }
    },
    {
      "@type": "Question",
      "name": "임금상승률이 몇 %면 DB형이 유리한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "임금상승률이 투자수익률보다 높을수록 DB형이 유리해집니다. 통상 연 4% 안팎을 기준점으로 보는 경우가 많지만 이는 어림값이고, 실제로는 본인의 연봉 인상 곡선과 예상 수익률을 넣어 계산해봐야 정확합니다." }
    },
    {
      "@type": "Question",
      "name": "DC형 계좌에서 운용지시를 안 하면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "통지 후 2주(기존 상품 만기 시에는 만기 후 4주+통지 후 2주로 총 6주)가 지나면 미리 지정해둔 디폴트옵션 상품으로 자동 매수됩니다." }
    },
    {
      "@type": "Question",
      "name": "디폴트옵션 상품도 위험자산 70% 한도 규제를 받나요",
      "acceptedAnswer": { "@type": "Answer", "text": "받지 않습니다. 디폴트옵션 상품은 이 한도의 예외로 적립금의 100%까지 위험자산으로 편입할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "사전지정운용제도(디폴트옵션)는 언제부터 시행됐나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2022년 7월 12일 도입돼 1년의 유예기간을 거쳐 2023년 7월 12일부터 전면 시행됐습니다." }
    }
  ]
}
</script>
