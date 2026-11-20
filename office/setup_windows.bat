@echo off
chcp 65001 >nul
cd /d %~dp0..
echo ===== AI 타워 준비 (Windows) =====
echo [1/5] 파이썬 패키지
python -m pip install --upgrade pip
python -m pip install playwright pillow imageio-ffmpeg requests beautifulsoup4
echo [2/5] 그림 도구(글꼴 내려받기 + 시험 그림)
python -m blog_automation.render_env --setup
echo [3/5] 업로더 설정
if not exist pc_uploader\config.json copy pc_uploader\config.example.json pc_uploader\config.json
echo [4/5] git 서명(이 저장소에서만)
git config user.name >nul 2>&1 || git config user.name "AI Tower (Windows)"
git config user.email >nul 2>&1 || git config user.email "tower-windows@users.noreply.github.com"
echo [5/5] Claude Code 확인
where claude >nul 2>&1
if errorlevel 1 (
  if exist "%USERPROFILE%\.local\bin\claude.exe" (echo Claude Code 있음) else (
    echo Claude Code가 없어서 설치합니다...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://claude.ai/install.ps1 | iex"
  )
) else (echo Claude Code 있음)
echo.
echo 다음: 새 검은 창에서 claude 를 한 번 실행해 로그인하세요(SETUP.md 3단계).
pause
