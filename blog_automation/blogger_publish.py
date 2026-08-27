import os

from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/blogger']
TOKEN_URI = 'https://oauth2.googleapis.com/token'


def _get_credentials():
    return Credentials(
        token=None,
        refresh_token=os.environ['GOOGLE_REFRESH_TOKEN'],
        client_id=os.environ['GOOGLE_CLIENT_ID'],
        client_secret=os.environ['GOOGLE_CLIENT_SECRET'],
        token_uri=TOKEN_URI,
        scopes=SCOPES,
    )


def post_to_blogger(title, content, labels, search_description, slug=None, is_draft=True):
    """Blogger API v3로 글을 발행한다.

    Blogger API v3의 Post 리소스에는 검색 설명(meta description) 필드가
    없어 search_description은 API로 반영되지 않는다 — 발행 후 Blogger
    관리 화면에서 수동으로 입력해야 한다. slug 역시 공식 지원 필드가
    아니라 url에 실어 보내는 비공식적인 방식이라 Blogger가 무시할 수 있다.

    안전을 위해 기본값은 초안(is_draft=True)이다. 실제 자동 발행이
    확인되면 호출 시 is_draft=False로 넘긴다.
    """
    creds = _get_credentials()
    service = build('blogger', 'v3', credentials=creds)
    blog_id = os.environ['BLOGGER_BLOG_ID']

    body = {
        'title': title,
        'content': content,
        'labels': labels,
    }
    if slug:
        blog = service.blogs().get(blogId=blog_id).execute()
        body['url'] = f"{blog['url'].rstrip('/')}/{slug}.html"

    response = service.posts().insert(
        blogId=blog_id,
        body=body,
        isDraft=is_draft,
    ).execute()

    print(f"블로그스팟 자동 발행 완료! URL: {response.get('url')}")
    return response
