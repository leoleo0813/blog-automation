"""이미 assets/thumbnails/에 있는 기존 벡터(폰트 텍스트) SVG 썸네일들을
일괄적으로 PNG로 래스터화해서 같은 파일명으로 덮어쓴다 (make_thumbnail.py의
_rasterize_to_png_bytes/_wrap_png_as_svg 로직 재사용).

한 번 실행하는 백필용 스크립트다 — 이미 <image href="data:image/png...">로
감싸진(이미 래스터화된) 파일은 건드리지 않고 건너뛴다.

    python -m blog_automation.rasterize_thumbnails
"""
from pathlib import Path

from blog_automation.make_thumbnail import _rasterize_to_png_bytes, _wrap_png_as_svg


def main():
    thumb_dir = Path('assets/thumbnails')
    changed, skipped, failed = [], [], []

    for svg_path in sorted(thumb_dir.glob('*.svg')):
        text = svg_path.read_text(encoding='utf-8')
        if 'data:image/png' in text:
            skipped.append(svg_path.name)
            continue

        png_bytes = _rasterize_to_png_bytes(text)
        if png_bytes is None:
            failed.append(svg_path.name)
            continue

        svg_path.write_text(_wrap_png_as_svg(png_bytes), encoding='utf-8')
        changed.append(svg_path.name)

    print(f"래스터화 완료: {len(changed)}개")
    for name in changed:
        print(f"  - {name}")
    if skipped:
        print(f"이미 래스터화되어 건너뜀: {len(skipped)}개")
    if failed:
        print(f"실패: {len(failed)}개")
        for name in failed:
            print(f"  - {name}")


if __name__ == '__main__':
    main()
