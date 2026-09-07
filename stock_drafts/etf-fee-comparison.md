---
keyword: ETF 수수료
title: ETF 수수료 총보수 실부담 확인법
slug: etf-fee-comparison
keyword_class: human-assisted
publish_effort: capture
monthly_search_volume: 770 (PC 190 / 모바일 580)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
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
  [완성 2026-09-07 — 금융투자협회 공시 원자료 반영]
  핵심 정보이득은 "표시된 총보수가 실제로 내는 전부가 아니다"를 공시 실측값으로 보여주는 것.
  파생형 ETF 242개를 집계해 평균 총보수 0.332% → 실부담 0.602%(1.81배), 242개 중 80개(33%)가
  실부담 2배 초과임을 확인했다. 개별 사례로는 총보수 0.022%인 선물 인버스 2X의 실부담이
  0.611%(27.8배), 반도체 레버리지가 0.490% → 2.713%다.
  여기에 왜 상품마다 다른지를 회전율로 설명한다 — 레버리지·인버스 89개와 그 외 153개의
  총보수는 0.348% vs 0.323%로 거의 같은데 매매·중개수수료가 0.3137% vs 0.0893%로 3.5배
  차이 난다. 총보수만 비교하면 안 보이는 차이다.
  상위 경쟁 글은 대부분 총보수 설명에서 그치고 실부담 실측값까지 제시하지 않는다.
primary_source: |
  금융투자협회 전자공시서비스(dis.kofia.or.kr) > 펀드공시 > 펀드별 보수비용비교.
  사람이 직접 조회해 엑셀로 내려받아 제공(2026-09-07). 원본 파일은
  sources/kofia-etf-fee-comparison-20260907.xls 에 보존, 집계·해석은
  sources/kofia-etf-fee-comparison.md 에 정리.
  ※ 범위 한정 — 받은 자료의 ETF 242개가 전부 파생형(주식파생형 177 / 채권파생형 29 /
    혼합채권파생형 15 / 혼합주식파생형 12 / 재간접파생형 9)이다. 일반 지수형(비파생) ETF는
    포함되지 않았으므로 "국내 ETF 평균"이라고 쓰면 틀린다. 본문에 범위를 명시했다.
기준일: 2026-09-07 (공시 조회·다운로드일). 파일 안에 기준일자 표기가 없어 조회일로 기록한다. 공시값 자체의 산정 기준 시점은 조회 화면에서 별도 확인이 필요하다.
tags: ETF수수료, 총보수, 실부담비용, TER, ETF투자, 운용보수, 매매중개수수료, 주식초보, ETF비교
gate_pass: true
capture_guide: |
  [해결됨 2026-09-07] 사람이 금융투자협회 전자공시에서 펀드별 보수비용비교를 조회해
  엑셀 원본(1,214행)을 내려받아 제공. 그 안의 ETF 242개로 표 세 개를 모두 채웠다.
  ★ 원자료 덕분에 잡은 것: 받은 데이터의 ETF가 전부 파생형이었다. 조회 결과를 그대로
    "국내 ETF 평균"이라고 썼으면 틀린 글이 될 뻔했다. 본문에 "파생형 ETF 242개 기준"으로
    범위를 명시했다.
  ★ 원자료가 아니면 못 만들었을 수치: 총보수 0.022%짜리 선물 인버스 2X의 실부담이
    0.611%(27.8배). 검색으로는 이런 개별 격차 사례를 확인할 수 없다.
  남은 선택 사항(없어도 발행 가능): 일반 지수형(비파생) ETF까지 포함한 조회 결과가 있으면
  "국내 ETF 전체" 기준 수치로 확장할 수 있다. 조회 조건에서 유형 필터를 바꿔 다시 받으면 된다.
  조회 화면 스크린샷이 있으면 본문 이미지로 넣어 절차 설명을 보강할 수 있다(현재는 글로만 설명).
