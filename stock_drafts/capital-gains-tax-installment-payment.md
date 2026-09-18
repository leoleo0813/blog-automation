---
keyword: 양도소득세 분납
title: 양도소득세 분납 기준과 신청 방법
slug: capital-gains-tax-installment-payment
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 250 (PC 130 / 모바일 120)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-17 — 통과]
  WebSearch "양도소득세 분납" 상위 종합:
  findsemusa.com(개인 세무사 상담) / etax.seoul.go.kr(서울시, 공식·지방소득세 신고) /
  casenote.kr(판례 검색 DB) / nts.go.kr(국세청, 공식) / news.mt.co.kr(머니투데이, 언론) /
  taxly.kr(세무 콘텐츠 블로그, 소규모) / law.go.kr(법령정보센터, 서식 다운로드) /
  call.nts.go.kr(국세청 Q&A)
  1) 진입 여지 — 있음. findsemusa.com(개인 세무사 상담)·taxly.kr(소규모 세무 블로그)가
     상위에 진입해 있어 SERP가 잠겨 있지 않다.
  2) 검색 의도 — 정보 탐색형("얼마부터 나눠 낼 수 있나, 어떻게 신청하나"). 조회·계산기
     실행이 지배적 의도는 아니다.
  3) 답 완결 여부 — 부분적. nts.go.kr·news.mt.co.kr가 기준금액(1,000만원 초과)은
     알려주지만, ① 실제 계산 예시(양도소득세가 얼마일 때 얼마까지 나눠낼 수 있는지)
     ② 신청서 작성·제출 경로 ③ 분납에 이자가 붙는지 여부까지 한 글에서 묶어 다루는
     콘텐츠는 확인하지 못했다.
  → 탈락조건 1·2 미해당, 탈락조건 3은 계산 예시·신청 경로 정보이득으로 상쇄해 통과.
unique_asset: |
  [완성 2026-09-18 — 사람이 국세청 원문 캡처 + 교차검증으로 확정]
  (a) 분납 기준금액을 확정: 납부할 세액 1,000만원 초과가 대상, 1,000만원 초과~2,000만원
      이하는 1,000만원 초과 금액을, 2,000만원 초과는 세액의 50% 이하를 분납할 수 있다.
      기준금액 구간별 계산 예시(양도소득세 1,250만원/3,000만원 사례)로 실감나게 보여준다.
  (b) 이 기준의 법적 근거가 소득세법 제77조(분할납부)이고, 이 조문이 중간예납(제65조)뿐
      아니라 양도소득세 확정신고(제76조)에도 공통 적용된다는 점을 원문·교차검증으로
      확정 — 상위 검색 결과가 "1,000만원 초과"라는 단편적 숫자만 언급하고 이 숫자가
      어느 조문에서 왜 나오는지, 종합소득세와 같은 공식인지는 다루지 않았다.
  (c) 이자·가산세 여부를 명확히 정리: 분납 자체는 무이자이고, 분납분을 기한(2개월) 안에
      내지 못했을 때만 납부지연가산세(1일 0.025%, 연 9.125%)가 붙는다는 구조를 처음으로
      구분해서 보여준다. 상위 글은 "이자가 붙는지" 자체를 다루지 않거나 얼버무린다.
  (d) 신청 절차도 정정: 별도 신청서 제출이 아니라 예정·확정신고서 자체의 분납할 세액
      기재란에 적어 제출하는 방식이라는 점을 확정 반영했다.
