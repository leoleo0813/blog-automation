"""티스토리 자동 업로드 (PC에서 실행). 2026-11-20 사용자 요청.

흐름: 저장소(PC에 복제)에서 아직 안 올린 초안 1편을 골라
  ① 썸네일·본문 그림을 티스토리에 직접 업로드
  ② 본문 첫 줄에 썸네일, 그림 자리(assets/figures)에 업로드한 그림을 넣고
  ③ 제목·태그·카테고리·고유주소를 채운 뒤
  ④ --mode draft 면 임시저장, --mode private 면 비공개 발행
캐러셀 카드는 옆으로 넘기는 HTML이 깨지지 않도록 지금처럼 저장소 주소로 둔다.

처음 한 번:  python tistory_upload.py --login      (열린 창에서 직접 로그인 → 창 닫기)
시험:        python tistory_upload.py --mode draft --slug <슬러그>
평소(예약):  python tistory_upload.py --mode private

티스토리 화면이 바뀌면 멈출 수 있다. 단계마다 logs/ 에 화면을 저장하니, 멈추면 그 사진을 보내 주면 고친다.
비밀번호는 이 프로그램이 다루지 않는다. 로그인은 사람이 직접, 그 상태(쿠키)는 profile/ 폴더에만 남는다.
"""
import argparse
import datetime
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / 'config.json').read_text(encoding='utf-8')) if (HERE / 'config.json').exists() else {}
REPO = Path(CFG.get('repo_path') or HERE.parent)
BLOG = CFG.get('blog', 'sensitiveboss3')
PROFILE = HERE / 'profile'
LOGS = HERE / 'logs'
STATE = HERE / 'state.json'
AUTH = HERE / 'auth.json'   # 로그인 쿠키(이 PC에만, 저장소에 올라가지 않음)
RAW = 'https://raw.githubusercontent.com/leoleo0813/blog-automation/main/'
IMG_TOKEN = re.compile(r'\[##_Image\|.*?_##\]', re.S)


def log(msg):
    line = f"[{datetime.datetime.now():%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    LOGS.mkdir(exist_ok=True)
    with open(LOGS / 'upload.log', 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def shot(page, name):
    LOGS.mkdir(exist_ok=True)
    try:
        page.screenshot(path=str(LOGS / f"{datetime.datetime.now():%m%d-%H%M%S}-{name}.png"), full_page=False)
    except Exception:
        pass


def load_state():
    return json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {'done': {}}


def save_state(st):
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding='utf-8')


def front_matter(text):
    lines = text.splitlines()
    fm, i = {}, 1
    while i < len(lines) and lines[i].strip() != '---':
        m = re.match(r'^([A-Za-z_]+):\s?(.*)$', lines[i])
        if m and m.group(2) != '|':
            fm[m.group(1)] = m.group(2).strip()
        i += 1
    body = '\n'.join(lines[i + 1:]).strip()
    return fm, body


def pick_post(st, slug=None):
    series = json.loads((REPO / 'stock_beginner_series.json').read_text(encoding='utf-8'))
    min_id = int(CFG.get('min_id', 194))
    for p in sorted(series['items'], key=lambda x: int(x.get('order', x.get('id', 0)) or 0)):
        s = p.get('slug')
        if slug and s != slug:
            continue
        if not slug and (int(p.get('id') or 0) < min_id or s in st['done'] or p.get('status') != 'drafted' or not p.get('gate_pass')):
            continue
        path = REPO / 'stock_drafts' / f'{s}.md'
        if slug and not path.exists():   # 시험용: 이미 발행한 글도 --slug로 지정하면 쓸 수 있게
            path = REPO / 'stock_drafts' / '발행완료' / f'{s}.md'
        if path.exists():
            return s, path
    return None, None


