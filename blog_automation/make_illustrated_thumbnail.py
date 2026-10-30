"""그림이 들어간 썸네일(1200x900)을 만든다. 2026-10-30 사용자 피드백 "썸네일이 딱딱하고 AI 같다"로 추가.

어두운 단색 배경 + 고딕 글자 대신, 크림색 바탕에 둥근 손글씨풍 글꼴(Jua·Gaegu, OFL)과
갈래별 손그림 일러스트(차트: 캔들 카드 / 생활정보: 달력·동전)를 넣는다.

    python -m blog_automation.make_illustrated_thumbnail <slug> "<제목 1줄|제목 2줄>" <track> "<메모>" [달력 날짜] [그림]

그림(thumb_art): chart(캔들) · heater(난방기) · piggy(저금통) · calc(계산기). 비우면 track 기본(차트=캔들, 생활=달력).

track: chart(기본, 배지 "주식공부") 또는 life(배지 "생활정보"). 강조 글자는 life 달력에 동그라미 칠 날짜(예: 11/27).
"""
import shutil
import subprocess
import sys
from pathlib import Path

FONT_DIR = Path(__file__).resolve().parent.parent / 'assets' / 'fonts'
OUT = Path('assets/thumbnails')
W, H = 1200, 900

TRACKS = {
    'chart': dict(badge='주식공부', badge_bg='#2f6f4f', mark='#ffe08a', accent='#2f6f4f'),
    'life': dict(badge='생활정보', badge_bg='#e0703a', mark='#ffd6b8', accent='#e0703a'),
}


def _install_fonts():
    """Chromium이 fontconfig로 찾도록 저장소의 글꼴을 사용자 글꼴 폴더에 둔다."""
    dest = Path.home() / '.fonts'
    dest.mkdir(exist_ok=True)
    copied = False
    for f in FONT_DIR.glob('*.ttf'):
        if not (dest / f.name).exists():
            shutil.copy(f, dest / f.name)
            copied = True
    if copied:
        subprocess.run(['fc-cache', '-f'], capture_output=True)


def _esc(t):
    return str(t).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _chart_art():
    """살짝 기울어진 종이 카드 위 캔들과 선, 돋보기."""
    candles = [(0, 60, 120, 40, 140, 'u'), (1, 90, 150, 70, 170, 'd'), (2, 110, 60, 40, 130, 'u'),
               (3, 70, 40, 20, 90, 'u'), (4, 45, 95, 30, 115, 'd'), (5, 80, 30, 10, 100, 'u')]
    s = ['<g transform="translate(700,470) rotate(-4)">',
         '<rect x="8" y="12" width="420" height="320" rx="26" fill="#000" opacity="0.08"/>',
         '<rect x="0" y="0" width="420" height="320" rx="26" fill="#ffffff" stroke="#2b2b2b" stroke-width="5"/>']
    for i, o, c, hi, lo, d in candles:
        x = 60 + i * 58
        top, bot = 70 + min(o, c), 70 + max(o, c)
        col = '#e35d5b' if d == 'u' else '#4a7bd0'  # 한국식: 오르면 빨강, 내리면 파랑
        s.append(f'<line x1="{x}" y1="{70+hi-30}" x2="{x}" y2="{70+lo+20}" stroke="#2b2b2b" stroke-width="4" stroke-linecap="round"/>')
        s.append(f'<rect x="{x-17}" y="{top}" width="34" height="{max(bot-top, 8)}" rx="6" fill="{col}" stroke="#2b2b2b" stroke-width="4"/>')
    s.append('<path d="M40 270 C 120 250, 170 290, 230 230 S 340 150, 390 120" fill="none" stroke="#f0a020" stroke-width="7" stroke-linecap="round"/>')
    s.append('</g>')
    # 돋보기
    s.append('<g transform="translate(1040,760) rotate(20)"><circle cx="0" cy="0" r="52" fill="#fff8" stroke="#2b2b2b" stroke-width="8"/>'
             '<line x1="38" y1="38" x2="92" y2="92" stroke="#2b2b2b" stroke-width="16" stroke-linecap="round"/></g>')
    return s