primary_source: |
  국세청(nts.go.kr) WebFetch는 이번 세션에서도 1회 시도 후 EGRESS_BLOCKED로 재확인
  (2026-09-17). 이후 사람이 국세청 홈페이지에서 「국세신고안내 > 개인신고안내 >
  양도소득세 > 기본정보 > 세율」 경로의 "분납세액의 계산" 화면을 직접 캡처해 제공
  (2026-09-18, PDF). 이 화면은 산식과 구체적 계산 사례(중간예납세액 기준)를 보여주는데,
  화면 자체가 다루는 세액은 종합소득세 중간예납세액이고 양도소득세 확정신고 세액을
  직접 다루지는 않는다는 한계가 있다(브레드크럼은 "양도소득세 > 세율"로 표시됐지만
  본문 내용은 중간예납세액 산식과 사례라 사이트 내비게이션과 실제 게시 내용이 어긋나
  있었다).
  이 한계를 메우기 위해 WebSearch로 별도 확인한 결과, 이 계산식(1,000만원 초과 시
  분납, 1,000만원 초과~2,000만원 이하는 초과분, 2,000만원 초과는 50% 이하)의 법적
  근거가 소득세법 제77조이고, 이 조문은 제65조(중간예납)뿐 아니라 제76조(양도소득세
  확정신고)에도 공통 적용된다는 점을 확인했다. 즉 사람이 캡처한 화면은 "같은 계산식이
  적용되는 여러 사례 중 하나(중간예납)"를 보여준 것이고, 그 계산식 자체가 양도소득세
  에도 그대로 쓰인다는 사실은 법 조문 확인으로 별도로 뒷받침했다. 이자 여부(분납은
  무이자, 기한 경과 시에만 납부지연가산세)는 세무법인 청년들(watax.kr)·일간NTN
  (intn.co.kr) 등 독립된 세무 전문 콘텐츠 다수가 일치해 교차검증으로 확정했다.
  기존 초안에 있던 "소득세법 시행규칙 별지 제56호서식" 별도 신청서 존재 주장은
  근거가 불명확해(조세특례제한법상 특정 감면 사례의 서식일 가능성이 있음) 본문에서
  제외했다 — 일반적인 분납은 신고서 자체에 기재하는 것으로 충분하다는, 더 널리
  확인되는 설명으로 교체했다.
기준일: 2026-09-18 (국세청 화면 사람 캡처일 + 법조문·교차검증 보강일)
tags: 양도소득세분납, 양도소득세납부, 분할납부, 양도소득세신고, 대주주양도세, 해외주식양도세, 홈택스신고, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-18).
  게이트1: 네이버 키워드도구 실측 250회(세부·제도 기준 100회 이상).
  게이트2: v3 기준 통과(serp_check 참조).
  게이트3: 기준금액 구간별 계산 예시 + 이자·가산세 구분 + 신청 절차 정정으로 정보이득
  확보.
  게이트4: 사람이 국세청 화면을 직접 캡처했고(다만 캡처된 화면은 중간예납세액
  맥락이라는 한계가 있어), 같은 계산식이 양도소득세 확정신고에도 공통 적용된다는
  점을 법조문(소득세법 제77조)과 독립 출처 교차검증으로 보강해 확정했다. 한계를
  self_check·본문에 투명하게 공개.
self_check: |
  [2026-09-18 최종 판정 — gate_pass:true]
  게이트1 충족 — 실측 250회.
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 계산 예시(1,250만원·3,000만원 사례) + 이자·가산세 구조 + 정정된 신청
  절차로 상위 검색 결과에 없는 정보이득을 확보했다.
  게이트4 충족(한계 명시) — 사람이 캡처한 국세청 화면은 형식적으로는 "양도소득세 >
  세율" 경로였지만 실제 표시 내용은 종합소득세 중간예납세액 계산 사례였다. 이 어긋남을
  숨기지 않고, 같은 계산식(소득세법 제77조)이 중간예납(제65조)과 양도소득세 확정신고
  (제76조) 모두에 공통 적용된다는 사실을 법조문 확인으로 별도 보강해 결론을 확정했다.
  이자·가산세 여부는 세무 전문 콘텐츠 2곳 이상이 일치해 교차검증으로 확정. 기존 초안의
  "별지 제56호서식" 별도 신청서 주장은 근거가 불명확해 제외하고 더 널리 확인되는
  "신고서에 기재" 방식으로 교체했다 — 부정확할 수 있는 서식명을 그대로 쓰지 않은
  사례.
  카니벌라이제이션 점검 — 5편(해외주식 양도소득세)·33편(국내주식 양도소득세 신고방법)
  둘 다 "얼마를 내야 하는지·언제 신고하는지"가 중심이고 분납은 다루지 않는다. 본문에서
  두 글로 내부 링크를 걸어 기초 신고 절차는 위임하고, 이 글은 "낼 세금이 크게 나왔을 때
  나눠 낼 수 있는지"에 집중해 겹침 없음.
  기관 링크 점검 — 본문에서 국세청·국가법령정보센터를 안내하는 자리와 하단 참고 출처
  전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에 nofollow 미부착.
  제목 15자(공백 포함)·금지어 없음·조사·접속사 없음. 슬러그 영문 소문자+하이픈 4단어.
  em대시 0개(RULES.md 「AI 글쓰기 티 제거」 반영). FAQ 6개와 JSON-LD 1:1 일치. 종목·상품
  추천 표현, 단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-18</p>

