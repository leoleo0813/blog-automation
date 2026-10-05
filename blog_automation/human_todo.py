"""발행 보류(gate_pass:false) 초안마다 사용자가 할 일을 모아 저장소 맨 위 `사용자_할일.md`로 만든다.

2026-10-05 사용자 요청: "게이트 통과 실패했을 때 내가 해야 하는 추가자료를 구체적으로 적어 줘.
지금 상태론 무엇을 해야 할지 알 수 없다." — 할 일이 초안 front matter 깊숙이 긴 문단으로
묻혀 있었다. 이제 보류 초안은 front matter에 `user_todo`를 정해진 형식으로 적고(RULES.md
「보류 시 사용자 할 일」), 이 스크립트가 한 파일로 모은다. 검색량 큰 순으로 정렬한다.

    python -m blog_automation.human_todo        # 사용자_할일.md 다시 만들기

user_todo 형식(YAML):
    user_todo:
      why: 막힌 이유 한 줄(쉬운 말)
      steps: [클릭 단위 단계, ...]          # 각 단계에 링크 1개까지
      must_show: [캡처에 꼭 보여야 할 것, ...]
      minutes: 3                             # 예상 소요 시간(분)
      device: 휴대폰 가능 | PC 권장
      if_skipped: 안 하면 어떻게 되는지
"""
import datetime
import json
import re
from pathlib import Path

import yaml

OUT = Path('사용자_할일.md')
SERIES = Path('stock_beginner_series.json')


def _volume(fm):
    m = re.match(r'\s*([\d,]+)', str(fm.get('monthly_search_volume', '')))
    return int(m.group(1).replace(',', '')) if m else 0


def collect():
    series = json.loads(SERIES.read_text(encoding='utf-8'))['items']
    order = {i.get('slug'): i.get('order') for i in series}
    status = {i.get('slug'): i.get('status') for i in series}
    held, missing = [], []
    for path in sorted(Path('stock_drafts').glob('*.md')):
        fm = yaml.safe_load(path.read_text(encoding='utf-8').split('---', 2)[1]) or {}
        slug = fm.get('slug') or path.stem
        if fm.get('gate_pass') is not False or status.get(slug) == 'published':
            continue
        todo = fm.get('user_todo')
        item = dict(slug=slug, order=order.get(slug), title=fm.get('title', slug),
                    keyword=fm.get('keyword', ''), volume=_volume(fm), todo=todo)
        (held if isinstance(todo, dict) else missing).append(item)
    held.sort(key=lambda x: -x['volume'])
    return held, missing


def render(held, missing):
    today = datetime.date.today().isoformat()
    total = sum(int(h['todo'].get('minutes', 0) or 0) for h in held)
    L = [f'# 사용자 할 일 — 발행 보류 글에 필요한 자료',
         '',
         f'마지막 갱신: {today} · 보류 {len(held) + len(missing)}편 · 예상 합계 약 {total}분',
         '',
         '**보내는 법(공통):** 캡처한 사진을 Claude 대화창에 올리고 "N편 자료"라고만 적어 주세요.',
         '사진을 받으면 본문을 고치고 보류를 풀어 드립니다. 위에서부터(검색량 큰 순) 하면 효과가 큽니다.',
         '']
    for h in held:
        t = h['todo']
        num = f"{h['order']}편" if h['order'] else '번호 없음'
        L += [f"## [ ] {num} · {h['title']}",
              f"월 검색량 {h['volume']:,} · 약 {t.get('minutes', '?')}분 · {t.get('device', '')}".rstrip(' ·'),
              '',
              f"**왜 막혔나:** {t.get('why', '')}",
              '',
              '**할 일**']
        L += [f'{i}. {s}' for i, s in enumerate(t.get('steps', []), 1)]
        if t.get('must_show'):
            L += ['', '**캡처에 꼭 보여야 할 것**'] + [f'- {m}' for m in t['must_show']]
        if t.get('if_skipped'):
            L += ['', f"**안 하면:** {t['if_skipped']}"]
        L += ['', f"보낼 때: \"{num} 자료\"", '', '---', '']
    if missing:
        L += ['## 할 일 정리가 아직 안 된 보류 글', '']
        L += [f"- {m['order'] or ''}편 {m['title']} (`{m['slug']}`)" for m in missing]
        L.append('')
    if not held and not missing:
        L += ['지금 보류 중인 글이 없습니다.', '']
    return '\n'.join(L)


def main():
    held, missing = collect()
    OUT.write_text(render(held, missing), encoding='utf-8')
    print(f'{OUT}: 보류 {len(held)}편 정리, 할 일 미작성 {len(missing)}편')


if __name__ == '__main__':
    main()
