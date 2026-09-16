---
keyword: 해외금융계좌 신고
title: 해외금융계좌 신고 기준과 과태료
slug: foreign-financial-account-reporting
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 290 (PC 160 / 모바일 130, 2026-09-16 실측, check-keywords.yml)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요 — "신고" 키워드 포함으로 세부·제도 분류 적용)
serp_check: |
  [게이트2 v3 판정 2026-09-16 — 통과]
  WebSearch "해외금융계좌 신고 2026 기준금액 과태료" + "해외금융계좌 신고 5억원 초과
  과태료 10% 명단공개 형사처벌" + "해외금융계좌 신고 과태료율 20% 15% 10% 구간" 상위 종합:
  coinone.co.kr(가상자산거래소 공지) / law.go.kr(정부 법령 ×2) / asiae.co.kr·
  m.sateconomy.co.kr·biz.heraldcorp.com·sejungilbo.com·intn.co.kr(언론 5곳) /
  nts.go.kr(국세청 공식) / watax.kr·nexttala.com(세무법인 콘텐츠) / crypto.com(거래소 공지) /
  premiatnc.blog(세무·회계 컨설팅 콘텐츠마케팅 블로그) / kmoney101.com(개인 재테크 블로그) /
  webzine.kacta.or.kr(한국세무사회 세무사신문, 준정부 성격 전문지) /
  daeryunlaw-finance.com(대륜, 법무법인)
  1) 진입 여지 — 있음. kmoney101.com(개인 블로그)·premiatnc.blog(소규모 컨설팅 콘텐츠)가
     상위권에 진입해 SERP가 완전히 잠겨 있지 않음.
  2) 검색 의도 — 정보 탐색("얼마 넘으면 신고해야 하나, 과태료가 얼마인가"). 계좌 조회나
     신청 도구를 원하는 의도가 아님.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 "5억원 초과 시 6월 신고, 미신고 10% 과태료"
     까지는 다루지만, (a) 2025-01-01 국제조세조정법 시행령 개정으로 과태료율이 10~20%
     누진에서 10% 단일로 바뀌고 한도가 20억→10억으로 낮아진 최신 구조, (b) 반복위반 시
     가중(2차 30%/3차 이상 50%)·부분 감경(50%) 기준까지 한 표로 정리한 글, (c) 여러
     해외계좌(예금+증권+가상자산)를 합산해서 5억원 초과 여부를 판단하는 구체적 예시를
     갖춘 글은 찾지 못했다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (1) 2025-01-01 국제조세조정에 관한 법률 시행령 개정 전/후 비교표 — 과태료율(구
      10~20% 누진 → 신 10% 단일), 과태료 한도(20억원 → 10억원), 미소명·거짓소명
      과태료율(20% → 10%)까지 개정 전/후를 나란히 정리.
  (2) 가중·감경 구조표 — 2차 위반 30%, 3차 이상 위반 50% 가중, 해외재산 불법 반출·은닉
      확인 시 30~50% 가중, 반대로 계좌정보 일부가 이미 확인되는 단순 미신고는 50% 감경.
  (3) 합산 판단 예시 — "해외증권사 계좌 3억원 + 해외은행 예금 2억5천만원을 같은 해
      어느 한 달 말일에 동시 보유"처럼, 서로 다른 기관·종류의 계좌라도 합산해서 5억원
      초과 여부를 따진다는 점을 가상의 라운드 숫자로 보여준다(실제 개인 사례 수치가
      아니라 제도 이해를 위한 예시임을 명시).
  기존 항목 중 6편(금융소득 종합과세)·5편(해외주식 양도소득세 신고 방법)·39편(해외주식
  배당소득세)은 "세금을 얼마 내는가"를 다루지만, 이 글은 "신고 의무 자체(세금이 아니라
  계좌 정보 신고)"를 다뤄 검색 의도와 정보이득 모두 겹치지 않는다.
