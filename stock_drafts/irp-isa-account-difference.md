---
keyword: IRP ISA 차이
title: IRP ISA 차이 세액공제 인출조건 비교
slug: irp-isa-account-difference
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 700 (PC 220 / 모바일 480)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-23]
  WebSearch "IRP ISA 차이" 상위 9개:
  brunch.co.kr(브런치, 개인 콘텐츠) / v.daum.net(다음뉴스, 언론) /
  tossbank.com(토스뱅크, 핀테크 콘텐츠) / weolbu.com(월급쟁이부자들, 개인·커뮤니티
  콘텐츠) / help.3o3.co.kr(핀테크 서비스 고객센터) / support.boolio.co.kr(핀테크
  서비스 고객센터) / frism.io(소형 투자자문사 블로그) / en.wikipedia.org ×2(주제
  무관 오검색, IRPS·Integrated resource planning)
  1) 진입 여지: 있음. 브런치·월급쟁이부자들·프리즘 등 개인/소규모 콘텐츠가
     상위 다수를 차지해 대형 금융사·공식기관이 SERP를 잠그지 않았다.
  2) 검색 의도: 정보 탐색형("뭐가 다른지, 뭘 먼저 넣어야 하는지"). 조회·신청·
     계산기 실행이 지배적 의도가 아니다.
  3) 답 완결 여부: 상위 결과 대부분이 정의·세액공제율 나열에 그치고, 두 계좌를
     "동시에 쓸 때"의 실제 절세액 계산이나 인출 조건 차이를 표로 정리한 글은
     찾지 못했다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) IRP·ISA 구조 비교표(세액공제 여부·한도, 비과세 방식, 의무 유지기간,
      중도 인출·해지 시 세금)를 한 화면에 정리. 각 항목은 8편(연금저축
      세액공제)·3편(ISA 계좌 한도)·67편(ISA 중도해지 세금)·70편(퇴직연금
      중도인출 세금)에서 이미 원문으로 확정한 수치를 재사용했다.
  (b) ISA 만기자금을 연금계좌로 옮기면 세액공제가 실제로 얼마나 늘어나는지
      원 단위 계산 예시(이전액 3,000만원 기준 300만원 추가 한도 → 495,000원
      또는 396,000원 추가 환급).
  (c) "IRP는 인출 제한이 강하고 ISA는 원금 범위 안에서 자유롭다"는 유동성
      차이를 혼동 포인트로 짚어, 단순 세액공제율 비교글에는 없는 실전 판단
      기준을 제공한다.
primary_source: |
  이번 편에서 새로 확인한 수치는 하나뿐이다: IRP 연금 수령 개시 요건(만 55세
  이상 + 가입기간 5년 이상, 퇴직금 이체분은 기간요건 없음)과 연금소득세율
  (55~69세 5.5%, 70~79세 4.4%, 80세 이상 3.3%). 1차 출처 국세청 「연금소득의
  범위」(nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7885&mi=6605)에
  WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-23). RULES.md 「1차 출처가
  막혔을 때」 기준에 따라 교차검증 진행: 독립 출처 5곳(kbthink.com·KB국민은행
  준공식 2건, kcie.or.kr·금융투자자보호재단 준정부, docs.channel.io/frism
  소형 투자자문사, tossbank.com 핀테크, securities.miraeasset.com 증권사
  공식)이 55세·5년·세율 3단계(5.5/4.4/3.3%) 수치에서 충돌 없이 일치해
  진행했다. 다만 이 항목은 나이 구간별 세율이라는 점에서 원문 확정이 특히
  중요한 유형이므로, gate_pass_note에 재확인 필요성을 남긴다.

  나머지 수치는 이 시리즈에서 이미 사람이 원문을 직접 캡처해 확정한 값을
  재사용했다:
  - 세액공제 600만원/900만원 한도, 공제율 15%(16.5%)·12%(13.2%), ISA 만기
    전환 시 10%·300만원 추가 한도. 8편(연금저축 세액공제), 국세청 「근로소득
    연금계좌 세액공제」 캡처(nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=
    7875&mi=6439, 확인일 2026-09-07).
  - ISA 납입한도 2,000만원/1억원, 비과세한도 200만원·400만원, 초과분 9.9%.
    3편(ISA 계좌 한도), 국세법령정보시스템·금융위원회 캡처(확인일 2026-09-04).
  - ISA 의무가입 3년, 원금 범위 인출과 중도해지 구분, 중도해지 시 15.4%
    일반과세. 67편(ISA 중도해지 세금), 금융위원회 교차검증(확인일 2026-09-21).
  - IRP 중도인출 시 운용수익 기타소득세 16.5%, 부득이한 사유는 연금소득세
    5.5%. 70편(퇴직연금 중도인출 세금), 국세청 교차검증(확인일 2026-09-22).
