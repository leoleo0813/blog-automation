"""pending_posts/ 안의 JSON 파일을 읽어 Blogger에 발행한다.

GitHub Actions 워크플로(.github/workflows/publish-pending-post.yml)에서
호출한다:
    python blog_automation/run_pending_post.py pending_posts/<파일>.json
"""
import json
import sys

from blog_automation.blogger_publish import post_to_blogger


def main():
    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    post_to_blogger(
        title=data['title'],
        content=data['content'],
        labels=data['labels'],
        search_description=data['search_description'],
        slug=data.get('slug'),
        is_draft=data.get('is_draft', True),
    )


if __name__ == '__main__':
    main()
