"""최초 1회 실행해서 GOOGLE_REFRESH_TOKEN 값을 발급받는 스크립트.

브라우저가 열리는 로컬 환경에서 실행해야 한다:
    python blog_automation/get_refresh_token.py
"""
import os

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/blogger']


def main():
    client_config = {
        'installed': {
            'client_id': os.environ['GOOGLE_CLIENT_ID'],
            'client_secret': os.environ['GOOGLE_CLIENT_SECRET'],
            'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            'token_uri': 'https://oauth2.googleapis.com/token',
            'redirect_uris': ['http://localhost'],
        }
    }
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=0)

    print("\n아래 값을 .env 의 GOOGLE_REFRESH_TOKEN 에 저장하세요:\n")
    print(creds.refresh_token)


if __name__ == '__main__':
    main()
