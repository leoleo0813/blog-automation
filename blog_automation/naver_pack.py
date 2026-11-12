"""네이버 블로그 병행용 묶음(원고 HTML + 요약 영상). 2026-11-11 사용자 요청.

네이버 블로그는 HTML 붙여넣기가 안 되고 글쓰기 API도 없어서, 사용자가 미리보기 HTML을 브라우저에서 열어
전체 복사 → 스마트에디터에 붙여 넣고, 그림·영상은 [여기에 ○○ 넣기] 자리에 직접 올린다.
같은 글 복사는 중복 문서가 되므로 원고는 티스토리 글과 구조·문장을 다르게 쓴다(RULES 「네이버 병행」).

    from blog_automation.naver_pack import make_video, naver_html
    make_video(slug, out_mp4, theme='forest')     # assets/carousel/<slug>-NN.png → 세로 요약 영상
    naver_html(title, blocks, out_html)           # 복사용 미리보기 HTML

2026-11-12 사용자 결정: 네이버용 그림·캐러셀은 티스토리와 같은 파일을 쓰지 않는다(RULES 「네이버 병행」 1-1).
그림·캐러셀은 blog_automation/naver_style.py(공책 형식, 캐릭터 없음, 정사각형)로 <slug>-naver-N.png·<slug>-naver-NN.png를
저장소 밖(채팅 전달 폴더)에 만들고, 영상은 make_video(f'{slug}-naver', ..., card_dir=그 폴더)로 만든다.

blocks: [('p', 글), ('h', 소제목), ('q', 인용구/핵심 한 줄), ('ul', [항목...]), ('table', [[머리...], [행...], ...]),
         ('img', 파일명, 설명), ('video', 파일명), ('hr',)]
"""
import subprocess
import tempfile
from pathlib import Path

from blog_automation.make_illustrated_thumbnail import _esc
from blog_automation.pop_style import THEMES

CAROUSEL = Path('assets/carousel')


def make_video(slug, out_mp4, theme='navy', sec=3.5, fade=0.5, card_dir=CAROUSEL, bg=None):
    """캐러셀 카드(1080x1350)를 9:16(1080x1920) 세로 영상으로. 카드마다 sec초, 사이는 fade초 겹쳐 넘김. 소리 없음.
    card_dir: 네이버 전용 카드(저장소 밖)를 쓸 때 그 폴더."""
    cards = sorted(Path(card_dir).glob(f'{slug}-[0-9][0-9].png'))
    if not cards:
        raise FileNotFoundError(f'캐러셀 카드 없음: {slug}')
    bg = (bg or THEMES.get(theme, THEMES['navy'])[0]).lstrip('#')
    inputs, filters = [], []
    for i, c in enumerate(cards):
        inputs += ['-loop', '1', '-t', str(sec), '-i', str(c)]
        filters.append(f'[{i}:v]scale=1080:-2,pad=1080:1920:0:(oh-ih)/2:color=0x{bg},setsar=1,fps=30,format=yuv420p[v{i}]')
    last = 'v0'
    for i in range(1, len(cards)):
        off = i * (sec - fade)
        filters.append(f'[{last}][v{i}]xfade=transition=slideleft:duration={fade}:offset={off:.2f}[x{i}]')
        last = f'x{i}'
    Path(out_mp4).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inputs, '-filter_complex', ';'.join(filters),
                    '-map', f'[{last}]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out_mp4)],
                   check=True)
    return str(out_mp4)


def naver_html(title, blocks, out_html, tags=()):
    """브라우저에서 열어 전체 복사 → 네이버 스마트에디터에 붙여 넣는 미리보기. 그림·영상 자리는 노란 상자로 표시."""
    s = ['<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{_esc(title)}</title>',
         '<style>body{font-family:"Noto Sans KR",sans-serif;max-width:720px;margin:0 auto;padding:16px;line-height:1.9;font-size:17px;color:#222}'
         'h1{font-size:24px}h2{font-size:21px;margin-top:36px}blockquote{border-left:5px solid #03c75a;margin:18px 0;padding:6px 14px;background:#f3fbf6;font-weight:bold}'
         'table{border-collapse:collapse;width:100%;margin:14px 0}th,td{border:1px solid #ccc;padding:8px;text-align:center}th{background:#f1f3f5}'
         '.slot{background:#fff7cc;border:2px dashed #e0a800;padding:10px 14px;margin:16px 0;font-size:15px;color:#7a5b00}'
         '.note{background:#eef3ff;padding:10px 14px;font-size:14px;color:#334;margin-bottom:20px}</style></head><body>',
         '<div class="note">📋 이 화면에서 <b>제목 아래부터 끝까지</b> 드래그해 복사 → 네이버 블로그 글쓰기에 붙여 넣으세요. '
         '노란 상자 자리에는 그 파일을 직접 올리고, 노란 상자 글자는 지워 주세요.</div>',
         f'<h1>{_esc(title)}</h1>']
    for b in blocks:
        k = b[0]
        if k == 'p':
            s.append(f'<p>{b[1]}</p>')
        elif k == 'h':
            s.append(f'<h2>{_esc(b[1])}</h2>')
        elif k == 'q':
            s.append(f'<blockquote>{b[1]}</blockquote>')
        elif k == 'ul':
            s.append('<ul>' + ''.join(f'<li>{x}</li>' for x in b[1]) + '</ul>')
        elif k == 'table':
            head, *rows = b[1]
            s.append('<table><tr>' + ''.join(f'<th>{_esc(h)}</th>' for h in head) + '</tr>'
                     + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>')
        elif k == 'img':
            s.append(f'<div class="slot">🖼 여기에 그림 넣기: <b>{_esc(b[1])}</b> — {_esc(b[2])}</div>')
        elif k == 'video':
            s.append(f'<div class="slot">🎬 여기에 영상 넣기: <b>{_esc(b[1])}</b> (글쓰기 화면의 [동영상] 버튼으로 올리기)</div>')
        elif k == 'hr':
            s.append('<hr>')
    if tags:
        s.append('<div class="slot">🏷 태그(글쓰기 화면 아래 태그 칸에 입력): ' + ' '.join('#' + t for t in tags) + '</div>')
    s.append('</body></html>')
    Path(out_html).parent.mkdir(parents=True, exist_ok=True)
    Path(out_html).write_text('\n'.join(s), encoding='utf-8')
    return str(out_html)
