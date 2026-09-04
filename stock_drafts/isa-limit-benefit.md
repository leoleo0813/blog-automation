---
keyword: ISA 계좌 한도
title: ISA 계좌 한도 확인하는 법
slug: isa-limit-benefit
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 확인필요
gate1_pass: false
serp_check: WebSearch 확인(2026-09-04) — "ISA 계좌 한도" 상위 5개 중 공식·언론·백과 0개(미래에셋/농협 등 증권사·은행 안내 페이지 2개, 나머지 개인 재테크 블로그). 5개 미만이라 게이트2는 통과.
unique_asset_plan: 유형별(일반형/서민형/농어민형 등) 연간 납입한도·계좌 총한도·비과세 한도 실측표 + 공식 출처 확인 절차. 표 값은 1차 출처 캡처 전까지 비워둠.
primary_source: 미확보 — fsc.go.kr(금융위원회), kofia.or.kr(금융투자협회), nts.go.kr(국세청), easylaw.go.kr(법제처) 전부 이번 세션에서 WebFetch가 EGRESS_BLOCKED로 실패. 상세 기록: sources/isa-limit-access-note.md
기준일: 미확정 — 캡처 시 원문에 명시된 기준일을 그대로 기입할 것
tags: ISA계좌, ISA한도, ISA비과세, 개인종합자산관리계좌, 절세계좌, 서민형ISA, 일반형ISA, 주식초보, 재테크초보, ISA가입조건
gate_pass: false
self_check: |
  게이트1 미확인 — monthly_search_volume을 확인필요로 기록. 커밋 후 notify-repo-only.yml이 네이버 키워드도구로 자동 조회해 채울 예정. (참고: 2026-09-03 예비 조사 당시 큐에는 월 3,360회로 기록되어 있었으나, 이 초안 자체의 게이트 판정은 자동 재조회 결과를 기다린다.)
  게이트2 통과 — WebSearch 상위 5개 중 공식·언론·백과 0개.
  게이트3 미충족 — 실측표가 정보 이득의 핵심인데 1차 출처 캡처 전이라 표 값이 비어 있음. 캡처 없이는 정보 이득 없음.
  게이트4 미충족 — 1차 출처 원문에 접근하지 못했다. fsc.go.kr/kofia.or.kr/nts.go.kr/easylaw.go.kr 네 도메인 모두 WebFetch가 EGRESS_BLOCKED. RULES.md는 kofia/nts/easylaw를 "열림"으로 기록하고 있으나 이번 세션에서는 재현되지 않았다 — 세션별 프록시 허용 목록 차이로 추정.
  추가 사실확인: WebSearch로 확인한 여러 비공식 출처가 "2026년 조세특례제한법 개정으로 ISA 한도가 연 4천만원(비과세 500만/1000만원)으로 상향, 2026-01-01 시행"이라고 주장하는 반면, 다른 자료는 기존 수치(연 2천만원, 비과세 200만/400만원)를 그대로 쓴다. 두 수치가 충돌하고 1차 출처로 검증하지 못했으므로 본문에는 어느 쪽 수치도 확정값으로 쓰지 않았다 — 표는 "확인 필요"로 비워둠.
  제목 14자·금지어 없음·조사 없음(절차형 제목으로 조정: "한도" 표에 실제 값이 없는 상태이므로 RULES.md "비교/한도형 제목은 표가 있어야 하고, 없으면 절차형으로 바꾼다" 원칙에 따라 "확인하는 법"으로 작성).
  슬러그 영문 소문자+하이픈 3단어. FAQ 6개와 JSON-LD 1:1 일치. @id를 티스토리 entry 패턴으로 지정.
  이미지 없음 — human-assisted/capture 유형이라 공식 자료 화면 캡처 이미지도 사람이 함께 준비해야 함(og:image 겸용 권장).
  캡처 필요 항목: (1) 유형별 연간 납입한도·계좌 총한도·비과세 한도 표의 실제 값, (2) 캡처한 공식 페이지의 URL과 기준일, (3) 가능하면 화면 캡처 이미지 1장.
---

<p>ISA 계좌 한도는 최근 세제 개편 관련 논의로 자료마다 서로 다른 수치가 돌고 있어, 지금 시점의 정확한 한도는 반드시 공식 출처로 직접 확인해야 합니다. 이 글은 어떤 기관에서 무엇을 확인해야 하는지 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>ISA 계좌 납입한도·비과세 한도는 <mark>제도 개편 시점에 따라 수치가 바뀔 수 있어</mark> 블로그 글마다 다르게 안내되는 경우가 많습니다.</li>
    <li>정확한 현재 한도는 국세청·금융위원회·금융투자협회 등 <b>공식 자료</b>로 확인해야 합니다.</li>
    <li>가입 유형(일반형·서민형·농어민형 등)에 따라 조건과 혜택이 다르므로, 본인이 어떤 유형에 해당하는지부터 확인해야 합니다.</li>
    <li>의무 가입기간을 채우지 못하고 중도 해지하면 세제 혜택을 받지 못할 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ISA 계좌란 무엇인가요</li>
  <li>ISA 계좌 한도는 왜 지금 다시 확인해야 하나요</li>
  <li>ISA 계좌 유형별로 무엇이 다른가요</li>
  <li>ISA 계좌 한도는 어디서 확인하나요</li>
  <li>ISA 계좌 유형별 한도 (확인 중)</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ISA 계좌란 무엇인가요</h2>

