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
# 저장소가 공개라 본문 그림은 여기서 바로 불러온다(RULES.md 「이미지」).
RAW = 'https://raw.githubusercontent.com/leoleo0813/blog-automation/main/'

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

    # 글 번호("4편", "61편과")는 독자에게 보이지 않는 내부 번호다(2026-10-03 발행 글 18편에서 발견).
    nums = re.findall(r'\b\d{1,3}편', text)
    if nums:
        fails.append(f"내부 글 번호 노출 {len(nums)}개(예: {nums[0]}) — 글 제목으로 쓰고 링크를 건다")

    imgs = re.findall(r'<img[^>]*src="([^"]+)"', html)
    if not imgs:
        fails.append("본문 이미지 0장 (썸네일 제외 최소 1장)")
    for src in imgs:
        if src.startswith(RAW):
            local = src[len(RAW):]
            if not Path(local).exists():
                fails.append(f"이미지 파일 없음(같은 커밋으로 push할 것): {local}")
        elif not src.startswith('http'):
            fails.append(f"상대경로 이미지(티스토리에서 깨짐, GitHub 원본 주소로): {src}")

    # 그림 장수는 내용에 따라 1~3장(RULES.md 「이미지」). 숫자 표가 많은데 1장이면 이유를 적게 한다.
    if len(imgs) > 3:
        fails.append(f"본문 그림 {len(imgs)}장 (최대 3장)")
    num_tables = sum(1 for tb in re.findall(r'<table.*?</table>', html, re.S)
                     if len(re.findall(r'\d[\d,.]*\s*(%|원|조|만|억|년|월|일|배|달러)', tb)) >= 4)
    if len(imgs) == 1 and num_tables >= 3 and not fm.get('figure_plan'):
        fails.append(f"숫자 표 {num_tables}개인데 그림 1장 — 그림을 늘리거나 figure_plan에 1장으로 충분한 이유를 적을 것")

    # 금지 어휘가 소제목·박스 제목·FAQ 헤딩에 쓰였는지(RULES.md 2026-10-01 점검 반영)
    for head in re.findall(r'<(?:h2|summary|strong)[^>]*>(.*?)</(?:h2|summary|strong)>', html, re.S):
        h = re.sub(r'<[^>]+>', '', head)
        for w in ('걸리는', '막히는', '헷갈', '세 줄', '먼저 잡아 둘', '전망', '추천', '목표가', '급등', '대박'):
            if w in h and len(h) < 60:
                fails.append(f"제목·소제목 금지 어휘 '{w}': {h.strip()[:30]}")

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

    # 목차 항목은 전부 본문 H2로 이동하는 링크여야 한다(toc_anchors.py로 만든다).
    toc = re.search(r'<h2[^>]*>\s*목차\s*</h2>\s*<ol[^>]*>(.*?)</ol>', html, re.S)
    if toc:
        ids = set(re.findall(r'<h2[^>]*\bid="([^"]+)"', html))
        items = re.findall(r'<li[^>]*>(.*?)</li>', toc.group(1), re.S)
        unlinked = [re.sub(r'<[^>]+>', '', i).strip() for i in items
                    if not (m := re.search(r'<a href="#([^"]+)"', i)) or m.group(1) not in ids]
        if unlinked:
            fails.append(f"목차 링크 없음/대상 없음 {len(unlinked)}개(python -m blog_automation.toc_anchors 실행): {unlinked[:2]}")

    # 보류 초안은 사용자가 할 일을 정해진 형식으로 적어야 한다(RULES.md 「보류 시 사용자 할 일」).
    if fm.get('gate_pass') is False:
        todo = fm.get('user_todo')
        if not isinstance(todo, dict):
            fails.append("gate_pass:false인데 user_todo 없음 — 사용자가 할 일을 형식대로 적을 것")
        else:
            for key in ('why', 'steps', 'must_show', 'minutes', 'if_skipped'):
                if not todo.get(key):
                    fails.append(f"user_todo.{key} 비어 있음")
            if not any('http' in str(s) or '앱' in str(s) for s in todo.get('steps') or []):
                fails.append("user_todo.steps에 링크나 앱 경로가 하나도 없음 — 어디로 가야 하는지 적을 것")

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
