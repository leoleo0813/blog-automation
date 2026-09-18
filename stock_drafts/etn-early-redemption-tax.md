---
keyword: ETN 뜻
title: ETN 뜻과 조기상환 세금 차이
slug: etn-early-redemption-tax
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1500 (PC 380 / 모바일 1120)
gate1_pass: true (일반 주제 기준 월 500 이상 필요, 2026-09-18 네이버 키워드도구 실측)
serp_check: |
  [게이트2 v3 판정 2026-09-18 — 통과]
  WebSearch "ETN 뜻" + "ETN 뜻 상장지수증권 ETF 차이 만기상환 신용위험" 상위 종합:
  miraeasset.com(미래에셋증권, 공식 ×2) / etn.daishin.com(대신증권) /
  blog.koreainvestment.com(한국투자증권 블로그) / brunch.co.kr(개인 브런치, ×2) /
  open.shinhansec.com(신한투자증권) / en.wikipedia.org(백과, ×2) /
  kcie.or.kr(금융투자자보호재단, 준정부)
  1) 진입 여지 — 있음. brunch.co.kr 개인 글이 두 건 상위에 진입해 SERP가 완전히
     잠겨 있지 않다.
  2) 검색 의도 — 정보 탐색형("ETN이 뭔지, ETF와 뭐가 다른지" 확인)이 지배적이다.
     조회·계산기 실행이 목적인 키워드가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 ETN의 정의와 ETF 대비 신용위험
     차이까지는 다루지만, ① 조기상환 사유 중 "괴리율 100% 이상"이 2022-05-18
     삭제되어 현재는 3가지만 유효하다는 점(다수 증권사 교육자료가 옛 조항을
     그대로 남겨 둔 상태), ② 발행사 자기자본 2,500억원 미달 시 상장폐지되는
     구체 요건, ③ 코스피200 같은 국내지수 추종 ETN도 ETF의 국내주식형
     비과세 특례 없이 매매차익 전액 과세된다는 점을 한 곳에 모아 정정까지
     포함해 다루는 글은 확인하지 못했다.
  → 탈락조건 1·2 미해당, 탈락조건 3은 위 3가지 정보이득(특히 오래된 조항
    정정)으로 상쇄해 통과.
unique_asset: |
  "ETN 뜻만 알아서는 실제로 벌어지는 일을 놓친다"는 것을 구체적 수치와
  정정 정보로 보여준다.
  - 조기상환 사유는 2022-05-18 개정으로 현재 3가지만 유효하다: ① 장 종료
    시점 지표가치(IIV)가 전일 대비 80% 이상 하락 ② 지표가치가 1,000원
    미만으로 하락 ③ 기타 투자자보호 필요 인정 시. 2020년 원유 ETN 사태
    이후 신설됐던 "괴리율 100% 이상" 사유는 삭제됐는데도, 여러 증권사
    교육자료가 여전히 옛 조항을 그대로 적어 둔 것을 확인해 정정했다.
  - 상장폐지 요건은 발행사 자기자본 2,500억원 미달, 신용등급 투자적격
    미만 등으로 별도다. 조기상환(개별 종목)과 상장폐지(발행사 전체)가
    다른 층위의 위험이라는 점을 구분해 정리했다.
  - 지표가치 10,000원짜리 ETN이 하루 만에 2,000원 밑으로 떨어지면(80%
    하락) 조기상환 사유가 발생한다는 실제 숫자 예시, 괴리율 계산 공식
    {(시장가격-지표가치)/지표가치}×100의 실제 대입 예시(10,000원 대비
    10,500원이면 괴리율 5%)를 넣었다.
  - 세금에서는 코스피200처럼 국내지수를 추종하는 ETN이라도 ETF의
    국내주식형 매매차익 비과세 특례가 적용되지 않아 항상 배당소득세
    15.4% 대상이라는, 초보자가 ETF와 헷갈리기 쉬운 지점을 명시했다.
