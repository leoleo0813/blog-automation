"""Blogger 발행 없이, 저장소에 새로 커밋된 콘텐츠를 카카오톡으로만 알린다.

Blogger 자동 발행이 일시중단된 동안 사용한다 — Blogger API는 전혀
호출하지 않고, pending_posts/<slug>.json의 내용을 요약해 카카오톡
'나에게 보내기'로만 보낸다.

GitHub Actions 워크플로(.github/workflows/notify-repo-only.yml)에서 호출:
    python -m blog_automation.notify_repo_only pending_posts/<파일>.json
"""
import json
import os
import sys

REPO_BLOB_BASE = 'https://github.com/leoleo0813/blog-automation/blob/main'


def main():
    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    pending_url = f"{REPO_BLOB_BASE}/{path}"

    message = f"[저장소 저장 완료 - Blogger 발행 보류]\n제목: {data['title']}"
    slug = data.get('slug', '')
    if slug:
        message += f"\n슬러그: {slug}"

    search_description = data.get('search_description', '')
    if search_description:
        message += f"\n\n검색 설명:\n{search_description}"

    threads_hook = data.get('threads_hook', '')
    if threads_hook:
        message += f"\n\nThreads 훅:\n{threads_hook}"

    tistory_url = data.get('tistory_url', '')
    if tistory_url:
        message += f"\n\n티스토리 원고(복사해서 붙여넣기):\n{tistory_url}"

    message += f"\n\n저장소 파일(자세히 보기):\n{pending_url}"

    if not os.environ.get('KAKAO_REST_API_KEY') or not os.environ.get('KAKAO_REFRESH_TOKEN'):
        print("카카오 시크릿 미설정 - 알림 전송 생략")
        return

    from blog_automation.kakao_notify import send_kakao_message
    try:
        send_kakao_message(message, link_url=pending_url)
    except Exception as e:
        print(f"카카오톡 알림 전송 실패: {e}")


if __name__ == '__main__':
    main()
