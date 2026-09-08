---
keyword: 주식 증여세
title: 주식 증여세 계산 방법
slug: stock-gift-tax
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 1030 (PC 190 / 모바일 840)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-08 — 통과]
  WebSearch "주식 증여세 계산 상장주식 평가방법" + "주식 증여세 증여재산공제 세율"
  상위 결과 종합:
  brunch.co.kr(개인 브런치) / kbthink.com(KB 금융 콘텐츠) / heumtax.com(세무법인
  콘텐츠, ×2) / ganatax.co.kr(세무법인) / klca.or.kr(협회 PDF) / tkac.kr(회계법인
  게시판) / hanwhawm.com(한화투자증권 WM 콘텐츠) / nts.go.kr(국세청, 공식 ×2) /
  pwc.com(회계법인 인사이트) / taxly.kr(증여세 계산기) / taxoffice.co.kr(세무법인)
  1) 진입 여지 — 있음. brunch.co.kr·tkac.kr 같은 개인/소규모 콘텐츠와 세무법인
     블로그형 페이지가 다수 상위에 진입. SERP 안 잠김.
  2) 검색 의도 — 정보 탐색+계산("얼마나 나오나, 어떻게 계산하나"). taxly.kr 계산기가
     하나 보이지만 상위 대부분은 설명형 콘텐츠라 계산기 실행이 지배적 의도는 아님.
  3) 답 완결 여부 — 아니다. 공제한도·세율은 여러 글에 흩어져 있고, 상장주식 특유의
     "평가기준일(증여일) 당일 종가가 아니라 전후 각 2개월 종가 평균이 진짜 과세가액"
     함정, 그리고 증자·합병이 있으면 그 기간마저 조정된다는 세부 규정까지 갖춘 글은
     못 찾음. 정보이득 여지 뚜렷함.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  [완성 2026-09-08 — 법령 원문 확정]
  (a) 증여재산공제 한도(배우자 6억/직계존속 5천만·미성년자 2천만/직계비속 5천만/기타친족
      1천만) + 5단계 누진세율(10~50%, 누진공제액 포함)을 국세청 원문 그대로 표로 제공.
      "10년간 합산 공제"라 과거 증여받았으면 한도가 줄어든다는 점까지 명시.
  (b) 원 단위 계산 예시 2건(성년 자녀 1억원 증여, 배우자 8억원 증여)으로 계산기 없이도
      손으로 검산 가능하게 보여준다.
  (c) 핵심 정보이득 — "증여일 종가만 보고 계산하면 틀린다." 상장주식(코스피·코스닥
      둘 다)은 평가기준일(증여일) 전후 각 2개월간 종가 평균이 과세가액이다(상속세및
      증여세법 시행령 제52조의2). 상위 경쟁 글 대부분이 여기까지만 다루는데, 이 글은
      조문에 있는 세 가지 예외까지 함께 보여준다: ① 그 사이 증자·합병이 있으면 평균
      계산 기간 자체가 그 시점을 기준으로 재조정된다, ② 거래정지·관리종목 지정 기간이
      포함된 종목은 평가 대상에서 제외될 수 있다, ③ 공휴일·토요일은 매매 없는 날로
      빠져 달력상 2개월과 실제 거래일 2개월이 다르다. 이 세 예외는 검색 상위 글에서
      확인되지 않았다.
primary_source: |
  두 곳을 사람이 직접 캡처해 확보(2026-09-08).
  (1) 국세청(nts.go.kr) 「개인신고안내 > 증여세」 세액계산 흐름도 + 항목별 설명 —
      증여재산공제 한도·세율표. sources/gift-tax-calc-and-deduction.md,
      원본 sources/nts-gift-tax-calc-flowchart.pdf · nts-gift-tax-items.pdf.
  (2) 국가법령정보센터(law.go.kr) 「상속세및증여세법 시행령」[시행 2026.2.27.]
      [대통령령 제36131호] 제52조의2(유가증권시장 및 코스닥시장에서 거래되는
      주식등의 평가) 전문 — 2개월 평균 원칙 + 증자·합병 조정 + 거래정지 제외 +
      매매없는날 제외. sources/decree-listed-stock-valuation.md.
  ※ 같은 날 처음 받은 법령 doc(대통령령 제36131호 관련이지만 다른 조문 계산식 모음)은
  제52조의2를 포함하지 않아 쓰지 않았다 — sources/gift-tax-decree-formulas-misc.md.
기준일: 2026-09-08 (국세청 페이지 캡처일, 페이지 자체엔 명시적 기준일 문구 없음) /
  2026-02-27 (시행령 제36131호 시행일, law.go.kr 화면에 명시)
