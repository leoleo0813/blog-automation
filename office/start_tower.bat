@echo off
chcp 65001 >nul
cd /d %~dp0..
title AI 타워 (이 창을 닫으면 타워가 꺼져요)
echo 최신 내용 받는 중...
git pull --rebase --autostash
python office\server.py
pause
