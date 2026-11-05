"""Threads용 캐러셀 카드(4:5, 1080x1350). 2026-11-04 사용자 요청.

"제작해줘" 때 글은 저장소에 원래대로 만들고, 같은 글로 Threads 캐러셀을 만들어 채팅에 한 장씩 따로 보낸다.
카드 2026-11-05부터 블로그에도 같은 카드를 넣으므로 assets/carousel/에 저장한다(blog_html로 넘기는 HTML 생성). 카드마다 글 + 캐릭터(안경 쓴 '보스')가 들어간다.
디자인은 팝 스타일(pop_style.py)과 같은 남색 바탕·원색·Black Han Sans/Do Hyeon.

    from blog_automation.threads_carousel import make_carousel
    make_carousel(slug, cards, out_dir, badge='주식공부')

cards: 카드마다 dict
    kind: cover | big | list | end
    title: [줄, ...]           제목(cover는 크게)
    big: '69,304원'            kind=big일 때 가운데 큰 숫자
    sub: '...'                 큰 숫자 아래 설명
    lines: [줄, ...]           kind=list일 때 번호 목록(흰 카드), 다른 kind에선 보조 문장
    say: '...'                 캐릭터 말풍선
    pose: point | think | wow | thumb | wave | calc
숫자는 본문과 같은 출처 기준을 따른다(지어낸 숫자 금지).
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.make_illustrated_thumbnail import _install_fonts, _esc

W, H = 1080, 1350
NAVY, NAVY2 = '#1b2a4e', '#24366a'
YELLOW, CORAL, SKY, MINT = '#ffc93c', '#ff6b6b', '#4dabf7', '#38d9a9'
SKIN, HAIR, SHIRT = '#ffd9b8', '#2b2f45', '#4dabf7'
TF, BF = 'Black Han Sans', 'Do Hyeon'


def _t(x, y, text, size, fill, font=BF, anchor='start'):
    return f'<text x="{x:.0f}" y="{y:.0f}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{_esc(text)}</text>'


# ------------------------------------------------------------------ 캐릭터
def character(x, y, scale=1.0, pose='point', flip=False):
    """(x, y) = 발밑 가운데. 키 약 520*scale. 안경 쓴 단발 캐릭터, 외곽선 없는 flat."""
    sx = -scale if flip else scale
    g = [f'<g transform="translate({x:.0f},{y:.0f}) scale({sx:.3f},{scale:.3f}) translate(-200,-520)">']
    arm = 'stroke-width="34" stroke-linecap="round" fill="none"'
    # 뒤쪽 팔(왼쪽, 화면 기준)
    back = {
        'point': f'<path d="M135 350 Q 95 400 105 450" stroke="{SHIRT}" {arm}/>',
        'think': f'<path d="M135 350 Q 100 400 115 445" stroke="{SHIRT}" {arm}/>',
        'wow': f'<path d="M135 345 Q 70 300 60 230" stroke="{SHIRT}" {arm}/><circle cx="60" cy="222" r="22" fill="{SKIN}"/>',
        'thumb': f'<path d="M135 350 Q 95 400 105 450" stroke="{SHIRT}" {arm}/>',
        'wave': f'<path d="M135 350 Q 95 400 105 450" stroke="{SHIRT}" {arm}/>',
        'calc': f'<path d="M135 350 Q 120 410 175 420" stroke="{SHIRT}" {arm}/>',
    }[pose]
    g.append(back)
    if pose != 'wow':
        hand = {'point': (105, 458), 'think': (115, 452), 'thumb': (105, 458), 'wave': (105, 458), 'calc': (180, 420)}[pose]
        g.append(f'<circle cx="{hand[0]}" cy="{hand[1]}" r="21" fill="{SKIN}"/>')
    # 몸·다리
    g.append(f'<rect x="165" y="470" width="28" height="50" rx="12" fill="{HAIR}"/><rect x="207" y="470" width="28" height="50" rx="12" fill="{HAIR}"/>')
    g.append(f'<path d="M125 480 Q 120 340 200 320 Q 280 340 275 480 Z" fill="{SHIRT}"/>')
    g.append(f'<path d="M180 322 L200 350 L220 322 Z" fill="#ffffff"/>')
    # 머리
    g.append(f'<circle cx="200" cy="200" r="118" fill="{SKIN}"/>')
    g.append(f'<path d="M82 215 Q 70 90 200 78 Q 330 90 318 215 Q 300 150 250 140 Q 200 175 120 150 Q 95 175 82 215 Z" fill="{HAIR}"/>')
    g.append(f'<ellipse cx="84" cy="215" rx="16" ry="22" fill="{SKIN}"/><ellipse cx="316" cy="215" rx="16" ry="22" fill="{SKIN}"/>')
    # 눈·안경
    if pose == 'wow':
        g.append(f'<circle cx="155" cy="212" r="14" fill="{HAIR}"/><circle cx="245" cy="212" r="14" fill="{HAIR}"/>')
    elif pose == 'thumb':
        g.append(f'<path d="M140 214 q15 -16 30 0 M230 214 q15 -16 30 0" stroke="{HAIR}" stroke-width="8" stroke-linecap="round" fill="none"/>')
    else:
        g.append(f'<ellipse cx="155" cy="212" rx="10" ry="13" fill="{HAIR}"/><ellipse cx="245" cy="212" rx="10" ry="13" fill="{HAIR}"/>')
        g.append('<circle cx="159" cy="207" r="4" fill="#fff"/><circle cx="249" cy="207" r="4" fill="#fff"/>')
    g.append(f'<circle cx="155" cy="212" r="36" fill="#ffffff" fill-opacity="0.18" stroke="{HAIR}" stroke-width="7"/>')
    g.append(f'<circle cx="245" cy="212" r="36" fill="#ffffff" fill-opacity="0.18" stroke="{HAIR}" stroke-width="7"/>')
    g.append(f'<line x1="191" y1="210" x2="209" y2="210" stroke="{HAIR}" stroke-width="7"/>')
    if pose == 'think':
        g.append(f'<path d="M128 160 l40 -8 M232 152 l40 8" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/>')
    if pose == 'wow':
        g.append(f'<path d="M128 155 q25 -18 50 0 M222 155 q25 -18 50 0" stroke="{HAIR}" stroke-width="8" stroke-linecap="round" fill="none"/>')
    # 볼·입
    g.append('<circle cx="128" cy="262" r="17" fill="#ff8fa3" opacity="0.55"/><circle cx="272" cy="262" r="17" fill="#ff8fa3" opacity="0.55"/>')
    mouth = {
        'wow': f'<ellipse cx="200" cy="280" rx="18" ry="24" fill="#c0392b"/>',
        'think': f'<path d="M180 282 q20 -6 40 0" stroke="{HAIR}" stroke-width="7" stroke-linecap="round" fill="none"/>',
    }.get(pose, f'<path d="M170 268 q30 34 60 0 z" fill="#c0392b"/>')
    g.append(mouth)
    # 앞쪽 팔(오른쪽)
    front = {
        'point': f'<path d="M265 350 Q 320 300 345 235" stroke="{SHIRT}" {arm}/><circle cx="348" cy="228" r="22" fill="{SKIN}"/><path d="M352 212 L372 170" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>',
        'think': f'<path d="M265 350 Q 300 330 255 300" stroke="{SHIRT}" {arm}/><circle cx="246" cy="298" r="22" fill="{SKIN}"/>',
        'wow': f'<path d="M265 345 Q 330 300 340 230" stroke="{SHIRT}" {arm}/><circle cx="340" cy="222" r="22" fill="{SKIN}"/>',
        'thumb': f'<path d="M265 350 Q 320 360 335 300" stroke="{SHIRT}" {arm}/><circle cx="336" cy="292" r="24" fill="{SKIN}"/><rect x="326" y="246" width="18" height="40" rx="9" fill="{SKIN}"/>',
        'wave': f'<path d="M265 350 Q 330 320 345 245" stroke="{SHIRT}" {arm}/><circle cx="347" cy="236" r="24" fill="{SKIN}"/><path d="M380 210 q12 18 0 36 M398 200 q16 28 0 56" stroke="{YELLOW}" stroke-width="7" stroke-linecap="round" fill="none"/>',
        'calc': f'<rect x="205" y="360" width="110" height="140" rx="16" fill="#ffffff"/><rect x="218" y="373" width="84" height="32" rx="6" fill="{NAVY}"/>'
                + ''.join(f'<rect x="{218+c*30}" y="{415+r*28}" width="22" height="20" rx="5" fill="{CORAL if c == 2 else "#e1e6f2"}"/>' for r in range(3) for c in range(3))
                + f'<path d="M265 350 Q 330 400 300 440" stroke="{SHIRT}" {arm}/><circle cx="296" cy="446" r="21" fill="{SKIN}"/>',
    }[pose]
    g.append(front)
    g.append('</g>')
    return g


def bubble(x, y, text, w=None, tail='left', color='#ffffff', ink=NAVY, size=40):
    """(x, y) = 말풍선 왼쪽 위. tail: 꼬리 방향(left=왼쪽 아래, right=오른쪽 아래)."""
    w = w or 70 + sum(size if '가' <= ch <= '힣' else size * 0.55 for ch in text)
    h = size + 50
    tx = x + 60 if tail == 'left' else x + w - 60
    return [f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h}" rx="{h/2:.0f}" fill="{color}"/>',
            f'<path d="M{tx-18:.0f} {y+h-2:.0f} L{tx + (-30 if tail == "left" else 30):.0f} {y+h+34:.0f} L{tx+18:.0f} {y+h-2:.0f} Z" fill="{color}"/>',
            _t(x + w / 2, y + h / 2 + size * 0.36, text, size, ink, BF, 'middle')]


# ------------------------------------------------------------------ 카드
def _base(i, n, badge, accent):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            f'<circle cx="{W-60}" cy="{H-140}" r="380" fill="{NAVY2}"/>',
            f'<rect x="70" y="70" width="{40 + len(badge) * 36}" height="64" rx="32" fill="{accent}"/>',
            _t(90 + len(badge) * 18, 114, badge, 34, NAVY, BF, 'middle'),
            f'<rect x="{W-190}" y="70" width="120" height="64" rx="32" fill="#ffffff" fill-opacity="0.12"/>',
            _t(W - 130, 114, f'{i}/{n}', 32, '#ffffff', BF, 'middle')]


def _title(lines, y, size, colors=('#ffffff', YELLOW)):
    s = []
    for k, ln in enumerate(lines):
        s.append(_t(70, y, ln, size, colors[min(k, len(colors) - 1)], TF))
        y += size + 26
    return s, y


def card_svg(c, i, n, badge='주식공부', accent=MINT):
    kind = c.get('kind', 'list')
    s = _base(i, n, badge, accent)
    pose = c.get('pose', 'point')
    if kind == 'cover':
        t, y = _title(c['title'], 330, 108, ('#ffffff', accent, YELLOW))
        s += t
        for k, ln in enumerate(c.get('lines', [])):
            s.append(_t(72, y + 30 + k * 56, ln, 44, '#c9d3ee'))
        s += character(760, H - 70, 1.25, pose)
        if c.get('say'):
            s += bubble(70, H - 420, c['say'], tail='right')
        s.append(_t(72, H - 70, '옆으로 넘겨 보세요 →', 36, '#8fa0c8'))
    elif kind == 'big':
        t, y = _title(c['title'], 260, 74)
        s += t
        s.append(f'<rect x="70" y="{y+10}" width="{W-140}" height="300" rx="40" fill="#ffffff"/>')
        s.append(_t(W / 2, y + 190, c['big'], 128 if len(c['big']) <= 8 else 100, NAVY, TF, 'middle'))
        if c.get('sub'):
            s.append(_t(W / 2, y + 268, c['sub'], 38, '#6b7590', BF, 'middle'))
        for k, ln in enumerate(c.get('lines', [])):
            s.append(_t(72, y + 400 + k * 54, ln, 42, '#ffffff'))
        s += character(870, H - 60, 0.95, pose)
        if c.get('say'):
            s += bubble(80, H - 330, c['say'], tail='right')
    elif kind == 'list':
        t, y = _title(c['title'], 260, 74)
        s += t
        rows = c.get('lines', [])
        bh = 40 + len(rows) * 92
        s.append(f'<rect x="70" y="{y+10}" width="{W-140}" height="{bh}" rx="40" fill="#ffffff"/>')
        for k, ln in enumerate(rows):
            cy = y + 10 + 66 + k * 92
            s.append(f'<circle cx="140" cy="{cy}" r="30" fill="{(SKY, MINT, CORAL, YELLOW, SKY)[k % 5]}"/>')
            s.append(_t(140, cy + 13, str(k + 1), 36, '#ffffff', TF, 'middle'))
            s.append(_t(196, cy + 15, ln, 44, NAVY))
        s += character(880, H - 60, 0.9, pose)
        if c.get('say'):
            s += bubble(80, H - 320, c['say'], tail='right')
    else:  # end
        t, y = _title(c['title'], 330, 92, ('#ffffff', YELLOW))
        s += t
        for k, ln in enumerate(c.get('lines', [])):
            s.append(_t(72, y + 30 + k * 58, ln, 44, '#c9d3ee'))
        # 2026-11-05 사용자 요청: 블로그 이름을 크게 박으면 노골적으로 보여서, 마지막 장은 이름 대신 은은한 안내 칩만 둔다.
        cta = c.get('cta', '프로필 링크에서 이어 보기')
        cw = (80 if cta.endswith(('↓', '→')) else 120) + sum(37 if '\uac00' <= ch <= '\ud7a3' else 20 for ch in cta)
        s.append(f'<rect x="70" y="{y+200}" width="{cw}" height="88" rx="44" fill="#ffffff" fill-opacity="0.12"/>')
        if not cta.endswith(('↓', '→')):
            s.append(f'<path d="M{cw+10} {y+226} l18 18 l-18 18" fill="none" stroke="{YELLOW}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
        s.append(_t(108, y + 258, cta, 42, YELLOW))
        s += character(820, H - 70, 1.15, pose)
        if c.get('say'):
            s += bubble(120, H - 300, c['say'], tail='right')
    if kind != 'end':
        s.append(_t(W - 70, H - 40, '나도!지식 한입만', 28, '#8fa0c8', BF, 'end'))
    s.append('</svg>')
    return '\n'.join(s)


def make_carousel(slug, cards, out_dir, badge='주식공부', accent=None):
    accent = accent or (YELLOW if badge == '생활정보' else MINT)
    _install_fonts()
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, c in enumerate(cards, 1):
        p = out / f'{slug}-{i:02d}.svg'
        p.write_text(card_svg(c, i, len(cards), badge, accent), encoding='utf-8')
        subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(p)], check=True, capture_output=True)
        p.unlink()
        paths.append(str(p.with_suffix('.png')))
    return paths


RAW = 'https://raw.githubusercontent.com/leoleo0813/blog-automation/main/'


def blog_html(slug, n, alts):
    """블로그용 옆으로 넘기는 캐러셀 HTML(자바스크립트 없이 CSS scroll-snap). 이미지는 assets/carousel/<slug>-NN.png."""
    items = ''.join(
        f'<div style="flex:0 0 82%;max-width:420px;scroll-snap-align:center;">'
        f'<img src="{RAW}assets/carousel/{slug}-{i:02d}.png" alt="{_esc(alts[i-1])}" style="width:100%;border-radius:14px;display:block;"></div>'
        for i in range(1, n + 1))
    return ('<div style="margin:24px 0;">'
            '<div style="display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding-bottom:8px;">'
            f'{items}</div>'
            f'<p style="font-size:13px;color:#888;margin:6px 0 0 0;">옆으로 넘겨 보세요 → (카드 {n}장 요약)</p></div>')
