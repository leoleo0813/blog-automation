"""추세선 예시용 가정 종가(실제 종목 아님). 5일·25일 저점을 이은 상승 추세선, 45일 재접촉, 59일 첫 이탈."""
PIVOTS = [(0, 10300), (5, 10000), (15, 10900), (25, 10800), (35, 11900), (45, 11580), (53, 12600), (60, 11950), (66, 11700)]
C = []
for (d0, p0), (d1, p1) in zip(PIVOTS, PIVOTS[1:]):
    for d in range(d0, d1):
        t = (d - d0) / (d1 - d0)
        near = min(abs(d - d0), abs(d - d1)) <= 2
        wob = 0 if near else (30 if d % 3 == 0 else -20 if d % 3 == 1 else 10)
        C.append(round((p0 + (p1 - p0) * t + wob) / 10) * 10)
C.append(PIVOTS[-1][1])
N = len(C)
A, B = (5, 10000), (25, 10800)
SLOPE = (B[1] - A[1]) / (B[0] - A[0])            # 하루 40원
line = lambda d: A[1] + SLOPE * (d - A[0])
G = (B[1] / A[1]) ** (1 / (B[0] - A[0]))          # 로그(비율) 추세선: 하루 0.386%
logline = lambda d: A[1] * G ** (d - A[0])
if __name__ == '__main__':
    print('N', N, 'slope', SLOPE, 'daily% log', round((G - 1) * 100, 3))
    print('d45 line', line(45), 'close', C[45], 'gap%', round((C[45] - line(45)) / line(45) * 100, 2))
    first = next(d for d in range(46, N) if C[d] < line(d))
    print('first close below', first, C[first], round(line(first)), 'gap%', round((C[first] - line(first)) / line(first) * 100, 2))
    print('d60 line', line(60), 'close', C[60], round((C[60] - line(60)) / line(60) * 100, 2), 'log', round(logline(60)), round(logline(45)))
    print('below before 46?', [d for d in range(6, 45) if C[d] < line(d) - 0.5 and d not in (25,)])
    print('d80 proj', line(80), round(logline(80)))