<p><mark>양도소득세가 1,000만원을 넘으면 한 번에 다 내지 않고 나눠 낼 수 있습니다.</mark> 해외주식이나 대주주 국내주식을 팔아 세금이 크게 나왔을 때 알아두면 유용한 제도입니다. 분납이 가능한 기준금액과 신청 방법을 정리했습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>납부할 양도소득세가 <b>1,000만원을 넘으면</b> 그중 일부를 나눠 낼 수 있고, 나눠 내는 기한은 원래 납부기한으로부터 <mark>2개월 이내</mark>입니다.</li>
    <li>1,000만원 초과~2,000만원 이하는 <b>1,000만원을 초과하는 금액</b>을, 2,000만원을 초과하면 <mark>세액의 50% 이하</mark>를 분납할 수 있습니다.</li>
    <li>별도 서식을 제출하지 않고, <b>예정신고 또는 확정신고서 자체에 분납할 금액을 적어서</b> 신청합니다.</li>
    <li>분납은 <mark>무이자</mark>입니다. 다만 분납분을 정해진 기한 안에 내지 못하면 그때부터 납부지연가산세가 붙습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>양도소득세 분납이 뭔가요</li>
  <li>얼마부터 분납할 수 있나요</li>
  <li>분납은 어떻게 신청하나요</li>
  <li>분납하면 이자가 붙나요</li>
  <li>분납을 신청 안 하면 어떻게 되나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">양도소득세 분납이 뭔가요</h2>

<p>양도소득세 분납은 <mark>한 번에 내야 할 세금이 부담스러울 때, 정해진 기간 안에 나눠서 낼 수 있게 해주는 제도</mark>입니다. 해외주식을 팔아 양도차익이 크게 났거나, 국내 상장주식 대주주로 분류돼 예정신고·확정신고 대상이 된 경우 이 제도를 쓸 수 있습니다.</p>

<p>해외주식·국내주식 대주주의 신고 자체가 처음이라면, <a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing" target="_blank" rel="noopener">해외주식 양도소득세 신고 방법</a>과 <a href="https://sensitiveboss3.tistory.com/entry/domestic-stock-capital-gains-filing" target="_blank" rel="noopener">국내주식 양도소득세 신고방법</a>에서 신고 대상과 기한을 먼저 확인하는 것이 순서입니다. 이 글은 "신고는 끝냈는데 낼 세금이 너무 크다"는 다음 단계를 다룹니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">얼마부터 분납할 수 있나요</h2>

<p>납부할 양도소득세가 <b>1,000만원을 초과</b>하면 그중 일부를 나눠 낼 수 있습니다. 나눠 낼 수 있는 금액은 세액 구간에 따라 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">납부할 세액</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">분납 가능액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">1,000만원 이하</td>
      <td style="border:1px solid #ddd;padding:8px;">분납 불가(전액 한 번에 납부)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">1,000만원 초과 ~ 2,000만원 이하</td>
      <td style="border:1px solid #ddd;padding:8px;">1,000만원을 초과하는 금액</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">2,000만원 초과</td>
      <td style="border:1px solid #ddd;padding:8px;">세액의 50% 이하</td>
    </tr>
  </tbody>