primary_source: |
  1차 시도: 국세청(nts.go.kr) 해외금융계좌 신고 안내 페이지
  (cntntsView.do?cntntsId=7819&mi=2513) WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-16).
  대조군으로 언론 기사 도메인(view.asiae.co.kr) 1회 추가 시도했으나 동일하게
  EGRESS_BLOCKED로 확인돼, 특정 도메인이 아니라 이번 세션의 전면 차단으로 판단했다
  (RULES.md 누적 기록 패턴과 일치, 그 이상 재시도하지 않음).
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로
  진행했다 — 서로 무관한 독립 출처가 3곳을 크게 넘는 9곳 이상 확인됐고, 그중
  언론 5곳(아시아경제·사이버경제·헤럴드경제·세종일보·일간NTN) + 준정부 성격 전문지
  1곳(한국세무사회 세무사신문) + 법무법인 1곳(대륜)이 포함된다. 핵심 수치(기준금액
  5억원, 신고기한 6월, 과태료 10% 단일율, 2025-01-01 개정, 가중·감경 비율, 명단공개·
  형사처벌 기준 50억원)가 이 9곳 이상에서 충돌 없이 일치했다. 세율·구간처럼 이 프로젝트가
  과거 오류를 잡아낸 유형의 숫자이지만, 단일 보도자료를 베낀 것이 아니라 서로 다른
  매체·법무법인이 독립적으로 같은 시행령 개정 내용을 보도한 것이어서(예: 일간NTN 두 편이
  시차를 두고 같은 개정 후 수치를 재확인) 신뢰도가 높다고 판단해 진행했다.
