---
keyword: 주식 매도 세금
title: 주식 매도 세금 얼마
slug: stock-sell-tax-amount
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1250 (PC 290 / 모바일 960)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: WebSearch 확인(2026-09-04) — 상위 5개 중 공식·금융사·백과 2~3개(kbthink/kbcapital 같은 계열, namu.wiki), 나머지 개인 커뮤니티/세무서비스 마케팅. 5개 미만이라 통과.
unique_asset: 국내 상장주식 매도 시 증권거래세 실제 계산(코스피/코스닥/코넥스 요율별 100만원·1,000만원 매도 예시) + 양도소득세 과세 여부 판단 기준 + 대주주·해외주식 양도소득세 계산 예시. 전부 1차 출처의 공식 세율·공제액을 그대로 적용한 계산.
primary_source: 찾기쉬운 생활법령정보(법제처) "양도소득세·증권거래세 및 배당소득세" (2026년 8월 15일 기준 작성) — 소득세법 제104조·증권거래세법 제7·8조 등 명시 / 국세청 "양도소득세" 안내 페이지 / sources/stock-sell-tax-nts.md
기준일: 2026년 8월 기준 (법제처 원문 명시 기준일 그대로 사용 — 발행 3주 이내로 신선함)
tags: 주식매도세금, 증권거래세, 양도소득세, 주식세금, 대주주양도세, 해외주식세금, 주식초보, 증권거래세율, 양도소득세율
gate_pass: true
self_check: |
  게이트1 통과(1,250회, 세부·제도 기준 월100 이상). 게이트2 통과(WebSearch 확인, 공식·백과 2~3/5).
  게이트3 충족 — 1차 출처의 공식 세율·공제액을 적용한 실제 계산 예시(계산예시형 정보이득), 캡처 불필요.
  게이트4 충족 — 법제처 생활법령정보 원문 확인, 기준일 2026-08-15 명시(3주 이내로 신선), 소득세법·증권거래세법 조문 인용.
  제목 8자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈. FAQ 6개와 JSON-LD 1:1 일치.
  @id를 티스토리 entry 패턴으로 지정. 자동화 가능(oneclick) — 사람은 검토 후 붙여넣기+발행만 하면 됨.
  이미지는 별도 캡처 불필요(oneclick 유형) — 다만 og:image 확보를 위해 참고용 도표 이미지를 원하면 직접 추가 가능.
---

<p>주식을 팔면 <mark>증권거래세는 누구나 내지만, 양도소득세는 대부분의 개인 투자자가 내지 않습니다.</mark> 국내 상장주식을 증권시장에서 파는 소액주주라면 원칙적으로 양도소득세 대상이 아니기 때문입니다. 이 글에서는 실제 세율로 계산한 예시를 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>증권거래세는 매도 금액에 <b>코스피 0.05%, 코스닥·협회장외 0.2%, 코넥스 0.1%</b>가 자동으로 붙습니다.</li>
    <li>양도소득세는 <b>대주주, 비상장주식, 해외주식</b>을 파는 경우에만 냅니다.</li>
    <li>대주주가 아니고 국내 상장주식을 증권시장 안에서 팔면 <b>양도소득세는 0원</b>입니다.</li>
    <li>해외주식은 대주주 여부와 상관없이 <b>연 250만원을 넘는 차익</b>에 세금이 붙습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>주식 팔면 세금 얼마나 내나요</li>
  <li>증권거래세는 얼마나 내나요</li>
  <li>양도소득세도 내야 하나요</li>
  <li>양도소득세는 얼마나 내나요</li>
  <li>세금은 언제 어떻게 내나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">주식 팔면 세금 얼마나 내나요</h2>

<p>주식을 팔 때 붙는 세금은 <b>증권거래세</b>와 <b>양도소득세</b> 두 가지입니다. 증권거래세는 국내 상장주식을 팔 때마다 예외 없이 부과됩니다.</p>