self_check: |
  [2026-09-07 공시 원자료 반영 후 최종 판정]
  게이트1 충족 — 네이버 키워드도구 실측 770회(PC 190 / 모바일 580).
  게이트2 충족 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  브런치·개인 블로그·커뮤니티가 셋이나 상위에 있어 이 시리즈 중 진입 여지가 가장 크다.
  게이트3 충족 — 금융투자협회 공시 원자료로 표를 전부 실측값으로 채웠다. 집계표(평균·중앙값),
  개별 사례표(0.022%→0.611% 등 4건), 레버리지 대비 그 외 비교표, 장기 누적 비교표.
  경쟁 글이 총보수 설명에서 그치는 자리에서 실부담 실측값과 그 원인(회전율)까지 제시한다.
  게이트4 충족 — 1차 출처는 금융투자협회 전자공시 원본 엑셀(1,214행). 사람이 직접 조회해
  내려받아 제공했고 sources/kofia-etf-fee-comparison-20260907.xls 에 원본을 보존했다.
  검색 요약에 나온 "국내 ETF 평균 총보수 0.3084% / 전체 비용 0.4982%" 같은 숫자는 끝까지
  쓰지 않았다. 본문 수치는 전부 원자료를 직접 집계해 얻었다.
  ★ 범위 한계를 본문에 명시했다 — 받은 자료의 ETF 242개가 전부 파생형이라 "국내 ETF 평균"이
  아니다. 그대로 일반화했으면 틀린 글이 됐을 자리라, 표 아래 캡션과 본문 문장 양쪽에
  "파생형 ETF 242개 기준"을 적었다.
  검산 — 평균 총보수 0.3319% / TER 0.4298% / 실부담 0.6016%, 배수 1.81배.
  2배 초과 80/242 = 33%. 레버리지·인버스 89개 매매중개 평균 0.3137% vs 그 외 153개
  0.0893%(3.5배). 개별 사례는 원본 행에서 그대로 옮겼다.
  장기 누적표는 원금 1,000만원 고정 가정의 단순 계산이며, 그 가정을 캡션에 밝혔다.
  금지 사항 점검 — 특정 상품 추천으로 읽히지 않도록 개별 사례를 종목명 대신 유형명
  ("선물 인버스 2X", "반도체 레버리지")으로 표기했다. 레버리지·인버스의 비용이 큰 것은
  구조상 회전율이 높기 때문이지 상품이 나쁘다는 뜻이 아니라는 단서도 본문에 달았다.
  카니발라이제이션 점검 — 1편(증권사 수수료 비교)은 거래마다 내는 위탁수수료, 이 글은
  보유하는 동안 상품에서 빠지는 보수라 대상이 다르다. 본문에서 1편으로 안내한다.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 금융투자협회 전자공시로 안내하는 문장과
  하단 참고 출처를 전부 링크 처리. target="_blank" rel="noopener", nofollow 미부착.
  제목 16자·금지어 없음·조사 없음. "비교"가 아니라 "확인법"이라 비교표 필수 규칙에 걸리지
  않는다(다만 결과적으로 비교표가 여러 개 들어갔다). 슬러그는 큐 등록값 유지.
  FAQ 6개와 JSON-LD 1:1 일치. @id 티스토리 entry 패턴. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족 → gate_pass:true. 발행 가능.
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

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ETF 수수료는 언제 어떻게 빠져나가나요</li>
  <li>총보수 말고 또 무슨 비용이 있나요</li>
  <li>실제 부담은 어디서 확인하나요</li>
  <li>격차가 얼마나 벌어지나요</li>
  <li>왜 상품마다 차이가 나나요</li>
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

<p>실제 공시 자료로 확인해 보면 격차가 뚜렷합니다. 아래는 <a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시</a>에서 <b>파생형 ETF 242개</b>를 내려받아 집계한 결과입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">총보수</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">합성총보수(TER)</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">실부담비용</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">평균</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.332%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.430%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>0.602%</mark></td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">중앙값</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.350%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.435%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.561%</td></tr>
  </tbody>
</table>

<p><mark>평균 실부담비용이 평균 총보수의 1.81배</mark>입니다. 242개 중 <b>80개(33%)</b>는 실부담이 총보수의 2배를 넘습니다.</p>

<p style="font-size:13px;color:#888;">출처: <a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시</a> 펀드별 보수비용비교, 2026-09-07 조회. 이 집계는 <b>파생형 ETF 242개</b> 기준이며 일반 지수형 ETF는 포함되지 않았습니다. 공시값은 주기적으로 갱신됩니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">실제 부담은 어디서 확인하나요</h2>

<p>운용사 페이지나 증권사 앱에는 보통 총보수만 크게 나옵니다. 세 항목을 나눠서 보려면 <mark><a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시서비스</a>의 펀드별 보수비용비교</mark>를 이용합니다.</p>

<ol style="line-height:1.9;">
  <li><a href="https://dis.kofia.or.kr" target="_blank" rel="noopener">금융투자협회 전자공시</a>에 접속합니다.</li>
  <li>「펀드공시」에서 <b>펀드별 보수비용비교</b> 메뉴로 이동합니다.</li>
  <li>유형을 <b>ETF</b>로 선택해 조회합니다.</li>
  <li>총보수·기타비용·매매중개수수료가 <b>각각 따로</b> 표시된 열을 확인합니다.</li>
</ol>

<p>조회 결과에는 <b>총보수(합계 A)</b>, <b>기타비용(B)</b>, <b>합성총보수 TER(A+B)</b>, <b>매매·중개수수료율(D)</b>이 각각 다른 열로 나옵니다. 상품 페이지에 크게 적힌 숫자는 대개 첫 번째 열 하나뿐입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">격차가 얼마나 벌어지나요</h2>