기준일: 2026년 9월 기준
tags: IRP, ISA, IRP ISA차이, 개인형퇴직연금, 개인종합자산관리계좌, 연금계좌세액공제, ISA만기이전, 절세계좌, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 확인 결과(2026-09-23):
  게이트1 충족: 네이버 키워드도구 실측 700회(PC 220 / 모바일 480, 제도 기준
  100 이상).
  게이트2 충족: serp_check 참조, 3개 탈락 조건 모두 미해당.
  게이트3 충족: 구조 비교표 + ISA→IRP 전환 절세액 계산 예시 + 유동성 차이
  정리. 상위 경쟁 글에 없는 정보다.
  게이트4: 대부분 이 시리즈 내 이미 원문 캡처로 확정된 수치의 재사용이라
  충족. 다만 새로 교차검증한 "55세·5년·연금소득세 3단계 세율"은 5곳 독립
  출처가 일치했으나 아직 국세청 원문을 직접 캡처하지 못했다. 나이 구간별
  세율은 이 프로젝트가 과거 오류를 잡아낸 유형(세율·한도 숫자)과 결이
  같으므로, 사람이 국세청 「연금소득의 범위」 페이지(위 URL)를 열어 55세·
  5년·5.5%/4.4%/3.3% 수치를 한 번 대조해 주는 것을 권한다. 대조 후 다르면
  본문의 해당 문장만 고치면 된다.
