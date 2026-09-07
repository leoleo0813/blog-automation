---
keyword: ETF 수수료
title: ETF 수수료 총보수 실부담 확인법
slug: etf-fee-comparison
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 확인필요
gate1_pass: 확인필요 (큐 참고값 월 890 — 커밋 후 워크플로가 네이버 API로 실측 기입)
serp_check: |
  [게이트2 v3 판정 2026-09-07 — 통과]
  WebSearch "ETF 수수료 총보수" 상위 7개:
  alphasquare.co.kr(알파스퀘어, 핀테크 콘텐츠) / brunch.co.kr(브런치 개인 글) /
  v.daum.net(언론) / hankyung.com(한국경제, 언론) / open.shinhansec.com(신한투자증권 가이드) /
  etflove.com(ETF사랑, 개인 블로그) / a-ha.io(아하, Q&A 커뮤니티)
  1) 진입 여지 — 있음. 브런치 개인 글, etflove.com 개인 블로그, 아하 커뮤니티까지
     개인·커뮤니티 콘텐츠가 셋이나 상위에 있다. 이 시리즈 중 SERP가 가장 안 잠긴 키워드다.
  2) 검색 의도 — 정보 탐색("수수료가 얼마고 어디서 보나"). 조회·신청·계산기 실행 아님.
     ※ 단, "확인 방법"을 찾는 의도가 섞여 있어 조회 화면 캡처가 그대로 정보이득이 된다.
  3) 답 완결 여부 — 아니다. 총보수만 설명하고 끝내는 글이 많고, 실부담비용(총보수 +
     기타비용 + 매매중개수수료)까지 짚는 글은 상대적으로 적다. 어디서 그 숫자를 보는지
     조회 경로를 화면으로 보여주는 글은 더 적다.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  핵심 정보이득은 "표시된 총보수가 실제로 내는 전부가 아니다"라는 점과, 그 실부담을
  직접 확인하는 경로를 화면 캡처로 보여주는 것이다. ETF 상품 페이지에 크게 적힌 총보수
  옆에 기타비용과 매매·중개수수료가 따로 붙어, 합산하면 표시 총보수보다 커진다.
  여기에 (a) 총보수 / 합성총보수(TER) / 실부담비용 용어 구분, (b) 금융투자협회
  전자공시에서 실제로 조회하는 절차, (c) 보수 차이가 장기 수익에 미치는 영향을 넣는다.
  ※ 실제 수치와 조회 화면은 사람 캡처가 필요하다(capture_guide 참조).
primary_source: 미확보 — RULES.md「1차 출처 접근」에 dis.kofia.or.kr(금융투자협회 전자공시)은 JS 앱이라 렌더링해도 수치가 나오지 않는다고 이미 기록돼 있어, 이번에는 WebFetch를 시도하지 않고 곧바로 human-assisted/capture로 분류했다(불필요한 재시도로 시간·토큰을 쓰지 않는다는 RULES.md 방침). WebSearch 요약에 국내 ETF 평균 총보수율과 전체 비용 평균으로 보이는 숫자가 나오지만 검색엔진 합성 문장이라 본문에 쓰지 않았다.
기준일: 미확정 — 캡처한 공시 화면의 기준일자를 그대로 기입할 것
tags: ETF수수료, 총보수, 실부담비용, TER, ETF투자, 운용보수, 매매중개수수료, 주식초보, ETF비교
gate_pass: false
capture_guide: |
  왜 필요한가: 이 글의 정보이득이 "표시 총보수와 실제 부담이 다르다"를 실제 숫자와
  조회 화면으로 보여주는 것인데, 금융투자협회 전자공시(dis.kofia.or.kr)는 자바스크립트
  앱이라 자동화가 열어도 화면에 수치가 나오지 않습니다(RULES.md에 이미 기록된 사항이라
  이번에는 시도하지 않았습니다). 사람이 직접 조회한 화면이 필요합니다.

  1순위 — 금융투자협회 전자공시서비스: https://dis.kofia.or.kr 접속 →
  「펀드공시」 > 「펀드별 보수비용비교」 메뉴로 이동 → 유형을 ETF로 선택해 조회 →
  다음이 보이게 캡처해 주세요:
    (1) 아무 ETF 한두 종목의 **총보수**와 **기타비용**, **매매·중개수수료**가 각각
        따로 보이는 행 (이 세 항목이 나뉘어 보이는 것이 핵심입니다)
    (2) 있으면 **실부담비용(TER)** 또는 합계 열
    (3) 화면에 표시된 **기준일자**
  ※ 종목은 아무거나 괜찮습니다. 특정 상품을 추천하는 글이 아니라 "이렇게 확인한다"를
     보여주는 용도라, 가급적 널리 알려진 지수형 ETF 두어 개면 충분합니다.

  2순위 — 증권사 앱/HTS의 ETF 상세 화면: 보유 중이거나 관심 종목인 ETF의 상세 정보에서
  총보수가 표시된 화면을 캡처. 1순위 화면과 나란히 놓으면 "앱에 적힌 총보수 < 실제 부담"을
  바로 보여줄 수 있어 정보이득이 커집니다.

  3순위(있으면 좋음) — 운용사 홈페이지의 해당 ETF 상품 페이지에서 보수 항목이 적힌 부분.

  캡처 후: 스크린샷을 대화에 올려주시면 표와 비교 예시를 채우고 게이트를 재판정하겠습니다.
  캡처 이미지는 본문 이미지로도 함께 씁니다(RULES.md「이미지」— 직접 캡처 우선).
