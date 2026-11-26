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
MOD = 'Meta' if sys.platform == 'darwin' else 'Control'   # Mac은 Cmd, Windows는 Ctrl
SHARED = REPO / 'office' / 'uploaded.json'   # 여러 PC(Windows·Mac)가 같이 보는 '올린 글' 기록(저장소에 올라감)
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
    st = json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {'done': {}}
    if SHARED.exists():   # 다른 PC가 올린 글도 '완료'로 본다
        for k, v in json.loads(SHARED.read_text(encoding='utf-8')).items():
            st['done'].setdefault(k, v)
    return st


def share_done(slug, info):
    """비공개 발행 성공을 저장소(office/uploaded.json)에 기록하고 올린다 → 다른 PC가 같은 글을 또 올리지 않는다."""
    import platform
    import subprocess
    g = lambda *a: subprocess.run(['git', '-C', str(REPO), *a], capture_output=True, text=True)
    g('pull', '--rebase', '--autostash', '-q')
    d = json.loads(SHARED.read_text(encoding='utf-8')) if SHARED.exists() else {}
    d[slug] = dict(info, machine=platform.node())
    SHARED.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    g('add', str(SHARED))
    g('commit', '-q', '-m', f'업로드 기록: {slug} 비공개 발행')
    r = g('push', '-q')
    log('올린 글 기록 공유: ' + ('완료' if r.returncode == 0 else '실패(나중에 git push 해 주세요) ' + r.stderr[-120:]))


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


def chrome_path():
    import shutil
    if sys.platform == 'darwin':
        cands = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                 str(Path.home() / 'Applications/Google Chrome.app/Contents/MacOS/Google Chrome')]
    elif sys.platform.startswith('win'):
        import os
        cands = [str(Path(os.environ.get(k, '')) / 'Google/Chrome/Application/chrome.exe')
                 for k in ('PROGRAMFILES', 'PROGRAMFILES(X86)', 'LOCALAPPDATA')]
    else:
        cands = [shutil.which('google-chrome') or '', shutil.which('chromium') or '']
    return next((c for c in cands if c and Path(c).is_file()), None)


