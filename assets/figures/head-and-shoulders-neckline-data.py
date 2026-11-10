"""헤드앤숄더 예시용 가정 종가(실제 종목 아님)."""
PIVOTS = [(0, 10000, ''), (10, 11400, '왼어깨'), (17, 10800, '저점1'), (27, 12000, '머리'), (35, 10900, '저점2'),
          (43, 11450, '오른어깨'), (50, 10700, ''), (54, 10960, '되돌림'), (62, 10400, '')]
C = []
for (d0, p0, _), (d1, p1, _) in zip(PIVOTS, PIVOTS[1:]):
    for d in range(d0, d1):
        t = (d - d0) / (d1 - d0)
        near = min(abs(d - d0), abs(d - d1)) <= 1
        wob = 0 if near else (30 if d % 3 == 0 else -20 if d % 3 == 1 else 10)
        C.append(round((p0 + (p1 - p0) * t + wob) / 10) * 10)
C.append(PIVOTS[-1][1])
N = len(C)
T1, T2 = (17, 10800), (35, 10900)
SLOPE = (T2[1] - T1[1]) / (T2[0] - T1[0])
neck = lambda d: T1[1] + SLOPE * (d - T1[0])
if __name__ == '__main__':
    P = {n: (d, p) for d, p, n in PIVOTS if n}
    for d, p, n in PIVOTS: assert C[d] == p, (d, C[d], p)
    print('N', N, 'slope', round(SLOPE, 2))
    ls, hd, rs = P['왼어깨'][1], P['머리'][1], P['오른어깨'][1]
    print('head-LS', hd - ls, 'head-RS', hd - rs, 'shoulder diff %', round(abs(rs - ls) / ls * 100, 2))
    h = hd - neck(27); print('height', round(h), 'neck@27', round(neck(27)))
    brk = next(d for d in range(44, N) if C[d] < neck(d)); print('break', brk, C[brk], round(neck(brk)), round((C[brk] - neck(brk)) / neck(brk) * 100, 2))
    b1 = next(d for d in range(44, N) if C[d] < neck(d) * 0.99); print('break1%', b1, C[b1], round(neck(b1)))
    print('retest54', C[54], round(neck(54)), round((C[54]-neck(54))/neck(54)*100,2))
    print('measured', round(neck(brk) - h), 'min after', min(C[brk:]), 'last', C[-1])
