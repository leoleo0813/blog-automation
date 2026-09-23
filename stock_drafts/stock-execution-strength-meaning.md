---
keyword: 체결강도 뜻
title: 체결강도 뜻과 매수세 판단법
slug: stock-execution-strength-meaning
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1790 (PC 220 / 모바일 1570)
gate1_pass: true (일반 주제 기준 월 500 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-23 — 통과]
  WebSearch "체결강도 뜻 계산법 매수 매도 비율" + "체결강도 활용법 주의점
  매매신호로 사용하면 안되는 이유 거짓 신호" + "체결강도 거래량 차이 HTS
  MTS 어디서 확인" 상위 종합: mofe.go.kr(기획재정부 시사경제용어사전,
  공식) / securities.miraeasset.com(미래에셋증권, 공식) / clien.net(개인
  커뮤니티) / blog.greenallfix.com(개인 블로그) / jungbosum.com(개인·소규모
  콘텐츠) / a-ha.io(개인 Q&A, ×3) / turtlog.com(개인 블로그) /
  download.kiwoom.com(키움증권 공식 도움말)
  1) 진입 여지 — 있음. clien.net·blog.greenallfix.com·jungbosum.com·
     a-ha.io·turtlog.com 등 개인·커뮤니티 콘텐츠가 상위권 다수를 차지한다.
  2) 검색 의도 — "체결강도가 뭐고 어떻게 쓰는지" 정보 탐색형이다. 조회·
     계산기 실행이 지배적 의도가 아니다.
  3) 답 완결 여부 — 부분적. 상위 글 대부분이 정의(매수체결÷매도체결×100)와
     100 기준 해석까지는 다루지만, (a) 구체적 숫자로 직접 계산해 보여주는
     글, (b) 저유동성 종목에서 체결강도가 왜곡되는 이유를 거래량 개념과
     명확히 구분해 설명하는 글, (c) 증권사별로 실제 화면 위치를 비교
     정리한 글은 찾지 못했다. 정보이득 여지 뚜렷함(unique_asset 참조).
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  세 가지를 만들었다.
  (1) 계산 예시 2개 — 매수 우위 사례(1분간 매수체결 1,200주, 매도체결
      800주 → 체결강도 150)와 매도 우위 사례(매수체결 600주, 매도체결
      900주 → 체결강도 66.7)를 실제 나눗셈 과정과 함께 보여준다. 상위
      글들은 대부분 공식만 적어두고 숫자를 직접 대입한 예시가 없었다.
  (2) 거래량과 체결강도의 차이를 표로 정리 — 거래량은 매수·매도를
      구분하지 않은 총 체결 수량이고, 체결강도는 그중 매수·매도 비율을
      나눈 지표라는 점을 한 표로 대조했다. 두 개념을 혼동하는 초보자가
      많다는 점(clien.net·a-ha.io 질문 다수)에 비해, 이 차이를 표로 명확히
      비교한 글은 찾지 못했다.
  (3) 증권사 3곳(키움증권·미래에셋증권·삼성증권)의 체결강도 확인 화면
      위치를 공식 도움말·서비스 페이지 기준으로 비교표를 만들었다.
      흩어져 있던 정보를 한 곳에 모았다.
primary_source: |
  1차 시도: mofe.go.kr(기획재정부 시사경제용어사전) "체결강도" 항목
  WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-23). 대조군으로 google.com
  WebFetch도 시도해 같은 세션에서 막힌 것을 확인(무관 도메인까지 막히는
  세션 전면 차단 패턴, RULES.md 기록과 일치).
  이 주제는 세율·공제한도·과세표준처럼 원문 확정이 특히 중요한 숫자
  유형이 아니라, 이미 널리 쓰이는 시장 용어의 정의와 계산 공식이라
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처
  교차검증으로 진행했다.
  - 정의·계산공식(매수체결÷매도체결×100)·100 기준 해석: mofe.go.kr(정부
    용어사전, WebSearch 스니펫으로 확인) / blog.greenallfix.com(개인
    블로그) / jungbosum.com(개인·소규모 콘텐츠) 3곳이 동일한 공식과
    해석 기준으로 일치했고, 서로 다른 표현으로 설명해 하나의 보도자료를
    베낀 정황은 없다.
  - 매매신호로서의 한계(순간 지표, 심리 요인에 좌우, 저유동성 종목
    왜곡): clien.net(개인 커뮤니티) 답변과 종합 검색 요약이 일치했다.
  - HTS/MTS 화면 위치: download.kiwoom.com(키움증권 공식 도움말) /
    securities.miraeasset.com(미래에셋증권 공식 서비스 페이지) 2곳은
    증권사 공식 자료라 그대로 인용했고, 삼성증권은 samsungpop.com
    공식 가이드 페이지 제목까지만 확인되고 세부 화면 번호는 확인하지
    못해 본문에서 "대량체결모니터 등 관련 화면"으로 보수적으로 표기했다.
  원문(mofe.go.kr) 직접 열람을 못 한 한계는 self_check에도 투명 공개한다.
