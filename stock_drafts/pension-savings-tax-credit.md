---
keyword: 연금저축 세액공제
title: 연금저축 세액공제 얼마 돌려받나
slug: pension-savings-tax-credit
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 3180 (PC 800 / 모바일 2380) / 2026-10-15 실측 IRP 세액공제 5,020, 연금저축 세액공제 한도 4,550
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-07 — 통과]
  WebSearch "연금저축 세액공제" 상위 7개:
  easylaw.go.kr(법제처, 공식) / myasset.com(증권사 안내) / banksalad.com(핀테크 콘텐츠) /
  samsungpop.com(증권사 안내) / nts.go.kr(국세청, 공식) / tossbank.com ×2(핀테크 콘텐츠)
  1) 진입 여지 — 있음. 뱅크샐러드·토스뱅크 등 대형 은행이 아닌 핀테크 서비스의 콘텐츠
     페이지가 다수 상위에 진입해 있어 SERP가 잠겨 있지 않다.
  2) 검색 의도 — 정보 탐색("한도가 얼마고 얼마나 돌려받나"). 조회·신청·계산기 실행이
     주 의도가 아니다.
  3) 답 완결 여부 — 상위 3개(법제처·증권사·핀테크)가 소득 구간별 실제 환급액 계산
     예시까지 정확히 제공하지 않는다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과. 상세는 sources/pension-savings-tax-credit-access-note.md
unique_asset: |
  [완성 2026-09-07 — 국세청 원문 캡처 반영]
  (a) 소득 구간별 실제 환급액 계산표(600만원/900만원 × 16.5%/13.2%)와 IRP 합산 한도의
      포함 관계. 연금저축 계좌 하나로는 900만원을 다 못 쓴다는 점까지 명시.
  (b) 15% vs 16.5% 혼란 해소 — 국세청 원문은 15%/12%이고 인터넷은 16.5%/13.2%인데,
      충돌이 아니라 지방소득세 포함 여부의 차이(15%×1.1)다. 상위 글들이 16.5%만 쓰고
      근거를 설명하지 않는 자리라 이 구분 자체가 정보이득이다.
  (c) 한도는 두 소득 구간이 600만원(900만원)으로 동일하고 공제율만 갈린다. 예전엔
      소득별로 한도도 달라서, 오래된 글과 갈리는 지점이다.
  (d) ISA 만기자금을 연금계좌로 옮기면 전환금액의 10%(최대 300만원)만큼 한도가 확대된다.
  (e) 수치 없이도 성립하는 두 가지. 상위 경쟁 글이 "최대 148만원 환급"을 앞세우는
      자리에서 이쪽이 실질적 차별점이다.
      · 결정세액 한계: 세액공제는 현금 지급이 아니라 낼 세금을 깎는 것이라, 결정세액이
        공제액보다 적으면 거기까지만 돌아오고 남은 공제액은 이월 없이 사라진다.
      · 중도해지 추징: 공제받은 원금·운용수익에 기타소득세가 매겨진다(부득이한 사유는 예외).
      둘 다 금융사·핀테크의 상품 안내성 콘텐츠가 앞세우지 않는 부분이다.
primary_source: |
  국세청 「근로소득 > 세액공제 > 연금계좌 세액공제」 —
  https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&mi=6439
  사람이 직접 접속해 화면 캡처를 제공(2026-09-07). 전문은
  sources/nts-pension-account-tax-credit.md 에 보존.
  확보한 값: 세액공제 대상 납입한도 600만원(퇴직연금 포함 900만원, 두 소득 구간 동일),
  공제율 15%(종합소득금액 4,500만원·총급여 5,500만원 이하) / 12%(초과),
  ISA 만기자금 연금계좌 전환 시 전환금액의 10%·300만원 한도로 세액공제 한도 확대.
기준일: 2026-09-07 (국세청 페이지 확인일 — 페이지에 명시적 기준일 문구는 없으나 같은 화면의 혼인세액공제가 "24년~26년 혼인신고 분"으로 적혀 있어 2026년 기준 유지 페이지임을 확인)
tags: 연금저축, 세액공제, IRP세액공제, 연금저축세액공제한도, 연말정산, 연금계좌, 세액공제한도, 연금저축IRP, 연말절세, 환급액
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-07).
  게이트1: 네이버 키워드도구 실측 3,180회(PC 800 / 모바일 2,380).
  게이트2: RULES.md v3 기준 통과(serp_check 참조).
  게이트3: 소득 구간별 환급액 계산표 + 15%/16.5% 구분 + 한도 동일 사실 + ISA 전환
    추가한도 + 결정세액 한계 + 중도해지 추징. 상위 경쟁 글이 다루지 않는 항목이 다수다.
  게이트4: 국세청 원문 사람 캡처 확보(2026-09-07), sources/nts-pension-account-tax-credit.md.
