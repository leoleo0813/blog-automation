#!/bin/bash
# Mac: 더블클릭하면 AI 타워가 열린다. 이 창을 닫으면 타워가 꺼진다.
cd "$(dirname "$0")/.."
echo "최신 내용 받는 중..."
git pull --rebase --autostash
python3 office/server.py
