@echo off
chcp 65001 >nul
cd /d %~dp0
rem 사람이 직접 로그인하는 '일반 크롬'을 연다. 업로드 프로그램은 이 창에 연결만 한다.
set CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
if not exist %CHROME% set CHROME="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
if not exist %CHROME% set CHROME="%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
start "" %CHROME% --remote-debugging-port=9222 --user-data-dir="%~dp0chrome-profile" https://www.tistory.com/auth/login
