---
keyword: ELS 뜻
title: ELS 뜻과 원금손실 낙인배리어 조건
slug: els-principal-loss-barrier
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 1,390 (PC 240 / 모바일 1,150, 2026-09-22 실측, check-keywords.yml)
gate1_pass: true (일반 주제 기준 월 500 이상 필요, 1,390회로 통과)
serp_check: |
  [게이트2 v3 판정 2026-09-22 - 통과]
  WebSearch "ELS 뜻 원금손실 조건 낙인 배리어 계산 예시" 상위 종합:
  cardif.co.kr(BNP파리바카디프생명, 보험사 공식) / shinhansec.com(신한투자증권,
  증권사 공식 PDF) / 50plus.or.kr(서울시 준정부기관 포털) / kcie.or.kr(금융투자자
  보호재단, 준정부) / velog.io(개인 개발자 블로그) / namu.wiki(백과) x2 /
  mynamuh.com(개인·소규모 용어사전 사이트) / iprovest.com(교보증권, 증권사 공식)
  1) 진입 여지 - 있음. velog.io·mynamuh.com 등 개인·소규모 콘텐츠가 상위권에
     섞여 있어 SERP가 완전히 잠겨 있지 않다.
  2) 검색 의도 - 개념·구조 이해형("ELS가 뭔지, 손실이 언제 나는지"). 홈택스
     신청이나 계산기 실행처럼 도구가 검색 의도를 대체하는 유형이 아니다.
  3) 답 완결 여부 - 부분적. 증권사·백과 페이지들은 낙인배리어 정의와 짧은
     계산 예시까지는 다루지만, 실제로 원금손실이 발생했던 공식 분쟁조정
     사례(배상비율·후속 제재)까지 연결해 "손실이 나면 실제로 어떻게 되는지"를
     보여주는 글은 상위에서 찾지 못했다.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (a) 낙인배리어 개념을 가상의 숫자(기준가 15,000, 배리어 50%)로 직접
      계산해 보여주는 예시.
  (b) 조기상환 조건표(예시 스케줄)를 실제 표로 정리해 "몇 % 이상이면
      돈을 언제 돌려받는지"를 시각화.
  (c) 2024년 홍콩H지수 ELS 사태의 실제 분쟁조정 배상비율(은행별 30~65%)과
      2026년까지 이어진 후속 제재 현황을 표로 정리 - 대부분의 "ELS 뜻"
      설명글이 다루지 않는, 실제로 손실이 났을 때 벌어진 일의 사례.
  (d) ELS 수익 4,500만 원 발생 시 배당소득세가 얼마인지 계산하는 예시.
