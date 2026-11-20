@echo off
chcp 65001 >nul
cd /d %~dp0
git -C .. pull >> logs\git.log 2>&1
python tistory_upload.py --mode private
