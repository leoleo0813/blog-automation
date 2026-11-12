"""네이버 전용 그림·카드 — 티스토리(pop_style·threads_carousel)와 완전히 다른 생김새. 2026-11-12 사용자 요청.

"문구만 다르고 캐릭터·글씨체·구조가 똑같아 보인다"는 피드백으로, 네이버용은 처음부터 다른 형식으로 그린다.
  - 캐릭터 없음. 모눈 공책 종이 + 빨간 여백선 + 형광펜 밑줄 + 점선 장부 + 손글씨 메모지.
  - 글씨체: 제목 Noto Serif CJK KR(굵은 명조), 본문 Noto Sans CJK KR, 메모 Gaegu(손글씨).
  - 크기: 정사각형 1080x1080(카드·그림 모두). 영상은 naver_pack.make_video(card_dir=...)가 세로로 감싼다.

    from blog_automation.naver_style import make_cards, figure
    make_cards(slug, cards, out_dir, tag='기초연금 노트')   # <slug>-01.png ...
    figure(path_png, kind, **kw)                            # 본문 그림 한 장

카드 kind:
  cover  : title(줄 목록), sub, note(메모지 줄 목록)
  ledger : title, rows[(이름, 값, 강조여부)], note
  big    : title, big(큰 숫자), formula(계산식 한 줄), rows(선택), note
  check  : title, items[(굵은 글, 작은 글)], note
  end    : title, items(줄 목록), note
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.make_illustrated_thumbnail import _install_fonts, _esc

W = H = 1080
PAPER, GRID, MARGIN = '#fbf8f1', '#e7e2d6', '#e8a0a0'
INK, SOFT, GREEN = '#1f1f1f', '#5b5b5b', '#0a7d48'
MARK = '#c9f2a8'          # 형광펜(연두)
MARK2 = '#ffe58a'         # 형광펜(노랑)
NOTE = '#fff3a8'
SERIF, SANS, HAND = 'Noto Serif CJK KR', 'Noto Sans CJK KR', 'Gaegu'


def _t(x, y, text, size, fill=INK, font=SANS, weight=400, anchor='start', extra=''):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{_esc(text)}</text>')


def _w(text, size):
    """대략적인 글자 폭(한글 1, 숫자·기호 0.6)."""
    return sum(size * (0.58 if ord(ch) < 128 else 1.0) for ch in str(text))


def _paper(tag, page=''):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
    for y in range(60, H, 40):
        s.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{GRID}" stroke-width="1.5"/>')
    for x in range(40, W, 40):
        s.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{GRID}" stroke-width="1" opacity="0.55"/>')
    s.append(f'<line x1="104" y1="0" x2="104" y2="{H}" stroke="{MARGIN}" stroke-width="3"/>')
    # 위쪽 띠: 작은 태그 + 쪽수
    s.append(f'<rect x="140" y="56" width="{_w(tag, 26) + 44:.0f}" height="46" rx="4" fill="{INK}"/>')
    s.append(_t(162, 88, tag, 26, '#ffffff', SANS, 700))
    if page:
        s.append(_t(W - 70, 90, page, 30, SOFT, SERIF, 700, 'end'))
    return s


def _title(lines, y=210, size=70, mark_last=True):
    s = []
    for k, ln in enumerate(lines):
        yy = y + k * (size + 22)
        if mark_last and k == len(lines) - 1:
            w = _w(ln, size)
            s.append(f'<path d="M136 {yy + 8} q {w / 2:.0f} -10 {w + 16:.0f} -4 l 0 -30 q {-w / 2:.0f} -8 {-w - 16:.0f} 2 z" '
                     f'fill="{MARK}" opacity="0.95"/>')
        s.append(_t(140, yy, ln, size, INK, SERIF, 900))
    return s, y + (len(lines) - 1) * (size + 22)


def _ledger(rows, y, gap=96):
    """점선 장부: 이름 ........ 값"""
    s = []
    for k, (name, val, hot) in enumerate(rows):
        yy = y + k * gap
        vs = 46 if hot else 40
        vw = _w(val, vs)
        nw = _w(name, 36)
        if hot:
            s.append(f'<rect x="{W - 90 - vw - 14:.0f}" y="{yy - 40}" width="{vw + 28:.0f}" height="54" rx="6" fill="{MARK2}" '
                     f'transform="rotate(-1.2 {W - 90 - vw / 2:.0f} {yy - 12})"/>')
        s.append(_t(140, yy, name, 36, INK, SANS, 500))
        s.append(f'<line x1="{140 + nw + 18:.0f}" y1="{yy - 8}" x2="{W - 90 - vw - 22:.0f}" y2="{yy - 8}" '
                 f'stroke="#9a9a9a" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>')
        s.append(_t(W - 90, yy, val, vs, GREEN if hot else INK, SERIF, 900, 'end'))
    return s


def _note(lines, x=600, y=830, rot=-3, w=380):
    if not lines:
        return []
    h = 54 + 50 * len(lines)
    s = [f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})">',
         f'<rect x="{x + 8}" y="{y + 10}" width="{w}" height="{h}" fill="#000" opacity="0.08"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{NOTE}"/>',
         f'<rect x="{x + w / 2 - 60}" y="{y - 16}" width="120" height="34" fill="#d9d2c0" opacity="0.85"/>']
    for k, ln in enumerate(lines):
        s.append(_t(x + 30, y + 62 + k * 50, ln, 40, '#3a3a3a', HAND, 700))
    s.append('</g>')
    return s


def _foot(text):
    return [_t(140, H - 50, text, 24, '#8d8d8d', SANS, 400)]


def card_svg(c, i, n, tag):
    s = _paper(tag, f'{i:02d} / {n:02d}')
    k = c['kind']
    if k == 'cover':
        t, yb = _title(c['title'], 330, 92)
        s += t
        if c.get('sub'):
            s.append(_t(140, yb + 90, c['sub'], 38, SOFT, SANS, 500))
        s += _note(c.get('note'), 560, 760, -4, 400)
        s.append(_t(140, H - 60, '넘겨서 보기 →', 30, GREEN, SANS, 700))
    elif k == 'ledger':
        t, yb = _title(c['title'])
        s += t
        s += _ledger(c['rows'], yb + 140)
        s += _note(c.get('note'), 600, 800, -3, 380)
    elif k == 'big':
        t, yb = _title(c['title'])
        s += t
        cy = yb + 230
        bw = _w(c['big'], 120)
        s.append(f'<ellipse cx="{180 + bw / 2:.0f}" cy="{cy - 42}" rx="{bw / 2 + 34:.0f}" ry="82" fill="none" '
                 f'stroke="#e0523f" stroke-width="5" transform="rotate(-3 {180 + bw / 2:.0f} {cy - 42})"/>')
        s.append(_t(180, cy, c['big'], 120, INK, SERIF, 900))
        s.append(_t(150, cy + 110, c['formula'], 36, SOFT, SANS, 500))
        if c.get('rows'):
            s += _ledger(c['rows'], cy + 220, 84)
        s += _note(c.get('note'), 620, 850, 3, 360)
    elif k == 'check':
        t, yb = _title(c['title'])
        s += t
        for j, (b, small) in enumerate(c['items']):
            yy = yb + 150 + j * 150
            s.append(f'<rect x="140" y="{yy - 44}" width="52" height="52" rx="6" fill="#fff" stroke="{INK}" stroke-width="4"/>')
            s.append(f'<path d="M150 {yy - 20} l 14 16 l 30 -40" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/>')
            s.append(_t(220, yy, b, 42, INK, SANS, 700))
            if small:
                s.append(_t(220, yy + 52, small, 32, SOFT, SANS, 400))
        s += _note(c.get('note'), 620, 840, -2, 360)
    elif k == 'end':
        t, yb = _title(c['title'], 260, 76)
        s += t
        for j, ln in enumerate(c['items']):
            s.append(_t(140, yb + 140 + j * 70, '— ' + ln, 38, INK, SANS, 500))
        s += _note(c.get('note'), 560, 780, -3, 400)
    s.append('</svg>')
    return '\n'.join(s)


def _render(svg_text, png_path):
    _install_fonts()
    p = Path(png_path).with_suffix('.svg')
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(svg_text, encoding='utf-8')
    subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(p)], check=True, capture_output=True)
    p.unlink()
    return str(p.with_suffix('.png'))


def make_cards(slug, cards, out_dir, tag='생활 노트'):
    return [_render(card_svg(c, i, len(cards), tag), Path(out_dir) / f'{slug}-{i:02d}.png')
            for i, c in enumerate(cards, 1)]


def figure(png_path, kind, title, tag='생활 노트', source='', **kw):
    """본문 그림. kind: 'bars'(items[(이름, 값, 표시글)]) / 'ledger'(rows, formula) / 'timeline'(steps[(때, 할 일)], note)"""
    s = _paper(tag)
    t, yb = _title(title if isinstance(title, list) else [title], 200, 62)
    s += t
    if kind == 'bars':
        items = kw['items']
        vmax = max(v for _, v, _ in items)
        for j, (name, v, lab) in enumerate(items):
            yy = yb + 150 + j * 170
            s.append(_t(140, yy, name, 36, INK, SANS, 700))
            ln = 700 * v / vmax
            s.append(f'<path d="M140 {yy + 30} q {ln / 2:.0f} -8 {ln:.0f} 2 l 0 46 q {-ln / 2:.0f} 6 {-ln:.0f} -2 z" '
                     f'fill="{MARK if j % 2 == 0 else MARK2}"/>')
            s.append(_t(150 + ln + 16, yy + 70, lab, 40, GREEN if j == len(items) - 1 else INK, SERIF, 900))
    elif kind == 'ledger':
        if kw.get('formula'):
            s.append(f'<rect x="136" y="{yb + 70}" width="{W - 226}" height="96" rx="8" fill="#fff" stroke="{INK}" stroke-width="3"/>')
            s.append(_t(W / 2 + 20, yb + 132, kw['formula'], 38, INK, SERIF, 900, 'middle'))
        s += _ledger(kw['rows'], yb + 280, 100)
    elif kind == 'timeline':
        steps = kw['steps']
        x = 190
        s.append(f'<line x1="{x}" y1="{yb + 110}" x2="{x}" y2="{yb + 110 + 150 * (len(steps) - 1)}" stroke="{INK}" stroke-width="4"/>')
        for j, (when, what) in enumerate(steps):
            yy = yb + 110 + j * 150
            s.append(f'<circle cx="{x}" cy="{yy}" r="22" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>')
            s.append(f'<circle cx="{x}" cy="{yy}" r="9" fill="{GREEN}"/>')
            s.append(_t(x + 50, yy - 4, when, 38, GREEN, SERIF, 900))
            s.append(_t(x + 50, yy + 46, what, 34, INK, SANS, 500))
    s += _note(kw.get('note'), 600, 850, -3, 360)
    if source:
        s += _foot(source)
    s.append('</svg>')
    return _render('\n'.join(s), png_path)
