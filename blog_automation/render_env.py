"""그림 렌더 환경을 Windows·Mac·리눅스(클라우드)에서 똑같이 맞춘다. 2026-11-20 'AI 타워를 PC로' 요청.

- find_chrome(): 리눅스 Playwright Chromium → Mac/Windows 크롬 → PATH 순서로 찾는다.
- prepare_svg(svg_text): Mac·Windows에는 Noto CJK 글꼴이 없으므로 저장소 글꼴을 @font-face로 직접 끼워 넣는다.
  (리눅스는 시스템 글꼴을 그대로 써서 기존 결과와 같게 둔다.)
- chrome_shot(...): 헤드리스 크롬으로 SVG → PNG. 임시 프로필을 써서 평소 크롬과 부딪히지 않는다.
- ffmpeg(): PATH의 ffmpeg, 없으면 pip의 imageio-ffmpeg 실행 파일.

처음 한 번:  python -m blog_automation.render_env --setup   (Noto 한글 글꼴 내려받기 + 점검)
"""
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / 'assets' / 'fonts'
NOTO_DIR = FONT_DIR / 'noto'          # .gitignore (용량이 커서 저장소에 올리지 않음)
SYSTEM = platform.system()             # 'Windows' / 'Darwin' / 'Linux'

GF = 'https://github.com/google/fonts/raw/main/ofl/'
NOTO = {   # 파일 이름: 내려받을 주소
    'NotoSansKR.ttf': GF + 'notosanskr/NotoSansKR%5Bwght%5D.ttf',
    'NotoSerifKR.ttf': GF + 'notoserifkr/NotoSerifKR%5Bwght%5D.ttf',
    'GowunDodum-Regular.ttf': GF + 'gowundodum/GowunDodum-Regular.ttf',
}
# SVG가 부르는 글꼴 이름 → 파일
FACES = [
    ('Noto Sans CJK KR', NOTO_DIR / 'NotoSansKR.ttf'),
    ('Noto Sans KR', NOTO_DIR / 'NotoSansKR.ttf'),
    ('Noto Serif CJK KR', NOTO_DIR / 'NotoSerifKR.ttf'),
    ('Noto Serif KR', NOTO_DIR / 'NotoSerifKR.ttf'),
    ('Gowun Dodum', NOTO_DIR / 'GowunDodum-Regular.ttf'),
    ('Black Han Sans', FONT_DIR / 'BlackHanSans-Regular.ttf'),
    ('Do Hyeon', FONT_DIR / 'DoHyeon-Regular.ttf'),
    ('Gaegu', FONT_DIR / 'Gaegu-Bold.ttf'),
    ('Jua', FONT_DIR / 'Jua-Regular.ttf'),
]


def find_chrome():
    pw = os.environ.get('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
    for c in sorted(Path(pw).glob('chromium-*/chrome-linux*/chrome'), reverse=True):
        if c.is_file():
            return str(c)
    cands = []
    if SYSTEM == 'Darwin':
        cands = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                 str(Path.home() / 'Applications/Google Chrome.app/Contents/MacOS/Google Chrome'),
                 '/Applications/Chromium.app/Contents/MacOS/Chromium']
    elif SYSTEM == 'Windows':
        for base in (os.environ.get('PROGRAMFILES', r'C:\Program Files'), os.environ.get('PROGRAMFILES(X86)', r'C:\Program Files (x86)'),
                     os.environ.get('LOCALAPPDATA', '')):
            cands.append(str(Path(base) / 'Google/Chrome/Application/chrome.exe'))
        cands.append(str(Path(os.environ.get('PROGRAMFILES(X86)', r'C:\Program Files (x86)')) / 'Microsoft/Edge/Application/msedge.exe'))
    for c in cands:
        if Path(c).is_file():
            return c
    for name in ('chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable', 'chrome'):
        f = shutil.which(name)
        if f:
            return f
    return None


def font_css():
    rules = []
    for fam, path in FACES:
        if path.exists():
            rules.append(f"@font-face{{font-family:'{fam}';src:url('{path.resolve().as_uri()}');font-weight:100 900;}}")
    return ''.join(rules)


def prepare_svg(svg_text):
    """리눅스가 아니면 <svg ...> 바로 뒤에 @font-face <style>을 넣는다."""
    if SYSTEM == 'Linux':
        return svg_text
    css = font_css()
    if not css:
        return svg_text
    i = svg_text.find('>', svg_text.find('<svg'))
    return svg_text[:i + 1] + f'<style>{css}</style>' + svg_text[i + 1:]


def chrome_shot(chrome, svg_path, raw_png, width, height):
    svg_path = Path(svg_path)
    if SYSTEM == 'Linux':   # 클라우드: 예전과 똑같은 명령(결과 동일)
        subprocess.run([chrome, '--headless', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
                        f'--window-size={width},{height + 300}', '--virtual-time-budget=3000',
                        f'--screenshot={raw_png}', f'file://{svg_path.resolve()}'],
                       check=True, timeout=30, capture_output=True)
        return
    # Mac·Windows: Playwright로 설치된 크롬을 띄워 글꼴이 다 읽힌 뒤 찍는다(업로더와 같은 도구).
    from playwright.sync_api import sync_playwright
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / 'page.svg'
        src.write_text(prepare_svg(svg_path.read_text(encoding='utf-8')), encoding='utf-8')
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=chrome, headless=True)
            pg = b.new_page(viewport={'width': width, 'height': height + 300}, device_scale_factor=1)
            pg.goto(src.resolve().as_uri())
            pg.evaluate('document.fonts.ready.then(() => true)')
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(raw_png))
            b.close()


def ffmpeg():
    f = shutil.which('ffmpeg')
    if f:
        return f
    try:
        import imageio_ffmpeg
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', 'imageio-ffmpeg'], check=True)
        import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def setup():
    NOTO_DIR.mkdir(parents=True, exist_ok=True)
    for name, url in NOTO.items():
        p = NOTO_DIR / name
        if p.exists() and p.stat().st_size > 10000:
            print(f'글꼴 있음: {name}')
            continue
        print(f'글꼴 내려받는 중: {name} ...')
        urllib.request.urlretrieve(url, p)
    ok = True
    c = find_chrome()
    print('크롬:', c or '못 찾음 — 크롬을 설치해 주세요'); ok &= bool(c)
    try:
        print('ffmpeg:', ffmpeg())
    except Exception as e:
        print('ffmpeg 준비 실패:', e); ok = False
    try:
        import PIL  # noqa
        print('Pillow: 있음')
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', 'pillow'])
        print('Pillow: 설치함')
    # 시험 렌더
    if c:
        test = ROOT / 'office' / 'runs' / 'render-test.svg'
        test.parent.mkdir(parents=True, exist_ok=True)
        test.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200"><rect width="600" height="200" fill="#fbf8f1"/>'
                        '<text x="30" y="90" font-family="Noto Serif CJK KR" font-size="48" font-weight="900">한글 명조 테스트</text>'
                        '<text x="30" y="160" font-family="Noto Sans CJK KR" font-size="40" font-weight="700">고딕 123,456원</text></svg>',
                        encoding='utf-8')
        r = subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(test)], capture_output=True, text=True)
        print('시험 그림:', test.with_suffix('.png') if r.returncode == 0 else ('실패 ' + r.stderr[-300:]))
        ok &= r.returncode == 0
    print('준비 완료' if ok else '준비 덜 됨 — 위 메시지를 Claude에게 보내 주세요')
    return ok


if __name__ == '__main__':
    if '--setup' in sys.argv:
        sys.exit(0 if setup() else 1)
    print(find_chrome())