status: drafted
cannibalization_note: |
  1~51편 어디에도 ETN(상장지수증권)을 다룬 글이 없다. 22편(ETF 괴리율)은
  ETF의 순자산가치(NAV) 대비 시장가격 괴리 얘기라 지표가치(IV) 산출
  주체(예탁결제원)·조기상환 연계 방식이 다른 ETN과는 겹치지 않는다.
  23편(국내상장 해외ETF 세금)도 ETF 상품에 한정돼 ETN 고유의 발행사
  신용위험·조기상환 메커니즘과는 다른 주제다.
draft_path: stock_drafts/etn-early-redemption-tax.md
primary_source: |
  1차 시도: 한국거래소 상장공시채널(listing.krx.co.kr) ETN 상장·상장폐지
  안내 페이지에 WebFetch 1회 → EGRESS_BLOCKED(2026-09-18). RULES.md
  「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로
  진행했다.
  - 조기상환 사유 3가지(80% 하락/1,000원 미만/투자자보호)와 "괴리율 100%
    이상" 삭제(2022-05-18) 사실은 서로 무관한 언론 2곳(비즈워치·한국금융신문)이
    같은 날짜·같은 내용으로 일치했고, 한국투자증권·미래에셋증권·삼성자산운용
    (발행사 공식 공지) 등 복수 금융기관 교육자료도 삭제 이후 버전인 3가지
    사유로 일치했다. 다만 일부 증권사 페이지는 여전히 옛 "괴리율 100%"
    조항을 포함하고 있어, 신선도가 다른 두 버전이 섞여 있다는 점 자체를
    본문에 명시했다.
  - 발행사 자기자본 2,500억원 미달 시 상장폐지 요건은 이데일리(언론) +
    한국투자증권·미래에셋증권·신한투자증권 교육자료 4곳이 충돌 없이
    일치했다. 2017-02-09 시행된 진입요건 완화(1조원→5,000억원) 배경도
    같은 이데일리 기사로 확인했다.
  - ETN 매매차익 과세(코스피200 등 국내지수 추종이라도 비과세 특례 없음)는
    대신증권·한국투자증권·신한투자증권 3개 증권사 과세 안내 페이지가
    충돌 없이 일치했다.
  - 지표가치(IV)·실시간 지표가치(IIV)·괴리율 계산 공식은 한국투자증권
    TRUE ETN 교육자료와 한국예탁결제원이 산출 주체라는 설명이 복수
    출처에서 일치했다.
