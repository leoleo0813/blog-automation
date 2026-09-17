---
keyword: ISA 손익통산
title: ISA 손익통산 계산 방법
slug: isa-gain-loss-netting
keyword_class: 자동화 가능
publish_effort: oneclick
monthly_search_volume: 120 (PC 40 / 모바일 80)
gate1_pass: true (세부·제도 주제 기준 월 100 이상 필요)
serp_check: |
  [게이트2 v3 판정 2026-09-17 — 통과]
  WebSearch "ISA 계좌 손익통산 뜻 계산 방법" + "ISA 만기 손익통산 비과세 200만원 초과
  계산" + "ISA 국내상장주식 매매차익 비과세 손익통산 제외" 상위 종합:
  toss.im(토스, 핀테크 대기업 콘텐츠) / kbthink.com(KB 금융 용어사전) / kbsec.com(KB증권
  공식) / obank.kbstar.com(KB국민은행 공식) / bluedino.kr(개인/소규모 콘텐츠, 4회 등장) /
  frism.io(개인 투자자문 블로그) / mynamuhbegin.com(나무증권 블로그형 콘텐츠) /
  financecoffeechat.com·calcmoney.kr·easyzetec.com·lifeinfobox.com(개인 블로그, 총 5회
  등장) / 신한투자증권·한국투자증권·삼성증권매거진(증권사 공식) / eugenefn.com(유진투자증권
  상품설명서 PDF)
  1) 진입 여지 — 있음. bluedino.kr·frism.io·financecoffeechat.com·calcmoney.kr·
     easyzetec.com·lifeinfobox.com 등 개인/소규모 콘텐츠가 두 차례 검색 모두 상위권에
     다수 진입해 SERP가 잠겨 있지 않음.
  2) 검색 의도 — 정보 탐색+계산("손익통산이 뭔지, 어떻게 계산되는지"). 조회·신청·계산기
     실행 의도가 지배적이지 않음.
  3) 답 완결 여부 — 부분적. 상위 블로그 다수가 손익통산의 기본 개념과 200만원 비과세
     초과분 계산까지는 다루지만, "국내 상장주식 매매차익은 애초에 비과세라 통산 대상
     이익에서 제외되지만 손실은 통산에 포함되어 다른 상품 이익을 줄여준다"는 비대칭
     구조를 두 가지 방향(이익 케이스/손실 케이스) 계산 예시로 함께 보여주는 글은 찾지
     못했다. 정보이득 여지 있음.
  → 3개 탈락 조건 모두 미해당, 게이트2 통과.
unique_asset: |
  (1) 손익통산 비대칭 구조표 — 국내 상장주식 매매"이익"은 애초 비과세라 통산 대상에서
      제외되지만, 매매"손실"은 통산에 포함되어 다른 상품(펀드·파생결합증권 등)의 과세
      대상 이익을 줄여준다는 점을 대비해서 정리.
  (2) 계산 예시 두 가지 — ① 펀드이익 500만원 + 국내주식손실 200만원 → 순이익 300만원
      기준 과세(200만원 비과세, 초과 100만원에 9.9% 분리과세=99,000원) ② 국내주식이익
      400만원 + 펀드손실 100만원 → 국내주식이익은 통산 제외돼 그대로 비과세 수령, 통산
      대상은 펀드손실 100만원뿐이라 순손실이 되어 세금 0원. 기존 3편(ISA 계좌 한도와
      비과세 혜택)은 유형별 납입한도·비과세 한도 구조를 다루지만 손익통산 계산 방식은
      다루지 않아 검색 의도와 정보이득이 겹치지 않는다(cannibalization_note 참고).