self_check: |
  게이트1 미확인 — monthly_search_volume 확인필요로 남김. 커밋 후 notify-repo-only.yml이
  네이버 키워드도구로 실측해 채운다(큐 참고값 890회는 추측해 쓰지 않았다).
  ※ 890회는 이 시리즈에서 가장 낮은 편이라, 실측값이 RULES.md 게이트1 기준(주식 월 500+)에
  못 미치면 gate_pass는 그 사유로도 false가 된다. 실측 결과를 보고 판단할 것.
  게이트2 충족 — RULES.md 게이트2 v3 기준 판정, 3개 탈락 조건 모두 미해당(serp_check 참조).
  브런치·개인 블로그·커뮤니티가 셋이나 상위에 있어 이 시리즈 중 진입 여지가 가장 크다.
  게이트3 부분 충족 — "표시 총보수 ≠ 실제 부담"이라는 구조와 용어 구분(총보수/합성총보수
  /실부담비용), 조회 경로 설명은 서술로 넣었으나, 실제 수치와 조회 화면 캡처가 없어
  비교표가 비어 있다. RULES.md「실측표 자리를 비워두면 false」에 해당한다.
  게이트4 미충족 — dis.kofia.or.kr은 RULES.md에 "JS 앱이라 렌더링해도 수치 없음 →
  human-assisted 캡처로 처리"로 이미 기록돼 있어 WebFetch를 시도조차 하지 않았다.
  막힐 것이 확인된 곳을 다시 두드려 시간·토큰을 쓰지 않는다는 방침을 따랐다.
  RULES.md「키워드 3분류」가 ETF 총보수를 human-assisted 예시로 직접 명시하고 있어,
  이 글은 애초에 캡처형으로 설계됐다. 큐 원안(자동화 가능/oneclick)이 잘못 잡혀 있었다.
  금지 사항 점검 — 특정 ETF 상품 추천으로 흐르지 않도록, 종목명 나열이나 "어떤 ETF가
  낫다"는 서술을 넣지 않고 "확인하는 방법"에만 집중했다. capture_guide에도 종목은
  아무거나 괜찮다고 명시했다.
  카니발라이제이션 점검 — 1편(증권사 수수료 비교)과 "수수료"만 겹치고 대상이 다르다.
  1편은 증권사가 거래마다 떼는 위탁수수료, 이 글은 상품이 매년 떼는 보수라 성격이 다르다.
  본문에서 1편으로 내부 링크를 건다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 본문 기관 안내 문장과 하단 참고 출처를
  전부 링크 처리. 금융투자협회 전자공시는 RULES.md URL 표에 있는 주소를 그대로 썼다.
  target="_blank" rel="noopener", 공공성 기관이라 nofollow 미부착.
  제목 16자·금지어 없음·조사 없음. 제목이 "비교"가 아니라 "확인법"이라 RULES.md의
  "비교 제목이면 비교표 필수" 규칙에 걸리지 않는다(큐 원안 제목 "ETF 수수료 비교"는
  캡처 전까지 비교표가 없어 절차형으로 바꿨다).
  슬러그는 큐에 등록된 etf-fee-comparison을 유지(이미 커밋된 썸네일·링크와의 일관성).
  FAQ 6개와 JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 하단 면책 문구 포함.
  종합 판정: 게이트3·4 미충족 → gate_pass:false. 캡처 후 재판정.
---

<p>ETF 수수료는 <mark>상품 페이지에 적힌 총보수가 전부가 아닙니다.</mark> 여기에 기타비용과 매매·중개수수료가 따로 붙어서, 실제로 부담하는 비용은 표시된 숫자보다 큽니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>ETF 비용은 사고팔 때 내는 게 아니라 <b>보유하는 동안 매일 조금씩</b> 빠져나갑니다.</li>
    <li>상품에 크게 적힌 <b>총보수</b> 외에 <mark>기타비용과 매매·중개수수료</mark>가 따로 있습니다.</li>
    <li>이 셋을 합친 것이 <b>실제로 부담하는 비용</b>입니다. 총보수만 보면 과소평가하게 됩니다.</li>
    <li>실부담은 <b>금융투자협회 전자공시</b>에서 직접 조회할 수 있습니다.</li>
  </ul>
