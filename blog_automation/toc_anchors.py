"""초안 목차(<h2>목차</h2> 다음 <ol>)의 항목을 해당 본문 H2로 이동하는 링크로 바꾼다.

2026-10-02 사용자 요청("목차를 누르면 그 본문으로 이동")으로 추가. 각 H2에 id="sec-N"을
붙이고 목차 항목을 <a href="#sec-N">으로 감싼다. 여러 번 실행해도 결과가 같다(기존 sec-N
링크와 id를 지우고 다시 만든다). front matter와 JSON-LD는 건드리지 않는다.

    python -m blog_automation.toc_anchors stock_drafts/<slug>.md [...]
"""
import re
import sys

TOC_RE = re.compile(r'(<h2[^>]*>\s*목차\s*</h2>\s*<ol[^>]*>)(.*?)(</ol>)', re.S)
LINK_STYLE = 'color:inherit;text-decoration:underline;text-underline-offset:3px;'


def _text(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html)).strip()


def _words(t):
    return set(re.findall(r'[0-9A-Za-z가-힣]+', t))


def link_toc(body):
    """body(HTML)의 목차를 본문 H2 링크로 바꾼다. (새 body, 못 찾은 목차 항목 목록)을 돌려준다."""
    # 이전 실행 흔적 제거
    body = re.sub(r'(<h2[^>]*?) id="sec-\d+"', r'\1', body)
    body = body.replace('scroll-margin-top:72px;', '')
    m = TOC_RE.search(body)
    if not m:
        return body, ['(목차 없음)']
    toc_inner = re.sub(r'<a href="#sec-\d+"[^>]*>(.*?)</a>', r'\1', m.group(2), flags=re.S)

    h2s = [(hm.start(), hm.group(0), _text(hm.group(1)))
           for hm in re.finditer(r'<h2[^>]*>(.*?)</h2>', body, re.S)]
    h2s = [h for h in h2s if h[2] != '목차']

    items = re.findall(r'<li([^>]*)>(.*?)</li>', toc_inner, re.S)
    used, targets, missing = set(), [], []
    for _, inner in items:
        t = _text(inner)
        cand = [h for h in h2s if h[2] == t and h[0] not in used]
        if not cand:  # 목차가 제목을 줄여 쓴 경우: 겹치는 단어가 가장 많은 H2(2개 이상 겹칠 때만)
            scored = sorted(((len(_words(t) & _words(h[2])), h) for h in h2s if h[0] not in used),
                            key=lambda x: -x[0])
            cand = [scored[0][1]] if scored and scored[0][0] >= 2 else []
        if cand:
            used.add(cand[0][0])
            targets.append(cand[0])
        else:
            targets.append(None)
            missing.append(t)

    # 목차 항목 링크화
    new_items, k = [], 0
    id_for = {}
    for (attrs, inner), tgt in zip(items, targets):
        if tgt is None:
            new_items.append(f'<li{attrs}>{inner}</li>')
            continue
        k += 1
        id_for[tgt[0]] = f'sec-{k}'
        new_items.append(f'<li{attrs}><a href="#sec-{k}" style="{LINK_STYLE}">{inner.strip()}</a></li>')
    new_toc = '\n  ' + '\n  '.join(new_items) + '\n'

    # H2에 id 부여(뒤에서부터 바꿔 위치가 밀리지 않게)
    for pos, tag, _ in sorted(h2s, key=lambda h: -h[0]):
        if pos not in id_for:
            continue
        new_tag = tag.replace('<h2', f'<h2 id="{id_for[pos]}"', 1)
        if 'style="' in new_tag:
            new_tag = new_tag.replace('style="', 'style="scroll-margin-top:72px;', 1)
        body = body[:pos] + new_tag + body[pos + len(tag):]

    m = TOC_RE.search(body)
    body = body[:m.start(2)] + new_toc + body[m.end(2):]
    return body, missing


def main():
    failed = False
    for path in sys.argv[1:]:
        src = open(path, encoding='utf-8').read()
        head, fm, rest = src.split('---', 2)
        ld_at = rest.find('<script type="application/ld+json">')
        body, ld = (rest, '') if ld_at < 0 else (rest[:ld_at], rest[ld_at:])
        new_body, missing = link_toc(body)
        open(path, 'w', encoding='utf-8').write(head + '---' + fm + '---' + new_body + ld)
        if missing:
            failed = True
            print(f'{path}: 본문 H2를 못 찾은 목차 항목 {missing}')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