def _life_art(date_text):
    """달력 한 장(날짜에 빨간 동그라미)과 동전 더미."""
    s = ['<g transform="translate(720,440) rotate(3)">',
         '<rect x="8" y="12" width="380" height="340" rx="26" fill="#000" opacity="0.08"/>',
         '<rect x="0" y="0" width="380" height="340" rx="26" fill="#ffffff" stroke="#2b2b2b" stroke-width="5"/>',
         '<rect x="0" y="0" width="380" height="80" rx="26" fill="#e0703a" stroke="#2b2b2b" stroke-width="5"/>',
         '<rect x="0" y="50" width="380" height="30" fill="#e0703a"/>',
         '<line x1="0" y1="80" x2="380" y2="80" stroke="#2b2b2b" stroke-width="5"/>',
         '<circle cx="90" cy="0" r="12" fill="#2b2b2b"/><circle cx="290" cy="0" r="12" fill="#2b2b2b"/>']
    for r in range(3):
        for c in range(5):
            s.append(f'<rect x="{38 + c*66}" y="{110 + r*72}" width="40" height="40" rx="8" fill="#f1ece4"/>')
    s.append(f'<text x="190" y="240" font-family="Jua" font-size="74" text-anchor="middle" fill="#2b2b2b">{_esc(date_text)}</text>')
    s.append('<ellipse cx="190" cy="215" rx="150" ry="62" fill="none" stroke="#e35d5b" stroke-width="8" transform="rotate(-6 190 215)"/>')
    s.append('</g>')
    for i in range(4):  # 동전 더미
        y = 790 - i * 26
        s.append(f'<ellipse cx="660" cy="{y}" rx="70" ry="24" fill="#f5c542" stroke="#2b2b2b" stroke-width="5"/>')
    s.append('<text x="660" y="722" font-family="Jua" font-size="34" text-anchor="middle" fill="#8a6500">₩</text>')
    return s


def _heater_art():
    """라디에이터(난방기)와 김 세 줄, 따뜻한 머그잔."""
    s = ['<g transform="translate(700,470) rotate(-3)">',
         '<rect x="10" y="14" width="400" height="290" rx="30" fill="#000" opacity="0.08"/>']
    for i in range(6):
        x = 20 + i * 64
        s.append(f'<rect x="{x}" y="40" width="52" height="250" rx="26" fill="#ffffff" stroke="#2b2b2b" stroke-width="5"/>')
        s.append(f'<line x1="{x+26}" y1="70" x2="{x+26}" y2="260" stroke="#f3d3c2" stroke-width="8" stroke-linecap="round"/>')
    s.append('<rect x="0" y="250" width="420" height="34" rx="14" fill="#e0703a" stroke="#2b2b2b" stroke-width="5"/>')
    for i in range(3):  # 김
        x = 110 + i * 100
        s.append(f'<path d="M{x} 20 c -22 -30, 22 -45, 0 -75 s 22 -45, 0 -75" fill="none" stroke="#e35d5b" stroke-width="7" stroke-linecap="round" opacity="0.8"/>')
    s.append('</g>')
    s.append('<g transform="translate(545,700)"><rect x="0" y="0" width="110" height="120" rx="18" fill="#f5c542" stroke="#2b2b2b" stroke-width="5"/>'
             '<path d="M110 30 q 45 0 45 35 t -45 35" fill="none" stroke="#2b2b2b" stroke-width="8"/></g>')
    return s


def _piggy_art():
    """저금통 돼지와 떨어지는 동전."""
    s = ['<g transform="translate(760,520)">',
         '<ellipse cx="170" cy="150" rx="190" ry="140" fill="#000" opacity="0.07"/>',
         '<ellipse cx="160" cy="140" rx="190" ry="140" fill="#f7a8b8" stroke="#2b2b2b" stroke-width="6"/>',
         '<ellipse cx="335" cy="140" rx="42" ry="50" fill="#f48fa5" stroke="#2b2b2b" stroke-width="6"/>',
         '<circle cx="325" cy="128" r="7" fill="#2b2b2b"/><circle cx="345" cy="152" r="7" fill="#2b2b2b"/>',
         '<circle cx="250" cy="90" r="11" fill="#2b2b2b"/>',
         '<path d="M180 10 l 40 -55 l 30 60 z" fill="#f48fa5" stroke="#2b2b2b" stroke-width="6" stroke-linejoin="round"/>',
         '<rect x="110" y="0" width="90" height="16" rx="8" fill="#2b2b2b"/>',
         '<rect x="40" y="250" width="40" height="60" rx="12" fill="#f48fa5" stroke="#2b2b2b" stroke-width="6"/>',
         '<rect x="230" y="250" width="40" height="60" rx="12" fill="#f48fa5" stroke="#2b2b2b" stroke-width="6"/>',
         '</g>']
    for x, y in ((900, 400), (980, 330)):
        s.append(f'<g transform="translate({x},{y}) rotate(-15)"><ellipse cx="0" cy="0" rx="40" ry="40" fill="#f5c542" stroke="#2b2b2b" stroke-width="5"/>'
                 '<text x="0" y="14" font-family="Jua" font-size="38" text-anchor="middle" fill="#8a6500">₩</text></g>')
    return s


