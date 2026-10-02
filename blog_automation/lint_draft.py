"""주식 초안(stock_drafts/*.md)이 독자 관점 필수 규칙을 지키는지 검사한다.

2026-10-02 1~107편 독자 관점 점검에서 규칙으로 적어 둔 것(이미지 최소 1장 등)이
97편 내내 지켜지지 않은 게 드러나, 사람 눈 대신 커밋 전에 기계로 막는다.
RULES.md 「★ 2026-10-02 독자 관점 점검 반영」의 항목과 1:1로 대응한다.

    python -m blog_automation.lint_draft stock_drafts/<slug>.md [...]
    python -m blog_automation.lint_draft --due     # refresh_due가 지난 발행 글 목록

FAIL이 하나라도 있으면 exit 1. WARN은 통과시키되 출력만 한다.
"""
import datetime
import json
import re
import sys
from pathlib import Path

import yaml

SERIES = Path('stock_beginner_series.json')
BLOG = 'https://sensitiveboss3.tistory.com/entry/'

# 독자에게 보이면 안 되는 작업용 표현(83·86·107편에서 실제로 노출됐다).
INTERNAL_WORDS = ['저장소', 'sources/', '초안', '게이트', 'gate_pass', 'self_check', '루틴']
DEFER_RE = re.compile(r'확인(하세요|해야 합니다|하셔야|하시기 바랍니다|해 보세요)')
MAX_DEFER = 2
MIN_INTERNAL_LINKS = 2


def _load_series():
    items = json.loads(SERIES.read_text(encoding='utf-8'))['items']
    return {it['slug']: it for it in items if it.get('slug')}


def _split(path):
    text = Path(path).read_text(encoding='utf-8')
    _, fm, body = text.split('---', 2)
    return yaml.safe_load(fm) or {}, body


def _visible(body):
    body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    return body


def lint(path, series):
    fails, warns = [], []
    fm, body = _split(path)
    html = _visible(body)
    text = re.sub(r'<[^>]+>', ' ', html)
    slug = fm.get('slug') or Path(path).stem

    for w in INTERNAL_WORDS:
        if w in text:
            fails.append(f"작업용 표현 노출: '{w}'")

    imgs = re.findall(r'<img[^>]*src="([^"]+)"', html)
    if not imgs:
        fails.append("본문 이미지 0장 (썸네일 제외 최소 1장)")
    for src in imgs:
        if src.startswith('assets/') and not Path(src).exists():
            fails.append(f"이미지 파일 없음: {src}")

    targets = re.findall(re.escape(BLOG) + r'([^"#?]+)', html)
    usable = 0
    for t in set(targets):
        if t == slug:
            continue
        it = series.get(t)
        if it is None:
            fails.append(f"없는 글로 가는 내부 링크: {t}")
        elif it.get('gate_pass') is False and it.get('status') != 'published':
            fails.append(f"발행 보류(gate_pass:false) 글로 가는 내부 링크: {t}")
        else:
            usable += 1
            if it.get('status') != 'published':
                warns.append(f"아직 발행 전인 글로 가는 링크(그 글을 먼저 발행할 것): {t}")
    if usable < MIN_INTERNAL_LINKS:
        fails.append(f"블로그 내부 링크 {usable}개 (최소 {MIN_INTERNAL_LINKS}개)")

    n_defer = len(DEFER_RE.findall(text))
    if n_defer > MAX_DEFER:
        fails.append(f"'확인하세요'류 {n_defer}회 (최대 {MAX_DEFER}회)")

    intro = re.sub(r'<[^>]+>', ' ', html.split('<h2', 1)[0])
    if '이 글은' in intro:
        fails.append("인트로에 '이 글은 ~' 메타 문장")

    due = fm.get('refresh_due')
    if due is not None and not isinstance(due, datetime.date):
        fails.append(f"refresh_due 형식 오류(YYYY-MM-DD): {due}")

    return fails, warns


def list_due(series):
    today = datetime.date.today()
    found = False
    for path in sorted(Path('stock_drafts').glob('*.md')):
        fm, _ = _split(path)
        due = fm.get('refresh_due')
        it = series.get(fm.get('slug') or path.stem, {})
        if isinstance(due, datetime.date) and due <= today and it.get('status') == 'published':
            found = True
            print(f"{it.get('order')}편 {path.stem}: refresh_due {due} — {fm.get('refresh_reason', '')}")
    if not found:
        print("갱신 기한이 지난 발행 글 없음")


def main():
    series = _load_series()
    if sys.argv[1:] == ['--due']:
        list_due(series)
        return
    failed = False
    for path in sys.argv[1:]:
        fails, warns = lint(path, series)
        print(f"== {path}: {'FAIL' if fails else 'OK'}")
        for f in fails:
            print(f"  FAIL {f}")
        for w in warns:
            print(f"  WARN {w}")
        failed = failed or bool(fails)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
