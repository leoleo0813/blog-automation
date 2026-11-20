# 글 1편 제작 순서 (AI 오피스 [기획 시작] 버튼용)

너는 티스토리 블로그 sensitiveboss3.tistory.com("나도!지식 한입만")의 제작 팀이다. **이번 실행에서 글 1편만** 만든다.
지금 작업 폴더가 저장소(blog-automation) 맨 위다. **빠르게** 움직인다: 둘러보기·같은 파일 다시 읽기·긴 대기를 하지 않는다.

## 속도 규칙 (꼭 지킨다)
- RULES.md·TEAM.md 전체를 읽지 않는다. 필요한 규칙은 아래 '핵심 규칙'에 다 있다. 더 필요하면 `grep -n "키워드" RULES.md`로 그 부분만 본다.
- 참고 원고는 1편만(아래 작가 항목) 읽는다. `ls`·`git log`로 저장소를 둘러보지 않는다.
- 한 번에 할 수 있는 명령은 `&&`로 묶어서 한 번에 실행한다.
- **작가와 디자이너는 동시에 일한다**: 리서치가 끝나면 Task(하위 에이전트) 2개를 **한 번에** 띄워 작가·디자이너를 같이 돌린다(아래 참고).
- 역할이 끝나면 **바로 다음 역할로 넘긴다**(인계 명령 한 줄). 사람에게 묻지 않는다.

## 상태 기록 (AI 오피스 화면이 이것을 읽는다)
```
python -m blog_automation.office --set planner working "후보 10개 검색량 측정 요청"     # 시작
python -m blog_automation.office --log planner "결과 받음: 청년월세지원 46,290 선택"       # 중간 진행(자주! 방을 누르면 보인다)
python -m blog_automation.office --handoff planner research "‘청년월세지원’ 월 46,290 선택"  # 끝 + 다음 팀 바로 시작
python -m blog_automation.office --set research blocked "공식 출처 2곳 확인 실패"         # 막힘(주인님께 보고됨)
```
역할 이름: planner(기획) research(리서치) writer(작가) designer(디자이너) reviewer(검수) deploy(배포).
중간 진행 `--log`는 의미 있는 단계마다 1줄씩 남긴다(검색 1번, 그림 1장, 고친 것 등). office/status.json·index.html은 커밋하지 않는다.

## 핵심 규칙 (RULES.md 요약)
- 숫자·날짜는 2곳 이상(공식·언론·법)에서 같은 값일 때만 쓴다. 확인 못 한 숫자는 쓰지 않는다. 공식 공고 전 날짜는 쓰지 않는다.
- 매수·매도 권유, 목표가, 방향 예측 금지. 광고 클릭 유도 문구 금지. 개인 정보 외부 전송 금지.
- 강조는 `<span style="background-color:#fff3a3;padding:0 2px;">`만(`<mark>` 금지). 질문형 H2 + 바로 아래 결론 <p>. 키워드 정의 문장("X은 ~이다") 1개.
- 그림 파일(assets/figures, assets/carousel, assets/thumbnails)은 지우지 않는다. 티스토리·네이버에 직접 올리지 않는다.
- 네이버 원고는 티스토리 문장을 붙여넣지 않고 순서·문장을 새로 쓴다. 공식 링크 2~3개, 내 다른 블로그 링크 없음.

## 1. 기획 (목표 3분)
1. `git pull -q --rebase --autostash && python -m blog_automation.office --set planner working "차례 확인"`
2. 주제를 받았으면 그 주제로 하고 키워드 변형 5개만 잰다. 비어 있으면 stock_beginner_series.json 마지막 2개 track을 보고
   생활정보(life) 2편 뒤 차트(chart) 1편. 마감 있는 지원금·세금은 생활정보를 당긴다. 후보 8~10개.
3. 겹침 확인은 한 줄로: `ls stock_drafts stock_drafts/발행완료 | grep -i "<영어 키워드 일부>"`
4. keyword_requests/request.txt에 쉼표로 적어 커밋·푸시 → GitHub Actions가 약 1분 뒤 keyword_requests/result.txt를 올린다.
   **기다리는 동안 놀지 않는다**: 가장 유력한 후보 1~2개로 리서치 검색을 먼저 시작한다.
   20초마다 `git pull -q` 후 result.txt 첫 줄 '요청 커밋'이 내 커밋인지 본다. 같은 키워드의 결과가 30분 안에 이미 있으면 그걸 쓴다.
   실패 확인: `curl -s "https://api.github.com/repos/leoleo0813/blog-automation/actions/workflows/check-keywords-file.yml/runs?per_page=1"`
   → 내 커밋이 `failure`면 즉시 1번 다시 요청, 또 실패하면 planner blocked. 3분 넘게 소식이 없어도 1번 다시 요청.
