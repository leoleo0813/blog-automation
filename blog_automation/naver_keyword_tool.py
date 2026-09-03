"""네이버 검색광고 API 키워드도구로 월간 검색량을 조회한다 (게이트 1 자동화).

필요한 시크릿 3개 (검색광고 > 도구 > API 사용 관리에서 발급):
    NAVER_AD_CUSTOMER_ID     고객 번호 (6~8자리 숫자)
    NAVER_AD_ACCESS_LICENSE  액세스 라이선스
    NAVER_AD_SECRET_KEY      비밀키 (서명용)

인증은 HMAC-SHA256 서명 방식이다:
    message   = "{밀리초 타임스탬프}.{HTTP메서드}.{URI}"
    signature = base64(HMAC-SHA256(message, secret_key))
헤더로 X-Timestamp / X-API-KEY / X-Customer / X-Signature 를 보낸다.
"""
import base64
import hashlib
import hmac
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.searchad.naver.com'
KEYWORD_URI = '/keywordstool'

CUSTOMER_ID_ENV = 'NAVER_AD_CUSTOMER_ID'
ACCESS_LICENSE_ENV = 'NAVER_AD_ACCESS_LICENSE'
SECRET_KEY_ENV = 'NAVER_AD_SECRET_KEY'


def _env(name):
    """시크릿에 딸려 들어온 공백·줄바꿈·따옴표를 제거한다.

    GitHub Secrets에 값을 붙여넣을 때 끝에 줄바꿈이 들어가거나 .env 형식의
    따옴표(KEY="값")가 그대로 복사되는 일이 잦다. 줄바꿈이 남아 있으면
    HTTP 헤더 값으로 쓸 수 없어 요청 자체가 실패한다.
    """
    return os.environ[name].strip().strip('"').strip("'").strip()


def _signature(timestamp, method, uri, secret_key):
    message = f"{timestamp}.{method}.{uri}"
    digest = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).digest()
    return base64.b64encode(digest).decode('utf-8')


def _headers(method, uri):
    timestamp = str(int(time.time() * 1000))
    return {
        'X-Timestamp': timestamp,
        'X-API-KEY': _env(ACCESS_LICENSE_ENV),
        'X-Customer': _env(CUSTOMER_ID_ENV),
        'X-Signature': _signature(timestamp, method, uri, _env(SECRET_KEY_ENV)),
    }


def _to_int(value):
    """검색량이 적으면 '< 10' 같은 문자열로 오므로 정수로 정규화한다."""
    if isinstance(value, int):
        return value
    text = str(value).replace('<', '').replace(',', '').strip()
    try:
        return int(text)
    except ValueError:
        return 0


def has_credentials():
    return all(os.environ.get(k) for k in (CUSTOMER_ID_ENV, ACCESS_LICENSE_ENV, SECRET_KEY_ENV))


def lookup(keyword):
    """키워드 하나의 월간 검색량을 조회한다.

    반환: {'keyword', 'pc', 'mobile', 'total', 'matched'} — matched는 API가
    돌려준 연관키워드 중 요청 키워드와 정확히 일치하는 항목을 찾았는지 여부.
    정확히 일치하는 항목이 없으면 가장 검색량이 큰 연관키워드를 대신 쓴다.
    """
    # API는 공백을 무시하므로 붙여서 조회하는 편이 정확도가 높다.
    hint = keyword.replace(' ', '')
    resp = requests.get(
        BASE_URL + KEYWORD_URI,
        params={'hintKeywords': hint, 'showDetail': '1'},
        headers=_headers('GET', KEYWORD_URI),
        timeout=30,
    )
    resp.raise_for_status()
    rows = resp.json().get('keywordList', [])
    if not rows:
        return None

    exact = next((r for r in rows if r.get('relKeyword', '').replace(' ', '') == hint), None)
    row = exact or max(rows, key=lambda r: _to_int(r.get('monthlyPcQcCnt')) + _to_int(r.get('monthlyMobileQcCnt')))

    pc = _to_int(row.get('monthlyPcQcCnt'))
    mobile = _to_int(row.get('monthlyMobileQcCnt'))
    return {
        'keyword': row.get('relKeyword', hint),
        'pc': pc,
        'mobile': mobile,
        'total': pc + mobile,
        'matched': exact is not None,
    }


if __name__ == '__main__':
    import sys
    result = lookup(sys.argv[1])
    print(result)
