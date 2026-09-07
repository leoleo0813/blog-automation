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
  [일부 완성 / 일부 캡처 대기]
  (a) 캡처 대기 — 납입액이 아니라 "실제로 얼마 돌려받나"를 소득 구간별로 계산해 보여주는
      예시 + IRP 합산 한도와의 관계. 계산 재료인 한도·공제율·소득구간 수치가 원문 캡처
      전이라 표·계산이 뼈대만 있고 값이 비어 있다.
  (b) 이미 완성 — 수치 없이도 성립하는 두 가지를 본문 섹션으로 넣었다. 상위 경쟁 글이
      "최대 148만원 환급"을 앞세우는 자리에서 이쪽이 실질적 차별점이다.
      · 결정세액 한계: 세액공제는 현금 지급이 아니라 낼 세금을 깎는 것이라, 결정세액이
        공제액보다 적으면 거기까지만 돌아오고 남은 공제액은 이월 없이 사라진다.
      · 중도해지 추징: 공제받은 원금·운용수익에 기타소득세가 매겨진다(부득이한 사유는 예외).
      둘 다 금융사·핀테크의 상품 안내성 콘텐츠가 앞세우지 않는 부분이다.
primary_source: |
  [미확보] 국세청 「연금계좌 세액공제」 안내 페이지로 계획했으나 이번 세션
  WebFetch가 EGRESS_BLOCKED(대조군 google.com도 동일 차단, 세션 전면 차단으로 판단).
  WebSearch로 확인한 다수 출처(토스뱅크·뱅크샐러드·삼성증권·미래에셋)가 "연금저축
  단독 한도 600만원, IRP 합산 900만원, 공제율 16.5%/13.2%(총급여 5,500만원 기준)"로
  일치하지만, 국세청 자체 페이지 스니펫 중 하나는 이보다 낮은 구법 수치(400만원/700만원
  등)를 섞어 인용해 두 세트가 충돌한다. 어느 쪽도 원문 캡처 없이 확정하지 않는다.
  상세: sources/pension-savings-tax-credit-access-note.md
기준일: 확인필요 (원문 캡처 후 페이지에 표시된 최종수정일 또는 확인일로 기입)
tags: 연금저축, 세액공제, 연말정산, 연금저축세액공제, IRP세액공제, 연금계좌, 세액공제한도, 노후준비, 절세
gate_pass: false
gate_pass_note: |
  게이트1 미확인(false) — 큐 등록 시 참고값(월 3,400)은 있으나 이번 실행에서
  네이버 키워드도구로 재확인하지 않았다. notify-repo-only.yml이 커밋 후 자동으로
  monthly_search_volume/gate1_pass를 채운다.
  게이트2 통과(serp_check 참조, v3 기준).
  게이트3 미충족 — 계산 예시의 재료인 한도·공제율 수치가 아직 원문으로 확정되지 않아
  표와 계산이 뼈대만 있고 비어 있다.
  게이트4 미충족 — 1차 출처(국세청) 원문을 캡처로 확보하지 못했다. WebSearch 단서만
  있고, 그마저 신구 수치가 충돌해 원문 대조 없이는 어느 쪽도 쓸 수 없다.
  4개 게이트 중 하나라도 미충족이면 발행 금지 원칙에 따라 gate_pass:false로 저장.
