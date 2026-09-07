---
keyword: 증권거래세 세율
title: 증권거래세 세율 2026
slug: securities-transaction-tax-rate
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 920 (PC 620 / 모바일 300)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-07 — 통과]
  WebSearch "증권거래세 세율 2026" 상위 7개:
  kbsec.com(KB증권 공지) / easylaw.go.kr(법제처, 공식) / kiwoomam.com(키움투자자산운용) /
  namu.wiki(백과) / glasswallet.com 유리지갑(소규모 블로그) / kbcapital.co.kr(KB캐피탈) /
  trendmetriclab.com(소규모 블로그)
  1) 진입 여지 — 있음. glasswallet.com·trendmetriclab.com 두 개의 소규모 개인/블로그형
     콘텐츠가 상위에 올라 있다. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색("지금 세율이 몇 %냐"). 조회·신청·계산기 실행 의도 아님.
  3) 답 완결 여부 — 아니다. 오히려 상위 글들끼리 수치가 어긋난다. 같은 glasswallet.com
     페이지가 검색 결과에 따라 제목이 "코스피·코스닥 0.20%"로도 "0.15%"로도 나온다.
     2026-01-01 인상이 최근이라 인하 시절 수치가 그대로 남은 글이 많다.
     시장별 합산 부담(증권거래세 + 농어촌특별세)을 한 표로 정리하면 정보이득이 분명하다.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  핵심 정보이득은 "코스피는 증권거래세율만 보면 안 된다"는 점이다. 코스피 매도에는
  증권거래세와 별도로 농어촌특별세가 함께 붙어서, 증권거래세율만 적은 글을 보면 실제
  부담을 크게 과소평가하게 된다. 여기에 2026-01-01 환원(금투세 폐지에 따라 인하했던
  세율을 되돌림)까지 반영한 시장별 합산 부담표와 연도별 변화 이력을 넣는다.
  ※ 표의 실제 수치는 국세청·법제처 원문 캡처 전까지 비워둔다(capture_guide 참조).
primary_source: |
  [일부 확보] 농어촌특별세법 전문(법률 제21611호, 2026.5.12. 일부개정) — 사람이 원문을
  내려받아 제공(2026-09-07). 원본 sources/act-rural-special-tax-21611.doc,
  정리 sources/act-rural-special-tax.md.
  이 조문으로 "코스피는 왜 증권거래세율만 보면 안 되는가"의 법적 근거를 확정했다:
  제3조제4호(증권거래세 납세의무자 = 농특세 납세의무자), 제4조제7호 단서(대통령령으로 정하는
  증권시장에서 0% 세율이 적용되는 경우는 비과세 대상에서 제외 → 증권거래세 0%여도 농특세 부과),
  제7조제4항(거래징수 시 함께 신고·납부).
  [미확보] 세율 숫자. 제5조 세율표가 원문에 이미지(GIF)로 삽입돼 있고 그마저 잘려 있어
  증권거래세분 농특세율(제5조제1항제5호)을 읽을 수 없다. 시장별 증권거래세율도 마찬가지다.
  easylaw.go.kr WebFetch는 EGRESS_BLOCKED(2026-09-07, 1회 시도 후 중단).
  ※ 같은 날 제공된 국세청 「원천세 > 농어촌특별세」 캡처는 원천징수분 농특세(이자·배당소득
  감면세액 ×10%, 주택자금차입금 이자세액공제 ×20%)로, 증권거래세분과 다른 조항이라 쓰지 않았다.
기준일: 미확정 — 캡처한 원문에 표시된 기준일/시행일을 그대로 기입할 것
related_correction: |
  ⚠️ 이 글을 쓰다 이미 발행된 2편(주식 매도 세금 얼마, stock-sell-tax-amount)의 오류를 발견했다.
  2편은 증권거래세를 "코스피 0.05%, 코스닥·협회장외 0.2%, 코넥스 0.1%"로 적고 있는데,
  본문 전체에서 농어촌특별세를 단 한 번도 언급하지 않는다(grep 결과 0회).
  코스피 매도에는 증권거래세와 별도로 농어촌특별세가 함께 붙으므로, 코스피 실제 부담은
  2편이 적은 것보다 크다. 100만원 매도 시 2편 계산은 500원이지만 실제 부담은 그보다 많다.
  2편이 1차 출처로 쓴 법제처 페이지가 증권거래세만 다루고 농특세를 별도 항목으로 뒀을
  가능성이 높다 — 7편에서 확인한 "법제처 요약 콘텐츠의 수치 신뢰도" 문제와 같은 계열이다.
  → 이 글의 캡처가 확보되면 정확한 합산 세율로 2편도 함께 정정해야 한다. 2편은 이미
    티스토리에 발행돼 있어 사람이 본문을 고쳐야 한다.
