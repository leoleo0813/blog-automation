# 글 1편 제작 순서 (AI 타워 [기획 시작] 버튼용)

AI 타워에서 7층 [기획 시작]을 누르면 PC(Windows·Mac)의 Claude Code가 이 파일을 읽고 글 1편을 만든다.
너는 티스토리 블로그 sensitiveboss3.tistory.com("나도!지식 한입만")의 제작 팀이다. **이번 실행에서 글 1편만** 만든다.
지금 작업 폴더가 저장소(blog-automation) 맨 위다.

## 상태 기록 (AI 타워 화면이 이것을 읽는다)
역할을 시작할 때와 끝낼 때 꼭 적는다. 화면의 층 불이 이걸로 켜진다.
```
python -m blog_automation.office --set planner working "후보 10개 검색량 측정 중"
python -m blog_automation.office --set planner done "‘국가장학금 신청기간’ 월 9,730 선택"
```
역할 이름: planner(기획) research(리서치) writer(작가) designer(디자이너) reviewer(검수) deploy(배포).
막히면 `blocked`로 적고 이유를 남긴다. 상태 파일(office/status.json, office/index.html)은 이 PC 전용이라 커밋하지 않는다(.gitignore).

## 준비
1. `git pull --rebase --autostash`
2. RULES.md, TEAM.md, CLAUDE.md를 먼저 읽는다. 규칙이 충돌하면 RULES.md가 우선이다.
3. 사용자가 주제를 주었으면(아래 '이번 주제') 그 주제로 한다. 비어 있으면 stock_beginner_series.json 마지막 항목들로 차례를 정한다:
   생활정보(track: life) 2편 뒤 차트(track: chart) 1편. 신청 마감이 있는 지원금·세금 주제는 생활정보 차례를 당겨서 먼저 한다.

## TEAM.md 역할 순서
- **기획**: 후보 8~10개(주제를 받았으면 그 주제의 키워드 변형 5개)를 keyword_requests/request.txt에 쉼표로 적어 main에 커밋·푸시하면,
  GitHub Actions(check-keywords-file.yml)가 약 1분 뒤 keyword_requests/result.txt를 "검색량 측정 결과" 커밋으로 올린다.
  **20초 간격**으로 git pull 해서 result.txt 첫 줄의 '요청 커밋'이 내 커밋과 같아지면 읽는다. 결과는 보통 40초~1분 30초 안에 온다.
  기다리는 동안 매번 측정 작업 상태도 함께 본다(공개 저장소라 로그인 없이 됨):
  `curl -s "https://api.github.com/repos/leoleo0813/blog-automation/actions/workflows/check-keywords-file.yml/runs?per_page=1"`
  → 내 커밋(head_sha)의 `conclusion`이 `failure`면 **기다리지 말고 즉시** 1번만 다시 요청(request.txt 끝에 공백 하나 추가해 커밋·푸시)하고,
  또 실패하면 `planner blocked "검색량 측정 실패 — 액션 로그 확인 필요"`로 적고 멈춘다. 3분이 지나도 결과·상태가 없으면 같은 방식으로 다시 요청 1번.
  월 500 이상, 기존 stock_drafts·stock_drafts/발행완료 글과 겹치지 않는 것 중 가장 높은 것을 고른다. 차트는 매매 신호·목표가로 흐를 주제는 피한다.
- **리서치**: WebSearch로 숫자·날짜를 2곳 이상 같은 값으로 확인. 확인 못 한 숫자는 쓰지 않는다. 날짜가 공식 공고 전이면 그 주제를 보류한다.
- **작가**: 최근 편(stock_drafts/발행완료/annual-leave-pay-calculation-2026.md, vwap-calculation.md)과 같은 구조·문체로 front matter와 본문을 쓴다.
  3,500자 이상, 질문형 H2와 바로 아래 결론 <p>, 키워드 정의 문장, 낱말 풀이·따라 하기·실수 5가지·Q&A 5개·함께 보면 좋은 글(status가 published인 글만)·출처.
  강조는 `<span style="background-color:#fff3a3;padding:0 2px;">`만 쓰고 `<mark>`는 쓰지 않는다.
- **디자이너**: 테마는 navy→forest→plum→charcoal 순서로 직전 편 다음 색. blog_automation/pop_style.py로 그림 3장(assets/figures/<slug>-N.png, svg는 지움),
  threads_carousel.make_carousel로 캐러셀 6장, `python -m blog_automation.ensure_thumbnail`로 썸네일(svg 지움).
  생활정보면 네이버 묶음도: naver_pack.naver_html 원고(티스토리와 다른 문장·순서, 공식 링크 2~3개), naver_style.make_cards 카드 6장·naver_style.figure 정사각형 그림 3장,
  naver_pack.make_video(card_dir=…, bg=naver_style.PAPER) 영상. 네이버 파일은 모두 naver_packs/<slug>/에 넣고 원고 html은 naver_drafts/에도 복사한다.
  만든 그림은 모두 Read로 직접 열어 보고 글자 겹침·잘림·이중 번호를 고친다.
- **검수**: `python -m blog_automation.lint_draft stock_drafts/<slug>.md`가 OK이고 WARN 0개일 때까지 고친다. 본문 숫자를 다시 계산해 보고 출처와 대조한다.
  매수·매도 권유, 목표가, 방향 예측 표현이 없어야 한다.
- **배포**: stock_beginner_series.json에 다음 id로 항목 추가(status drafted, gate_pass true, made_at 오늘 날짜 YYYY-MM-DD), threads/<slug>.txt에 쓰레드 [본문]과
  [첫 댓글](https://sensitiveboss3.tistory.com/entry/<slug>)을 저장. office/result.json에
  `{"slug": "...", "title": "...", "threads": "threads/<slug>.txt", "naver": "naver_packs/<slug>/", "at": "..."}`를 쓴다.
  office/result.json도 같이 커밋한다. main 브랜치에 커밋·푸시(PR 만들지 않음, 거절되면 `git pull --rebase` 후 다시 푸시). 커밋 메시지 끝에
  "Co-Authored-By: Claude <noreply@anthropic.com>"를 넣고 모델 이름은 넣지 않는다.

## 멈춤 규칙
- 확인된 출처가 부족하면 다음 후보로 넘어가고, 3개 후보 모두 안 되면 글은 만들지 말고 사용자_할일.md에 이유를 적어 푸시한다(해당 역할 blocked).
- 사용자 이메일 등 개인 정보를 외부로 보내지 않는다. 그림 파일(assets/figures, assets/carousel, assets/thumbnails)은 지우지 않는다.
- 티스토리·네이버에 직접 올리지 않는다. 업로드는 AI 타워가 끝난 뒤 pc_uploader로 따로 한다.

## 끝나면
마지막 답변에 한국어로 짧게: 만든 글 제목, 고른 이유(검색량), 확인한 출처, 저장 위치(원고·썸네일·그림·네이버 묶음·쓰레드 문구).