def build_parts(path):
    fm, body = front_matter(path.read_text(encoding='utf-8'))
    slug = fm.get('slug') or path.stem
    thumb = REPO / 'assets' / 'thumbnails' / f'{slug}.png'
    figs = []  # (원래 <figure>...</figure> 전체, 로컬 파일)
    for m in re.finditer(r'<figure[^>]*>\s*<img src="' + re.escape(RAW) + r'(assets/figures/[^"]+)".*?</figure>', body, re.S):
        figs.append((m.group(0), REPO / m.group(1)))
    return fm, body, thumb, figs


# ---------------- 브라우저 조작 ----------------

CDP_URL = CFG.get('cdp_url', 'http://127.0.0.1:9222')


def open_browser(p):
    """start_chrome.bat으로 띄운 '일반 크롬'(사람이 로그인한 창)에 연결한다. 연결이 안 되면 예전 방식으로 연다."""
    try:
        browser = p.chromium.connect_over_cdp(CDP_URL, timeout=5000)
        ctx = browser.contexts[0] if browser.contexts else browser.new_context()
        log('일반 크롬에 연결했어요.')
        return ctx, (lambda: None)   # 사람이 쓰는 크롬이니 닫지 않는다
    except Exception:
        log('일반 크롬을 찾지 못했어요. start_chrome.bat 을 먼저 실행해 주세요. (예전 방식으로 시도)')
        ctx = p.chromium.launch_persistent_context(str(PROFILE), headless=bool(CFG.get('headless', False)),
                                                   channel=CFG.get('browser_channel') or None,
                                                   permissions=['clipboard-read', 'clipboard-write'])
        restore_cookies(ctx)
        return ctx, ctx.close


def handle_dialogs(page):
    def on_dialog(d):
        msg = d.message or ''
        log(f'알림창: {msg[:60]}')
        if '저장된 글' in msg or '이어서' in msg:   # 예전 임시저장 글 불러오기 → 새로 쓰기
            d.dismiss()
        else:
            d.accept()
    page.on('dialog', on_dialog)


def wait_editor(page):
    page.wait_for_function("window.tinymce && tinymce.activeEditor && tinymce.activeEditor.initialized", timeout=60000)


def set_mode(page, mode):
    """mode: '기본모드' 또는 'HTML'. 오른쪽 위 모드 선택 메뉴를 연다."""
    btn = page.locator('#editor-mode-layer-btn-open, button:has-text("기본모드"), button:has-text("HTML"), button:has-text("마크다운")').first
    btn.click()
    page.locator(f'#editor-mode-{"html" if mode == "HTML" else "kakao"}, .mce-menu-item:has-text("{mode}"), li:has-text("{mode}")').first.click()
    time.sleep(1.5)


def html_get(page):
    return page.evaluate("""() => {
        const cm = document.querySelector('.CodeMirror');
        if (cm && cm.CodeMirror) return cm.CodeMirror.getValue();
        const ta = document.querySelector('textarea.html-editor, #html-editor textarea');
        return ta ? ta.value : null; }""")


def html_set(page, html):
    ok = page.evaluate("""(html) => {
        const cm = document.querySelector('.CodeMirror');
        if (cm && cm.CodeMirror) { cm.CodeMirror.setValue(html); cm.CodeMirror.save && cm.CodeMirror.save(); return 'codemirror'; }
        return null; }""", html)
    if not ok:  # CodeMirror를 못 찾으면 실제 붙여넣기처럼 입력(편집기가 입력을 알아채도록)
        box = page.locator('.CodeMirror textarea, textarea').first
        box.click()
        page.keyboard.press('Control+A')
        page.evaluate("t => navigator.clipboard.writeText(t)", html)
        page.keyboard.press('Control+V')
        ok = 'paste'
    return ok


def upload_image(page, file):
    """기본모드에서 사진 1장을 올린다. 파일 선택 창은 Playwright가 직접 채운다."""
    before = page.evaluate("() => tinymce.activeEditor.getBody().querySelectorAll('img').length")
    try:
        with page.expect_file_chooser(timeout=8000) as fc:
            page.locator('#attach-layer-btn, button[aria-label*="첨부"], button:has-text("첨부")').first.click()
            page.locator('#attach-image, li:has-text("사진"), button:has-text("사진")').first.click()
        fc.value.set_files(str(file))
    except Exception:
        page.locator('input[type=file][accept*="image"], input[type=file]').first.set_input_files(str(file))
    page.wait_for_function(f"() => tinymce.activeEditor.getBody().querySelectorAll('img').length > {before}", timeout=60000)
    time.sleep(1)


