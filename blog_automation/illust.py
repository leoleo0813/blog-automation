"""본문용 그림 카드(손그림 스타일). 2026-10-30 사용자 요청 "본문 이미지도 더".

썸네일(make_illustrated_thumbnail)과 같은 크림색 바탕·Jua/Gaegu 글꼴·검은 외곽선 스타일로
막대·벤다이어그램·비교 카드·일정표를 그린다. 결과는 assets/figures/<이름>.svg → PNG.

    from blog_automation.illust import bars, venn, compare, steps
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.make_illustrated_thumbnail import _install_fonts, _esc

FIG = Path('assets/figures')
INK = '#2b2b2b'
PALETTE = ['#f5c542', '#7cc4a4', '#f39c7a', '#8fb3e8', '#c9a3e0']


def _frame(W, H, title, sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            '<defs><pattern id="d" width="34" height="34" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="2" fill="#ece0cc"/></pattern></defs>',
            f'<rect width="{W}" height="{H}" fill="#fff8ee"/><rect width="{W}" height="{H}" fill="url(#d)"/>',
            f'<text x="60" y="88" font-family="Jua" font-size="50" fill="{INK}">{_esc(title)}</text>',
            f'<text x="62" y="138" font-family="Gaegu" font-weight="bold" font-size="34" fill="#9a7b55">{_esc(sub)}</text>']


def _save(name, s, H, source):
    s.append(f'<text x="60" y="{H-26}" font-family="Jua" font-size="22" fill="#b8a98f">{_esc(source)}</text></svg>')
    _install_fonts()
    FIG.mkdir(parents=True, exist_ok=True)
    p = FIG / f'{name}.svg'
    p.write_text('\n'.join(s), encoding='utf-8')
    subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(p)], check=True, capture_output=True)
    return str(p.with_suffix('.png'))


def bars(name, title, sub, items, source, unit='', W=1200, H=760):
    """items: [(이름, 값, 아래 작은 글자)] — 둥근 막대, 값은 막대 위."""
    top, base = 210, H - 170
    vmax = max(v for _, v, _ in items)
    n = len(items)
    bw = min(200, (W - 160) // n - 50)
    gap = (W - 120 - n * bw) / (n + 1)
    s = _frame(W, H, title, sub)
    s.append(f'<line x1="60" y1="{base}" x2="{W-60}" y2="{base}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    for i, (lab, v, small) in enumerate(items):
        x = 60 + gap * (i + 1) + bw * i
        h = (base - top) * v / vmax
        c = PALETTE[i % len(PALETTE)]
        s.append(f'<rect x="{x+8:.0f}" y="{base-h+10:.0f}" width="{bw}" height="{h:.0f}" rx="22" fill="#000" opacity="0.07"/>')
        s.append(f'<rect x="{x:.0f}" y="{base-h:.0f}" width="{bw}" height="{h+20:.0f}" rx="22" fill="{c}" stroke="{INK}" stroke-width="5"/>')
        s.append(f'<rect x="{x-6:.0f}" y="{base}" width="{bw+12}" height="30" fill="#fff8ee"/>')
        s.append(f'<line x1="{x-6:.0f}" y1="{base}" x2="{x+bw+6:.0f}" y2="{base}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
        s.append(f'<text x="{x+bw/2:.0f}" y="{base-h-18:.0f}" font-family="Jua" font-size="40" text-anchor="middle" fill="{INK}">{_esc(f"{v:,}{unit}")}</text>')
        s.append(f'<text x="{x+bw/2:.0f}" y="{base+52:.0f}" font-family="Jua" font-size="32" text-anchor="middle" fill="{INK}">{_esc(lab)}</text>')
        if small:
            s.append(f'<text x="{x+bw/2:.0f}" y="{base+92:.0f}" font-family="Gaegu" font-weight="bold" font-size="28" text-anchor="middle" fill="#9a7b55">{_esc(small)}</text>')
    return _save(name, s, H, source)


def venn(name, title, sub, left, right, center, source, W=1200, H=760):
    """left/right: (제목, [줄...]) — 두 원이 겹치는 곳이 center."""
    s = _frame(W, H, title, sub)
    cy = 440
    s.append(f'<circle cx="455" cy="{cy}" r="250" fill="#8fb3e8" fill-opacity="0.55" stroke="{INK}" stroke-width="5"/>')
    s.append(f'<circle cx="745" cy="{cy}" r="250" fill="#f39c7a" fill-opacity="0.55" stroke="{INK}" stroke-width="5"/>')
    for (head, lines), x in ((left, 330), (right, 870)):
        s.append(f'<text x="{x}" y="{cy-90}" font-family="Jua" font-size="38" text-anchor="middle" fill="{INK}">{_esc(head)}</text>')
        for k, ln in enumerate(lines):
            s.append(f'<text x="{x}" y="{cy-35+k*42}" font-family="Gaegu" font-weight="bold" font-size="32" text-anchor="middle" fill="{INK}">{_esc(ln)}</text>')
    s.append(f'<g transform="translate(600,{cy}) rotate(-4)"><rect x="-80" y="-38" width="160" height="76" rx="38" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             f'<text x="0" y="14" font-family="Jua" font-size="40" text-anchor="middle" fill="#d0452f">{_esc(center)}</text></g>')
    return _save(name, s, H, source)


def compare(name, title, sub, cards, source, W=1200, H=760):
    """cards: [(아이콘, 제목, [줄...], 색)] 2~3장. 아이콘: bill · card · house · check · cross."""
    s = _frame(W, H, title, sub)
    n = len(cards)
    cw = (W - 120 - (n - 1) * 40) / n
    for i, (icon, head, lines, c) in enumerate(cards):
        x = 60 + i * (cw + 40)
        rot = -2 if i % 2 == 0 else 2
        s.append(f'<g transform="rotate({rot} {x+cw/2:.0f} 440)">')
        s.append(f'<rect x="{x+8:.0f}" y="190" width="{cw:.0f}" height="480" rx="30" fill="#000" opacity="0.07"/>')
        s.append(f'<rect x="{x:.0f}" y="180" width="{cw:.0f}" height="480" rx="30" fill="#fff" stroke="{INK}" stroke-width="5"/>')
        s += _icon(icon, x + cw / 2, 290, c)
        s.append(f'<text x="{x+cw/2:.0f}" y="420" font-family="Jua" font-size="42" text-anchor="middle" fill="{INK}">{_esc(head)}</text>')
        for k, ln in enumerate(lines):
            s.append(f'<text x="{x+cw/2:.0f}" y="{480+k*46}" font-family="Gaegu" font-weight="bold" font-size="33" text-anchor="middle" fill="#4a4a4a">{_esc(ln)}</text>')
        s.append('</g>')
    return _save(name, s, H, source)


def steps(name, title, sub, events, source, W=1200, H=700):
    """events: [(날짜, 설명, 강조 여부)] — 손그림 길 위에 깃발."""
    s = _frame(W, H, title, sub)
    n = len(events)
    xs = [140 + (W - 280) * i / max(n - 1, 1) for i in range(n)]
    d = f'M{xs[0]-60} 420 ' + ' '.join(f'Q {x-80} {380 if i % 2 else 460} {x} 420' for i, x in enumerate(xs[1:], 1)) + f' T {xs[-1]+60} 420'
    s.append(f'<path d="{d}" fill="none" stroke="#e9d9bf" stroke-width="34" stroke-linecap="round"/>')
    s.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 12" stroke-linecap="round"/>')
    for x, (date, desc, hot) in zip(xs, events):
        c = '#e35d5b' if hot else '#7cc4a4'
        s.append(f'<line x1="{x:.0f}" y1="420" x2="{x:.0f}" y2="300" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
        s.append(f'<path d="M{x:.0f} 300 l 70 22 l -70 22 z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
        s.append(f'<circle cx="{x:.0f}" cy="420" r="14" fill="{c}" stroke="{INK}" stroke-width="4"/>')
        s.append(f'<text x="{x:.0f}" y="510" font-family="Jua" font-size="38" text-anchor="middle" fill="{"#d0452f" if hot else INK}">{_esc(date)}</text>')
        for k, ln in enumerate(desc.split('\n')):
            s.append(f'<text x="{x:.0f}" y="{556+k*40}" font-family="Gaegu" font-weight="bold" font-size="32" text-anchor="middle" fill="#4a4a4a">{_esc(ln)}</text>')
    return _save(name, s, H, source)


def _icon(kind, cx, cy, c):
    if kind == 'bill':
        return [f'<g transform="translate({cx-50:.0f},{cy-65:.0f}) rotate(-6 50 65)"><path d="M0 0 h100 v130 l-17 -12 l-17 12 l-16 -12 l-17 12 l-16 -12 l-17 12 z" fill="#fff" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
                f'<line x1="18" y1="30" x2="82" y2="30" stroke="{INK}" stroke-width="5"/><line x1="18" y1="55" x2="70" y2="55" stroke="{INK}" stroke-width="5"/>'
                f'<rect x="18" y="74" width="64" height="26" rx="6" fill="{c}" stroke="{INK}" stroke-width="4"/></g>']
    if kind == 'card':
        return [f'<g transform="translate({cx-85:.0f},{cy-55:.0f}) rotate(5 85 55)"><rect x="0" y="0" width="170" height="110" rx="16" fill="{c}" stroke="{INK}" stroke-width="5"/>'
                f'<rect x="0" y="24" width="170" height="22" fill="{INK}"/><rect x="18" y="66" width="44" height="28" rx="6" fill="#f5c542" stroke="{INK}" stroke-width="4"/></g>']
    if kind == 'house':
        return [f'<g transform="translate({cx-70:.0f},{cy-70:.0f})"><path d="M10 65 L70 10 L130 65" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                f'<rect x="25" y="60" width="90" height="75" rx="8" fill="{c}" stroke="{INK}" stroke-width="5"/><rect x="58" y="92" width="26" height="43" fill="#fff" stroke="{INK}" stroke-width="4"/></g>']
    if kind == 'check':
        return [f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="62" fill="{c}" stroke="{INK}" stroke-width="5"/>',
                f'<path d="M{cx-30:.0f} {cy:.0f} l 22 24 l 40 -48" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>']
    if kind == 'cross':
        return [f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="62" fill="{c}" stroke="{INK}" stroke-width="5"/>',
                f'<path d="M{cx-26:.0f} {cy-26:.0f} l 52 52 M{cx+26:.0f} {cy-26:.0f} l -52 52" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>']
    return []
