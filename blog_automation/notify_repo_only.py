"""Blogger 발행 없이, 저장소에 새로 커밋된 콘텐츠를 카카오톡으로만 알린다.

두 종류의 입력을 받는다:
- `pending_posts/<slug>.json` — 일반 트렌드 모드 산출물 (Blogger 발행 대기 중)
- `stock_drafts/<slug>.md`     — 주식 모드 산출물 (티스토리 수동 발행용, YAML 머리말 포함)

어느 쪽이든 Blogger API는 전혀 호출하지 않고, 요약만 카카오톡 '나에게 보내기'로 보낸다.

GitHub Actions 워크플로(.github/workflows/notify-repo-only.yml)에서 호출:
    python -m blog_automation.notify_repo_only <파일 경로>
"""
import json
import os
import sys
from pathlib import Path

REPO_BLOB_BASE = 'https://github.com/leoleo0813/blog-automation/blob/main'
THUMBNAIL_CDN_BASE = 'https://cdn.jsdelivr.net/gh/leoleo0813/blog-automation@main/assets/thumbnails'


def _parse_front_matter(text):
    """--- 로 감싼 평평한 YAML 머리말을 dict로 읽는다 (pyyaml 의존성 없이).

    `key: value` 한 줄 필드와 `key: |` 블록 스칼라(다음 줄부터 들여쓰기된 줄을
    줄바꿈으로 이어붙인 값) 둘 다 지원한다. self_check/capture_guide처럼 여러
    줄로 쓰는 필드는 후자 형태라야 값이 제대로 채워진다.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    fields = {}
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.strip() == '---':
            break
        if ':' in line and not line.startswith((' ', '\t', '-')):
            key, _, value = line.partition(':')
            key, value = key.strip(), value.strip()
            if value == '|':
                block = []
                i += 1
                while i < len(lines) and (lines[i][:1] in (' ', '\t') or not lines[i].strip()):
                    if lines[i].strip() == '---':
                        break
                    block.append(lines[i].lstrip())
                    i += 1
                fields[key] = '\n'.join(block).strip()
                continue
            fields[key] = value
        i += 1
    return fields


def _build_json_message(data, file_url):
    message = f"[저장소 저장 완료 - Blogger 발행 보류]\n제목: {data['title']}"
    if data.get('slug'):
        message += f"\n슬러그: {data['slug']}"
    if data.get('search_description'):
        message += f"\n\n검색 설명:\n{data['search_description']}"
    if data.get('threads_hook'):
        message += f"\n\nThreads 훅:\n{data['threads_hook']}"
    if data.get('tistory_url'):
        message += f"\n\n티스토리 원고(복사해서 붙여넣기):\n{data['tistory_url']}"
    return message + f"\n\n저장소 파일(자세히 보기):\n{file_url}"


def _build_draft_message(fields, file_url):
    gate_pass = fields.get('gate_pass', 'false')
    header = "✅ 게이트 통과" if gate_pass.lower() == 'true' else "⏸ 게이트 미통과 - 발행 보류"

    message = f"[주식 초안 작성 완료 - 티스토리 수동 발행]\n{header}\n"

    # 캡처가 필요해 막힌 글은 "무엇을, 어디서, 어떻게" 캡처할지부터 맨 위에 보여준다.
    # 자체 점검 문구만으로는 사람이 뭘 해야 할지 알기 어려워서 별도 필드로 관리한다.
    if fields.get('gate_pass', 'false').lower() != 'true' and fields.get('capture_guide'):
        message += f"\n📋 지금 필요한 조치:\n{fields['capture_guide']}\n"

    message += f"\n제목: {fields.get('title', '(제목 없음)')}"
    if fields.get('keyword'):
        message += f"\n키워드: {fields['keyword']}"
    if fields.get('slug'):
        message += f"\n슬러그: {fields['slug']}"
    message += f"\n\n월간 검색량: {fields.get('monthly_search_volume', '확인필요')}"
    if fields.get('serp_check'):
        message += f"\n경쟁 강도: {fields['serp_check']}"
    if fields.get('unique_asset'):
        message += f"\n정보 이득: {fields['unique_asset']}"
    if fields.get('primary_source'):
        message += f"\n1차 출처: {fields['primary_source']}"
    if fields.get('self_check'):
        message += f"\n\n자체 점검: {fields['self_check']}"
    if fields.get('tags'):
        message += f"\n\n티스토리 태그:\n{fields['tags']}"

    message += "\n\n👉 네이버 검색광고 키워드도구로 검색량을 확인한 뒤 발행 여부를 판단하세요."
    return message + f"\n\n초안 파일(자세히 보기):\n{file_url}"


def _thumbnail_url(fields):
    """주식 초안의 slug에 해당하는 썸네일이 이미 저장소에 있으면 jsDelivr URL을 준다.

    (notify-repo-only.yml의 ensure_thumbnail 단계가 이 스크립트보다 먼저 실행되어
    커밋·푸시까지 마쳐 둔다는 전제. 파일이 없으면 None을 돌려주고 조용히 생략한다.)
    """
    slug = fields.get('slug')
    if not slug or not (Path('assets/thumbnails') / f"{slug}.png").exists():
        return None
    return f"{THUMBNAIL_CDN_BASE}/{slug}.png"


def main():
    path = sys.argv[1]
    file_url = f"{REPO_BLOB_BASE}/{path}"
    is_stock_draft = not path.endswith('.json')

    with open(path, encoding='utf-8') as f:
        raw = f.read()

    if path.endswith('.json'):
        fields = json.loads(raw)
        message = _build_json_message(fields, file_url)
    else:
        fields = _parse_front_matter(raw)
        message = _build_draft_message(fields, file_url)

    if not os.environ.get('KAKAO_REST_API_KEY') or not os.environ.get('KAKAO_REFRESH_TOKEN'):
        print("카카오 시크릿 미설정 - 알림 전송 생략")
        return

    from blog_automation.kakao_notify import send_kakao_feed_message, send_kakao_message

    # 썸네일 카드(feed)는 주식 초안(.md)에만 붙인다 - 일반 트렌드 모드(json)는 대상 아님.
    if is_stock_draft:
        thumb_url = _thumbnail_url(fields)
        if thumb_url:
            gate_pass = fields.get('gate_pass', 'false').lower() == 'true'
            status = "✅ 게이트 통과" if gate_pass else "⏸ 게이트 미통과 - 발행 보류"
            description = f"{status} · 검색량 {fields.get('monthly_search_volume', '확인필요')}"
            try:
                send_kakao_feed_message(
                    title=fields.get('title', '(제목 없음)'),
                    description=description,
                    image_url=thumb_url,
                    link_url=file_url,
                )
            except Exception as e:
                print(f"카카오톡 썸네일 카드 전송 실패: {e}")

    try:
        send_kakao_message(message, link_url=file_url)
    except Exception as e:
        print(f"카카오톡 알림 전송 실패: {e}")


if __name__ == '__main__':
    main()