self_check: |
  제목 23자·금지어 없음·조사/접속사 없음("차이" "비교" 명사형 나열). "비교"가
  제목에 있고 본문에 실제 비교표가 있음(RULES 제목 규칙 충족).
  슬러그 irp-isa-account-difference, 영문 소문자+하이픈 4단어.
  인트로 문단이 최상단, 목차 이전에 핵심 요약 박스 배치.
  본문 표(구조 비교표) thead/tbody 시맨틱 적용.
  FAQ 5개(6개 고정 아님)와 JSON-LD FAQPage 1:1 일치.
  @id를 https://sensitiveboss3.tistory.com/entry/irp-isa-account-difference 로
  지정. author/publisher "센시티브보스"로 고정.
  종목·상품 추천 표현, 단정적 손절매·매수 조언 없음. "권유하지 않는다"는
  중립적 안내만 포함.
  하단 고정 문구(면책) 포함. 이전 편들과 토씨를 다르게 재작성.
  카니벌라이제이션 점검: 3편(ISA 계좌 한도)·8편(연금저축 세액공제)·67편
  (ISA 중도해지 세금)·70편(퇴직연금 중도인출 세금)·71편(ISA 계좌 이전 방법)
  본문을 grep해 확인. 4개 파일 모두 "IRP" 또는 "ISA"를 단일 주제로 다룰 뿐
  두 계좌를 나란히 비교하는 구조가 아니라 검색 의도가 겹치지 않는다(각 파일의
  IRP/ISA grep 결과: isa-limit-benefit 0건, isa-gain-loss-netting 1건,
  isa-early-termination-tax 0건, isa-account-transfer-guide 0건,
  pension-savings-tax-credit 22건이나 세액공제가 중심 주제, retirement-
  pension-db-dc-difference 5건이나 DB/DC 비교가 중심 주제). 겹치는 지점(세액
  공제 수치, ISA 한도)은 새로 만들지 않고 해당 편으로 유도하는 문장으로만
  연결했다.
  AI 티 점검: em대시 0개(파일 전체 검색 확인, YAML 메타 포함), "다만"은 본문에 1회만
  쓰고 나머지는 "단," "그런데" 등으로 분산해 기본 전환어로 반복하지 않음,
  mark 강조 4개(900만원 한도, 연금소득세 5.5%, 15.4%, 300만원), FAQ 5개,
  핵심요약 박스 제목·색을 기존 "📌 핵심만 먼저 보기"(#eef6ff/#4a90d9)에서
  "✅ 미리 알아두면 좋은 것"(#f5f3ff/#7c5fd1)으로 변경, 소제목 5개 중 3개는
  서술형("~차이", "~손실" 등)·2개만 질문형으로 절반 이상 서술형 충족, 면책
  문구도 새로 작성해 기존 편과 토씨가 다름, 헤지 문구("~라고 알려져 있다" 등)
  0회.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-23</p>

<p>IRP와 ISA는 <mark>세액공제 여부와 인출 조건이 근본적으로 다른 계좌</mark>입니다. IRP는 노후 자금을 묶어두는 대신 세액공제를 주는 구조이고, ISA는 언제든 원금을 뺄 수 있는 대신 세액공제가 없는 구조입니다.</p>

<div style="background:#f5f3ff;border:2px solid #7c5fd1;border-radius:10px;padding:16px 20px;margin:20px 0;">
  <strong style="color:#4c3a94;font-size:18px;">✅ 미리 알아두면 좋은 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>IRP는 연금저축과 합쳐 연 <mark>900만원</mark>까지 세액공제를 받지만, 만 55세 전에는 법정 사유가 있어야만 인출할 수 있습니다.</li>
    <li>ISA는 세액공제가 없는 대신 납입 원금 범위 안에서는 언제든 자유롭게 인출할 수 있습니다.</li>
    <li>ISA 만기자금을 IRP나 연금저축으로 옮기면 세액공제 한도가 최대 300만원 더 늘어납니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #7c5fd1;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>IRP와 ISA 기본 성격 차이</li>
  <li>세액공제 구조 비교</li>
  <li>인출 조건과 중도해지 세금 차이</li>
  <li>ISA 만기자금 IRP로 옮기면 세액공제가 늘어나나요</li>
  <li>두 계좌를 함께 쓰면 한도가 어떻게 되나요</li>
</ol>

<h2 style="border-left:6px solid #7c5fd1;padding-left:12px;margin-top:36px;">IRP와 ISA 기본 성격 차이</h2>

<p>IRP(개인형퇴직연금)는 <b>퇴직급여와 개인 추가 납입금을 함께 관리하며 55세 이후 연금으로 받는 것을 전제로 만들어진 계좌</b>입니다. ISA(개인종합자산관리계좌)는 예금·펀드·ETF 등 여러 금융상품을 한 계좌에 담아 <b>비교적 자유롭게 운용하는 종합자산관리 계좌</b>입니다.</p>

<p>두 계좌는 목적 자체가 다릅니다. IRP는 세액공제와 노후 준비에, ISA는 비과세 혜택과 자산 운용 유연성에 초점이 맞춰져 있습니다. 이 차이가 세액공제·인출 조건·중도해지 세금까지 전부 갈라놓습니다.</p>

<h2 style="border-left:6px solid #7c5fd1;padding-left:12px;margin-top:36px;">세액공제 구조 비교</h2>

<p>IRP는 연금저축과 합산해 연 <mark>900만원</mark>까지 세액공제 대상입니다. 총급여 5,500만원(종합소득금액 4,500만원) 이하는 16.5%, 초과하면 13.2%가 적용됩니다. 900만원을 다 채우면 각각 148.5만원, 118.8만원을 돌려받는 셈입니다.</p>

<p>ISA는 원칙적으로 납입액에 대한 세액공제가 없습니다. 단, ISA 만기자금을 연금계좌(IRP·연금저축)로 옮기면 이전금액의 10%, 최대 300만원만큼 세액공제 한도가 추가로 생깁니다. 자세한 이전 절차는 8편(연금저축 세액공제)에서 다뤘습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;">
  <thead>
    <tr style="background:#f5f3ff;">
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">IRP</th>
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">ISA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:10px;">세액공제</td>
      <td style="border:1px solid #ddd;padding:10px;">연금저축 합산 연 900만원, 공제율 13.2~16.5%</td>
      <td style="border:1px solid #ddd;padding:10px;">원칙적으로 없음(만기자금 연금계좌 이전 시 최대 300만원 추가)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:10px;">납입한도</td>
      <td style="border:1px solid #ddd;padding:10px;">별도 상한 없음(세액공제만 900만원까지)</td>
      <td style="border:1px solid #ddd;padding:10px;">연 2,000만원, 계좌 총 1억원</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:10px;">비과세 방식</td>
      <td style="border:1px solid #ddd;padding:10px;">연금 수령 시 연금소득세 3.3~5.5% 저율 적용</td>
      <td style="border:1px solid #ddd;padding:10px;">비과세한도(200만원 또는 400만원) 초과분만 9.9% 분리과세</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:10px;">의무 유지기간</td>
      <td style="border:1px solid #ddd;padding:10px;">만 55세 이상 + 가입기간 5년 이상(퇴직금 이체분은 기간요건 없음)</td>
      <td style="border:1px solid #ddd;padding:10px;">3년</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:10px;">중도 인출·해지</td>
      <td style="border:1px solid #ddd;padding:10px;">법정 사유 외 인출 제한, 운용수익에 기타소득세 16.5%(부득이한 사유는 5.5%)</td>
      <td style="border:1px solid #ddd;padding:10px;">원금 범위 안 인출은 자유(과세 없음), 원금 초과 인출은 중도해지로 보아 전체 수익에 15.4% 과세</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #7c5fd1;padding-left:12px;margin-top:36px;">인출 조건과 중도해지 세금 차이</h2>

<p>IRP는 <b>연금으로 받는 것이 기본값</b>입니다. 무주택자의 주택구입, 전세보증금 마련, 6개월 이상 요양 등 법정 사유에 해당해야만 중도인출이 가능하고, 그 외에는 55세가 될 때까지 사실상 묶입니다. 자세한 인출 사유별 세금은 70편(퇴직연금 중도인출 세금)에서 원 단위 계산 예시와 함께 정리했습니다.</p>

<p>ISA는 반대로 <b>원금 범위 안에서는 언제든 인출해도 불이익이 없습니다.</b> 문제는 원금을 초과해서 뺄 때입니다. 이 경우 세법상 중도해지로 간주되어, 3년을 채우지 못하면 비과세·분리과세 혜택이 사라지고 수익 전체에 15.4% 일반과세가 붙습니다. 단, 사망·해외이주 등 특별중도해지 사유에 해당하면 그 시점까지의 혜택은 유지됩니다. 이 계산 예시는 67편(ISA 중도해지 세금)에 있습니다.</p>

<h2 style="border-left:6px solid #7c5fd1;padding-left:12px;margin-top:36px;">ISA 만기자금 IRP로 옮기면 세액공제가 늘어나나요</h2>

<p>늘어납니다. ISA 만기자금 3,000만원을 IRP나 연금저축으로 옮기면 이전금액의 10%인 300만원이 그해 세액공제 한도에 추가로 더해집니다. 900만원 한도를 이미 채운 상태에서 300만원이 더 생기면, 공제율에 따라 <mark>495,000원(16.5%)</mark> 또는 396,000원(13.2%)을 추가로 돌려받을 수 있습니다.</p>

<ul style="line-height:1.9;">
  <li>추가 공제받을 금액은 안전자산 운용이 원칙인 IRP로 이전</li>
  <li>당장 쓸 가능성이 있는 여유 자금은 인출이 비교적 자유로운 연금저축으로 이전</li>
  <li>이전은 ISA 만기일 이후 일정 기간 안에 마쳐야 하며, 구체적인 절차는 8편에서 확인</li>
</ul>

<h2 style="border-left:6px solid #7c5fd1;padding-left:12px;margin-top:36px;">두 계좌를 함께 쓰면 한도가 어떻게 되나요</h2>

<p>IRP 세액공제 한도(900만원)와 ISA 납입한도(연 2,000만원)는 서로 다른 제도라 겹치지 않습니다. ISA에 2,000만원을 넣으면서 동시에 IRP·연금저축에 900만원을 넣어 세액공제를 받는 것도 가능합니다. 다만 현금 여력이 한정돼 있다면 어느 쪽을 먼저 채울지는 각자의 자금 계획에 달려 있습니다.</p>

<div style="background:#fff7ed;border:2px solid #d97706;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#92400e;font-size:18px;">🔑 다시 정리하면</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>IRP는 세액공제(최대 900만원)가 강점이지만 55세까지 인출이 제한됩니다.</li>
    <li>ISA는 원금 범위 안 인출이 자유롭고 초과분만 9.9%로 저율 과세됩니다.</li>
    <li>ISA 만기자금을 연금계좌로 옮기면 세액공제 한도를 최대 300만원 더 늘릴 수 있습니다.</li>
  </ul>
</div>

<h3>Q. IRP와 ISA 중 하나만 가입해도 되나요?</h3>
<p>A. 목적이 달라 함께 쓰는 경우가 많습니다. IRP는 세액공제와 노후 자금 마련에, ISA는 비과세 혜택과 자금 유동성 확보에 각각 초점이 맞춰져 있습니다.</p>

<h3>Q. ISA 만기자금을 IRP로 꼭 옮겨야 하나요?</h3>
<p>A. 의무는 아닙니다. 옮기지 않고 그대로 인출해도 ISA 자체의 비과세·분리과세 혜택은 이미 적용된 상태입니다. 옮기면 세액공제 한도가 늘어나는 것뿐입니다.</p>

<h3>Q. IRP에 넣은 돈을 55세 전에 뺄 수 있나요?</h3>
<p>A. 무주택자 주택구입, 전세보증금 마련, 6개월 이상 요양 등 법정 사유에 해당할 때만 가능하며, 사유 충족 여부에 따라 세금이 달라집니다.</p>

<h3>Q. ISA를 3년 전에 해지하면 무조건 손해인가요?</h3>
<p>A. 납입 원금 범위 안에서 인출하는 것은 해지가 아니라 손해가 없습니다. 원금을 초과해 인출할 때만 중도해지로 보아 비과세·분리과세 혜택이 사라집니다.</p>

<h3>Q. 세액공제는 IRP와 연금저축 중 어디에 넣어도 똑같나요?</h3>
<p>A. 합산 한도(900만원) 안에서는 공제 금액이 같습니다. 그런데 IRP는 예금·보험 등 안전자산 비중 규제가 있어 상품 구성 방식이 연금저축과 다릅니다.</p>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처 (2026년 9월 기준):
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7875&amp;mi=6439" target="_blank" rel="noopener">국세청 - 근로소득 연금계좌 세액공제</a></li>
    <li><a href="https://www.fsc.go.kr/po020201/27339" target="_blank" rel="noopener">금융위원회 - ISA(개인종합자산관리계좌) 주요정책문답</a></li>
    <li><a href="https://www.kcie.or.kr" target="_blank" rel="noopener">금융투자자보호재단 - 퇴직연금 수령 안내</a></li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 IRP·ISA 두 계좌의 제도 차이를 설명하는 정보 제공용 글이며, 특정 금융상품이나 계좌 가입을 권하지 않습니다. 어느 계좌에 얼마를 넣을지는 개인 상황에 따라 다르므로 그 판단과 결과는 가입자 본인의 몫입니다. 세액공제·한도·세율은 법 개정으로 달라질 수 있어, 실제 신청 전 반드시 원출처에서 최신 내용을 다시 확인해야 합니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "IRP ISA 차이 세액공제 인출조건 비교",
  "description": "IRP와 ISA의 세액공제 구조, 인출 조건, 중도해지 시 세금 차이를 비교표와 계산 예시로 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-23",
  "dateModified": "2026-09-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensitiveboss3.tistory.com/entry/irp-isa-account-difference" }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "IRP와 ISA 중 하나만 가입해도 되나요?",
      "acceptedAnswer": { "@type": "Answer", "text": "목적이 달라 함께 쓰는 경우가 많습니다. IRP는 세액공제와 노후 자금 마련에, ISA는 비과세 혜택과 자금 유동성 확보에 각각 초점이 맞춰져 있습니다." }
    },
    {
      "@type": "Question",
      "name": "ISA 만기자금을 IRP로 꼭 옮겨야 하나요?",
      "acceptedAnswer": { "@type": "Answer", "text": "의무는 아닙니다. 옮기지 않고 그대로 인출해도 ISA 자체의 비과세·분리과세 혜택은 이미 적용된 상태입니다. 옮기면 세액공제 한도가 늘어나는 것뿐입니다." }
    },
    {
      "@type": "Question",
      "name": "IRP에 넣은 돈을 55세 전에 뺄 수 있나요?",
      "acceptedAnswer": { "@type": "Answer", "text": "무주택자 주택구입, 전세보증금 마련, 6개월 이상 요양 등 법정 사유에 해당할 때만 가능하며, 사유 충족 여부에 따라 세금이 달라집니다." }
    },
    {
      "@type": "Question",
      "name": "ISA를 3년 전에 해지하면 무조건 손해인가요?",
      "acceptedAnswer": { "@type": "Answer", "text": "납입 원금 범위 안에서 인출하는 것은 해지가 아니라 손해가 없습니다. 원금을 초과해 인출할 때만 중도해지로 보아 비과세·분리과세 혜택이 사라집니다." }
    },
    {
      "@type": "Question",
      "name": "세액공제는 IRP와 연금저축 중 어디에 넣어도 똑같나요?",
      "acceptedAnswer": { "@type": "Answer", "text": "합산 한도(900만원) 안에서는 공제 금액이 같습니다. 그런데 IRP는 예금·보험 등 안전자산 비중 규제가 있어 상품 구성 방식이 연금저축과 다릅니다." }
    }
  ]
}
</script>