primary_source: |
  1차 시도: 홍콩H지수 ELS 분쟁조정 결정 원문을 찾기 위해 KDI 경제정보센터
  정책자료(eiec.kdi.re.kr/policy/materialView.do?num=251462, "홍콩 H지수 ELS
  관련 국민은행 등 5개 은행의 대표사례에 대한 분쟁조정 결정")에 WebFetch
  1회 시도 → EGRESS_BLOCKED(2026-09-22). RULES.md 「1차 출처가 막혔을 때」
  (2026-09-12) 기준에 따라 교차검증으로 진행.
  독립 출처 5곳 이상(이투데이 etoday.co.kr, 이데일리 edaily.co.kr x2,
  아주경제 ajunews.com x2, 서울신문 seoul.co.kr, 네이트뉴스 news.nate.com -
  전부 서로 무관한 언론사, KDI 경제정보센터 eiec.kdi.re.kr는 준정부 연구
  기관으로 금감원 발표를 재게시)가 다음 핵심 수치에서 충돌 없이 일치:
  ① 금융분쟁조정위원회가 2024-05-13 국민·신한·하나·농협·SC제일 5개 은행
  대표사례에 대해 손실액의 30~65%를 배상하도록 결정, ② 기본배상비율은
  20~40%에서 결정(적합성 원칙 위반·설명의무 위반·부당권유 등 고려),
  ③ 은행별 대표사례 배상비율은 농협 65%, 국민 60%, 신한 55%, SC제일 55%,
  하나 30%, ④ 2024-10 기준 판매사 평균 자율배상비율 31.6%(손실 확정 계좌
  원금 10조4,000억 원, 손실금액 4조6,000억 원), ⑤ 2026-02-12 금감원이 5개
  은행에 대한 제재 수위를 당초 통보된 과징금 약 2조 원대에서 약 1조4,000억
  원대로 감경 확정.
  ELS 수익 과세(배당소득세 15.4% 원천징수, 금융소득종합과세 2천만 원 기준
  포함)는 조세금융신문(언론)·금융투자자보호재단 kcie.or.kr(준정부)·삼일PwC
  (회계법인) 3곳이 일치해 별도 검증했다. ELS 자체 정의·낙인배리어 개념은
  교보증권·신한투자증권 등 복수 증권사 공식 자료와 일치하는 일반적 상품
  구조 설명이라 추가 교차검증 없이 서술했다.
  본문의 "기준가 15,000/배리어 50%" 계산 예시와 "95-95-90-85-80-75" 조기상환
  조건표는 실제 특정 상품의 수치가 아니라 계산 원리를 보여주기 위한 예시임을
  본문에 명시했다.
기준일: 2026-09-22 (WebSearch 교차검증 확인일 기준)
tags: ELS뜻, 주가연계증권, 낙인배리어, 원금손실조건, 조기상환조건, 홍콩H지수ELS, ELS세금, 배당소득세, 파생결합증권, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-22). 게이트1은 이번 세션에서 check-keywords.yml로
  직접 실측(1,390회, 일반 주제 기준 500 이상). 게이트2는 RULES.md v3 기준으로
  정식 판정, 개인 블로그 진입 여지 있음을 확인. 게이트3은 낙인배리어 계산
  예시 + 조기상환 조건표 + 홍콩H지수 ELS 사태 실제 배상비율표 + 세금 계산
  예시로 충족. 게이트4는 1차 출처(KDI 재게시 자료) 접근이 EGRESS_BLOCKED로
  막혀, 서로 무관한 언론사 5곳 이상과 준정부 연구기관이 핵심 수치에서 충돌
  없이 일치하는 것을 확인해 교차검증으로 진행했다.
