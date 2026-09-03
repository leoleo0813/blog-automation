"""1차 출처 페이지를 받아 텍스트로 저장한다 (게이트 4 근거 확보용).

콘텐츠 생성 샌드박스는 egress가 제한되어 국세청·금융투자협회 같은 1차 출처
도메인에 직접 접근할 수 없다. 그래서 네트워크가 열려 있는 GitHub Actions에서
원문을 받아 `sources/` 아래에 텍스트로 저장해 두고, 글을 쓰는 세션은 그 파일을
읽어 수치를 인용한다. 이렇게 해야 "원문에 없는 수치는 만들지 않는다"를 실제로
지킬 수 있다.

    python -m blog_automation.fetch_source <이름> <URL> [<URL> ...]

저장 위치: sources/<이름>.md (원문 URL과 수집 시각을 머리말에 남긴다)
"""
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests

KST = timezone(timedelta(hours=9))
OUT_DIR = Path('sources')
UA = 'Mozilla/5.0 (compatible; blog-automation/1.0; +https://github.com/leoleo0813/blog-automation)'

SCRIPT_STYLE = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.DOTALL | re.IGNORECASE)
TAG = re.compile(r'<[^>]+>')
BLANKS = re.compile(r'\n{3,}')


def _html_to_text(html):
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup(['script', 'style', 'noscript']):
            tag.decompose()
        text = soup.get_text('\n')
    except ImportError:
        text = TAG.sub('\n', SCRIPT_STYLE.sub('', html))

    lines = [line.strip() for line in text.splitlines()]
    return BLANKS.sub('\n\n', '\n'.join(line for line in lines if line))


def fetch(url):
    resp = requests.get(url, headers={'User-Agent': UA}, timeout=45)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or resp.encoding
    return _html_to_text(resp.text)


def main():
    name, urls = sys.argv[1], sys.argv[2:]
    if not urls:
        print("URL을 하나 이상 지정하세요.")
        return

    fetched_at = datetime.now(KST).strftime('%Y-%m-%d %H:%M KST')
    parts = [f"# 1차 출처 원문 수집: {name}\n", f"수집 시각: {fetched_at}\n"]

    for url in urls:
        parts.append(f"\n---\n\n## 출처: {url}\n")
        try:
            parts.append(fetch(url))
        except Exception as e:
            parts.append(f"[수집 실패] {e}")
            print(f"실패: {url} — {e}")
        else:
            print(f"수집: {url}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{name}.md"
    out_path.write_text('\n'.join(parts) + '\n', encoding='utf-8')
    print(f"저장: {out_path}")


if __name__ == '__main__':
    main()