capture_guide: |
  (1) 왜 필요한가: 이 글의 핵심 정보이득은 "소득 구간별로 실제 얼마를 돌려받는지"
  계산해 보여주는 것인데, 계산의 재료인 세액공제 한도(연금저축 단독/IRP 합산)와
  소득 구간별 공제율(16.5%/13.2%)을 이번 세션에서 국세청 원문으로 확인하지 못했다.
  WebSearch로 찾은 여러 출처는 "600만원/900만원, 16.5%/13.2%, 총급여 5,500만원
  기준"으로 일치하지만, 국세청 자체 페이지 스니펫 중 하나는 이보다 낮은 구법 수치
  (400만원/700만원 등)를 섞어 인용해 신뢰할 수 없다. 원문을 직접 봐야 어느 쪽이
  현재 유효한 수치인지 확정할 수 있다.

  (2) 시도할 사이트 (우선순위):
  1순위 — 국세청 「연금계좌 세액공제」 안내:
    https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&mi=6439
    접속 → 페이지 안에서 "연금계좌 세액공제" 항목을 열어 (a) 총급여/종합소득금액
    구간별 세액공제 대상 납입한도(연금저축 단독, IRP 합산), (b) 구간별 공제율(%),
    (c) 페이지 하단이나 상단의 최종수정일/기준일을 화면 그대로 캡처.
  2순위 — 국세청 국세상담센터 Q&A(연금계좌 세액공제):
    https://call.nts.go.kr/call/qna/selectQnaInfo.do?mi=1318&ctgId=CTG11905
    접속 → 목록에서 "연금계좌 세액공제" 관련 질문을 열어 위와 같은 한도·공제율
    수치를 캡처. 1순위 페이지가 열리지 않을 때 대체용.
  3순위 — 법제처 찾기쉬운 생활법령정보:
    https://easylaw.go.kr 접속 → 검색창에 "연금저축 세액공제" 입력 →
    노후준비와 연금제도 > 개인연금제도 항목을 열어 기준일과 함께 캡처.
    (단, RULES.md "수치는 소관 부처 원문에서" 규칙에 따라 법제처 수치는 국세청
    수치와 교차확인 용도로만 쓰고, 충돌 시 국세청 원문을 우선한다.)

  (3) 캡처 후 할 일: 캡처한 화면(스크린샷)을 대화에 올려주세요. 위 (a)(b)(c)
  수치와 기준일을 알려주시면 이 초안의 표·계산 예시·본문 수치를 채우고
  gate_pass를 재판정하겠습니다.
self_check: |
  [2026-09-07, human-assisted/capture 재분류]
  게이트1 — 확인필요로 유지, notify-repo-only.yml 워크플로가 자동 기입 예정.
  게이트2 — v3 기준으로 통과 판정(serp_check 참조).
  게이트3 — 부분 충족. 계산 예시에 쓸 한도·공제율 수치가 아직 원문 미확정이라 표를
  채우지 않고 뼈대만 두었다(캡처 없이 gate_pass를 true로 만들지 않았다). 다만 수치 없이도
  성립하는 정보이득 두 가지를 본문 섹션으로 추가했다 — 결정세액 한계(공제액이 커도
  낸 세금보다 많이 못 깎고, 남은 공제액은 이월 없이 소멸)와 중도해지 시 기타소득세 추징.
  상위 경쟁 글이 "최대 148만원 환급"만 앞세우고 다루지 않는 부분이라 이 글의 실질적
  차별점이며, 표가 채워지면 게이트3이 완성된다.
  [2026-09-07 병합 기록] 이 초안은 루틴 자동 실행분과 사람 요청으로 만든 수동 초안이
  같은 시각에 겹쳐 생성됐다. 루틴판을 기준으로 두고(측정된 검색량 3,180회, 구법 수치
  충돌 발견, access-note 보존이 루틴판에만 있었음), 수동판에서 제목의 조사 제거와
  위 두 정보이득 섹션, 태그 순서를 가져와 합쳤다. 어느 한쪽을 버리지 않았다.
  게이트4 — 미충족. nts.go.kr WebFetch가 EGRESS_BLOCKED(대조군 google.com도 차단,
  세션 전면 차단). WebSearch 단서는 신구 수치가 충돌해 본문 출처로 인용하지 않았다.
  제목 15자 내외·금지어 없음. 슬러그 영문 소문자+하이픈(pension-savings-tax-credit,
  4단어). 인트로 문단 최상단. FAQ 6개와 JSON-LD 1:1 일치(문항은 수치 확정 전에도
  답할 수 있는 개념·절차 위주로 구성). @id를 티스토리 entry 패턴으로 지정.
  종목·상품 추천 표현, 단정 표현 없음. 하단 고정 문구 포함.
  3편(ISA 계좌 한도)과의 카니발라이제이션 점검 — 3편은 ISA 계좌의 납입·비과세
  한도가 중심, 이 글은 연금저축·IRP 계좌의 세액공제가 중심이라 대상 계좌와 세제
  혜택 종류가 달라 검색 의도가 다르다. 본문에서 3편으로 절세계좌 비교 관점으로
  내부 링크 안내.
  기관 링크 점검(RULES.md 「기관 링크 필수」) — 본문에서 국세청·홈택스로 안내하는
  문장 전부 <a target="_blank" rel="noopener"> 처리, 하단 참고 출처 목록도 전부
  링크 처리. 정부기관이라 nofollow 미부착. href 안 &는 &amp;로 이스케이프.
  종합 판정: 게이트3·4 미충족 → gate_pass:false. capture_guide대로 사람이
  원문을 캡처해 주면 표·계산 예시를 채우고 재판정한다. 그 전까지는 저장만 하고
  발행하지 않는다.
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

