"""박진영 자기관리 루틴 포스트를 발행하는 스크립트.

    python blog_automation/publish_park_jinyoung.py
"""
from blog_automation.blogger_publish import post_to_blogger

TITLE = "자기관리 끝판왕 박진영, 20년째 지킨 아침 루틴의 비밀"

CONTENT = """
<p>가수 겸 프로듀서로 활동 중인 박진영이 54세의 나이에도 20년 넘게 한결같은 아침 루틴을 지켜오고 있어 화제다. 최근 방송을 통해 공개된 그의 하루는 철저한 자기관리의 표본으로 꼽힌다.</p>

<h2>20년째 이어온 철벽 아침 루틴</h2>
<p>박진영의 하루는 영단어 암기와 신문 읽기로 시작된다. 이후 정성껏 차린 아침 식사를 마치고 반려견 호두를 돌본 뒤, 90분간의 운동과 보컬 연습으로 이어진다.</p>

<h3>유기농으로 채운 아침 식단</h3>
<div style="background:#f5f5f5;border-left:4px solid #4CAF50;padding:12px 16px;margin:16px 0;">
<strong>박진영의 아침 식단 구성</strong>
<ul>
<li>올리브유</li>
<li>꿀에 절인 마늘과 무</li>
<li>그릭 요거트</li>
<li>견과류</li>
<li>제철 과일</li>
<li>당근 주스</li>
</ul>
</div>
<p>박진영은 한 매체와의 인터뷰에서 "건강한 것 중에 맛있는 것을 찾고 찾는다"며 "20년째 같은 원칙으로 먹고 있다"고 밝혔다. 식재료는 모두 유기농을 고집하며, 치약이나 샴푸 같은 생활용품까지 유기농 인증 제품만 사용한다고 한다.</p>

<h2>운동과 보컬 연습, 그리고 효율적인 생활 철학</h2>
<p>아침 식사 이후에는 90분간의 운동과 보컬 연습이 쉼 없이 이어진다. 데뷔 30년이 넘은 지금까지도 몸 상태와 컨디션을 최상으로 유지하기 위한 노력이다.</p>

<h3>준비 시간을 줄이는 효율 중심 생활</h3>
<p>박진영은 계절마다 단 두 벌의 옷만 입고, 직접 만든 '인공 가르마'로 스타일링 시간을 줄이는 등 불필요한 시간 소모를 최소화하는 생활을 실천하고 있다. 이러한 습관은 그가 오랜 시간 왕성하게 활동할 수 있는 원동력으로 꼽힌다.</p>

<p><strong>Tip.</strong> 박진영처럼 매일 90분씩 운동하기는 어렵더라도, 아침에 견과류와 제철 과일 등 간단한 건강식을 챙기는 것만으로도 하루를 활기차게 시작하는 데 도움이 될 수 있다.</p>

<h2>영상으로 보는 박진영의 모닝 루틴</h2>
<iframe width="560" height="315" src="https://www.youtube.com/embed/g3KAQPQi51U" title="박진영 모닝 루틴" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<p>20년 넘게 한결같이 이어온 박진영의 자기관리 루틴은 거창한 비법보다는 꾸준함에서 나온다는 것을 보여준다. 오늘 아침, 나만의 작은 루틴 하나를 시작해보는 건 어떨까.</p>
""".strip()

LABELS = ["박진영", "자기관리", "모닝루틴"]

SEARCH_DESCRIPTION = (
    "가수 겸 프로듀서 박진영이 20년째 지켜온 유기농 아침 식단과 90분 운동 루틴을 공개했다. "
    "자기관리 끝판왕이라 불리는 그의 하루 루틴과 생활 철학을 정리했다."
)

SLUG = "park-jin-young-morning-routine-secret"

# Threads용 짧은 훅 텍스트 (참고용 — Threads 연동 완료 후 별도로 발행)
THREADS_HOOK = (
    "54세 박진영이 20년째 하루도 안 거른 루틴 🌱\n"
    "영단어 암기 → 신문 → 유기농 아침밥 → 90분 운동.\n"
    "'건강한 것 중 맛있는 것'만 골라 먹는다는 그의 아침 식탁, 궁금하지 않으세요?\n"
    "자세한 이야기는 블로그에서 👇"
)

if __name__ == '__main__':
    post_to_blogger(
        title=TITLE,
        content=CONTENT,
        labels=LABELS,
        search_description=SEARCH_DESCRIPTION,
        slug=SLUG,
    )
    print("\n[Threads 훅 텍스트 (참고용)]\n" + THREADS_HOOK)
