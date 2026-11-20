# AI 타워 PC 설치 (Windows · Mac)

7층 [기획 시작]을 누르면 이 PC의 Claude Code가 글 1편을 만들고, 끝나면 티스토리에 비공개로 올립니다.
Windows PC와 Mac 둘 다 같은 저장소를 쓰고, 서로 같은 글을 겹쳐 만들거나 올리지 않게 기록을 나눠 봅니다.

| | Windows (회사 PC) | Mac |
|---|---|---|
| 처음 준비 | `office\setup_windows.bat` 더블클릭 | `office/setup_mac.command` 더블클릭 |
| 타워 켜기 | `office\start_tower.bat` 더블클릭 | `office/start_tower.command` 더블클릭 |
| 파이썬 명령 | `python` | `python3` |

---

## Windows (이미 저장소·파이썬·업로더가 있는 PC)

1. `blog-automation` 폴더 주소창에 `cmd` → Enter → `git pull`
2. `office` 폴더의 **`setup_windows.bat`** 더블클릭 → 끝까지 기다리기(5~10분)
   - 마지막에 `준비 완료`가 보이면 그림 도구 준비가 끝난 것입니다.
   - Claude Code가 없으면 자동으로 설치합니다.
3. **Claude Code 로그인(한 번만)**: 새 검은 창을 열고 `claude` 입력 → Enter
   - 처음 화면에서 글자 색 등은 Enter로 넘기고, 로그인 방법은 **Claude 구독 계정(Pro)** 선택
   - 브라우저가 열리면 지금 쓰는 Claude 계정으로 로그인 → "로그인됨"이 보이면 검은 창에서 `/exit`
4. **`start_tower.bat`** 더블클릭 → 브라우저에 AI 타워(`http://127.0.0.1:8765`)가 열립니다.
   - 검은 창은 닫지 말고 최소화해 두세요(닫으면 타워가 꺼집니다).

## Mac (오늘 저녁)

1. **터미널** 열기(Spotlight에서 "터미널")
2. 저장소 받기:
   ```
   cd ~/Desktop
   git clone https://github.com/leoleo0813/blog-automation.git
   ```
   - "명령어 라인 개발자 도구를 설치하겠습니까?"가 뜨면 **설치** → 끝난 뒤 위 명령을 다시 입력
3. **GitHub 로그인(올리기 권한, 한 번만)**: https://cli.github.com 에서 Mac용 설치 파일(.pkg)을 받아 설치 → 터미널에서
   ```
   gh auth login
   gh auth setup-git
   ```
   - 질문에는 GitHub.com → HTTPS → Login with a web browser 순서로 고르고, 화면의 8자리 코드를 브라우저에 입력
4. Finder에서 바탕화면 `blog-automation/office/` → **`setup_mac.command`** 더블클릭
   - "확인되지 않은 개발자" 경고가 뜨면: 파일을 **마우스 오른쪽 → 열기 → 열기**
5. **Claude Code 로그인(한 번만)**: 터미널에서 `claude` → Pro 계정으로 로그인 → `/exit`
   - `claude`를 못 찾는다고 나오면 터미널을 껐다 켠 뒤 다시
6. **티스토리 로그인(한 번만)**: 터미널에서
   ```
   cd ~/Desktop/blog-automation/pc_uploader
   python3 tistory_upload.py --chrome
   ```
   → 새 크롬 창(업로드 전용)이 뜨면 그 창에서 티스토리에 직접 로그인. 이후로는 자동입니다.
7. **`start_tower.command`** 더블클릭 → 브라우저에 AI 타워가 열립니다.
   - Mac은 붙여넣기에 Cmd 키를 쓰도록 업로더가 알아서 바꿉니다.
   - 처음 실행 때 "터미널이 Chrome을 제어하려고 합니다" 같은 권한 창이 뜨면 **허용**

---

## 쓰는 법 (두 PC 같음)

1. 타워 화면에서 **7층 기획 칸**(점선 테두리)이나 오른쪽 **[7층 기획 시작]** 클릭
2. 주제를 적거나 비워 두고 **시작** → 층마다 불이 켜지며 20~40분 진행
   - 오른쪽 **제작 조종석**에 지금 하는 일이 한 줄씩 나옵니다.
3. 끝나면 업로드용 크롬이 떠서 티스토리에 **비공개**로 올립니다(이때는 마우스를 건드리지 마세요).
4. **방금 만든 글** 칸의 **[쓰레드 문구 복사]** → 쓰레드에 붙여넣기. 네이버 묶음은 `naver_packs/<글 주소>/` 폴더.
5. 티스토리 글 관리에서 비공개 글 확인 → 공개.

## 안전장치
- 하루 2편까지만 시작됩니다(두 PC 합계, 저장소 기록 기준).
- 한쪽 PC가 만드는 중이면 다른 PC의 시작 버튼이 "○○에서 제작 중"으로 막힙니다(2시간 지나면 풀림).
- 한쪽 PC가 올린 글은 다른 PC가 다시 올리지 않습니다(`office/uploaded.json`).
- 타워는 이 PC 안에서만 열립니다(다른 기기에서 접속 불가).
- Claude Code는 이 저장소 폴더 안에서 파일 편집·명령 실행·웹 검색만 하도록 허용해 두었습니다.
- Pro 사용량을 함께 씁니다. 한도에 걸리면 조종석에 오류가 나오고 그 편은 멈춥니다 — 다음 날 다시 누르면 됩니다.

## 멈췄을 때
- 조종석 기록 마지막 부분을 캡처해서 Claude 대화에 보내 주세요. 전체 기록은 `office/runs/` 폴더에 날짜별로 남습니다.
- 업로드만 실패했다면 원인을 고친 뒤 **[업로드만 다시]**.