<p style="background:#fff3cd;border:1px solid #e0a800;border-radius:6px;padding:10px 14px;font-size:14px;color:#7a5c00;">⚠️ 이 초안은 세액공제 한도·공제율 수치를 국세청 원문으로 아직 확정하지 못한 상태입니다(자동화 세션의 네트워크 접근이 막혀 있음). 아래 표와 계산 예시는 사람이 원문을 캡처해 준 뒤 채워집니다 — capture_guide 참고.</p>

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

<p>세액공제를 받을 수 있는 납입한도는 <b>연금저축 단독</b>인지 <b>IRP를 함께 넣는지</b>에 따라 달라집니다. 정확한 한도는 아래 표가 채워지는 대로 확인하실 수 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f4f8;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">세액공제 대상 납입한도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">연금저축 단독</td>
      <td style="border:1px solid #ddd;padding:8px;">캡처 필요</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">연금저축 + IRP 합산</td>
      <td style="border:1px solid #ddd;padding:8px;">캡처 필요</td>
    </tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;margin-top:6px;">※ 위 한도는 <a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> 원문 캡처가 반영되는 대로 확정됩니다. 한도를 넘겨 넣은 금액은 세액공제 대상에서 빠지지만, 인출 전까지 과세는 이연됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">소득 구간별 공제율은 어떻게 다른가요</h2>

<p>공제율은 <b>총급여(근로소득자) 또는 종합소득금액(사업소득자 등)</b> 구간에 따라 두 단계로 나뉩니다. 소득이 낮은 구간일수록 공제율이 더 높게 적용됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f4f8;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">소득 구간</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">공제율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">캡처 필요 이하</td>
      <td style="border:1px solid #ddd;padding:8px;">캡처 필요</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">캡처 필요 초과</td>
      <td style="border:1px solid #ddd;padding:8px;">캡처 필요</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제로 얼마나 돌려받나요</h2>

<p>한도를 꽉 채워 납입했을 때 실제로 돌려받는 금액은 <mark>납입한도 × 공제율</mark>로 계산합니다. 이 계산 예시는 위 두 표의 수치가 확정된 뒤 채워집니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>계산 예시 자리 (캡처 후 작성)</b>
  <p style="margin:8px 0 0 0;">예: 연금저축만 한도까지 납입한 경우, IRP까지 합산해 한도까지 납입한 경우를 소득 구간별로 각각 계산해 보여줄 예정입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">IRP와 함께 넣으면 한도가 어떻게 되나요</h2>

<p>연금저축 단독 한도를 넘는 금액을 IRP에 추가로 넣으면, 합산한도까지 세액공제를 더 받을 수 있습니다. 즉 연금저축과 IRP는 <b>경쟁 관계가 아니라 보완 관계</b>입니다.</p>

<ul style="line-height:1.9;">
  <li>연금저축만 가입한 경우: 연금저축 단독 한도까지만 공제</li>
  <li>연금저축 + IRP를 함께 가입한 경우: 합산한도까지 공제 (정확한 한도는 캡처 후 반영)</li>
</ul>

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
  <p style="margin:10px 0 0 0;">아니요. 연금저축만으로도 단독 한도까지 세액공제를 받을 수 있습니다. IRP는 그 한도를 넘겨 더 공제받고 싶을 때 추가로 활용하는 계좌입니다.</p>
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
        "text": "아니요. 연금저축만으로도 단독 한도까지 세액공제를 받을 수 있습니다. IRP는 그 한도를 넘겨 더 공제받고 싶을 때 추가로 활용하는 계좌입니다."
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
