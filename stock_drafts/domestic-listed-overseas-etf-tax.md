---
keyword: 국내상장 해외ETF 세금
title: 국내상장 해외ETF 세금 얼마나 내나
slug: domestic-listed-overseas-etf-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1230 (PC 300 / 모바일 930)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-13 — 통과]
  WebSearch "국내상장 해외ETF 세금 배당소득세 종합과세" + "국내상장 해외ETF 세금 계산 예시" +
  "국내주식형 ETF 매매차익 비과세 해외ETF 배당소득세 차이" 상위 종합:
  pwc.com(회계법인 인사이트) / kbcapital.co.kr(KB 공식) / sisajournal-e.com(언론) /
  v.daum.net(언론 칼럼) / kbthink.com(KB 공식) / shinhansec.com(신한투자증권 공식) /
  kcie.or.kr(금융투자자보호재단, 준정부 성격) / kbam.co.kr(KB자산운용 공식) /
  miraeasset.com(미래에셋증권 블로그) / samsungfund.com(삼성자산운용 공식) /
  kiwoomam.com(키움자산운용 공식) / trendmetriclab.com(개인·소규모 콘텐츠) /
  1qetf.com(개인·소규모 ETF 서비스형 사이트) / calcmoney.kr(개인·소규모 블로그) /
  wikidocs.net/@Insight_Lab(개인 블로그) / kacpta.or.kr(세무학회 논문, 학술기관)
  1) 진입 여지 — 있음. trendmetriclab.com·1qetf.com·calcmoney.kr·wikidocs.net 개인/소규모
     블로그가 상위권에 다수 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색+계산("세금이 얼마냐, 왜 다르냐"). 계산기·조회 실행이 지배적 의도가 아님.
  3) 답 완결 여부 — 부분적. 대부분 글이 "매매차익·분배금 15.4%, 해외상장 ETF는 22%" 기본 구도는
     다루지만, (a) 국내주식형 ETF도 레버리지·인버스·TR·액티브면 과세 대상이 된다는 예외,
     (b) 보유기간과세의 실제 계산 방식(과표기준가 증가분과 실제 차익 중 더 작은 금액에만 과세),
     (c) 손익통산 불가를 실제 원 단위 손익 예시로 보여주는 글, (d) 2025-01-01 시행된 외국납부세액
     공제 방식 개편(선환급 폐지)까지 한 번에 엮은 글은 찾지 못함. 정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  상위 글 대부분이 다루는 "매매차익·분배금 15.4% vs 해외상장 ETF 22%" 기본 구도를 넘어서
  (1) 국내주식형 ETF라도 레버리지·인버스·TR·액티브 유형이면 매매차익 비과세 대상에서 빠진다는
  예외를 명확히 밝히고, (2) 보유기간과세 계산식(매수·매도 시점 과표기준가 증가분과 실제 매매차익
  중 더 작은 금액에 15.4% 과세)을 가상의 숫자로 계산 예시를 보여주며, (3) 손익통산이 안 된다는
  점을 "한 종목 100만원 이익 + 다른 종목 50만원 손실을 같은 해에 realize해도 손실은 반영되지
  않고 100만원 전액에 과세된다"는 원 단위 예시와 해외 직접 상장 ETF(손익통산 가능)와의 대비로
  보여준다. (4) 2025-01-01부터 시행된 외국납부세액 공제 "선환급 폐지"(사전에 세금을 돌려받아
  세전 배당금에 얹어주던 방식이 없어지고, 원천징수 시점에 투자자별로 바로 정산)까지 반영해
  최신성을 확보한다.
