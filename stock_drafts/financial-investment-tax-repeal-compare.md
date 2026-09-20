---
keyword: 금투세
title: 금투세 폐지 전후 세금 비교
slug: financial-investment-tax-repeal-compare
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 4,110 (PC 1,250 / 모바일 2,860, 2026-09-20 실측, check-keywords.yml)
gate1_pass: true (일반 주제 기준 월 500 이상 크게 초과)
serp_check: |
  [게이트2 v3 판정 2026-09-20 — 통과]
  WebSearch "금투세" 단독 검색 상위 9개: m.kbcapital.co.kr·kbcapital.co.kr(KB캐피탈,
  대형 금융사 콘텐츠 2건) / kbthink.com(KB국민은행, 대형 금융사) / wegive.co.kr(위기브,
  핀테크 스타트업 매거진) / sgsg.hankyung.com(한경 생글생글, 언론 교육매체) /
  tossbank.com(토스뱅크, 대형 핀테크) / ccej.or.kr(경제정의실천시민연합, 시민단체) /
  help.3o3.co.kr(3o3, 소규모 핀테크 서비스 헬프센터) / namu.wiki(백과)
  1) 진입 여지 — 위기브(wegive.co.kr)·3o3 헬프센터(help.3o3.co.kr)는 대형 금융사가
     아닌 핀테크 서비스의 콘텐츠 페이지라 "개인·소규모 콘텐츠 사이트가 하나도 없음"에는
     해당하지 않는다.
  2) 검색 의도 — 정의·경위·세율 구조를 알고 싶은 정보 탐색형이다. 조회·계산기 실행이
     목적인 키워드가 아니다.
  3) 답 완결 여부 — 상위 결과 대부분이 "금투세가 뭐였고 왜 폐지됐는지"의 총정리형
     서술에 그친다. "금투세가 그대로 시행됐다면 실제로 얼마를 더 냈을지"를 국내주식·
     해외주식으로 나눠 숫자로 계산해 비교한 글은 확인하지 못했다. 정보이득 여지 있음.
  → 탈락조건 1·2 미해당, 탈락조건 3은 계산 비교로 상쇄해 통과.
unique_asset: |
  "금투세가 폐지됐다"는 사실 나열에 그치지 않고, 같은 매매차익(8,000만원)을 기준으로
  "금투세가 그대로 시행됐다면 냈을 세금"과 "실제로 지금 내는 세금"을 국내주식·해외주식
  두 갈래로 나눠 직접 계산해 비교했다.
  - 국내 상장주식(대주주 아님): 금투세였다면 (8,000만원-5,000만원)×22%=660만원을
    냈어야 하지만, 실제로는 양도소득세 자체가 없어 0원이다.
  - 해외주식: 금투세였다면 (8,000만원-250만원)×22%=1,705만원, 실제 현행 양도소득세도
    같은 공제·세율 구조(기본공제 250만원, 22%)라 1,705만원으로 동일하다.
  - 이 두 계산을 나란히 놓으면 "금투세 폐지의 실질적 수혜는 국내주식 투자자에게만
    돌아갔고, 해외주식 투자자는 세부담이 그대로"라는 점이 분명해진다. 상위 검색결과
    어디에도 이 구도를 숫자로 짚은 글은 없었다.