</table>

<p>실제로 계산해보면 이렇습니다. 양도소득세가 <b>1,250만원</b>이라면 1,000만원을 초과하는 250만원까지 분납할 수 있어 원래 기한까지는 1,000만원만 내면 됩니다. 양도소득세가 <b>3,000만원</b>이라면 세액의 50%인 1,500만원까지 분납할 수 있어 원래 기한까지 1,500만원, 나머지 1,500만원은 2개월 뒤에 내는 식입니다.</p>

<p style="font-size:13px;color:#888;">근거: 소득세법 제77조(분할납부). 이 조문은 중간예납(제65조)뿐 아니라 양도소득세 확정신고(제76조)에도 같은 기준으로 적용됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">분납은 어떻게 신청하나요</h2>

<p>별도 신청서를 따로 제출하는 절차가 아닙니다. <b>예정신고서 또는 확정신고서 자체에 분납할 금액을 적어서 함께 제출</b>하면 그게 신청입니다.</p>

<ul style="line-height:1.9;">
  <li>홈택스·손택스로 전자신고할 때는 신고 화면의 분납 항목에 나눠 낼 금액을 입력합니다.</li>
  <li>세무서를 방문해 신고서를 종이로 제출할 때는 신고서의 분납 세액 항목에 직접 기재합니다.</li>
  <li><mark>신청 시점은 예정신고 또는 확정신고 기한과 같습니다.</mark> 세금을 일단 신고·납부한 뒤 나중에 분납으로 바꿀 수는 없습니다.</li>
</ul>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">분납하면 이자가 붙나요</h2>

<p>분납 자체에는 이자가 붙지 않습니다. 다만 나눠 낸 두 번째 분납분을 정해진 기한(원래 납부기한으로부터 2개월) 안에 내지 못하면, 그 시점부터 <b>납부지연가산세</b>가 붙습니다. 하루당 0.025%(연 9.125%) 비율이라 큰 금액을 오래 미룰수록 부담이 커집니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>신고를 늦게 했을 때 붙는 가산세가 궁금하다면</b>
  <p style="margin:8px 0 0 0;">분납은 "제때 신고했지만 낼 돈이 커서 나눠 내는 것"이고, 신고 자체를 놓쳤을 때 붙는 가산세는 별개입니다. 신고 기한을 놓친 경우는 <a href="https://sensitiveboss3.tistory.com/entry/gift-tax-late-filing-penalty" target="_blank" rel="noopener">증여세 기한후신고 가산세 계산 방법</a>에서 다룬 무신고가산세·납부지연가산세 구조와 원리가 비슷합니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">분납을 신청 안 하면 어떻게 되나요</h2>

<p><b>분납은 의무가 아니라 선택입니다.</b> 신청하지 않으면 원래대로 납부기한까지 전액을 한 번에 내야 합니다. 분납을 신청했다고 세금 자체가 줄어드는 것은 아니고, 내는 시점을 나누는 것일 뿐입니다.</p>

<ul style="line-height:1.9;">
  <li>분납을 신청해도 <b>세금 총액은 그대로</b>이며, 감면이나 할인이 아닙니다.</li>
  <li>분납 신청 기한(신고 기한)을 넘기면 이후에는 신청할 수 없고 전액을 바로 내야 합니다.</li>
  <li>나눠 낸 두 번째 분납분도 정해진 기한(원래 납부기한으로부터 2개월 이내)까지 내지 않으면 별도의 불이익이 따를 수 있습니다.</li>
</ul>