def start_chrome():
    """업로드용 '일반 크롬'(chrome-profile 폴더, 9222 포트)을 띄운다. Windows·Mac 공통. 이미 떠 있으면 그대로 쓴다."""
    import subprocess
    import urllib.request
    try:
        urllib.request.urlopen(CDP_URL + '/json/version', timeout=2)
        return True
    except Exception:
        pass
    c = chrome_path()
    if not c:
        log('크롬을 찾지 못했어요. 크롬을 설치해 주세요.')
        return False
    subprocess.Popen([c, '--remote-debugging-port=9222', f'--user-data-dir={HERE / "chrome-profile"}', '--no-first-run',
                      f'https://{BLOG}.tistory.com/manage'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(30):
        time.sleep(1)
        try:
            urllib.request.urlopen(CDP_URL + '/json/version', timeout=2)
            log('업로드용 크롬을 띄웠어요.')
            time.sleep(2)
            return True
        except Exception:
            continue
    return False


def open_browser(p):
    """업로드용 '일반 크롬'(사람이 로그인한 창)에 연결한다. 꺼져 있으면 직접 띄운다."""
    start_chrome()
    try:
        browser = p.chromium.connect_over_cdp(CDP_URL, timeout=8000)
        ctx = browser.contexts[0] if browser.contexts else browser.new_context()
        try:
            ctx.grant_permissions(['clipboard-read', 'clipboard-write'], origin=f'https://{BLOG}.tistory.com')
        except Exception:
            pass
        log('일반 크롬에 연결했어요.')
        return ctx, (lambda: None)   # 사람이 쓰는 크롬이니 닫지 않는다
    except Exception:
        log('일반 크롬에 연결하지 못했어요. (예전 방식으로 시도)')
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


def dismiss_resume_popup(page):
    """'작성 중인 글이 있습니다. 이어서 쓰시겠어요?' 안내 창(웹 화면 안의 창)이 뜨면 새로 쓰기를 고른다."""
    for _ in range(6):
        try:
            box = page.locator('text=/이어서|작성 중인 글|저장된 글/').first
            if box.count() and box.is_visible():
                for label in ('취소', '아니요', '아니오', '새로 작성', '새 글', '새로쓰기'):
                    btn = page.locator(f'button:has-text("{label}"), a:has-text("{label}")').first
                    if btn.count() and btn.is_visible():
                        btn.click()
                        log(f'이어 쓰기 안내 창 → [{label}]')
                        time.sleep(1.5)
                        return True
                shot(page, 'resume-popup')
                log('이어 쓰기 안내 창의 버튼을 찾지 못했어요. 최근 사진을 보내 주세요.')
                return False
        except Exception:
            pass
        time.sleep(1)
    return False


def wait_editor(page):
    try:
        page.wait_for_function("window.tinymce && tinymce.activeEditor && tinymce.activeEditor.initialized", timeout=25000)
    except Exception:
        info = page.evaluate("""() => ({
            title: document.title,
            keys: Object.keys(window).filter(k => /editor|tiny|mce|tx|kakao/i.test(k)).slice(0, 30),
            iframes: [...document.querySelectorAll('iframe')].map(f => f.id || f.name || f.src).slice(0, 10),
            buttons: [...document.querySelectorAll('button')].map(b => (b.id || '') + ':' + (b.innerText || '').trim()).filter(x => x.length > 1).slice(0, 40),
            inputs: [...document.querySelectorAll('input,textarea')].map(i => (i.id || i.name || '') + ':' + (i.placeholder || '')).slice(0, 20),
            modal: [...document.querySelectorAll('[role=dialog], .layer_popup, .modal')].map(m => (m.innerText || '').trim().slice(0, 80)).slice(0, 5)
        })""")
        (LOGS / 'editor-info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')
        log('편집기를 찾지 못했어요. logs/editor-info.json 과 최근 사진을 보내 주세요.')
        shot(page, 'editor-not-found')
        raise


def click_first(page, selectors, what, timeout=4000):
    """여러 후보 중 화면에 보이는 첫 번째를 누른다. 누른 후보를 기록한다."""
    for sel in selectors:
        try:
            loc = page.locator(sel).locator('visible=true').first
            if loc.count():
                loc.click(timeout=timeout)
                log(f'{what}: {sel}')
                return True
        except Exception:
            continue
    log(f'{what}: 버튼을 찾지 못했어요')
    shot(page, f'notfound-{what}')
    return False


def set_mode(page, mode):
    """mode: '기본모드' 또는 'HTML'. 오른쪽 위 모드 메뉴를 열고 고른다."""
    click_first(page, ['#editor-mode-layer-btn-open', 'button:has-text("기본모드")', 'button:has-text("HTML")',
                       'button:has-text("마크다운")', '[class*=mode] button'], '모드 메뉴 열기')
    time.sleep(0.8)
    target = ['#editor-mode-html', '[id*=mode-html]', 'text="HTML"'] if mode == 'HTML' else \
             ['#editor-mode-kakao', '[id*=mode-kakao]', 'text="기본모드"']
    if not click_first(page, target, f'{mode} 고르기'):
        raise RuntimeError(f'{mode} 모드로 바꾸지 못했어요')
    time.sleep(2)


def dump_page_info(page):
    info = page.evaluate("""() => {
        const vis = e => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
        const pick = e => ({tag: e.tagName, id: e.id, cls: (e.className && e.className.baseVal === undefined ? e.className : '').toString().slice(0, 60),
                            text: (e.innerText || e.value || '').trim().slice(0, 30), label: e.getAttribute('aria-label') || '', vis: vis(e)});
        return {
            ids: [...document.querySelectorAll('[id]')].filter(e => /mode|attach|publish|category|tag|title|open|image|photo/i.test(e.id)).map(pick).slice(0, 80),
            buttons: [...document.querySelectorAll('button')].filter(vis).map(pick).slice(0, 80),
            codemirror: !!document.querySelector('.CodeMirror')
        }; }""")
    (LOGS / 'page-info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')


VISIBLE_CM = """() => [...document.querySelectorAll('.CodeMirror')].filter(e => e.offsetWidth || e.offsetHeight || e.getClientRects().length)"""


def html_get(page):
    return page.evaluate(f"""() => {{ const cms = ({VISIBLE_CM})(); return cms.length && cms[0].CodeMirror ? cms[0].CodeMirror.getValue() : null; }}""")


def html_set(page, html):
    """보이는 HTML 칸에 실제 붙여넣기(Ctrl+V)로 넣는다. 티스토리 편집기는 붙여넣기로 넣어야 내용을 받는다(2026-11-20 확인)."""
    page.evaluate("t => navigator.clipboard.writeText(t)", html)
    page.locator('.CodeMirror:visible').first.click()
    page.keyboard.press(f'{MOD}+A')
    page.keyboard.press(f'{MOD}+V')
    time.sleep(2)
    n = len(html_get(page) or '')
    log(f'HTML 칸 붙여넣기: {n}자')
    return 'paste'


def upload_info(page):
    info = page.evaluate("""() => ({
        files: [...document.querySelectorAll('input[type=file]')].map(i => ({id: i.id, name: i.name, accept: i.accept, cls: i.className})),
        buttons: [...document.querySelectorAll('button')].map(b => (b.id || '') + '|' + (b.getAttribute('aria-label') || '') + '|' + (b.innerText || '').trim()).filter(x => x.length > 2).slice(0, 60)
    })""")
    (LOGS / 'upload-info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')
    return info


def img_count(page):
    return page.evaluate("() => tinymce.activeEditor.getBody().querySelectorAll('img').length")


ATTACH_BTN = ['#mceu_0-open', '#mceu_0 button', '#attach-layer-btn', '#mceu_0', 'button[aria-label*="첨부"]', 'button[aria-label*="사진"]',
              '[class*=attach] button', '[class*=attach]', '[class*=image] button[class*=open]']


def open_attach_menu(page):
    """도구 막대 맨 왼쪽 그림 버튼(옆에 ▾)을 눌러 [사진 / 파일 / 슬라이드쇼] 메뉴를 연다(2026-11-20 사용자 캡처)."""
    if click_first(page, ATTACH_BTN, '첨부(그림) 버튼'):
        return True
    # 이름으로 못 찾으면: 굵게(B) 버튼보다 왼쪽에 있는, 도구 막대 줄의 맨 왼쪽 버튼을 누른다
    box = page.evaluate("""() => {
        const vis = e => e.offsetWidth && e.offsetHeight;
        const bold = [...document.querySelectorAll('button, [role=button], div[class*=btn]')].find(e => vis(e) &&
            /굵게|bold/i.test((e.getAttribute('aria-label') || '') + (e.title || '') + e.className));
        if (!bold) return null;
        const r = bold.getBoundingClientRect(), y = r.top + r.height / 2;
        const cands = [...document.querySelectorAll('button, [role=button], div[class*=btn], span[class*=btn]')].filter(e => {
            if (!vis(e)) return false; const q = e.getBoundingClientRect();
            return Math.abs(q.top + q.height / 2 - y) < 12 && q.right < r.left && q.width < 80; });
        cands.sort((p, q) => p.getBoundingClientRect().left - q.getBoundingClientRect().left);
        if (!cands.length) return null;
        const q = cands[0].getBoundingClientRect();
        return {x: q.left + q.width / 2, y: q.top + q.height / 2, html: cands[0].outerHTML.slice(0, 300)}; }""")
    if not box:
        return False
    (LOGS / 'attach-info.json').write_text(json.dumps(box, ensure_ascii=False, indent=2), encoding='utf-8')
    page.mouse.click(box['x'], box['y'])
    log('첨부(그림) 버튼: 위치로 누름')
    return True


def upload_image(page, file):
    """기본모드에서 사진 1장을 올린다. [그림 버튼 ▾] → [사진] → 파일 선택 창에 파일을 넣는다."""
    before = img_count(page)
    try:
        if not open_attach_menu(page):
            return False
        time.sleep(0.8)
        with page.expect_file_chooser(timeout=10000) as fc:
            if not click_first(page, ['#attach-image', '[id*=attach-image]', 'text="사진"', 'li:has-text("사진")',
                                      'button:has-text("사진")'], '사진 메뉴'):
                raise RuntimeError('사진 메뉴 없음')
        fc.value.set_files(str(file))
        page.wait_for_function(f"() => tinymce.activeEditor.getBody().querySelectorAll('img').length > {before}", timeout=40000)
        time.sleep(1.5)
        return True
    except Exception as e:
        log(f'사진 올리기 실패: {str(e).splitlines()[0][:120]}')
        page.keyboard.press('Escape')
        return False


def set_permalink(page, slug):
    """발행 창의 URL 줄에서 입력 칸을 찾아 영어 고유주소로 바꾼다."""
    js = """(slug) => {
        const vis = e => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
        const label = [...document.querySelectorAll('dt, th, strong, span, div, label')].find(e => vis(e) && e.innerText && e.innerText.trim() === 'URL');
        if (!label) return 'URL 줄 없음';
        let row = label; for (let i = 0; i < 4 && row && !row.querySelector('input'); i++) row = row.parentElement;
        const inp = row && [...row.querySelectorAll('input')].find(vis);
        if (!inp) { const span = row && [...row.querySelectorAll('span, a, div')].find(e => vis(e) && /entry/.test(e.innerText || '')); if (span) span.click(); return 'retry'; }
        const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
        inp.focus(); set.call(inp, slug); inp.dispatchEvent(new Event('input', {bubbles: true})); inp.dispatchEvent(new Event('change', {bubbles: true}));
        return 'ok:' + inp.value; }"""
    r = page.evaluate(js, slug)
    if r == 'retry':
        time.sleep(0.8)
        r = page.evaluate(js, slug)
    log(f'URL 설정: {r}')
    if not str(r).startswith('ok'):
        log('URL 입력 칸을 찾지 못했어요. 발행 뒤 글 수정에서 URL을 직접 바꿔 주세요.')
        shot(page, 'notfound-URL')


def set_cover(page, thumb):
    """발행 창 오른쪽 [대표이미지 추가](.box_thumb).
    본문이 비어 있으면 파일 선택 창이 뜨고, 본문에 그림이 있으면 본문 그림 고르는 창이 뜬다(2026-11-20 확인).
    → 파일 창이면 썸네일 파일을 넣고, 고르는 창이면 첫 번째 그림(= 본문 첫 줄 썸네일)을 고른다."""
    if not thumb or not Path(thumb).exists():
        log('대표이미지: 썸네일 파일이 없어 건너뜀')
        return
    has = page.evaluate("() => { const b = document.querySelector('.box_thumb'); return !!(b && [...b.querySelectorAll('img')].some(i => i.offsetWidth || i.naturalWidth)); }")
    if has:
        log('대표이미지: 이미 들어가 있어요(본문 첫 그림 = 썸네일) → 그대로 둠')
        return
    chosen = []
    def on_chooser(fc):
        try:
            fc.set_files(str(thumb)); chosen.append(1)
        except Exception as e:
            log(f'대표이미지 파일 넣기 실패: {e}')
    page.on('filechooser', on_chooser)
    try:
        before = page.evaluate("() => [...document.querySelectorAll('img')].filter(i => i.offsetWidth).map(i => i.src)")
        if not click_first(page, ['.box_thumb .txt_thumb', '.box_thumb .inner_box', '.box_thumb', 'text=대표이미지 추가'], '대표이미지 추가'):
            return
        time.sleep(3)
        if chosen:
            time.sleep(3)
            shot(page, 'cover-set')
            log(f'대표이미지 올림(파일): {Path(thumb).name}')
            return
        shot(page, 'cover-picker')
        info = page.evaluate("""(before) => {
            const vis = e => e.offsetWidth && e.offsetHeight;
            const imgs = [...document.querySelectorAll('img')].filter(vis);
            const fresh = imgs.filter(i => !before.includes(i.src) || i.closest('[class*=thumb], [class*=layer], [class*=Modal]'));
            return {count: imgs.length, fresh: fresh.slice(0, 12).map(i => ({src: i.src.slice(-90), cls: String(i.className),
                    parent: String(i.parentElement && i.parentElement.className).slice(0, 60)})),
                    buttons: [...document.querySelectorAll('button')].filter(vis).map(b => (b.innerText || '').trim()).filter(Boolean).slice(-15)}; }""", before)
        (LOGS / 'cover-layer.json').write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')
        r = page.evaluate("""() => {
            const vis = e => e.offsetWidth && e.offsetHeight;
            const modal = [...document.querySelectorAll('.ReactModal__Content, [class*=layer]')].filter(vis).pop() || document;
            const img = [...modal.querySelectorAll('img')].filter(vis).find(i => !i.closest('.box_thumb'));
            if (!img) return 'none';
            (img.closest('button, a, li, label') || img).click();
            return 'ok:' + img.src.slice(-70); }""")
        log(f'대표이미지 고르기: {r}')
        time.sleep(1)
        click_first(page, ['button:has-text("확인")', 'button:has-text("선택")', 'button:has-text("적용")', 'button:has-text("등록")'], '대표이미지 확인')
        time.sleep(2)
        shot(page, 'cover-set')
    except Exception as e:
        log(f'대표이미지 실패: {str(e).splitlines()[0][:120]} — 발행 뒤 글 수정에서 직접 넣어 주세요.')
        shot(page, 'notfound-cover')
    finally:
        page.remove_listener('filechooser', on_chooser)


SCHEDULE = REPO / 'office' / 'schedule.json'   # 예약해 둔 시간(여러 PC 공통)
DEFAULT_SLOTS = ['토 09:00', '토 19:00', '일 09:00', '일 19:00']   # 주말 예약 기본값(config.json의 schedule_slots로 바꿀 수 있음)
WD = '월화수목금토일'


def next_slot():
    """아직 비어 있는 다음 예약 시간(지금부터 30분 이후). office/schedule.json에 잡힌 시간은 건너뛴다."""
    taken = set()
    if SCHEDULE.exists():
        taken = {v.get('at') for v in json.loads(SCHEDULE.read_text(encoding='utf-8')).values()}
    slots = CFG.get('schedule_slots') or DEFAULT_SLOTS
    now = datetime.datetime.now()
    for day in range(0, 60):
        d = now.date() + datetime.timedelta(days=day)
        for sl in slots:
            wd, hm = sl.split()
            if WD[d.weekday()] != wd and wd != '매일':
                continue
            h, m = map(int, hm.split(':'))
            at = datetime.datetime(d.year, d.month, d.day, h, m)
            if at > now + datetime.timedelta(minutes=30) and at.strftime('%Y-%m-%d %H:%M') not in taken:
                return at
    return None


def share_schedule(slug, at):
    import platform
    import subprocess
    g = lambda *a: subprocess.run(['git', '-C', str(REPO), *a], capture_output=True, text=True)
    g('pull', '--rebase', '--autostash', '-q')
    d = json.loads(SCHEDULE.read_text(encoding='utf-8')) if SCHEDULE.exists() else {}
    d[slug] = {'at': at.strftime('%Y-%m-%d %H:%M'), 'machine': platform.node()}
    SCHEDULE.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    g('add', str(SCHEDULE)); g('commit', '-q', '-m', f'예약 발행 기록: {slug} {d[slug]["at"]}'); g('push', '-q')


VIS_JS = """(want) => {
    const vis = e => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
    const radios = [...document.querySelectorAll('input[type=radio]')];
    const labelOf = r => { const l = r.id && document.querySelector(`label[for="${r.id}"]`) || r.closest('label') || r.parentElement;
        return ((l && l.innerText) || '').replace(/\\s+/g, ''); };
    const r = radios.find(x => labelOf(x) === want);
    if (!r) return {found: false, checked: radios.filter(x => x.checked).map(labelOf)};
    if (want && !r.checked) { const l = r.id && document.querySelector(`label[for="${r.id}"]`) || r.closest('label'); (l && vis(l) ? l : r).click(); }
    return {found: true, ok: r.checked, checked: radios.filter(x => x.checked).map(labelOf)}; }"""


def open_state(page):
    """지금 공개 범위: 발행 버튼 글자로 판단('공개 발행'/'비공개 저장'/'예약 …'). 티스토리 라디오는 직접 그린 단추라 버튼 글자가 가장 확실하다."""
    bt = publish_button_text(page)
    if '비공개' in bt:
        return '비공개', bt
    if '보호' in bt:
        return '공개(보호)', bt
    if '공개' in bt or '예약' in bt or '발행' in bt:
        return '공개', bt
    return '', bt


def choose_open(page, want):
    """발행 창의 공개 범위(공개/비공개)를 누르고, 발행 버튼 글자로 실제로 바뀌었는지 확인."""
    cands = [f'label:visible:text-is("{want}")', f'text="{want}"', f'span:visible:text-is("{want}")']
    for i in range(3):
        cur, bt = open_state(page)
        if cur == want:
            log(f'공개 범위: {want} 확인(버튼 {bt!r})')
            return True
        try:   # 1) 라디오 칸이 있으면 그 라벨을 누른다
            r = page.evaluate(VIS_JS, want)
            if not r.get('found'):
                raise RuntimeError
        except Exception:
            click_first(page, cands[i % len(cands):] + cands[:i % len(cands)], f'{want} 선택')
        time.sleep(0.6)
    cur, bt = open_state(page)
    if cur != want:
        info = page.evaluate("""() => { const vis = e => !!(e.offsetWidth || e.offsetHeight);
            const lab = [...document.querySelectorAll('dt, th, strong, span, div')].find(e => vis(e) && (e.innerText || '').trim() === '기본');
            let row = lab; for (let i = 0; i < 4 && row && !/비공개/.test(row.innerText || ''); i++) row = row.parentElement;
            return row ? row.outerHTML.slice(0, 2500) : ''; }""")
        (LOGS / 'open-info.html').write_text(info or '', encoding='utf-8')
        log(f'공개 범위 {want} 선택 실패 — 버튼 {bt!r} (logs/open-info.html 기록)')
        return False
    log(f'공개 범위: {want} 확인(버튼 {bt!r})')
    return True


def schedule_values(page):
    """발행일 줄의 [날짜, 시, 분] 현재 값."""
    return page.evaluate("""() => {
        const vis = e => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
        const lab = [...document.querySelectorAll('dt, th, strong, span, div, label, p')].find(e => vis(e) && (e.innerText || '').trim() === '발행일');
        if (!lab) return [];
        let row = lab; for (let i = 0; i < 5 && row && row.querySelectorAll('input').length < 3; i++) row = row.parentElement;
        return [...row.querySelectorAll('input, select')].filter(vis).slice(0, 3).map(e => e.value); }""")


def schedule_ok(page, at):
    v = schedule_values(page)
    want = [at.strftime('%Y-%m-%d'), at.strftime('%H'), at.strftime('%M')]
    norm = lambda x: ''.join(ch for ch in str(x) if ch.isdigit()).lstrip('0') or '0'
    return len(v) >= 3 and all(norm(a) == norm(b) for a, b in zip(v, want)), v


def publish_button_text(page):
    try:
        return page.locator('#publish-btn').first.inner_text(timeout=2000).strip()
    except Exception:
        return ''


def set_schedule(page, at, skip_open=False):
    """발행 창: [공개] → 발행일 [예약] → 날짜·시간 입력. 확인되면 True. 화면 정보는 logs/schedule-info.json."""
    if not skip_open:
        if not choose_open(page, '공개'):
            return False
        time.sleep(0.4)
    if not click_first(page, ['label:visible:text-is("예약")', 'button:visible:text-is("예약")', 'text="예약"'], '예약 선택'):
        return False
    time.sleep(1)
    # '발행일' 줄 안의 입력 칸(날짜·시·분) — 2026-11-25 사용자 캡처: [2026-11-25] [10] : [16] 현재 | 예약
    row_js = """() => {
        const vis = e => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
        const lab = [...document.querySelectorAll('dt, th, strong, span, div, label, p')].find(e => vis(e) && (e.innerText || '').trim() === '발행일');
        if (!lab) return null;
        let row = lab; for (let i = 0; i < 5 && row && row.querySelectorAll('input').length < 3; i++) row = row.parentElement;
        return row; }"""
    info = page.evaluate("""() => { const row = (""" + row_js + """)(); if (!row) return {found: false};
        return {found: true, html: row.outerHTML.slice(0, 3000),
                inputs: [...row.querySelectorAll('input, select')].map(e => ({tag: e.tagName, type: e.type, cls: String(e.className).slice(0, 60),
                         val: e.value, ro: e.readOnly, vis: !!(e.offsetWidth || e.offsetHeight)}))}; }""")
    (LOGS / 'schedule-info.json').write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')
    if not info.get('found'):
        log('발행일 줄을 찾지 못했어요')
        shot(page, 'schedule')
        return False
    want = [at.strftime('%Y-%m-%d'), at.strftime('%H'), at.strftime('%M')]
    # 1) 사람이 치듯 입력(가능하면) 2) 안 되면 값 직접 넣기(React가 알아듣게 input·change 이벤트)
    page.evaluate("""([want]) => { const row = (""" + row_js + """)();
        const els = [...row.querySelectorAll('input, select')].filter(e => e.offsetWidth || e.offsetHeight);
        els.slice(0, 3).forEach((e, i) => { e.setAttribute('data-sched', String(i)); }); }""", [want])
    for i, v in enumerate(want):
        loc = page.locator(f'[data-sched="{i}"]')
        if not loc.count():
            continue
        try:
            if loc.evaluate('e => e.tagName') == 'SELECT':
                loc.select_option(v if loc.locator(f'option[value="{v}"]').count() else str(int(v)))
            elif not loc.evaluate('e => e.readOnly'):
                loc.click(); loc.fill(''); loc.type(v if i == 0 else v, delay=40); loc.press('Tab')
        except Exception:
            pass
        time.sleep(0.3)
    r = page.evaluate("""([want]) => {
        const setv = (e, v) => { const proto = e.tagName === 'SELECT' ? HTMLSelectElement.prototype : HTMLInputElement.prototype;
            Object.getOwnPropertyDescriptor(proto, 'value').set.call(e, v);
            ['input', 'change', 'blur'].forEach(t => e.dispatchEvent(new Event(t, {bubbles: true}))); };
        const norm = v => String(v).replace(/[^0-9]/g, '').replace(/^0+(?=\\d)/, '');
        const out = [];
        [0, 1, 2].forEach(i => { const e = document.querySelector(`[data-sched="${i}"]`); if (!e) { out.push(false); return; }
            if (norm(e.value) !== norm(want[i])) setv(e, i === 0 && /\\./.test(e.value) ? want[i].replace(/-/g, '.') : want[i]);
            out.push(norm(e.value) === norm(want[i])); });
        return out; }""", [want])
    log(f'예약 시간 입력: 날짜 {r[0]} / 시 {r[1]} / 분 {r[2]} → {want[0]} {want[1]}:{want[2]}')
    shot(page, 'schedule')
    return all(r)


def publish(page, fm, mode, thumb=None, at=None):
    tags = [t.strip() for t in (fm.get('tags') or '').split(',') if t.strip()]
    try:
        tag_in = page.locator('#tagText, input[placeholder*="태그"]').first
        for t in tags:
            tag_in.fill(t)
            tag_in.press('Enter')
        log(f'태그 {len(tags)}개 입력')
    except Exception as e:
        log(f'태그 입력 실패: {str(e).splitlines()[0][:80]}')
    if mode == 'draft':
        click_first(page, ['button:has-text("임시저장")', 'a:has-text("임시저장")'], '임시저장')
        time.sleep(3)
        return
    click_first(page, ['#publish-layer-btn', 'button:has-text("완료")'], '완료(발행 창 열기)')
    time.sleep(2)
    scheduled = False
    if mode == 'schedule' and at:
        scheduled = set_schedule(page, at)
        if not scheduled:   # 예약 시간을 못 넣었으면 절대 바로 공개하지 않고 비공개로 저장
            log('예약 시간을 넣지 못해서 비공개로 저장해요. logs/schedule-info.json과 schedule.png를 보내 주세요.')
    if not scheduled:
        if not choose_open(page, '비공개') and not click_first(page, ['label:visible:has-text("비공개")', 'text="비공개"'], '비공개 선택'):
            raise RuntimeError('비공개를 선택하지 못했어요')
    time.sleep(0.8)
    set_permalink(page, fm.get('slug', ''))
    # 대표이미지: 티스토리가 본문 첫 그림(= 첫 줄 썸네일)을 자동으로 쓴다(2026-11-25 확인). 칸을 누르면 발행 창 상태가 흔들려서 건드리지 않는다.
    if scheduled:   # 발행 직전: 공개인지 + 예약 시간이 그대로인지 확인(공개를 다시 누르면 발행일이 '현재'로 돌아가므로 순서 주의)
        bt = publish_button_text(page)
        log(f'발행 버튼 글자: {bt!r}')
        if '비공개' in bt:
            log('공개가 풀려 있어요 → 공개 다시 선택 후 예약 시간도 다시 입력')
            choose_open(page, '공개')
            time.sleep(0.5)
            set_schedule(page, at, skip_open=True)
        ok, vals = schedule_ok(page, at)
        if not ok:
            log(f'예약 시간이 바뀌어 있어요({vals}) → 다시 입력')
            set_schedule(page, at, skip_open=True)
            time.sleep(0.5)
            ok, vals = schedule_ok(page, at)
        bt = publish_button_text(page)
        log(f'최종 확인: 버튼 {bt!r} · 발행일 {vals}')
        if not ok or '비공개' in bt:
            log('예약 상태를 확정하지 못해서 바로 공개하지 않고 비공개로 저장해요. schedule.png를 보내 주세요.')
            choose_open(page, '비공개')
            scheduled = False
    shot(page, 'publish-layer')
    btns = (['button:visible:text-is("예약 발행")', 'button:visible:text-is("공개 예약")', 'button:visible:text-is("공개 발행")',
             '#publish-btn'] if scheduled else
            ['button:visible:has-text("비공개 발행")', 'button:visible:has-text("비공개 저장")', '#publish-btn', 'button:visible:has-text("발행")'])
    if not click_first(page, btns, '발행 버튼'):
        raise RuntimeError('발행 버튼을 찾지 못했어요')
    time.sleep(4)
    return scheduled


def parse_at(txt):
    """'2026-11-29 10:00' 또는 '2026-11-29T10:00' → datetime. 30분 이내·지난 시간이면 None."""
    try:
        at = datetime.datetime.strptime(txt.replace('T', ' ')[:16], '%Y-%m-%d %H:%M')
    except Exception:
        return None
    return at if at > datetime.datetime.now() + datetime.timedelta(minutes=10) else None


def run(mode, slug=None, keep_open=False, at_txt=None):
    at = None
    if mode == 'schedule':
        at = parse_at(at_txt) if at_txt else next_slot()
        if at_txt and not at:
            log(f'예약 시간 {at_txt}은 지났거나 너무 가까워요(10분 이후만 가능) → 비공개로 저장')
    if mode == 'schedule':
        log(f'예약 시간: {at:%Y-%m-%d %H:%M} ({WD[at.weekday()]})' if at else '빈 예약 시간이 없어요 → 비공개로 저장')
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
        dismiss_resume_popup(page)
        wait_editor(page)
        dump_page_info(page)
        shot(page, '1-editor')
        page.locator('#post-title-inp, textarea[placeholder*="제목"], input[placeholder*="제목"]').first.fill(fm.get('title', s))

        # ① 그림 업로드(썸네일 먼저, 그다음 본문 그림 순서). 하나라도 실패하면 저장소 주소 그림으로 대신한다.
        files = ([thumb] if thumb.exists() else []) + [f for _, f in figs]
        info = upload_info(page)
        log(f'파일 입력 칸 {len(info["files"])}개 발견')
        try:
            page.evaluate('() => tinymce.activeEditor.focus()')   # 커서를 본문으로(제목 칸에 머물지 않게)
        except Exception:
            pass
        uploaded = True
        for f in files:
            if not upload_image(page, f):
                uploaded = False
                log(f'그림 업로드 실패({f.name}) → 저장소 주소 그림으로 대신해요.')
                shot(page, 'upload-failed')
                break
            log(f'업로드: {f.name}')
        set_mode(page, 'HTML')
        tokens = IMG_TOKEN.findall(html_get(page) or '') if uploaded else []
        if uploaded and len(tokens) < len(files):
            log(f'그림 표시를 {len(tokens)}개만 찾았어요(필요 {len(files)}개). 저장소 주소 그림으로 대신해요.')
            tokens = []
        # ② 본문 조립: 첫 줄 썸네일, figure 자리마다 업로드한 그림(실패 시 저장소 주소 그대로)
        html = body
        if tokens:
            k = 0
            if thumb.exists():
                html = f'<p>{tokens[0]}</p>\n' + html
                k = 1
            for (orig, _), tok in zip(figs, tokens[k:]):
                cap = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', orig, re.S)
                html = html.replace(orig, f'<p>{tok}</p>' + (f'\n<p style="font-size:13px;color:#888;text-align:center;">{cap.group(1)}</p>' if cap else ''), 1)
        elif thumb.exists():
            html = f'<p style="text-align:center;"><img src="{RAW}assets/thumbnails/{s}.png" alt="{fm.get("title", s)}" style="max-width:100%;"></p>\n' + html
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
        scheduled = publish(page, fm, mode, thumb, at)
        if scheduled:
            share_schedule(s, at)
            log(f'예약 발행 완료: {at:%m/%d %H:%M} 공개 예정')
        shot(page, '4-saved')
        if mode in ('private', 'schedule'):   # 시험(임시저장)은 기록하지 않는다 → 나중에 자동 실행 때 다시 올라간다
            st['done'][s] = {'mode': mode, 'at': datetime.datetime.now().isoformat(timespec='minutes')}
            save_state(st)
            if not slug:   # 시험(--slug 지정)은 공유 기록에 남기지 않는다
                share_done(s, st['done'][s])
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
    ap.add_argument('--mode', choices=['draft', 'private', 'schedule'], default='draft')
    ap.add_argument('--at', help='예약 시간 "YYYY-MM-DD HH:MM"(없으면 다음 빈 주말 시간)')
    ap.add_argument('--slug')
    ap.add_argument('--keep-open', action='store_true')
    ap.add_argument('--mark-done', nargs='*', help='이미 직접 올린 글의 슬러그(자동 업로드 대상에서 뺌)')
    ap.add_argument('--list', action='store_true', help='다음에 올릴 순서 보기')
    ap.add_argument('--chrome', action='store_true', help='업로드용 크롬만 띄우기(처음 로그인할 때)')
    a = ap.parse_args()
    if a.chrome:
        ok = start_chrome()
        print('업로드용 크롬이 열렸어요. 그 창에서 티스토리에 직접 로그인해 두세요(창은 닫아도 로그인은 유지돼요).' if ok
              else '크롬을 띄우지 못했어요. 크롬이 설치되어 있는지 확인해 주세요.')
        sys.exit(0 if ok else 1)
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
    try:
        sys.exit(run(a.mode, a.slug, a.keep_open, a.at))
    except SystemExit:
        raise
    except Exception:
        import traceback
        log('오류로 멈췄어요:\n' + traceback.format_exc())
        input('이 창 내용을 캡처해서 보내 주세요. Enter를 누르면 닫혀요...')
        sys.exit(1)