기준일: 2026-09-16 (WebSearch 확인일. 과태료 관련 시행령 개정 시행일은 2025-01-01)
tags: 해외금융계좌신고, 해외금융계좌과태료, 해외자산신고, 해외주식신고, 국제조세조정법, 미신고과태료, 해외가상자산신고, 홈택스신고, 세금신고기한, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-16).
  게이트1: 네이버 키워드도구 실측 290회(check-keywords.yml, 2026-09-16 — 세부·제도 기준
  100회 이상). 같은 배치에서 ISA 만기 연금계좌 이체(20회)·RP통장 이자소득세(20회)·
  배당세액공제 계산방법(20회)·미수동결계좌 해제방법(20회, 기준500)·해외주식 상속세
  신고(20회)·증권거래세 면제 대상(20회, 기준500)은 게이트1 미달로 탈락.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그 진입 여지 있고, 2025년
  시행령 개정 반영 여부·합산 판단 예시가 상위 결과에 부재해 정보이득 여지 있음.
  게이트3: 개정 전/후 비교표 + 가중·감경 구조표 + 여러 계좌 합산 판단 예시로 정보이득
  확보.
  게이트4: nts.go.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군(view.asiae.co.kr)도 차단돼
  세션 전면 차단 확인 후, RULES.md 2026-09-12 기준에 따라 독립 출처 9곳 이상(언론 5곳+
  준정부 전문지 1곳+법무법인 1곳 포함) 교차검증, 핵심 수치 충돌 없음 확인 후 진행. 이
  방식은 16·17·18편, 39편(해외주식 배당소득세)에서 같은 기준으로 gate_pass:true 처리한
  선례와 일치한다.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 290회(세부·제도 기준 100회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 2025-01-01 시행령 개정 전/후 비교표, 가중(2차 30%/3차 이상 50%)·감경
  (50%) 구조표, 여러 해외계좌 합산 판단 예시로 상위 결과가 다루지 않는 각도를 확보했다.
  게이트4 — nts.go.kr 직접 열람은 막혔고(대조군 asiae.co.kr도 차단, 세션 전면 차단),
  독립 출처 9곳 이상(언론 5곳, 준정부 성격 전문지 1곳, 법무법인 1곳 포함)이 핵심 수치에서
  충돌 없이 일치함을 확인해 교차검증으로 진행했다. 합산 판단 예시의 구체 금액(3억원+
  2억5천만원)은 실제 사례가 아니라 제도 이해를 위한 가상 예시임을 본문에 명시했다.
  카니벌라이제이션 점검 — 6편(금융소득 종합과세)·5편(해외주식 양도소득세 신고 방법)·
  39편(해외주식 배당소득세)은 전부 "세금을 얼마 내는가"를 다루고, 이 글은 "계좌 정보
  신고 의무"라는 별개 제도를 다뤄 검색 의도가 겹치지 않는다. 본문에서 관련 글로
  내부 링크.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 국세청·홈택스·국가법령정보센터 안내
  문장과 하단 참고 출처 목록 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관
  링크에 nofollow 미부착. 출처 URL은 RULES.md 기관 링크 표와 WebSearch로 실제 확인된
  주소만 사용(지어내지 않음).
  제목 "해외금융계좌 신고 기준과 과태료" 17자(공백 포함)·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 4단어(foreign-financial-account-reporting). 인트로 문단
  최상단 배치. 표는 thead/tbody 시맨틱 사용. 기준일 명시. FAQ 6개와 JSON-LD 1:1 일치.
  종목·상품 추천 표현, 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 9곳 이상 독립 출처 교차검증으로 대체, 한계
  투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-16</p>

<p><mark>해외 예금·증권·가상자산 계좌 잔액을 합쳐 어느 한 달 말일에라도 5억원을 넘긴 적이 있다면, 다음 해 6월에 해외금융계좌 신고를 해야 합니다.</mark> 신고를 놓치면 세금이 아니라 계좌 정보를 안 알렸다는 이유만으로 과태료가 부과됩니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>해외 계좌 잔액 합계가 <b>해당 연도 매월 말일 중 단 하루라도 5억원을 초과</b>하면 신고 대상입니다.</li>
    <li>신고 기간은 다음 해 <b>6월 1일~6월 30일</b>, 관할 세무서 또는 홈택스입니다.</li>
    <li>2025년 1월 1일 개정으로 과태료율이 <mark>10~20% 누진에서 10% 단일</mark>로 바뀌었습니다(한도도 20억→10억원으로 완화).</li>
    <li>미·과소신고 금액이 <b>50억원을 초과</b>하면 명단공개와 형사처벌(2년 이하 징역 또는 13~20% 벌금) 대상이 될 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>해외금융계좌 신고, 누가 얼마나 보유하면 해야 하나요</li>
  <li>여러 계좌를 갖고 있으면 어떻게 합산하나요</li>
  <li>신고는 언제 어떻게 하나요</li>
  <li>신고를 안 하면 과태료가 얼마나 나오나요</li>
  <li>과태료가 늘거나 줄어드는 경우도 있나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외금융계좌 신고, 누가 얼마나 보유하면 해야 하나요</h2>

<p>국내 거주자나 내국법인이 보유한 <b>해외금융계좌(해외가상자산계좌 포함)</b> 잔액의 합계액이, 해당 연도의 매월 말일 중 <mark>어느 하루라도 5억원을 초과</mark>하면 다음 해에 신고해야 합니다. 매년 말 잔액이 아니라 <b>매월 말일마다 확인</b>한다는 점이 자주 놓치는 부분입니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">해외증권사 위탁계좌로 해외주식·해외ETF를 사고 있다면 이 신고 대상에 포함될 수 있다</span>는 점을 신경 써야 합니다. 해외주식 자체에 붙는 세금은 <a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing" target="_blank" rel="noopener">이전 글(해외주식 양도소득세 신고 방법)</a>에서 다뤘지만, 이 글의 신고는 세금이 아니라 <b>계좌 정보 자체를 알리는 별개의 의무</b>입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">여러 계좌를 갖고 있으면 어떻게 합산하나요</h2>

<p>기관이 다르거나 계좌 종류(예금·증권·가상자산 등)가 달라도, 본인 명의의 해외금융계좌는 <b>전부 합산</b>해서 5억원 초과 여부를 판단합니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>합산 판단 예시 (제도 이해용 가상 사례)</b>
  <p style="margin:8px 0 0 0;">해외증권사 위탁계좌 3억원 + 해외은행 예금 2억 5,000만원을 같은 해 어느 한 달 말일에 동시에 보유했다면, 합계 5억 5,000만원으로 <b>기준금액(5억원)을 넘겨 신고 대상</b>이 됩니다. 두 계좌가 서로 다른 나라, 다른 기관에 있어도 본인 명의라면 합산합니다. (실제 개인 사례 수치가 아니라 합산 방식을 보여주기 위한 예시입니다.)</p>
</div>

<ul style="line-height:1.9;">
  <li>합산 대상 — 해외예금, 해외증권(해외주식 포함), 해외적립식보험, 해외파생상품, 해외집합투자증권, 해외가상자산계좌 등</li>
  <li>기준 시점 — 해당 연도의 <b>매월 말일</b> (연말 잔액만 보는 것이 아님)</li>
  <li>기준 방향 — <b>단 하루라도</b> 초과하면 그 연도분은 신고 대상</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고는 언제 어떻게 하나요</h2>

<p>신고 대상이 된 해의 <b>다음 해 6월 1일부터 6월 30일까지</b> 관할 세무서에 신고서를 제출하거나, <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>에서 전자신고할 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">항목</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기준금액</td>
      <td style="border:1px solid #ddd;padding:8px;">매월 말일 중 하루라도 합계 5억원 초과</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">신고기간</td>
      <td style="border:1px solid #ddd;padding:8px;">다음 해 6월 1일 ~ 6월 30일</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">신고처</td>
      <td style="border:1px solid #ddd;padding:8px;">관할 세무서 또는 홈택스 전자신고</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고를 안 하면 과태료가 얼마나 나오나요</h2>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">2025년 1월 1일 국제조세조정에 관한 법률 시행령 개정으로 과태료율이 달라졌습니다.</span> 개정 전에는 미신고·과소신고 금액에 따라 10~20% 누진율이 적용됐지만, 개정 후에는 <mark>10% 단일율</mark>로 바뀌었고 과태료 한도도 낮아졌습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">개정 전</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">개정 후(2025-01-01~)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">미신고·과소신고 과태료율</td>
      <td style="border:1px solid #ddd;padding:8px;">10~20% 누진</td>
      <td style="border:1px solid #ddd;padding:8px;">10% 단일</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">과태료 한도</td>
      <td style="border:1px solid #ddd;padding:8px;">20억원</td>
      <td style="border:1px solid #ddd;padding:8px;">10억원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">미소명·거짓소명 과태료율</td>
      <td style="border:1px solid #ddd;padding:8px;">20%</td>
      <td style="border:1px solid #ddd;padding:8px;">10%</td>
    </tr>
  </tbody>
</table>

<p>미·과소신고 금액이 <b>50억원을 초과</b>하면 과태료 외에도 위반자의 성명·나이·직업·주소·위반금액 등이 <b>명단공개</b>되고, <b>2년 이하 징역 또는 미·과소신고 금액의 13% 이상 20% 이하 벌금</b>의 형사처벌 대상이 될 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">과태료가 늘거나 줄어드는 경우도 있나요</h2>

<p>같은 사람이 반복해서 위반하거나 재산을 숨기려 한 정황이 있으면 과태료가 <b>가중</b>되고, 반대로 이미 계좌 정보 일부가 확인된 단순 미신고라면 <b>감경</b>됩니다.</p>

<ul style="line-height:1.9;">
  <li>2차 위반 — 30% 가중</li>
  <li>3차 이상 위반 — 50% 가중</li>
  <li>해외재산 불법 반출·은닉 등이 확인되는 경우 — 30~50% 가중</li>
  <li>단순 미신고이면서 관련 신고·이전 연도 신고 등으로 계좌정보 일부가 이미 확인되는 경우 — 50% 감경</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>구체적인 과태료 금액은 사안마다 다릅니다</b>
  <p style="margin:8px 0 0 0;">가중·감경 사유가 겹치는 경우의 최종 과태료율은 개별 사실관계에 따라 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 안내나 세무 전문가 상담으로 정확히 확인하는 것이 안전합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외금융계좌 신고 기준금액은 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">해당 연도 매월 말일 중 어느 하루라도 해외금융계좌 잔액 합계액이 5억원을 초과하면 신고 대상입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 계좌도 신고 대상인가요</summary>
  <p style="margin:10px 0 0 0;">네, 해외증권사 위탁계좌로 보유한 해외주식도 해외금융계좌에 포함됩니다. 다른 해외예금·가상자산계좌 등과 합산해서 5억원 초과 여부를 판단합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">신고 기한은 언제인가요</summary>
  <p style="margin:10px 0 0 0;">신고 대상이 된 해의 다음 해 6월 1일부터 6월 30일까지 관할 세무서에 신고하거나 홈택스에서 전자신고할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">미신고하면 과태료가 얼마나 나오나요</summary>
  <p style="margin:10px 0 0 0;">2025년 1월 1일 개정 이후로는 미신고·과소신고 금액의 10%가 과태료로 부과됩니다(한도 10억원). 개정 전에는 10~20% 누진율이었습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">과태료가 더 늘어나는 경우도 있나요</summary>
  <p style="margin:10px 0 0 0;">네. 2차 위반은 30%, 3차 이상 위반이나 해외재산 불법 반출·은닉이 확인되면 30~50%까지 가중됩니다. 반대로 계좌정보 일부가 이미 확인된 단순 미신고는 50% 감경됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">형사처벌까지 받을 수도 있나요</summary>
  <p style="margin:10px 0 0 0;">미·과소신고 금액이 50억원을 초과하면 명단공개와 함께 2년 이하 징역 또는 미·과소신고 금액의 13~20% 벌금 처벌 대상이 될 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> - 해외금융계좌 신고 안내</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> - 해외금융계좌 신고 전자신고</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 국제조세조정에 관한 법률 시행령(과태료 규정)</li>
  </ul>
  기준일: 2026-09-16(WebSearch 확인일). 과태료율 개정(10~20% 누진 → 10% 단일)은
  2025-01-01 시행령 개정 기준입니다. 국세청 원문 페이지는 이번 세션 WebFetch가 차단돼
  직접 열람하지 못했고, 언론 5곳·준정부 성격 전문지 1곳·법무법인 1곳을 포함한 9곳 이상의
  독립 출처가 동일 수치로 일치함을 확인해 교차검증으로 대체했습니다.
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
  "headline": "해외금융계좌 신고 기준과 과태료",
  "description": "해외금융계좌 신고 기준금액(5억원)과 여러 계좌 합산 방법, 신고 기한, 2025년 개정된 과태료율(10% 단일)과 가중·감경 구조, 명단공개·형사처벌 기준을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-16",
  "dateModified": "2026-09-16",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/foreign-financial-account-reporting"
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
      "name": "해외금융계좌 신고 기준금액은 얼마인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "해당 연도 매월 말일 중 어느 하루라도 해외금융계좌 잔액 합계액이 5억원을 초과하면 신고 대상입니다." }
    },
    {
      "@type": "Question",
      "name": "해외주식 계좌도 신고 대상인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "네, 해외증권사 위탁계좌로 보유한 해외주식도 해외금융계좌에 포함됩니다. 다른 해외예금·가상자산계좌 등과 합산해서 5억원 초과 여부를 판단합니다." }
    },
    {
      "@type": "Question",
      "name": "신고 기한은 언제인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "신고 대상이 된 해의 다음 해 6월 1일부터 6월 30일까지 관할 세무서에 신고하거나 홈택스에서 전자신고할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "미신고하면 과태료가 얼마나 나오나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2025년 1월 1일 개정 이후로는 미신고·과소신고 금액의 10%가 과태료로 부과됩니다(한도 10억원). 개정 전에는 10~20% 누진율이었습니다." }
    },
    {
      "@type": "Question",
      "name": "과태료가 더 늘어나는 경우도 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 2차 위반은 30%, 3차 이상 위반이나 해외재산 불법 반출·은닉이 확인되면 30~50%까지 가중됩니다. 반대로 계좌정보 일부가 이미 확인된 단순 미신고는 50% 감경됩니다." }
    },
    {
      "@type": "Question",
      "name": "형사처벌까지 받을 수도 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "미·과소신고 금액이 50억원을 초과하면 명단공개와 함께 2년 이하 징역 또는 미·과소신고 금액의 13~20% 벌금 처벌 대상이 될 수 있습니다." }
    }
  ]
}
</script>
