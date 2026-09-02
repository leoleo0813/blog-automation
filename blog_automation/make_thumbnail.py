"""뉴스 매거진 스타일의 한글 인포그래픽 카드 SVG 썸네일을 만들어 assets/thumbnails/에 저장한다.

    python -m blog_automation.make_thumbnail <slug> "<한글 제목/짧은 문구>" <배경hex> <포인트색hex> "<짧은 카테고리 태그>" ["<포인트1>" "<포인트2>" "<포인트3>"]

포인트(핵심 키워드, 최대 3개, 각 4~6자 이내)를 추가하면 하단 다크 티커 바에
번호가 매겨진 칩 형태로 표시되어 뉴스 그래픽 느낌이 강해진다. 포인트 없이
4개 인자만 넘기면 제목 카드만 나온다.

예:
    python -m blog_automation.make_thumbnail autumn-immunity-tips "환절기 면역력 지키는 법" 2f4f7f 4a90d9 "건강 팁" "체온관리" "수면" "비타민C"

만든 SVG 파일 경로를 표준출력에 찍는다 — 그 파일을 git add/commit/push 한 뒤,
아래 형태의 jsDelivr URL을 <img src>로 쓴다:

    https://cdn.jsdelivr.net/gh/leoleo0813/blog-automation@main/assets/thumbnails/<slug>.svg
"""
import sys
from pathlib import Path

FONT_STACK = "'Apple SD Gothic Neo','Malgun Gothic','Noto Sans KR',sans-serif"

BASE_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_light}"/>
      <stop offset="100%" stop-color="{bg_dark}"/>
    </linearGradient>
    <radialGradient id="vignette" cx="80%" cy="90%" r="75%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dotGrid" width="26" height="26" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="2" fill="{accent}"/>
    </pattern>
    <filter id="softShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="1200" height="630" fill="url(#bgGrad)"/>
  <polygon points="700,0 1200,0 1200,420" fill="{accent}" opacity="0.10"/>
  <rect x="840" y="50" width="300" height="230" fill="url(#dotGrid)" opacity="0.35"/>
  <rect width="1200" height="630" fill="url(#vignette)"/>

  <circle cx="106" cy="107" r="7" fill="{accent}" filter="url(#softShadow)"/>
  <rect x="122" y="80" width="{tag_width}" height="54" rx="27" fill="{accent}" filter="url(#softShadow)"/>
  <text x="152" y="116" font-family="{font}" font-size="28" font-weight="bold" fill="#ffffff">{tag}</text>
  <rect x="90" y="152" width="220" height="4" rx="2" fill="{accent}" opacity="0.85"/>

  {title_lines}
  {points_block}

  <rect x="24" y="24" width="1152" height="582" rx="26" fill="none" stroke="{accent}" stroke-width="4" opacity="0.55"/>
</svg>"""

TITLE_LINE = (
    '<text x="90" y="{y}" font-family="{font}" font-size="66" font-weight="bold" '
    'fill="#ffffff" filter="url(#softShadow)">{text}</text>'
)

TICKER_BAR = '<rect x="0" y="502" width="1200" height="128" fill="#0d1420" opacity="0.62"/>' \
             '<rect x="0" y="500" width="1200" height="4" fill="{accent}"/>'

HASHTAG = (
    '<text x="600" y="576" font-family="{font}" font-size="26" fill="#ffffff" '
    'opacity="0.55" text-anchor="middle">#{tag}</text>'
)

POINT_CHIP = (
    '<circle cx="{cx}" cy="{cy}" r="24" fill="{accent}" filter="url(#softShadow)"/>'
    '<text x="{cx}" y="{text_y}" font-family="{font}" font-size="22" font-weight="bold" '
    'fill="#ffffff" text-anchor="middle">{num}</text>'
    '<text x="{label_x}" y="{text_y}" font-family="{font}" font-size="27" font-weight="bold" '
    'fill="#ffffff">{label}</text>'
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
    """factor < 1 어둡게, factor > 1 밝게(흰색 쪽으로 보간)."""
    r, g, b = _hex_to_rgb(c)
    if factor <= 1:
        return _rgb_to_hex(r * factor, g * factor, b * factor)
    t = factor - 1
    return _rgb_to_hex(r + (255 - r) * t, g + (255 - g) * t, b + (255 - b) * t)


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


def _build_points_block(points, accent, tag):
    n = len(points)
    slot_width = 1020 / n
    items = []
    for i, label in enumerate(points):
        cx = 90 + slot_width * i + 28
        label_x = cx + 38
        items.append(POINT_CHIP.format(
            cx=cx, cy=566, text_y=574, num=i + 1, label=label,
            label_x=label_x, accent=accent, font=FONT_STACK,
        ))
    return TICKER_BAR.format(accent=accent) + '\n  ' + '\n  '.join(items)


def main():
    slug, title, bg, accent, tag = sys.argv[1:6]
    points = sys.argv[6:9]
    bg = _normalize_color(bg)
    accent = _normalize_color(accent)

    line1, line2 = _wrap_title(title)
    tag_width = len(tag) * 32 + 60

    if line2:
        title_lines = '\n  '.join([
            TITLE_LINE.format(y=290, font=FONT_STACK, text=line1),
            TITLE_LINE.format(y=370, font=FONT_STACK, text=line2),
        ])
    else:
        title_lines = TITLE_LINE.format(y=330, font=FONT_STACK, text=line1)

    if points:
        points_block = _build_points_block(points, accent, tag)
    else:
        points_block = TICKER_BAR.format(accent=accent) + '\n  ' + HASHTAG.format(font=FONT_STACK, tag=tag)

    svg = BASE_TEMPLATE.format(
        bg_light=_shade(bg, 1.18),
        bg_dark=_shade(bg, 0.55),
        accent=accent,
        font=FONT_STACK,
        tag=tag,
        tag_width=tag_width,
        title_lines=title_lines,
        points_block=points_block,
    )

    out_dir = Path('assets/thumbnails')
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}.svg"
    out_path.write_text(svg, encoding='utf-8')
    print(out_path)


if __name__ == '__main__':
    main()
