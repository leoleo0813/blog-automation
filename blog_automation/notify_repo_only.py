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

REPO_BLOB_BASE = 'https://github.com/leoleo0813/blog-automation/blob/main'


def _parse_front_matter(text):
    """--- 로 감싼 평평한 YAML 머리말을 dict로 읽는다 (pyyaml 의존성 없이)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if ':' in line and not line.startswith((' ', '\t', '-')):
            key, _, value = line.partition(':')
            fields[key.strip()] = value.strip()
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


def main():
    path = sys.argv[1]
    file_url = f"{REPO_BLOB_BASE}/{path}"

    with open(path, encoding='utf-8') as f:
        raw = f.read()

    if path.endswith('.json'):
        message = _build_json_message(json.loads(raw), file_url)
    else:
        message = _build_draft_message(_parse_front_matter(raw), file_url)

    if not os.environ.get('KAKAO_REST_API_KEY') or not os.environ.get('KAKAO_REFRESH_TOKEN'):
        print("카카오 시크릿 미설정 - 알림 전송 생략")
        return

    from blog_automation.kakao_notify import send_kakao_message
    try:
        send_kakao_message(message, link_url=file_url)
    except Exception as e:
        print(f"카카오톡 알림 전송 실패: {e}")


if __name__ == '__main__':
    main()
