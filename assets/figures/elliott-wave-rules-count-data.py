"""엘리어트 파동 예시용 가정 종가(실제 종목 아님). 꼭짓점 사이를 직선으로 잇고 작은 흔들림을 더했다."""
PIVOTS = [  # (일, 가격, 이름)
    (0, 10000, '0'), (12, 11200, '1'), (20, 10500, '2'), (40, 12900, '3'),
    (50, 12100, '4'), (60, 13000, '5'), (70, 12300, 'A'), (76, 12700, 'B'), (90, 11800, 'C'),
]
C = []
for (d0, p0, _), (d1, p1, _) in zip(PIVOTS, PIVOTS[1:]):
    for d in range(d0, d1):
        t = (d - d0) / (d1 - d0)
        wob = 0 if d == d0 else (40 if d % 3 == 0 else -30 if d % 3 == 1 else 10)
        C.append(round((p0 + (p1 - p0) * t + wob) / 10) * 10)
C.append(PIVOTS[-1][1])
N = len(C)
if __name__ == '__main__':
    P = {n: p for _, p, n in PIVOTS}
    w1, w3, w5 = P['1'] - P['0'], P['3'] - P['2'], P['5'] - P['4']
    print('N', N, 'w1 w3 w5', w1, w3, w5)
    print('rule1 W2>W0', P['2'] > P['0'], 'retr2 %', round((P['1'] - P['2']) / w1 * 100, 1))
    print('rule2 w3 not shortest', w3 > min(w1, w5), 'w3/w1', w3 / w1)
    print('rule3 W4>W1', P['4'] > P['1'], 'retr4 %', round((P['3'] - P['4']) / w3 * 100, 1))
    print('w5/w1', round(w5 / w1, 3), 'A-C', P['5'] - P['C'], 'C retr of 0-5 %', round((P['5'] - P['C']) / (P['5'] - P['0']) * 100, 1))
    # 피크·바닥이 데이터에서 실제로 극값인지
    for d, p, n in PIVOTS: assert C[d] == p, (d, C[d], p)
