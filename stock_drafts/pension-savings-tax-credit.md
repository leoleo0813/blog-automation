---
keyword: 연금저축 세액공제
title: 연금저축 세액공제 얼마 돌려받나
slug: pension-savings-tax-credit
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 3180 (PC 800 / 모바일 2380)
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
tags: 연금저축, 세액공제, 연말정산, 연금저축세액공제, IRP세액공제, 연금계좌, 세액공제한도, 노후준비, 절세
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
---

<p>연금저축과 IRP(개인형 퇴직연금)에 돈을 넣으면 <mark>연말정산이나 종합소득신고 때 세액공제</mark>를 받을 수 있습니다. 다만 한도를 넘겨 넣어도 세액공제가 늘지 않으므로, 얼마까지 넣어야 하는지 먼저 아는 것이 중요합니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>연금저축과 IRP에 넣은 금액 중 <b>세액공제 한도까지만</b> 실제로 세금을 돌려받습니다.</li>
    <li>공제율은 <b>총급여(또는 종합소득금액) 구간</b>에 따라 달라집니다.</li>
    <li>연금저축만 넣을 때와 IRP를 함께 넣을 때 <b>적용되는 한도가 다릅니다.</b></li>
    <li>한도를 넘겨 넣은 금액은 세액공제는 없지만, 인출 전까지 과세가 이연됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>연금저축 세액공제란 무엇인가요</li>
  <li>연금저축 세액공제 한도는 얼마인가요</li>
  <li>소득 구간별 공제율은 어떻게 다른가요</li>
  <li>실제로 얼마나 돌려받나요</li>
  <li>IRP와 함께 넣으면 한도가 어떻게 되나요</li>
  <li>한도까지 넣으면 그 금액을 다 돌려받나요</li>
  <li>중도에 해지하면 어떻게 되나요</li>
  <li>세액공제는 언제까지 신청해야 하나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">연금저축 세액공제란 무엇인가요</h2>

<p>연금저축은 노후자금을 준비하면서 <mark>납입한 금액의 일부를 세금에서 직접 빼주는</mark> 개인연금 계좌입니다. 소득공제가 아니라 세액공제라서, 계산된 세금 자체에서 공제율만큼 금액이 빠집니다.</p>

<ul style="line-height:1.9;">
  <li>연금저축펀드, 연금저축보험 등 상품 종류와 무관하게 "연금저축" 계좌면 대상입니다.</li>
  <li>개인형 퇴직연금(IRP)도 별도로 또는 연금저축과 함께 세액공제 대상이 됩니다.</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">연금저축 세액공제 한도는 얼마인가요</h2>

<p>세액공제를 받을 수 있는 납입한도는 <b>연금저축 단독</b>인지 <b>IRP를 함께 넣는지</b>에 따라 달라집니다.</p>

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

<p style="font-size:13px;color:#888;margin-top:6px;">출처: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&amp;mi=6439" target="_blank" rel="noopener">국세청 근로소득 세액공제 안내</a>(2026-09-07 확인). 한도를 넘겨 넣은 금액은 세액공제 대상에서 빠지지만, 인출 전까지 과세는 이연됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>한도는 소득과 무관합니다</b>
  <p style="margin:8px 0 0 0;">예전에는 소득에 따라 납입한도까지 달랐지만, 현재 국세청 표에서는 <b>두 소득 구간의 한도가 600만원(합산 900만원)으로 같습니다.</b> 소득에 따라 달라지는 것은 한도가 아니라 공제율입니다. 오래된 글에는 소득별로 한도가 다르게 적혀 있을 수 있습니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">소득 구간별 공제율은 어떻게 다른가요</h2>

<p>공제율은 <b>총급여(근로소득자) 또는 종합소득금액(사업소득자 등)</b> 구간에 따라 두 단계로 나뉩니다. 소득이 낮은 구간일수록 공제율이 더 높게 적용됩니다.</p>

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
    <li><b>15% / 12%</b> — 국세청이 고시하는 <b>소득세</b> 기준 공제율입니다.</li>
    <li><b>16.5% / 13.2%</b> — 소득세가 줄면 그에 딸린 <b>지방소득세(소득세의 10%)</b>도 함께 줄어드는 효과까지 더한 값입니다. 15% × 1.1 = 16.5%, 12% × 1.1 = 13.2%.</li>
  </ul>
  <p style="margin:10px 0 0 0;">체감상 손에 돌아오는 비율은 <mark>16.5% / 13.2%</mark>가 맞습니다. 다만 세법 조문이나 국세청 표를 직접 보면 15% / 12%로 적혀 있어 혼란스러울 수 있는데, 서로 다른 숫자가 아니라 지방소득세를 포함했는지의 차이입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제로 얼마나 돌려받나요</h2>

