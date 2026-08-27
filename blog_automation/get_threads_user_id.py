"""THREADS_USER_ID 값을 확인하는 스크립트.

.env 에 THREADS_ACCESS_TOKEN 을 먼저 채운 뒤 실행한다:
    python blog_automation/get_threads_user_id.py
"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()

GRAPH_API_BASE = "https://graph.threads.net/v1.0"


def main():
    access_token = os.environ['THREADS_ACCESS_TOKEN']
    resp = requests.get(
        f"{GRAPH_API_BASE}/me",
        params={'fields': 'id,username', 'access_token': access_token},
    )
    resp.raise_for_status()
    data = resp.json()

    print(f"username: {data.get('username')}")
    print("\n아래 값을 .env 의 THREADS_USER_ID 에 저장하세요:\n")
    print(data['id'])


if __name__ == '__main__':
    main()
