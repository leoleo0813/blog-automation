"""카카오 '나에게 보내기' 권한의 refresh token을 발급받는 스크립트.

.env 에 KAKAO_REST_API_KEY 를 먼저 채운 뒤 로컬에서 실행한다:
    python blog_automation/get_kakao_token.py
"""
import os
import urllib.parse
import webbrowser

import requests
from dotenv import load_dotenv

load_dotenv()

REST_API_KEY = os.environ['KAKAO_REST_API_KEY']
REDIRECT_URI = 'http://localhost:5000'
AUTH_URL = 'https://kauth.kakao.com/oauth/authorize'
TOKEN_URL = 'https://kauth.kakao.com/oauth/token'


def main():
    params = {
        'client_id': REST_API_KEY,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': 'talk_message',
    }
    auth_link = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    print(f"브라우저에서 아래 링크를 열어 로그인 및 동의하세요:\n{auth_link}\n")
    webbrowser.open(auth_link)

    print("로그인/동의 후 브라우저가 'localhost에서 연결을 거부했습니다' 같은 에러 페이지로 이동합니다.")
    print("그래도 정상입니다 — 그 페이지의 주소창 URL 전체를 복사해서 붙여넣으세요.")
    redirected = input("리디렉션된 URL: ").strip()
    code = urllib.parse.parse_qs(urllib.parse.urlparse(redirected).query)['code'][0]

    resp = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'client_id': REST_API_KEY,
        'redirect_uri': REDIRECT_URI,
        'code': code,
    })
    resp.raise_for_status()
    tokens = resp.json()

    print("\n아래 값을 .env 의 KAKAO_REFRESH_TOKEN 에 저장하세요:\n")
    print(tokens['refresh_token'])


if __name__ == '__main__':
    main()