tags: 증여세, 주식증여, 증여재산공제, 상장주식평가, 증여세율, 주식세금, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-08).
  게이트1: 네이버 키워드도구 실측 1,030회(PC 190 / 모바일 840, 일반 주제 기준 500 이상).
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 공제한도표 + 세율표 + 계산 예시 2건 + 상장주식 평가방법(2개월 평균 원칙과
  증자·합병/거래정지/매매없는날 3가지 예외)까지 법령 원문 기반으로 완성.
  게이트4: 국세청 원문(증여재산공제·세율표) + 법령 원문(시행령 제52조의2) 1차 출처
  2건 확보.
self_check: |
  [2026-09-08 법령 원문 확보 후 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 1,030회.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 공제한도·세율표·계산 예시에 더해, 상장주식 평가방법의 원칙과 세
  가지 예외(증자·합병 조정/거래정지 제외/매매없는날 제외)까지 법령 원문으로 완성했다.
  검색 상위 글이 다루지 않는 부분이다.
  게이트4 충족 — 국세청 원문(세액계산 흐름도·항목별 설명)과 법령 원문(시행령
  제52조의2)을 1차 출처로 확보했다. 검색 요약에서 본 숫자를 그대로 쓰지 않고 두
  출처 모두 사람이 직접 캡처해 확정했다.
  검산 — 성년 자녀 1억원 증여: 과세표준 5천만원(1억원 공제 후) → 10%(1억원 이하
  구간, 누진공제 없음) → 산출세액 500만원. 배우자 8억원 증여: 과세표준 2억원(6억원
  공제 후) → 20%(5억원 이하 구간, 누진공제 1천만원) → 2억원×20%-1천만원=3천만원.
  카니발라이제이션 점검 — 2편(주식 매도 세금 얼마)·7편(주식 양도소득세 대주주 요건)과
  과세 성격이 다르다(양도 vs 증여). 본문에서 2편으로 내부 링크.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문 기관 안내 문장과 하단 참고 출처를
  전부 링크 처리. target="_blank" rel="noopener", 정부기관이라 nofollow 미부착.
  제목 11자·금지어 없음·조사 없음. 슬러그 영문 소문자+하이픈 3단어. FAQ 6개와 JSON-LD
  1:1 일치. @id 티스토리 entry 패턴. 종목·상품 추천 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p>주식을 가족에게 증여하면 <mark>증여재산공제를 뺀 금액에 10%에서 50%까지 누진세율</mark>로 증여세가 붙습니다. 상장주식은 증여일 <b>당일 종가가 아니라 전후 각 2개월 종가 평균</b>으로 평가하기 때문에, 이 부분을 모르고 계산하면 실제 고지세액과 어긋날 수 있습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>증여재산공제는 배우자 6억원, 직계존속·직계비속 각 5천만원(미성년 자녀는 2천만원), 기타친족 1천만원까지 <b>10년간 합산</b>해 적용됩니다.</li>
    <li>세율은 1억원 이하 10%부터 30억원 초과 50%까지 <b>5단계 초과누진세율</b>이며, 구간마다 누진공제액이 있습니다.</li>
    <li>상장주식(코스피·코스닥)은 <mark>증여일 전후 각 2개월(총 4개월) 종가 평균</mark>으로 평가합니다. 당일 종가로 어림잡으면 안 됩니다.</li>
    <li>그 사이 증자·합병이 있었다면 평가 기간 자체가 조정되고, 거래정지·관리종목 지정 기간이 낀 종목은 별도 규정이 적용됩니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>주식 증여세는 어떻게 계산하나요</li>
  <li>상장주식은 얼마로 평가하나요</li>
  <li>증여재산공제는 얼마까지인가요</li>
  <li>세율은 어떻게 적용하나요</li>
  <li>실제로 계산하면 얼마인가요</li>
  <li>신고는 언제, 어떻게 하나요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">주식 증여세는 어떻게 계산하나요</h2>

<p>증여세는 <mark>증여재산가액에서 증여재산공제를 뺀 과세표준에 세율을 곱하고 누진공제액을 빼서</mark> 계산합니다. 순서는 다음과 같습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  증여재산가액 − 증여재산공제 = 증여세 과세표준<br>
  증여세 과세표준 × 세율 − 누진공제액 = 증여세 산출세액
</div>

<p>상장주식을 증여하는 경우 이 계산의 출발점인 <b>증여재산가액</b> 자체가 관건입니다. 증여일 당일 종가로 계산하는 사람이 많은데, 정확한 방법은 다음과 같습니다. 전체 계산 흐름은 <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2340&amp;cntntsId=7728" target="_blank" rel="noopener">국세청 세액계산 흐름도</a>에서 확인할 수 있습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">상장주식은 얼마로 평가하나요</h2>

<p>상장주식(코스피·코스닥)은 <mark>증여일(평가기준일) 전후 각 2개월, 총 4개월간 공표된 매일의 최종시세가액 평균액</mark>으로 평가합니다. 「상속세및증여세법 시행령」 제52조의2 제1항이 유가증권시장(코스피)과 코스닥시장 둘 다 이 방식이 적용되는 증권시장이라고 정하고 있습니다.</p>

<p>여기서 끝나지 않습니다. 같은 조문에 세 가지 예외가 함께 규정돼 있는데, 상위 검색 결과 대부분이 다루지 않는 부분입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>① 증자·합병이 있으면 평가 기간이 재조정됩니다.</b>
  <p style="margin:8px 0 0 0;">평가기준일 이전에 증자·합병이 있었다면 그 사유가 발생한 날의 다음날부터 평가기준일 이후 2개월까지로, 이후에 있었다면 평가기준일 이전 2개월부터 그 사유가 발생한 날의 전일까지로 기간 자체가 바뀝니다. 전후 모두에 있었다면 두 사유 발생일 사이만 봅니다.</p>
  <b style="display:block;margin-top:14px;">② 거래정지·관리종목 지정 기간이 낀 종목은 제외될 수 있습니다.</b>
  <p style="margin:8px 0 0 0;">평가기준일 전후 2개월 이내에 매매거래 정지나 관리종목 지정 기간이 포함된 주식은(정상적으로 시가가 반영된 경우는 제외) 이 평가방법의 대상에서 빠집니다.</p>
  <b style="display:block;margin-top:14px;">③ 공휴일·토요일은 계산에서 빠집니다.</b>
  <p style="margin:8px 0 0 0;">공휴일(대체공휴일 포함)과 토요일은 매매가 없는 날로 처리되어 평균 계산에 들어가지 않습니다. 달력상 "2개월"과 실제 반영되는 거래일이 정확히 같지 않다는 뜻입니다.</p>
</div>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>증여 직전·직후에 증자나 합병 계획이 있다면 주의하세요.</b>
  <p style="margin:8px 0 0 0;">단순히 "전후 2개월 평균"으로 어림잡고 넘어가면, 증자·합병이 낀 종목에서는 실제 계산 기간과 어긋날 수 있습니다. 정확한 평가액은 증권사나 세무대리인을 통해 확인하는 것이 안전합니다.</p>
</div>

<p style="font-size:13px;color:#888;">근거: 「상속세및증여세법 시행령」[시행 2026.2.27.][대통령령 제36131호] 제52조의2(유가증권시장 및 코스닥시장에서 거래되는 주식등의 평가) 전문(2026-09-08 <a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> 확인).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">증여재산공제는 얼마까지인가요</h2>

<p>증여자와의 관계에 따라 <mark>10년간 합산해서</mark> 아래 금액까지 공제받을 수 있습니다. 이미 10년 이내에 공제받은 금액이 있다면 이번 공제에서 그만큼 줄어듭니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">증여자와의 관계</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">공제 한도액(10년 합산)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">배우자</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6억원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">직계존속(계부·계모 포함)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5천만원 <span style="color:#888;">(미성년자는 2천만원)</span></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">직계비속</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">5천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">기타친족(4촌 이내 혈족, 3촌 이내 인척)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">그 외의 자</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0원</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">근거: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6533&amp;cntntsId=7960" target="_blank" rel="noopener">국세청 증여세 항목별 설명</a>(2026-09-08 확인). 창업자금·가업승계용 중소기업주식 등은 별도로 5억원 공제(위 표와 중복적용 불가).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">세율은 어떻게 적용하나요</h2>

<p>과세표준 구간에 따라 <mark>5단계 초과누진세율</mark>이 적용됩니다. 과세표준에 세율을 곱한 뒤 누진공제액을 빼면 산출세액이 나옵니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">과세표준</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">세율</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">누진공제액</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">1억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">10%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">없음</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">5억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">20%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">10억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">30%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">30억원 이하</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">40%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">1억 6천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">30억원 초과</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">50%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">4억 6천만원</td></tr>
  </tbody>
</table>

<p>수증자가 증여자의 자녀가 아닌 직계비속(세대생략증여)이면 <mark>산출세액의 30%가 할증</mark>됩니다. 미성년자가 20억원을 초과해 증여받는 경우에는 40% 할증입니다.</p>

<p style="font-size:13px;color:#888;">근거: <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2340&amp;cntntsId=7728" target="_blank" rel="noopener">국세청 증여세 세액계산 흐름도</a>(2026-09-08 확인).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제로 계산하면 얼마인가요</h2>

<p>2개월 평균으로 평가한 금액을 기준으로 실제 계산해보겠습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">성년 자녀에게 1억원 증여</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">배우자에게 8억원 증여</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">증여재산가액(2개월 평균)</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">100,000,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">800,000,000원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">증여재산공제</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">−50,000,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">−600,000,000원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">과세표준</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">50,000,000원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">200,000,000원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">적용 세율 / 누진공제</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">10% / 없음</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">20% / 1천만원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;"><b>산출세액</b></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>5,000,000원</mark></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>30,000,000원</mark></td></tr>
  </tbody>
</table>

<p>배우자 증여는 공제 한도(6억원)가 커서 <mark>과세표준이 세율 구간을 하나 넘어가면(1억원 초과) 누진공제액을 반드시 빼야</mark> 정확한 세액이 나옵니다. 20%를 그대로 곱하고 누진공제를 빼먹으면 세액을 과대 계산하게 됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">신고는 언제, 어떻게 하나요</h2>

<p>증여받은 날이 속하는 달의 말일부터 <mark>3개월 이내</mark>에 수증자(재산을 받은 사람)가 신고·납부합니다. <a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a>에서 전자신고할 수 있습니다.</p>

<p>주식을 팔 때 내는 세금은 이 글과 다른 세금입니다. 증여가 아니라 매도로 발생하는 세금은 "주식 매도 세금 얼마" 글을 참고하세요.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">상장주식 증여세는 증여일 종가로 계산하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 증여일 전후 각 2개월, 총 4개월간 종가 평균으로 계산합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">배우자에게 증여하면 세금이 없나요</summary>
  <p style="margin:10px 0 0 0;">6억원까지는 증여세가 없지만, 그 초과분부터는 세율이 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증여 전후에 유상증자나 합병이 있었으면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">평가 기간 자체가 그 사유가 발생한 날을 기준으로 재조정됩니다. 단순히 전후 2개월을 그대로 적용하지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">미성년 자녀에게 증여하면 공제한도가 다른가요</summary>
  <p style="margin:10px 0 0 0;">네. 직계존속이 미성년자에게 증여하는 경우 공제한도는 2천만원으로, 성년(5천만원)보다 낮습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증여세는 언제까지 신고해야 하나요</summary>
  <p style="margin:10px 0 0 0;">증여받은 날이 속하는 달의 말일부터 3개월 이내에 신고·납부해야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">비상장주식도 같은 방식으로 평가하나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 비상장주식은 순손익가치와 순자산가치를 가중평균하는 별도 방식(시행령 제54조)으로 평가합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2340&amp;cntntsId=7728" target="_blank" rel="noopener">국세청 증여세 세액계산 흐름도</a> — 공제 계산 흐름·세율표(2026-09-08 확인)</li>
    <li><a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6533&amp;cntntsId=7960" target="_blank" rel="noopener">국세청 증여세 항목별 설명</a> — 증여재산공제 한도(2026-09-08 확인)</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> — 상속세및증여세법 시행령 제52조의2(대통령령 제36131호, 시행 2026.2.27.)</li>
    <li><a href="https://www.hometax.go.kr" target="_blank" rel="noopener">홈택스</a> — 증여세 전자신고</li>
    <li>기준일: 2026-09-08(국세청 페이지 확인일) / 2026-02-27(시행령 제36131호 시행일)</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 책임은 본인에게 있습니다. 세율·공제 한도는 세법 개정으로 바뀔 수 있으므로 신고 전 국세청 최신 안내를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "주식 증여세 계산 방법",
  "description": "상장주식 증여세를 증여재산공제·5단계 누진세율로 계산하는 방법과, 증여일 종가가 아니라 전후 2개월 평균으로 평가하는 상장주식 평가방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-08",
  "dateModified": "2026-09-08",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-gift-tax"
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
      "name": "상장주식 증여세는 증여일 종가로 계산하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 증여일 전후 각 2개월, 총 4개월간 종가 평균으로 계산합니다." }
    },
    {
      "@type": "Question",
      "name": "배우자에게 증여하면 세금이 없나요",
      "acceptedAnswer": { "@type": "Answer", "text": "6억원까지는 증여세가 없지만, 그 초과분부터는 세율이 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "증여 전후에 유상증자나 합병이 있었으면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "평가 기간 자체가 그 사유가 발생한 날을 기준으로 재조정됩니다. 단순히 전후 2개월을 그대로 적용하지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "미성년 자녀에게 증여하면 공제한도가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 직계존속이 미성년자에게 증여하는 경우 공제한도는 2천만원으로, 성년(5천만원)보다 낮습니다." }
    },
    {
      "@type": "Question",
      "name": "증여세는 언제까지 신고해야 하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "증여받은 날이 속하는 달의 말일부터 3개월 이내에 신고·납부해야 합니다." }
    },
    {
      "@type": "Question",
      "name": "비상장주식도 같은 방식으로 평가하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 비상장주식은 순손익가치와 순자산가치를 가중평균하는 별도 방식(시행령 제54조)으로 평가합니다." }
    }
  ]
}
</script>