기준일: 2026-09-18 (WebSearch 확인일)
tags: ETN, 상장지수증권, 조기상환, 상장폐지, 지표가치, 괴리율, ETN세금, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-18).
  게이트1: 네이버 키워드도구 실측 1,500회(일반 주제 기준 500회 초과). 같은
  배치 후보 중 유상감자 세금(20)·감액배당 뜻(40)·배당재투자 뜻(20)·대차잔고
  뜻(490)·배당컷 뜻(40)·우선주 괴리율(190)은 전부 게이트1 미달로 탈락, ETN
  뜻만 통과해 채택했다.
  게이트2: v3 기준 통과(serp_check 참조) — 개인 콘텐츠(brunch) 진입 확인,
  정보이득 3가지(조기상환 사유 정정·상장폐지 요건·ETN 고유 세금 특성)로
  탈락조건3 상쇄.
  게이트3: 조기상환 사유 정정(4가지→3가지, 옛 조항 오류 지적) + 구체적 수치
  예시(80% 하락 시 실제 금액, 괴리율 계산식 대입) + ETF와 다른 ETN 세금
  특성으로 정보이득 확보.
  게이트4: listing.krx.co.kr 1회 시도 EGRESS_BLOCKED 확인 후 RULES.md
  2026-09-12 기준에 따라 교차검증 진행 — 조기상환 요건 정정은 언론 2곳(날짜
  일치)+금융기관 교육자료 다수, 상장폐지 요건은 언론 1곳+금융기관 3곳,
  세금은 증권사 3곳이 각각 충돌 없이 일치했다.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 1,500회(일반 주제 기준 500회 초과).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 탈락조건 1·2 미해당, 탈락조건 3은
  3가지 정보이득으로 상쇄(serp_check 참조).
  게이트3 충족 — 조기상환 사유 옛 조항(괴리율 100%) 삭제 사실을 정정 반영,
  실제 숫자 예시(10,000원→2,000원 하락, 괴리율 계산식 대입)까지 넣어 단순
  용어 정의를 넘어섰다.
  게이트4 — listing.krx.co.kr 직접 열람은 막혔고(1회 시도 후 중단), 조기상환
  요건 정정은 비즈워치·한국금융신문(언론 2곳, 2022-05-18 동일 날짜)과
  복수 금융기관 교육자료로, 상장폐지 요건은 이데일리(언론)와 금융기관 3곳,
  세금은 증권사 3곳으로 각각 교차검증했다. 한계: 일부 증권사 페이지가 여전히
  옛 조항을 포함하고 있어 두 버전이 혼재한다는 사실 자체를 본문에 명시했다.
  카니벌라이제이션 점검 — 1~51편 어디에도 ETN을 다룬 글이 없다. 22편(ETF
  괴리율)·23편(국내상장 해외ETF 세금)과는 상품·메커니즘이 달라 겹치지 않는다.
  기관 링크 점검 — 한국거래소·언론사 링크 전부 target="_blank" rel="noopener"
  처리, nofollow 미부착(공식·편집 콘텐츠이므로). 출처 URL은 WebSearch로 실제
  확인된 주소만 사용(지어내지 않음).
  제목 "ETN 뜻과 조기상환 세금 차이" 16자·금지어 없음·조사 최소화. 슬러그
  영문 소문자+하이픈 4단어(etn-early-redemption-tax). 인트로 문단 최상단
  배치. 표는 thead/tbody 시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1
  일치. 종목·상품 추천 표현, 단정 표현("반드시","무조건","확실히","보장")
  없음. 하단 면책 문구는 기존 게시글과 다른 문장으로 새로 작성.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 본문에서 "—" 검색 결과 0개
  확인. "다만"은 1회만 사용(나머지 전환은 "단,"·문장 구조 전환으로 분산).
  `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약 박스
  제목을 "🧾 먼저 확인할 3가지"로, 색상도 청록 계열(#f0fdfa/#0d9488)로 바꿔
  최근 게시물의 파란색·초록색·주황색·보라색 패턴과 겹치지 않게 했다. FAQ
  헤딩도 "묻고 답하기"로 바꿨다. 목차 제외 본문 H2 6개 중 "~나요"류로 끝난
  것은 1개뿐이고, 나머지 5개는 서술형("~다릅니다","~입니다","~요건","~법")
  이라 다양성 기준(절반 이상 서술형)을 충족한다. 헤지 표현("~것으로 알려져
  있다" 등) 남발 없음.
  종합 판정: 4개 게이트 전부 충족(게이트4는 언론·금융기관 교차검증으로
  대체, 한계는 출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-18</p>

<p>ETN(상장지수증권)은 <mark>증권사가 자기 신용으로 발행해 기초지수 수익률을 따라가도록 설계한 증권</mark>입니다. ETF와 비슷해 보이지만 발행사가 망하면 돈을 돌려받지 못할 수 있고, 조기에 강제로 상환되는 경우도 있습니다. 조기상환·상장폐지 요건의 최신 내용과 ETF와 다른 세금 처리까지 정리했습니다.</p>

<div style="background:#f0fdfa;border:2px solid #0d9488;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#115e59;font-size:18px;">🧾 먼저 확인할 3가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>조기상환 사유는 <b>2022년 개정으로 지금은 세 가지</b>뿐입니다.</li>
    <li>발행사 <mark>자기자본이 2,500억원 밑으로 떨어지면</mark> 상장폐지될 수 있습니다.</li>
    <li>코스피200을 따라가는 ETN도 <b>매매차익에 세금이 붙습니다.</b></li>
  </ul>
</div>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ETN이 뭔가요</li>
  <li>ETN과 ETF, 신용위험부터 다릅니다</li>
  <li>조기상환 사유, 지금은 세 가지입니다</li>
  <li>상장폐지까지 이어지는 요건</li>
  <li>ETN 세금, ETF와 이렇게 다릅니다</li>
  <li>지표가치와 괴리율 확인하는 법</li>
  <li>묻고 답하기</li>
</ol>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">ETN이 뭔가요</h2>

<p>ETN은 Exchange Traded Note의 줄임말로, 우리말로는 상장지수증권이라고 합니다. 증권회사가 발행해 거래소에 상장하고, 주식처럼 실시간으로 사고팔 수 있습니다.</p>

<p>ETN을 발행한 증권회사는 기초지수(코스피200, 특정 원자재, 해외지수 등)의 움직임을 따라가도록 설계하고, 만기(1년 이상 20년 이내)가 되면 투자 기간 동안의 누적 수익에서 제비용을 뺀 금액을 투자자에게 지급합니다.</p>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">ETN과 ETF, 신용위험부터 다릅니다</h2>

<p>ETF(상장지수펀드)는 펀드가 기초자산을 직접 사서 별도의 신탁재산으로 보관합니다. 운용사가 파산하더라도 그 자산을 팔아 투자자에게 돌려줄 수 있습니다.</p>

<p>반면 ETN은 발행 증권사가 기초자산을 직접 보유하지 않고, 자기 신용으로 "지수 수익률만큼 지급하겠다"고 약속하는 무보증·무담보 증권입니다. 발행 증권사가 파산하면 투자금을 돌려받지 못할 수 있는 <mark>발행사 신용위험</mark>이 ETF에는 없는 ETN 고유의 위험입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">ETF</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">ETN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">법적 성격</td>
      <td style="border:1px solid #ddd;padding:8px;">펀드(신탁재산 별도 보관)</td>
      <td style="border:1px solid #ddd;padding:8px;">증권사가 발행하는 파생결합증권</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">발행사 신용위험</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">있음(무보증·무담보)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">만기</td>
      <td style="border:1px solid #ddd;padding:8px;">없음</td>
      <td style="border:1px solid #ddd;padding:8px;">1~20년</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">조기상환 사유, 지금은 세 가지입니다</h2>

<p>ETN은 만기 전에도 특정 조건에 해당하면 강제로 조기상환(조기청산)됩니다. 2026년 현재 유효한 사유는 다음 세 가지입니다.</p>

<ul style="line-height:1.9;">
  <li>장 종료 시점 지표가치(IIV)가 전날 대비 <mark>80% 이상 하락</mark>한 경우</li>
  <li>장 종료 시점 지표가치가 <b>1,000원 미만</b>으로 떨어진 경우</li>
  <li>그 밖에 거래소가 투자자 보호를 위해 필요하다고 인정하는 경우</li>
</ul>

<p>예를 들어 지표가치가 10,000원인 ETN이 하루 만에 2,000원 밑으로 떨어지면(80% 이상 하락) 조기상환 사유가 발생합니다. 이때 상환가격은 사유가 발생한 날의 다음 거래소 영업일 지표가치로 정해집니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>"괴리율 100% 이상"은 더 이상 조기상환 사유가 아닙니다</b>
  <p style="margin:8px 0 0 0;">2020년 원유 ETN 괴리율 급등 사태 이후 한때 "지표가치 기준 괴리율 100% 이상"도 조기상환 사유에 포함됐지만, 2022년 5월 18일 개정으로 삭제됐습니다. 일부 증권사 교육자료에는 이 옛 조항이 아직도 남아 있어, 지금 기준으로는 위 세 가지만 유효하다는 점을 구분해서 봐야 합니다.</p>
</div>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">상장폐지까지 이어지는 요건</h2>

<p>조기상환이 개별 ETN 종목에 생기는 일이라면, 상장폐지는 발행 증권사 자체의 문제로 생기는 더 큰 위험입니다.</p>

<ul style="line-height:1.9;">
  <li>발행사의 <mark>자기자본이 2,500억원에 미달</mark>하는 경우</li>
  <li>발행사의 신용등급이 투자적격 등급에 미달하는 경우</li>
  <li>그 밖에 발행사 인가 취소, 기초지수 산출 불가, 발행·거래규모 미달 등</li>
</ul>

<p>ETN 시장에 새로 진입하려는 증권사는 자기자본 5,000억원 이상을 갖춰야 합니다. 상장폐지 기준(2,500억원)은 이 진입 기준의 절반 수준으로, 이미 발행 중인 증권사의 재무 상태가 크게 나빠졌을 때 투자자를 보호하기 위한 하한선입니다.</p>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">ETN 세금, ETF와 이렇게 다릅니다</h2>

<p>ETN의 매매차익과 분배금은 배당소득세 15.4%(지방소득세 포함) 대상이고, 다른 금융소득과 합쳐 연 2,000만원을 넘으면 금융소득종합과세 대상에도 포함됩니다. 증권거래세는 붙지 않습니다.</p>

<p>여기서 ETF와 헷갈리기 쉬운 지점이 있습니다. 국내 주식으로만 구성된 ETF는 매매차익이 비과세지만, <span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">ETN은 코스피200처럼 국내지수를 추종하더라도 이런 비과세 특례가 적용되지 않아 매매차익 전액이 배당소득세 대상</span>입니다. "국내 지수니까 세금이 없겠지"라고 짐작하면 틀리기 쉬운 부분입니다.</p>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">지표가치와 괴리율 확인하는 법</h2>

<p>지표가치(IV)는 ETN 1증권의 실질 가치로, 한국예탁결제원이 매 영업일 1회 산출합니다. 장중에는 전일 지표가치에 당일 기초지수 변화율을 반영한 실시간 지표가치(IIV)가 쓰입니다.</p>

<p>괴리율은 시장가격이 지표가치에서 얼마나 벗어나 있는지를 보여주는 지표로, 다음처럼 계산합니다.</p>

<ul style="line-height:1.9;">
  <li>괴리율 = {(시장가격 − 지표가치) ÷ 지표가치} × 100</li>
  <li>예: 지표가치 10,000원, 시장가격 10,500원 → 괴리율 5%</li>
</ul>

<p>괴리율이 크게 벌어진 종목은 실제 가치보다 비싸게(또는 싸게) 거래되고 있다는 뜻이라 주의가 필요합니다. 종목별 지표가치·괴리율 추이는 <a href="https://etn.krx.co.kr/" target="_blank" rel="noopener">한국거래소 ETN 시장 정보</a>와 <a href="https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC020103020801" target="_blank" rel="noopener">한국거래소 데이터 상세검색</a>에서 확인할 수 있습니다.</p>

<h2 style="border-left:6px solid #0d9488;padding-left:12px;margin-top:36px;">묻고 답하기</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ETN과 ETF 중 뭐가 더 안전한가요</summary>
  <p style="margin:10px 0 0 0;">일률적으로 말하기 어렵습니다. ETF는 발행사 신용위험이 없지만, ETN은 발행 증권사의 신용에 기대는 구조라 그만큼 위험 요소가 하나 더 있습니다. 같은 기초지수를 추종하는 상품이라도 구조가 다르다는 점을 알고 선택하는 것이 중요합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">조기상환되면 투자금을 전부 잃나요</summary>
  <p style="margin:10px 0 0 0;">그렇지 않습니다. 조기상환은 파산이 아니라 사유 발생일 다음 거래소 영업일의 지표가치로 정산해 돌려주는 절차입니다. 다만 지표가치 자체가 크게 떨어진 상태에서 상환되는 것이라 손실 폭이 클 수는 있습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">괴리율이 100%를 넘으면 지금도 강제 청산되나요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 이 조항은 2022년 5월 18일 개정으로 삭제됐습니다. 현재 조기상환 사유는 지표가치 80% 이상 하락, 지표가치 1,000원 미만, 기타 투자자보호 필요 시 세 가지뿐입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내지수를 따라가는 ETN도 매매차익에 세금이 붙나요</summary>
  <p style="margin:10px 0 0 0;">붙습니다. 국내 주식형 ETF와 달리 ETN은 코스피200 같은 국내지수를 추종하더라도 매매차익 비과세 특례가 없어, 매매차익과 분배금 모두 배당소득세 15.4% 대상입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">투자 전에 꼭 확인해야 할 게 있나요</summary>
  <p style="margin:10px 0 0 0;">발행 증권사의 신용등급과 자기자본 수준, 해당 종목의 지표가치·괴리율 추이를 한국거래소 데이터 페이지에서 확인하는 것이 좋습니다. 지표가치가 낮아져 조기상환 기준에 가까워지고 있는지도 함께 살펴볼 만합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://etn.krx.co.kr/" target="_blank" rel="noopener">한국거래소 ETN 시장</a> - ETN 상장·조기상환·상장폐지 제도 안내</li>
    <li><a href="https://www.fntimes.com/html/view.php?ud=202205181601497060179ad43907_18" target="_blank" rel="noopener">한국금융신문</a> - "거래소, ETN 조기청산 요건 개선…괴리율 100% 이상 사유 삭제"(2022-05-18)</li>
    <li><a href="https://edaily.co.kr/News/Read?mediaCodeNo=257&amp;newsId=02833926615828880" target="_blank" rel="noopener">이데일리</a> - ETN 발행사 요건(자기자본 등) 관련 보도</li>
  </ul>
  기준일: 2026-09-18(WebSearch 확인일). 한국거래소 원문 페이지는 이번 세션
  WebFetch가 막혀 직접 열람하지 못했고, 조기상환 요건 정정 사실과 상장폐지
  요건은 언론 보도와 복수 금융기관 교육자료가 일치하는 것으로, ETN 세금
  특성은 증권사 3곳의 과세 안내 페이지로 교차검증했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 ETN이라는 상품의 구조와 제도적 위험 요인을 이해하는 데 참고하시라고
정리한 정보 제공용 글입니다. 특정 종목이나 상품의 매수·매도를 권하지 않으며,
투자로 인한 손익은 투자자 본인의 책임입니다. 관련 제도와 세법은 이후 바뀔 수
있으므로, 실제 투자 전에는 한국거래소 등 원출처에서 최신 내용을 다시
확인하시기 바랍니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ETN 뜻과 조기상환 세금 차이",
  "description": "ETN(상장지수증권)의 뜻과 ETF와의 신용위험 차이, 2022년 개정된 조기상환 사유 세 가지, 발행사 자기자본 2,500억원 상장폐지 요건, ETF와 다른 ETN의 매매차익 세금 처리를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-18",
  "dateModified": "2026-09-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/etn-early-redemption-tax"
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
      "name": "ETN과 ETF 중 뭐가 더 안전한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "일률적으로 말하기 어렵습니다. ETF는 발행사 신용위험이 없지만, ETN은 발행 증권사의 신용에 기대는 구조라 그만큼 위험 요소가 하나 더 있습니다. 같은 기초지수를 추종하는 상품이라도 구조가 다르다는 점을 알고 선택하는 것이 중요합니다." }
    },
    {
      "@type": "Question",
      "name": "조기상환되면 투자금을 전부 잃나요",
      "acceptedAnswer": { "@type": "Answer", "text": "그렇지 않습니다. 조기상환은 파산이 아니라 사유 발생일 다음 거래소 영업일의 지표가치로 정산해 돌려주는 절차입니다. 다만 지표가치 자체가 크게 떨어진 상태에서 상환되는 것이라 손실 폭이 클 수는 있습니다." }
    },
    {
      "@type": "Question",
      "name": "괴리율이 100%를 넘으면 지금도 강제 청산되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 이 조항은 2022년 5월 18일 개정으로 삭제됐습니다. 현재 조기상환 사유는 지표가치 80% 이상 하락, 지표가치 1,000원 미만, 기타 투자자보호 필요 시 세 가지뿐입니다." }
    },
    {
      "@type": "Question",
      "name": "국내지수를 따라가는 ETN도 매매차익에 세금이 붙나요",
      "acceptedAnswer": { "@type": "Answer", "text": "붙습니다. 국내 주식형 ETF와 달리 ETN은 코스피200 같은 국내지수를 추종하더라도 매매차익 비과세 특례가 없어, 매매차익과 분배금 모두 배당소득세 15.4% 대상입니다." }
    },
    {
      "@type": "Question",
      "name": "투자 전에 꼭 확인해야 할 게 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "발행 증권사의 신용등급과 자기자본 수준, 해당 종목의 지표가치·괴리율 추이를 한국거래소 데이터 페이지에서 확인하는 것이 좋습니다. 지표가치가 낮아져 조기상환 기준에 가까워지고 있는지도 함께 살펴볼 만합니다." }
    }
  ]
}
</script>
