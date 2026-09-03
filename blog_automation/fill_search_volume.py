"""주식 초안(.md)의 게이트 1(월간 검색량)을 네이버 검색광고 API로 채운다.

초안 머리말의 `keyword`로 키워드도구를 조회해 `monthly_search_volume`과
`gate1_pass`를 채워 넣고, 같은 슬러그의 stock_beginner_series.json 항목도
갱신한다. 시크릿이 없거나 조회에 실패하면 아무 것도 바꾸지 않는다 —
`확인필요` 상태가 그대로 남으므로 사람이 수동으로 확인하면 된다.

임계값 (CLAUDE.md Section 7.2 게이트 1):
    일반 주제        월 500 이상
    세부·제도 주제   월 100 이상
제도·세금·한도성 키워드는 자동으로 세부 주제로 보고 100을 적용한다.

    python -m blog_automation.fill_search_volume stock_drafts/<slug>.md
"""
import json
import re
import sys
from pathlib import Path

from blog_automation import naver_keyword_tool

QUEUE_PATH = Path('stock_beginner_series.json')
DETAIL_TOPIC_HINTS = ('세금', '세율', '소득세', '양도소득', '공제', '한도', 'isa', '연금', '신고', '과세')

GENERAL_THRESHOLD = 500
DETAIL_THRESHOLD = 100


def _threshold_for(keyword):
    lowered = keyword.lower()
    if any(hint in lowered for hint in DETAIL_TOPIC_HINTS):
        return DETAIL_THRESHOLD, '세부·제도'
    return GENERAL_THRESHOLD, '일반'


def _read_field(text, key):
    match = re.search(rf'^{re.escape(key)}:\s*(.*)$', text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ''


def _set_field(text, key, value):
    """머리말의 key를 value로 바꾼다. 없으면 gate_pass 줄 앞에 새로 넣는다."""
    pattern = rf'^{re.escape(key)}:.*$'
    if re.search(pattern, text, flags=re.MULTILINE):
        return re.sub(pattern, f'{key}: {value}', text, count=1, flags=re.MULTILINE)
    return re.sub(r'^gate_pass:', f'{key}: {value}\ngate_pass:', text, count=1, flags=re.MULTILINE)


def _update_queue(slug, volume, gate1_pass):
    if not QUEUE_PATH.exists():
        return
    data = json.loads(QUEUE_PATH.read_text(encoding='utf-8'))
    changed = False
    for item in data.get('items', []):
        if item.get('slug') == slug:
            item['monthly_search_volume'] = volume
            item['gate1_pass'] = gate1_pass
            changed = True
    if changed:
        QUEUE_PATH.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
        )


def main():
    path = Path(sys.argv[1])
    if path.suffix != '.md':
        print(f"{path} 는 주식 초안(.md)이 아니므로 검색량 조회를 건너뜁니다.")
        return

    text = path.read_text(encoding='utf-8')
    keyword = _read_field(text, 'keyword')
    if not keyword:
        print("머리말에 keyword가 없어 검색량 조회를 건너뜁니다.")
        return

    if not naver_keyword_tool.has_credentials():
        print("네이버 검색광고 시크릿 미설정 - 검색량은 '확인필요'로 남겨둡니다.")
        return

    try:
        result = naver_keyword_tool.lookup(keyword)
    except Exception as e:
        print(f"검색량 조회 실패, '확인필요' 유지: {e}")
        return

    if not result:
        print(f"'{keyword}' 조회 결과가 비어 있어 '확인필요'로 남겨둡니다.")
        return

    threshold, topic_kind = _threshold_for(keyword)
    gate1_pass = result['total'] >= threshold

    volume_text = f"{result['total']} (PC {result['pc']} / 모바일 {result['mobile']})"
    if not result['matched']:
        volume_text += f" ※정확 일치 없음, 유사어 '{result['keyword']}' 기준"

    text = _set_field(text, 'monthly_search_volume', volume_text)
    text = _set_field(
        text, 'gate1_pass',
        f"{'true' if gate1_pass else 'false'} ({topic_kind} 주제 기준 월 {threshold} 이상 필요)",
    )
    path.write_text(text, encoding='utf-8')

    slug = _read_field(text, 'slug')
    if slug:
        _update_queue(slug, volume_text, gate1_pass)

    verdict = '통과' if gate1_pass else '미달 - 키워드 재선정 검토'
    print(f"게이트 1: {keyword} → 월 {result['total']}회 ({topic_kind}, 기준 {threshold}) → {verdict}")


if __name__ == '__main__':
    main()
