---
keyword: 커버드콜 ETF 세금
title: 커버드콜 ETF 세금 국내형과 해외형 차이
slug: covered-call-etf-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 110 (PC 40 / 모바일 70, 2026-09-22 실측)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요, 근소하게 충족)
serp_check: |
  [게이트2 v3 판정 2026-09-22 — 통과]
  WebSearch "커버드콜 ETF 세금 분배금 과세 옵션프리미엄 배당소득세" +
  "해외지수 커버드콜 ETF 옵션프리미엄 과세 국내주식형 차이" 상위 종합:
  news.bizwatch.co.kr(언론) / v.daum.net(언론 재배포, 2건) /
  investpension.miraeasset.com(미래에셋증권 공식 매거진) /
  hankyung.com(언론, 2건) / samsungfund.com(삼성자산운용 Kodex 공지, 공식) /
  sisajournal-e.com(언론) / m.joseilbo.com(언론) /
  cashflowinvestnote.com(개인 블로그) / keyzard.cc(개인·소규모) /
  eorim.com(개인·소규모, ETF 비교 콘텐츠)
  1) 진입 여지 — 있음. cashflowinvestnote.com·keyzard.cc·eorim.com 등
     개인·소규모 콘텐츠가 상위권에 섞여 있어 SERP가 잠겨 있지 않다.
     탈락조건1 미해당.
  2) 검색 의도 — "왜 세금이 다르게 붙는지, 얼마나 떼는지" 정보 탐색형이다.
     조회·계산기 실행으로 대체되는 의도가 아니다. 탈락조건2 미해당.
  3) 답 완결 여부 — 부분적. 언론 기사와 운용사 공지가 "국내주식형은
     옵션프리미엄 비과세, 해외지수형은 전액 과세"라는 핵심 규칙 자체는
     이미 설명한다. 다만 실제 분배금을 놓고 과세대상 금액을 직접
     계산해 보여주거나, 두 유형의 세후 수령액을 나란히 비교한 표,
     분배금 중 과세 비중을 확인하는 방법까지 한 번에 정리한 글은
     상위에서 찾지 못했다. 정보이득 여지 있음(부분 통과로 기록).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과(3번은 부분 통과).
unique_asset: |
  (a) 국내주식형과 해외지수형 커버드콜 ETF의 과세 대상·비과세 근거·
      적용 세율을 나란히 정리한 비교표.
  (b) 분배금 100원을 가정한 계산 예시로 국내형(배당수익 40원+옵션
      프리미엄 60원 가정 시 40원만 과세)과 해외형(전액 과세)의 실제
      원천징수세액과 세후 수령액을 직접 비교.
  (c) "배당수익이 먼저 분배된 것으로 간주"되는 분배 순서 규칙 때문에
      국내형도 특정 달에는 분배금 전액이 과세될 수 있다는, 상위 글이
      스치듯 언급만 하는 예외를 구체적으로 짚었다.
  (d) 분배금 지급명세서·운용사 공시에서 과세/비과세 비중을 직접
      확인하는 절차.
  ★ (b)의 "40원/60원" 구성비는 실제 특정 상품의 확정 수치가 아니라
  구조를 보여주기 위한 가정값임을 본문에 명시했다. 개별 ETF의 실제
  비중은 그 상품의 분배금 공시에서 확인하도록 안내했다.