primary_source: |
  국세청(nts.go.kr) 및 관련 소득세법 시행령 원문에 WebFetch를 1회 시도했으나 EGRESS_BLOCKED로
  확인(2026-09-13). 대조군으로 www.google.com도 동일하게 차단되어 이번 세션 전면 차단으로
  판단(RULES.md에 누적 기록된 기존 패턴과 일치).
  RULES.md 「1차 출처가 막혔을 때: 2차 출처 교차검증 vs 사람 캡처 요청」(2026-09-12) 기준 적용 —
  핵심 사실관계가 서로 무관한 다수 독립 출처에서 충돌 없이 일치했다:
  - 세율(매매차익·분배금 배당소득세 15.4%, 해외 직접상장 ETF 양도소득세 22%, 250만원 기본공제,
    금융소득종합과세 2천만원 기준)은 이미 이 시리즈 4편(배당소득세)·5편(해외주식 양도소득세)·
    6편(금융소득종합과세)에서 국세청·법제처 원문으로 확정된 값을 그대로 재사용 — 신규 확인이
    필요한 숫자가 아니다.
  - 보유기간과세 계산 방식과 손익통산 불가 여부는 KB캐피탈·KB증권(kbcapital.co.kr, kbthink.com),
    신한투자증권(shinhansec.com), 키움투자자산운용(kiwoomam.com), 토스(toss.im/tossfeed),
    시사저널e(언론, sisajournal-e.com), 국제신문 재테크 칼럼(언론, kookje.co.kr), 세무학회 논문
    (준학술기관, kacpta.or.kr) 등 7곳 이상 독립 출처가 동일하게 설명해 충돌 없음.
  - 국내주식형 ETF 매매차익 비과세와 레버리지·인버스·TR·액티브 예외는 1qetf.com·uppity.co.kr
    (개인/소규모 콘텐츠) 및 위 증권사·자산운용사 공식 콘텐츠에서 일치.
  - 2025-01-01 외국납부세액 공제 선환급 폐지는 RISE ETF·하나로ETF(NH-Amundi)·삼성자산운용 등
    복수의 자산운용사 공식 고객센터 공지(riseetf.co.kr, hanaroetf.com, nh-amundi.com)와
    조세일보(언론, joseilbo.com)에서 동일하게 확인되어 충돌 없음.
  세율·공제한도 자체는 신규 숫자가 아니라 이미 원문 확정된 값의 재사용이고, 이번 편에서 새로 다루는
  사실(과세방식 분류, 계산 방법론, 제도 개편)은 과거 오류가 발견됐던 "세율·공제한도·과세표준 구간"
  유형이 아니라 구조·절차형 사실이라 교차검증으로 진행했다. 한계는 self_check에 투명 공개.
기준일: 2026-09-13 (WebSearch 확인일, 외국납부세액 공제 개편 시행일 2025-01-01)
tags: 국내상장해외ETF, ETF세금, 배당소득세, 보유기간과세, 손익통산, 금융소득종합과세, 외국납부세액공제, 주식초보, ETF투자
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-13).
  게이트1: 네이버 키워드도구 실측 1,230회(check-keywords.yml, 2026-09-13). 이번 배치 8개 후보 중
  유일하게 PASS(나머지 7개는 20~220회로 게이트1 미달).
  게이트2: v3 기준 통과(serp_check 참조) — 개인/소규모 콘텐츠 다수 진입, 예외 규정·계산 방식·
  2025년 제도 개편 미반영으로 정보이득 여지 뚜렷.
  게이트3: 레버리지·인버스·TR·액티브 예외 + 보유기간과세 계산 예시 + 손익통산 불가 원 단위 예시 +
  2025년 외국납부세액 공제 개편으로 정보이득 확보.
  게이트4: nts.go.kr 1회 시도 EGRESS_BLOCKED 확인(google.com 대조군도 차단, 세션 전면 차단) 후
  RULES.md 2026-09-12 기준에 따라 세율 등 기존 확정값은 4·5·6편 원문 재사용, 신규 사실(계산방식·
  손익통산·2025년 개편)은 10곳 이상 독립 출처(증권사·자산운용사 공식, 언론 2곳, 학회 논문, 개인
  콘텐츠) 교차검증으로 진행, 충돌 없음 확인.