def _calc_art():
    """계산기와 영수증."""
    s = ['<g transform="translate(760,450) rotate(4)">',
         '<rect x="10" y="14" width="300" height="400" rx="30" fill="#000" opacity="0.08"/>',
         '<rect x="0" y="0" width="300" height="400" rx="30" fill="#ffffff" stroke="#2b2b2b" stroke-width="6"/>',
         '<rect x="30" y="30" width="240" height="80" rx="12" fill="#dff0e6" stroke="#2b2b2b" stroke-width="5"/>',
         '<text x="250" y="88" font-family="Jua" font-size="48" text-anchor="end" fill="#2b2b2b">12%</text>']
    keys = ['7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '−', '0', '.', '=', '+']
    for k, lab in enumerate(keys):
        r, c = divmod(k, 4)
        x, y = 30 + c * 62, 135 + r * 62
        col = '#f0a020' if c == 3 else '#f1ece4'
        s.append(f'<rect x="{x}" y="{y}" width="50" height="50" rx="12" fill="{col}" stroke="#2b2b2b" stroke-width="4"/>')
        s.append(f'<text x="{x+25}" y="{y+36}" font-family="Jua" font-size="28" text-anchor="middle" fill="#2b2b2b">{lab}</text>')
    s.append('</g>')
    return s


ARTS = {'chart': _chart_art, 'heater': _heater_art, 'piggy': _piggy_art, 'calc': _calc_art}


def build_svg(title_lines, track, note, date_text='', art=''):
    t = TRACKS.get(track, TRACKS['chart'])
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<defs><pattern id="dots" width="36" height="36" patternUnits="userSpaceOnUse">'
         '<circle cx="2" cy="2" r="2" fill="#e9dcc8"/></pattern></defs>',
         f'<rect width="{W}" height="{H}" fill="#fff8ee"/>', f'<rect width="{W}" height="{H}" fill="url(#dots)"/>']
    # 배지
    s.append(f'<g transform="translate(90,90) rotate(-3)"><rect x="0" y="0" width="210" height="68" rx="34" fill="{t["badge_bg"]}"/>'
             f'<text x="105" y="47" font-family="Jua" font-size="38" text-anchor="middle" fill="#fff">{_esc(t["badge"])}</text></g>')
    # 제목(첫 줄은 형광펜)
    y = 290
    for i, line in enumerate(title_lines[:3]):
        size = 92 if len(line) <= 10 else 80
        if i == 0:
            w = min(len(line) * size * 0.95, 1040)
            s.append(f'<rect x="80" y="{y-62}" width="{w:.0f}" height="58" rx="12" fill="{t["mark"]}" transform="rotate(-1.5 80 {y})"/>')
        s.append(f'<text x="90" y="{y}" font-family="Jua" font-size="{size}" fill="#2b2b2b">{_esc(line)}</text>')
        y += size + 22
    if art in ARTS:
        s += ARTS[art]()
    else:
        s += _life_art(date_text or '') if track == 'life' else _chart_art()
    # 손글씨 메모
    s.append(f'<g transform="translate(90,{H-130}) rotate(-2)">'
             f'<path d="M0 62 Q 160 74 330 60" fill="none" stroke="{t["accent"]}" stroke-width="5" stroke-linecap="round"/>'
             f'<text x="0" y="44" font-family="Gaegu" font-weight="bold" font-size="54" fill="{t["accent"]}">{_esc(note)}</text></g>')
    s.append('<text x="1110" y="133" font-family="Jua" font-size="28" text-anchor="end" fill="#b8a98f">나도!지식 한입만</text>')
    s.append('</svg>')
    return '\n'.join(s)


def main():
    slug, title, track, note = sys.argv[1:5]
    date_text = sys.argv[5] if len(sys.argv) > 5 else ''
    art = sys.argv[6] if len(sys.argv) > 6 else ''
    _install_fonts()
    OUT.mkdir(parents=True, exist_ok=True)
    svg = OUT / f'{slug}.svg'
    svg.write_text(build_svg([p.strip() for p in title.split('|')], track, note, date_text, art), encoding='utf-8')
    subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(svg)], check=True)


if __name__ == '__main__':
    main()
