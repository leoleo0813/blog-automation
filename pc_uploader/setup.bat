@echo off
chcp 65001 >nul
cd /d %~dp0
echo [1/3] 파이썬 패키지 설치
python -m pip install --upgrade pip playwright
echo [2/3] 설정 파일 만들기
if not exist config.json copy config.example.json config.json
echo [3/3] 티스토리 로그인 (열린 창에서 직접 로그인)
python tistory_upload.py --login
echo 준비 끝. 시험: test_draft.bat
pause
