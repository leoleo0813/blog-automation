# Blog Automation System Guidelines

> **⏸ Blogger 자동 발행 일시중단 중.** 사람이 재개를 지시하기 전까지, 생성된 콘텐츠는 이 저장소에만 커밋되고 GitHub Actions 발행 워크플로는 트리거되지 않습니다 (Blogger API 호출도, 카카오톡 알림도 없음). 이 문서의 콘텐츠 작성 규칙 자체는 그대로 유효합니다 — 무엇을 "발행"할지가 아니라 "커밋까지만" 한다는 점만 다릅니다. 실제 스킵 로직은 3시간마다 도는 Routine의 프롬프트에 있습니다.

## 1. Role & Architecture
- You are an automated content creation and multi-platform distribution agent.
- **Writing order matters:** Tistory main article first → Blogger version is a rewrite of it → Threads hook last. Never write Blogger first and pad it out — that produces a thin, generic piece.
- **Main:** Tistory (deep-dive, long-form, manual publish — no API integration, by policy).
- **Hub:** Google Blogger (SEO & GEO optimized rewrite of the Tistory piece, auto-published via Blogger API).
- **Branch:** Threads (short-form hook derived from either piece, manual publish for now).

## 2. Content Generation Rules
- **Tistory Main Article (write this first):**
  - A genuine deep-dive in Korean: thorough, specific, more detailed than the Blogger version — this is the authoritative long-form piece, not a byproduct.
  - Structure: title, intro, several H2/H3 sections covering the topic in depth, a closing wrap-up. Plain, readable Markdown (Tistory's own editor handles formatting) — no Blogger-specific HTML info boxes or metadata needed here.
  - Save as `tistory_drafts/<slug>.md` (same slug as the Blogger post). This is never auto-published — Tistory has no API access — so it only needs to be committed to the repo for the human to copy into Tistory's editor manually.
- **Blogger Post (rewrite of the Tistory article, not a copy):**
  - Must differ meaningfully in wording and structure from the Tistory piece — same facts, different phrasing/organization/length. Identical text on two domains hurts both pages' SEO.
  - **Title must reflect the H2 sections' actual topics** — write the H2 structure first, then compose a title that summarizes what those sections cover (not a generic hook or empathy line only). A reader should be able to guess most of the H2 topics from the title alone; this also keeps the title keyword-aligned with the body for SEO/GEO.
  - **Never write a wall of text.** No paragraph may run longer than 3 sentences. Anything enumerable (steps, causes, examples, tips) MUST be an `<ul>`/`<ol>` list, never comma-spliced prose or "첫째, 둘째, 셋째" run into a paragraph. This is a readability/SEO/GEO requirement, not a style preference — long undifferentiated paragraphs are the #1 complaint about past posts.
  - Structure (every element below is required, not optional decoration):
    0. **Last-reviewed date line** — directly under the title, before the introduction, visible to readers (not just Blogger's own hidden `dateModified` metadata):
       ```html
       <p style="font-size:13px;color:#888;">최종 검토일: YYYY-MM-DD</p>
       ```
       Use today's actual generation date. This is an E-E-A-T signal — a reader (and a crawler) should see at a glance that the page was recently checked, not just when it was first published.
    1. **Introduction:** Empathy + core summary, 2-3 short sentences.
    2. **TL;DR box** — immediately after the intro, before any H2. 3 bullet points, the reader's key takeaways, in a highlighted box:
       ```html
       <div style="background:#eef6ff;border:2px solid #4a90d9;border-radius:10px;padding:16px 20px;margin:20px 0;">
         <strong style="color:#2f4f7f;font-size:18px;">📌 핵심 요약</strong>
         <ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.8;">
           <li>...</li><li>...</li><li>...</li>
         </ul>
       </div>
       ```
    3. **Body Part 1 & 2** — 2-4 `<h2>` sections, each styled with an accent left-border (pick a hex to match the thumbnail's accent color), each containing:
       - `<h2 style="border-left:6px solid #4a90d9;padding-left:12px;margin-top:36px;">섹션 제목</h2>`
       - Short paragraphs (≤3 sentences each) with the single most important sentence per section wrapped in a highlight span: `<span style="background:linear-gradient(transparent 60%, #fff3b0 60%);font-weight:bold;">핵심 문장</span>`
       - At least one `<ul>`/`<ol>` list per section wherever there's enumerable content
       - At least 2 info/tip boxes total across the post (reuse the existing box style), spaced out — not just one near the top
    4. **Closing recap box** — same visual style as the TL;DR box, 2-3 bullets restating the key action items, right before the closing paragraph.
    5. **Optional short FAQ** (2-3 Q&A) before the closing — good for SEO/GEO (AI Overview / "people also ask" citation): `<h3>Q. ...?</h3><p>A. ...</p>`
    6. **Conclusion & Media:**
       - Search for a high-view/high-like YouTube video related to the topic and embed it using an `<iframe>`.
       - **The video must be a Korean-language video from a Korean channel** — never embed a foreign-language video just because it has high views, even if no good Korean option is found (see Exception Rule below).
       - **A source line is mandatory directly under every embedded video** — the channel name, linked to the video's YouTube URL:
         ```html
         <p style="font-size:13px;color:#888;margin-top:6px;">출처: <a href="https://www.youtube.com/watch?v=VIDEO_ID" target="_blank" rel="noopener">채널명</a></p>
         ```
       - **Exception Rule:** If no relevant, high-quality, Korean-language video is available, omit the video section entirely and provide a neat, comprehensive closing statement instead. Never substitute a non-Korean video to fill this slot.
    7. **References block (mandatory, last element of the post)** — an E-E-A-T signal, not decoration. List 1-3 primary/authoritative sources for the topic's domain, each a real linked source (verify the URL via WebSearch; never fabricate a link):
       ```html
       <div style="border-top:1px solid #ddd;margin-top:32px;padding-top:12px;font-size:13px;color:#888;">
         참고 출처:
         <ul style="margin:6px 0 0 0;padding-left:20px;">
           <li><a href="..." target="_blank" rel="noopener">기관명 - 자료명</a></li>
         </ul>
       </div>
       ```
       Pick sources matching the topic's domain — health topics: 질병관리청, 대한내과학회(또는 관련 전문 학회), 건강보험심사평가원; financial/stock topics: 금융감독원, 한국거래소(KRX), 한국예탁결제원; consumer/policy topics: 관련 정부 부처나 공공기관. If no genuine primary source is verifiable for a general lifestyle/trend topic, it's fine to omit this block for that post rather than inventing one.
- **Thumbnail Image (Crucial, mandatory — never skip):**
  - Blogger has no dedicated thumbnail field — it auto-generates the post's thumbnail/preview image from the first `<img>` tag found in the content. Every post MUST include one near the top (right after the introduction).
  - The content-generation environment's network access is restricted, so a real photo URL found via search cannot be verified to actually exist — do not use WebSearch results or hand-written photo-hosting guesses for this.
  - Instead, generate a simple Korean-language infographic-style card SVG thumbnail locally (no network needed — it's built from plain text/color parameters, so it always works):
    ```
    python -m blog_automation.make_thumbnail <slug> "<한글 제목/짧은 문구>" <배경hex> <포인트색hex> "<짧은 카테고리 태그>" ["<포인트1>" "<포인트2>" "<포인트3>"]
    ```
    e.g. `python -m blog_automation.make_thumbnail autumn-immunity-tips "환절기 면역력 지키는 법" 2f4f7f 4a90d9 "건강 팁" "체온관리" "수면" "비타민C"`
    Pick a background hex color and an accent hex color matching the topic's mood, a short Korean category tag, and up to 3 short (4-6자) core keywords from the post as points — these render as numbered items for an infographic feel. Points are optional; omit them for a plain title card.
    This writes `assets/thumbnails/<slug>.svg` — commit and push this file *together with* the `pending_posts/*.json` in the same commit, then reference it in the post content via jsDelivr (this repo is public, so both jsDelivr and raw.githubusercontent.com work, but jsDelivr is the standard choice):
    ```
    https://cdn.jsdelivr.net/gh/leoleo0813/blog-automation@main/assets/thumbnails/<slug>.svg
    ```
  - Because this is generated locally from parameters (not fetched or guessed), there is no exception case — every post must include one.
- **Metadata Rules (Crucial):**
  - **Labels:** 2–3 relevant tags.
  - **Permalink:** Must be automatically generated by **translating the post title into English** (using lowercase letters and hyphens `-` to separate words, e.g., `youth-future-savings-2026`).
  - **Search Description:** 100–150 characters summary containing core keywords. Note: the Blogger API has no field for this — it must be pasted manually into the post's search-description setting in the Blogger UI after publishing.

## 3. Extension & Linking Rules
- Do not hard-code a link from the Blogger post to the Tistory post — the Tistory post doesn't exist yet at automation time (it's published manually, later). Instead, the Kakao notification reminds the human to add that internal link manually once the Tistory piece is live.
- Generate a companion short-form hook text for Instagram Threads, following the guidelines below (auto-published later once Threads API integration is set up; for now it's delivered via the Kakao notification for manual posting).

## 4. Threads Hook Guidelines
The goal is to pull blog traffic and views simultaneously — write for the feed, not like a blog intro.

- **Structure & layout:**
  - First line is the headline hook — the one line that stops the scroll. Leave the second line blank (an actual line break) for visual breathing room before the rest.
  - Summarize the core content as a numbered list of 3-4 items max, not prose paragraphs. Use emoji numbering (1️⃣ 2️⃣ 3️⃣, or 📌) with short keyword phrases, not full sentences.
  - **Never put a URL in the body text** — Threads' algorithm suppresses reach for posts with outbound links in the body. End the post with only a pointer line like `(자세한 내용은 댓글 링크 참고 👇)` — the actual URL goes in the first reply instead (see Publishing Process below).
- **Hook & voice:**
  - No warm greetings or scene-setting ("안녕하세요", "선선해진 바람이 불어오는 가을입니다" style openers) — these read as blog/Instagram voice and get skipped instantly in a feed.
  - Lean into scarcity and loss-aversion language — phrasing like "지금 안 보면 1년 기다려야 함", "남들 다 시작한", "모르면 손해" that creates urgency.
  - Front-load the single most attention-grabbing concrete number or fact from the post directly into the hook line itself (e.g. "언급량 79% 증가", "트렌드 컬러 4가지") rather than saving it for later.
- **Publishing process** (applies once Threads posting — manual now, automated later — actually happens):
  1. Post the body text first.
  2. Immediately self-reply on the new post with the blog post URL — this is where the link actually lives.
  3. Attach exactly one image: a single curiosity-driving visual, not a multi-panel card summarizing the whole post.

## 5. Execution Rule
- **Step 0 — check the stock content queue first.** Read `stock_beginner_series.json`. If it contains any item with `"status": "pending"`, that item (lowest `id` first) is this run's topic — skip trend research entirely and follow **Section 7** end to end. That path is Tistory-only (sensitiveboss3.tistory.com): it writes a single `stock_drafts/<slug>.md` draft with a gate YAML header, never creates a `pending_posts/*.json`, never triggers the Blogger workflow, and never produces a Threads hook. Only when no item is `"pending"` does this repo fall back to ad-hoc trend research.
- Otherwise, when a topic or keyword is given (or found via trend research), generate in this order: (1) the Tistory main article → `tistory_drafts/<slug>.md`, (2) the rewritten Blogger post + metadata, (3) the thumbnail SVG, (4) the Threads hook per Section 4. Include a `tistory_url` field in the `pending_posts/<slug>.json` pointing to the Tistory draft's GitHub blob URL:
  ```
  https://github.com/leoleo0813/blog-automation/blob/main/tistory_drafts/<slug>.md
  ```
  so the Kakao notification carries a direct, easy-to-copy link to it (repo is public, so this is viewable without login).

## 6. Site-Wide E-E-A-T Setup (one-time, outside per-post automation)
These are blog-level (Blogger theme / static page) changes, not something a per-post content-generation run can do through the Blogger API's `posts()` resource — they need a one-time manual (or separately-scripted) setup, done once by the human operator:
- **About/소개 page:** a standalone Blogger Page (not a Post) explaining who runs the blog and why, the writing/fact-checking principles, and a contact method — without necessarily disclosing a real name. This answers "why should I trust this page" for both readers and crawlers.
- **Person schema:** the blog currently emits only Organization JSON-LD (if any). Adding a Person schema (author identity, even a pen name/persona) requires editing the Blogger theme's HTML (테마 > HTML 편집) to inject a sitewide or per-post `<script type="application/ld+json">` block — this repo's automation only creates individual posts/pages via API, it doesn't touch the theme.
- Both items are tracked here as a known gap, not forgotten — ask the human operator before automating either, since a Page create or theme edit is a live, harder-to-undo action unlike a Blogger draft post.

## 7. 주식 초보 콘텐츠 발행 지침 v1 (재무 YMYL)

**대상 블로그:** sensitiveboss3.tistory.com (주식 초보 카테고리) — Blogger가 아니다.
**최종 개정:** 2026-09-03

이 지침은 건강 블로그 961편의 서치콘솔 실적(2026-06-01~08-31) 분석에서 도출했다. 961편 중 노출 발생 237편, 평균 게재순위 26.3위, 3개월 총 클릭 35회. 실패 원인은 색인도 페널티도 아니었다 — **검색량 없는 키워드로 제목을 지었고, 검증 없이 대량 발행했다.** 아래 규칙은 그 실패를 반복하지 않기 위한 것이므로 어느 하나도 완화하지 않는다.

> ⚠️ 이전 버전(44편 Blogger 시리즈)은 이 지침으로 대체되었다. 이미 Blogger에 올라간 1~2편은 기록으로만 남기고 건드리지 않는다.

### 7.1 파이프라인
```
[1] 소재 감지 (자동)       국세청·금융감독원·한국거래소·예탁결제원·금융투자협회 공시/보도자료
[2] 검색량 확인 (사람)     네이버 검색광고 키워드도구 — 자동화 미연동, 아래 주의 참고
[3] 출처 원문 수집 (자동)  1차 출처 페이지를 WebFetch로 실제로 열어 수치를 추출
[4] 초안 생성 (자동)       stock_drafts/<slug>.md 로 저장. 절대 자동 발행하지 않는다
[5] 게이트 자체 점검 (자동) 4개 게이트 결과를 초안 상단 YAML에 기록
[6] 사람 검토 (필수)       게이트 통과 여부 + 수치 원문 대조
[7] 티스토리 수동 발행     Tistory Open API 종료로 자동 등록이 불가능하다
```
- **발행 상한 하루 2편, 생성 주기 12시간.** 8편을 얕게 만드는 것보다 2편을 깊게 만드는 편이 낫다는 것이 961편의 결론이다.
- **자동 발행 경로가 존재하지 않는다.** Blogger 워크플로도, Threads도 이 카테고리에는 쓰지 않는다. 자동화의 산출물은 저장소의 `.md` 초안 하나뿐이고, 게시는 항상 사람이 티스토리 편집기에 붙여넣어 한다.
- **주의 — 게이트 1 자동화 공백:** 네이버 검색광고 키워드도구 API가 연동되어 있지 않아 월간 검색량을 자동으로 확인할 수 없다. 자동화는 `monthly_search_volume: 확인필요` 로 기록하고 **절대 스스로 `gate_pass: true` 로 만들지 않는다.** 사람이 키워드도구에서 실제 수치를 확인해 채운 뒤에야 발행 여부를 판단한다.

### 7.2 발행 전 게이트 — 하나라도 실패하면 저장만 하고 발행하지 않는다
초안 최상단에 반드시 이 형식으로 기록한다.
```yaml
keyword: 증권사 수수료 비교
monthly_search_volume: 확인필요          # 게이트 1 — 사람이 키워드도구로 채운다
serp_check: 개인블로그 4 / 증권사·언론 4   # 게이트 2
unique_asset: 증권사 12곳 수수료율 실측표  # 게이트 3
primary_source: 금융투자협회 공시 (2026-09-01)  # 게이트 4
gate_pass: false                         # 사람 확인 전까지 항상 false
```
- **게이트 1 — 검색량:** 일반 주제 월 500 이상, 세부·제도 주제 월 100 이상. 검색량을 확인하지 못한 키워드는 발행 금지.
- **게이트 2 — 경쟁 강도:** 해당 키워드 구글 상위 10개 확인. 증권사 공식·언론사·지식백과가 5개 이상이면 키워드 재선정. 개인 블로그가 3개 이상이면 진입 가능.
- **게이트 3 — 정보 이득:** 아래 중 최소 하나가 반드시 있어야 한다. 없으면 순위가 나와도 클릭이 0이다.
  - 실제 숫자표 (증권사별 수수료율, 세율, 한도)
  - 계산 예시 ("100만 원 사고팔면 실제로 얼마")
  - 직접 해본 과정 (화면 캡처, 실제 소요 시간)
  > 근거: "MRI 비용 2026 총정리"는 게재순위 8.5위였으나 3개월 클릭 0. 검색결과에 보였는데도 아무도 누르지 않았다. **총정리는 정보 이득이 아니다.**
- **게이트 4 — 출처와 기준일:** 1차 출처만 인정 (국세청 / 금융감독원 / 한국거래소 / 예탁결제원 / 금융투자협회). 블로그·뉴스·커뮤니티는 출처로 쓰지 않는다. 본문에 `2026년 9월 기준` 형태로 기준일 명시. **원문에 없는 수치는 절대 생성하지 않는다** — 없으면 `공시에 명시되지 않음`으로 표기.

### 7.3 제목 규칙
961편이 26위에 머문 단 하나의 이유가 여기 있다. 제목이 **검색어가 아니라 글의 요약**이었다.

- **30자 이내.** 모바일 검색결과는 30~35자에서 잘린다
- **핵심 키워드를 맨 앞에** 배치
- **접속사·조사를 제거한다.** `~이나`, `~부터 ~까지`, `~인가요`, `~일까요`가 들어가면 검색어가 아니다
- 수수료·세율·한도 주제는 **연도를 붙인다**
- **금지어(전부 총정리형 — 961편이 이 형식으로 실패했다):** `완전 정복` · `총정리` · `쉽게 알아보기` · `무엇일까요` · `알아야 할 모든 것` · `바로알기` · `A to Z` · `한눈에 보기`
- 금지 예: `PER PBR ROE 뜻 쉽게 알아보기`, `주식이 뭔지 하나도 모르겠어요 (완전 기초 편)`
- 권장 예: `증권사 수수료 비교 2026`, `해외주식 양도소득세 신고 방법`, `배당소득세 얼마 떼나`, `ISA 계좌 조건과 한도`

| 유형 | 패턴 | 예시 |
|---|---|---|
| 비교 | `{대상} 비교 {연도}` | 증권사 수수료 비교 2026 |
| 금액 | `{대상} 얼마` | 주식 매도 세금 얼마 |
| 절차 | `{대상} 신고 방법` | 해외주식 양도소득세 신고 방법 |
| 제도 | `{제도명} 조건과 한도` | ISA 계좌 조건과 한도 |
| 계산 | `{대상} 계산 방법` | 배당소득세 계산 방법 |

**URL 슬러그:** 영문 소문자 + 하이픈, 3~5단어. en dash(`–`)·물결·괄호·한글 금지 (`%E2%80%93`로 인코딩되어 URL이 지저분해진다). 예: `overseas-stock-capital-gains-tax`

### 7.4 GEO — AI 검색에 인용되게 쓰는 법
- **각 섹션 첫 문장에 결론을 쓴다.** AI는 문단 앞부분을 발췌한다. "결론부터 말하면" 같은 서두 없이 바로 답
- **수치·정의·비교는 인용 가능한 단문으로.** 한 문장에 하나의 사실 (예: `국내 상장주식은 대주주가 아니면 양도소득세가 없습니다.`)
- **H2는 실제 검색 질문형으로.** `세금 관련 사항` ✕ → `주식 팔면 세금 얼마나 내나요` ○
- **표를 쓴다.** AI는 구조화된 데이터를 우선 인용한다 (`thead`/`tbody` 시맨틱 필수)
- **기준일과 출처를 문장 안에 넣는다.** `2026년 9월 국세청 기준`이 문장에 있으면 인용 신뢰도가 올라간다
- `~라고 알려져 있다`류 모호한 표현은 글당 최대 2회, 초과분은 구체 수치로 대체

### 7.5 본문 구조 (순서 고정)
1. **인트로 문단** — 반드시 최상단. 티스토리 스킨이 본문 맨 앞 텍스트를 메타설명으로 긁어간다
2. **📌 핵심만 먼저 보기 박스** — 불릿 3~4개. 인트로 바로 다음, 목차보다 앞
3. 목차
4. 본문 — H2는 검색 질문형
5. **FAQ 6개** — `details` 아코디언, JSON-LD와 1:1 매칭
6. 출처 목록 + 기준일
7. 투자 책임 안내

**HTML 규칙**
- `DOCTYPE`·`head`·`<style>` 시트·`body` 태그 금지. **인라인 style만** 사용
- 1문단 1~2문장. 세 문장 이상 이어붙이기 금지
- 체크리스트·단계 나열은 `ul>li` 또는 `ol>li`. `p` 나열 금지
- 핵심 수치는 `mark` 하이라이트, 문서당 2~4회
- 표는 `thead`/`tbody` 시맨틱 필수

**JSON-LD 이중 스키마 (필수)**
- **FAQPage** — 본문 FAQ 6개와 1:1 일치
- **Article** — `headline`, `description`, `author`, `publisher`, `datePublished`, `dateModified`, `mainEntityOfPage`
- 세율·수수료·한도 글은 값이 바뀔 때마다 `dateModified`를 반드시 갱신. 신선도가 이 카테고리의 핵심 신호다

**태그:** 발행 시 티스토리 태그란에 8~10개 (핵심 키워드 + 연관어, 쉼표 구분). 초안 YAML에 `tags:` 로 제안해 둔다.

### 7.6 재무 YMYL 안전장치
무료 블로그는 유사투자자문업 신고 대상이 아니지만, 아래는 선을 넘는다.

**절대 금지**
- **특정 종목 추천 · 목표가 · 매수매도 시점 제시** (수수료 "비교표"는 사실 나열이라 허용 — `○○증권 추천` 같은 표현만 금지)
- **개별 종목 상담 답변** — 2024년 8월 개정 이후 개별성이 인정되면 투자자문업으로 분류되며, 등록 없이 하면 형사처벌 대상
- **유료방·오픈채팅 유인** — 무료로 시작해도 유료 전환 통로를 만들면 대가성이 인정된다
- **수익률 인증**, 본인 보유 종목 언급 후 긍정 서술
- **단정 표현** — `반드시`, `무조건`, `확실히`, `보장`

**문체:** 중학생도 이해하는 쉬운 말, 짧은 문장, `~습니다`체 유지.

**하단 고정 문구 (모든 글, 문구 그대로)**
```
이 글은 정보 제공을 목적으로 하며 특정 종목이나 상품의 매수·매도를
권유하지 않습니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
세율·수수료·한도는 변경될 수 있으므로 반드시 원출처에서 최신 내용을
확인하시기 바랍니다.
```

### 7.7 발행 후 4주 검증 (사람이 수행)
44편을 한 번에 쓰지 않는다. **5편을 쓰고 4주를 기다린 뒤 판단한다.** 4주를 쓰는 것이 44편을 헛되이 쓰는 것보다 훨씬 싸다.

| 시점 | 확인 | 판정 |
|---|---|---|
| 3일 | URL 검사로 색인 여부 | 미색인이면 색인 요청 |
| 2주 | 서치콘솔 노출 발생 여부 | 노출 0이면 제목 재검토 |
| 4주 | 노출 · 순위 · CTR | 아래 기준 적용 |

- **노출 있고 20위 안** → 통했다. 같은 유형으로 확장
- **노출 있고 20위 밖** → 본문 보강. 게이트 3(정보 이득)이 약했다
- **노출 0** → 키워드가 틀렸다. 글을 더 쓰지 말고 게이트 1·2부터 다시

### 7.8 첫 5편
기존 44편 기획안에서 **제도·비용·세금** 축만 뽑았다. 개념 설명형(PER 뜻, 호가창 보는 법, 캔들차트, ETF란)은 경쟁이 극심하고 정보 이득을 만들 수 없어 후순위로 미룬다. 큐는 `stock_beginner_series.json`에서 관리한다.

1. **증권사 수수료 비교 2026** — 실제 수수료율 표
2. **주식 매도 세금 얼마** — 100만 원 기준 계산 예시
3. **ISA 연금저축 일반계좌 세제 차이** — 한도·공제 비교표
4. **배당소득세 계산 방법** — 2,000만 원 종합과세 기준
5. **ETF 운용보수 비교하는 법** — 실제 상품 보수율 표

### 7.9 출력 전 자체 점검
초안을 저장하기 전에 스스로 확인하고 결과를 초안 상단에 기록한다.
- [ ] 게이트 1~4 전부 통과했는가 (게이트 1은 사람 확인 전까지 미통과로 본다)
- [ ] 제목이 30자 이내이고 금지어가 없는가
- [ ] 제목에 접속사·조사가 들어가지 않았는가
- [ ] 슬러그가 영문 소문자 + 하이픈인가
- [ ] 인트로 문단이 최상단인가
- [ ] 표가 `thead`/`tbody` 시맨틱인가
- [ ] 본문의 모든 수치가 1차 출처 원문에 존재하는가
- [ ] 기준일이 명시되어 있는가
- [ ] FAQ 6개와 JSON-LD가 1:1 일치하는가
- [ ] 종목·상품 추천 표현, 단정 표현이 없는가
- [ ] 하단 고정 문구가 있는가

하나라도 실패하면 `gate_pass: false`로 기록하고 발행 대기 상태로 저장한다.