<p>실제 공시값으로 보면 상품에 따라 차이가 큽니다. 아래는 위 조회 결과에서 그대로 뽑은 숫자입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:9px;text-align:left;">유형</th>
      <th style="border:1px solid #ccd;padding:9px;text-align:right;">총보수</th>
      <th style="border:1px solid #ccd;padding:9px;text-align:right;">기타비용</th>
      <th style="border:1px solid #ccd;padding:9px;text-align:right;">매매·중개</th>
      <th style="border:1px solid #ccd;padding:9px;text-align:right;">실부담</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:9px;">선물 인버스 2X</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.022%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.10%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.4914%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;"><mark>0.611%</mark></td></tr>
    <tr><td style="border:1px solid #ccd;padding:9px;">반도체 레버리지</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.490%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.06%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">2.1631%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;"><mark>2.713%</mark></td></tr>
    <tr><td style="border:1px solid #ccd;padding:9px;">국채 선물</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.300%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.06%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.0677%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.428%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:9px;">해외 지수 합성</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.350%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.05%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.0000%</td><td style="border:1px solid #ccd;padding:9px;text-align:right;">0.400%</td></tr>
  </tbody>
</table>

<div style="background:#fdeaea;border-left:4px solid #d9534f;padding:14px 18px;margin:20px 0;line-height:1.8;">
  <b>총보수가 낮다고 안심할 수 없습니다.</b>
  <p style="margin:8px 0 0 0;">첫 줄을 보세요. 총보수는 <b>0.022%</b>로 이 표에서 가장 낮은데, 매매·중개수수료가 붙자 실부담은 <mark>0.611%로 27.8배</mark>가 됐습니다. 두 번째 줄은 실부담이 <b>2.7%</b>까지 올라갑니다.</p>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">왜 상품마다 차이가 나나요</h2>

<p>매매·중개수수료는 <mark>펀드가 편입 종목을 얼마나 자주 사고파는지</mark>에 따라 정해집니다. 그래서 회전율이 높은 구조일수록 이 항목이 커집니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">구분</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">개수</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">평균 총보수</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">평균 매매·중개</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">평균 실부담</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">레버리지·인버스</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">89</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.348%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>0.3137%</mark></td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.745%</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">그 외</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">153</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.323%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.0893%</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">0.518%</td></tr>
  </tbody>
</table>

<p>두 집단의 <b>총보수는 0.348%와 0.323%로 거의 같습니다.</b> 그런데 매매·중개수수료가 3.5배 차이 나면서 실부담이 갈립니다. 총보수만 비교했다면 보이지 않았을 차이입니다.</p>

<p style="font-size:13px;color:#888;">레버리지·인버스는 구조상 매일 기초자산을 재조정해야 해서 회전율이 높습니다. 비용이 크다는 것이 상품이 나쁘다는 뜻은 아니며, 성격이 다른 상품이라는 의미입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">보수 차이가 수익에 얼마나 영향을 주나요</h2>

<p>연 몇 %p 차이는 작아 보이지만 <mark>보유 기간이 길수록 누적</mark>됩니다. 매년 자산에서 비율로 빠져나가기 때문에, 원금이 커질수록 절대 금액도 함께 커집니다.</p>

<p>위 집계의 평균 총보수(0.332%)만 보고 고른 경우와 실부담(0.602%)을 확인하고 고른 경우를 비교해 보겠습니다. <b>1,000만원을 넣고 수익률이 같다고 가정</b>했을 때, 비용으로 빠져나가는 금액의 차이입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;">
  <thead>
    <tr style="background:#eef6ff;">
      <th style="border:1px solid #ccd;padding:10px;text-align:left;">보유 기간</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">0.332% 부담 시</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">0.602% 부담 시</th>
      <th style="border:1px solid #ccd;padding:10px;text-align:right;">차이</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ccd;padding:10px;">1년</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">3만 3천원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">6만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">2만 7천원</td></tr>
    <tr><td style="border:1px solid #ccd;padding:10px;">10년</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">약 33만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;">약 60만원</td><td style="border:1px solid #ccd;padding:10px;text-align:right;"><mark>약 27만원</mark></td></tr>
  </tbody>
</table>

<p style="font-size:13px;color:#888;">원금 1,000만원이 그대로 유지된다고 단순 가정한 계산입니다. 실제로는 자산이 불어나면 비율로 떼는 금액도 함께 커지므로 차이는 이보다 벌어집니다.</p>

<p>금액만 보면 크지 않아 보일 수 있지만, <mark>확인하는 데 1분이면 되는 정보</mark>라는 점을 생각하면 확인하지 않을 이유가 없습니다.</p>

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
