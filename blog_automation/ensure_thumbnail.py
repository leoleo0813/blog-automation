"""주식 초안(stock_drafts/*.md)에 카카오톡 알림용 썸네일이 없으면 만든다.

assets/thumbnails/<slug>.png가 이미 있으면 아무 일도 하지 않는다. 없으면
make_thumbnail.py로 새로 만든다(주식 시리즈 전체에 고정된 네이비+골드 배색으로
브랜드 통일감을 준다). .md가 아닌 파일(pending_posts/*.json, 일반 트렌드
모드)은 건너뛴다 — 썸네일 자동 첨부는 현재 주식 글에만 적용한다.

GitHub Actions 워크플로(.github/workflows/notify-repo-only.yml)에서 호출:
    python -m blog_automation.ensure_thumbnail <stock_drafts/*.md 경로>
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.notify_repo_only import _parse_front_matter

BRAND_BG = '1a2744'
BRAND_ACCENT = 'd4a017'
BRAND_TAG = '주식초보'


def main():
    path = sys.argv[1]
    if not path.endswith('.md'):
        print("주식 초안(.md)이 아님 - 썸네일 생략")
        return

    with open(path, encoding='utf-8') as f:
        fields = _parse_front_matter(f.read())

    slug = fields.get('slug')
    title = fields.get('title')
    if not slug or not title:
        print("front matter에 slug/title 없음 - 썸네일 생략")
        return

    png_path = Path('assets/thumbnails') / f"{slug}.png"
    if png_path.exists():
        print(f"이미 존재함 - 생략: {png_path}")
        return

    points = [p.strip()[:6] for p in fields.get('tags', '').split(',') if p.strip()][:3]

    subprocess.run(
        [
            sys.executable, '-m', 'blog_automation.make_thumbnail',
            slug, title, BRAND_BG, BRAND_ACCENT, BRAND_TAG, *points,
        ],
        check=True,
    )


if __name__ == '__main__':
    main()