<p>한도를 꽉 채워 납입했을 때 돌려받는 금액은 <mark>납입한도 × 공제율</mark>로 계산합니다. 아래는 지방소득세를 포함한 실제 체감 금액 기준입니다.</p>

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

<p style="font-size:13px;color:#888;">소득세 기준(15% / 12%)으로만 계산하면 각각 90만원·72만원, 135만원·108만원입니다. 위 표는 지방소득세까지 포함한 금액입니다.</p>

<p>흔히 보이는 <b>"최대 148만원 환급"</b>이라는 문구는 <mark>연금저축과 IRP를 합쳐 900만원을 다 넣고, 총급여가 5,500만원 이하인 경우</mark>의 숫자입니다. 조건이 하나라도 다르면 금액이 달라집니다.</p>

<p>총급여가 5,500만원 경계를 넘으면 같은 900만원을 넣어도 <b>29만 7천원</b>이 줄어듭니다. 경계 근처라면 신경 쓸 만한 차이입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">IRP와 함께 넣으면 한도가 어떻게 되나요</h2>

<p>연금저축 단독 한도를 넘는 금액을 IRP에 추가로 넣으면, 합산한도까지 세액공제를 더 받을 수 있습니다. 즉 연금저축과 IRP는 <b>경쟁 관계가 아니라 보완 관계</b>입니다.</p>

<ul style="line-height:1.9;">
  <li>연금저축만 가입한 경우: <b>600만원</b>까지만 공제</li>
  <li>연금저축 + IRP를 함께 가입한 경우: <b>900만원</b>까지 공제</li>
</ul>

<p>연금저축에 600만원을 채웠다면, 나머지 <mark>300만원은 IRP에 넣어야</mark> 합산한도를 다 쓸 수 있습니다. 연금저축 계좌 하나에 900만원을 넣어도 공제는 600만원까지만 됩니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>ISA 만기자금을 옮기면 한도가 늘어납니다</b>
  <p style="margin:8px 0 0 0;">ISA 계약기간이 만료된 뒤 그 계좌 잔액을 연금계좌로 옮기면, 옮긴 금액이 그해 연금계좌 납입액에 포함되면서 <b>세액공제 한도가 전환금액의 10%(최대 300만원)만큼 늘어납니다.</b> 이 추가한도는 ISA 만기잔액을 연금계좌에 넣은 해에만 적용됩니다.</p>
  <p style="margin:8px 0 0 0;">ISA 자체의 한도와 비과세 혜택은 따로 정리한 "ISA 계좌 한도와 비과세 혜택" 글을 참고하세요.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">한도까지 넣으면 그 금액을 다 돌려받나요</h2>

<p>아닐 수 있습니다. 이 지점이 "최대 얼마 환급"이라는 홍보 문구와 실제 결과가 갈리는 자리입니다.</p>

<p><mark>세액공제는 나라가 현금을 주는 제도가 아니라, 내가 낼 세금을 깎아주는 제도</mark>입니다. 그래서 공제받을 수 있는 금액이 아무리 커도 <b>원래 내야 할 세금(결정세액)보다 많이 깎을 수는 없습니다.</b></p>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>이런 경우 최대 환급액을 못 받습니다.</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>소득이 적어 결정세액 자체가 공제액보다 작은 경우</li>
    <li>다른 공제(인적공제·주택자금·의료비 등)로 이미 결정세액이 0에 가까워진 경우</li>
  </ul>
  <p style="margin:10px 0 0 0;">두 경우 모두 남은 공제액은 <b>다음 해로 이월되지 않고 그대로 사라집니다.</b> 연말정산 결과를 먼저 확인한 뒤 납입액을 정하는 편이 안전한 이유입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">중도에 해지하면 어떻게 되나요</h2>

<p>세액공제를 받은 뒤 연금 개시 전에 해지하면 <mark>그동안 받은 혜택을 되돌려 내야 합니다.</mark> 공제받았던 납입 원금과 그 운용수익에 기타소득세가 매겨지는 방식입니다.</p>

<p>연금저축을 <b>중도 인출이 자유로운 저축</b>으로 생각하고 시작하면 이 지점에서 손해를 봅니다. 세액공제는 노후에 연금으로 받는 것을 전제로 미리 주는 혜택이기 때문입니다.</p>