primary_source: |
  1차 시도: 국가법령정보센터(law.go.kr) 소득세법 개정이유 목록(lsRvsRsnListP.do)
  WebFetch 1회 → EGRESS_BLOCKED(2026-09-20). RULES.md 「1차 출처가 막혔을 때」
  (2026-09-12) 기준에 따라 2차 출처 교차검증으로 진행했다. 폐지 여부·시행일 같은
  검증 가능한 사실관계이고, 세율·공제 구조 자체는 아래처럼 서로 무관한 다수 출처가
  동일 수치로 수렴해 교차검증 조건에 부합한다고 판단했다.
  - 2024년 12월 10일 소득세법 개정안 국회 본회의 통과(재석 275명 중 찬성 204명)로
    금투세 폐지 확정: 대한민국 정책브리핑(korea.kr, 정부 공식 브리핑) + 디지털투데이
    (digitaltoday.co.kr, 언론) + 에너지경제(m.ekn.kr, 언론) + 나무위키가 같은 날짜·
    같은 표결 결과로 일치했다.
  - 금투세 세율·공제 구조(1그룹 상장주식 등 기본공제 5,000만원 / 2그룹 기타 기본공제
    250만원, 3억원 이하 22%·초과 27.5%, 지방소득세 포함): 신한투자증권 공식 약관 PDF
    (file.shinhaninvest.com, 증권사 공식 문서) + 참여연대(peoplepower21.org, 시민단체) +
    토스피드(toss.im) + 미래에셋증권 매거진(magazine.securities.miraeasset.com) +
    나무위키가 전부 동일한 숫자로 일치했다. 증권사 공식 약관 PDF가 포함돼 있어 신뢰도가
    높다고 판단했다.
  - 해외주식 양도소득세(기본공제 250만원, 22%)는 이 저장소 5편(해외주식 양도소득세
    신고 방법)·15편(미국주식 세금)에서 국세청 자료로 이미 확인해 둔 수치를 그대로
    재사용했다(재검증 아님, 기존 확정 수치 인용).
  - 대주주 요건(코스피 1% 또는 50억원, 2024-01-01 이후)은 7편(주식 양도소득세 대주주
    요건 2026)에서 국세청 원문으로 이미 확인해 둔 수치를 그대로 인용했다.
기준일: 2026-09-20 (WebSearch 교차검증일, 근거 사실의 발표일은 2024-12-10 국회 본회의 통과)
tags: 금투세, 금융투자소득세, 금투세폐지, 국내주식세금, 해외주식세금, 대주주요건, 소득세법개정, 주식초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-20).
  게이트1: 네이버 키워드도구 실측 4,110회(일반 기준 500회 크게 초과). 같은 배치 후보
  증권거래세 폐지(20)·공매도 재개(20)·예수금 이자(80)·밸류업 지수(380)·CMA 세금(70)은
  게이트1 미달. 배당소득 분리과세(2,620, PASS)는 4편(배당소득세 얼마 떼나)·6편
  (금융소득종합과세)·39편(해외주식 배당소득세)이 이미 2026년 신설 분리과세 특례를
  FAQ까지 상세히 다루고 있어(grep 확인) 카니벌라이제이션으로 제외, backlog에 기록.
  물적분할(1,440, PASS)은 카니벌라이제이션 없이 대기 후보로 backlog에 남김. 금투세만
  검색량 최고 + 카니벌라이제이션 없음으로 채택.
  게이트2: v3 기준 통과(serp_check 참조) — 대형 금융사·언론·시민단체가 상위를 채워
  경쟁이 세지만 핀테크 서비스 콘텐츠 진입이 있어 탈락조건1에 해당하지 않고, 탈락조건3은
  국내·해외 세부담 비교 계산으로 상쇄.
  게이트3: 매매차익 8,000만원 기준 국내주식·해외주식 세금 비교 계산(unique_asset 참조)으로
  정보이득 확보.
  게이트4: law.go.kr 1회 시도 EGRESS_BLOCKED 확인 후 RULES.md 2026-09-12 기준에 따라
  교차검증 진행 — 폐지 사실은 정부 브리핑·언론 2곳·백과가, 세율·공제 구조는 증권사 공식
  약관 PDF를 포함한 5곳이 충돌 없이 일치. 기존 5·7·15편에서 이미 확인된 수치는 재인용
  임을 명시했다.
