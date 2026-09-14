"""주식 초안(stock_drafts/*.md)에 카카오톡 알림용 썸네일이 없으면 만든다.

assets/thumbnails/<slug>.png가 이미 있으면 아무 일도 하지 않는다. 없으면
make_thumbnail.py로 새로 만든다. .md가 아닌 파일(pending_posts/*.json, 일반
트렌드 모드)은 건너뛴다 — 썸네일 자동 첨부는 현재 주식 글에만 적용한다.

GitHub Actions 워크플로(.github/workflows/notify-repo-only.yml)에서 호출:
    python -m blog_automation.ensure_thumbnail <stock_drafts/*.md 경로>
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.notify_repo_only import _parse_front_matter

# 매번 같은 네이비+골드만 나온다는 피드백(2026-09-14)으로 팔레트를 여러 개 두고
# 편마다 돌아가며 쓴다. 전부 어두운 배경(흰 글자 대비 확보)에 채도 있는 포인트
# 색을 짝지어, "주식초보" 시리즈 톤은 유지하면서도 매번 같은 그림처럼 보이지
# 않게 했다.
BRAND_PALETTE = [
    ('1a2744', 'd4a017'),  # 네이비 + 골드 (기존 기본색)
    ('0f3d3e', 'ff6b4a'),  # 딥틸 + 코럴
    ('1f2937', '38bdf8'),  # 차콜 + 스카이블루
    ('2e1a47', 'f5a623'),  # 딥퍼플 + 앰버
    ('3d1a2b', 'e8a33d'),  # 버건디 + 골드오렌지
    ('14301f', '7ed957'),  # 포레스트그린 + 라임
    ('1b2a4a', 'ff8c42'),  # 슬레이트블루 + 오렌지
]
BRAND_TAG = '주식초보'


def _pick_palette():
    existing = len(list(Path('assets/thumbnails').glob('*.png')))
    return BRAND_PALETTE[existing % len(BRAND_PALETTE)]


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
    bg, accent = _pick_palette()

    subprocess.run(
        [
            sys.executable, '-m', 'blog_automation.make_thumbnail',
            slug, title, bg, accent, BRAND_TAG, *points,
        ],
        check=True,
    )


if __name__ == '__main__':
    main()