capture_guide: |
  (해당 없음 - 이번 편은 교차검증으로 게이트4를 충족해 캡처가 필요하지
  않다. 단, 사람이 최종 검토 시 아래 원문을 직접 열어 대조하면 더 안전하다.)
  1순위 - 금융감독원 홈페이지(https://www.fss.or.kr)에서 "홍콩 H지수 ELS
  분쟁조정" 보도자료 검색해 배상비율 원문 확인.
  2순위 - KDI 경제정보센터(https://eiec.kdi.re.kr/policy/materialView.do?num=251462)
  접속해 분쟁조정 결정 전문 캡처.
self_check: |
  [2026-09-22 판정 - gate_pass:true]
  게이트1 충족 - 이번 세션 check-keywords.yml 실측 1,390회(일반 주제 기준
  500 이상, 함께 조회한 MMF 뜻 2,560회보다는 낮지만 MMF는 일간 변동하는
  시장수익률 데이터라 고정된 1차 출처 수치를 확보할 수 없어 이번 편에서는
  제외하고 backlog에 기록).
  게이트2 충족 - RULES.md v3 기준 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 - 낙인배리어 계산 예시 + 조기상환 조건표 + 홍콩H지수 ELS
  사태 은행별 배상비율표 + 세금 계산 예시로 다른 "ELS 뜻" 설명글에 없는
  정보이득 확보.
  게이트4 충족(교차검증) - KDI 재게시 자료 1회 시도 EGRESS_BLOCKED. 서로
  무관한 언론사 5곳 이상 + 준정부 연구기관이 배상비율·과징금 수치에서
  충돌 없이 일치. ELS 세율(15.4%)도 언론·준정부·회계법인 3곳으로 별도 교차검증.
  카니벌라이제이션 점검 - grep 결과 43편(ISA 손익통산, isa-gain-loss-netting)
  본문에 "ELS·DLS 등"이 과세 대상 파생결합증권의 예시로 1회 짧게 언급될
  뿐, ELS 자체의 구조·손실조건·세금을 다루지 않는다. 그 외 1~71편 keyword
  전체 확인 결과 ELS를 다루는 편 없음. 43편 관련 문단에 링크로 연결했다.
  제목 "ELS 뜻과 원금손실 낙인배리어 조건" 20자·금지어 없음·"~이나/~부터~까지/
  ~인가요/~일까요" 없음. 슬러그 영문 소문자+하이픈 4단어
  (els-principal-loss-barrier).
  종목·상품 추천 표현 없음("○○증권 ELS 추천" 등 일절 없음), 단정 표현
  ("반드시"·"무조건"·"확실히"·"보장") 없음 - "보장"은 "원금보장이 되지
  않는 상품"이라는 사실 서술에서만 사용, 투자 결과를 보장하는 의미로는
  쓰지 않음.
  FAQ 5개와 JSON-LD 1:1 일치.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) - 본문(YAML 제외)에서 "-"
  (em대시) 0개 확인. "다만" 0회(대신 "단,"·"여기서 중요한 건" 등으로 전환).
  본문 `<mark>` 총 5개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약
  박스 제목을 "🔍 오늘 짚고 갈 포인트"로, 박스 색을 amber 계열(#fdf3e3/
  #c98a1f)로 최근 편들의 청록(#e8f7f5, 71편)·보라(#f1eefc, 70편)·초록
  (#eafaf1, 69편 / #eafaf3, 68편)과 다르게 바꿨다. 면책 문구도 이전 편들과
  다른 문장으로 새로 썼다. 목차 제외 본문 H2 6개 중 서술형 4개("ELS 뜻과
  기본 구조", "홍콩H지수 ELS 사태로 본 실제 손실 사례", "ELS 수익에 붙는
  세금 계산법", "ELS 투자 전 확인할 점"), 질문형 2개("낙인배리어는 어떻게
  계산하나요", "조기상환 조건은 어떻게 정해지나요")로 "~나요" 편중 없음
  (6개 중 2개, 33%).
  종합 판정: 4개 게이트 전부 충족, gate_pass:true.
---

<p><mark>ELS는 기초자산 가격이 계약서에 정해진 낙인배리어 밑으로 떨어지고 만기까지 회복하지 못하면 원금손실이 발생하는 상품입니다.</mark> ELS 뜻과 낙인배리어 계산법을 예시로 정리하고, 2024년 홍콩H지수 ELS 사태에서 실제로 어떤 배상 결정이 나왔는지도 함께 다룹니다.</p>

<div style="background:#fdf3e3;border:2px solid #c98a1f;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#7a5410;font-size:18px;">🔍 오늘 짚고 갈 포인트</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>기초자산이 <b>낙인배리어 밑으로</b> 떨어지고 만기까지 회복 못 하면 원금손실이 발생합니다.</li>
    <li>조기상환 조건을 충족하면 손실 전에 원금과 수익을 돌려받을 수 있습니다.</li>
    <li>2024년 홍콩H지수 ELS 사태에서 은행별 배상비율은 <mark>30~65%로 갈렸습니다</mark>.</li>
    <li>ELS 수익은 배당소득세 15.4%가 원천징수되고, 2천만 원을 넘으면 금융소득종합과세 대상입니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ELS 뜻과 기본 구조</li>
  <li>낙인배리어는 어떻게 계산하나요</li>
  <li>조기상환 조건은 어떻게 정해지나요</li>
  <li>홍콩H지수 ELS 사태로 본 실제 손실 사례</li>
  <li>ELS 수익에 붙는 세금 계산법</li>
  <li>ELS 투자 전 확인할 점</li>
  <li>ELS 관련 자주 나오는 질문</li>
</ol>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">ELS 뜻과 기본 구조</h2>

<p>ELS(주가연계증권, Equity Linked Securities)는 코스피200이나 홍콩H지수 같은 주가지수, 또는 특정 종목의 가격 흐름과 수익이 연결된 파생결합증권입니다. 예금처럼 원금이 보장되지 않는 투자상품입니다.</p>

<p>가입 시점에 두 가지 숫자가 정해집니다. 정해진 시점마다 얼마나 올라야 조기상환되는지(조기상환 조건), 얼마까지 떨어지면 원금손실이 시작되는지(낙인배리어)입니다. 이 두 숫자를 모르고 가입하면 상품이 어떻게 움직이는지 이해하기 어렵습니다.</p>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">낙인배리어는 어떻게 계산하나요</h2>

<p>낙인배리어(Knock-In Barrier)는 원금손실이 시작되는 기준선입니다. 기초자산 가격이 가입 시점(기준가) 대비 이 비율 밑으로 한 번이라도 떨어지고, 만기까지 상환 조건을 채우지 못하면 하락률만큼 원금손실이 확정됩니다.</p>

<p>계산 원리를 예시로 보겠습니다. <b>기초자산이 홍콩H지수이고 기준가가 15,000, 낙인배리어가 50%로 설정됐다고 가정</b>하면, 지수가 <mark>7,500 밑으로</mark> 떨어지는 순간 낙인이 발생합니다. 이후 만기까지 지수를 회복하지 못하면 하락한 비율만큼 원금이 줄어듭니다. 실제 상품의 기준가와 배리어 비율은 상품마다 다르므로, 이 숫자는 계산 원리를 보여주기 위한 예시일 뿐입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">상황</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">지수 수준(예시)</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">결과</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">낙인 발생 전</td>
      <td style="border:1px solid #ddd;padding:8px;">7,500 초과 유지</td>
      <td style="border:1px solid #ddd;padding:8px;">조기상환 조건 충족 시 원금+수익 상환</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">낙인 발생, 만기 전 회복</td>
      <td style="border:1px solid #ddd;padding:8px;">한때 7,500 밑으로, 만기에는 회복</td>
      <td style="border:1px solid #ddd;padding:8px;">원금손실 없이 상환(상품 조건에 따라 다름)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">낙인 발생, 만기까지 미회복</td>
      <td style="border:1px solid #ddd;padding:8px;">만기에도 7,500 밑</td>
      <td style="border:1px solid #ddd;padding:8px;">하락률만큼 원금손실 확정</td>
    </tr>
  </tbody>
</table>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">조기상환 조건은 어떻게 정해지나요</h2>

<p>ELS는 보통 만기(3년) 전에 6개월 단위로 조기상환 기회가 옵니다. 각 시점마다 기초자산이 기준가의 몇 % 이상이어야 조기상환되는지가 정해지는데, 이 비율은 시간이 지날수록 낮아지는 구조가 흔합니다.</p>

<p>아래는 자주 쓰이는 조기상환 조건 스케줄의 한 가지 예시입니다. <b>여기서 중요한 건</b> 실제 조건은 상품마다 다르므로, 가입 전 투자설명서에서 본인 상품의 조건을 직접 확인해야 한다는 점입니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">평가 시점</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">조기상환 조건(예시)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">6개월</td><td style="border:1px solid #ddd;padding:8px;">기준가의 95% 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">12개월</td><td style="border:1px solid #ddd;padding:8px;">기준가의 95% 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">18개월</td><td style="border:1px solid #ddd;padding:8px;">기준가의 90% 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">24개월</td><td style="border:1px solid #ddd;padding:8px;">기준가의 85% 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">30개월</td><td style="border:1px solid #ddd;padding:8px;">기준가의 80% 이상</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">36개월(만기)</td><td style="border:1px solid #ddd;padding:8px;">기준가의 75% 이상</td></tr>
  </tbody>
</table>

<p>이 예시대로라면 6개월 뒤 지수가 기준가의 95%만 넘어도 조기상환되어 수익을 받고 끝납니다. 반대로 매번 조건을 못 채우고 만기까지 가서 낙인배리어까지 건드리면, 그제야 원금손실 여부가 확정됩니다.</p>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">홍콩H지수 ELS 사태로 본 실제 손실 사례</h2>

<p>낙인배리어가 어떤 의미인지는 실제 사례로 보면 더 분명해집니다. 2021~2023년 홍콩H지수가 큰 폭으로 하락하면서, 이 지수를 기초자산으로 한 ELS 상품 다수가 낙인배리어를 건드려 대규모 원금손실이 발생했습니다.</p>

<p>금융분쟁조정위원회는 2024년 5월 13일 국민·신한·하나·농협·SC제일 5개 은행의 대표사례에 대해 배상 결정을 내렸습니다. <mark>기본배상비율은 20~40%</mark>에서 결정됐고, 여기에 투자자별 가감점을 더해 최종 배상비율이 정해졌습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">판매 은행</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">대표사례 배상비율</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #ddd;padding:8px;">NH농협은행</td><td style="border:1px solid #ddd;padding:8px;">65%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">KB국민은행</td><td style="border:1px solid #ddd;padding:8px;">60%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">신한은행</td><td style="border:1px solid #ddd;padding:8px;">55%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">SC제일은행</td><td style="border:1px solid #ddd;padding:8px;">55%</td></tr>
    <tr><td style="border:1px solid #ddd;padding:8px;">하나은행</td><td style="border:1px solid #ddd;padding:8px;">30%</td></tr>
  </tbody>
</table>

<p>2024년 10월 기준으로 판매사들이 자율배상한 비율은 평균 31.6%였고(손실이 확정된 계좌 원금 10조4,000억 원, 손실금액 4조6,000억 원), 배상은 투자자마다 조건에 따라 갈렸습니다. 이후 2026년 2월 12일에는 금융감독원이 5개 은행에 대한 제재 수위를 당초 통보한 과징금 약 2조 원대에서 약 1조4,000억 원대로 감경 확정했습니다. 단, 관련 사안은 2026년 5월에도 금융위원회 논의가 이어질 정도로 계속 진행 중이므로, 최신 진행 상황은 별도로 확인하는 편이 좋습니다.</p>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">ELS 수익에 붙는 세금 계산법</h2>

<p>ELS는 원금보장이 되지 않는 투자상품이라 수익이 발생하면 배당소득세 15.4%(지방소득세 포함)가 원천징수됩니다. 예금처럼 이자소득으로 과세되는 ELD(주가연계예금)와는 이 점에서 다릅니다.</p>

<p>예를 들어 3억 원을 연 5% 쿠폰(수익률)의 ELS에 넣어 3년 만기로 상환받았다면, 배당소득은 3억 원 × 5% × 3년 = 4,500만 원입니다. 이 <mark>4,500만 원에 15.4%를 원천징수</mark>하면 세금은 693만 원입니다. 3년치 수익이지만 세법상으로는 상환받은 해의 금융소득으로 한 번에 잡힙니다.</p>

<p>이 4,500만 원은 다른 이자·배당소득과 합쳐 연간 2천만 원을 넘으므로 금융소득종합과세 대상이 됩니다. 종합과세의 기준과 계산법은 <a href="https://sensitiveboss3.tistory.com/entry/financial-income-comprehensive-tax">금융소득종합과세 2천만원 기준 확인법</a> 편에서 자세히 다뤘습니다. ISA 계좌 안에 ELS를 담으면 손익통산과 세제혜택이 어떻게 적용되는지는 <a href="https://sensitiveboss3.tistory.com/entry/isa-gain-loss-netting">ISA 손익통산 계산 방법</a> 편을 참고하세요.</p>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">ELS 투자 전 확인할 점</h2>

<p>가입 전에 아래 항목을 투자설명서에서 직접 확인하는 편이 좋습니다.</p>

<ul style="line-height:1.8;">
  <li>기초자산이 무엇인지(지수 1개인지, 여러 개를 묶은 스텝다운형인지)</li>
  <li>낙인배리어 비율과 조기상환 조건 스케줄</li>
  <li>기초자산 중 하나라도 낙인배리어를 건드리면 손실이 확정되는 구조인지</li>
  <li>중도환매 시 손실 가능성과 환매수수료</li>
</ul>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>기초자산이 여러 개면 위험이 더 커집니다</b>
  <p style="margin:8px 0 0 0;">기초자산 2~3개를 묶은 상품은 그중 가장 많이 떨어진 자산 하나만으로 낙인 여부가 판정되는 경우가 흔합니다. 지수 1개짜리보다 손실 가능성을 더 보수적으로 봐야 합니다.</p>
</div>

<h2 style="border-left:6px solid #c98a1f;padding-left:12px;margin-top:36px;">ELS 관련 자주 나오는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ELS와 ELD는 뭐가 다른가요</summary>
  <p style="margin:10px 0 0 0;">ELS는 원금이 보장되지 않는 투자상품으로 수익이 배당소득으로 과세됩니다. ELD(주가연계예금)는 원금이 보장되는 예금상품으로 수익이 이자소득으로 과세됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">낙인배리어를 건드리면 무조건 손실인가요</summary>
  <p style="margin:10px 0 0 0;">아니요. 낙인이 발생해도 만기 전에 기초자산이 회복해 상환 조건을 채우면 손실 없이 상환될 수 있습니다. 만기까지 조건을 못 채운 경우에만 원금손실이 확정됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">조기상환에 계속 실패하면 어떻게 되나요</summary>
  <p style="margin:10px 0 0 0;">평가 시점마다 조건을 채우지 못하면 상환 없이 다음 평가 시점까지 계속 투자 상태로 남습니다. 만기까지 조건을 못 채우고 낙인배리어까지 건드렸다면 그때 원금손실 여부가 최종 확정됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ELS 수익도 금융소득종합과세에 포함되나요</summary>
  <p style="margin:10px 0 0 0;">네. ELS 수익은 배당소득으로 분류되어 다른 이자·배당소득과 합산됩니다. 연간 합계가 2천만 원을 넘으면 금융소득종합과세 대상이 됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">홍콩H지수 ELS 사태 배상은 전액 받을 수 있나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 분쟁조정 결과 기본배상비율은 20~40%였고, 은행별 대표사례 배상비율도 30~65%로 투자자와 판매 은행에 따라 달랐습니다. 손실액 전부를 돌려받은 사례는 아닙니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://eiec.kdi.re.kr/policy/materialView.do?num=251462" target="_blank" rel="noopener">KDI 경제정보센터 - 홍콩 H지수 ELS 관련 5개 은행 대표사례 분쟁조정 결정</a></li>
    <li><a href="https://www.fss.or.kr" target="_blank" rel="noopener">금융감독원</a></li>
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a></li>
  </ul>
  기준일: 2026년 9월 기준. 분쟁조정·제재 관련 후속 절차는 계속 진행 중이므로
  최신 내용은 금융감독원에서 다시 확인하시기 바랍니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 ELS라는 상품 구조와 과세 방식을 설명하는 정보성 글이며, 특정
증권사·판매사나 상품 가입을 권하지 않습니다. 가입 여부와 그 결과에 대한
책임은 투자자 본인에게 있습니다. 상품별 조건과 세율은 바뀔 수 있으니
가입 전 투자설명서와 최신 세법을 직접 확인해 주세요.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "ELS 뜻과 원금손실 낙인배리어 조건",
  "description": "ELS 뜻과 낙인배리어 계산법, 조기상환 조건, 홍콩H지수 ELS 사태의 실제 배상비율, ELS 수익 세금 계산법을 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-22",
  "dateModified": "2026-09-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/els-principal-loss-barrier"
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
      "name": "ELS와 ELD는 뭐가 다른가요",
      "acceptedAnswer": { "@type": "Answer", "text": "ELS는 원금이 보장되지 않는 투자상품으로 수익이 배당소득으로 과세됩니다. ELD(주가연계예금)는 원금이 보장되는 예금상품으로 수익이 이자소득으로 과세됩니다." }
    },
    {
      "@type": "Question",
      "name": "낙인배리어를 건드리면 무조건 손실인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 낙인이 발생해도 만기 전에 기초자산이 회복해 상환 조건을 채우면 손실 없이 상환될 수 있습니다. 만기까지 조건을 못 채운 경우에만 원금손실이 확정됩니다." }
    },
    {
      "@type": "Question",
      "name": "조기상환에 계속 실패하면 어떻게 되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "평가 시점마다 조건을 채우지 못하면 상환 없이 다음 평가 시점까지 계속 투자 상태로 남습니다. 만기까지 조건을 못 채우고 낙인배리어까지 건드렸다면 그때 원금손실 여부가 최종 확정됩니다." }
    },
    {
      "@type": "Question",
      "name": "ELS 수익도 금융소득종합과세에 포함되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. ELS 수익은 배당소득으로 분류되어 다른 이자·배당소득과 합산됩니다. 연간 합계가 2천만 원을 넘으면 금융소득종합과세 대상이 됩니다." }
    },
    {
      "@type": "Question",
      "name": "홍콩H지수 ELS 사태 배상은 전액 받을 수 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 분쟁조정 결과 기본배상비율은 20~40%였고, 은행별 대표사례 배상비율도 30~65%로 투자자와 판매 은행에 따라 달랐습니다. 손실액 전부를 돌려받은 사례는 아닙니다." }
    }
  ]
}
</script>
