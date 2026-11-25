"""글마다 구조·양식·글씨체를 무작위로 바꾸는 '스타일 주사위' — 2026-11-25 사용자 요청
"계속 똑같은 양식과 폼으로 제작된다. AI티가 난다. 랜덤 시스템으로 본문 글의 구조, 양식, 글씨체 등 변경".

    python -m blog_automation.style_dice <slug>          # office/work/<slug>-style.md 에 이번 글 설계서를 쓴다
    python -m blog_automation.style_dice <slug> --show   # 화면에만 보여 주기

규칙(lint)은 그대로 지킨다: 질문형 소제목 2개 이상, 소제목 바로 아래 결론 <p>, 정의 문장, 3,500자 이상,
'함께 보면 좋은 글'. 그 안에서 순서·도입·상자 모양·소제목 모양·마무리·글꼴·색·그림 종류를 고른다.
직전 3편과 같은 조합은 피한다(office/style_history.json, 여러 PC 공통).
"""
import json
import random
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HIST = ROOT / 'office' / 'style_history.json'
OUT = ROOT / 'office' / 'work'

DICE = {
    'intro': [
        ('질문형', '독자가 지금 궁금해할 질문 2개로 시작하고, 3줄 안에 답(핵심 숫자)을 준다.'),
        ('사례형', '"월급 300만원 직장인 A씨는…"처럼 구체적인 한 사람의 상황으로 시작한다(가상 인물은 가상이라고 밝힌다).'),
        ('숫자형', '첫 문장을 핵심 숫자 하나로 시작한다(예: "1,000만원까지 17%"). 다음 문장에서 그 숫자의 뜻을 푼다.'),
        ('실수형', '"많이들 여기서 손해를 봐요"처럼 흔한 실수 하나로 시작해 이 글로 피하는 법을 약속한다.'),
        ('대화형', '짧은 문답 2~3줄(Q/A 또는 따옴표 대화)로 시작한다.'),
    ],
    'flow': [
        ('결론 먼저', '핵심 요약 → 조건 → 계산 → 신청·방법 → 실수 → Q&A'),
        ('단계 따라가기', '준비물 → 1단계 → 2단계 → 3단계 → 결과 확인 → 실수 → Q&A'),
        ('비교 중심', '두세 가지 경우 비교표 → 경우별 설명 → 내 경우 고르기 → 실수 → Q&A'),
        ('질문 사다리', '질문형 소제목 5~6개를 쉬운 질문에서 어려운 질문 순으로 이어 간다(각 소제목 아래 바로 답)'),
        ('사례 3개', '서로 다른 세 사람의 사례를 계산해 보며 규칙을 설명 → 정리표 → 실수 → Q&A'),
    ],
    'heading': [
        ('질문 위주', '소제목 대부분 질문형(예: "얼마 받나요?").'),
        ('번호+질문', '"1. 누가 받나요?"처럼 번호를 붙인 질문형과 번호 붙인 설명형을 섞는다(질문형 2개 이상).'),
        ('키워드+질문', '짧은 키워드형 소제목(예: "신청 기간")과 질문형을 번갈아 쓴다(질문형 2개 이상).'),
    ],
    'box': [
        ('왼쪽 줄 상자', '<div style="border-left:5px solid {c1};background:{bg};padding:12px 16px;margin:16px 0;">'),
        ('둥근 상자', '<div style="border:2px solid {c1};border-radius:14px;padding:14px 18px;margin:16px 0;">'),
        ('점선 메모', '<div style="border:2px dashed {c1};background:{bg};padding:12px 16px;margin:16px 0;">'),
        ('제목 띠 상자', '<div style="border:1px solid {c1};margin:16px 0;"><div style="background:{c1};color:#fff;font-weight:700;padding:6px 14px;">제목</div><div style="padding:12px 16px;">내용</div></div>'),
        ('그림자 카드', '<div style="background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.08);border-radius:10px;padding:14px 18px;margin:16px 0;">'),
    ],
    'palette': [
        ('바다', {'c1': '#1f6feb', 'bg': '#eef5ff', 'mark': '#fff3a3', 'h2': '#163d7a'}),
        ('숲', {'c1': '#1e8a5a', 'bg': '#ecf8f1', 'mark': '#fff1a8', 'h2': '#145c3c'}),
        ('노을', {'c1': '#e0662f', 'bg': '#fff2ea', 'mark': '#ffe58a', 'h2': '#8a3412'}),
        ('보라', {'c1': '#7b4bc4', 'bg': '#f4eefc', 'mark': '#fff3a3', 'h2': '#4b2a80'}),
        ('먹색', {'c1': '#3b4250', 'bg': '#f2f3f5', 'mark': '#ffe9a6', 'h2': '#20242c'}),
    ],
    # 티스토리 에디터 글꼴 메뉴에 있는 글꼴(블로그에서 불러옴). 본문 전체가 아니라 소제목·상자 제목에만 쓴다.
    'font': [
        ('기본(스킨 글꼴)', ''),
        ('나눔고딕', "'Nanum Gothic', sans-serif"),
        ('나눔명조', "'Nanum Myeongjo', serif"),
        ('본고딕', "'Noto Sans KR', sans-serif"),
        ('본명조', "'Noto Serif KR', serif"),
    ],
    'list_style': [
        ('표 위주', '숫자 비교는 표로, 절차는 번호 목록으로.'),
        ('목록 위주', '표는 1개만, 나머지는 짧은 글머리표 목록으로.'),
        ('문단 위주', '표 1개 + 문단 설명 위주(문단은 2~3문장으로 짧게).'),
    ],
    'ending': [
        ('체크리스트', '마지막에 "오늘 할 일" 체크리스트 4~5개.'),
        ('한 줄 정리', '소제목별 한 줄 정리 목록.'),
        ('요약표', '조건·금액·기한을 한 표로 정리.'),
        ('다음 단계', '"이 글 다음에 할 일" 3단계와 관련 글 안내.'),
    ],
    'qa': [3, 4, 5, 6],
    'figures': [
        ('막대+비교+단계', ['bars', 'compare', 'steps']),
        ('비교+막대', ['compare', 'bars']),
        ('단계+막대+비교', ['steps', 'bars', 'compare']),
        ('막대+단계', ['bars', 'steps']),
        ('비교+단계+막대', ['compare', 'steps', 'bars']),
    ],
    'tone': [
        ('다정한 해요체', '해요체, 짧은 문장, 독자를 "~하신 분"으로.'),
        ('담백한 설명체', '해요체지만 감탄·이모지 없이 사실 위주.'),
        ('옆자리 선배', '해요체, 경험담 같은 말투("저도 처음엔 헷갈렸어요" 같은 표현 1~2번).'),
    ],
}