capture_guide: |
  [해결됨 2026-09-07] 사람이 국세청 「근로소득 > 세액공제」 화면을 직접 캡처해 제공 —
  한도 600만원/900만원, 공제율 15%/12%, 소득 기준 4,500만원(총급여 5,500만원),
  ISA 전환 추가한도까지 모두 확보. 표 세 개를 채우고 게이트3·4를 충족으로 전환했다.
  전문은 sources/nts-pension-account-tax-credit.md.
  ★ 캡처 덕분에 잡은 것: 검색 결과의 16.5%/13.2%와 국세청 원문의 15%/12%가 달랐다.
    충돌이 아니라 지방소득세 포함 여부의 차이(15%×1.1=16.5%)임을 확인해, 그 구분 자체를
    본문 정보이득으로 넣었다. 원문을 안 봤으면 근거 없이 16.5%만 적었을 자리다.
  ★ 함께 확인한 것: 두 소득 구간의 납입한도가 600만원(900만원)으로 동일하다.
    예전에는 소득별로 한도도 달랐어서, 오래된 글과 갈리는 지점으로 본문에 명시했다.
self_check: |
  [2026-09-07 캡처 반영 후 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 3,180회(PC 800 / 모바일 2,380).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 국세청 원문 수치로 표 세 개를 모두 채웠다(한도표·공제율표·환급액 계산표).
  여기에 수치 없이도 성립하는 결정세액 한계와 중도해지 추징 섹션이 더해져 있다.
  특히 15%(국세청) vs 16.5%(인터넷) 구분은 캡처를 보지 않았으면 만들 수 없었던 정보이득이다.
  게이트4 충족 — 국세청 「근로소득 > 세액공제」 원문 캡처 확보(2026-09-07).
  전문 sources/nts-pension-account-tax-credit.md. 검색 요약의 숫자는 끝까지 쓰지 않았고,
  본문 수치는 전부 원문에서 나왔다.
  계산 검산 — 600×16.5%=99만원, 600×13.2%=79.2만원, 900×16.5%=148.5만원,
  900×13.2%=118.8만원, 경계 초과 시 차액 148.5−118.8=29.7만원. 소득세 기준으로는
  600×15%=90만원, 900×15%=135만원, 900×12%=108만원. 모두 재확인했다.
  [2026-09-07 병합 기록] 이 초안은 루틴 자동 실행분과 사람 요청 수동 초안이 겹쳐 생성됐다.
  루틴판을 기준으로 두고(측정 검색량·구법 수치 충돌 발견·access-note가 루틴판에만 있었음),
  수동판에서 제목 조사 제거와 정보이득 두 섹션, 태그 순서를 가져와 합쳤다.
  제목 16자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 4단어. 인트로 최상단.
  FAQ 6개와 JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 표현 없음.
  하단 면책 문구 포함.
  3편(ISA 계좌 한도)과의 카니발라이제이션 점검 — 3편은 ISA 계좌의 납입·비과세 한도가
  중심, 이 글은 연금계좌 세액공제가 중심이라 검색 의도가 다르다. ISA 전환 추가한도
  부분에서 3편으로 내부 링크를 건다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문 기관 안내 문장과 하단 참고 출처를
  전부 링크 처리. 국세청 연금계좌 세액공제 딥링크는 캡처로 페이지가 확인됐으므로
  이번에 본문 출처 캡션에 걸었다. target="_blank" rel="noopener", nofollow 미부착,
  href 안 &는 &amp;로 이스케이프.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
refresh_due: 2026-12-10
figure_plan: |
  2장. 그림1은 한도 납입 시 환급액 크기 비교(막대: 600만원/900만원 × 16.5%/13.2%), 그림2는 올해 납입 마감부터
  연말정산까지의 일정과 남은 공제 여지 계산(타임라인). 두 그림이 보여 주는 정보가 다르다(크기 vs 시간).
refresh_note: |
  [2026-10-15 갱신 - 티스토리 재반영 필요] 연말 절세 시즌 키워드(IRP 세액공제 월 5,020, 연금저축 세액공제 한도
  월 4,550)에 맞춰 첫 두 문장을 한도 900만원·12월 31일 마감·환급 148.5만/118.8만원 직답으로 교체.
  본문에 남아 있던 "원문 캡처 후 반영 예정" 문구 4곳 제거(캡처는 9/7에 이미 반영됨). 그림 2장, 연말까지 남은 공제
  여지 표, 투자자 관점 H2, 중도해지 추징 계산, 내부 링크 4개 추가. 수치는 9/7 국세청 캡처값과 70편 교차검증값(기타소득세
  16.5%, 연금소득세 3.3~5.5%) 재사용. 연 납입한도 1,800만원은 소득세법 시행령 근거로 금융사 안내 3곳이 일치(국세청 원문 미확인).
  2027년 시행 세제개편안은 국회 확정 전이라 이 글 수치에 반영하지 않았고, 12월 10일 갱신 때 확정 여부를 다시 본다.
self_check_refresh: |
  [2026-10-15 갱신 점검] 첫 문장 유형: 수치충격형(900만원·12/31 마감). 구조 유형: 계산형(첫 H2 한도표 + 연말 남은 공제 여지 계산표).
  어투 A 해설형. AI 티 점검: em대시 0개, mark 4개, FAQ 7개. 기관 안내 문장·출처 목록 전부 링크 처리.
  내부 링크: irp-isa-account-difference, retirement-pension-withdrawal-tax, isa-limit-benefit (전부 published).
  계산 검산: 600x0.165=99, 600x0.132=79.2, 900x0.165=148.5, 900x0.132=118.8, 300x0.165=49.5, 300x0.132=39.6,
  148.5-118.8=29.7. 2026-10-15~12-31 = 77일. 공제받은 900만원에 기타소득세 16.5% = 148.5만원.

---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-10-15</p>

<p>올해 연금저축·IRP 세액공제는 12월 31일까지 넣은 금액이 기준이고, 둘을 합쳐 <mark>연 900만원</mark>까지 공제됩니다. 한도를 다 채우면 총급여 5,500만원 이하는 148만 5천원, 초과는 118만 8천원을 돌려받습니다.</p>

<div style="background:#ecfdf5;border:2px solid #10b981;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#065f46;font-size:18px;">📌 연말 마감 전에 볼 숫자</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>연금저축 단독 공제 한도는 600만원이고, IRP를 더하면 합산 900만원입니다.</li>
    <li>공제율은 총급여 5,500만원을 기준으로 15%와 12%로 갈립니다(지방소득세 포함 16.5%·13.2%).</li>
    <li>2026년 10월 15일 기준 올해 납입 마감까지 77일 남았습니다.</li>
    <li>공제받은 뒤 중도해지하면 공제받은 납입금에 기타소득세가 붙어, 환급액이 사실상 되돌아갑니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li><a href="#sec-1" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">연금저축 세액공제 한도와 IRP 합산 한도</a></li>
  <li><a href="#sec-2" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">공제율과 실제 환급액 계산</a></li>
  <li><a href="#sec-3" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">IRP와 함께 넣으면 한도가 어떻게 되나요</a></li>
  <li><a href="#sec-4" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">연말까지 남은 기간, 얼마를 더 넣어야 하나요</a></li>
  <li><a href="#sec-5" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">연금계좌 세액공제가 투자자에게 주는 의미</a></li>
  <li><a href="#sec-6" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">한도까지 넣으면 그 금액을 다 돌려받나요</a></li>
  <li><a href="#sec-7" style="color:inherit;text-decoration:underline;text-underline-offset:3px;">중도에 해지하면 어떻게 되나요</a></li>
</ol>

<h2 id="sec-1" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">연금저축 세액공제 한도와 IRP 합산 한도</h2>

<p>연금저축 세액공제 한도는 연 600만원이고, IRP를 함께 넣으면 합산 연 900만원입니다. 소득세 공제가 아니라 <b>세액공제</b>라서, 계산된 세금에서 공제율만큼 직접 빠집니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f4f8;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">세액공제 대상 납입한도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">연금저축만 납입</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>연 600만원</mark></td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">연금저축 + 퇴직연금(IRP) 합산</td>
      <td style="border:1px solid #ddd;padding:8px;"><mark>연 900만원</mark></td>
    </tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;margin-top:6px;">출처: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&amp;mi=6439" target="_blank" rel="noopener">국세청 근로소득 세액공제 안내</a>(2026-09-07 확인).</p>

<p>공제 한도와 계좌에 넣을 수 있는 한도는 다른 개념입니다. 소득세법 시행령에 따라 모든 금융회사의 연금저축과 IRP를 합쳐 연 1,800만원까지 넣을 수 있지만, 세액공제는 그중 900만원까지만 받습니다. 900만원을 넘겨 넣은 금액은 공제 없이, 인출 전까지 운용수익의 과세만 미뤄집니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>한도는 소득과 무관합니다</b>
  <p style="margin:8px 0 0 0;">예전에는 소득에 따라 납입한도까지 달랐지만, 현재 국세청 표에서는 <b>두 소득 구간의 한도가 600만원(합산 900만원)으로 같습니다.</b> 소득에 따라 달라지는 것은 한도가 아니라 공제율입니다. 오래된 글에는 소득별로 한도가 다르게 적혀 있을 수 있습니다.</p>
</div>

<h2 id="sec-2" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">공제율과 실제 환급액 계산</h2>

<p>공제율은 총급여(근로소득자) 또는 종합소득금액(사업소득자 등) 구간에 따라 두 단계입니다. 소득이 낮은 구간이 공제율이 더 높습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f4f8;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">종합소득금액(총급여액)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">공제율</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:right;">지방소득세 포함</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">4,500만원(5,500만원) 이하</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;"><mark>15%</mark></td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">16.5%</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">4,500만원(5,500만원) 초과</td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;"><mark>12%</mark></td>
      <td style="border:1px solid #ddd;padding:8px;text-align:right;">13.2%</td>
    </tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;margin-top:6px;">괄호 밖은 종합소득금액(사업소득자 등), 괄호 안은 총급여액(근로소득자) 기준입니다. 출처: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&amp;mi=6439" target="_blank" rel="noopener">국세청 근로소득 세액공제 안내</a>(2026-09-07 확인).</p>

<div style="background:#fff8e6;border:2px solid #e0a800;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5c00;font-size:17px;">15%인가요, 16.5%인가요</strong>
  <p style="margin:10px 0 0 0;line-height:1.9;">둘 다 맞습니다. 기준이 다를 뿐입니다.</p>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>15% / 12%</b>: 국세청이 고시하는 <b>소득세</b> 기준 공제율입니다.</li>
    <li><b>16.5% / 13.2%</b>: 소득세가 줄면 딸린 <b>지방소득세(소득세의 10%)</b>도 함께 줄어드는 효과까지 더한 값입니다. 15% × 1.1 = 16.5%, 12% × 1.1 = 13.2%.</li>
  </ul>
  <p style="margin:10px 0 0 0;">체감상 손에 돌아오는 비율은 16.5% / 13.2%입니다. 국세청 표만 보면 15% / 12%로 적혀 있어 헷갈리는데, 서로 다른 숫자가 아니라 지방소득세를 포함했는지의 차이입니다.</p>
</div>

<p>한도를 꽉 채웠을 때 돌려받는 금액은 납입한도 × 공제율입니다. 아래는 지방소득세를 포함한 금액입니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/pension-savings-tax-credit-1.png" alt="연금저축만 600만원 납입 시 99만원과 79.2만원, 연금저축과 IRP 합산 900만원 납입 시 148.5만원과 118.8만원을 비교한 막대 그래프" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 국세청 공제율 표(2026-09-07 확인)로 계산한 환급액</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">납입 방식</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">납입액</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">5,500만원 이하<br>(16.5%)</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">5,500만원 초과<br>(13.2%)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">연금저축만</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">600만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">99만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">79만 2천원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">연금저축 + IRP</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">900만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>148만 5천원</mark></td><td style="border:1px solid #ccd;padding:10px;text-align:right;">118만 8천원</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">소득세 기준(15% / 12%)으로만 계산하면 각각 90만원·72만원, 135만원·108만원입니다.</p>

<p>"최대 148만원 환급"이라는 문구는 연금저축과 IRP를 합쳐 900만원을 넣고 총급여가 5,500만원 이하일 때의 숫자입니다. 총급여가 5,500만원 경계를 넘으면 같은 900만원을 넣어도 <b>29만 7천원</b>이 줄어듭니다.</p>

<h2 id="sec-3" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">IRP와 함께 넣으면 한도가 어떻게 되나요</h2>

<p>연금저축 600만원을 채운 뒤 남는 300만원은 IRP에 넣어야 합산 900만원을 다 쓸 수 있습니다. 연금저축과 IRP는 경쟁 관계가 아니라 보완 관계입니다.</p>

<ul style="line-height:1.9;">
  <li>연금저축만 가입한 경우: <b>600만원</b>까지만 공제</li>
  <li>연금저축 + IRP를 함께 가입한 경우: <b>900만원</b>까지 공제</li>
</ul>

<p>연금저축 계좌 하나에 900만원을 넣어도 공제는 600만원까지만 됩니다. IRP는 퇴직금을 받는 계좌이기도 해서 성격이 다른데, 두 계좌의 인출 조건 차이는 <a href="https://sensitiveboss3.tistory.com/entry/irp-isa-account-difference" target="_blank" rel="noopener">IRP와 ISA 차이 글</a>에 따로 정리했습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>ISA 만기자금을 옮기면 한도가 늘어납니다</b>
  <p style="margin:8px 0 0 0;">ISA 계약기간이 만료된 뒤 그 계좌 잔액을 연금계좌로 옮기면, 옮긴 금액이 그해 연금계좌 납입액에 포함되면서 <b>세액공제 한도가 전환금액의 10%(최대 300만원)만큼 늘어납니다.</b> 이 추가한도는 ISA 만기잔액을 연금계좌에 넣은 해에만 적용됩니다.</p>
  <p style="margin:8px 0 0 0;">ISA 자체의 한도와 비과세 혜택은 <a href="https://sensitiveboss3.tistory.com/entry/isa-limit-benefit" target="_blank" rel="noopener">ISA 계좌 한도와 비과세 혜택 글</a>을 참고하세요.</p>
</div>

<h2 id="sec-4" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">연말까지 남은 기간, 얼마를 더 넣어야 하나요</h2>

<p>올해 몫은 12월 31일까지 계좌에 들어간 금액만 잡히고, 2026년 10월 15일 기준으로 77일이 남았습니다. 남은 공제 여지는 900만원에서 올해 이미 넣은 금액을 뺀 값입니다.</p>

<figure style="margin:24px 0;"><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/pension-savings-tax-credit-2.png" alt="10월 15일부터 12월 31일 납입 마감까지 77일, 이후 2027년 초 연말정산과 5월 종합소득세 신고로 이어지는 일정 도식" style="max-width:100%;"><figcaption style="font-size:13px;color:#888;">자료: 국세청 안내와 소득세법 기준 일정, 2026-10-15 기준</figcaption></figure>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">올해 이미 넣은 금액</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">남은 공제 여지</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">추가 환급 최대<br>(16.5%)</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">추가 환급 최대<br>(13.2%)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">0원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">900만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">148만 5천원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">118만 8천원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">300만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">600만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">99만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">79만 2천원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">600만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">300만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">49만 5천원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">39만 6천원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">900만원 이상</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0원</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">연금저축에 600만원을 이미 채운 경우 남은 300만원은 IRP로 넣어야 합니다. IRP 계좌가 없다면 개설부터 해야 하니 연말에 몰리기 전에 시작하는 편이 시간이 덜 듭니다.</p>

<p>납입 금액은 2027년 초 연말정산(근로소득자)이나 5월 종합소득세 신고(사업소득자 등)에서 반영됩니다. 납입 내역은 <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>의 연금계좌 납입증명서로 볼 수 있습니다.</p>

<h2 id="sec-5" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">연금계좌 세액공제가 투자자에게 주는 의미</h2>

<p>세액공제는 납입하는 해에 확정되는 혜택이고, 계좌 안에서 투자한 결과와는 별개입니다. 900만원을 넣으면 투자 성과가 어떻든 총급여 5,500만원 이하는 148만 5천원, 초과는 118만 8천원이 공제 대상입니다.</p>

<ul style="line-height:1.9;">
  <li>공제율 16.5%는 납입액 대비 비율이라, 계좌 안의 펀드·ETF 수익률과 따로 계산합니다.</li>
  <li>반대로 계좌 안 투자가 손실이어도 공제 자체는 줄지 않지만, 원금 손실 가능성은 그대로입니다.</li>
  <li>연금 개시 전에는 자유롭게 빼기 어려워, 당장 쓸 돈은 넣지 않는 쪽이 구조에 맞습니다.</li>
</ul>

<p>인출 조건이 이 계좌의 핵심 제약입니다. 연금계좌의 인출 규칙과 세금은 <a href="https://sensitiveboss3.tistory.com/entry/retirement-pension-withdrawal-tax" target="_blank" rel="noopener">퇴직연금 중도인출 세금 글</a>에서 사유별로 계산해 두었습니다.</p>

<h2 id="sec-6" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">한도까지 넣으면 그 금액을 다 돌려받나요</h2>

<p>아닐 수 있습니다. 세액공제는 현금을 주는 제도가 아니라 내가 낼 세금을 깎아주는 제도라서, 원래 내야 할 세금(결정세액)보다 많이 깎을 수 없습니다.</p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>이런 경우 최대 환급액을 못 받습니다.</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>소득이 적어 결정세액 자체가 공제액보다 작은 경우</li>
    <li>다른 공제(인적공제·주택자금·의료비 등)로 이미 결정세액이 0에 가까워진 경우</li>
  </ul>
  <p style="margin:10px 0 0 0;">두 경우 모두 남은 공제액은 <b>다음 해로 이월되지 않고 그대로 사라집니다.</b> 올해 연말정산 예상 결과를 먼저 보고 납입액을 정하는 편이 안전합니다.</p>
</div>

<h2 id="sec-7" style="scroll-margin-top:72px;border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">중도에 해지하면 어떻게 되나요</h2>

<p>세액공제를 받은 계좌를 연금 개시 전에 해지하면 공제받은 납입금과 운용수익에 기타소득세 16.5%(지방소득세 포함)가 붙습니다. 900만원을 넣어 공제받았다면 900만원 × 16.5% = <mark>148만 5천원</mark>으로, 총급여 5,500만원 이하의 환급액과 같은 크기입니다.</p>

<ul style="line-height:1.9;">
  <li>총급여 5,500만원 이하: 환급 148만 5천원, 해지 시 추징 148만 5천원(운용수익 과세는 별도)</li>
  <li>총급여 5,500만원 초과: 환급 118만 8천원인데 추징은 148만 5천원이라 오히려 29만 7천원 손해</li>
</ul>

<p>사망·해외이주, 가입자나 부양가족의 장기 요양, 개인회생·파산처럼 세법상 부득이한 사유라면 운용수익에 나이별 3.3~5.5%의 낮은 연금소득세가 적용됩니다. 사유별 계산은 <a href="https://sensitiveboss3.tistory.com/entry/retirement-pension-withdrawal-tax" target="_blank" rel="noopener">퇴직연금 중도인출 세금 글</a>에 나와 있습니다.</p>

<div style="background:#ecfdf5;border:2px solid #10b981;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#065f46;font-size:18px;">마감 전에 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>합산 900만원이 공제 한도이고, 올해는 12월 31일까지 넣은 금액만 인정됩니다.</li>
    <li>이미 넣은 금액을 900만원에서 빼면 남은 공제 여지가 나옵니다.</li>
    <li>중도해지하면 환급 효과가 사실상 사라지므로 당장 쓸 돈은 넣지 않습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #10b981;padding-left:12px;margin-top:36px;">한도·환급 궁금증 모아 보기</h2>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">IRP 세액공제 한도는 연금저축과 따로 있나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 연금저축과 IRP는 합쳐서 연 900만원 안에서 공제됩니다. 연금저축이 600만원까지이고, 나머지 300만원을 IRP로 채우는 구조입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">연금저축 세액공제는 소득공제와 다른가요</summary>
  <p style="margin:10px 0 0 0;">네. 소득공제는 과세표준(세금을 매기는 기준금액)을 줄이는 방식이고, 세액공제는 계산된 세금 자체에서 공제율만큼 직접 빼주는 방식입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">한도를 넘겨 납입하면 초과분은 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">세액공제 대상에서는 빠지지만, 인출하기 전까지 운용 수익에 대한 과세가 이연되는 혜택은 그대로 유지됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">연금저축과 IRP를 둘 다 가입해야 하나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 연금저축만으로도 600만원까지 세액공제를 받을 수 있습니다. 합산 한도 900만원을 다 쓰려면 나머지 300만원을 IRP에 넣어야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공제율은 매년 소득이 바뀌면 같이 바뀌나요</summary>
  <p style="margin:10px 0 0 0;">네. 그해의 총급여(근로소득자) 또는 종합소득금액(사업소득자 등)이 어느 구간에 속하는지에 따라 공제율이 달라집니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">연금으로 나중에 받을 때는 세금이 없나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 연금으로 받을 때는 나이에 따라 3.3~5.5%의 연금소득세가 붙습니다. 공제받은 납입 원금과 운용수익이 과세 대상입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">공제받은 돈을 중도에 인출하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">부득이한 사유가 아니면 공제받은 납입금과 운용수익에 기타소득세 16.5%(지방소득세 포함)가 붙습니다. 부득이한 사유라면 나이별 3.3~5.5%의 연금소득세가 적용됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&amp;mi=6439" target="_blank" rel="noopener">국세청</a> 근로소득 세액공제 안내(연금계좌 세액공제, 2026-09-07 확인)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> 연금계좌 납입증명서 조회</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> 소득세법 시행령 연금계좌 납입한도 조문</li>
  </ul>
  기준일: 2026년 10월 15일(공제율·한도는 국세청 2026-09-07 확인값)
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공이 목적이며 특정 종목이나 금융상품의 매수·매도를 권하지 않습니다.
투자 판단과 그 결과의 책임은 투자자 본인에게 있습니다.
세율과 한도는 바뀔 수 있으니 최신 내용은 국세청 등 원출처에서 확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "IRP 세액공제 한도는 연금저축과 따로 있나요", "acceptedAnswer": {"@type": "Answer", "text": "아니요. 연금저축과 IRP는 합쳐서 연 900만원 안에서 공제됩니다. 연금저축이 600만원까지이고, 나머지 300만원을 IRP로 채우는 구조입니다."}},
    {"@type": "Question", "name": "연금저축 세액공제는 소득공제와 다른가요", "acceptedAnswer": {"@type": "Answer", "text": "네. 소득공제는 과세표준(세금을 매기는 기준금액)을 줄이는 방식이고, 세액공제는 계산된 세금 자체에서 공제율만큼 직접 빼주는 방식입니다."}},
    {"@type": "Question", "name": "한도를 넘겨 납입하면 초과분은 어떻게 되나요", "acceptedAnswer": {"@type": "Answer", "text": "세액공제 대상에서는 빠지지만, 인출하기 전까지 운용 수익에 대한 과세가 이연되는 혜택은 그대로 유지됩니다."}},
    {"@type": "Question", "name": "연금저축과 IRP를 둘 다 가입해야 하나요", "acceptedAnswer": {"@type": "Answer", "text": "아니요. 연금저축만으로도 600만원까지 세액공제를 받을 수 있습니다. 합산 한도 900만원을 다 쓰려면 나머지 300만원을 IRP에 넣어야 합니다."}},
    {"@type": "Question", "name": "공제율은 매년 소득이 바뀌면 같이 바뀌나요", "acceptedAnswer": {"@type": "Answer", "text": "네. 그해의 총급여(근로소득자) 또는 종합소득금액(사업소득자 등)이 어느 구간에 속하는지에 따라 공제율이 달라집니다."}},
    {"@type": "Question", "name": "연금으로 나중에 받을 때는 세금이 없나요", "acceptedAnswer": {"@type": "Answer", "text": "아니요. 연금으로 받을 때는 나이에 따라 3.3~5.5%의 연금소득세가 붙습니다. 공제받은 납입 원금과 운용수익이 과세 대상입니다."}},
    {"@type": "Question", "name": "공제받은 돈을 중도에 인출하면 어떻게 되나요", "acceptedAnswer": {"@type": "Answer", "text": "부득이한 사유가 아니면 공제받은 납입금과 운용수익에 기타소득세 16.5%(지방소득세 포함)가 붙습니다. 부득이한 사유라면 나이별 3.3~5.5%의 연금소득세가 적용됩니다."}}
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "연금저축 세액공제 얼마 돌려받나",
  "description": "연금저축·IRP 세액공제 한도 900만원, 소득 구간별 환급액, 12월 31일 납입 마감까지 남은 공제 여지와 중도해지 추징을 계산해 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-07",
  "dateModified": "2026-10-15",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/pension-savings-tax-credit"
  }
}
</script>
