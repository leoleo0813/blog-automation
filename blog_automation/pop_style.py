"""'팝' 스타일 썸네일·본문 그림. 2026-11-04 사용자 요청 "이미지 느낌도 변경해줘".

기존 손그림 스타일(크림 바탕·Jua/Gaegu·검은 외곽선)과 다르게, 진한 남색 바탕 + 원색 포인트,
외곽선 없는 납작한(flat) 도형, 포스터 같은 굵은 글꼴(Black Han Sans·Do Hyeon, OFL)을 쓴다.

썸네일: front matter에 thumb_style: pop 을 넣으면 ensure_thumbnail이 이 모듈로 그린다.
    python -m blog_automation.pop_style <slug> "<1줄|2줄>" <track> "<메모>" [화면/날짜 글자] [그림]
    그림: calc(계산기) · calendar(달력) · coin(동전) · chart(막대+화살표). 비우면 life=달력, chart=chart.

본문 그림: illust.py와 같은 이름의 함수.
    from blog_automation.pop_style import bars, compare, steps, line_levels
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.make_illustrated_thumbnail import _install_fonts, _esc

FIG = Path('assets/figures')
OUT = Path('assets/thumbnails')
NAVY, NAVY2, PAPER = '#1b2a4e', '#24366a', '#f4f6fb'
YELLOW, CORAL, SKY, MINT, LILAC = '#ffc93c', '#ff6b6b', '#4dabf7', '#38d9a9', '#b197fc'
PALETTE = [SKY, YELLOW, CORAL, MINT, LILAC]
TITLE_FONT, BODY_FONT = 'Black Han Sans', 'Do Hyeon'
TRACKS = {'chart': ('주식공부', MINT), 'life': ('생활정보', YELLOW)}


# ---------------------------------------------------------------- 테마(색 조합) 돌려쓰기
# 2026-11-10 사용자 요청 "반복 디자인 방지": 그림을 그린 뒤 기본(남색) 색을 테마 색으로 한 번에 바꾼다.
# 글마다 front matter `theme:`로 고르고, navy → forest → plum → charcoal 순서로 돌려 쓴다(RULES 「이미지」).
_BASE = ['#1b2a4e', '#24366a', '#f4f6fb', '#ffc93c', '#ff6b6b', '#4dabf7', '#38d9a9', '#b197fc',
         '#8fa0c8', '#a9b6d8', '#c9d3ee', '#6b7590', '#4a5470', '#cfd5e3', '#e7ebf5', '#e1e6f2', '#8a93a8', '#b3bacb']
THEMES = {
    'navy': _BASE,
    'forest': ['#173a33', '#1f4a41', '#f3f7f2', '#ffd166', '#f08a5d', '#6cc4a1', '#b8e05c', '#f4a6c0',
               '#93b5a8', '#a9c9bd', '#cfe3da', '#5f7068', '#3f5149', '#cfdcd5', '#e6eee9', '#e0e9e4', '#7f938a', '#adbdb5'],
    'plum': ['#2d1e4a', '#3b2860', '#f7f4fb', '#ffcf5c', '#ff7a90', '#7aa7ff', '#4fd1c5', '#ffb3d9',
             '#a99cc9', '#bdb2db', '#dcd3ef', '#6e6488', '#4c4266', '#d8d2e6', '#ece8f4', '#e6e1f0', '#958cab', '#bdb6cf'],
    'charcoal': ['#24262b', '#30333a', '#f6f5f2', '#ffb84d', '#ff6f59', '#5aa9e6', '#7bd389', '#c9a7eb',
                 '#a2a6b0', '#b8bcc5', '#d9dbe0', '#6b6e76', '#45484f', '#d6d7da', '#ebebed', '#e4e5e8', '#8e9198', '#b9bbc0'],
}
THEME = 'navy'


def set_theme(name):
    global THEME
    THEME = name if name in THEMES else 'navy'


def apply_theme(svg, name=None):
    import re as _re
    cmap = dict(zip(_BASE, THEMES.get(name or THEME, _BASE)))
    return _re.sub(r'#[0-9a-fA-F]{6}\b', lambda m: cmap.get(m.group(0).lower(), m.group(0)), svg)


def _shade(c, k=0.78):
    r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return '#%02x%02x%02x' % (int(r * k), int(g * k), int(b * k))


def _t(x, y, text, size, fill, font=BODY_FONT, anchor='start', extra=''):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{font}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" {extra}>{_esc(text)}</text>')


def _render(path, svg_lines):
    _install_fonts()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(apply_theme('\n'.join(svg_lines)), encoding='utf-8')
    subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(path)], check=True, capture_output=True)
    return str(path.with_suffix('.png'))


# ---------------------------------------------------------------- 썸네일 그림
def _art_calc(cx, cy, text):
    s = [f'<g transform="translate({cx-150},{cy-200}) rotate(-6 150 200)">',
         f'<rect x="14" y="18" width="300" height="400" rx="34" fill="#000000" fill-opacity="0.18"/>',
         f'<rect x="0" y="0" width="300" height="400" rx="34" fill="#ffffff"/>',
         f'<rect x="26" y="26" width="248" height="92" rx="18" fill="{NAVY}"/>',
         _t(254, 92, text or '₩', 50, YELLOW, TITLE_FONT, 'end')]
    for k in range(16):
        r, c = divmod(k, 4)
        col = CORAL if c == 3 else ('#e7ebf5' if r < 3 else SKY)
        s.append(f'<rect x="{30 + c*62}" y="{140 + r*62}" width="50" height="50" rx="14" fill="{col}"/>')
    s.append('</g>')
    return s


def _art_calendar(cx, cy, text):
    s = [f'<g transform="translate({cx-190},{cy-170}) rotate(5 190 170)">',
         f'<rect x="14" y="18" width="380" height="340" rx="34" fill="#000000" fill-opacity="0.18"/>',
         '<rect x="0" y="0" width="380" height="340" rx="34" fill="#ffffff"/>',
         f'<path d="M0 34 a34 34 0 0 1 34 -34 h312 a34 34 0 0 1 34 34 v56 h-380 z" fill="{CORAL}"/>',
         f'<rect x="80" y="-18" width="20" height="44" rx="10" fill="{NAVY}"/><rect x="280" y="-18" width="20" height="44" rx="10" fill="{NAVY}"/>',
         _t(190, 250, text or 'D-DAY', 84, NAVY, TITLE_FONT, 'middle'),
         f'<rect x="70" y="282" width="240" height="14" rx="7" fill="{YELLOW}"/>', '</g>']
    return s


def _art_coin(cx, cy, text):
    s = []
    for i in range(5):
        y = cy + 150 - i * 38
        s.append(f'<ellipse cx="{cx-60}" cy="{y+14}" rx="110" ry="36" fill="#000000" fill-opacity="0.18"/>')
        s.append(f'<ellipse cx="{cx-60}" cy="{y}" rx="110" ry="36" fill="#ffd966"/>')
    s.append(f'<circle cx="{cx+90}" cy="{cy-90}" r="120" fill="#ffffff"/>')
    s.append(_t(cx + 90, cy - 50, text or '₩', 110 if len(text or '₩') < 3 else 64, NAVY, TITLE_FONT, 'middle'))
    return s


def _art_chart(cx, cy, text):
    s = [f'<g transform="translate({cx-200},{cy-170})">',
         f'<rect x="14" y="18" width="400" height="330" rx="34" fill="#000000" fill-opacity="0.18"/>',
         '<rect x="0" y="0" width="400" height="330" rx="34" fill="#ffffff"/>']
    for i, h in enumerate((90, 150, 120, 210)):
        s.append(f'<rect x="{50 + i*80}" y="{290-h}" width="56" height="{h}" rx="12" fill="{(SKY, MINT, CORAL, NAVY)[i]}"/>')
    s.append(f'<path d="M50 200 L150 140 L230 170 L350 60" fill="none" stroke="{YELLOW}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="M318 52 L362 50 L356 94 Z" fill="{YELLOW}"/>')
    s.append('</g>')
    return s


ARTS = {'calc': _art_calc, 'calendar': _art_calendar, 'coin': _art_coin, 'chart': _art_chart}


def build_thumb(title_lines, track, note, text='', art=''):
    W, H = 1200, 900
    badge, accent = TRACKS.get(track, TRACKS['chart'])
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
         f'<circle cx="1010" cy="640" r="360" fill="{NAVY2}"/>',
         f'<circle cx="960" cy="600" r="250" fill="{accent}"/>',
         # 기하 장식
         f'<circle cx="1120" cy="210" r="18" fill="{CORAL}"/>',
         f'<rect x="630" y="760" width="36" height="36" rx="8" fill="{SKY}" transform="rotate(20 648 778)"/>',
         f'<path d="M590 560 h34 M607 543 v34" stroke="{MINT}" stroke-width="10" stroke-linecap="round"/>',
         f'<rect x="80" y="86" width="196" height="64" rx="32" fill="{accent}"/>',
         _t(178, 131, badge, 38, NAVY, BODY_FONT, 'middle'),
         _t(1120, 131, '나도!지식 한입만', 28, '#8fa0c8', BODY_FONT, 'end')]
    y = 300
    for i, line in enumerate(title_lines[:3]):
        size = 104 if len(line) <= 8 else (90 if len(line) <= 10 else 76)
        s.append(_t(84, y, line, size, '#ffffff' if i == 0 else accent, TITLE_FONT))
        y += size + 30
    kind = art if art in ARTS else ('calendar' if track == 'life' else 'chart')
    s += ARTS[kind](960, 600, text)
    if note:
        w = 90 + sum(36 if '\uac00' <= ch <= '\ud7a3' else 19 for ch in note)
        s.append(f'<rect x="80" y="{H-160}" width="{w}" height="76" rx="38" fill="#ffffff" fill-opacity="0.12"/>')
        s.append(f'<circle cx="118" cy="{H-122}" r="12" fill="{CORAL}"/>')
        s.append(_t(144, H - 108, note, 42, '#ffffff'))
    s.append('</svg>')
    return s


def thumbnail(slug, title, track, note, text='', art=''):
    return _render(OUT / f'{slug}.svg', build_thumb([p.strip() for p in title.split('|')], track, note, text, art))


# ---------------------------------------------------------------- 본문 그림
def _frame(W, H, title, sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
            f'<rect width="{W}" height="170" fill="{NAVY}"/>',
            f'<rect x="60" y="54" width="10" height="70" rx="5" fill="{YELLOW}"/>',
            _t(92, 100, title, 50, '#ffffff', TITLE_FONT),
            _t(94, 142, sub, 30, '#a9b6d8')]


def _save(name, s, W, H, source):
    s.append(_t(60, H - 26, source, 22, '#8a93a8'))
    s.append(_t(W - 60, H - 26, '나도!지식 한입만', 22, '#b3bacb', anchor='end'))
    s.append('</svg>')
    return _render(FIG / f'{name}.svg', s)


def bars(name, title, sub, items, source, unit='', W=1200, H=760, colors=None):
    """items: [(이름, 값, 아래 작은 글자)]. 막대는 외곽선 없이 위만 둥글게, 값은 막대 위 굵게."""
    top, base = 260, H - 170
    vmax = max(v for _, v, _ in items)
    n = len(items)
    bw = min(190, (W - 160) // n - 50)
    gap = (W - 120 - n * bw) / (n + 1)
    s = _frame(W, H, title, sub)
    s.append(f'<rect x="60" y="{base}" width="{W-120}" height="6" rx="3" fill="#cfd5e3"/>')
    for i, (lab, v, small) in enumerate(items):
        x = 60 + gap * (i + 1) + bw * i
        h = max((base - top) * v / vmax, 8)
        c = (colors or PALETTE)[i % len(colors or PALETTE)]
        s.append(f'<path d="M{x:.0f} {base} v{-(h-24):.0f} a24 24 0 0 1 24 -24 h{bw-48} a24 24 0 0 1 24 24 v{h-24:.0f} z" fill="{c}"/>')
        s.append(_t(x + bw / 2, base - h - 20, f'{v:,}{unit}', 42, NAVY, TITLE_FONT, 'middle'))
        s.append(_t(x + bw / 2, base + 52, lab, 32, NAVY, anchor='middle'))
        if small:
            s.append(_t(x + bw / 2, base + 90, small, 26, '#6b7590', anchor='middle'))
    return _save(name, s, W, H, source)


def compare(name, title, sub, cards, source, W=1200, H=760):
    """cards: [(큰 글자 또는 기호, 제목, [줄...], 색)] 2~3장. 카드 위쪽 색 띠 + 큰 원 안 글자."""
    s = _frame(W, H, title, sub)
    n = len(cards)
    cw = (W - 120 - (n - 1) * 36) / n
    for i, (big, head, lines, c) in enumerate(cards):
        x = 60 + i * (cw + 36)
        s.append(f'<rect x="{x:.0f}" y="214" width="{cw:.0f}" height="450" rx="28" fill="#ffffff"/>')
        s.append(f'<path d="M{x:.0f} 242 a28 28 0 0 1 28 -28 h{cw-56:.0f} a28 28 0 0 1 28 28 v20 h{-cw:.0f} z" fill="{c}"/>')
        s.append(f'<circle cx="{x+cw/2:.0f}" cy="330" r="62" fill="{c}"/>')
        s.append(_t(x + cw / 2, 330 + (22 if len(big) <= 2 else 14), big, 64 if len(big) <= 2 else 40, '#ffffff', TITLE_FONT, 'middle'))
        s.append(_t(x + cw / 2, 450, head, 40, NAVY, TITLE_FONT, 'middle'))
        for k, ln in enumerate(lines):
            s.append(_t(x + cw / 2, 508 + k * 44, ln, 31, '#4a5470', anchor='middle'))
    return _save(name, s, W, H, source)


def steps(name, title, sub, events, source, W=1200, H=700):
    """events: [(큰 글자, 설명(줄바꿈 \\n), 강조 여부)] — 굵은 가로줄 위 번호 원."""
    s = _frame(W, H, title, sub)
    n = len(events)
    xs = [160 + (W - 320) * i / max(n - 1, 1) for i in range(n)]
    s.append(f'<rect x="{xs[0]:.0f}" y="352" width="{xs[-1]-xs[0]:.0f}" height="12" rx="6" fill="#cfd5e3"/>')
    for k, (x, (big, desc, hot)) in enumerate(zip(xs, events), 1):
        c = CORAL if hot else SKY
        s.append(f'<circle cx="{x:.0f}" cy="358" r="54" fill="{c}"/>')
        s.append(_t(x, 376, str(k), 52, '#ffffff', TITLE_FONT, 'middle'))
        s.append(_t(x, 470, big, 38, CORAL if hot else NAVY, TITLE_FONT, 'middle'))
        for j, ln in enumerate(desc.split('\n')):
            s.append(_t(x, 516 + j * 40, ln, 30, '#4a5470', anchor='middle'))
    return _save(name, s, W, H, source)


def line_levels(name, title, sub, series, levels, source, marks=(), W=1200, H=800, pad=None, slopes=()):
    """series: 종가 목록. levels: [(가격, 이름, 색)] 가로 점선. marks: [(인덱스, 글자, 색[, dx, dy])] 점과 말풍선."""
    x0, x1, y0, y1 = 150, W - 230, 220, H - 120
    lo, hi = min(series), max(series)
    pad = pad if pad is not None else (hi - lo) * 0.08
    lo, hi = lo - pad, hi + pad
    X = lambda i: x0 + (x1 - x0) * i / (len(series) - 1)
    Y = lambda v: y1 - (y1 - y0) * (v - lo) / (hi - lo)
    s = _frame(W, H, title, sub)
    s.append(f'<rect x="{x0-20}" y="{y0-20}" width="{x1-x0+40}" height="{y1-y0+40}" rx="22" fill="#ffffff"/>')
    for v, lab, c in levels:
        s.append(f'<line x1="{x0}" y1="{Y(v):.0f}" x2="{x1}" y2="{Y(v):.0f}" stroke="{c}" stroke-width="4" stroke-dasharray="12 10"/>')
        s.append(f'<rect x="{x1+24}" y="{Y(v)-20:.0f}" width="180" height="40" rx="20" fill="{c}"/>')
        s.append(_t(x1 + 114, Y(v) + 10, lab, 26, '#ffffff', anchor='middle'))
        s.append(_t(x0 - 30, Y(v) + 9, f'{v:,.0f}', 24, '#6b7590', anchor='end'))
    # slopes: [(d0, v0, d1, v1, 이름, 색, 점선여부)] 기울어진 선(추세선). 이름은 선 끝 오른쪽에.
    for d0, v0, d1, v1, lab, c, dash in slopes:
        da = 'stroke-dasharray="12 10"' if dash else ''
        s.append(f'<line x1="{X(d0):.0f}" y1="{Y(v0):.0f}" x2="{X(d1):.0f}" y2="{Y(v1):.0f}" stroke="{c}" stroke-width="5" {da} stroke-linecap="round"/>')
        if lab:
            s.append(f'<rect x="{x1+24}" y="{Y(v1)-20:.0f}" width="180" height="40" rx="20" fill="{c}"/>')
            s.append(_t(x1 + 114, Y(v1) + 10, lab, 26, '#ffffff', anchor='middle'))
    pts = ' '.join(f'{X(i):.1f},{Y(v):.1f}' for i, v in enumerate(series))
    s.append(f'<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>')
    for m in marks:
        i, lab, c = m[:3]
        x, y = X(i), Y(series[i])
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="13" fill="{c}" stroke="#ffffff" stroke-width="4"/>')
        w = 30 + len(lab) * 25
        if len(m) > 3:  # (dx, dy): 말풍선 가운데를 점에서 이만큼 옮긴다
            bx, by = x + m[3] - w / 2, y + m[4] - 23
        else:
            by = y - 70 if y > (y0 + y1) / 2 else y + 40
            bx = min(max(x - w / 2, x0), x1 - w)
        s.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{bx+w/2:.0f}" y2="{by+23:.0f}" stroke="{c}" stroke-width="3"/>')
        s.append(f'<rect x="{bx:.0f}" y="{by:.0f}" width="{w:.0f}" height="46" rx="23" fill="{c}"/>')
        s.append(_t(bx + w / 2, by + 32, lab, 27, '#ffffff', anchor='middle'))
    return _save(name, s, W, H, source)


def main():
    slug, title, track, note = sys.argv[1:5]
    text = sys.argv[5] if len(sys.argv) > 5 else ''
    art = sys.argv[6] if len(sys.argv) > 6 else ''
    set_theme(sys.argv[7] if len(sys.argv) > 7 else 'navy')
    print(thumbnail(slug, title, track, note, text, art))


if __name__ == '__main__':
    main()
