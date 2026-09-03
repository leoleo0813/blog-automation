import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

REST_API_KEY_ENV = 'KAKAO_REST_API_KEY'
REFRESH_TOKEN_ENV = 'KAKAO_REFRESH_TOKEN'
TOKEN_URL = 'https://kauth.kakao.com/oauth/token'
SEND_URL = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'


def _env(name):
    """시크릿에 딸려 들어온 공백·줄바꿈·따옴표를 제거한다.

    GitHub Secrets 등록 시 값 끝에 줄바꿈이 붙거나 .env 형식의 따옴표
    (KEY="값")가 그대로 복사되는 일이 잦아, 인증이 조용히 실패한다.
    """
    return os.environ[name].strip().strip('"').strip("'").strip()


def _get_access_token():
    resp = requests.post(TOKEN_URL, data={
        'grant_type': 'refresh_token',
        'client_id': _env(REST_API_KEY_ENV),
        'refresh_token': _env(REFRESH_TOKEN_ENV),
    })
    resp.raise_for_status()
    return resp.json()['access_token']


def send_kakao_message(text, link_url=''):
    """카카오톡 '나에게 보내기'로 텍스트 메시지를 전송한다.

    link_url을 넘기면 메시지의 '자세히 보기' 버튼이 그 URL로 이동한다.
    """
    access_token = _get_access_token()
    template_object = {
        'object_type': 'text',
        'text': text,
        'link': {'web_url': link_url, 'mobile_web_url': link_url},
    }
    resp = requests.post(
        SEND_URL,
        headers={'Authorization': f'Bearer {access_token}'},
        data={'template_object': json.dumps(template_object, ensure_ascii=False)},
    )
    resp.raise_for_status()
    print("카카오톡 알림 전송 완료!")
    return resp.json()