def publish(page, fm, mode):
    tags = [t.strip() for t in (fm.get('tags') or '').split(',') if t.strip()]
    tag_in = page.locator('#tagText, input[placeholder*="태그"]').first
    for t in tags:
        tag_in.fill(t)
        tag_in.press('Enter')
    if mode == 'draft':
        page.locator('button:has-text("임시저장"), a:has-text("임시저장")').first.click()
        time.sleep(3)
        return
    page.locator('#publish-layer-btn, button:has-text("완료")').first.click()
    time.sleep(1.5)
    page.locator('label:has-text("비공개"), #open0').first.click()
    cat = CFG.get('categories', {}).get(fm.get('track', ''), '')
    if cat:
        try:
            page.locator('#category-btn, button:has-text("카테고리")').first.click()
            page.locator(f'.mce-menu-item:has-text("{cat}"), li:has-text("{cat}"), span:has-text("{cat}")').first.click()
        except Exception as e:
            log(f'카테고리 선택 실패(직접 지정 필요): {e}')
    slug = fm.get('slug', '')
    try:
        url_in = page.locator('input[placeholder*="URL"], #post-permalink, input[name="slogan"]').first
        if url_in.count():
            url_in.fill(slug)
    except Exception as e:
        log(f'고유주소 입력 실패(직접 확인 필요): {e}')
    shot(page, 'publish-layer')
    page.locator('#publish-btn, button:has-text("비공개 저장"), button:has-text("저장"), button:has-text("발행")').last.click()
    time.sleep(4)


def run(mode, slug=None, keep_open=False):
    from playwright.sync_api import sync_playwright
    st = load_state()
    s, path = pick_post(st, slug)
    if not s:
        log('올릴 초안이 없어요.')
        return 0
    fm, body, thumb, figs = build_parts(path)
    log(f'시작: {s} ({mode}) · 그림 {len(figs)}장 + 썸네일 {"있음" if thumb.exists() else "없음"}')
    with sync_playwright() as p:
        ctx, close = open_browser(p)
        page = ctx.new_page()
        handle_dialogs(page)
        page.goto(f'https://{BLOG}.tistory.com/manage/newpost/?type=post&returnURL=ENTRY', wait_until='domcontentloaded')
        time.sleep(3)
        log(f'열린 주소: {page.url} · 저장된 로그인 정보: {"있음" if AUTH.exists() else "없음"}')
        if 'auth/login' in page.url or 'accounts.kakao' in page.url:
            log('로그인이 풀렸어요. --login 으로 다시 로그인해 주세요.')
            shot(page, 'need-login')
            page.close(); close()
            return 2
        wait_editor(page)
        shot(page, '1-editor')
        page.locator('#post-title-inp, textarea[placeholder*="제목"], input[placeholder*="제목"]').first.fill(fm.get('title', s))

        # ① 그림 업로드(썸네일 먼저, 그다음 본문 그림 순서) → HTML 모드에서 티스토리 그림 표시를 순서대로 모은다
        files = ([thumb] if thumb.exists() else []) + [f for _, f in figs]
        for f in files:
            upload_image(page, f)
            log(f'업로드: {f.name}')
        shot(page, '2-uploaded')
        set_mode(page, 'HTML')
        tokens = IMG_TOKEN.findall(html_get(page) or '')
        if len(tokens) < len(files):
            log(f'그림 표시를 {len(tokens)}개만 찾았어요(필요 {len(files)}개). 저장소 주소 그림으로 대신해요.')
            tokens = []
        # ② 본문 조립: 첫 줄 썸네일, figure 자리마다 업로드한 그림
        html = body
        if tokens:
            k = 0
            if thumb.exists():
                html = f'<p>{tokens[0]}</p>\n' + html
                k = 1
            for (orig, _), tok in zip(figs, tokens[k:]):
                cap = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', orig, re.S)
                html = html.replace(orig, f'<p>{tok}</p>' + (f'\n<p style="font-size:13px;color:#888;text-align:center;">{cap.group(1)}</p>' if cap else ''), 1)
        how = html_set(page, html)
        log(f'본문 입력 방식: {how}')
        set_mode(page, '기본모드')
        n = page.evaluate("() => tinymce.activeEditor.getContent({format:'text'}).length")
        shot(page, '3-body')
        if n < 1000:
            log(f'본문이 {n}자뿐이에요. 저장하지 않고 멈춰요.')
            if not keep_open:
                page.close(); close()
            return 3
        log(f'본문 확인: {n}자')
        publish(page, fm, mode)
        shot(page, '4-saved')
        if mode == 'private':   # 시험(임시저장)은 기록하지 않는다 → 나중에 자동 실행 때 다시 올라간다
            st['done'][s] = {'mode': mode, 'at': datetime.datetime.now().isoformat(timespec='minutes')}
            save_state(st)
        log(f'완료: {s} ({mode})')
        if keep_open:
            input('창을 확인한 뒤 Enter를 누르면 닫혀요...')
        page.close(); close()
    return 0