<p>ISA(개인종합자산관리계좌)는 예금, 펀드, ETF 등 여러 금융상품을 <b>하나의 계좌</b>에 담아 운용하고, 만기 시 발생한 손익을 통산해 세금 혜택을 받을 수 있는 절세 계좌입니다.</p>

<p>2016년에 도입된 이후 지금까지 개인 투자자의 대표적인 절세 수단 중 하나로 꼽힙니다. <mark>계좌 안에서 발생한 이익과 손실을 합쳐 계산한다는 점</mark>이 일반 위탁계좌와 가장 큰 차이입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ISA 계좌 한도는 왜 지금 다시 확인해야 하나요</h2>

<p>ISA 계좌의 연간 납입한도, 계좌 총한도, 비과세 한도는 세법 개정에 따라 조정될 수 있는 수치입니다. <mark>같은 검색어로 찾은 글이라도 작성 시점에 따라 서로 다른 한도를 안내하고 있을 수 있습니다.</mark></p>

<div style="background:#fff8e6;border-left:4px solid #e0a800;padding:14px 18px;margin:20px 0;">
  <b>확인이 필요한 이유</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>납입한도·비과세 한도는 조세특례제한법 등 관련 법 개정 시 바뀔 수 있습니다.</li>
    <li>오래된 글이 개정 전 수치를 그대로 싣고 있는 경우가 있습니다.</li>
    <li>반대로 아직 시행되지 않은 개편안을 이미 적용된 것처럼 쓰는 글도 있을 수 있습니다.</li>
  </ul>
</div>

<p>그래서 이 글은 특정 숫자를 단정해 알려주는 대신, <b>어디서 최신 수치를 직접 확인할 수 있는지</b>를 안내하는 데 집중했습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ISA 계좌 유형별로 무엇이 다른가요</h2>

<p>ISA는 가입자의 소득 수준이나 조건에 따라 <b>일반형, 서민형, 농어민형</b> 등 여러 유형으로 나뉘어 운영되어 왔습니다. 유형마다 비과세 한도와 가입 조건이 다르게 적용됩니다.</p>

<ul style="line-height:1.9;">
  <li>일반형: 별도 소득 조건 없이 가입 가능한 기본 유형입니다.</li>
  <li>서민형: 총급여나 종합소득금액이 일정 기준 이하인 경우 가입할 수 있으며, 비과세 혜택이 더 큽니다.</li>
  <li>농어민형: 농어업인을 대상으로 한 유형입니다.</li>
</ul>

<p>본인이 어떤 유형에 해당하는지, 그리고 각 유형의 정확한 소득 기준은 가입하려는 금융회사나 국세청 안내에서 확인하는 것이 정확합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ISA 계좌 한도는 어디서 확인하나요</h2>

<p>정확한 한도는 아래 공식 경로에서 직접 확인하는 것이 가장 안전합니다.</p>

<ol style="line-height:1.9;">
  <li><b>국세청</b> 홈페이지 또는 홈택스 안내 자료에서 ISA 관련 세제 안내를 확인합니다.</li>
  <li><b>금융위원회</b> 보도자료·정책문답에서 제도 개편 여부와 시행일을 확인합니다.</li>
  <li><b>금융투자협회</b> ISA 비교공시(다모아) 페이지에서 상품별 안내를 확인합니다.</li>
  <li>실제 가입할 <b>증권사·은행 앱</b>의 ISA 상품 안내 화면에서 현재 적용되는 한도를 확인합니다. 금융회사는 법 개정 즉시 반영하는 경우가 많아 실무적으로 가장 빠르게 최신 수치를 볼 수 있습니다.</li>
</ol>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>확인할 때 함께 메모해 둘 것</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>확인한 페이지의 <b>기준일 또는 시행일</b></li>
    <li>본인이 해당하는 <b>가입 유형</b></li>
    <li>연간 납입한도 / 계좌 총한도 / 비과세 한도 <b>세 가지 숫자를 각각 따로</b> 기록 (혼동하기 쉬운 항목입니다)</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ISA 계좌 유형별 한도 (확인 중)</h2>

