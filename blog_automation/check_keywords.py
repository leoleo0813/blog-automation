"""키워드 후보들의 월간 검색량을 한 번에 조회해 게이트 1 통과 여부를 표로 출력한다.

제목을 확정하기 전에 후보 키워드를 일괄 검증하는 용도다 (지침: "제목과 슬러그는
게이트 1 통과 후 확정한다").

    python -m blog_automation.check_keywords "증권사 수수료 비교" "주식 매도 세금" ...

인자를 주지 않으면 stock_beginner_series.json의 candidates 목록을 조회한다.
"""
import json
import sys
import time
from pathlib import Path

from blog_automation import naver_keyword_tool
from blog_automation.fill_search_volume import _threshold_for

QUEUE_PATH = Path('stock_beginner_series.json')


def _candidates_from_queue():
    if not QUEUE_PATH.exists():
        return []
    data = json.loads(QUEUE_PATH.read_text(encoding='utf-8'))
    keywords = []
    for item in data.get('candidates', []) + data.get('items', []):
        kw = item.get('keyword') or item.get('title')
        if kw and kw not in keywords:
            keywords.append(kw)
    return keywords


def main():
    keywords = sys.argv[1:] or _candidates_from_queue()
    if not keywords:
        print("조회할 키워드가 없습니다.")
        return

    if not naver_keyword_tool.has_credentials():
        print("네이버 검색광고 시크릿 미설정 - 조회할 수 없습니다.")
        return

    print(f"{'키워드':<28} {'월간검색량':>10} {'PC':>7} {'모바일':>8} {'기준':>6} {'판정':>6}")
    print('-' * 74)

    for keyword in keywords:
        threshold, topic_kind = _threshold_for(keyword)
        try:
            result = naver_keyword_tool.lookup(keyword)
        except Exception as e:
            print(f"{keyword:<28} {'조회실패':>10}  ({e})")
            continue

        if not result:
            print(f"{keyword:<28} {'결과없음':>10}")
            continue

        verdict = 'PASS' if result['total'] >= threshold else 'FAIL'
        note = '' if result['matched'] else f"  ※유사어 '{result['keyword']}'"
        print(
            f"{keyword:<28} {result['total']:>10,} {result['pc']:>7,} "
            f"{result['mobile']:>8,} {threshold:>6} {verdict:>6}{note}"
        )
        time.sleep(0.3)  # API 호출 간격을 살짝 둔다


if __name__ == '__main__':
    main()