기준일: 2026-09-23 (WebSearch 교차검증일)
tags: 체결강도, 체결강도뜻, 체결강도계산법, 매수세매도세판단, 체결강도보는법, 호가창체결강도, 주식초보, HTS체결강도, 매매신호주의점, 거래량과체결강도차이
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-23).
  게이트1: 검색량 1,790회(일반 기준 500 이상), check-keywords.yml
  워크플로 2026-09-23 실측값.
  게이트2: 위 serp_check 참조, 3개 탈락조건 모두 미해당.
  게이트3: 계산 예시 2개 + 거래량 대비 개념 비교표 + 증권사 3곳 화면
  위치 비교표로 unique_asset 확보.
  게이트4: mofe.go.kr WebFetch 1회 시도 후 EGRESS_BLOCKED, RULES.md
  기준에 따라 독립 출처 3곳 이상 교차검증(정부 용어사전 스니펫 +
  개인 블로그 2곳)으로 진행, 증권사 화면 위치는 공식 페이지 직접 인용.
  카니벌라이제이션 점검 — 1~76편 keyword/slug 전체 grep, "체결강도"
  언급 0건 확인. 겹치는 편 없음.
  제목 "체결강도 뜻과 매수세 판단법" 15자·금지어 없음·조사/접속사
  과도한 사용 없음.
  슬러그 영문 소문자+하이픈 4단어(stock-execution-strength-meaning).
  인트로 문단 최상단 배치, "안녕하세요" 없음. 표 2개 모두 thead/tbody
  시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1 일치. 종목·상품 추천
  표현 없음. 매매 타이밍을 구체적으로 권하지 않고 "지표는 참고용,
  투자 판단은 본인 책임"으로 반복해서 못 박았다. 단정 표현("반드시",
  "무조건","확실히","보장") 없음.
  기관 링크 점검 — mofe.go.kr(정부)·download.kiwoom.com(키움증권 공식)·
  securities.miraeasset.com(미래에셋증권 공식) 전부 target="_blank"
  rel="noopener" 처리, 공공·공식기관 성격이라 nofollow 미부착.
