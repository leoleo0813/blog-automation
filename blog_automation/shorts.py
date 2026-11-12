"""유튜브 쇼츠 전용 세로 영상(1080x1920). 2026-11-12 사용자 요청 "쇼츠 전용으로 만들어줘".

블로그 카드를 이어 붙인 영상은 쇼츠에서 약하다(소리 없음·첫 장면이 제목·같은 길이 반복). 그래서 쇼츠는
  - 첫 장면에 결론 숫자(훅), 장면마다 길이를 다르게(핵심 숫자는 길게), 천천히 확대되는 움직임,
  - 검은 바탕·아주 큰 글자·노란 강조(작은 화면에서 읽히게), 쇼츠 화면 가림 영역(위 220px·아래 480px·오른쪽 150px) 비움.
소리는 넣지 않는다 — 사용자가 유튜브 앱 [사운드 추가]에서 오디오 보관함 음악을 고른다(저작권 안전).

    from blog_automation.shorts import make_shorts
    make_shorts(out_mp4, scenes, frame_dir)

scene: dict(sec=초, kicker='작은 윗글', lines=[(글, 크기, 색키)], foot='아래 작은 글')
  색키: 'w'(흰), 'y'(노랑 강조), 'g'(회색), 'm'(노랑 형광 띠 위 검은 글)
"""
import subprocess
import sys
from pathlib import Path

from blog_automation.make_illustrated_thumbnail import _install_fonts, _esc

W, H = 1080, 1920
BG, WHITE, YEL, GRAY = '#111111', '#ffffff', '#ffd23f', '#9a9a9a'
FONT = 'Noto Sans CJK KR'
TOP, BOTTOM, RIGHT = 260, 1440, 930   # 글자를 둘 안전 영역(쇼츠 UI 피함)


def _w(text, size):
    return sum(size * (0.6 if ord(ch) < 128 else 1.0) for ch in str(text))


def scene_svg(sc, i, n):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']
    # 진행 막대(몇 번째 장면인지)
    for k in range(n):
        x = 70 + k * (W - 140) / n
        s.append(f'<rect x="{x + 4:.0f}" y="{TOP - 60}" width="{(W - 140) / n - 8:.0f}" height="8" rx="4" '
                 f'fill="{YEL if k <= i else "#333"}"/>')
    lines = sc['lines']
    total = sum(sz * 1.28 for _, sz, _ in lines)
    y = (TOP + BOTTOM) / 2 - total / 2 + (60 if sc.get('kicker') else 0)
    if sc.get('kicker'):
        s.append(f'<text x="80" y="{y - 70:.0f}" font-family="{FONT}" font-size="46" font-weight="700" fill="{YEL}">{_esc(sc["kicker"])}</text>')
    for text, sz, ck in lines:
        y += sz * 1.12
        if ck == 'm':
            w = min(_w(text, sz), RIGHT - 80)
            s.append(f'<rect x="66" y="{y - sz * 0.92:.0f}" width="{w + 30:.0f}" height="{sz * 1.18:.0f}" rx="10" fill="{YEL}"/>')
        fill = {'w': WHITE, 'y': YEL, 'g': GRAY, 'm': BG}[ck]
        s.append(f'<text x="80" y="{y:.0f}" font-family="{FONT}" font-size="{sz}" font-weight="900" fill="{fill}">{_esc(text)}</text>')
        y += sz * 0.16
    if sc.get('foot'):
        s.append(f'<text x="80" y="{BOTTOM:.0f}" font-family="{FONT}" font-size="34" font-weight="500" fill="{GRAY}">{_esc(sc["foot"])}</text>')
    s.append('</svg>')
    return '\n'.join(s)


def make_shorts(out_mp4, scenes, frame_dir, fade=0.35, fps=30):
    _install_fonts()
    fd = Path(frame_dir)
    fd.mkdir(parents=True, exist_ok=True)
    pngs = []
    for i, sc in enumerate(scenes):
        p = fd / f'scene-{i + 1:02d}.svg'
        p.write_text(scene_svg(sc, i, len(scenes)), encoding='utf-8')
        subprocess.run([sys.executable, '-m', 'blog_automation.make_figure', str(p)], check=True, capture_output=True)
        p.unlink()
        pngs.append(p.with_suffix('.png'))
    inputs, filters = [], []
    for i, (p, sc) in enumerate(zip(pngs, scenes)):
        d = sc['sec']
        nf = int(d * fps)
        inputs += ['-loop', '1', '-framerate', str(fps), '-t', f'{d}', '-i', str(p)]
        # 천천히 3% 확대(정지 화면보다 덜 넘겨짐)
        filters.append(f'[{i}:v]scale=2160:3840,zoompan=z=\'1+0.03*on/{nf}\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':'
                       f'd=1:s={W}x{H}:fps={fps},setsar=1,format=yuv420p,trim=duration={d}[v{i}]')
    last, t = 'v0', scenes[0]['sec']
    for i in range(1, len(scenes)):
        filters.append(f'[{last}][v{i}]xfade=transition=fade:duration={fade}:offset={t - fade:.2f}[x{i}]')
        last, t = f'x{i}', t - fade + scenes[i]['sec']
    Path(out_mp4).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inputs, '-filter_complex', ';'.join(filters),
                    '-map', f'[{last}]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', str(fps),
                    '-movflags', '+faststart', str(out_mp4)], check=True)
    return str(out_mp4), round(t, 2)