tags: 증권거래세, 세율, 주식매도, 증권거래세율, 농어촌특별세, 코스피세금, 코스닥세금, 주식세금, 주식초보
gate_pass: false
capture_guide: |
  왜 필요한가: 이 글의 핵심이 "시장별로 실제 얼마가 떼이는가"인데, 그 표를 채울
  증권거래세율과 농어촌특별세율을 국세청·법제처 원문으로 확인하지 못했습니다
  (easylaw.go.kr EGRESS_BLOCKED). 게다가 2026-01-01 세율 환원이 최근이라 인터넷에는
  인하 시절 수치가 그대로 남은 글이 많고, 검색 결과끼리도 0.15%와 0.20%로 어긋납니다.
  추측으로 쓰면 안 되는 자리입니다.

  더 중요한 이유: 이미 발행한 2편(주식 매도 세금 얼마)이 코스피를 0.05%로만 적고
  농어촌특별세를 빠뜨렸습니다. 이 캡처로 정확한 합산 세율을 확정하면 2편도 함께
  정정해야 합니다.

  [2026-09-07 진행] 농어촌특별세법 원문은 확보됐다(법적 구조 확정). 남은 것은 세율 숫자뿐이다.

  1순위 — 국세청 증권거래세 안내: https://www.nts.go.kr 접속 →
  상단 검색창에 "증권거래세" 입력 → 세율 안내 페이지를 열어 다음이 한 화면에 보이게 캡처:
    (1) 시장별(코스피/코스닥/코넥스/K-OTC·장외) 증권거래세율
    (2) 농어촌특별세율과 어느 시장에 붙는지
    (3) 적용 시기(예: "2026.1.1. 이후 양도분부터")

  2순위 — 법제처 찾기쉬운 생활법령정보(2편이 쓴 바로 그 페이지):
  https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1701&ccfNo=2&cciNo=3&cnpClsNo=1
  접속 → "증권거래세" 부분과 페이지 하단 "이 정보는 OOOO년 O월 O일 기준" 문구가
  같이 보이게 캡처. 여기에 농어촌특별세가 어떻게 적혀 있는지도 함께 봐주세요
  (2편 오류의 원인을 확인하는 데 필요합니다).
  ※ 1순위(국세청)와 숫자가 다르면 국세청을 따릅니다 — RULES.md「수치는 소관 부처 원문에서」.

  3순위(있으면 좋음) — 연도별 세율 변화(2021~2026). 기획재정부 세법개정 보도자료나
  증권사 공지(예: KB증권 "2026년 증권거래세율 변경 안내")에 정리돼 있습니다.
  이력표를 채우는 데 쓰되, 현행 수치는 반드시 1순위로 확정합니다.

  캡처 후: 스크린샷을 대화에 올려주시면 표를 채우고 게이트를 재판정하며, 2편 정정본도
  같이 만들어 드리겠습니다.
