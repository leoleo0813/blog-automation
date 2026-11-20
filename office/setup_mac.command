#!/bin/bash
# AI 타워 준비 (Mac) — 더블클릭해서 실행
cd "$(dirname "$0")/.."
echo "===== AI 타워 준비 (Mac) ====="
echo "[1/5] 파이썬 패키지"
python3 -m pip install --user --upgrade pip
python3 -m pip install --user playwright pillow imageio-ffmpeg requests beautifulsoup4
echo "[2/5] 그림 도구(글꼴 내려받기 + 시험 그림)"
python3 -m blog_automation.render_env --setup
echo "[3/5] 업로더 설정"
[ -f pc_uploader/config.json ] || cp pc_uploader/config.example.json pc_uploader/config.json
echo "[4/5] git 서명(이 저장소에서만)"
git config user.name >/dev/null || git config user.name "AI Tower (Mac)"
git config user.email >/dev/null || git config user.email "tower-mac@users.noreply.github.com"
echo "[5/5] Claude Code 확인"
if command -v claude >/dev/null || [ -x "$HOME/.local/bin/claude" ]; then echo "Claude Code 있음"
else echo "Claude Code 설치 중..."; curl -fsSL https://claude.ai/install.sh | bash; fi
echo
echo "다음: 터미널에서 claude 를 한 번 실행해 로그인하세요(SETUP.md 3단계)."
read -p "Enter를 누르면 닫혀요..."
