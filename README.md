# blog-automation

Blogger(허브) / Tistory / Threads 자동 콘텐츠 생성 및 발행 시스템.

## 구성
- `CLAUDE.md` — 콘텐츠 생성 및 발행 가이드라인
- `blog_automation/get_refresh_token.py` — Blogger OAuth refresh token 발급 (로컬 1회 실행)
- `blog_automation/blogger_publish.py` — Blogger API v3 발행 함수
- `blog_automation/get_threads_user_id.py` — Threads user ID 확인 (로컬 1회 실행)
- `blog_automation/threads_publish.py` — Threads API 발행 함수

Tistory는 정책상 API 연동을 하지 않고, 가이드라인대로 수동 링크만 유지한다.

## 시작하기 (Blogger)
1. `.env.example`을 `.env`로 복사하고 값 채우기
2. `pip install -r requirements.txt`
3. `python blog_automation/get_refresh_token.py` 실행 후 발급된 refresh token을 `.env`에 저장
4. `post_to_blogger(...)` 호출 (기본은 draft 모드)

## 시작하기 (Threads)
1. Meta 개발자 앱 생성 → Threads API 제품 추가 → 액세스 토큰 발급 후 `.env`의 `THREADS_ACCESS_TOKEN`에 저장
2. `python blog_automation/get_threads_user_id.py` 실행 후 출력된 값을 `.env`의 `THREADS_USER_ID`에 저장
3. `post_to_threads("훅 텍스트")` 호출

## 자동 발행 (PC 없이, GitHub Actions)
Claude가 트렌드 조사와 글 작성을 맡고, 비밀값이 필요한 실제 Blogger 발행은
GitHub Actions가 대신 실행한다.

1. GitHub 저장소 **Settings → Secrets and variables → Actions**에서 아래 4개를
   Repository secret으로 등록 (로컬 `.env`와 동일한 값):
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`
   - `GOOGLE_REFRESH_TOKEN`
   - `BLOGGER_BLOG_ID`
2. `pending_posts/<slug>.json` 형태로 글 데이터를 커밋 (필드: `title`, `content`,
   `labels`, `search_description`, `slug`, `is_draft`)
3. **Publish pending post** 워크플로를 `post_file` 입력값과 함께 수동 실행
   (Actions 탭에서 직접 실행하거나, GitHub API로 `workflow_dispatch` 호출)
4. 워크플로가 `blog_automation/run_pending_post.py`로 해당 JSON을 읽어 발행한다
