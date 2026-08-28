"""pending_posts/ 안의 JSON 파일을 읽어 Blogger에 발행한다.

GitHub Actions 워크플로(.github/workflows/publish-pending-post.yml)에서
호출한다:
    python blog_automation/run_pending_post.py pending_posts/<파일>.json
"""
import json
import os
import sys

from blog_automation.blogger_publish import post_to_blogger


def main():
    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    response = post_to_blogger(
        title=data['title'],
        content=data['content'],
        labels=data['labels'],
        search_description=data['search_description'],
        slug=data.get('slug'),
        is_draft=data.get('is_draft', True),
    )

    threads_hook = data.get('threads_hook', '')
    if threads_hook:
        print(f"\nThreads 훅 텍스트:\n{threads_hook}")

    _notify_kakao(data['title'], response.get('url', ''), data['search_description'], threads_hook)


def _notify_kakao(title, url, search_description, threads_hook):
    """카카오 시크릿이 설정되어 있으면 발행 요약을 '나에게 보내기'로 전송한다.

    아직 설정 전이라 실패하더라도 Blogger 발행 자체는 이미 끝난 뒤이므로
    카카오 전송 실패가 전체 작업 실패로 이어지지 않게 한다.
    """
    if not os.environ.get('KAKAO_REST_API_KEY') or not os.environ.get('KAKAO_REFRESH_TOKEN'):
        return

    from blog_automation.kakao_notify import send_kakao_message

    message = f"[블로그 초안 발행]\n제목: {title}\nURL: {url}\n\n검색 설명(수동 입력 필요):\n{search_description}"
    if threads_hook:
        message += f"\n\nThreads 훅:\n{threads_hook}"

    try:
        send_kakao_message(message)
    except Exception as e:
        print(f"카카오톡 알림 전송 실패 (Blogger 발행 자체는 성공): {e}")


if __name__ == '__main__':
    main()