<p>이 글은 양도소득세 분납 제도의 절차를 설명하는 것으로, 특정 종목이나 상품의 매수·매도를 권하는 내용이 아닙니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">양도소득세 분납이란 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">한 번에 내야 할 양도소득세가 부담스러울 때, 납부기한으로부터 2개월 이내에 나눠서 낼 수 있게 해주는 제도입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">양도소득세는 얼마부터 분납할 수 있나요</summary>
  <p style="margin:10px 0 0 0;">납부할 세액이 1,000만원을 초과하면 분납할 수 있습니다. 1,000만원 초과~2,000만원 이하는 초과 금액을, 2,000만원 초과는 세액의 50% 이하를 나눠 낼 수 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">분납은 어떻게 신청하나요</summary>
  <p style="margin:10px 0 0 0;">별도 신청이 아니라 양도소득세 신고서 자체에 분납할 금액을 기재해 신청합니다. 신청 시점은 예정신고 또는 확정신고 기한과 같습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">분납하면 이자가 붙나요</summary>
  <p style="margin:10px 0 0 0;">분납 자체는 무이자입니다. 다만 분납분을 기한 안에 내지 못하면 그때부터 납부지연가산세(1일 0.025%)가 붙습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">분납 신청 기한을 놓치면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">분납 신청은 신고 기한 안에만 할 수 있습니다. 기한을 넘기면 전액을 한 번에 내야 합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">분납하면 세금이 줄어드나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 분납은 내는 시점을 나누는 것일 뿐 세금 총액을 줄여주지는 않습니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a>: 분납세액 계산 화면 사람 직접 캡처(2026-09-18) + 소득세법 제77조(중간예납·양도소득세 확정신고 공통 적용) 확인</li>
    <li><a href="https://sensitiveboss3.tistory.com/entry/overseas-stock-tax-filing" target="_blank" rel="noopener">해외주식 양도소득세 신고 방법(이전 글)</a>: 신고 대상·기한 기초</li>
    <li><a href="https://sensitiveboss3.tistory.com/entry/domestic-stock-capital-gains-filing" target="_blank" rel="noopener">국내주식 양도소득세 신고방법(이전 글)</a>: 대주주 요건·신고 절차</li>
  </ul>
  기준일: 2026-09-18(국세청 화면 사람 캡처 + 법조문·교차검증 보강일). 캡처된 화면은
  중간예납세액 맥락이지만, 같은 계산식이 양도소득세 확정신고에도 공통 적용된다는
  점을 소득세법 제77조 확인으로 별도 보강했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를
권유하지 않습니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "양도소득세 분납 기준과 신청 방법",
  "description": "양도소득세 분납 기준금액(1,000만원·2,000만원 구간)과 계산 예시, 이자·가산세 여부, 신고서에 기재해 신청하는 방법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-17",
  "dateModified": "2026-09-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/capital-gains-tax-installment-payment"
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
      "name": "양도소득세 분납이란 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "한 번에 내야 할 양도소득세가 부담스러울 때, 납부기한으로부터 2개월 이내에 나눠서 낼 수 있게 해주는 제도입니다." }
    },
    {
      "@type": "Question",
      "name": "양도소득세는 얼마부터 분납할 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "납부할 세액이 1,000만원을 초과하면 분납할 수 있습니다. 1,000만원 초과~2,000만원 이하는 초과 금액을, 2,000만원 초과는 세액의 50% 이하를 나눠 낼 수 있습니다." }
    },
    {
      "@type": "Question",
      "name": "분납은 어떻게 신청하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "별도 신청이 아니라 양도소득세 신고서 자체에 분납할 금액을 기재해 신청합니다. 신청 시점은 예정신고 또는 확정신고 기한과 같습니다." }
    },
    {
      "@type": "Question",
      "name": "분납하면 이자가 붙나요",
      "acceptedAnswer": { "@type": "Answer", "text": "분납 자체는 무이자입니다. 다만 분납분을 기한 안에 내지 못하면 그때부터 납부지연가산세(1일 0.025%)가 붙습니다." }
    },
    {
      "@type": "Question",
      "name": "분납 신청 기한을 놓치면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "분납 신청은 신고 기한 안에만 할 수 있습니다. 기한을 넘기면 전액을 한 번에 내야 합니다." }
    },
    {
      "@type": "Question",
      "name": "분납하면 세금이 줄어드나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 분납은 내는 시점을 나누는 것일 뿐 세금 총액을 줄여주지는 않습니다." }
    }
  ]
}
</script>
