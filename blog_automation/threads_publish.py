import os

import requests
from dotenv import load_dotenv

load_dotenv()

GRAPH_API_BASE = "https://graph.threads.net/v1.0"


def post_to_threads(text):
    """Threads API로 짧은 훅 텍스트를 발행한다.

    미디어 컨테이너 생성(threads) -> 발행(threads_publish) 2단계로 이루어진다.
    """
    user_id = os.environ['THREADS_USER_ID']
    access_token = os.environ['THREADS_ACCESS_TOKEN']

    create_resp = requests.post(
        f"{GRAPH_API_BASE}/{user_id}/threads",
        data={
            'media_type': 'TEXT',
            'text': text,
            'access_token': access_token,
        },
    )
    create_resp.raise_for_status()
    creation_id = create_resp.json()['id']

    publish_resp = requests.post(
        f"{GRAPH_API_BASE}/{user_id}/threads_publish",
        data={
            'creation_id': creation_id,
            'access_token': access_token,
        },
    )
    publish_resp.raise_for_status()
    result = publish_resp.json()

    print(f"스레드 자동 발행 완료! ID: {result.get('id')}")
    return result
