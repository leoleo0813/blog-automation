"""AI 타워(팀원 사무실 화면) — 2026-11-20 사용자 요청 "AI 팀원 사무실 화면".

office/status.json(팀원 상태) + stock_beginner_series.json(글 수)을 읽어 office/index.html 한 장을 만든다.
TEAM.md의 각 역할은 일을 시작·끝낼 때 상태를 적는다.

    python -m blog_automation.office                       # 화면만 다시 만들기
    python -m blog_automation.office --set writer working "원고 3,500자 쓰는 중"
    python -m blog_automation.office --set reviewer done "lint OK, 숫자 대조 OK"
    python -m blog_automation.office --log uploader "비공개 발행 성공"

state: idle(대기) / working(일하는 중) / done(완료) / blocked(막힘)
"""
import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS = ROOT / 'office' / 'status.json'
TEMPLATE = ROOT / 'office' / 'template.html'
OUT = ROOT / 'office' / 'index.html'
SERIES = ROOT / 'stock_beginner_series.json'
KST = timezone(timedelta(hours=9))
ROLES = ['planner', 'research', 'writer', 'designer', 'reviewer', 'deploy', 'uploader', 'human']
THEMES = ['navy', 'forest', 'plum', 'charcoal']


def now():
    return datetime.now(KST).isoformat(timespec='seconds')


def load():
    return json.loads(STATUS.read_text(encoding='utf-8'))


def save(st):
    st['updated_at'] = now()
    STATUS.write_text(json.dumps(st, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def counts():
    d = json.loads(SERIES.read_text(encoding='utf-8'))
    items = d['items']
    pub = [i for i in items if i.get('status') == 'published']
    new = [i for i in items if isinstance(i['id'], int) and i['id'] >= 194]
    waiting = [i for i in new if i.get('status') != 'published']
    last = items[-1]
    recent = [i.get('track') for i in items[-2:]]
    nxt = 'chart' if recent == ['life', 'life'] else 'life'   # 생활정보:차트 = 2:1
    return {
        'published': len(pub), 'total': len(items), 'waiting_upload': len(waiting),
        'last': {'id': last['id'], 'title': last['title'], 'track': last.get('track')},
        'next_track': nxt,
        'recent': [{'id': i['id'], 'title': i['title'], 'track': i.get('track'), 'status': i.get('status')}
                   for i in reversed(items[-6:])],
    }


def build():
    st = load()
    st['counts'] = counts()
    html = TEMPLATE.read_text(encoding='utf-8')
    data = json.dumps(st, ensure_ascii=False).replace('</', '<\\/')
    OUT.write_text(html.replace('__OFFICE_DATA__', data), encoding='utf-8')
    return str(OUT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--set', nargs=3, metavar=('ROLE', 'STATE', 'TASK'))
    ap.add_argument('--log', nargs=2, metavar=('ROLE', 'MSG'))
    a = ap.parse_args()
    if a.set or a.log:
        st = load()
        if a.set:
            role, state, task = a.set
            assert role in ROLES and state in ('idle', 'working', 'done', 'blocked'), (role, state)
            st['members'][role] = {'state': state, 'task': task, 'at': now()}
            st['log'].insert(0, {'at': now(), 'who': role, 'msg': task})
        if a.log:
            st['log'].insert(0, {'at': now(), 'who': a.log[0], 'msg': a.log[1]})
        st['log'] = st['log'][:30]
        save(st)
    print(build())


if __name__ == '__main__':
    main()
