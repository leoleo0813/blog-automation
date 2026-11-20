@echo off
chcp 65001 >nul
cd /d %~dp0
if not exist logs mkdir logs
call start_chrome.bat
timeout /t 8 >nul
git -C .. pull >> logs\git.log 2>&1
python tistory_upload.py --mode private
