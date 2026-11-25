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
STATUS = ROOT / 'office' / 'status.json'          # PC마다 따로(저장소에 안 올라감)
EXAMPLE = ROOT / 'office' / 'status.example.json'
TEMPLATE = ROOT / 'office' / 'template.html'
OUT = ROOT / 'office' / 'index.html'
SERIES = ROOT / 'stock_beginner_series.json'
KST = timezone(timedelta(hours=9))
ROLES = ['planner', 'research', 'writer', 'designer', 'reviewer', 'deploy', 'uploader', 'human', 'auditor', 'naver']
THEMES = ['navy', 'forest', 'plum', 'charcoal']
KO = {'auditor': '구조검토', 'naver': '네이버', 'planner': '기획', 'research': '리서치', 'writer': '작가', 'designer': '디자이너', 'reviewer': '검수', 'deploy': '배포', 'uploader': '업로드', 'human': '주인님'}


def now():
    return datetime.now(KST).isoformat(timespec='seconds')


def load():
    try:
        return json.loads(STATUS.read_text(encoding='utf-8'))
    except Exception:   # 처음이거나 깨졌으면 기본 상태로 시작
        return json.loads(EXAMPLE.read_text(encoding='utf-8'))


def save(st):
    st['updated_at'] = now()
    STATUS.write_text(json.dumps(st, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def counts():
    d = json.loads(SERIES.read_text(encoding='utf-8'))
    items = d['items']
    pub = [i for i in items if i.get('status') == 'published']
    today = datetime.now(KST).strftime('%Y-%m-%d')
    made_today = sum(1 for i in items if str(i.get('made_at', '')).startswith(today))   # 모든 PC 공통(저장소 기록)
    new = [i for i in items if isinstance(i['id'], int) and i['id'] >= 194]
    waiting = [i for i in new if i.get('status') != 'published']
    last = items[-1]
    recent = [i.get('track') for i in items[-2:]]
    nxt = 'chart' if recent == ['life', 'life'] else 'life'   # 생활정보:차트 = 2:1
    return {
        'published': len(pub), 'total': len(items), 'made_today': made_today, 'waiting_upload': len(waiting),
        'last': {'id': last['id'], 'title': last['title'], 'track': last.get('track')},
        'next_track': nxt,
        'recent': [{'id': i['id'], 'title': i['title'], 'track': i.get('track'), 'status': i.get('status')}
                   for i in reversed(items[-6:])],
    }


HEAD = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        '<style>body{margin:0}</style></head><body>')


def render(st, standalone=True):
    """standalone=True: PC에서 바로 여는 완전한 문서. False: Artifact 게시용(뼈대는 게시할 때 붙음)."""
    html = TEMPLATE.read_text(encoding='utf-8')
    data = json.dumps(st, ensure_ascii=False).replace('</', '<\\/')
    html = html.replace('__OFFICE_DATA__', data)
    return HEAD + html + '</body></html>' if standalone else html


def build():
    st = load()
    st['counts'] = counts()
    OUT.write_text(render(st), encoding='utf-8')
    return str(OUT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--set', nargs=3, metavar=('ROLE', 'STATE', 'TASK'))
    ap.add_argument('--log', nargs=2, metavar=('ROLE', 'MSG'))
    ap.add_argument('--handoff', nargs=3, metavar=('FROM', 'TO', 'MSG'), help='FROM 완료 + TO 바로 시작(한 번에)')
    a = ap.parse_args()
    if a.set or a.log or a.handoff:
        st = load()
        if a.set:
            role, state, task = a.set
            assert role in ROLES and state in ('idle', 'working', 'done', 'blocked'), (role, state)
            st['members'][role] = {'state': state, 'task': task, 'at': now()}
            st['log'].insert(0, {'at': now(), 'who': role, 'msg': task})
        if a.handoff:
            fr, to, msg = a.handoff
            assert fr in ROLES and to in ROLES, (fr, to)
            st['members'][fr] = {'state': 'done', 'task': msg, 'at': now()}
            st['members'][to] = {'state': 'working', 'task': f'{msg} → 받아서 시작', 'at': now()}
            st['log'].insert(0, {'at': now(), 'who': fr, 'msg': f'{msg} → {KO[to]}에게 넘김'})
        if a.log:
            st['log'].insert(0, {'at': now(), 'who': a.log[0], 'msg': a.log[1]})
        st['log'] = st['log'][:80]
        save(st)
    print(build())


if __name__ == '__main__':
    main()