<p>반면 양도소득세는 조건에 해당하는 경우에만 냅니다. <mark>대주주가 아닌 소액주주가 국내 상장주식을 증권시장 안에서 팔면 양도소득세 과세 대상이 아닙니다.</mark> 비상장주식이나 해외주식은 대주주 여부와 관계없이 별도 기준이 적용됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>과세 대상 요약</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>증권거래세: 국내 상장주식 매도 시 항상 부과</li>
    <li>양도소득세: 대주주가 파는 주식, 비상장주식, 해외주식에 부과</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">증권거래세는 얼마나 내나요</h2>

<p>증권거래세는 <b>주식의 양도가액에 시장별 세율을 곱해</b> 계산합니다. 시장에 따라 세율이 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">시장 구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세율</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">유가증권시장(코스피)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>0.05%</mark></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">코넥스시장</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.1%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">코스닥시장 · 금융투자협회 장외 양도</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.2%</td></tr>
  </tbody>
</table>

<p>이 세율을 실제 매도 금액에 적용하면 다음과 같습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">매도 금액</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">코스피(0.05%)</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">코스닥(0.2%)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">100만 원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">500원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">2,000원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">1,000만 원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">20,000원</td></tr>
  </tbody>
</table>

<p>증권거래세는 <b>매도할 때 증권사가 자동으로 징수</b>합니다. 따로 신고하거나 납부할 필요가 없습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">양도소득세도 내야 하나요</h2>

<p>대부분의 개인 투자자는 양도소득세를 내지 않습니다. <mark>국내 상장주식을 증권시장 안에서 파는 소액주주는 양도소득세 과세 대상이 아니기 때문입니다.</mark></p>

<p>다만 아래 경우는 다릅니다.</p>

<div style="background:#fff8e6;border-left:4px solid #e0a800;padding:14px 18px;margin:20px 0;">
  <b>양도소득세를 내야 하는 경우</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>주권상장법인 <b>대주주</b>가 주식을 팔 때</li>
    <li>대주주가 아니더라도 <b>증권시장 밖에서</b> 상장주식을 팔 때</li>
    <li><b>비상장주식</b>을 팔 때 (대주주·소액주주 구분 없이 모두 대상)</li>
    <li><b>해외주식</b>을 팔 때 (대주주 여부와 무관)</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">양도소득세는 얼마나 내나요</h2>

<p>양도소득세는 <b>양도소득과세표준에 세율을 곱해</b> 계산합니다. 과세표준은 양도소득금액에서 필요경비와 기본공제(연 250만 원)를 뺀 금액입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세율</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">대주주 · 1년 미만 보유(중소기업 외 법인)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">30%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">대주주 · 과세표준 3억 원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">20%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">대주주 · 과세표준 3억 원 초과분</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6천만 원 + 초과액의 25%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">대주주 아닌 자 · 중소기업 주식</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">10%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">해외주식 · 중소기업 외</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">20%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">해외주식 · 중소기업</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">10%</td></tr>
  </tbody>
</table>

<p>예를 들어 대주주가 아닌 투자자가 <b>해외주식에서 연 500만 원의 차익</b>을 냈다고 가정하면, 기본공제 250만 원을 뺀 <b>과세표준 250만 원에 20%를 곱해 50만 원</b>이 양도소득세가 됩니다.</p>

<p>대주주가 <b>과세표준 2억 원</b>의 양도차익을 냈다면 3억 원 이하 구간이므로 <b>20%인 4천만 원</b>이 세금입니다. 과세표준이 <b>5억 원</b>이라면 3억 원 초과분(2억 원)에 25%를 곱한 5천만 원에 6천만 원을 더해 <b>1억 1천만 원</b>이 됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">세금은 언제 어떻게 내나요</h2>

<p>증권거래세는 <b>매도 시점에 증권사가 자동으로 원천징수</b>합니다. 투자자가 별도로 할 일은 없습니다.</p>

<p>양도소득세는 다릅니다. <mark>주식을 판 반기(半期)의 말일부터 2개월 이내에 예정신고를 하고 세액을 납부해야 합니다.</mark> 이후 여러 번 양도해 세액이 달라지면 다음 해 5월 1일부터 31일까지 확정신고를 합니다.</p>

