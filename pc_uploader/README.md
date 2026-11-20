# 티스토리 자동 업로드 (PC용)

클라우드에서 만든 글(저장소의 `stock_drafts/`)을 PC에서 티스토리에 올립니다.
썸네일을 본문 첫 줄에 넣고, 본문 그림(`assets/figures/`)은 티스토리에 직접 업로드한 그림으로 바꾼 뒤
**임시저장(draft)** 또는 **비공개 발행(private)** 합니다. 캐러셀 카드는 옆으로 넘기는 모양이 깨지지 않게 저장소 주소 그대로 둡니다.

> 네이버는 자동 업로드 대상이 아닙니다(자동 프로그램 게시 금지). 네이버 묶음은 지금처럼 직접 올려 주세요.

## 1. 처음 한 번 준비 (약 15분)

1. **파이썬 설치**: https://www.python.org/downloads/ → 설치 화면 맨 아래 **"Add python.exe to PATH" 체크** 후 설치
2. **Git 설치**: https://git-scm.com/download/win → 기본값으로 설치
3. **저장소 받기**: 바탕화면에서 마우스 오른쪽 → "Open Git Bash here" →
   `git clone https://github.com/leoleo0813/blog-automation.git`
   → 바탕화면에 `blog-automation` 폴더가 생깁니다.
   - 썸네일: `blog-automation\assets\thumbnails\`
   - 본문 그림: `blog-automation\assets\figures\`
   - 캐러셀: `blog-automation\assets\carousel\`
4. `blog-automation\pc_uploader\setup.bat` 더블클릭 → 열린 크롬 창에서 **티스토리에 직접 로그인** → 검은 창으로 돌아와 Enter
5. 이미 직접 올린 글은 자동 대상에서 빼기(검은 창에서):
   `python tistory_upload.py --mark-done national-scholarship-2027-first-application`

## 2. 시험해 보기 (임시저장)

`test_draft.bat` 더블클릭 → 다음 글 1편을 **임시저장**하고 창을 열어 둡니다.
티스토리 화면에서 확인할 것: 첫 줄 썸네일 / 그림 위치 / 표·캐러셀 / 제목·태그.
확인 후 검은 창에서 Enter → 창이 닫힙니다.

순서 보기: `python tistory_upload.py --list`

## 3. 자동 실행 (하루 2번, 비공개 발행)

시험이 잘 되면 Windows **작업 스케줄러**에 등록합니다.
1. 시작 메뉴 → "작업 스케줄러" → 오른쪽 **[기본 작업 만들기]**
2. 이름: `티스토리 업로드` → 트리거: **매일** → 시작 시간 **12:20**
3. 동작: **프로그램 시작** → 프로그램: `blog-automation\pc_uploader\run_private.bat` 선택
4. 같은 방법으로 **19:20** 작업을 하나 더 만듭니다(하루 2편).
5. PC가 켜져 있고 로그인된 상태여야 실행됩니다.

클라우드 제작은 매일 **10:41, 17:13(한국 시간)** 에 1편씩 저장소에 올라옵니다. 업로드는 그 뒤 시간에 맞춰 두었습니다.

## 4. 멈췄을 때

- `pc_uploader\logs\` 폴더에 단계별 화면(png)과 `upload.log`가 남습니다. **가장 최근 사진 2~3장을 Claude 대화에 보내 주세요.**
- "로그인이 풀렸어요" → `python tistory_upload.py --login` 으로 다시 로그인
- "본문이 N자뿐이에요" → 저장하지 않고 멈춘 것입니다(빈 글이 올라가지 않게). 사진을 보내 주세요.
- 비공개로 올라간 글은 티스토리 **관리 → 글 관리**에서 확인 후 공개로 바꿔 주세요.

## 안전 규칙

- 비밀번호는 이 프로그램이 저장하지 않습니다. 로그인 상태는 `pc_uploader\profile\` 폴더에만 남습니다(저장소에 올라가지 않음).
- 한 번 실행에 1편만 올립니다. 하루 2편보다 늘리지 마세요(스팸 판정 위험).
- 공개 전환은 사람이 직접 확인하고 합니다.
