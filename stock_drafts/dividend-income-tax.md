---
keyword: 배당소득세
title: 배당소득세 얼마 떼나
slug: dividend-income-tax
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 확인필요
gate1_pass: false (자동 조회 대기 — 커밋 후 notify-repo-only.yml이 네이버 키워드도구로 채울 예정. 큐 예비조사 당시 월 3,860회로 기록되어 있었으나 최종 판정은 자동 재조회 결과를 기다림)
serp_check: WebSearch 확인(2026-09-04) — "배당소득세" 관련 상위 7개 중 공식·언론·백과류 4개(kbthink.com 금융사 콘텐츠, kcmi.re.kr 자본시장연구원, namu.wiki 2건), 개인/서비스형 블로그 3개(taxcalc.co.kr 세금계산기, jiwonfund.kr 개인블로그, hometax-go.kr 개인 사이트·공식 홈택스 도메인 아님). 5개 미만이라 게이트2는 통과. 다만 이 결과는 WebSearch 요약 기반 추정치이며 구글 상위 10개 전체를 직접 스크롤 확인한 것은 아님.
unique_asset_plan: 배당금 원천징수 계산 예시 + 금융소득종합과세 판단 절차 (세율·기준금액은 1차 출처 캡처 전까지 표에서 비워둠)
primary_source: 미확보 — easylaw.go.kr(법제처 찾기쉬운 생활법령정보), nts.go.kr(국세청), kofia.or.kr 전부 이번 세션에서 WebFetch가 EGRESS_BLOCKED로 실패. www.google.com 대조군도 동일하게 차단되어 이번 세션은 WebFetch 자체가 전면 차단된 상태로 판단. 상세 기록: sources/dividend-income-tax-access-note.md
기준일: 미확정 — 캡처 시 원문에 명시된 기준일을 그대로 기입할 것
tags: 배당소득세, 배당소득세율, 금융소득종합과세, 원천징수세율, 배당금세금, 주식배당세금, 배당소득세계산, 금융소득기준금액, 종합과세기준
gate_pass: false
capture_guide: |
  왜 필요한가: 배당소득세 원천징수세율과 금융소득종합과세 합산기준금액(2천만원)은 여러 비공식
  출처(금융사 콘텐츠, 세금계산기 서비스)에서 서로 일치하게 나타나지만, 1차 출처 원문을 이번
  세션에서 열람하지 못해 RULES.md 게이트4(1차 출처만 인정)를 충족하지 못했습니다. 아래 화면에서
  "배당소득세 원천징수세율·금융소득종합과세 기준금액·종합과세 시 적용 세율표·기준일"이 함께
  보이는 부분을 캡처해서 보내주시면 표를 채우고 게이트를 다시 판정하겠습니다.

  1순위 — 법제처 찾기쉬운 생활법령정보: https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1701&ccfNo=2&cciNo=3&cnpClsNo=1
  ("주식투자자 > 주식의 거래 > 주식거래에 따른 세금 납부하기 > 양도소득세·증권거래세 및
  배당소득세" 페이지) 접속 → 배당소득세 항목에서 원천징수세율(소득세+지방소득세), 금융소득
  종합과세 합산기준금액, 종합과세 시 적용되는 세율 구간, "이 정보는 OOOO년 O월 O일 기준" 문구가
  함께 보이도록 화면 캡처.
  2순위 — 국세청: https://www.nts.go.kr 접속 → 검색창에 "배당소득세" 입력 → 세금종류별 안내
  페이지에서 원천징수세율·조문 근거 캡처.
  3순위 — 국세청 국세법령정보시스템(https://taxlaw.nts.go.kr)에서 소득세법 배당소득 관련 조문
  원문 캡처 (조문 번호와 시행일이 함께 보이게).

  캡처했으면: 스크린샷을 이 대화에 그대로 올려주세요. 그걸로 표를 채우고 재판정하겠습니다.
self_check: |
  게이트1 미확인 — monthly_search_volume을 확인필요로 기록. 커밋 후 notify-repo-only.yml이 자동 조회해 채울 예정.
  게이트2 통과 — WebSearch 상위 7개 중 공식·언론·백과 4개(5개 미만).
  게이트3 미충족 — 계산 예시가 정보 이득의 핵심인데 정확한 세율을 1차 출처로 확인하지 못해 표 값이 비어 있음.
  게이트4 미충족 — easylaw.go.kr / nts.go.kr / kofia.or.kr 전부 WebFetch EGRESS_BLOCKED. 대조군인 www.google.com도 동일하게 차단되어 도메인별 차단이 아니라 이번 세션의 WebFetch 자체가 전면 차단된 것으로 판단(같은 날 isa-limit-benefit 초안이 남긴 관찰과 일치, 두 번째 재현).
  출처 신선도: 원문을 못 열어 확인 불가 — 캡처 시 반드시 페이지의 기준일/시행일을 함께 확인해야 함.
  제목 "배당소득세 얼마 떼나" 9자, 30자 이내, 금지어 없음, 조사·접속사 없음. "금액형" 패턴({대상} 얼마)에 부합.
  슬러그 dividend-income-tax 영문 소문자+하이픈 3단어.
  FAQ 6개와 JSON-LD 1:1 일치. @id를 티스토리 entry 패턴으로 지정.
  이미지 없음 — human-assisted/capture 유형이라 공식 자료 화면 캡처 이미지도 사람이 함께 준비하는 것을 권장(og:image 겸용).
  캡처 필요 항목: (1) 원천징수세율(소득세+지방소득세) 실제 값, (2) 금융소득종합과세 합산기준금액과 초과 시 적용 세율 구간, (3) 캡처한 공식 페이지의 URL과 기준일.
---

<p>배당금을 받으면 세금이 자동으로 빠져나가지만, <b>정확히 얼마가 빠지는지</b>는 원천징수세율과 금융소득종합과세 기준을 함께 봐야 알 수 있습니다. 이 글은 그 계산 구조와 확인 방법을 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>배당소득세는 배당금을 받는 즉시 <mark>원천징수 방식으로 자동 차감</mark>되므로 따로 신고할 필요가 없는 경우가 많습니다.</li>
    <li>정확한 원천징수세율은 자료마다 표현이 조금씩 달라 <b>공식 출처로 직접 확인</b>하는 것이 안전합니다.</li>
    <li>이자·배당소득을 합쳐 일정 금액을 넘으면 <b>금융소득종합과세</b> 대상이 되어 다른 소득과 합산해 세금을 다시 계산합니다.</li>
    <li>본인이 종합과세 대상인지, 대상이라면 얼마를 더 내는지는 합산기준금액과 세율 구간을 정확히 알아야 계산할 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>배당소득세란 무엇인가요</li>
  <li>배당소득세 세율은 왜 원문으로 다시 확인해야 하나요</li>
  <li>배당소득세는 언제 얼마나 원천징수되나요</li>
  <li>금융소득종합과세는 무엇이고 언제 적용되나요</li>
  <li>배당소득세 관련 수치는 어디서 확인하나요</li>
  <li>배당소득세 계산 예시 (확인 중)</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당소득세란 무엇인가요</h2>

<p>배당소득세는 주식을 보유해 받은 <b>배당금에 부과되는 세금</b>입니다. 근로소득세처럼 매년 따로 신고서를 내는 것이 아니라, 배당금을 지급하는 회사(또는 증권사)가 지급 시점에 세금을 미리 떼는 <b>원천징수</b> 방식으로 처리됩니다.</p>

<p><mark>배당금이 통장에 들어올 때는 이미 세금이 빠진 금액</mark>인 경우가 대부분이라, 투자자가 별도로 계산해서 납부할 일이 적습니다. 다만 다른 금융소득과 합산되는 경우는 예외입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당소득세 세율은 왜 원문으로 다시 확인해야 하나요</h2>

<p>배당소득세 원천징수세율은 인터넷 검색만 해봐도 여러 글에서 같은 숫자가 반복되는 편입니다. 하지만 <mark>정확한 세율과 종합과세 기준금액은 소득세법에 근거한 수치</mark>이므로, 이 글은 확인되지 않은 숫자를 그대로 옮겨 적지 않았습니다.</p>

<div style="background:#fff8e6;border-left:4px solid #e0a800;padding:14px 18px;margin:20px 0;">
  <b>확인이 필요한 이유</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>세율과 기준금액은 세법 개정에 따라 바뀔 수 있는 수치입니다.</li>
    <li>블로그·언론 기사마다 인용 시점이 달라 최신 여부를 장담하기 어렵습니다.</li>
    <li>1차 출처(법제처·국세청) 원문을 직접 확인해야 기준일까지 함께 알 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당소득세는 언제 얼마나 원천징수되나요</h2>

<p>배당금을 지급받는 순간, 지급하는 쪽(회사·증권사)이 소득세와 지방소득세를 더한 세율만큼을 <b>미리 떼고 나머지 금액</b>을 지급합니다. 세후 실수령액은 배당금에서 원천징수세액을 뺀 값입니다.</p>

<p style="font-size:13px;color:#888;">정확한 세율(%)은 1차 출처 캡처 전까지 이 글에서 확정하지 않습니다. 캡처가 반영되면 아래 표와 계산 예시가 채워집니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">금융소득종합과세는 무엇이고 언제 적용되나요</h2>

<p>이자소득과 배당소득을 <b>1년 동안 합친 금액</b>이 일정 기준금액을 넘으면, 그 초과분이 다른 소득(근로소득·사업소득 등)과 합산되어 <b>종합소득세율</b>로 다시 계산됩니다. 이를 금융소득종합과세라고 합니다.</p>

<ul style="line-height:1.9;">
  <li>기준금액 이하: 원천징수만으로 납세 의무가 끝나는 경우가 많습니다(분리과세).</li>
  <li>기준금액 초과: 초과분이 다른 소득과 합산되어 종합소득세율이 적용됩니다.</li>
  <li>정확한 기준금액과 세율 구간은 1차 출처 캡처 후 이 글에 반영합니다.</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당소득세 관련 수치는 어디서 확인하나요</h2>

<p>정확한 세율과 기준금액은 아래 공식 경로에서 직접 확인하는 것이 가장 안전합니다.</p>

<ol style="line-height:1.9;">
  <li><b>법제처 찾기쉬운 생활법령정보</b>에서 "주식거래에 따른 세금 납부하기" 항목을 확인합니다.</li>
  <li><b>국세청</b> 홈페이지 또는 국세법령정보시스템에서 배당소득 관련 세율·조문을 확인합니다.</li>
  <li>실제 거래하는 <b>증권사 앱</b>의 배당금 지급 내역에서 실제 차감된 세액을 직접 확인할 수도 있습니다.</li>
</ol>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>확인할 때 함께 메모해 둘 것</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>확인한 페이지의 <b>기준일 또는 시행일</b></li>
    <li>원천징수세율(소득세+지방소득세)</li>
    <li>금융소득종합과세 <b>합산기준금액</b>과 초과 시 적용되는 세율 구간</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">배당소득세 계산 예시 (확인 중)</h2>

<p>아래 표는 배당금별 원천징수 계산 구조를 정리하는 틀입니다. 공식 출처로 세율이 확인되는 대로 실제 수치를 채울 예정입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">배당금</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">원천징수세율</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">원천징수세액</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세후 실수령액</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">100,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">1,000,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">10,000,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">위 표는 1차 출처(법제처·국세청) 원문을 캡처해 채운 뒤에만 발행합니다. 캡처 전에는 발행하지 않습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>배당소득세는 배당금 지급 시점에 원천징수되므로 대부분 별도 신고가 필요 없습니다.</li>
    <li>이자·배당소득 합계가 기준금액을 넘으면 금융소득종합과세로 다시 계산됩니다.</li>
    <li>정확한 세율·기준금액·세율 구간은 법제처·국세청 공식 자료로 확인해야 합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당소득세란 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">주식을 보유해 받은 배당금에 부과되는 세금으로, 배당금을 지급하는 회사나 증권사가 지급 시점에 미리 떼는 원천징수 방식으로 처리됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당소득세는 따로 신고해야 하나요</summary>
  <p style="margin:10px 0 0 0;">원천징수만으로 납세 의무가 끝나는 경우가 많아 별도 신고가 필요 없는 경우가 대부분입니다. 다만 금융소득종합과세 대상이 되면 다른 소득과 합산해 신고해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당소득세 원천징수세율은 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">정확한 세율은 소득세법에 근거한 수치이며, 이 글은 1차 출처(법제처·국세청) 원문 확인 전까지 확정 수치를 싣지 않았습니다. 공식 자료로 직접 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금융소득종합과세는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">이자소득과 배당소득을 1년 동안 합친 금액이 기준금액을 넘으면, 초과분이 다른 소득과 합산되어 종합소득세율로 다시 계산되는 제도입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금융소득종합과세 대상이 되면 세금이 얼마나 늘어나나요</summary>
  <p style="margin:10px 0 0 0;">기준금액을 넘는 부분이 다른 소득과 합산되어 종합소득세율 구간에 따라 세액이 달라집니다. 정확한 세율 구간은 국세청 공식 자료로 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당소득세 관련 최신 수치는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">법제처 찾기쉬운 생활법령정보와 국세청 공식 자료가 가장 정확합니다. 실제 차감된 세액은 거래 중인 증권사 앱의 배당금 지급 내역에서도 확인할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li>1차 출처 캡처 대기 — 법제처 찾기쉬운 생활법령정보 / 국세청 중 확인된 페이지로 채울 예정 (sources/dividend-income-tax-access-note.md 참고)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를 권유하지 않습니다.
투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "배당소득세란 무엇인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "주식을 보유해 받은 배당금에 부과되는 세금으로, 배당금을 지급하는 회사나 증권사가 지급 시점에 미리 떼는 원천징수 방식으로 처리됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "배당소득세는 따로 신고해야 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "원천징수만으로 납세 의무가 끝나는 경우가 많아 별도 신고가 필요 없는 경우가 대부분입니다. 다만 금융소득종합과세 대상이 되면 다른 소득과 합산해 신고해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "배당소득세 원천징수세율은 얼마인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "정확한 세율은 소득세법에 근거한 수치이며, 이 글은 1차 출처(법제처·국세청) 원문 확인 전까지 확정 수치를 싣지 않았습니다. 공식 자료로 직접 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "금융소득종합과세는 무엇인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "이자소득과 배당소득을 1년 동안 합친 금액이 기준금액을 넘으면, 초과분이 다른 소득과 합산되어 종합소득세율로 다시 계산되는 제도입니다."
      }
    },
    {
      "@type": "Question",
      "name": "금융소득종합과세 대상이 되면 세금이 얼마나 늘어나나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "기준금액을 넘는 부분이 다른 소득과 합산되어 종합소득세율 구간에 따라 세액이 달라집니다. 정확한 세율 구간은 국세청 공식 자료로 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "배당소득세 관련 최신 수치는 어디서 확인하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "법제처 찾기쉬운 생활법령정보와 국세청 공식 자료가 가장 정확합니다. 실제 차감된 세액은 거래 중인 증권사 앱의 배당금 지급 내역에서도 확인할 수 있습니다."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "배당소득세 얼마 떼나",
  "description": "배당소득세 원천징수 계산 구조와 금융소득종합과세 판단 방법, 정확한 세율·기준금액을 확인할 수 있는 공식 출처를 정리했습니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-04",
  "dateModified": "2026-09-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/dividend-income-tax"
  }
}
</script>
