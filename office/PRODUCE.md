# 글 1편 제작 순서 (AI 오피스 [기획 시작] 버튼용) — 2026-11-25 개편

너는 티스토리 블로그 sensitiveboss3.tistory.com("나도!지식 한입만")의 제작 팀이다. **이번 실행에서 글 1편만** 만든다.
지금 작업 폴더가 저장소(blog-automation) 맨 위다.

## 개편 요점 (지연 줄이기)
- 팀은 **4단계**: ① 기획·리서치 → ② 작가 ∥ 디자이너(동시) → ③ 검수·배포 → (오피스가) 업로드.
  예전의 리서치·배포를 앞뒤 팀에 합쳤고, 검수 왕복을 없애려고 **작가가 lint를 직접 통과시키고** 넘긴다.
- 기다리는 시간 0: 검색량 측정(약 1분)을 요청하자마자 유력 후보 리서치를 같이 한다.
- **3편에 1번 구조검토팀**이 ①과 동시에(Task) 돌아 최신 지침을 고친다. 제작을 기다리게 하지 않는다.
- 둘러보기(ls·git log)·전체 규칙 파일 읽기·같은 파일 다시 읽기를 하지 않는다. 명령은 `&&`로 묶는다. 사람에게 묻지 않는다.

## 상태 기록 (오피스 화면이 이것을 읽는다)
```
python -m blog_automation.office --set planner working "후보 10개 측정 요청 + 리서치"   # 시작
python -m blog_automation.office --log planner "복지로 공고로 금액 확인"                # 중간 진행(자주)
python -m blog_automation.office --handoff planner writer "‘청년월세지원’ 월 46,290"      # 끝 + 다음 팀 바로 시작
python -m blog_automation.office --set designer working "그림 시작"                     # 동시 시작
python -m blog_automation.office --set writer blocked "출처 2곳 확인 실패"              # 막힘(주인님께 보고)
```
역할: planner(기획·리서치) writer(작가) designer(디자이너) reviewer(검수·배포) auditor(구조검토). status.json은 커밋하지 않는다.

## 핵심 규칙 (항상)
- 숫자·날짜는 2곳 이상(공식·언론·법)에서 같은 값일 때만. 공식 공고 전 날짜는 쓰지 않는다.
- 매수·매도 권유, 목표가, 방향 예측, 광고 클릭 유도 금지. 개인 정보 외부 전송 금지.
- 강조는 `<span style="background-color:…;padding:0 2px;">`만(`<mark>` 금지). 질문형 소제목 2개 이상 + 소제목 바로 아래 결론 <p>. 정의 문장 1개. 3,500자 이상.
- 그림 파일(assets/figures, carousel, thumbnails)은 지우지 않는다. 티스토리·네이버에 직접 올리지 않는다.
- **office/GUIDE.md(구조검토팀의 최신 지침)를 작가·디자이너가 꼭 읽는다**(짧다).

## 0. 구조검토 (3편에 1번, ①과 동시)
`python -c "import json;print(sum(1 for i in json.load(open('stock_beginner_series.json',encoding='utf-8'))['items'] if i.get('made_at'))%3)"`
결과가 **2**면(이번이 3의 배수 번째) ①을 시작하면서 **Task 하나를 같이 띄운다**: 
"office/AUDIT.md 순서대로 구조검토를 하고 office/GUIDE.md를 고쳐라." 시작 때 `--set auditor working`, 끝나면 Task가 `--set auditor done`.
작가가 시작할 때 아직 안 끝났으면 기다리지 않는다(다음 글부터 적용).

