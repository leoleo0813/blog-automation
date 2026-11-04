"""피보나치 되돌림 예시용 가정 종가(실제 종목 아님). 1~41일 10,000→14,000 상승, 59일까지 되돌림, 이후 반등."""
C = []
for i in range(41):  # 상승: 저점 10,000(1일) → 고점 14,000(41일)
    C.append(10000 + 100 * i + (0 if i in (0, 40) else (60 if i % 3 == 0 else -50 if i % 3 == 1 else 10)))
for i in range(1, 19):  # 되돌림: 59일 12,040
    C.append(14000 - 110 * i + (40 if i % 2 else -30) * (0 if i == 18 else 1))
b = C[-1]
for i in range(1, 17):  # 반등
    C.append(b + 90 * i + (35 if i % 2 else -35))
C = [round(x / 10) * 10 for x in C]
N = len(C)
HI, LO = max(C), min(C)
RATIOS = [0.236, 0.382, 0.5, 0.618, 0.786]
LEVELS = {r: HI - r * (HI - LO) for r in RATIOS}
if __name__ == '__main__':
    print(N, HI, C.index(HI) + 1, LO, C.index(LO) + 1)
    pull = min(C[C.index(HI):]); print('pullback low', pull, C.index(pull) + 1, 'retr%', round((HI - pull) / (HI - LO) * 100, 1))
    for r, v in LEVELS.items(): print(r, round(v))
    # 각 선 ±1% 띠가 상승폭(저점~고점)을 얼마나 덮나
    cover = set()
    for v in LEVELS.values():
        for p in range(LO, HI + 1, 10):
            if abs(p - v) <= v * 0.01: cover.add(p)
    print('cover', round(len(cover) / len(range(LO, HI + 1, 10)) * 100, 1))
    print(C)