primary_source: |
  1차 시도: 금융위원회 "ISA(개인종합자산관리계좌) 주요정책문답"
  (https://www.fsc.go.kr/po020201/27339) WebFetch 1회 시도 → EGRESS_BLOCKED(2026-09-17).
  대조군으로 무관한 도메인(www.google.com) 1회 추가 시도했으나 동일하게 EGRESS_BLOCKED로
  확인돼, 특정 도메인이 아니라 이번 세션의 전면 차단으로 판단했다(RULES.md 누적 기록
  패턴과 일치, 그 이상 재시도하지 않음).
  RULES.md 「1차 출처가 막혔을 때」(2026-09-12) 기준에 따라 2차 출처 교차검증으로
  진행했다 — 서로 무관한 독립 출처가 3곳을 넘는 5곳 이상 확인됐고, 그중 언론 1곳
  (조세일보, payzon.co.kr) + 준정부 연구기관 2곳(KDI 경제정보센터 eiec.kdi.re.kr,
  국회예산정책처 NABO 2026-04-30 보고서 nabo.go.kr) + 준정부 성격 재단(금융투자자보호재단
  kcie.or.kr)이 포함된다. 핵심 수치(비과세 한도 일반형 200만원/서민형·농어민형 400만원,
  초과분 9.9% 분리과세, "국내상장주식 매매이익은 통산 제외·매매손실은 통산 포함"이라는
  비대칭 구조)가 이들 출처와 다수의 증권사 공식 콘텐츠(신한투자증권·한국투자증권·
  삼성증권매거진·유진투자증권 상품설명서)에서 충돌 없이 일치했다. 비과세 한도·세율
  수치는 이미 3편(isa-limit-benefit, 조세특례제한법 제91조의18 국세법령정보시스템 원문
  확인)에서 사람이 직접 원문 캡처로 확정한 값과도 정확히 일치해(일반형 200만원/서민형·
  농어민형 400만원/9.9%) 교차 신뢰도를 보강했다.
기준일: 2026-09-17 (WebSearch 확인일)
tags: ISA손익통산, ISA계좌, ISA비과세, 손익통산계산, 개인종합자산관리계좌, 절세계좌, ISA세금, 주식초보, 재테크초보
gate_pass: true
gate_pass_note: |
  4개 게이트 전부 충족(2026-09-17).
  게이트1: 네이버 키워드도구 실측 120회(check-keywords.yml, 2026-09-17 — 세부·제도 기준
  100회 이상). 같은 배치에서 해외주식 이중과세 조정(20회)·주식 매매내역 조회 방법
  (20회)·코스피 상장요건(20회)·배당소득 원천징수 환급(20회)·IRP 계좌 개설 방법(410회,
  기준500 미달)·배당소득세 신고 방법(20회)·해외주식 매도 후 환전 시점(20회)은 게이트1
  미달로 탈락. 이전 배치(ISA 만기 연금계좌 이체·RP통장 이자소득세·배당세액공제 계산방법·
  미수동결계좌 해제방법·해외주식 상속세 신고·증권거래세 면제 대상·증권거래세 신고납부
  방법·신주인수권증서 매매 방법)도 전부 20회로 게이트1 미달.
  게이트2: v3 기준 통과(serp_check 참조) — 개인·소규모 블로그 진입 여지 있고, 손익통산
  비대칭 구조를 두 방향 계산 예시로 보여주는 글이 상위 결과에 부재해 정보이득 여지 있음.
  게이트3: 비대칭 구조표 + 이익/손실 두 방향 계산 예시로 정보이득 확보.
  게이트4: fsc.go.kr WebFetch 1회 시도 EGRESS_BLOCKED, 대조군(google.com)도 차단돼 세션
  전면 차단 확인 후, RULES.md 2026-09-12 기준에 따라 독립 출처 5곳 이상(언론 1곳+준정부
  연구기관 2곳+준정부 성격 재단 1곳 포함) 교차검증, 핵심 수치 충돌 없음 확인 후 진행.
  비과세 한도·세율 수치는 3편에서 원문으로 이미 확정된 값과도 일치해 신뢰도를 보강했다.
self_check: |
  게이트1 충족 — 네이버 키워드도구 실측 120회(세부·제도 기준 100회 이상).
  게이트2 통과 — RULES.md 게이트2 v3 기준, 3개 탈락 조건 모두 미해당(serp_check 참조).
  게이트3 충족 — 국내상장주식 매매이익(통산 제외)·매매손실(통산 포함) 비대칭 구조표와
  이익 케이스/손실 케이스 두 방향 계산 예시로 상위 결과가 다루지 않는 각도를 확보했다.
  게이트4 — fsc.go.kr 직접 열람은 막혔고(대조군 google.com도 차단, 세션 전면 차단),
  독립 출처 5곳 이상(언론 1곳, 준정부 연구기관 2곳, 준정부 성격 재단 1곳 포함)이 핵심
  수치에서 충돌 없이 일치함을 확인해 교차검증으로 진행했다. 비과세 한도·세율은 3편에서
  원문으로 확정한 값(일반형 200만원/서민형·농어민형 400만원/9.9%)과도 일치.
  카니벌라이제이션 점검 — 3편(ISA 계좌 한도와 비과세 혜택)은 유형별 납입한도·비과세
  한도 구조와 "생산적금융 ISA 혼동 해소"가 중심이고 손익통산 계산 방식은 다루지 않아
  검색 의도가 겹치지 않는다(draft_path 내 grep 확인, 손익통산 언급 0회). 본문에서 3편으로
  내부 링크.
  기관 링크 점검(RULES.md「기관 링크 필수」) — 국세청·국가법령정보센터 안내 문장과 하단
  참고 출처 목록 전부 target="_blank" rel="noopener"로 링크 처리, 공공기관 링크에
  nofollow 미부착. 출처 URL은 RULES.md 기관 링크 표와 WebSearch로 실제 확인된 주소만
  사용(지어내지 않음). 조세특례제한법 시행령의 정확한 조번호는 검색 결과가 서로 엇갈려
  (손익통산 근거 조문 vs 가입자격 확인 조문으로 다르게 언급) 신뢰도 있게 확정하지 못해
  본문에 구체 조번호를 적지 않고 "조세특례제한법 제91조의18 및 하위 시행령"으로만
  서술했다(지어내지 않는다는 원칙 우선).
  제목 "ISA 손익통산 계산 방법" 12자(공백 포함)·금지어 없음·조사·접속사 없음.
  슬러그 영문 소문자+하이픈 4단어(isa-gain-loss-netting). 인트로 문단 최상단 배치. 표는
  thead/tbody 시맨틱 사용. 기준일 명시. FAQ 6개와 JSON-LD 1:1 일치. 종목·상품 추천 표현,
  단정 표현 없음. 하단 면책 문구 포함.
  종합 판정: 4개 게이트 전부 충족(게이트4는 5곳 이상 독립 출처 교차검증으로 대체, 한계
  투명 공개) → gate_pass:true. 발행 가능.
---

<p style="font-size:13px;color:#888;">최종 검토일: 2026-09-17</p>

<p><mark>ISA 계좌 안에서는 여러 상품의 이익과 손실을 합쳐서 순이익 기준으로 세금을 계산합니다.</mark> 다만 국내 상장주식은 예외라서, 매매 이익은 통산에서 빠지고 매매 손실만 통산에 반영되는 비대칭 구조를 알아야 정확히 계산할 수 있습니다.</p>

<div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:24px 0;">
  <strong style="color:#2f4f7f;font-size:18px;">📌 핵심만 먼저 보기</strong>
  <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.9;">
    <li>ISA는 계좌 안의 <b>모든 이익과 손실을 합쳐서 순이익</b>을 계산하고, 그 순이익 기준으로 세금을 매깁니다.</li>
    <li><b>국내 상장주식 매매이익은 원래 비과세</b>라 통산 대상 이익에 포함되지 않지만, <b>매매손실은 통산에 포함</b>돼 다른 상품의 이익을 줄여줍니다.</li>
    <li>순이익 중 <mark>일반형 200만원, 서민형·농어민형 400만원까지는 비과세</mark>이고, 초과분에는 9.9%(지방소득세 포함) 분리과세가 적용됩니다.</li>
    <li>계좌 안에서만 통산되며, 순손실이 나도 다음 해나 다른 계좌로 손실이 이월되지는 않습니다.</li>
  </ul>
</div>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">목차</h2>
<ol style="line-height:1.9;">
  <li>ISA 손익통산이 뭔가요</li>
  <li>손익통산 대상에 국내주식도 포함되나요</li>
  <li>손익통산 후 세금은 얼마나 나오나요</li>
  <li>손실만 났을 때는 어떻게 되나요</li>
  <li>자주 묻는 질문</li>
</ol>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">ISA 손익통산이 뭔가요</h2>

<p>일반 증권계좌라면 상품마다 따로 세금을 계산합니다. 펀드에서 600만원 벌고 다른 상품에서 200만원 잃어도, 번 600만원에는 세금이 붙고 잃은 200만원은 세금 계산에 반영되지 않습니다.</p>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">ISA는 계좌 안의 이익과 손실을 전부 합쳐서 순이익 하나만 남긴 뒤, 그 순이익을 기준으로 세제 혜택과 세금을 계산합니다.</span> 예를 들어 펀드에서 500만원 벌고 다른 상품에서 200만원 잃었다면, ISA는 둘을 통산해 300만원을 과세 기준 순이익으로 봅니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">손익통산 대상에 국내주식도 포함되나요</h2>

<p>여기서 자주 헷갈리는 부분이 국내 상장주식입니다. <b>국내 상장주식의 매매차익은 원래 비과세</b>이기 때문에, ISA 안에서 벌었더라도 애초에 세금을 매길 대상이 아니라서 통산 대상 이익에 들어가지 않습니다.</p>

<p>반대로 <mark>국내 상장주식에서 손실이 나면 그 손실 금액은 통산에 포함</mark>됩니다. 손실은 "세금을 매길 대상"이 아니라 "다른 이익에서 빼줄 금액"으로 취급되기 때문입니다. 이 비대칭 구조 때문에 국내주식을 함께 담은 ISA는 국내주식만 놓고 보면 항상 가입자에게 불리하지 않은 방향으로 작동합니다.</p>

<table style="width:100%;border-collapse:collapse;margin:16px 0;">
  <thead>
    <tr style="background:#f0f0f0;">
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">국내 상장주식 매매손익</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">손익통산 반영 여부</th>
      <th style="border:1px solid #ddd;padding:8px;text-align:left;">이유</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매매 이익</td>
      <td style="border:1px solid #ddd;padding:8px;">통산 대상 이익에서 제외</td>
      <td style="border:1px solid #ddd;padding:8px;">원래 비과세라 과세 대상 자체가 아님</td>
    </tr>
    <tr>
      <td style="border:1px solid #ddd;padding:8px;">매매 손실</td>
      <td style="border:1px solid #ddd;padding:8px;">통산에 포함(다른 이익에서 차감)</td>
      <td style="border:1px solid #ddd;padding:8px;">손실 금액만큼 과세 대상 순이익을 줄여줌</td>
    </tr>
  </tbody>
</table>

<p>펀드·파생결합증권(ELS·DLS 등)·예금이자처럼 원래 과세 대상인 상품은 이익과 손실 모두 그대로 통산에 반영됩니다. 예외는 국내 상장주식뿐입니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">손익통산 후 세금은 얼마나 나오나요</h2>

<p>통산으로 계산된 순이익에 <b>비과세 한도(일반형 200만원, 서민형·농어민형 400만원)</b>를 먼저 적용하고, 넘는 부분에만 <mark>9.9%(지방소득세 포함) 분리과세</mark>가 붙습니다. 일반 계좌에서 금융소득에 붙는 15.4% 원천징수보다 낮은 세율입니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (일반형 ISA, 가상 사례)</b>
  <p style="margin:8px 0 0 0;">펀드에서 500만원 이익, 국내주식에서 200만원 손실이 났다면, 국내주식 손실 200만원은 통산에 포함돼 순이익은 <b>500만원 − 200만원 = 300만원</b>입니다. 여기서 비과세 한도 200만원을 빼면 과세 대상은 100만원, 세금은 <b>100만원 × 9.9% = 99,000원</b>입니다.</p>
</div>

<p>같은 상황을 일반 계좌로 했다면 국내주식 손실은 애초에 반영되지 않아 펀드 이익 500만원 전체에 15.4%가 붙어 세금이 770,000원입니다. ISA 손익통산과 저율 분리과세 덕분에 이 예시에서는 세금이 약 67만원 줄어듭니다(실제 세액은 상품 구성과 시점에 따라 달라집니다).</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">손실만 났을 때는 어떻게 되나요</h2>

<p>반대로 <b>국내주식에서는 이익</b>이 나고 <b>다른 상품에서는 손실</b>이 난 경우를 보겠습니다.</p>

<div style="background:#f6f6f4;border-left:4px solid #999;padding:14px 18px;margin:20px 0;line-height:1.9;">
  <b>계산 예시 (일반형 ISA, 가상 사례)</b>
  <p style="margin:8px 0 0 0;">국내주식에서 400만원 이익, 펀드에서 100만원 손실이 났다면, 국내주식 이익 400만원은 통산 대상에서 제외되므로 <b>그대로 비과세</b>로 받습니다. 통산 대상에 남는 것은 펀드 손실 100만원뿐이라 순손익은 <b>−100만원</b>, 즉 과세할 순이익이 없어 <b>세금은 0원</b>입니다.</p>
</div>

<p><span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">순손실이 났다고 해서 그 손실이 다음 해나 다른 계좌로 이월되지는 않습니다.</span> ISA는 계좌 만기 시점에 그 안에서 발생한 손익만 정산하는 구조이기 때문에, 손실은 "세금을 0원으로 만드는 역할"까지만 하고 소멸합니다. 자세한 유형별 납입한도·비과세 한도 구조는 <a href="https://sensitiveboss3.tistory.com/entry/isa-limit-benefit" target="_blank" rel="noopener">이전 글(ISA 계좌 한도와 비과세 혜택)</a>에서 다뤘습니다.</p>

<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">자주 묻는 질문</h2>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">ISA 손익통산이란 정확히 무엇인가요</summary>
  <p style="margin:10px 0 0 0;">ISA 계좌 안에서 발생한 여러 상품의 이익과 손실을 전부 합쳐 순이익 하나를 계산하고, 그 순이익을 기준으로 비과세 한도와 세율을 적용하는 방식입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">국내주식 매매이익도 손익통산에 포함되나요</summary>
  <p style="margin:10px 0 0 0;">아니요. 국내 상장주식 매매이익은 원래 비과세라서 통산 대상 이익에 포함되지 않습니다. 반면 국내주식 매매손실은 통산에 포함돼 다른 상품의 과세 대상 이익을 줄여줍니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">손익통산 후 비과세 한도는 얼마인가요</summary>
  <p style="margin:10px 0 0 0;">일반형은 200만원, 서민형·농어민형은 400만원까지 비과세입니다. 초과분에는 9.9%(지방소득세 포함) 분리과세가 적용됩니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">순손실이 나면 손실이 다음 해로 이월되나요</summary>
  <p style="margin:10px 0 0 0;">이월되지 않습니다. ISA는 계좌 내에서 발생한 손익만 정산하는 구조라, 순손실이면 그 해 세금이 0원이 되는 것으로 끝나고 손실 자체가 다른 계좌나 다음 해로 넘어가지 않습니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">펀드나 파생결합증권 손익도 통산되나요</summary>
  <p style="margin:10px 0 0 0;">네. 펀드·파생결합증권(ELS·DLS 등)·예금이자처럼 원래 과세 대상인 상품은 이익과 손실 모두 그대로 통산에 반영됩니다. 통산에서 예외로 취급되는 것은 원래 비과세인 국내 상장주식뿐입니다.</p>
</details>

<details style="border:1px solid #ddd;border-radius:8px;padding:12px 16px;margin:10px 0;">
  <summary style="font-weight:bold;cursor:pointer;">일반 계좌와 비교하면 얼마나 유리한가요</summary>
  <p style="margin:10px 0 0 0;">상품 구성에 따라 다르지만, 국내주식 손실이 다른 상품 이익을 줄여주는 통산 효과와 9.9% 저율 분리과세(일반 계좌는 15.4% 원천징수)가 겹치면 세금 부담이 크게 줄어들 수 있습니다. 정확한 금액은 실제 보유 상품과 손익 규모에 따라 달라집니다.</p>
</details>

<div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
  참고 출처:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><a href="https://www.fsc.go.kr/po020201/27339" target="_blank" rel="noopener">금융위원회</a> - ISA(개인종합자산관리계좌) 주요정책문답(자동화 세션에서는 접속이 막혀 직접 확인하지 못함)</li>
    <li><a href="https://www.law.go.kr" target="_blank" rel="noopener">국가법령정보센터</a> - 조세특례제한법 제91조의18(개인종합자산관리계좌에 대한 과세특례)</li>
    <li><a href="https://eiec.kdi.re.kr/publish/naraView.do?fcode=00002000040000100012&amp;cidx=13833" target="_blank" rel="noopener">KDI 경제정보센터</a> - "김대리, 주식 세금은 ISA로 대비하자"</li>
  </ul>
  기준일: 2026-09-17(WebSearch 확인일). 금융위원회 원문 페이지는 이번 세션 WebFetch가
  차단돼 직접 열람하지 못했고, 언론 1곳·준정부 연구기관 2곳·준정부 성격 재단 1곳을
  포함한 5곳 이상의 독립 출처가 핵심 수치(비과세 한도, 세율, 손익통산 비대칭 구조)에서
  동일하게 일치함을 확인해 교차검증으로 대체했습니다. 비과세 한도·세율은 3편에서 원문으로
  확정한 값과도 일치합니다.
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
  "headline": "ISA 손익통산 계산 방법",
  "description": "ISA 계좌 안에서 여러 상품의 이익과 손실을 합쳐 순이익을 계산하는 손익통산 방식, 국내 상장주식의 비대칭 취급(이익 제외·손실 포함), 비과세 한도와 9.9% 분리과세 계산 예시를 정리합니다.",
  "author": { "@type": "Person", "name": "센시티브보스" },
  "publisher": { "@type": "Organization", "name": "센시티브보스" },
  "datePublished": "2026-09-17",
  "dateModified": "2026-09-17",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://sensitiveboss3.tistory.com/entry/isa-gain-loss-netting"
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
      "name": "ISA 손익통산이란 정확히 무엇인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "ISA 계좌 안에서 발생한 여러 상품의 이익과 손실을 전부 합쳐 순이익 하나를 계산하고, 그 순이익을 기준으로 비과세 한도와 세율을 적용하는 방식입니다." }
    },
    {
      "@type": "Question",
      "name": "국내주식 매매이익도 손익통산에 포함되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "아니요. 국내 상장주식 매매이익은 원래 비과세라서 통산 대상 이익에 포함되지 않습니다. 반면 국내주식 매매손실은 통산에 포함돼 다른 상품의 과세 대상 이익을 줄여줍니다." }
    },
    {
      "@type": "Question",
      "name": "손익통산 후 비과세 한도는 얼마인가요",
      "acceptedAnswer": { "@type": "Answer", "text": "일반형은 200만원, 서민형·농어민형은 400만원까지 비과세입니다. 초과분에는 9.9%(지방소득세 포함) 분리과세가 적용됩니다." }
    },
    {
      "@type": "Question",
      "name": "순손실이 나면 손실이 다음 해로 이월되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "이월되지 않습니다. ISA는 계좌 내에서 발생한 손익만 정산하는 구조라, 순손실이면 그 해 세금이 0원이 되는 것으로 끝나고 손실 자체가 다른 계좌나 다음 해로 넘어가지 않습니다." }
    },
    {
      "@type": "Question",
      "name": "펀드나 파생결합증권 손익도 통산되나요",
      "acceptedAnswer": { "@type": "Answer", "text": "네. 펀드·파생결합증권(ELS·DLS 등)·예금이자처럼 원래 과세 대상인 상품은 이익과 손실 모두 그대로 통산에 반영됩니다. 통산에서 예외로 취급되는 것은 원래 비과세인 국내 상장주식뿐입니다." }
    },
    {
      "@type": "Question",
      "name": "일반 계좌와 비교하면 얼마나 유리한가요",
      "acceptedAnswer": { "@type": "Answer", "text": "상품 구성에 따라 다르지만, 국내주식 손실이 다른 상품 이익을 줄여주는 통산 효과와 9.9% 저율 분리과세(일반 계좌는 15.4% 원천징수)가 겹치면 세금 부담이 크게 줄어들 수 있습니다. 정확한 금액은 실제 보유 상품과 손익 규모에 따라 달라집니다." }
    }
  ]
}
</script>