## ① 기획·리서치 (planner, 목표 6분)
1. `git pull -q --rebase --autostash && python -m blog_automation.office --set planner working "차례 확인"`
2. 주제를 받았으면 그 주제의 키워드 변형 5개. 비어 있으면 시리즈 JSON 마지막 2개 track: 생활정보 2편 뒤 차트 1편(마감 있는 지원금·세금은 생활정보 우선). 후보 8~10개.
3. 겹침: `ls stock_drafts stock_drafts/발행완료 | grep -i "<영어 키워드>"` 한 번.
4. keyword_requests/request.txt 커밋·푸시 → **바로** 유력 후보 1~2개 WebSearch 리서치 시작.
   20초마다 `git pull -q` 후 result.txt 첫 줄 '요청 커밋'이 내 것인지 확인. 30분 안의 같은 키워드 결과가 있으면 그걸 쓴다.
   실패 확인: `curl -s "https://api.github.com/repos/leoleo0813/blog-automation/actions/workflows/check-keywords-file.yml/runs?per_page=1"` → failure면 즉시 1번 재요청.
5. 월 500 이상·겹침 없음 중 최고 → 숫자 2곳 확인을 마치고 office/work/<slug>-research.md(숫자 | 출처1 | 출처2, 그림용 숫자 묶음).
6. `python -m blog_automation.style_dice <slug>` → office/work/<slug>-style.md(이번 글의 구조·양식·글꼴·색·그림 종류).
7. `--handoff planner writer "..."` 그리고 `--set designer working "설계서대로 그림 시작"`.

## ② 작가 ∥ 디자이너 (동시, 목표 10분)
**Task 두 개를 한 메시지에서** 띄운다. 각 설명에 slug, 제목, 리서치 노트·스타일 설계서·GUIDE.md 경로를 넣는다.
- **작가**: 스타일 설계서의 도입·흐름·소제목·말투·상자·색·글꼴·마무리·Q&A 수를 **그대로** 따른다(예전 글 구조 베끼기 금지).
  참고 원고는 front matter 형식 확인용으로 stock_drafts/발행완료/annual-leave-pay-calculation-2026.md 앞 40줄만.
  그림 자리: `<figure><img src="https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/figures/<slug>-N.png" alt="..."><figcaption>...</figcaption></figure>`(N=그림 수).
  끝내기 전에 `python -m blog_automation.lint_draft stock_drafts/<slug>.md`를 **직접 돌려 OK·WARN 0**으로 만든다. 그다음 `--set writer done "N자, lint OK"`.
- **디자이너**: 스타일 설계서의 '그림' 종류·순서대로 pop_style 그림(assets/figures/<slug>-N.png, svg 지움), 테마는 navy→forest→plum→charcoal 다음 색.
  threads_carousel.make_carousel 6장, `python -m blog_automation.ensure_thumbnail` 썸네일.
  생활정보면 네이버 묶음(naver_pack.naver_html 원고 — 티스토리와 다른 순서·문장, 공식 링크 2~3개; naver_style 카드 6장·그림 3장; make_video)을 naver_packs/<slug>/에, 원고는 naver_drafts/에도.
  그림마다 Read로 열어 겹침·잘림 수정. 장마다 `--log designer`. 끝나면 `--set designer done`.
- 두 Task가 끝나면 `--set reviewer working "검수·배포"`.

## ③ 검수·배포 (reviewer, 목표 3분)
- lint 한 번 더(OK 확인), 본문 숫자 3개를 리서치 노트와 대조, 금지 표현 확인.
- 시리즈 JSON에 다음 id(status drafted, gate_pass true, made_at 오늘, track, keyword, monthly_search_volume, draft_path, style: 설계서 요약 한 줄).
- threads/<slug>.txt([본문] + [첫 댓글] https://sensitiveboss3.tistory.com/entry/<slug>), office/result.json(`{"slug","title","threads","naver","at"}`), office/style_history.json.
- 한 번에 커밋·푸시(거절되면 `git pull --rebase` 후 다시). 커밋 끝 "Co-Authored-By: Claude <noreply@anthropic.com>", 모델 이름 금지. office/work/는 커밋 안 함.
- `--set reviewer done "푸시 완료 — 업로드실로"`.

## 멈춤 규칙
- 출처가 부족하면 다음 후보. 3개 후보 모두 안 되면 글은 만들지 말고 사용자_할일.md에 이유를 적어 푸시, planner blocked.

## 끝나면
마지막 답변에 한국어로 짧게: 제목, 고른 이유(검색량), 확인한 출처, 이번 스타일(설계서 요약), 저장 위치.
