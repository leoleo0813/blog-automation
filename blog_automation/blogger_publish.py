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

    Blogger는 URL을 "글 생성 시점의 제목"으로 한 번 고정하고 이후 제목을
    바꿔도 URL은 그대로 유지하는 특성이 있다. 이를 이용해 slug가 주어지면
    ① 슬러그 형태의 임시 제목으로 글을 만들어 원하는 URL을 확보한 뒤
    ② 곧바로 실제 제목으로 수정하는 2단계로 처리한다.

    검색 설명(meta description)은 Blogger API v3의 Post 리소스에 아예
    없는 필드라 API로는 반영할 수 없다 — 발행 후 화면에 출력되는 값을
    Blogger 관리 화면(게시물 설정 > 검색 설명)에 직접 붙여넣어야 한다.

    안전을 위해 기본값은 초안(is_draft=True)이다. 실제 자동 발행이
    확인되면 호출 시 is_draft=False로 넘긴다.
    """
    creds = _get_credentials()
    service = build('blogger', 'v3', credentials=creds)
    blog_id = os.environ['BLOGGER_BLOG_ID']

    insert_title = slug.replace('-', ' ') if slug else title
    body = {
        'title': insert_title,
        'content': content,
        'labels': labels,
    }
    response = service.posts().insert(
        blogId=blog_id,
        body=body,
        isDraft=is_draft,
    ).execute()

    if slug:
        response = service.posts().patch(
            blogId=blog_id,
            postId=response['id'],
            body={'title': title},
        ).execute()

    print(f"블로그스팟 자동 발행 완료! URL: {response.get('url')}")
    print(f"검색 설명(직접 입력 필요): {search_description}")
    return response