<p>해외주식은 절차가 조금 다릅니다. 예정신고 없이 <b>다음 해 5월 1일부터 31일까지 확정신고만</b> 하면 됩니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>증권거래세는 국내 상장주식을 팔면 누구나, 자동으로 냅니다.</li>
    <li>양도소득세는 대주주·비상장·해외주식에 해당할 때만 냅니다.</li>
    <li>양도소득세는 반기별 예정신고 + 다음 해 5월 확정신고가 원칙입니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주식을 팔면 항상 세금을 내나요</summary>
  <p style="margin:10px 0 0 0;">네, 국내 상장주식을 팔면 증권거래세는 항상 부과됩니다. 다만 양도소득세는 대주주나 해외주식 등 특정 조건에 해당할 때만 냅니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코스피와 코스닥의 증권거래세율이 다른가요</summary>
  <p style="margin:10px 0 0 0;">네, 다릅니다. 코스피(유가증권시장)는 0.05%, 코스닥과 금융투자협회 장외 양도는 0.2%, 코넥스는 0.1%입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">소액주주도 양도소득세를 내나요</summary>
  <p style="margin:10px 0 0 0;">아니요, 국내 상장주식을 증권시장 안에서 파는 소액주주는 양도소득세 과세 대상이 아닙니다. 대주주이거나 증권시장 밖에서 거래하는 경우에만 부과됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식을 팔면 세금이 다른가요</summary>
  <p style="margin:10px 0 0 0;">네, 해외주식은 대주주 여부와 상관없이 연 250만 원을 넘는 차익에 양도소득세가 붙습니다. 세율은 중소기업 주식 10%, 그 외 20%입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">양도소득세 기본공제는 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">연 250만 원입니다. 양도소득금액에서 필요경비와 이 기본공제를 뺀 금액이 과세표준이 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">양도소득세는 언제 신고하나요</summary>
  <p style="margin:10px 0 0 0;">주식을 판 반기의 말일부터 2개월 이내에 예정신고를 하고, 세액이 달라지면 다음 해 5월에 확정신고를 합니다. 해외주식은 예정신고 없이 다음 해 5월에 확정신고만 하면 됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (2026년 8월 15일 기준):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1701&ccfNo=2&cciNo=3&cnpClsNo=1" target="_blank" rel="noopener">찾기쉬운 생활법령정보(법제처) — 양도소득세·증권거래세 및 배당소득세</a></li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&mi=12274" target="_blank" rel="noopener">국세청 — 양도소득세 안내</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를 권유하지 않습니다.
투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·공제·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "주식을 팔면 항상 세금을 내나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네, 국내 상장주식을 팔면 증권거래세는 항상 부과됩니다. 다만 양도소득세는 대주주나 해외주식 등 특정 조건에 해당할 때만 냅니다."
      }
    },
    {
      "@type": "Question",
      "name": "코스피와 코스닥의 증권거래세율이 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네, 다릅니다. 코스피(유가증권시장)는 0.05%, 코스닥과 금융투자협회 장외 양도는 0.2%, 코넥스는 0.1%입니다."
      }
    },
    {
      "@type": "Question",
      "name": "소액주주도 양도소득세를 내나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아니요, 국내 상장주식을 증권시장 안에서 파는 소액주주는 양도소득세 과세 대상이 아닙니다. 대주주이거나 증권시장 밖에서 거래하는 경우에만 부과됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "해외주식을 팔면 세금이 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네, 해외주식은 대주주 여부와 상관없이 연 250만 원을 넘는 차익에 양도소득세가 붙습니다. 세율은 중소기업 주식 10%, 그 외 20%입니다."
      }
    },
    {
      "@type": "Question",
      "name": "양도소득세 기본공제는 얼마인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "연 250만 원입니다. 양도소득금액에서 필요경비와 이 기본공제를 뺀 금액이 과세표준이 됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "양도소득세는 언제 신고하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "주식을 판 반기의 말일부터 2개월 이내에 예정신고를 하고, 세액이 달라지면 다음 해 5월에 확정신고를 합니다. 해외주식은 예정신고 없이 다음 해 5월에 확정신고만 하면 됩니다."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "주식 매도 세금 얼마",
  "description": "주식을 팔 때 내는 증권거래세와 양도소득세를 법제처·국세청 공식 세율로 계산한 예시로 정리했습니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-04",
  "dateModified": "2026-09-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-sell-tax-amount"
  }
}
</script>