primary_source: |
  1차 시도: 법제처/국가법령정보센터(law.go.kr)에서 소득세법 시행령
  제26조의2제4항(국내 장내파생상품 매매차익 비과세) 원문 WebFetch
  1회 시도 → EGRESS_BLOCKED(2026-09-22). 세션 전면 차단 여부를 확인
  하기 위해 무관 도메인(samsungfund.com, hankyung.com, google.com)에도
  WebFetch를 추가로 시도했으나 전부 동일하게 EGRESS_BLOCKED로 막혀
  이번 세션 전체가 아웃바운드 차단 상태임을 확인했다. RULES.md
  「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 판단.
  이 항목은 세율·공제한도·과세표준 구간처럼 구간값이 아니라 "과세
  대상 여부를 가르는 법 조항 번호 + 이분법적 규칙"이라 교차검증
  대상으로 판단했다. 서로 무관한 독립 출처 6곳 이상(뉴스워치·한국경제
  2건·조세일보·시사저널e 등 언론사 4곳 이상 + 삼성자산운용 Kodex
  공식 공지 + 미래에셋증권 공식 매거진, 총 6곳)이 다음 핵심 사실에서
  충돌 없이 일치했다.
  ① 국내주식형 커버드콜 ETF의 옵션 프리미엄 수익은 소득세법 시행령
  제26조의2제4항의 국내 장내파생상품 매매차익 비과세 규정에 따라
  비과세다, ② 같은 ETF의 배당·이자 수익 부분만 15.4% 배당소득세가
  과세된다, ③ 분배 시에는 과세 대상인 배당수익이 비과세 대상인 옵션
  프리미엄보다 먼저 분배된 것으로 간주되어, 기초자산 배당수익이 목표
  분배율을 넘는 달에는 분배금 전액이 과세될 수도 있다, ④ 해외 지수를
  기초자산으로 하는 커버드콜 ETF는 이 비과세 규정의 적용 대상이 아니라
  분배금과 매매차익 모두 15.4% 배당소득세가 적용된다.
  15.4%라는 세율 자체는 새로 확정한 숫자가 아니라 4편(배당소득세,
  dividend-income-tax)에서 이미 원문 기준으로 확정한 값을 그대로
  재사용했다.
기준일: 2026-09-22 (WebSearch 교차검증 확인일 기준)
tags: 커버드콜ETF, ETF세금, 옵션프리미엄, 배당소득세, 국내상장ETF, 해외지수ETF, 월배당, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-22). 게이트1은 이번 세션 check-keywords.yml
  로 직접 실측(110회, 세부·제도 기준 100 이상에 근소하게 충족). 게이트2는
  RULES.md v3 기준으로 정식 판정(부분 통과 항목은 self_check에 투명 공개).
  게이트3은 국내형·해외형 비교표 + 분배금 100원 가정 계산 예시 + 과세
  비중 확인법으로 충족. 게이트4는 law.go.kr 접근이 EGRESS_BLOCKED됐고
  대조군(samsungfund.com·hankyung.com·google.com)도 동일하게 막혀 세션
  전면 차단을 확인, 이후 RULES.md 기준에 따라 독립 출처 6곳 교차검증으로
  진행했다. 세율(15.4%) 자체는 새 숫자가 아니라 4편에서 이미 확정한 값을
  재사용했고, 이 글에서 새로 제시하는 것은 법 조항 번호와 과세대상
  구분 규칙이라 세율·한도 구간형 숫자보다 교차검증에 적합하다고 판단했다.
