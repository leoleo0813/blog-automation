# blog-automation

Blogger(허브) / Tistory / Threads 자동 콘텐츠 생성 및 발행 시스템.

## 구성
- `CLAUDE.md` — 콘텐츠 생성 및 발행 가이드라인
- `blog_automation/get_refresh_token.py` — Blogger OAuth refresh token 발급 (로컬 1회 실행)
- `blog_automation/blogger_publish.py` — Blogger API v3 발행 함수

## 시작하기
1. `.env.example`을 `.env`로 복사하고 값 채우기
2. `pip install -r requirements.txt`
3. `python blog_automation/get_refresh_token.py` 실행 후 발급된 refresh token을 `.env`에 저장
4. `post_to_blogger(...)` 호출 (기본은 draft 모드)
