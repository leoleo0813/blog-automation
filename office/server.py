"""AI 타워 PC 서버 (Windows·Mac 공통) — 2026-11-20 사용자 요청 "7층 기획을 누르면 시작".

    python office/server.py          → 브라우저에 http://127.0.0.1:8765 이 열린다

- 7층 [기획 시작] → git pull → Claude Code(`claude -p`)가 office/PRODUCE.md 순서로 글 1편 제작
  → 끝나면 pc_uploader로 티스토리 비공개 발행(설정에서 끌 수 있음)
- 화면은 3초마다 office/status.json을 다시 읽어 층 불을 바꾼다.
- 하루 2편 제한, 다른 PC(Windows/Mac)가 제작 중이면 시작하지 않는다(저장소의 office/lock.json).
- 이 PC 밖에서는 접속할 수 없다(127.0.0.1만 연다).
"""
import json
import os
import platform
import shutil
import subprocess
import sys
import threading
import time
import webbrowser

try:   # Windows 검은 창에서 한글·기호가 깨지거나 멈추지 않게
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
CHILD_ENV = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
# Claude Code는 ANTHROPIC_API_KEY 등이 있으면 Pro 로그인보다 그걸 먼저 쓴다(쓴 만큼 요금·잘못된 키면 즉시 실패).
# 타워는 Pro 구독 로그인으로만 돌린다 → 제작용 환경에서는 빼고 실행.
CLAUDE_ENV = {k: v for k, v in CHILD_ENV.items()
              if k not in ('ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'CLAUDE_CODE_USE_BEDROCK', 'CLAUDE_CODE_USE_VERTEX')}
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from blog_automation import office  # noqa: E402

KST = timezone(timedelta(hours=9))
RUNS = ROOT / 'office' / 'runs'
LOCAL = ROOT / 'office' / 'local.json'      # 이 PC 설정(저장소에 안 올라감)
LOCK = ROOT / 'office' / 'lock.json'        # 여러 PC 공통 '제작 중' 표시(저장소에 올라감)
RESULT = ROOT / 'office' / 'result.json'
PORT = 8765
PORTS = [8765, 18765, 28765, 38765, 47865, 51765]   # Windows가 막아 둔 번호면 다음 번호로
MACHINE = platform.node() or platform.system()
DEFAULTS = {'auto_upload': True, 'daily_limit': 2, 'claude': ''}

job = {'proc': None, 'phase': 'idle', 'started': None, 'log': None, 'topic': ''}
lines = []   # 화면에 보여 줄 최근 진행 글


def cfg():
    c = dict(DEFAULTS)
    if LOCAL.exists():
        c.update(json.loads(LOCAL.read_text(encoding='utf-8')))
    return c


def now():
    return datetime.now(KST)


last_line = {'at': time.time()}


def say(msg):
    last_line['at'] = time.time()
    t = now().strftime('%H:%M:%S')
    lines.append(f'{t} {msg}')
    del lines[:-60]
    if job['log']:
        with open(job['log'], 'a', encoding='utf-8') as f:
            f.write(f'{t} {msg}\n')
    print(f'{t} {msg}', flush=True)


def kill_tree(p):
    """프로그램과 그 하위 프로그램(bash·python 등)을 함께 끈다."""
    try:
        if os.name == 'nt':
            subprocess.run(['taskkill', '/PID', str(p.pid), '/T', '/F'], capture_output=True)
        else:
            os.killpg(os.getpgid(p.pid), 15)
    except Exception:
        try:
            p.terminate()
        except Exception:
            pass


def popen_kw():
    """하위 프로그램을 한 묶음으로 띄워서 멈춤 때 한꺼번에 끌 수 있게."""
    return {'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == 'nt' else {'start_new_session': True}


def git(*a):
    return subprocess.run(['git', '-C', str(ROOT), *a], capture_output=True, text=True, encoding='utf-8', errors='replace')


def claude_bin():
    c = cfg().get('claude') or shutil.which('claude')
    if not c:
        for p in [Path.home() / '.local/bin/claude', Path.home() / '.claude/local/claude',
                  Path(os.environ.get('USERPROFILE', '')) / '.local/bin/claude.exe', Path(os.environ.get('APPDATA', '')) / 'npm/claude.cmd']:
            if p.is_file():
                return str(p)
    return c


def today_count():
    """오늘 만든 편 수 — 시리즈 JSON의 made_at(모든 PC 공통)과 이 PC 기록 중 큰 값."""
    st = office.load()
    d = now().strftime('%Y-%m-%d')
    local = sum(1 for r in st.get('runs', []) if r.get('date') == d and r.get('ok'))
    return max(local, office.counts().get('made_today', 0))


def other_lock():
    git('pull', '--rebase', '--autostash', '-q')
    if not LOCK.exists():
        return None
    lk = json.loads(LOCK.read_text(encoding='utf-8'))
    if not lk or lk.get('machine') == MACHINE:
        return None
    try:
        if now() - datetime.fromisoformat(lk['at']) > timedelta(hours=2):   # 2시간 넘은 표시는 끊긴 것으로 본다
            return None
    except Exception:
        return None
    return lk


def set_lock(on):
    LOCK.write_text(json.dumps({'machine': MACHINE, 'at': now().isoformat(timespec='seconds')} if on else {}, ensure_ascii=False) + '\n',
                    encoding='utf-8')
    git('add', str(LOCK))
    git('commit', '-q', '-m', f'AI 타워: {"제작 시작" if on else "제작 끝"} ({MACHINE})')
    r = git('push', '-q')
    if r.returncode != 0:
        git('pull', '--rebase', '--autostash', '-q')
        r = git('push', '-q')
    return r.returncode == 0


def record_run(ok, note):
    st = office.load()
    st.setdefault('runs', []).insert(0, {'date': now().strftime('%Y-%m-%d'), 'at': now().isoformat(timespec='seconds'),
                                         'machine': MACHINE, 'ok': ok, 'note': note})
    st['runs'] = st['runs'][:40]
    office.save(st)
    office.build()


def stream(proc):
    """claude --output-format stream-json 의 줄을 읽어 사람이 읽을 진행 글로 바꾼다."""
    final = ''
    for raw in proc.stdout:
        raw = raw.strip()
        if not raw:
            continue
        try:
            ev = json.loads(raw)
        except Exception:
            say(raw[:200])
            continue
        if ev.get('type') == 'assistant':
            for c in ev.get('message', {}).get('content', []):
                if c.get('type') == 'text' and c.get('text', '').strip():
                    say('💬 ' + c['text'].strip().replace('\n', ' ')[:220])
                elif c.get('type') == 'tool_use':
                    inp = c.get('input', {})
                    what = inp.get('command') or inp.get('file_path') or inp.get('query') or inp.get('url') or inp.get('pattern') or ''
                    say(f'🔧 {c.get("name")}: {str(what)[:160]}')
        elif ev.get('type') == 'result':
            final = ev.get('result') or ''
            say(f'결과: {"성공" if not ev.get("is_error") else "오류"} · {ev.get("num_turns", "?")}단계 · {round((ev.get("duration_ms") or 0) / 60000, 1)}분')
    return final


def run_upload():
    job['phase'] = 'upload'
    office_set('uploader', 'working', '티스토리 비공개 발행 중')
    say('업로드 시작: pc_uploader/tistory_upload.py --mode private')
    p = subprocess.Popen([sys.executable, str(ROOT / 'pc_uploader' / 'tistory_upload.py'), '--mode', 'private'],
                         cwd=str(ROOT / 'pc_uploader'), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         stdin=subprocess.DEVNULL, text=True, encoding='utf-8', errors='replace', env=CHILD_ENV, **popen_kw())
    job['proc'] = p
    for ln in p.stdout:
        if ln.strip():
            say('⬆ ' + ln.strip()[:200])
    p.wait()
    ok = p.returncode == 0
    office_set('uploader', 'done' if ok else 'blocked', '비공개 발행 완료 — 티스토리에서 확인 후 공개해 주세요' if ok else
               f'업로드 멈춤(코드 {p.returncode}) — pc_uploader/logs 확인')
    if ok:
        office_set('human', 'working', '비공개 글 확인 → 공개, 쓰레드 올리기, 네이버 직접 업로드')
    return ok


def office_set(role, state, task):
    st = office.load()
    st['members'][role] = {'state': state, 'task': task, 'at': now().isoformat(timespec='seconds')}
    st['log'].insert(0, {'at': now().isoformat(timespec='seconds'), 'who': role, 'msg': task})
    st['log'] = st['log'][:80]
    office.save(st)
    office.build()


def produce(topic):
    RUNS.mkdir(parents=True, exist_ok=True)
    job.update(stopped=False, phase='produce', started=now().isoformat(timespec='seconds'), topic=topic,
               log=str(RUNS / f'{now():%Y%m%d-%H%M%S}.log'))
    lines.clear()
    ok = False
    try:
        say(f'시작 ({MACHINE}) · 주제: {topic or "기획이 고름"}')
        r = git('pull', '--rebase', '--autostash')
        say('git pull: ' + (r.stdout.strip().splitlines() or ['완료'])[-1][:120])
        if not set_lock(True):
            say('⚠ 제작 중 표시를 저장소에 올리지 못했어요(인터넷·로그인 확인). 그래도 계속해요.')
        st = office.load()
        st['production'] = 'running'
        st['production_note'] = f'{MACHINE}에서 제작 중'
        for r_ in ('planner', 'research', 'writer', 'designer', 'reviewer', 'deploy', 'uploader'):
            st['members'][r_] = {'state': 'idle', 'task': '차례 기다리는 중', 'at': now().isoformat(timespec='seconds')}
        st['members']['planner'] = {'state': 'working', 'task': '시작 — 차례·후보 정하는 중', 'at': now().isoformat(timespec='seconds')}
        office.save(st)
        office.build()
        RESULT.unlink(missing_ok=True)
        prompt = ('office/PRODUCE.md 를 읽고 그 순서대로 글 1편을 만들어 줘. '
                  f'이번 주제: {topic if topic else "(비어 있음 — 기획이 차례대로 고름)"}. '
                  f'이 PC의 파이썬은 "{sys.executable}" 이다(python 명령이 안 되면 이것을 쓴다). '
                  f'stock_beginner_series.json 새 항목에 "made_at": "{now():%Y-%m-%d}"를 넣는다.')
        cmd = [claude_bin(), '-p', prompt, '--output-format', 'stream-json', '--verbose',
               '--allowedTools', 'Bash', 'Read', 'Write', 'Edit', 'MultiEdit', 'Glob', 'Grep', 'WebSearch', 'WebFetch', 'TodoWrite', 'Task', 'Agent']
        p = subprocess.Popen(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                             text=True, encoding='utf-8', errors='replace', env=CLAUDE_ENV if not cfg().get('keep_api_key') else CHILD_ENV, **popen_kw())
        job['proc'] = p
        final = stream(p)
        p.wait()
        git('pull', '--rebase', '--autostash', '-q')
        made = RESULT.exists()
        # 글이 저장소에 올라왔으면(result.json) 성공으로 본다 — Claude Code 종료 코드는 사소한 이유로 0이 아닐 때가 있다
        ok = made and not job.get('stopped')
        if made and p.returncode != 0:
            say(f'(Claude Code 종료 코드 {p.returncode} — 글은 만들어져서 업로드로 넘어가요)')
        if final:
            say('📋 ' + final.replace('\n', ' ')[:600])
        if 'login' in final.lower() or 'api key' in final.lower():
            say('⚠ Claude Code 로그인이 필요해요: 검은 창에서 claude → /login → "Claude account with subscription"(Pro) 선택')
        if job.get('stopped'):
            say('멈춤으로 이번 편은 중단했어요. 다시 시작하면 처음부터 만들어요.')
        elif not made:
            say('⚠ 글이 만들어지지 않았어요(office/result.json 없음). 위 진행 글과 사용자_할일.md를 확인해 주세요.')
        record_run(ok, json.loads(RESULT.read_text(encoding='utf-8')).get('title', '') if made else '제작 실패/보류')
        if ok and cfg().get('auto_upload'):
            run_upload()
        elif ok:
            say('자동 업로드가 꺼져 있어요(office/local.json). [업로드만 다시]로 올려 주세요.')
    except FileNotFoundError:
        say('⚠ Claude Code(claude)를 찾지 못했어요. 설치 안내(office/SETUP.md)를 따라 설치해 주세요.')
    except Exception as e:
        say(f'⚠ 오류: {e}')
    finally:
        st = office.load()
        for r_ in ('planner', 'research', 'writer', 'designer', 'reviewer', 'deploy'):   # 끝났는데 '일하는 중'으로 남은 층 정리
            if st['members'].get(r_, {}).get('state') == 'working':
                st['members'][r_] = {'state': 'done' if ok else 'blocked', 'task': '끝' if ok else '끝나지 않고 멈춤 — 조종석 기록 확인',
                                     'at': now().isoformat(timespec='seconds')}
        st['production'] = 'paused'
        st['production_note'] = '기획팀 방이나 [기획 시작]을 누르면 1편을 만들어요.'
        office.save(st)
        office.build()
        set_lock(False)
        job.update(proc=None, phase='idle')
        say('끝')


def status_payload():
    st = office.load()
    st['counts'] = office.counts()
    st['live'] = {'phase': job['phase'], 'started': job['started'], 'topic': job['topic'], 'lines': lines[-25:],
                  'machine': MACHINE, 'today': today_count(), 'limit': cfg()['daily_limit'],
                  'claude': bool(claude_bin()), 'auto_upload': cfg()['auto_upload'],
                  'quiet_sec': int(time.time() - last_line['at']) if job['phase'] != 'idle' else 0}
    if RESULT.exists():
        res = json.loads(RESULT.read_text(encoding='utf-8'))
        tp = ROOT / res.get('threads', '')
        res['threads_text'] = tp.read_text(encoding='utf-8') if tp.is_file() else ''
        st['result'] = res
    return st


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body, ctype='application/json; charset=utf-8'):
        b = body.encode('utf-8') if isinstance(body, str) else body
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path.startswith('/api/status'):
            return self.send(200, json.dumps(status_payload(), ensure_ascii=False))
        if self.path in ('/', '/index.html'):
            html = office.render(status_payload())
            return self.send(200, html, 'text/html; charset=utf-8')
        self.send(404, '{}')

    def do_POST(self):
        n = int(self.headers.get('Content-Length') or 0)
        try:
            body = json.loads(self.rfile.read(n) or b'{}')
        except Exception:
            body = {}
        if (self.headers.get('Host') or '').split(':')[0] not in ('127.0.0.1', 'localhost'):
            return self.send(403, '{}')
        if self.headers.get('Origin') not in (None, f'http://127.0.0.1:{PORT}', f'http://localhost:{PORT}'):  # PORT는 main()에서 실제 번호로 바뀜
            return self.send(403, '{"error":"다른 사이트에서 온 요청은 받지 않아요"}')
        if self.path == '/api/start':
            if job['phase'] != 'idle':
                return self.send(409, json.dumps({'error': '이미 일하는 중이에요'}, ensure_ascii=False))
            if not claude_bin():
                return self.send(400, json.dumps({'error': 'Claude Code가 설치되어 있지 않아요. office/SETUP.md를 봐 주세요.'}, ensure_ascii=False))
            if today_count() >= cfg()['daily_limit']:
                return self.send(429, json.dumps({'error': f'오늘은 이미 {cfg()["daily_limit"]}편을 만들었어요(하루 제한)'}, ensure_ascii=False))
            lk = other_lock()
            if lk:
                return self.send(409, json.dumps({'error': f'{lk["machine"]}에서 제작 중이에요({lk["at"][11:16]} 시작)'}, ensure_ascii=False))
            topic = str(body.get('topic') or '').strip()[:100]
            job['phase'] = 'produce'   # 스레드가 뜨기 전에 먼저 '일하는 중'으로(두 번 눌러도 한 판만)
            threading.Thread(target=produce, args=(topic,), daemon=True).start()
            return self.send(200, '{"ok":true}')
        if self.path == '/api/upload':
            if job['phase'] != 'idle':
                return self.send(409, json.dumps({'error': '이미 일하는 중이에요'}, ensure_ascii=False))
            job['phase'] = 'upload'
            def up():
                job['log'] = str(RUNS / f'{now():%Y%m%d-%H%M%S}-upload.log')
                RUNS.mkdir(parents=True, exist_ok=True)
                try:
                    run_upload()
                finally:
                    job.update(proc=None, phase='idle')
            threading.Thread(target=up, daemon=True).start()
            return self.send(200, '{"ok":true}')
        if self.path == '/api/stop':
            p = job.get('proc')
            if p and p.poll() is None:
                job['stopped'] = True
                say('사람이 멈춤을 눌렀어요.')
                kill_tree(p)
            return self.send(200, '{"ok":true}')
        self.send(404, '{}')


def main():
    office.build()
    global PORT
    import urllib.request
    srv = None
    for port in PORTS:
        try:   # 이미 켜진 타워가 있으면 그 화면만 연다
            with urllib.request.urlopen(f'http://127.0.0.1:{port}/api/status', timeout=1) as r:
                if b'members' in r.read(4000):
                    print(f'AI 타워가 이미 켜져 있어요: http://127.0.0.1:{port}')
                    webbrowser.open(f'http://127.0.0.1:{port}')
                    return
        except Exception:
            pass
        try:
            srv = ThreadingHTTPServer(('127.0.0.1', port), H)
            PORT = port
            break
        except OSError as e:
            print(f'{port}번은 쓸 수 없어요({e.__class__.__name__}) → 다음 번호로')
    if not srv:
        print('비어 있는 번호를 찾지 못했어요. PC를 다시 켠 뒤 시도해 주세요.')
        return
    url = f'http://127.0.0.1:{PORT}'
    print(f'AI 타워가 열렸어요: {url}  (이 창을 닫으면 타워도 꺼져요)')
    if '--no-browser' not in sys.argv:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
