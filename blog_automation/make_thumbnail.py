"""심플한 한글 인포그래픽 카드 스타일 SVG 썸네일을 만들어 assets/thumbnails/에 저장한다.

    python -m blog_automation.make_thumbnail <slug> "<한글 제목/짧은 문구>" <배경hex> <포인트색hex> "<짧은 카테고리 태그>" ["<포인트1>" "<포인트2>" "<포인트3>"]

포인트(핵심 키워드, 최대 3개, 각 4~6자 이내)를 추가하면 하단에 번호가 매겨진
작은 항목들로 표시되어 인포그래픽 느낌이 강해진다. 포인트 없이 4개 인자만
넘기면 제목 카드만 나온다.

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
  <rect width="1200" height="630" fill="{bg}"/>
  <rect x="90" y="80" width="{tag_width}" height="54" rx="27" fill="{accent}"/>
  <text x="120" y="116" font-family="{font}" font-size="28" font-weight="bold" fill="#ffffff">{tag}</text>
  {title_lines}
  {points_block}
</svg>"""

TITLE_LINE = '<text x="90" y="{y}" font-family="{font}" font-size="64" font-weight="bold" fill="#ffffff">{text}</text>'

DIVIDER = '<rect x="90" y="{y}" width="1020" height="2" fill="#ffffff" opacity="0.25"/>'

UNDERLINE = '<rect x="90" y="{y}" width="140" height="10" rx="5" fill="{accent}"/>'

POINT_ITEM = """<circle cx="{cx}" cy="{cy}" r="22" fill="{accent}"/>
  <text x="{cx}" y="{text_y}" font-family="{font}" font-size="22" font-weight="bold" fill="#ffffff" text-anchor="middle">{num}</text>
  <text x="{label_x}" y="{text_y}" font-family="{font}" font-size="26" fill="#ffffff">{label}</text>"""


def _normalize_color(c):
    return c if c.startswith('#') else f"#{c}"


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


def _build_points_block(points, accent):
    n = len(points)
    slot_width = 1020 / n
    items = []
    for i, label in enumerate(points):
        cx = 90 + slot_width * i + 26
        label_x = cx + 34
        items.append(POINT_ITEM.format(
            cx=cx, cy=530, text_y=538, num=i + 1, label=label,
            label_x=label_x, accent=accent, font=FONT_STACK,
        ))
    return DIVIDER.format(y=470) + '\n  ' + '\n  '.join(items)


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
        points_block = _build_points_block(points, accent)
    else:
        points_block = UNDERLINE.format(y=430 if line2 else 390, accent=accent)

    svg = BASE_TEMPLATE.format(
        bg=bg,
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
