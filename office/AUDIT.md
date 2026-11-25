# 구조검토팀 작업 순서 (3편에 1번) — 2026-11-25 사용자 요청

목적: 글 구조와 양식이 **티스토리·네이버 검색 최적화(SEO), AI 검색·생성형 엔진 최적화(GEO/AEO), 규제, 최근 트렌드**에 맞는지 점검하고,
작가·디자이너가 읽는 짧은 지침 **office/GUIDE.md**를 고친다. 제작을 막지 않는다(①과 동시에 Task로 돈다). 목표 8분.

1. `python -m blog_automation.office --set auditor working "구조검토 시작"`
2. 최근 3편(시리즈 JSON에서 made_at 최근 3개)의 원고 앞부분·소제목만 본다(`grep -n "<h2\|<h3" stock_drafts/<slug>.md`). 같은 패턴 반복이 있는지 적는다.
3. WebSearch로 최근 6개월 자료를 본다(각 1~2번 검색, 공식 문서 우선):
   - 구글 검색 센터: 유용한 콘텐츠·스팸 정책·AI 생성 콘텐츠 지침, 구조화 데이터(FAQ/HowTo 지원 범위)
   - 네이버 검색: 검색 반영·블로그 운영정책·저품질(유사문서·어뷰징) 관련 공지, 서치어드바이저
   - 티스토리: 공지(에디터·검색·애드센스 관련 변경)
   - AI 검색(AEO/GEO): 질문형 소제목·바로 답하기·출처 표기 등 인용되기 좋은 구조
   - 규제: 애드센스 정책(클릭 유도 금지), 표시광고법·금융상품 광고 관련 주의(투자 권유 금지), 저작권(이미지·인용)
4. office/audit/<YYYY-MM-DD>.md에 보고서: 바뀐 점 / 우리 글이 이미 맞는 점 / 고칠 점(구체적 규칙) / 출처 링크.
5. **office/GUIDE.md를 40줄 이내로 고친다**: 작가·디자이너가 바로 쓸 수 있는 "하라/하지 마라" 규칙만. 오래된 규칙은 지운다.
   lint가 막아야 할 새 규칙이 있으면 사용자_할일.md가 아니라 GUIDE.md 맨 아래 "lint 반영 제안"에 적는다(코드는 고치지 않는다).
6. 보고서·GUIDE.md를 커밋·푸시(커밋 끝 "Co-Authored-By: Claude <noreply@anthropic.com>").
7. `python -m blog_automation.office --set auditor done "지침 N개 갱신 — office/audit/<날짜>.md"`