capture_guide: |
  (해당 없음 — 이번 편은 교차검증으로 게이트4를 충족해 캡처가 필수는
  아니다. 다만 사람이 최종 검토 시 아래 원문을 직접 열어 대조하면
  더 안전하다.)
  1순위 — 국가법령정보센터(https://www.law.go.kr)에서 "소득세법
  시행령"을 검색해 제26조의2 제4항(국내 장내파생상품 매매차익
  비과세) 조문 원문 캡처.
  2순위 — 보유 중인 커버드콜 ETF가 있다면 운용사 홈페이지의 분배금
  공시(예: 삼성자산운용 Kodex 공지 페이지, https://www.samsungfund.com)
  에서 해당 월 분배금의 과세/비과세 구성 비율 캡처.
self_check: |
  [2026-09-22 판정 — gate_pass:true]
  게이트1 충족 — 이번 세션 check-keywords.yml 실측 110회(세부·제도
  기준 100 이상, 근소하게 충족했다는 한계를 투명하게 기록).
  게이트2 충족 — RULES.md v3 기준 3개 탈락 조건 모두 미해당(3번은
  부분 통과, serp_check 참조).
  게이트3 충족 — 국내형·해외형 비교표 + 분배금 100원 가정 계산 예시
  + 분배 순서 규칙에 따른 예외 설명 + 과세 비중 확인 절차.
  게이트4 충족(교차검증) — law.go.kr 1회 시도 EGRESS_BLOCKED, 대조군
  3곳(samsungfund.com·hankyung.com·google.com)도 동일하게 막혀 세션
  전면 차단으로 판단. 언론사 4곳 이상 + 자산운용사 공식 공지 +
  증권사 공식 매거진, 총 6곳이 핵심 사실(법 조항 번호, 과세대상 구분,
  분배 순서 규칙)에서 충돌 없이 일치.
  카니벌라이제이션 점검 — 63편(월배당 ETF, monthly-dividend-etf-basics)이
  "커버드콜"을 2회 언급하지만 세금 처리는 "4편·23편이 다루는 영역이라
  새로 설명하지 않고 링크로 위임"이라고 명시적으로 밝히고 있어(63편
  본문 직접 확인) 과세 구조를 깊게 다루지 않는다. 4편(배당소득세,
  dividend-income-tax)·23편(국내상장 해외ETF 세금,
  domestic-listed-overseas-etf-tax) 본문에서 "커버드콜"·"옵션
  프리미엄" 검색 결과 0건(grep 확인). 1~72편 keyword 전체 확인 결과
  겹치는 편 없음.
  제목 "커버드콜 ETF 세금 국내형과 해외형 차이" 22자·금지어 없음·
  "~이나/~부터~까지/~인가요/~일까요" 없음. 슬러그 영문 소문자+하이픈
  4단어(covered-call-etf-tax).
  종목·상품 추천 표현 없음(특정 ETF 종목명을 언급하지 않고 유형으로만
  설명), 단정 표현("반드시"·"무조건"·"확실히"·"보장") 없음.
  FAQ 5개와 JSON-LD 1:1 일치.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문(YAML 제외)에서
  "—"(em대시) 0개 확인. "다만" 0회(전환어를 "단,"·"여기서 핵심은"·
  문장 구조 전환으로 대체). 본문 `<mark>` 총 3개(3~5개 기준 충족).
  FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을 "💡 세금
  전에 먼저 볼 3가지"로, 박스 색을 인디고 계열(#eef0ff/#4a5fc1)로
  최근 편들의 주황(#fef3e2/#d98324, #fdf3e3/#c98a1f)·초록
  (#eafaf3/#1e8a6e, #eafaf1/#2e8b57)·보라(#f1eefc/#6a4fb6)·청록
  (#e8f7f5/#1f9e8a)과 다르게 바꿨다. 면책 문구도 이전 편들과 다른
  문장으로 새로 썼다. 목차 제외 본문 H2 5개 중 서술형 3개("국내주식형
  커버드콜 ETF는 이렇게 과세됩니다", "분배금 100원으로 보는 세후
  수령액 차이", "분배금 과세 비중 확인하는 법"), 질문형 2개("커버드콜
  ETF는 왜 세금이 다르게 붙나요", "해외지수형은 왜 전액 과세되나요")로
  "~나요" 편중 없음(5개 중 2개, 40%). 헤지 문구("~것으로 알려져
  있다" 류)는 사용하지 않았고, 확정된 사실은 단정형 어미로 서술했다.
  종합 판정: 4개 게이트 전부 충족, gate_pass:true. 단, 게이트1
  검색량(110회)이 세부·제도 기준선(100회)에 근소하게 걸쳐 있다는 점은
  발행 전 사람이 한 번 더 감안할 부분으로 남긴다.
---

<p><mark>커버드콜 ETF는 분배금이 어디서 나왔는지에 따라 세금이 완전히 달라집니다.</mark> 국내 주식을 기초자산으로 하면 분배금 일부가 비과세지만, 해외 지수를 기초자산으로 하면 같은 구조의 상품이라도 전액 과세됩니다. 이 글은 그 차이가 생기는 이유와 실제 세후 수령액 차이를 계산 예시로 정리했습니다.</p>

<div style="background:#eef0ff;border:2px solid #4a5fc1;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#333d8f;font-size:18px;">💡 세금 전에 먼저 볼 3가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>국내주식형은 <b>옵션 프리미엄이 비과세</b>, 배당수익만 15.4% 과세됩니다.</li>
    <li>해외지수형은 <mark>분배금과 매매차익 전체에 15.4%</mark>가 붙습니다.</li>
    <li>같은 국내형이라도 특정 달엔 분배금 전액이 과세될 수 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>커버드콜 ETF는 왜 세금이 다르게 붙나요</li>
  <li>국내주식형 커버드콜 ETF는 이렇게 과세됩니다</li>
  <li>해외지수형은 왜 전액 과세되나요</li>
  <li>분배금 100원으로 보는 세후 수령액 차이</li>
  <li>분배금 과세 비중 확인하는 법</li>
  <li>자주 나오는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">커버드콜 ETF는 왜 세금이 다르게 붙나요</h2>

<p>커버드콜 ETF는 기초자산을 보유하면서 동시에 콜옵션을 매도해 옵션 프리미엄을 함께 받는 구조입니다. 분배금의 재원은 두 가지, 기초자산에서 나오는 배당·이자 수익과 콜옵션 매도로 받는 옵션 프리미엄입니다.</p>

<p>세법은 이 두 재원을 다르게 취급합니다. 배당·이자 수익은 어떤 ETF든 배당소득세 과세 대상이지만, 국내 주식을 기초자산으로 하는 상품의 옵션 프리미엄은 <b>국내 장내파생상품 매매차익 비과세 규정</b>의 적용을 받습니다.</p>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">국내주식형 커버드콜 ETF는 이렇게 과세됩니다</h2>

<p>국내 주식을 기초자산으로 하는 커버드콜 ETF는 분배금 중 <mark>옵션 프리미엄 부분이 소득세법 시행령 제26조의2제4항에 따라 비과세</mark>됩니다. 이 조항은 국내 장내파생상품 매매차익 전반에 적용되는 비과세 규정으로, 커버드콜 ETF만을 위한 특례는 아닙니다.</p>

<p>배당·이자 수익 부분은 <a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax">4편에서 정리한</a> 배당소득세 원천징수세율 15.4%(소득세 14%+지방소득세 1.4%)가 그대로 적용됩니다. 결국 국내형은 분배금 전액이 아니라 배당·이자 부분에만 세금이 붙는 구조입니다.</p>

<p>단, 분배 순서 규칙 때문에 예외가 생깁니다. 분배 시에는 과세 대상인 배당수익이 비과세 대상인 옵션 프리미엄보다 <b>먼저 분배된 것으로 간주</b>됩니다. 그래서 기초자산의 배당수익이 그달의 목표 분배율을 넘어서면, 옵션 프리미엄을 더 벌었더라도 그달 분배금 전액이 과세될 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>배당수익이 목표 분배율보다 적은 달: 배당수익만 과세, 나머지는 비과세</li>
  <li>배당수익이 목표 분배율을 넘는 달: 분배금 전액 과세 가능</li>
</ul>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">해외지수형은 왜 전액 과세되나요</h2>

<p>앞서 설명한 비과세 규정은 <b>국내 장내파생상품</b>에만 적용됩니다. 미국 대형주 지수나 나스닥100 같은 해외 지수를 기초자산으로 하는 커버드콜 ETF는 이 규정의 적용 대상이 아닙니다.</p>

<p>그래서 해외지수형 커버드콜 ETF는 분배금과 매매차익 모두 배당소득세 15.4%가 적용됩니다. 매매차익은 보유기간 과세 방식이 적용되어 실제 매매차익과 과표기준가 증가분 중 작은 금액을 기준으로 세금을 매기지만, 옵션 프리미엄이라고 해서 별도로 빠지는 부분은 없습니다.</p>

<p>여기서 핵심은 두 상품이 "커버드콜"이라는 같은 이름을 쓰더라도, 기초자산이 국내인지 해외인지에 따라 세금 구조 자체가 다르다는 점입니다. 상품명만 보고 세금이 같을 거라 짐작하면 안 됩니다.</p>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">분배금 100원으로 보는 세후 수령액 차이</h2>

<p>두 유형의 차이를 가상의 숫자로 직접 계산해 보겠습니다. 아래 표의 "배당 40원 + 옵션 프리미엄 60원"은 실제 특정 상품의 확정 수치가 아니라, 구조를 보여주기 위한 가정값입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">분배금</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">과세대상 금액</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">원천징수세액(15.4%)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">세후 수령액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">국내주식형(가정)</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">100원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">40원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">6.16원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">93.84원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">해외지수형</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">100원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">100원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">15.4원</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">84.6원</td>
    </tr>
  </tbody>
</table>

<p>같은 100원을 분배해도 국내형은 93.84원, 해외형은 84.6원을 받습니다. 좌당 9.24원, 분배금 대비로는 9.24%p 차이입니다. 배당수익 비중이 이 가정보다 크거나 작으면 국내형의 실제 세후 수령액도 달라집니다.</p>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">분배금 과세 비중 확인하는 법</h2>

<p>내가 보유한 ETF의 실제 배당수익·옵션 프리미엄 비중은 이 글의 가정값과 다를 수 있습니다. 정확한 비중은 아래 두 곳에서 확인할 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>가입한 증권사 MTS의 분배내역 조회 화면에서 해당 월 분배금의 과세·비과세 구분을 확인합니다.</li>
  <li>운용사 홈페이지의 분배금 안내 공지나 <a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시서비스</a>에서 펀드별 분배 내역을 조회합니다.</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>월별로 과세 비중이 바뀔 수 있습니다</b>
  <p style="margin:8px 0 0 0;">국내형이라고 항상 일부만 과세되는 건 아닙니다. 배당수익이 몰리는 달에는 전액 과세될 수 있으므로, 매달 지급명세서를 확인하는 습관이 세후 수익률을 가늠하는 데 도움이 됩니다.</p>
</div>

<div style="background:#eef0ff;border:2px solid #4a5fc1;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#333d8f;font-size:18px;">💡 다시 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>국내형은 옵션 프리미엄 비과세, 해외형은 전액 과세라는 구조부터 구분합니다.</li>
    <li>같은 국내형도 배당수익이 많은 달엔 전액 과세될 수 있습니다.</li>
    <li>실제 비중은 가정이 아니라 매월 분배내역 공시로 직접 확인합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a5fc1;padding-left:12px;margin-top:36px;">자주 나오는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">커버드콜 ETF는 다른 ETF보다 세금이 항상 적은가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 국내 주식을 기초자산으로 하는 커버드콜 ETF만 옵션 프리미엄 비과세 혜택이 있고, 해외 지수를 기초자산으로 하면 분배금과 매매차익 모두 15.4%가 과세됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">옵션 프리미엄이 비과세인 법적 근거는 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">소득세법 시행령 제26조의2제4항의 국내 장내파생상품 매매차익 비과세 규정입니다. 커버드콜 ETF 전용 특례가 아니라 국내 장내파생상품 전반에 적용되는 규정입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배당수익이 먼저 분배된 것으로 간주된다는 게 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">분배금을 지급할 때 과세 대상인 배당수익부터 채운다고 보는 규칙입니다. 그달의 기초자산 배당수익이 목표 분배율을 넘으면, 옵션 프리미엄 수익이 있어도 분배금 전액이 과세될 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외지수형 커버드콜 ETF의 매매차익도 과세되나요</summary>
  <p style="margin:10px 0 0 0;">과세됩니다. 분배금뿐 아니라 매매차익도 15.4% 배당소득세가 적용되며, 보유기간 과세 방식으로 실제 매매차익과 과표기준가 증가분 중 작은 금액을 기준으로 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">내가 가진 ETF의 과세·비과세 비중은 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">가입한 증권사 MTS의 분배내역 조회 화면이나 운용사 홈페이지의 분배금 안내 공지, 금융투자협회 전자공시서비스에서 해당 월 분배금의 과세 구분을 확인할 수 있습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> - 배당소득세 일반 원천징수 규정 소관 부처</li>
    <li><a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시서비스</a> - 펀드·ETF 분배 내역 조회</li>
    <li><a href="https://sensitiveboss3.tistory.com/entry/dividend-income-tax">배당소득세 얼마 떼나 (관련 편)</a></li>
  </ul>
  기준일: 2026년 9월 기준. 개별 ETF의 옵션 프리미엄·배당수익 비중과 세율은
  상품·월별로 달라질 수 있으니 운용사 분배 공시에서 다시 확인하시기
  바랍니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 커버드콜 ETF의 과세 구조를 설명하는 정보성 글이며, 특정 종목이나
상품의 매수를 권하지 않습니다. 투자 여부와 그 결과에 대한 책임은 투자자
본인에게 있습니다. 세율과 법 조항은 개정될 수 있으니 투자 전 원출처에서
최신 내용을 확인해 주세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "커버드콜 ETF 세금 국내형과 해외형 차이",
  "description": "국내주식형 커버드콜 ETF의 옵션 프리미엄 비과세 근거와 해외지수형의 전액 과세 구조를 비교하고, 분배금 100원 가정 계산 예시로 실제 세후 수령액 차이를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-22",
  "dateModified": "2026-09-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/covered-call-etf-tax"
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
      "name": "커버드콜 ETF는 다른 ETF보다 세금이 항상 적은가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 국내 주식을 기초자산으로 하는 커버드콜 ETF만 옵션 프리미엄 비과세 혜택이 있고, 해외 지수를 기초자산으로 하면 분배금과 매매차익 모두 15.4%가 과세됩니다." }
    },
    {
      "@type": "Question",
      "name": "옵션 프리미엄이 비과세인 법적 근거는 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "소득세법 시행령 제26조의2제4항의 국내 장내파생상품 매매차익 비과세 규정입니다. 커버드콜 ETF 전용 특례가 아니라 국내 장내파생상품 전반에 적용되는 규정입니다." }
    },
    {
      "@type": "Question",
      "name": "배당수익이 먼저 분배된 것으로 간주된다는 게 무슨 뜻인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "분배금을 지급할 때 과세 대상인 배당수익부터 채운다고 보는 규칙입니다. 그달의 기초자산 배당수익이 목표 분배율을 넘으면, 옵션 프리미엄 수익이 있어도 분배금 전액이 과세될 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "해외지수형 커버드콜 ETF의 매매차익도 과세되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "과세됩니다. 분배금뿐 아니라 매매차익도 15.4% 배당소득세가 적용되며, 보유기간 과세 방식으로 실제 매매차익과 과표기준가 증가분 중 작은 금액을 기준으로 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "내가 가진 ETF의 과세·비과세 비중은 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "가입한 증권사 MTS의 분배내역 조회 화면이나 운용사 홈페이지의 분배금 안내 공지, 금융투자협회 전자공시서비스에서 해당 월 분배금의 과세 구분을 확인할 수 있습니다." }
    }
  ]
}
</script>