self_check: |
  게이트1 미확인 — monthly_search_volume 확인필요로 남김. 커밋 후 notify-repo-only.yml이
  네이버 키워드도구로 실측해 채운다(큐 참고값 1,030회는 추측해 쓰지 않았다).
  게이트2 충족 — RULES.md 게이트2 v3 기준 판정, 3개 탈락 조건 모두 미해당(serp_check 참조).
  특히 3번(답 완결)에서 상위 글들끼리 수치가 어긋나는 것을 확인해 정보이득 여지를 확인했다.
  게이트3 부분 충족(2026-09-07 대폭 보강) — 농어촌특별세법 조문을 확보해 "코스피는
  증권거래세율만 보면 안 된다"를 조문 인용으로 못박았다. 특히 제4조제7호 단서
  ("대통령령으로 정하는 증권시장에서 0% 세율이 적용되는 경우는 비과세 대상에서 제외")는
  코스피 증권거래세율이 0%였던 시기에도 농특세가 계속 떼인 이유를 설명하는 핵심 근거이고,
  경쟁 글에서 이 단서를 다루는 곳을 찾지 못했다. 다만 세율표 두 개는 여전히 비어 있어
  RULES.md「실측표 자리를 비워두면 false」에 걸린다.
  게이트4 부분 충족 — 농어촌특별세법 원문(법률 제21611호)은 1차 출처로 확보했으나,
  세율 숫자는 제5조 표가 이미지이고 잘려 있어 읽을 수 없다. 시장별 증권거래세율도 미확보.
  easylaw.go.kr WebFetch EGRESS_BLOCKED(1회 시도 후 중단). 검색 요약에 나온 숫자
  (코스피 0.05%+농특세 0.15%=0.20% 등)는 검색엔진 합성 문장이라 본문에 일절 쓰지 않았다.
  ※ 함께 받은 국세청 「원천세 > 농어촌특별세」 캡처는 원천징수분 농특세라 이 글과 무관하다.
    같은 "농어촌특별세"라도 본세가 다르다(이쪽은 감면받은 소득세, 9편은 증권거래세).
    혼동해 쓰지 않았고 sources/act-rural-special-tax.md에 그 구분을 기록했다.
  카니발라이제이션 점검 — 2편(주식 매도 세금 얼마)과 소재가 겹친다. 2편은 매도 시 내는
  세금 전반(증권거래세 + 양도소득세)이 중심이고, 이 글은 증권거래세 세율 수치 자체를
  찾는 검색 의도라 표 중심으로 차별화했다. 본문에서 2편으로 내부 링크를 건다.
  다만 겹침이 작지 않으므로, 캡처 후 2편을 정정할 때 두 글의 역할 분담을 다시 점검할 것.
  ★ 이 글을 쓰다 2편의 실제 오류를 발견해 related_correction 필드에 기록했다(농특세 누락).
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문 기관 안내 문장과 하단 참고 출처를
  전부 링크 처리. target="_blank" rel="noopener", 정부기관이라 nofollow 미부착.
  법제처 딥링크는 2편이 이미 1차 출처로 쓴 URL이라 본문에 걸었다.
  제목 12자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 4단어. FAQ 6개와 JSON-LD
  1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 하단 면책 문구 포함.
  종합 판정: 게이트3·4 미충족 → gate_pass:false. 캡처 후 재판정.
---

<p>증권거래세는 <mark>국내 주식을 팔 때 이익이 나든 손해가 나든 무조건 붙는 세금</mark>입니다. 2026년 1월 1일부터 세율이 인상됐고, 코스피는 증권거래세만 보면 실제 부담을 놓치게 됩니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>증권거래세는 <b>매도 금액 전체</b>에 붙습니다. 손해를 보고 팔아도 냅니다.</li>
    <li><mark>코스피는 증권거래세 외에 농어촌특별세가 따로 붙습니다.</mark> 증권거래세율만 적힌 표를 보면 실제 부담을 과소평가하게 됩니다.</li>
    <li>2026년 1월 1일부터 세율이 <b>인상</b>됐습니다. 금융투자소득세 도입을 전제로 내렸던 세율을 되돌린 것입니다.</li>
    <li>따로 신고할 일은 없습니다. 증권사가 매도 대금에서 <b>자동으로 떼고</b> 넘겨줍니다.</li>
  </ul>
</div>

<p style="background:#fff3cd;border:1px solid #e0a800;border-radius:6px;padding:10px 14px;font-size:14px;color:#7a5c00;">⚠️ 이 초안은 세율 수치를 국세청·법제처 원문으로 아직 확정하지 못한 상태입니다(자동화 세션의 네트워크 접근 차단). 아래 표는 사람이 원문을 캡처해 준 뒤 채워집니다 — capture_guide 참고.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>증권거래세는 어떤 세금인가요</li>
  <li>시장별 세율은 얼마인가요</li>
  <li>코스피는 왜 세율이 두 개인가요</li>
  <li>2026년에 무엇이 바뀌었나요</li>
  <li>매도 금액별로 얼마나 떼나요</li>
  <li>따로 신고해야 하나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">증권거래세는 어떤 세금인가요</h2>

<p>증권거래세는 <mark>주식을 팔 때 매도 금액에 대해 매기는 세금</mark>입니다. 이익에 매기는 세금이 아니라 거래 자체에 매기는 세금이라, <b>손실을 보고 팔아도 내야 합니다.</b></p>

<p>이 점이 양도소득세와 다릅니다. 양도소득세는 이익이 났을 때 대주주 등 일부만 내지만, 증권거래세는 국내 상장주식을 파는 모든 사람이 냅니다. 매도 시 내는 세금 전반은 따로 정리한 "주식 매도 세금 얼마" 글을 참고하세요.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">시장별 세율은 얼마인가요</h2>