5. 월 500 이상, 겹치지 않는 것 중 가장 높은 것 → `--handoff planner research "..."`

## 2. 리서치 (목표 6분)
- WebSearch로 숫자·날짜 확인, 출처 URL을 office/work/<slug>-research.md에 적는다(숫자 | 출처1 | 출처2).
- 그림에 쓸 숫자 묶음도 같은 파일에 적는다(디자이너가 이것만 보고 그린다).
- 끝나면 `--handoff research writer "핵심 숫자 N개 확인"` 그리고 `--set designer working "리서치 노트로 그림 시작"`.

## 3. 작가 ∥ 디자이너 (동시에, 목표 10분)
**Task 도구를 한 메시지에서 두 번 호출**해 동시에 돌린다. 각 Task 설명에 slug, 제목, 리서치 노트 경로, 아래 해당 항목을 그대로 넣는다.
- **작가**: stock_drafts/발행완료/annual-leave-pay-calculation-2026.md 1편만 참고해 같은 구조·문체로 stock_drafts/<slug>.md 작성.
  3,500자 이상, 낱말 풀이·따라 하기·실수 5가지·Q&A 5개·함께 보면 좋은 글(status published만)·출처. 그림 자리는
  `<figure><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/<slug>-N.png" alt="..."><figcaption>...</figcaption></figure>`(N=1~3).
  중간에 `--log writer "..."`. 끝나면 `--set writer done "N자 완료"`.
- **디자이너**: 테마는 navy→forest→plum→charcoal 순서로 직전 편 다음 색. pop_style로 그림 3장(assets/figures/<slug>-N.png, svg 지움),
  threads_carousel.make_carousel 캐러셀 6장, `python -m blog_automation.ensure_thumbnail`로 썸네일(svg 지움).
  생활정보면 네이버 묶음(naver_pack.naver_html 원고, naver_style.make_cards 카드 6장·figure 3장, naver_pack.make_video(card_dir=…, bg=naver_style.PAPER))을
  naver_packs/<slug>/에, 원고 html은 naver_drafts/에도. 그림마다 Read로 열어 겹침·잘림을 고친다. 장마다 `--log designer "그림 N 완료"`. 끝나면 `--set designer done "..."`.
- 두 Task가 끝나면 바로 `--set reviewer working "검수 시작"`.

## 4. 검수 (목표 3분)
- `python -m blog_automation.lint_draft stock_drafts/<slug>.md`가 OK, WARN 0개가 될 때까지 고친다. 본문 숫자를 리서치 노트와 대조, 계산 다시 해 보기. 금지 표현 확인.
- 끝나면 `--handoff reviewer deploy "lint OK·숫자 대조 OK"`.

## 5. 배포 (목표 2분)
- stock_beginner_series.json에 다음 id로 항목 추가(status drafted, gate_pass true, made_at 오늘 YYYY-MM-DD, track, keyword, monthly_search_volume, draft_path).
- threads/<slug>.txt에 [본문]과 [첫 댓글](https://sensitiveboss3.tistory.com/entry/<slug>).
- office/result.json에 `{"slug": "...", "title": "...", "threads": "threads/<slug>.txt", "naver": "naver_packs/<slug>/", "at": "..."}`.
- office/work/는 커밋하지 않아도 된다. 나머지를 main에 커밋·푸시(거절되면 `git pull --rebase` 후 다시). 커밋 끝에 "Co-Authored-By: Claude <noreply@anthropic.com>", 모델 이름은 넣지 않는다.
- `--set deploy done "푸시 완료 — 업로드실로"`.

## 멈춤 규칙
- 출처가 부족하면 다음 후보로. 3개 후보 모두 안 되면 글은 만들지 말고 사용자_할일.md에 이유를 적어 푸시하고 해당 역할 blocked.

## 끝나면
마지막 답변에 한국어로 짧게: 제목, 고른 이유(검색량), 확인한 출처, 저장 위치.
