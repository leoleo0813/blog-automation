"""심플한 플랫 에디토리얼 스타일 SVG 썸네일을 만들어 assets/thumbnails/에 저장한다.

    python -m blog_automation.make_thumbnail <slug> "<한글 제목/짧은 문구>" <배경hex> <포인트색hex> "<짧은 카테고리 태그>" ["<포인트1>" "<포인트2>" "<포인트3>"]

포인트(핵심 키워드, 최대 3개, 각 4~6자 이내)를 추가하면 하단 인덱스 바에
"01 키워드" 형태로 표시된다. 포인트 없이 4개 인자만 넘기면 제목 카드만 나온다.

의도적으로 그라디언트/드롭섀도우/카드 테두리 같은 전형적인 "AI 생성 SaaS
카드" 느낌의 장식은 배제했다 — 평평한 단색 배경 + 굵은 타이틀 + 얇은 액센트
라인 위주의, 실제 에디터가 손으로 만든 것 같은 담백한 구성이 목표다.

예:
    python -m blog_automation.make_thumbnail autumn-immunity-tips "환절기 면역력 지키는 법" 2f4f7f 4a90d9 "건강 팁" "체온관리" "수면" "비타민C"

만든 SVG 파일 경로를 표준출력에 찍는다 — 그 파일을 git add/commit/push 한 뒤,
아래 형태의 jsDelivr URL을 <img src>로 쓴다:

    https://cdn.jsdelivr.net/gh/leoleo0813/blog-automation@main/assets/thumbnails/<slug>.svg

내부적으로는: 텍스트가 포함된 벡터 SVG를 만든 뒤, 이 샌드박스에 있는
헤드리스 Chromium으로 한 번 렌더링해서 PNG로 구운(rasterize) 다음, 그
PNG를 다시 <svg><image href="data:image/png;base64,...">로 감싸서 같은
.svg 파일명으로 저장한다. 이렇게 하면 파일명/URL은 그대로인데, 텍스트가
더 이상 폰트가 아니라 픽셀이라서 뷰어(블로그 방문자의 브라우저)에 한글
폰트가 없어도 안 깨진다 — 실제로 <img>로 삽입된 SVG는 브라우저가 시스템
폰트 대체(fallback)를 제대로 안 해줘서 한글이 네모(tofu)로 깨지는 경우가
흔하다. Chromium/Pillow를 못 찾거나 렌더링이 실패하면 원래의 벡터 SVG를
그대로 저장한다(항상 무언가는 만들어지도록 하는 안전장치).
"""
import base64
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FONT_STACK = "'Apple SD Gothic Neo','Malgun Gothic','Noto Sans KR',sans-serif"

BASE_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="{bg}"/>
  <rect x="0" y="0" width="14" height="630" fill="{accent}"/>

  <rect x="90" y="86" width="{tag_width}" height="44" fill="{accent}"/>
  <text x="112" y="115" font-family="{font}" font-size="24" font-weight="bold" fill="#ffffff">{tag}</text>
  <rect x="90" y="148" width="150" height="3" fill="{accent}"/>

  {title_lines}
  {bottom_block}
