"""주제에 어울리는 그라데이션 SVG 썸네일을 만들어 assets/thumbnails/에 저장한다.

    python -m blog_automation.make_thumbnail <slug> "<영문 제목 2~5단어>" <hex색상1> <hex색상2> <이모지>

예:
    python -m blog_automation.make_thumbnail autumn-immunity-tips "Autumn Immunity Tips" "#4a7ab5" "#2f4f7f" "🍂"

색상은 #없이/있이 둘 다 가능하며 자동으로 '#'을 붙인다. 만든 SVG 파일 경로를 표준출력에 찍는다 —
그 파일을 git add/commit/push 한 뒤, 아래 형태의 raw GitHub URL을 <img src>로 쓴다:

    https://raw.githubusercontent.com/leoleo0813/blog-automation/main/assets/thumbnails/<slug>.svg
"""
import sys
from pathlib import Path

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}"/>
      <stop offset="100%" stop-color="{color2}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <circle cx="1060" cy="110" r="150" fill="#ffffff" opacity="0.08"/>
  <circle cx="90" cy="560" r="190" fill="#ffffff" opacity="0.08"/>
  <circle cx="1000" cy="540" r="60" fill="#ffffff" opacity="0.10"/>
  <text x="90" y="260" font-family="Arial, sans-serif" font-size="120">{emoji}</text>
  <text x="90" y="400" font-family="Arial, Helvetica, sans-serif" font-size="58" font-weight="bold" fill="#ffffff">{line1}</text>
  <text x="90" y="470" font-family="Arial, Helvetica, sans-serif" font-size="58" font-weight="bold" fill="#ffffff">{line2}</text>
  <rect x="90" y="520" width="110" height="8" rx="4" fill="#ffffff" opacity="0.85"/>
</svg>"""


def _normalize_color(c):
    return c if c.startswith('#') else f"#{c}"


def _wrap_title(title, max_chars=20):
    words = title.split()
    line1 = []
    line2 = []
    length = 0
    target = line1
    for w in words:
        if target is line1 and length + len(w) + 1 > max_chars and line1:
            target = line2
            length = 0
        target.append(w)
        length += len(w) + 1
    return ' '.join(line1), ' '.join(line2)


def main():
    slug, title, color1, color2, emoji = sys.argv[1:6]
    line1, line2 = _wrap_title(title)
    svg = TEMPLATE.format(
        color1=_normalize_color(color1),
        color2=_normalize_color(color2),
        emoji=emoji,
        line1=line1,
        line2=line2,
    )

    out_dir = Path('assets/thumbnails')
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}.svg"
    out_path.write_text(svg, encoding='utf-8')
    print(out_path)


if __name__ == '__main__':
    main()