def _hist():
    try:
        return json.loads(HIST.read_text(encoding='utf-8'))
    except Exception:
        return []


def roll(slug, seed=None):
    rnd = random.Random(seed if seed is not None else f'{slug}-{datetime.now().isoformat()}')
    recent = _hist()[-3:]
    pick = {}
    for k, opts in DICE.items():
        used = [h.get(k) for h in recent]
        names = [o[0] if isinstance(o, tuple) else o for o in opts]
        fresh = [o for o, n in zip(opts, names) if n not in used] or opts   # 직전 3편과 다른 것
        pick[k] = rnd.choice(fresh)
    return pick


def brief(slug, pick):
    pal = pick['palette'][1]
    box = pick['box'][1].format(**pal)
    font = pick['font'][1]
    fstyle = f'font-family:{font};' if font else ''
    return f"""# {slug} 이번 글 설계서 (스타일 주사위)

작가·디자이너는 이 설계서를 그대로 따른다. 규칙(질문형 소제목 2개 이상, 소제목 바로 아래 결론 문장, 정의 문장, 3,500자 이상,
'함께 보면 좋은 글', 강조는 span)은 항상 지킨다. 예전 글과 같은 순서·같은 상자·같은 마무리를 그대로 베끼지 않는다.

| 항목 | 이번 선택 | 쓰는 법 |
|---|---|---|
| 도입 | {pick['intro'][0]} | {pick['intro'][1]} |
| 흐름 | {pick['flow'][0]} | {pick['flow'][1]} |
| 소제목 | {pick['heading'][0]} | {pick['heading'][1]} |
| 말투 | {pick['tone'][0]} | {pick['tone'][1]} |
| 표·목록 | {pick['list_style'][0]} | {pick['list_style'][1]} |
| 마무리 | {pick['ending'][0]} | {pick['ending'][1]} |
| Q&A | {pick['qa']}개 | |
| 색 | {pick['palette'][0]} | 주색 {pal['c1']}, 배경 {pal['bg']}, 소제목 글자색 {pal['h2']}, 강조 형광 {pal['mark']} |
| 글꼴 | {pick['font'][0]} | 소제목·상자 제목에만 적용 |
| 그림 | {pick['figures'][0]} | pop_style: {', '.join(pick['figures'][1])} 순서(그림 수 = 이 개수) |

## 그대로 붙여 쓰는 코드
- 소제목: `<h2 style="color:{pal['h2']};{fstyle}">…</h2>`
- 강조: `<span style="background-color:{pal['mark']};padding:0 2px;">…</span>`
- 상자({pick['box'][0]}): `{box}` … `</div>`
"""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    slug = sys.argv[1]
    pick = roll(slug)
    text = brief(slug, pick)
    if '--show' in sys.argv:
        print(text)
        return
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f'{slug}-style.md').write_text(text, encoding='utf-8')
    h = _hist()
    h.append({'slug': slug, 'at': datetime.now().isoformat(timespec='minutes'),
              **{k: (v[0] if isinstance(v, tuple) else v) for k, v in pick.items()}})
    HIST.parent.mkdir(parents=True, exist_ok=True)
    HIST.write_text(json.dumps(h[-30:], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
