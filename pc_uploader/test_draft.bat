@echo off
chcp 65001 >nul
cd /d %~dp0
git -C .. pull
python tistory_upload.py --mode draft --keep-open
pause