<p>세율은 어느 시장에서 파는지에 따라 다릅니다. <mark>코스피는 증권거래세와 농어촌특별세를 합쳐서 봐야</mark> 실제 부담이 나옵니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">시장</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">증권거래세</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">농어촌특별세</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">합계(실제 부담)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">코스피(유가증권시장)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">코스닥</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">코넥스</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">장외(K-OTC 등)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">위 세율은 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 원문 확인 후 채웁니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">코스피는 왜 세율이 두 개인가요</h2>

<p>코스피에서 주식을 팔면 <b>증권거래세와 농어촌특별세가 함께</b> 부과되기 때문입니다. 두 세금은 근거 법이 다르지만 매도할 때 같이 떼입니다.</p>

<p>증권거래세를 내는 사람이 곧 농어촌특별세 납세의무자입니다. <a href="https://www.law.go.kr" target="_blank" rel="noopener">농어촌특별세법</a> 제3조제4호가 「증권거래세법」 제3조제1호의 증권거래세 납세의무자를 농어촌특별세 납세의무자로 정하고 있습니다.</p>

<h3 style="margin-top:28px;">증권거래세가 0%여도 농어촌특별세는 붙습니다</h3>

<p>여기가 많은 글이 놓치는 지점입니다. 농어촌특별세법 제4조는 <mark>증권거래세가 부과되지 않거나 0% 세율이 적용되면 농어촌특별세도 비과세</mark>라고 정해두었습니다. 그런데 <b>같은 조항에 단서가 붙어 있습니다.</b></p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>농어촌특별세법 제4조(비과세) 제7호</b>
  <p style="margin:8px 0 0 0;">「증권거래세법」 제6조에 따라 증권거래세가 부과되지 아니하거나 같은 법 제8조제2항에 따라 <b>영의 세율이 적용되는 경우</b>. <mark>다만, 「자본시장과 금융투자업에 관한 법률」에 따른 증권시장으로서 대통령령으로 정하는 증권시장에서 양도되는 증권의 양도가액에 대하여 영의 세율이 적용되는 경우는 제외한다.</mark></p>
</div>

<p>단서가 원칙을 뒤집습니다. 대통령령으로 정하는 증권시장에서 양도되는 경우는 <b>비과세 대상에서 제외</b>되므로, 증권거래세율이 0%로 내려가도 <mark>농어촌특별세는 그대로 부과</mark>됩니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>인터넷 정보를 볼 때 주의하세요.</b>
  <p style="margin:8px 0 0 0;">코스피 세율을 설명하면서 <b>증권거래세만 적고 농어촌특별세를 빠뜨린 글이 많습니다.</b> 특히 코스피 증권거래세율이 낮았던 시기에 쓰인 글은 "코스피는 거의 안 뗀다"는 인상을 주는데, 위 단서 때문에 실제로는 농어촌특별세가 계속 떼이고 있었습니다. 코스피는 반드시 두 세금을 합쳐서 확인하세요.</p>
</div>

<p>코스닥에는 농어촌특별세가 붙지 않습니다. 그래서 증권거래세율만 보면 코스닥이 더 높아 보이지만, 합산 부담으로 비교하면 이야기가 달라집니다.</p>

<p style="font-size:13px;color:#888;">근거: 농어촌특별세법(법률 제21611호, 2026.5.12. 일부개정) 제3조제4호·제4조제7호. 증권사가 매도 대금에서 증권거래세를 거래징수할 때 농어촌특별세도 함께 징수해 납부합니다(같은 법 제7조제4항).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">2026년에 무엇이 바뀌었나요</h2>

<p>2026년 1월 1일 이후 양도분부터 <mark>증권거래세율이 인상</mark>됐습니다. 금융투자소득세 도입을 전제로 단계적으로 내렸던 세율을, 금투세가 폐지되면서 되돌린 것입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">적용 시기</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">코스피</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">코스닥</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">2025년까지</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;"><b>2026.1.1. 이후(현행)</b></td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td></tr>
  </tbody>
</table>

<p>오래된 글에는 인하 시절 세율이 그대로 남아 있는 경우가 많습니다. <b>작성 시점이 2025년 이전인 글의 숫자는 지금 기준과 다를 수 있습니다.</b></p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">매도 금액별로 얼마나 떼나요</h2>

<p>증권거래세는 매도 금액에 세율을 곱해 계산합니다. 매수 금액이나 손익과는 무관합니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>계산 예시 자리 (캡처 후 작성)</b>
  <p style="margin:8px 0 0 0;">100만원·1,000만원·5,000만원을 코스피와 코스닥에서 각각 팔았을 때 떼이는 금액을 계산해 넣을 예정입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">따로 신고해야 하나요</h2>