<p>다만 사망·해외이주, 가입자나 부양가족의 장기 요양, 개인회생·파산처럼 부득이한 사유로 인정되는 경우에는 낮은 세율이 적용됩니다. 해당 여부와 정확한 세율은 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a>에서 확인하는 것이 정확합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">세액공제는 언제까지 신청해야 하나요</h2>

<p>세액공제는 <b>해당 연도 12월 31일까지 납입한 금액</b>을 기준으로 다음 해 연말정산(근로소득자) 또는 5월 종합소득세 신고(사업소득자 등)에서 반영됩니다. 신청은 별도 서류 제출보다는 연말정산 자료나 <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> 연금계좌 납입증명서 조회로 확인합니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:28px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">정리</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>연금저축·IRP 세액공제는 한도까지 넣은 금액에 소득 구간별 공제율을 곱해 돌려받습니다.</li>
    <li>연금저축과 IRP를 함께 넣으면 더 높은 합산한도까지 공제받을 수 있습니다.</li>
    <li>정확한 한도·공제율 수치는 국세청 원문 확인 후 이 글에 반영됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

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
  <p style="margin:10px 0 0 0;">아닙니다. 연금으로 수령할 때는 연금소득세가 저율로 부과됩니다. 다만 세액공제를 받은 원금과 운용수익 전체가 과세 대상이라는 점은 국세청 원문으로 별도 확인이 필요합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:6px;padding:12px 16px;margin:8px 0;">
  <summary style="font-weight:bold;cursor:pointer;">세액공제 받은 금액을 중도에 인출하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">세액공제를 받은 부분을 연금 외 형태로 중도 인출하면 기타소득세 등 불이익이 있을 수 있습니다. 정확한 세율과 예외 조건은 국세청 원문 확인 후 이 글에 반영할 예정입니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (캡처 후 최종 확정 예정):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> — 연금계좌 세액공제 안내 (원문 캡처 대기 중)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> — 연금계좌 납입증명서 조회</li>
  </ul>
  기준일: 확인필요 (원문 캡처 후 기입)
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를 권유하지 않습니다.
투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "연금저축 세액공제는 소득공제와 다른가요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네. 소득공제는 과세표준(세금을 매기는 기준금액)을 줄이는 방식이고, 세액공제는 계산된 세금 자체에서 공제율만큼 직접 빼주는 방식입니다."
      }
    },
    {
      "@type": "Question",
      "name": "한도를 넘겨 납입하면 초과분은 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "세액공제 대상에서는 빠지지만, 인출하기 전까지 운용 수익에 대한 과세가 이연되는 혜택은 그대로 유지됩니다."
      }
    },
    {
      "@type": "Question",
      "name": "연금저축과 IRP를 둘 다 가입해야 하나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아니요. 연금저축만으로도 600만원까지 세액공제를 받을 수 있습니다. 합산 한도 900만원을 다 쓰려면 나머지 300만원을 IRP에 넣어야 합니다."
      }
    },
    {
      "@type": "Question",
      "name": "공제율은 매년 소득이 바뀌면 같이 바뀌나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "네. 그해의 총급여(근로소득자) 또는 종합소득금액(사업소득자 등)이 어느 구간에 속하는지에 따라 공제율이 달라집니다."
      }
    },
    {
      "@type": "Question",
      "name": "연금으로 나중에 받을 때는 세금이 없나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "아닙니다. 연금으로 수령할 때는 연금소득세가 저율로 부과됩니다. 다만 세액공제를 받은 원금과 운용수익 전체가 과세 대상이라는 점은 국세청 원문으로 별도 확인이 필요합니다."
      }
    },
    {
      "@type": "Question",
      "name": "세액공제 받은 금액을 중도에 인출하면 어떻게 되나요",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "세액공제를 받은 부분을 연금 외 형태로 중도 인출하면 기타소득세 등 불이익이 있을 수 있습니다. 정확한 세율과 예외 조건은 국세청 원문 확인 후 이 글에 반영할 예정입니다."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "연금저축 세액공제 얼마 돌려받나",
  "description": "연금저축·IRP 세액공제 한도와 소득 구간별 공제율, 그리고 결정세액 때문에 최대 환급액을 다 못 받는 경우와 중도해지 시 추징까지 정리합니다. (한도·공제율 수치는 원문 캡처 후 확정)",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-07",
  "dateModified": "2026-09-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/pension-savings-tax-credit"
  }
}
</script>