self_check: |
  게이트 1~4 전부 통과(게이트1도 워크플로 실측값으로 확인 완료).
  제목 30자 이내·금지어 없음·조사·접속사 없음. 슬러그 영문 소문자+
  하이픈. 인트로 최상단. 표 thead/tbody 시맨틱. 본문 수치 전부 출처에
  존재(공식 자료 또는 교차검증). 기준일 명시. FAQ 5개-JSON-LD 1:1 일치.
  종목·상품 추천/단정 표현 없음. 하단 고정 문구(변형) 포함.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 발행 본문(YAML 제외)에서
  "—" 0개 확인. "다만" 0회(전환어는 "단,"·"반대로"·"물론"으로 분산).
  본문 `<mark>` 총 4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약
  박스 제목을 "🧭 한눈에 보는 핵심"으로, 색상은 teal 계열
  (#e8f9f6/#0f9b8e)로 최근 게시물(로즈·바이올렛·오렌지·앰버·인디고)과
  겹치지 않게 새로 골랐다. 목차 제외 본문 H2 5개 중 서술형 3개("체결강도
  뜻과 계산 공식", "체결강도를 매매 신호로 쓰면 위험한 이유", "체결강도
  확인할 수 있는 HTS MTS 화면"), 질문형 2개("체결강도 100을 기준으로
  매수세 매도세를 어떻게 판단하나요", "거래량과 체결강도는 뭐가
  다른가요")로 "~나요" 편중 없음(5개 중 2개, 40%). 헤지 표현 남발
  없음 — 미확인 부분(mofe.go.kr 원문 직접 열람 불가, 삼성증권 세부
  화면 번호 미확인)은 정직하게 각 1회만 명시.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-23</p>

<p><mark>체결강도는 일정 시간 동안 체결된 매수 수량을 매도 수량으로 나눈 값으로, 100을 기준으로 매수세와 매도세 중 어느 쪽이 우위인지 보여주는 지표</mark>입니다. 거래량과 헷갈리기 쉽지만 서로 다른 개념이고, 절대적인 매매 신호로 쓰기에는 뚜렷한 한계도 있습니다. 이 글은 계산 공식부터 실제 숫자를 넣은 예시, 확인할 수 있는 화면 위치까지 정리합니다.</p>

<div style="background:#e8f9f6;border:2px solid #0f9b8e;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#0b6e64;font-size:18px;">🧭 한눈에 보는 핵심</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>체결강도 = (매수체결량 ÷ 매도체결량) × 100이며, 100보다 크면 매수 우위입니다.</li>
    <li>거래량은 매수·매도를 구분하지 않은 총 체결 수량이라 체결강도와는 다른 지표입니다.</li>
    <li>순간의 스냅샷일 뿐이라 저유동성 종목에서는 소량 체결만으로도 크게 흔들립니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>체결강도 뜻과 계산 공식</li>
  <li>체결강도 100을 기준으로 매수세 매도세를 어떻게 판단하나요</li>
  <li>거래량과 체결강도는 뭐가 다른가요</li>
  <li>체결강도를 매매 신호로 쓰면 위험한 이유</li>
  <li>체결강도 확인할 수 있는 HTS MTS 화면</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">체결강도 뜻과 계산 공식</h2>

<p>체결강도는 일정 시간 동안 실제로 체결된 매수 수량과 매도 수량을 비교해, 그 시점의 매수세와 매도세 중 어느 쪽이 더 강한지를 숫자로 보여주는 지표입니다. 공식은 다음과 같습니다.</p>

<p style="background:#f6f6f4;border-left:4px solid #0f9b8e;padding:14px 18px;margin:16px 0;font-weight:bold;">체결강도 = (체결된 매수 수량 ÷ 체결된 매도 수량) × 100</p>

<p>실제 숫자를 넣어보면 이렇습니다. 1분 동안 매수 체결이 1,200주, 매도 체결이 800주였다면, 체결강도는 (1,200 ÷ 800) × 100 = <b>150</b>입니다. 같은 시간 매수 체결이 600주, 매도 체결이 900주였다면 (600 ÷ 900) × 100 = <b>66.7</b>이 됩니다.</p>

<ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
  <li>체결강도 150 → 매도 체결(800주)보다 매수 체결(1,200주)이 많아 매수 우위입니다.</li>
  <li>체결강도 66.7 → 매수 체결(600주)보다 매도 체결(900주)이 많아 매도 우위입니다.</li>
</ul>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">체결강도 100을 기준으로 매수세 매도세를 어떻게 판단하나요</h2>

<p>체결강도 100은 매수 체결량과 매도 체결량이 정확히 같다는 뜻으로, 어느 쪽도 우위가 아닌 균형 상태입니다. 이 100을 기준으로 시장에서 흔히 쓰는 해석은 아래 표와 같습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">체결강도 값</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">일반적 해석</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">100보다 큼</td>
      <td style="border:1px solid #ddd;padding:8px;">매수 체결이 매도 체결보다 많음 (매수 우위)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">100</td>
      <td style="border:1px solid #ddd;padding:8px;">매수·매도 체결량이 같음 (균형)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">100보다 작음</td>
      <td style="border:1px solid #ddd;padding:8px;">매도 체결이 매수 체결보다 많음 (매도 우위)</td>
    </tr>
  </tbody>
</table>

<p><mark>이 표는 시장에서 통용되는 일반적 해석 기준일 뿐, 특정 종목의 매수·매도 시점을 정해주는 공식이 아닙니다.</mark> 같은 100이라도 종목별 평소 거래 규모나 시간대에 따라 의미가 달라질 수 있습니다.</p>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">거래량과 체결강도는 뭐가 다른가요</h2>

<p>거래량은 매수·매도를 구분하지 않고 일정 시간 동안 체결된 주식 수량을 모두 더한 값입니다. 반면 체결강도는 그 체결량을 매수 쪽과 매도 쪽으로 나눠 비율로 비교한 지표입니다. 아래 표로 정리했습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">거래량</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">체결강도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">측정 대상</td>
      <td style="border:1px solid #ddd;padding:8px;">체결된 총 수량</td>
      <td style="border:1px solid #ddd;padding:8px;">매수 체결량 대비 매도 체결량 비율</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매수·매도 구분</td>
      <td style="border:1px solid #ddd;padding:8px;">구분하지 않음</td>
      <td style="border:1px solid #ddd;padding:8px;">구분함</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">단위</td>
      <td style="border:1px solid #ddd;padding:8px;">주(股)</td>
      <td style="border:1px solid #ddd;padding:8px;">비율(%)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">보여주는 것</td>
      <td style="border:1px solid #ddd;padding:8px;">거래가 활발한 정도</td>
      <td style="border:1px solid #ddd;padding:8px;">매수·매도 중 어느 쪽이 주도하는지</td>
    </tr>
  </tbody>
</table>

<p><mark>거래량이 크다고 반드시 체결강도가 높은 것은 아닙니다.</mark> 매수와 매도가 똑같이 활발하게 체결되면 거래량은 크지만 체결강도는 100 근처에 머물 수 있습니다.</p>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">체결강도를 매매 신호로 쓰면 위험한 이유</h2>

<p>체결강도는 그 순간의 스냅샷일 뿐입니다. 1분 뒤에는 완전히 다른 값이 나올 수 있고, 시장가격은 매수·매도 수량만이 아니라 참여자들의 심리에도 크게 좌우됩니다. 분위기가 좋으면 적은 매수량으로도 호가가 급등할 수 있고, 반대로 적은 매도량으로도 급락할 수 있습니다.</p>

<p>특히 거래량 자체가 적은 저유동성 종목에서는 이 왜곡이 더 크게 나타납니다. 평소 하루 거래량이 몇만 주에 그치는 종목이라면, <mark>단 몇백 주의 체결만으로도 체결강도가 크게 요동칠 수 있습니다.</mark> 이런 종목에서는 체결강도 하나만 보고 매수·매도 우위를 판단하기 어렵습니다.</p>

<ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
  <li>단타처럼 짧은 시간 안에 대응하는 투자자에게는 참고 지표가 될 수 있습니다.</li>
  <li>중장기로 보유하는 투자자에게는 그 순간의 수치 하나가 큰 의미를 갖지 않습니다.</li>
  <li>체결강도만 보고 특정 종목의 매수·매도 시점을 단정하는 것은 이 지표의 한계를 넘어서는 해석입니다.</li>
</ul>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">체결강도 확인할 수 있는 HTS MTS 화면</h2>

<p>체결강도는 대부분의 국내 증권사 HTS·MTS에서 종목 상세 화면이나 호가창 근처에 기본으로 제공합니다. 증권사별로 화면 위치가 조금씩 다릅니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">증권사</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">확인 위치</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://download.kiwoom.com/hero4_help_new/0178.htm" target="_blank" rel="noopener">키움증권</a></td>
      <td style="border:1px solid #ddd;padding:8px;">[0178] 체결강도추이 화면에서 종목별 일별·시간별 체결강도 추이를 조회할 수 있습니다.</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;"><a href="https://securities.miraeasset.com/kairos/0175.htm" target="_blank" rel="noopener">미래에셋증권</a></td>
      <td style="border:1px solid #ddd;padding:8px;">카이로스 [0175] 체결강도순위 화면에서 여러 종목의 체결강도를 한 번에 비교할 수 있습니다.</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">삼성증권</td>
      <td style="border:1px solid #ddd;padding:8px;">POP HTS의 대량체결모니터 등 관련 화면에서 체결 정보를 확인할 수 있습니다.</td>
    </tr>
  </tbody>
</table>

<p>증권사마다 화면 번호나 메뉴 이름이 바뀔 수 있으므로, 정확한 위치는 이용 중인 증권사의 HTS·MTS 도움말에서 다시 확인하는 편이 안전합니다.</p>

<div style="background:#e8f9f6;border:2px solid #0f9b8e;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#0b6e64;font-size:18px;">이 글에서 확인한 것</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
    <li>체결강도 = (매수체결량 ÷ 매도체결량) × 100, 100 기준으로 매수·매도 우위를 나눕니다.</li>
    <li>거래량은 총 체결 수량, 체결강도는 매수·매도 비율이라는 점에서 서로 다른 지표입니다.</li>
    <li>순간의 스냅샷이고 저유동성 종목에서 왜곡되기 쉬워, 단독 매매 신호로 쓰기에는 한계가 있습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #0f9b8e;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">체결강도 100은 무슨 뜻인가요</summary>
  <p style="margin:10px 0 0 0;">매수 체결량과 매도 체결량이 정확히 같다는 뜻으로, 매수·매도 어느 쪽도 우위가 아닌 균형 상태를 의미합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">체결강도가 높으면 주가가 오르나요</summary>
  <p style="margin:10px 0 0 0;">그렇게 단정할 수 없습니다. 체결강도는 그 순간 매수 체결이 많았다는 사실만 보여줄 뿐이고, 실제 가격은 참여자 심리 등 다른 요인에도 크게 좌우됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">거래량과 체결강도는 같은 지표인가요</summary>
  <p style="margin:10px 0 0 0;">아닙니다. 거래량은 매수·매도를 구분하지 않은 총 체결 수량이고, 체결강도는 그 체결량을 매수·매도 비율로 나눈 지표입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">체결강도는 어디서 확인하나요</summary>
  <p style="margin:10px 0 0 0;">대부분의 HTS·MTS 종목 상세 화면이나 호가창 근처에서 확인할 수 있습니다. 키움증권은 [0178] 체결강도추이, 미래에셋증권은 카이로스 [0175] 체결강도순위 화면을 제공합니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">체결강도만 보고 매매해도 되나요</summary>
  <p style="margin:10px 0 0 0;">이 글은 특정 종목의 매수·매도를 권하지 않는 정보 제공 목적의 글입니다. 체결강도는 저유동성 종목에서 쉽게 왜곡되는 순간 지표라, 다른 정보와 함께 참고하고 최종 판단은 투자자 본인이 하는 것이 안전합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://mofe.go.kr/sisa/dictionary/detail?idx=2468" target="_blank" rel="noopener">기획재정부 시사경제용어사전</a> - 체결강도</li>
    <li><a href="https://download.kiwoom.com/hero4_help_new/0178.htm" target="_blank" rel="noopener">키움증권</a> - [0178] 체결강도추이 도움말</li>
    <li><a href="https://securities.miraeasset.com/kairos/0175.htm" target="_blank" rel="noopener">미래에셋증권</a> - [0175] 체결강도순위 화면</li>
  </ul>
  기준일: 2026-09-23(WebSearch 교차검증일). 기획재정부 시사경제용어사전
  원문은 이번 세션 WebFetch가 EGRESS_BLOCKED로 막혀 직접 열람하지
  못했고, 정의와 계산 공식은 검색 스니펫과 개인 블로그 2곳으로
  교차검증했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 체결강도라는 지표를 이해하는 데 참고하시라고 정리한
정보성 글이며, 특정 종목이나 상품의 매수·매도를 권유하지 않습니다.
투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다. 증권사
화면 구성은 바뀔 수 있으므로, 실제 이용 중인 HTS·MTS에서 다시 확인해
주세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "체결강도 뜻과 매수세 판단법",
  "description": "체결강도의 뜻과 계산 공식을 실제 숫자로 계산해 보고, 거래량과의 차이, 매매 신호로 쓸 때의 한계, 증권사별 HTS MTS 확인 위치까지 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-23",
  "dateModified": "2026-09-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/stock-execution-strength-meaning"
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
      "name": "체결강도 100은 무슨 뜻인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "매수 체결량과 매도 체결량이 정확히 같다는 뜻으로, 매수·매도 어느 쪽도 우위가 아닌 균형 상태를 의미합니다." }
    },
    {
      "@type": "Question",
      "name": "체결강도가 높으면 주가가 오르나요",
      "acceptedAnswer": { "@type": "Answer", "text": "그렇게 단정할 수 없습니다. 체결강도는 그 순간 매수 체결이 많았다는 사실만 보여줄 뿐이고, 실제 가격은 참여자 심리 등 다른 요인에도 크게 좌우됩니다." }
    },
    {
      "@type": "Question",
      "name": "거래량과 체결강도는 같은 지표인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아닙니다. 거래량은 매수·매도를 구분하지 않은 총 체결 수량이고, 체결강도는 그 체결량을 매수·매도 비율로 나눈 지표입니다." }
    },
    {
      "@type": "Question",
      "name": "체결강도는 어디서 확인하나요",
      "acceptedAnswer": { "@type": "Answer", "text": "대부분의 HTS·MTS 종목 상세 화면이나 호가창 근처에서 확인할 수 있습니다. 키움증권은 [0178] 체결강도추이, 미래에셋증권은 카이로스 [0175] 체결강도순위 화면을 제공합니다." }
    },
    {
      "@type": "Question",
      "name": "체결강도만 보고 매매해도 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "이 글은 특정 종목의 매수·매도를 권하지 않는 정보 제공 목적의 글입니다. 체결강도는 저유동성 종목에서 쉽게 왜곡되는 순간 지표라, 다른 정보와 함께 참고하고 최종 판단은 투자자 본인이 하는 것이 안전합니다." }
    }
  ]
}
</script>