</div>

<p style="background:#fff3cd;border:1px solid #e0a800;border-radius:6px;padding:10px 14px;font-size:14px;color:#7a5c00;">⚠️ 이 초안은 실제 보수 수치와 조회 화면 캡처가 아직 없는 상태입니다(공시 사이트가 자바스크립트 기반이라 자동 수집 불가). 아래 표와 화면 안내는 사람이 조회 화면을 캡처해 준 뒤 채워집니다 — capture_guide 참고.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ETF 수수료는 언제 어떻게 빠져나가나요</li>
  <li>총보수 말고 또 무슨 비용이 있나요</li>
  <li>실제 부담은 어디서 확인하나요</li>
  <li>보수 차이가 수익에 얼마나 영향을 주나요</li>
  <li>증권사 거래 수수료와는 다른 건가요</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ETF 수수료는 언제 어떻게 빠져나가나요</h2>

<p>ETF 보수는 따로 청구서가 오지 않습니다. <mark>보유하는 동안 매일 조금씩 순자산가치에서 자동으로 차감</mark>되기 때문에, 투자자는 돈이 빠져나가는 것을 직접 보지 못합니다.</p>

<p>그래서 "수수료를 낸 적이 없다"고 느끼기 쉽지만, 실제로는 가격에 이미 반영된 뒤의 숫자를 보고 있는 것입니다. 오래 들고 있을수록 누적 부담이 커지는 이유이기도 합니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">총보수 말고 또 무슨 비용이 있나요</h2>

<p>상품 페이지에 크게 적힌 <b>총보수</b>는 운용사·판매사·수탁사 등에 가는 고정 보수입니다. 여기에 <mark>두 가지가 따로 붙습니다.</mark></p>

<ul style="line-height:1.9;">
  <li><b>기타비용</b> — 지수 사용료, 회계감사비 등 펀드를 운용하는 데 드는 비용</li>
  <li><b>매매·중개수수료</b> — 펀드가 편입 종목을 사고팔 때 발생하는 비용</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>용어 정리</b>
  <ul style="margin:8px 0 0 0;padding-left:20px;line-height:1.9;">
    <li><b>총보수</b>: 운용·판매·수탁 보수의 합. 상품 페이지에 크게 표시되는 숫자.</li>
    <li><b>합성총보수(TER)</b>: 총보수 + 기타비용.</li>
    <li><b>실부담비용</b>: 합성총보수 + 매매·중개수수료. 실제로 부담하는 전체.</li>
  </ul>
</div>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">항목</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">연 비율</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">비고</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">총보수</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;">상품 페이지 표시 숫자</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">기타비용</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;">지수 사용료·감사비 등</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">매매·중개수수료</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">캡처 필요</td><td style="border:1px solid #ccd;padding:10px;">편입 종목 매매 비용</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;"><b>실부담비용 합계</b></td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><b>캡처 필요</b></td><td style="border:1px solid #ccd;padding:10px;">실제로 내는 전체</td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">위 수치는 <a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시</a> 조회 화면 캡처 후 채웁니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제 부담은 어디서 확인하나요</h2>

<p>운용사 페이지나 증권사 앱에는 보통 총보수만 크게 나옵니다. 세 항목을 나눠서 보려면 <mark><a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시서비스</a>의 펀드별 보수비용비교</mark>를 이용합니다.</p>

<ol style="line-height:1.9;">
  <li><a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시</a>에 접속합니다.</li>
  <li>「펀드공시」에서 <b>펀드별 보수비용비교</b> 메뉴로 이동합니다.</li>
  <li>유형을 <b>ETF</b>로 선택해 조회합니다.</li>
  <li>총보수·기타비용·매매중개수수료가 <b>각각 따로</b> 표시된 열을 확인합니다.</li>
</ol>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>조회 화면 캡처 자리 (캡처 후 삽입)</b>
  <p style="margin:8px 0 0 0;">실제 조회 화면과, 같은 ETF를 증권사 앱에서 봤을 때 표시되는 총보수를 나란히 놓아 차이를 보여줄 예정입니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">보수 차이가 수익에 얼마나 영향을 주나요</h2>

<p>연 몇 %p 차이는 작아 보이지만 <mark>보유 기간이 길수록 누적</mark>됩니다. 매년 자산에서 비율로 빠져나가기 때문에, 원금이 커질수록 절대 금액도 함께 커집니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;">
  <b>장기 누적 비교 자리 (캡처 후 작성)</b>
  <p style="margin:8px 0 0 0;">같은 금액을 같은 기간 넣었을 때, 실부담비용 차이가 최종 금액에서 얼마가 되는지 계산해 넣을 예정입니다.</p>