<p>아닙니다. 증권사가 매도 대금을 정산할 때 <mark>자동으로 떼고 대신 납부</mark>합니다. 투자자가 따로 신고하거나 납부할 일은 없습니다.</p>

<p>실제로 얼마가 떼였는지는 증권사 앱의 거래내역이나 거래명세에서 확인할 수 있습니다. 세금 신고가 필요한 것은 양도소득세 대상일 때이고, 그 경우 <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>에서 신고합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">손해를 보고 팔아도 증권거래세를 내나요</summary>
  <p style="margin:10px 0 0 0;">네. 증권거래세는 이익이 아니라 매도 금액에 매기는 세금이라 손실이 나도 부과됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">코스피 세율이 자료마다 다르게 나오는 이유가 뭔가요</summary>
  <p style="margin:10px 0 0 0;">증권거래세만 적었는지, 농어촌특별세까지 합쳤는지에 따라 달라집니다. 코스피는 두 세금이 함께 부과되므로 합산 기준으로 봐야 실제 부담이 나옵니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">주식을 살 때도 증권거래세를 내나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 증권거래세는 팔 때만 부과됩니다. 매수할 때는 증권사 위탁수수료만 발생합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">2026년에 세율이 왜 올랐나요</summary>
  <p style="margin:10px 0 0 0;">금융투자소득세 도입을 전제로 단계적으로 내렸던 세율인데, 금투세가 폐지되면서 인하분을 되돌린 것입니다. 2026년 1월 1일 이후 양도분부터 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식에도 증권거래세가 붙나요</summary>
  <p style="margin:10px 0 0 0;">우리나라 증권거래세는 붙지 않습니다. 대신 해외주식은 양도차익에 양도소득세가 부과되고, 현지 거래 관련 비용이 별도로 발생할 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증권거래세를 따로 신고해야 하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 증권사가 매도 대금에서 자동으로 떼어 대신 납부하므로 투자자가 신고할 일은 없습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> — 증권거래세 세율 (원문 확인 예정)</li>
    <li><a href="https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1701&amp;ccfNo=2&amp;cciNo=3&amp;cnpClsNo=1" target="_blank" rel="noopener">법제처 찾기쉬운 생활법령정보</a> — 양도소득세·증권거래세 및 배당소득세</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> — 양도소득세 신고</li>
    <li>기준일: 미확정 — 원문 캡처 후 시행일 기준으로 확정</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 책임은 본인에게 있습니다. 세율은 세법 개정으로 바뀔 수 있으므로 거래 전 국세청 최신 안내를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "증권거래세 세율 2026",
  "description": "증권거래세 시장별 세율과 코스피에 함께 붙는 농어촌특별세, 2026년 1월 인상 내용을 정리합니다. (세율 수치는 원문 캡처 후 확정)",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-07",
  "dateModified": "2026-09-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/securities-transaction-tax-rate"
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
      "name": "손해를 보고 팔아도 증권거래세를 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 증권거래세는 이익이 아니라 매도 금액에 매기는 세금이라 손실이 나도 부과됩니다." }
    },
    {
      "@type": "Question",
      "name": "코스피 세율이 자료마다 다르게 나오는 이유가 뭔가요",
      "acceptedAnswer": { "@type": "Answer", "text": "증권거래세만 적었는지, 농어촌특별세까지 합쳤는지에 따라 달라집니다. 코스피는 두 세금이 함께 부과되므로 합산 기준으로 봐야 실제 부담이 나옵니다." }
    },
    {
      "@type": "Question",
      "name": "주식을 살 때도 증권거래세를 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 증권거래세는 팔 때만 부과됩니다. 매수할 때는 증권사 위탁수수료만 발생합니다." }
    },
    {
      "@type": "Question",
      "name": "2026년에 세율이 왜 올랐나요",
      "acceptedAnswer": { "@type": "Answer", "text": "금융투자소득세 도입을 전제로 단계적으로 내렸던 세율인데, 금투세가 폐지되면서 인하분을 되돌린 것입니다. 2026년 1월 1일 이후 양도분부터 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "해외주식에도 증권거래세가 붙나요",
      "acceptedAnswer": { "@type": "Answer", "text": "우리나라 증권거래세는 붙지 않습니다. 대신 해외주식은 양도차익에 양도소득세가 부과되고, 현지 거래 관련 비용이 별도로 발생할 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "증권거래세를 따로 신고해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 증권사가 매도 대금에서 자동으로 떼어 대신 납부하므로 투자자가 신고할 일은 없습니다." }
    }
  ]
}
</script>