<p>아래 표는 유형별 한도를 정리하는 틀입니다. 공식 출처로 확인되는 대로 실제 수치를 채울 예정입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">유형</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">연간 납입한도</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">계좌 총한도</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">비과세 한도</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">일반형</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">서민형</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">농어민형</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">확인 필요</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">위 표는 1차 출처(국세청·금융위원회·금융투자협회) 원문을 캡처해 채운 뒤에만 발행합니다. 캡처 전에는 발행하지 않습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>ISA 한도는 지금 이 순간에도 바뀔 수 있는 수치이므로 반드시 공식 출처로 확인해야 합니다.</li>
    <li>본인의 가입 유형(일반형/서민형/농어민형)에 따라 한도와 비과세 혜택이 다릅니다.</li>
    <li>국세청, 금융위원회, 금융투자협회, 가입 금융회사 앱 순으로 확인하면 가장 정확합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ISA 계좌란 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">예금, 펀드, ETF 등 여러 금융상품을 한 계좌에 담아 운용하고 손익을 통산해 세금 혜택을 받을 수 있는 절세 계좌입니다. 2016년에 도입됐습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ISA 계좌에는 어떤 유형이 있나요</summary>
  <p style="margin:10px 0 0 0;">소득 수준이나 조건에 따라 일반형, 서민형, 농어민형 등으로 나뉘며 유형마다 비과세 한도와 가입 조건이 다릅니다. 본인이 해당하는 유형은 가입 금융회사나 국세청 안내에서 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ISA 계좌 납입한도는 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">연간 납입한도와 계좌 총한도가 정해져 있지만 제도 개편에 따라 수치가 달라질 수 있어 이 글에서 단정하지 않았습니다. 국세청, 금융위원회, 금융투자협회의 최신 공식 자료로 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비과세 한도를 넘으면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">비과세 한도를 넘는 이익에는 일반 금융소득세율보다 낮은 분리과세가 적용되는 구조입니다. 정확한 세율과 한도는 국세청 공식 자료로 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ISA 계좌를 중도 해지하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">의무 가입기간을 채우지 못하고 중도 해지하면 세제 혜택을 받지 못할 수 있습니다. 정확한 의무 가입기간은 가입 시 금융회사 안내를 확인해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ISA 한도는 어디서 확인하는 게 가장 정확한가요</summary>
  <p style="margin:10px 0 0 0;">국세청, 금융위원회, 금융투자협회 같은 공식 기관 자료가 가장 정확합니다. 실무적으로는 가입하려는 증권사·은행 앱의 ISA 상품 안내 화면이 법 개정을 가장 빠르게 반영하는 경우가 많습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li>1차 출처 캡처 대기 — 국세청 / 금융위원회 / 금융투자협회 중 확인된 페이지로 채울 예정 (sources/isa-limit-access-note.md 참고)</li>
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
      "name": "ISA 계좌란 무엇인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "예금, 펀드, ETF 등 여러 금융상품을 한 계좌에 담아 운용하고 손익을 통산해 세금 혜택을 받을 수 있는 절세 계좌입니다. 2016년에 도입됐습니다."
      }
    },
    {
      "@type": "Question",
      "name": "ISA 계좌에는 어떤 유형이 있나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "소득 수준이나 조건에 따라 일반형, 서민형, 농어민형 등으로 나뉘며 유형마다 비과세 한도와 가입 조건이 다릅니다. 본인이 해당하는 유형은 가입 금융회사나 국세청 안내에서 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "ISA 계좌 납입한도는 얼마인가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "연간 납입한도와 계좌 총한도가 정해져 있지만 제도 개편에 따라 수치가 달라질 수 있어 이 글에서 단정하지 않았습니다. 국세청, 금융위원회, 금융투자협회의 최신 공식 자료로 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "비과세 한도를 넘으면 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "비과세 한도를 넘는 이익에는 일반 금융소득세율보다 낮은 분리과세가 적용되는 구조입니다. 정확한 세율과 한도는 국세청 공식 자료로 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "ISA 계좌를 중도 해지하면 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "의무 가입기간을 채우지 못하고 중도 해지하면 세제 혜택을 받지 못할 수 있습니다. 정확한 의무 가입기간은 가입 시 금융회사 안내를 확인해야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "ISA 한도는 어디서 확인하는 게 가장 정확한가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "국세청, 금융위원회, 금융투자협회 같은 공식 기관 자료가 가장 정확합니다. 실무적으로는 가입하려는 증권사·은행 앱의 ISA 상품 안내 화면이 법 개정을 가장 빠르게 반영하는 경우가 많습니다."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ISA 계좌 한도 확인하는 법",
  "description": "ISA 계좌의 납입한도와 비과세 한도를 정확하게 확인할 수 있는 공식 출처와 절차를 정리했습니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-04",
  "dateModified": "2026-09-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/isa-limit-benefit"
  }
}
</script>