</div>

<p>다만 비용이 낮다고 언제나 유리한 것은 아닙니다. 추종하는 지수가 다르거나 추적오차가 크면 결과가 달라지므로, <b>비용은 여러 판단 기준 중 하나</b>로 보는 편이 맞습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">증권사 거래 수수료와는 다른 건가요</h2>

<p>다릅니다. 두 비용은 내는 상대도 시점도 다릅니다.</p>

<ul style="line-height:1.9;">
  <li><b>증권사 위탁수수료</b>: 사고팔 때마다 증권사에 냅니다. 거래를 안 하면 발생하지 않습니다.</li>
  <li><b>ETF 보수</b>: 보유하는 동안 상품에서 매일 차감됩니다. 거래를 안 해도 계속 나갑니다.</li>
</ul>

<p>증권사별 거래 수수료 비교는 따로 정리한 "증권사 수수료 비교" 글을 참고하세요.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF 수수료는 언제 결제되나요</summary>
  <p style="margin:10px 0 0 0;">따로 결제하지 않습니다. 보유 기간 동안 매일 조금씩 순자산가치에서 자동 차감되므로 투자자가 별도로 내는 절차는 없습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">총보수와 실부담비용은 어떻게 다른가요</summary>
  <p style="margin:10px 0 0 0;">총보수는 운용·판매·수탁 보수의 합이고, 실부담비용은 여기에 기타비용과 매매·중개수수료까지 더한 전체 비용입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">실부담비용은 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">금융투자협회 전자공시서비스의 펀드별 보수비용비교에서 유형을 ETF로 조회하면 총보수·기타비용·매매중개수수료가 나뉘어 표시됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">보수가 낮은 ETF가 항상 유리한가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 추종 지수와 추적오차에 따라 결과가 달라지므로 비용은 여러 판단 기준 중 하나로 보는 편이 맞습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETF를 안 팔고 계속 들고 있으면 수수료를 안 내나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 보수는 거래가 아니라 보유에 대해 매일 차감되므로 팔지 않아도 계속 발생합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">증권사 거래 수수료와 ETF 보수는 같은 건가요</summary>
  <p style="margin:10px 0 0 0;">다릅니다. 거래 수수료는 사고팔 때 증권사에 내고, ETF 보수는 보유 기간 동안 상품에서 차감됩니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시서비스</a> — 펀드별 보수비용비교 (조회 화면 캡처 예정)</li>
    <li>기준일: 미확정 — 공시 조회 화면의 기준일자로 확정</li>
  </ul>
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
특정 종목·상품 매수매도 권유가 아닙니다. 투자 책임은 본인에게 있습니다. 보수와 비용은 상품과 시점에 따라 달라지므로 투자 전 해당 상품의 최신 공시를 확인하세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ETF 수수료 총보수 실부담 확인법",
  "description": "ETF의 총보수와 기타비용, 매매중개수수료를 구분하고 실제 부담하는 비용을 금융투자협회 전자공시에서 확인하는 방법을 정리합니다. (수치는 조회 화면 캡처 후 확정)",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-07",
  "dateModified": "2026-09-07",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/etf-fee-comparison"
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
      "name": "ETF 수수료는 언제 결제되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "따로 결제하지 않습니다. 보유 기간 동안 매일 조금씩 순자산가치에서 자동 차감되므로 투자자가 별도로 내는 절차는 없습니다." }
    },
    {
      "@type": "Question",
      "name": "총보수와 실부담비용은 어떻게 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "총보수는 운용·판매·수탁 보수의 합이고, 실부담비용은 여기에 기타비용과 매매·중개수수료까지 더한 전체 비용입니다." }
    },
    {
      "@type": "Question",
      "name": "실부담비용은 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "금융투자협회 전자공시서비스의 펀드별 보수비용비교에서 유형을 ETF로 조회하면 총보수·기타비용·매매중개수수료가 나뉘어 표시됩니다." }
    },
    {
      "@type": "Question",
      "name": "보수가 낮은 ETF가 항상 유리한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 추종 지수와 추적오차에 따라 결과가 달라지므로 비용은 여러 판단 기준 중 하나로 보는 편이 맞습니다." }
    },
    {
      "@type": "Question",
      "name": "ETF를 안 팔고 계속 들고 있으면 수수료를 안 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 보수는 거래가 아니라 보유에 대해 매일 차감되므로 팔지 않아도 계속 발생합니다." }
    },
    {
      "@type": "Question",
      "name": "증권사 거래 수수료와 ETF 보수는 같은 건가요",
      "acceptedAnswer": { "@type": "Answer", "text": "다릅니다. 거래 수수료는 사고팔 때 증권사에 내고, ETF 보수는 보유 기간 동안 상품에서 차감됩니다." }
    }
  ]
}
</script>