self_check: |
  [2026-09-13 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 1,230회(제도·세금 세부 키워드 기준 100회 이상).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 상위 검색 결과가 다루지 않는 예외 규정(레버리지·인버스·TR·액티브)과 보유기간과세
  계산 방식, 손익통산 불가 원 단위 예시, 2025년 외국납부세액 공제 개편을 정리해 차별화했다.
  게이트4 — nts.go.kr에 1회 시도해 EGRESS_BLOCKED 확인, google.com 대조군도 차단되어 세션 전면
  차단으로 판단. 세율(15.4%/22%/250만원/2천만원)은 신규 숫자가 아니라 4·5·6편에서 이미 원문
  확정한 값을 재사용했고, 이번 편의 신규 사실(계산 방식·손익통산 여부·2025년 제도 개편)은 서로
  무관한 10곳 이상 독립 출처(증권사·자산운용사 공식 콘텐츠 7곳, 언론 2곳, 세무학회 논문 1곳)가
  충돌 없이 일치함을 확인해 캡처 요청 없이 진행했다.
  카니벌라이제이션 점검 — 5편(해외주식 양도소득세 신고 방법)은 개별 해외주식 직접투자가 중심,
  10편(ETF 수수료)·22편(ETF 괴리율)은 매매비용·가격괴리가 중심, 4편(배당소득세)은 일반 배당소득
  세율이 중심. 이 글은 "ETF가 담은 자산 구성에 따라 과세 방식 자체가 달라진다"는 분류·계산 문제가
  중심이라 검색 의도가 겹치지 않는다. 본문에서 4·5·6·10편으로 내부 링크를 건다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문에서 안내하는 자리와 하단 참고 출처 전부
  target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow 미부착.
  제목 "국내상장 해외ETF 세금 얼마나 내나" 20자(공백 포함)·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 5단어(domestic-listed-overseas-etf-tax). FAQ 6개와 JSON-LD 1:1 일치.
  @id 티스토리 entry 패턴. 종목·상품 추천 없음. 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 기존 확정값 재사용 + 신규 사실 교차검증으로 대체,
  한계 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-13</p>

<p>같은 ETF라도 <mark>담긴 자산이 국내주식인지 해외주식인지에 따라 세금 매기는 방식 자체가 다릅니다</mark>. 국내상장 해외ETF는 매매차익과 분배금 모두 배당소득세 15.4%가 붙고, 손익통산도 되지 않습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>국내상장 해외ETF는 <mark>매매차익·분배금 모두 배당소득세 15.4%</mark>가 원천징수됩니다.</li>
    <li>국내주식형 ETF는 매매차익이 비과세지만, <b>레버리지·인버스·TR·액티브형</b>은 국내주식을 담고 있어도 과세 대상입니다.</li>
    <li>매매차익은 실제 차익이 아니라 <b>과표기준가 증가분과 실제 차익 중 더 작은 금액</b>에만 과세됩니다(보유기간과세).</li>
    <li>국내상장 해외ETF끼리는 <b>손익통산이 안 되고</b>, 2025년부터 외국납부세액 공제 방식도 바뀌었습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>국내상장 해외ETF, 왜 세금이 다르게 매겨지나요</li>
  <li>매매차익은 어떻게 계산하나요</li>
  <li>분배금은 얼마나 떼나요</li>
  <li>손익통산이 안 된다는 게 무슨 뜻인가요</li>
  <li>해외 직접 상장 ETF와 세금이 어떻게 다른가요</li>
  <li>2025년부터 외국납부세액 공제는 어떻게 바뀌었나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">국내상장 해외ETF, 왜 세금이 다르게 매겨지나요</h2>

<p>같은 국내 증권거래소에 상장된 ETF라도, 담고 있는 자산이 국내주식인지 해외주식·채권·원자재인지에 따라 세법상 분류가 달라집니다. <b>국내주식형 ETF</b>(대부분 국내 시장대표·섹터 ETF)는 국내 개별주식과 형평을 맞춰 매매차익에 세금을 매기지 않습니다.</p>

<p>반면 <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">해외주식이 단 한 종목이라도 들어 있는 ETF는 국내상장 해외ETF로 분류돼 매매차익에도 배당소득세가 과세됩니다.</span> 채권형·원자재형·파생형 ETF도 같은 방식으로 과세됩니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>국내주식으로만 구성돼도 과세될 수 있습니다</b>
  <p style="margin:8px 0 0 0;">국내주식형 ETF라도 <b>레버리지·인버스·TR(토탈리턴)·액티브</b> 유형이면 매매차익 비과세 대상에서 빠지고, 국내상장 해외ETF와 동일하게 보유기간과세(배당소득세 15.4%)가 적용됩니다. "국내주식만 담으면 세금이 없다"고 단순하게 판단하면 안 되는 이유입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">매매차익은 어떻게 계산하나요</h2>

<p>국내상장 해외ETF의 매매차익 과세에는 <b>보유기간과세</b>라는 방식이 적용됩니다. 실제로 벌어들인 매매차익 전부에 세금을 매기는 것이 아니라, <b>매수 시점과 매도 시점의 과표기준가격 차이(증가분)와 실제 매매차익 중 더 작은 금액</b>에만 15.4%가 과세됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시(가상의 숫자)</b>
  <p style="margin:8px 0 0 0;">매수 시 과표기준가격 10,000원, 매도 시 과표기준가격 11,500원이라면 과표기준가 증가분은 1,500원입니다. 만약 실제 매매차익이 1,800원이라면, 둘 중 더 작은 금액인 <mark>1,500원에만</mark> 15.4%가 과세돼 세금은 약 231원입니다.</p>
</div>

<p>과표기준가격은 펀드가 실제로 보유한 자산의 손익을 반영해 매일 산출되는 기준가로, 운용사·증권사 앱에서 종목별로 조회할 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">분배금은 얼마나 떼나요</h2>

<p>분배금(배당)은 계산이 단순합니다. <b>지급 시점에 15.4%가 원천징수</b>되고, 세후 금액이 계좌로 들어옵니다. 매매차익처럼 보유기간과세를 따지지 않고 지급액 전체에 곧바로 세율이 적용됩니다.</p>

<ul style="line-height:1.9;">
  <li>매매차익 — 과표기준가 증가분과 실제 차익 중 더 작은 금액에 15.4%</li>
  <li>분배금 — 지급액 전체에 15.4% 즉시 원천징수</li>
</ul>

<p>매매차익과 분배금을 합친 금융소득이 연 2,000만 원을 넘으면 다른 소득과 합산되는 <a href="https://sensitiveboss3.tistory.com/entry/financial-income-comprehensive-tax" target="_blank" rel="noopener">금융소득종합과세</a> 대상이 될 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">손익통산이 안 된다는 게 무슨 뜻인가요</h2>

<p>국내상장 해외ETF는 배당소득으로 과세되기 때문에, <b>같은 해에 여러 종목을 매도해도 이익과 손실을 서로 상계(손익통산)할 수 없습니다.</b> 이익이 난 종목은 그 이익 전액에 과세되고, 손실이 난 종목의 손실은 세금 계산에 반영되지 않습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시(가상의 숫자)</b>
  <p style="margin:8px 0 0 0;">같은 해에 ETF A를 팔아 100만 원 이익을, ETF B를 팔아 50만 원 손실을 봤다면, 두 금액을 합쳐 순이익 50만 원으로 계산할 수 없습니다. <mark>이익 100만 원 전액에 15.4%(약 15만 4천 원)가 원천징수</mark>되고, 50만 원 손실은 반영되지 않습니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">해외 직접 상장 ETF와 세금이 어떻게 다른가요</h2>

<p>같은 미국 지수를 추종해도, <b>국내 거래소에 상장된 ETF</b>와 <b>미국 거래소에 직접 상장된 ETF</b>를 사는 것은 과세 방식이 전혀 다릅니다. 아래 표로 비교합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">국내상장 해외ETF</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">해외 직접 상장 ETF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매매차익 세목·세율</td>
      <td style="border:1px solid #ddd;padding:8px;">배당소득세 15.4%</td>
      <td style="border:1px solid #ddd;padding:8px;">양도소득세 22%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">기본공제</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">연 250만 원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">손익통산</td>
      <td style="border:1px solid #ddd;padding:8px;">불가</td>
      <td style="border:1px solid #ddd;padding:8px;">가능(같은 해 해외주식·해외ETF끼리)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">납부 방식</td>
      <td style="border:1px solid #ddd;padding:8px;">매도·지급 시 자동 원천징수</td>
      <td style="border:1px solid #ddd;padding:8px;">다음 해 5월 본인이 직접 신고·납부</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">금융소득종합과세 합산</td>
      <td style="border:1px solid #ddd;padding:8px;">대상(연 2,000만 원 초과 시)</td>
      <td style="border:1px solid #ddd;padding:8px;">비대상(분리과세)</td>
    </tr>
  </tbody>
</table>

<p>개별 해외주식을 직접 매수했을 때의 양도소득세 신고 절차는 <a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing" target="_blank" rel="noopener">이전 글(해외주식 양도소득세 신고 방법)</a>에서 다뤘습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2025년부터 외국납부세액 공제는 어떻게 바뀌었나요</h2>

<p>국내상장 해외ETF가 해외 주식에서 배당을 받으면 해외에서도 세금이 원천징수됩니다. 예전에는 이 해외 납부세액을 <b>먼저 돌려받아('선환급') 세전 배당금에 얹은 뒤</b> 국내에서 15.4%를 다시 원천징수했습니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">2025년 1월 1일부터 이 선환급 절차가 폐지</span>되고, 원천징수의무자인 증권사·은행이 투자자별로 외국납부세액 공제 금액을 계산해 원천징수 단계에서 바로 반영하는 방식으로 바뀌었습니다.</p>

<ul style="line-height:1.9;">
  <li>일반 위탁계좌 — 개편 후에도 종합소득세 신고 시 외국납부세액 공제를 받을 수 있어 최종 수령액에 큰 차이가 없다고 안내되고 있습니다.</li>
  <li>ISA·연금계좌 — 각 계좌의 별도 과세체계가 적용돼 처리 방식이 다르며, 향후 세부 규정이 추가로 조정될 수 있습니다.</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내상장 해외ETF와 국내주식형 ETF는 세금이 왜 다른가요</summary>
  <p style="margin:10px 0 0 0;">해외주식·채권·원자재가 담긴 ETF는 매매차익도 배당소득으로 과세되지만, 국내주식형 ETF는 국내 개별주식과 형평을 맞춰 매매차익을 비과세하기 때문입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내주식으로만 구성된 ETF도 세금을 낼 수 있나요</summary>
  <p style="margin:10px 0 0 0;">네. 레버리지·인버스·TR·액티브 유형은 국내주식을 담고 있어도 매매차익 비과세 대상에서 제외돼 배당소득세 15.4%가 과세됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">보유기간과세는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">매수·매도 시점의 과표기준가격 증가분과 실제 매매차익 중 더 작은 금액에만 15.4%를 과세하는 방식입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내상장 해외ETF끼리 손실과 이익을 합쳐서 계산할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 손익통산이 되지 않아 이익이 난 종목은 전액 과세되고, 손실이 난 종목의 손실은 세금 계산에 반영되지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내상장 해외ETF와 해외 직접 상장 ETF 중 세금이 더 적은 쪽은 정해져 있나요</summary>
  <p style="margin:10px 0 0 0;">정해져 있지 않습니다. 세율·공제·손익통산 여부가 서로 달라 투자 규모와 손익 상황에 따라 유불리가 달라지므로 표를 비교해 판단해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">2025년부터 외국납부세액 공제는 어떻게 달라졌나요</summary>
  <p style="margin:10px 0 0 0;">해외 납부세액을 먼저 돌려받던 '선환급' 절차가 폐지되고, 증권사·은행이 투자자별로 공제 금액을 계산해 원천징수 단계에서 바로 반영하는 방식으로 바뀌었습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> — 배당소득세·양도소득세 일반 기준(4·5·6편에서 원문 확인)</li>
    <li><a href="https://m.joseilbo.com/news/view.htm?newsid=569118" target="_blank" rel="noopener">조세일보 — 해외ETF 외국납부세액공제 안내</a></li>
    <li><a href="https://www.kookje.co.kr/news2011/asp/newsbody.asp?code=1700&amp;key=20251219.99099007352" target="_blank" rel="noopener">국제신문 — [차호중의 재테크 칼럼] ETF와 세금</a></li>
  </ul>
  기준일: 2026-09-13(WebSearch 확인일). 외국납부세액 공제 개편 시행일은 2025-01-01입니다. 국세청 원문은 이번 세션 WebFetch가 차단돼 직접 확인하지 못했고, 세율·공제 기준은 이 시리즈 4·5·6편에서 이미 원문으로 확정한 값을 재사용했으며, 계산 방식·손익통산·2025년 개편은 위 언론과 증권사·자산운용사 공식 콘텐츠 등 10곳 이상 독립 출처의 교차 확인으로 대체했습니다.
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
  "headline": "국내상장 해외ETF 세금 얼마나 내나",
  "description": "국내상장 해외ETF의 매매차익·분배금 배당소득세 15.4%, 보유기간과세 계산법, 손익통산 불가 여부와 해외 직접 상장 ETF 세금 비교, 2025년 외국납부세액 공제 개편까지 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-13",
  "dateModified": "2026-09-13",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/domestic-listed-overseas-etf-tax"
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
      "name": "국내상장 해외ETF와 국내주식형 ETF는 세금이 왜 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "해외주식·채권·원자재가 담긴 ETF는 매매차익도 배당소득으로 과세되지만, 국내주식형 ETF는 국내 개별주식과 형평을 맞춰 매매차익을 비과세하기 때문입니다." }
    },
    {
      "@type": "Question",
      "name": "국내주식으로만 구성된 ETF도 세금을 낼 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 레버리지·인버스·TR·액티브 유형은 국내주식을 담고 있어도 매매차익 비과세 대상에서 제외돼 배당소득세 15.4%가 과세됩니다." }
    },
    {
      "@type": "Question",
      "name": "보유기간과세는 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "매수·매도 시점의 과표기준가격 증가분과 실제 매매차익 중 더 작은 금액에만 15.4%를 과세하는 방식입니다." }
    },
    {
      "@type": "Question",
      "name": "국내상장 해외ETF끼리 손실과 이익을 합쳐서 계산할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 손익통산이 되지 않아 이익이 난 종목은 전액 과세되고, 손실이 난 종목의 손실은 세금 계산에 반영되지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "국내상장 해외ETF와 해외 직접 상장 ETF 중 세금이 더 적은 쪽은 정해져 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "정해져 있지 않습니다. 세율·공제·손익통산 여부가 서로 달라 투자 규모와 손익 상황에 따라 유불리가 달라지므로 표를 비교해 판단해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "2025년부터 외국납부세액 공제는 어떻게 달라졌나요",
      "acceptedAnswer": { "@type": "Answer", "text": "해외 납부세액을 먼저 돌려받던 '선환급' 절차가 폐지되고, 증권사·은행이 투자자별로 공제 금액을 계산해 원천징수 단계에서 바로 반영하는 방식으로 바뀌었습니다." }
    }
  ]
}
</script>
