"""본문용 그림(그래프·도식) SVG를 PNG로 바꾼다.

2026-10-02 점검에서 1~107편 본문 이미지가 0장이었다. 티스토리에는 PNG를 올려야
하므로, 초안을 쓸 때 SVG로 그래프나 도식을 그리고 이 스크립트로 PNG를 만든다.
썸네일과 같은 헤드리스 Chromium 렌더러(make_thumbnail.py)를 쓴다.

    python -m blog_automation.make_figure assets/figures/<slug>-1.svg

SVG 루트에 width/height 속성이 있어야 한다(없으면 1200x800으로 본다). 결과는 같은
경로의 .png로 저장된다. 그래프 숫자는 출처에서 확인한 값만 쓴다 — 지어낸 수치로
그래프를 그리면 표보다 더 그럴듯하게 틀린다.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from blog_automation.make_thumbnail import _ensure_pillow, _find_chrome


def _size(svg_text):
    def attr(name, default):
        m = re.search(rf'<svg[^>]*\b{name}="(\d+)', svg_text)
        return int(m.group(1)) if m else default
    return attr('width', 1200), attr('height', 800)


def main():
    svg_path = Path(sys.argv[1])
    svg_text = svg_path.read_text(encoding='utf-8')
    width, height = _size(svg_text)

    chrome = _find_chrome()
    Image = _ensure_pillow()
    if not chrome or Image is None:
        print("Chromium 또는 Pillow 없음 - PNG 생성 실패", file=sys.stderr)
        sys.exit(1)

    png_path = svg_path.with_suffix('.png')
    with tempfile.TemporaryDirectory() as td:
        raw_png = Path(td) / 'raw.png'
        subprocess.run(
            [
                chrome, '--headless', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
                f'--window-size={width},{height + 300}', '--virtual-time-budget=3000',
                f'--screenshot={raw_png}', f'file://{svg_path.resolve()}',
            ],
            check=True, timeout=30, capture_output=True,
        )
        Image.open(raw_png).crop((0, 0, width, height)).save(png_path)
    print(png_path)


if __name__ == '__main__':
    main()