def login():
    """사람이 직접 로그인 → 글쓰기 화면이 열리는지 확인 → 로그인 쿠키를 auth.json에 저장(브라우저를 닫아도 유지)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(str(PROFILE), headless=False, channel=CFG.get('browser_channel') or None)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto('https://www.tistory.com/auth/login')
        print('열린 창에서 [카카오계정으로 로그인] → 아이디·비밀번호 입력 시 "로그인 상태 유지"를 꼭 체크하세요.')
        input('로그인이 끝나 티스토리 화면이 보이면 여기서 Enter를 누르세요...')
        page.goto(f'https://{BLOG}.tistory.com/manage/newpost/?type=post&returnURL=ENTRY', wait_until='domcontentloaded')
        time.sleep(3)
        log(f'확인 주소: {page.url}')
        if 'auth/login' in page.url or 'accounts.kakao' in page.url:
            log('아직 로그인되지 않았어요. 다시 setup.bat 또는 --login 을 실행해 주세요.')
            shot(page, 'login-failed')
            ctx.close()
            return 1
        ctx.storage_state(path=str(AUTH))
        log('로그인 확인 완료: 글쓰기 화면이 열렸어요. 로그인 정보를 저장했어요.')
        shot(page, 'login-ok')
        ctx.close()
    return 0


def restore_cookies(ctx):
    if AUTH.exists():
        try:
            ctx.add_cookies(json.loads(AUTH.read_text(encoding='utf-8')).get('cookies', []))
        except Exception as e:
            log(f'저장된 로그인 정보를 불러오지 못했어요: {e}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--login', action='store_true')
    ap.add_argument('--mode', choices=['draft', 'private'], default='draft')
    ap.add_argument('--slug')
    ap.add_argument('--keep-open', action='store_true')
    ap.add_argument('--mark-done', nargs='*', help='이미 직접 올린 글의 슬러그(자동 업로드 대상에서 뺌)')
    ap.add_argument('--list', action='store_true', help='다음에 올릴 순서 보기')
    a = ap.parse_args()
    if a.mark_done is not None:
        st = load_state()
        for x in a.mark_done:
            st['done'][x] = {'mode': 'manual', 'at': datetime.datetime.now().isoformat(timespec='minutes')}
        save_state(st)
        log(f'직접 올린 글로 표시: {a.mark_done}')
        sys.exit(0)
    if a.list:
        st = load_state()
        for _ in range(10):
            s, _p = pick_post(st)
            if not s:
                break
            print(s)
            st['done'][s] = {}
        sys.exit(0)
    if a.login:
        sys.exit(login())
    sys.exit(run(a.mode, a.slug, a.keep_open))