</svg>"""

TITLE_LINE = (
    '<text x="90" y="{y}" font-family="{font}" font-size="64" font-weight="bold" fill="#ffffff">{text}</text>'
)

BOTTOM_BAR = '<rect x="0" y="520" width="1200" height="110" fill="{bar_fill}"/>'

DIVIDER = '<rect x="{x}" y="550" width="2" height="30" fill="#ffffff" opacity="0.3"/>'

POINT_ITEM = (
    '<text x="{x}" y="582" font-family="{font}" font-size="24" font-weight="bold" fill="{accent}">{num}</text>'
    '<text x="{label_x}" y="582" font-family="{font}" font-size="26" fill="#ffffff">{label}</text>'
)

TAGLINE = (
    '<text x="90" y="582" font-family="{font}" font-size="24" fill="#ffffff" opacity="0.75">{tag} 더 알아보기</text>'
)


def _normalize_color(c):
    return c if c.startswith('#') else f"#{c}"


def _hex_to_rgb(c):
    c = c.lstrip('#')
    return int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)


def _rgb_to_hex(r, g, b):
    r, g, b = (max(0, min(255, int(v))) for v in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def _shade(c, factor):
    r, g, b = _hex_to_rgb(c)
    return _rgb_to_hex(r * factor, g * factor, b * factor)


def _wrap_title(title, max_chars=13):
    title = title.strip()
    if ' ' in title:
        words = title.split(' ')
        line1, line2 = [], []
        length = 0
        target = line1
        for w in words:
            if target is line1 and length + len(w) > max_chars and line1:
                target = line2
                length = 0
            target.append(w)
            length += len(w) + 1
        return ' '.join(line1), ' '.join(line2)
    return title[:max_chars], title[max_chars:max_chars * 2]


def _build_points_block(points, accent, bg):
    n = len(points)
    slot_width = 1020 / n
    items = []
    dividers = []
    for i, label in enumerate(points):
        x = 90 + slot_width * i
        label_x = x + 42
        items.append(POINT_ITEM.format(
            x=x, label_x=label_x, num=f"{i + 1:02d}", label=label, accent=accent, font=FONT_STACK,
        ))
        if i > 0:
            dividers.append(DIVIDER.format(x=x - 30))
    bar = BOTTOM_BAR.format(bar_fill=_shade(bg, 0.62))
    return bar + '\n  ' + '\n  '.join(dividers + items)


def _find_chrome():
    import os
    browsers_path = os.environ.get('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
    for candidate in sorted(Path(browsers_path).glob('chromium-*/chrome-linux/chrome'), reverse=True):
        if candidate.is_file():
            return str(candidate)
    for name in ('chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable'):
        found = shutil.which(name)
        if found:
            return found
    return None


def _ensure_pillow():
    try:
        from PIL import Image
        return Image
    except ImportError:
        pass
    try:
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '--quiet', 'pillow'],
            check=True, timeout=60, capture_output=True,
        )
        from PIL import Image
        return Image
    except Exception:
        return None


def _rasterize_to_png_bytes(svg_text):
    """svg_text를 헤드리스 Chromium으로 렌더링해 1200x630 PNG 바이트로 반환한다.
    Chromium/Pillow를 못 찾거나 렌더링이 실패하면 None을 반환한다."""
    chrome = _find_chrome()
    if not chrome:
        return None
    Image = _ensure_pillow()
    if Image is None:
        return None

    with tempfile.TemporaryDirectory() as td:
        svg_path = Path(td) / 'thumb.svg'
        svg_path.write_text(svg_text, encoding='utf-8')
        raw_png = Path(td) / 'raw.png'
        try:
            subprocess.run(
                [
                    chrome, '--headless', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
                    '--window-size=1200,900', '--virtual-time-budget=3000',
                    f'--screenshot={raw_png}', f'file://{svg_path}',
                ],
                check=True, timeout=30, capture_output=True,
            )
            cropped = Path(td) / 'cropped.png'
            Image.open(raw_png).crop((0, 0, 1200, 630)).save(cropped)
            return cropped.read_bytes()
        except Exception:
            return None


def _wrap_png_as_svg(png_bytes):
    b64 = base64.b64encode(png_bytes).decode('ascii')
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">'
        f'<image href="data:image/png;base64,{b64}" width="1200" height="630"/>'
        '</svg>'
    )


def main():
    slug, title, bg, accent, tag = sys.argv[1:6]
    points = sys.argv[6:9]
    bg = _normalize_color(bg)
    accent = _normalize_color(accent)

    line1, line2 = _wrap_title(title)
    tag_width = len(tag) * 30 + 44

    if line2:
        title_lines = '\n  '.join([
            TITLE_LINE.format(y=280, font=FONT_STACK, text=line1),
            TITLE_LINE.format(y=356, font=FONT_STACK, text=line2),
        ])
    else:
        title_lines = TITLE_LINE.format(y=320, font=FONT_STACK, text=line1)

    if points:
        bottom_block = _build_points_block(points, accent, bg)
    else:
        bottom_block = BOTTOM_BAR.format(bar_fill=_shade(bg, 0.62)) + '\n  ' + TAGLINE.format(font=FONT_STACK, tag=tag)

    svg = BASE_TEMPLATE.format(
        bg=bg,
        accent=accent,
        font=FONT_STACK,
        tag=tag,
        tag_width=tag_width,
        title_lines=title_lines,
        bottom_block=bottom_block,
    )

    png_bytes = _rasterize_to_png_bytes(svg)
    final_content = _wrap_png_as_svg(png_bytes) if png_bytes else svg

    out_dir = Path('assets/thumbnails')
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}.svg"
    out_path.write_text(final_content, encoding='utf-8')
    print(out_path)
    if png_bytes:
        png_path = out_dir / f"{slug}.png"
        png_path.write_bytes(png_bytes)
        print(png_path)
    else:
        print("(참고: 래스터화 실패 — 폰트 기반 벡터 SVG로 저장됨. 뷰어 환경에 한글 폰트가 없으면 깨질 수 있음)", file=sys.stderr)


if __name__ == '__main__':
    main()
