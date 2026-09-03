# Blog Automation System Guidelines

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
       - **Exception Rule:** If no relevant or high-quality video is available, omit the video section entirely and provide a neat, comprehensive closing statement instead.
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
- **Step 0 — check the stock beginner series queue first.** Read `stock_beginner_series.json`. If it contains any item with `"status": "pending"`, that item (lowest `id` first) is this run's topic — skip trend research (Section 5 step below) entirely and go straight to Section 6's process. Only when every item is `"done"` does this repo fall back to ad-hoc trend research.
- Otherwise, when a topic or keyword is given (or found via trend research), generate in this order: (1) the Tistory main article → `tistory_drafts/<slug>.md`, (2) the rewritten Blogger post + metadata, (3) the thumbnail SVG, (4) the Threads hook per Section 4. Include a `tistory_url` field in the `pending_posts/<slug>.json` pointing to the Tistory draft's GitHub blob URL:
  ```
  https://github.com/leoleo0813/blog-automation/blob/main/tistory_drafts/<slug>.md
  ```
  so the Kakao notification carries a direct, easy-to-copy link to it (repo is public, so this is viewable without login).

## 6. Stock Beginner Series (Blogspot-only priority category)
- Tracked entirely in `stock_beginner_series.json` — 44 posts across 9 clusters (A–J), a Korean stock-investing-for-beginners series. This is a **new Blogger category, separate from the health Tistory blog** (leoleo0813/tistory-blog) and unrelated to this repo's own `tistory_drafts/` step.
- **Priority:** while any item in the queue is `"pending"`, it takes precedence over general trend research every run (see Section 5 Step 0). Process items in `id` order, one per run.
- **No Tistory draft for this series** — it publishes to Blogger only. Skip the `tistory_drafts/<slug>.md` step and the Tistory-rewrite framing; write the Blogger post directly as the complete, authoritative piece. Leave `tistory_url` out of `pending_posts/<slug>.json` (or empty string).
- **Still follow Section 2's Blogger Post structure requirements** (TL;DR box, accent-bordered H2s, highlight spans, info boxes, closing recap, thumbnail, metadata) and Section 4's Threads hook guidelines — those apply regardless of category.
- **Label:** every post in this series must include the Blogger label `주식초보` (in addition to 1-2 topic-specific labels), so the series can be filtered/browsed as one category.
- **Writing principles (mandatory, do not soften — financial YMYL, same spirit as health YMYL):**
  1. Plain language a middle-schooler could follow; short sentences.
  2. Consistent `~습니다` sentence-ending style throughout.
  3. Never recommend or name a specific stock ticker, brokerage, or fund — use generic phrasing ("어떤 기업의 주식") instead of real names/examples.
  4. Never use absolute/certainty claims ("반드시 오릅니다", "무조건 수익") — describe possibilities and general principles only.
  5. Every post must end with this exact disclaimer line: "이 글은 정보 제공을 목적으로 하며, 투자 판단과 그 책임은 전적으로 본인에게 있습니다."
  6. Cite authoritative public sources where relevant (금융감독원, 한국거래소, 한국예탁결제원, etc.) — if a fact can't be verified via WebSearch, state it as general/common knowledge rather than attributing it to an unverified source.
- **After successfully publishing an item:** update its entry in `stock_beginner_series.json` — set `"status": "done"` and add a `"published_slug"` field with the post's slug — and commit that change together with the usual `pending_posts/*.json` + thumbnail files.