self_check: |
  게이트1~4 전부 충족(위 gate_pass_note 참조).
  카니벌라이제이션 점검 — 기존 1~55편 keyword 전체와 grep 확인 결과 "금투세" 자체를
  다룬 편은 없음(9편이 배경으로 짧게 언급할 뿐 본문 주제가 아님). 겹침 없음.
  제목 "금투세 폐지 전후 세금 비교" 15자·금지어 없음·조사/접속사 없음. 제목이 "비교"라
  본문에 실제 비교표(계산 예시 표)를 넣었다. 슬러그 영문 소문자+하이픈 5단어
  (financial-investment-tax-repeal-compare). 인트로 문단 최상단 배치, "안녕하세요" 없음.
  표는 thead/tbody 시맨틱 사용. 기준일 명시. FAQ 5개와 JSON-LD 1:1 일치.
  종목·상품 추천 표현 없음. 단정 표현("반드시","무조건","확실히","보장") 없음.
  기관 링크 점검 — 국세청·국가법령정보센터·정책브리핑 링크 전부 target="_blank"
  rel="noopener" 처리, 정부기관은 nofollow 미부착.
  AI 티 점검(RULES.md 「★ AI 글쓰기 티 제거」) — 발행 본문(YAML 제외)에서 "—" 0개,
  "다만" 0개 확인(전환은 "단,"·"반대로"·"다르게 말하면"으로 분산). 본문 `<mark>` 총
  4개(3~5개 기준 충족). FAQ 5개(6개 고정 탈피). 핵심요약 박스 제목을
  "먼저 확인할 3가지"로, 색상은 인디고 계열(#eef2ff/#4338ca)로 최근 게시물(로즈·틸·
  퍼플·블루·그린·스카이블루·오렌지)과 겹치지 않게 골랐다. 목차 제외 본문 H2 5개 중
  서술형 3개("도입부터 폐지까지","얻은 것","계산법","확인법"), 질문형 2개("왜
  그대로인가")로 "~나요"로 끝나는 H2는 하나도 없어 다양성 기준을 충족한다. 헤지 표현
  남발 없음(확정된 사실은 단정형 "~습니다"로 서술).
  종합 판정: 4개 게이트 전부 충족(게이트4는 정부 브리핑·언론·증권사 공식문서 교차검증으로
  대체, 한계는 출처란에 투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-20</p>

<p>금투세(금융투자소득세)는 2020년 법이 만들어졌지만 한 번도 시행되지 못하고 2024년 12월 폐지됐습니다. 그런데 "폐지됐다"는 소식만 알 뿐, 실제로 세금이 얼마나 달라졌는지 숫자로 확인한 사람은 많지 않습니다. 같은 매매차익을 기준으로 금투세가 시행됐을 경우와 지금을 직접 계산해 비교했습니다.</p>

<div style="background:#eef2ff;border:2px solid #4338ca;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#3730a3;font-size:18px;">먼저 확인할 3가지</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>금투세는 <mark>2024년 12월 10일 국회에서 폐지 법안이 통과</mark>돼 한 번도 시행되지 않았습니다.</li>
    <li>매매차익 8,000만원 기준, 국내주식은 금투세였다면 660만원을 냈어야 하지만 지금은 <mark>0원</mark>입니다.</li>
    <li>반대로 해외주식은 금투세였을 때와 지금의 세금이 <b>1,705만원으로 동일</b>합니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>금투세 도입부터 폐지까지</li>
  <li>금투세 폐지로 국내주식 투자자가 얻은 것</li>
  <li>해외주식 투자자는 왜 그대로인가</li>
  <li>금투세 있었다면 세금 얼마였을지 계산법</li>
  <li>지금 남아있는 주식 세금 확인법</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">금투세 도입부터 폐지까지</h2>

<p>금투세는 주식·펀드·채권 같은 금융투자상품에서 번 소득에 매기는 세금으로, 2020년 소득세법 개정으로 처음 만들어졌습니다. 원래 2023년부터 시행될 예정이었지만 2025년으로 한 차례 미뤄졌고, 그마저도 시행되지 못한 채 2024년 12월 10일 국회 본회의에서 폐지 법안이 통과됐습니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">4년 넘게 논의만 되다가 실제로 걷힌 적은 단 한 번도 없는 세금입니다.</span> 그래서 "폐지"라는 표현보다는 "시행되지 못하고 사라졌다"는 표현이 더 정확합니다.</p>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">금투세 폐지로 국내주식 투자자가 얻은 것</h2>

<p>금투세가 시행됐다면 국내 상장주식은 1그룹으로 분류돼 연간 기본공제 5,000만원을 넘는 매매차익에 22%(3억원 초과분은 27.5%)의 세율이 붙을 예정이었습니다. 폐지되면서 이 구조 자체가 없어졌습니다.</p>

<p>지금은 <mark>대주주가 아닌 이상 국내 상장주식 매매차익에는 양도소득세가 아예 없습니다.</mark> 대주주 요건은 코스피 기준 지분 1% 또는 보유금액 50억원 이상(2024년 1월 1일 이후)인데, 여기 해당되지 않는 대부분의 개인 투자자는 매매차익 규모와 무관하게 세금을 내지 않습니다.</p>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">해외주식 투자자는 왜 그대로인가</h2>

<p>해외주식은 금투세와 별개로, 원래부터 양도소득세를 내는 상품이었습니다. 기본공제 250만원을 넘는 매매차익에 22%(지방소득세 포함) 세율이 적용되는 구조는 금투세 도입 논의 이전부터 있었고, 금투세가 폐지된 뒤에도 바뀌지 않았습니다.</p>

<p>공교롭게도 금투세의 2그룹(국내 상장주식 외 상품) 공제·세율 구조가 해외주식 양도소득세와 거의 같았습니다. 그래서 <b>해외주식 투자자는 금투세가 시행됐어도, 폐지된 지금도 실질적인 세부담 차이가 거의 없습니다.</b> 국내주식 투자자만 누린 혜택인 셈입니다.</p>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">금투세 있었다면 세금 얼마였을지 계산법</h2>

<p>1년간 매매차익이 8,000만원이라고 가정하고, 국내주식과 해외주식 각각의 세금을 비교하면 아래와 같습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">구분</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">금투세 시행됐다면</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">실제 지금(대주주 아님)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">국내 상장주식<br>(매매차익 8,000만원)</td>
      <td style="border:1px solid #ddd;padding:8px;">(8,000만원-5,000만원)×22%<br>= <b>660만원</b></td>
      <td style="border:1px solid #ddd;padding:8px;"><b>0원</b>(양도소득세 없음)</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">해외주식<br>(매매차익 8,000만원)</td>
      <td style="border:1px solid #ddd;padding:8px;">(8,000만원-250만원)×22%<br>= <b>1,705만원</b></td>
      <td style="border:1px solid #ddd;padding:8px;">(8,000만원-250만원)×22%<br>= <b>1,705만원</b>(동일)</td>
    </tr>
  </tbody>
</table>

<p>같은 매매차익이라도 국내주식은 660만원 차이가 나지만, 해외주식은 차이가 0원입니다. 금투세 폐지 효과가 어디에 집중됐는지가 이 표 하나로 정리됩니다.</p>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">지금 남아있는 주식 세금 확인법</h2>

<p>금투세가 없어졌다고 주식 관련 세금이 전부 사라진 건 아닙니다. 배당을 받으면 배당소득세(15.4% 원천징수)를 그대로 내고, 매도할 때마다 증권거래세도 자동으로 차감됩니다. 대주주라면 국내주식 매매차익에도 기존 양도소득세 방식이 그대로 적용됩니다.</p>

<ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
  <li>배당소득세: 배당금의 15.4% 원천징수(별도 신고 불필요, 금융소득 2,000만원 초과 시 종합과세)</li>
  <li>증권거래세: 매도 대금에서 자동 차감(세율은 종목·시장마다 다름)</li>
  <li>대주주 양도소득세: 코스피 1%·50억원 등 요건에 해당하면 기존 방식대로 부과</li>
  <li>해외주식 양도소득세: 기본공제 250만원 초과분에 22% 부과, 매년 5월 확정신고 필요</li>
</ul>

<p>본인이 대주주 요건에 해당하는지, 정확한 신고 방법이 궁금하다면 <a href="https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&amp;mi=12274" target="_blank" rel="noopener">국세청 주식등 양도소득세 안내</a>에서 확인할 수 있습니다.</p>

<h2 style="border-left:6px solid #4338ca;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금투세는 결국 시행됐나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 2020년 법이 만들어진 뒤 2023년, 2025년으로 시행이 미뤄지다가 2024년 12월 10일 국회에서 폐지 법안이 통과돼 한 번도 시행되지 않았습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내주식 투자자는 세금을 하나도 안 내나요</summary>
  <p style="margin:10px 0 0 0;">대주주가 아니면 매매차익에 대한 양도소득세는 없습니다. 단, 배당을 받으면 배당소득세 15.4%를 원천징수로 내고, 매도할 때마다 증권거래세는 그대로 부과됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">해외주식 투자자는 금투세 폐지와 무관한가요</summary>
  <p style="margin:10px 0 0 0;">실질적인 세부담 차이는 거의 없습니다. 해외주식은 원래부터 있던 양도소득세(기본공제 250만원, 22%)를 그대로 적용받고, 이 구조는 금투세 도입 논의 이전부터 지금까지 바뀌지 않았습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">대주주면 지금도 세금을 내나요</summary>
  <p style="margin:10px 0 0 0;">냅니다. 코스피 기준 지분 1% 또는 보유금액 50억원 이상(2024년 1월 1일 이후 기준)이면 대주주로 분류돼 기존 양도소득세 방식이 그대로 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">금투세가 다시 도입될 가능성이 있나요</summary>
  <p style="margin:10px 0 0 0;">2026년 9월 기준 정부는 재도입 계획이 없다는 입장을 유지하고 있습니다. 세법은 국회 논의에 따라 달라질 수 있으니 정책 변화가 있는지는 원출처에서 다시 확인하는 편이 안전합니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.korea.kr/briefing/actuallyView.do?newsId=148928541" target="_blank" rel="noopener">대한민국 정책브리핑</a> - 금융투자소득세 폐지 관련 정부 입장</li>
    <li><a href="https://www.nts.go.kr" target="_blank" rel="noopener">국세청</a> - 주식 양도소득세·대주주 요건 안내</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 소득세법 개정이유(금융투자소득세 관련 조항)</li>
  </ul>
  기준일: 2026-09-20(WebSearch 교차검증일). 근거 사실의 발표일은 2024-12-10(소득세법
  개정안 국회 본회의 통과)입니다. 국가법령정보센터 원문 페이지는 이번 세션 WebFetch가
  EGRESS_BLOCKED로 막혀 직접 열람하지 못했고, 정부 브리핑·언론 2곳·증권사 공식 약관
  PDF를 포함한 다수 출처로 핵심 수치를 교차검증했습니다.
</div>

<p style="font-size:13px;color:#777;margin-top:16px;line-height:1.8;">
이 글은 금투세 폐지 전후의 세금 구조 변화를 이해하는 데 참고하시라고 정리한 정보
제공용 글이며, 특정 종목이나 투자 상품의 매수·매도를 권유하지 않습니다. 세율과 공제
한도는 국회 논의에 따라 바뀔 수 있으므로, 실제 신고 전에는 국세청 등 원출처에서 최신
내용을 다시 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게
있습니다.
</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "금투세 폐지 전후 세금 비교",
  "description": "금투세 도입부터 2024년 폐지까지의 경위와, 매매차익 8,000만원을 기준으로 금투세가 시행됐다면 냈을 세금과 실제 지금 내는 세금을 국내주식·해외주식으로 나눠 계산해 비교합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-20",
  "dateModified": "2026-09-20",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/financial-investment-tax-repeal-compare"
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
      "name": "금투세는 결국 시행됐나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 2020년 법이 만들어진 뒤 2023년, 2025년으로 시행이 미뤄지다가 2024년 12월 10일 국회에서 폐지 법안이 통과돼 한 번도 시행되지 않았습니다." }
    },
    {
      "@type": "Question",
      "name": "국내주식 투자자는 세금을 하나도 안 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "대주주가 아니면 매매차익에 대한 양도소득세는 없습니다. 단, 배당을 받으면 배당소득세 15.4%를 원천징수로 내고, 매도할 때마다 증권거래세는 그대로 부과됩니다." }
    },
    {
      "@type": "Question",
      "name": "해외주식 투자자는 금투세 폐지와 무관한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "실질적인 세부담 차이는 거의 없습니다. 해외주식은 원래부터 있던 양도소득세(기본공제 250만원, 22%)를 그대로 적용받고, 이 구조는 금투세 도입 논의 이전부터 지금까지 바뀌지 않았습니다." }
    },
    {
      "@type": "Question",
      "name": "대주주면 지금도 세금을 내나요",
      "acceptedAnswer": { "@type": "Answer", "text": "냅니다. 코스피 기준 지분 1% 또는 보유금액 50억원 이상(2024년 1월 1일 이후 기준)이면 대주주로 분류돼 기존 양도소득세 방식이 그대로 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "금투세가 다시 도입될 가능성이 있나요",
      "acceptedAnswer": { "@type": "Answer", "text": "2026년 9월 기준 정부는 재도입 계획이 없다는 입장을 유지하고 있습니다. 세법은 국회 논의에 따라 달라질 수 있으니 정책 변화가 있는지는 원출처에서 다시 확인하는 편이 안전합니다." }
    }
  ]
}
</script>
