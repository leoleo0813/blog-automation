"""엔벨로프 예시용 가정 종가(실제 종목 아님). 1~40일 잔잔한 옆걸음, 41~65일 꾸준한 상승, 66~100일 크게 출렁임, 101~120일 하락."""
import math
C = []
for d in range(121):
    if d <= 40:
        c = 10000 + 60 * math.sin(d / 2.2)
    elif d <= 65:
        c = 10000 + 95 * (d - 40) + 40 * math.sin(d / 1.7)
    elif d <= 100:
        c = 12375 + 700 * math.sin((d - 65) / 3.2) - 10 * (d - 65)
    else:
        c = C[100] - 120 * (d - 100) + 50 * math.sin(d / 1.5)
    C.append(round(c / 10) * 10)
N = len(C)
def ma(i, n=20):
    return sum(C[i - n + 1:i + 1]) / n if i >= n - 1 else None
def sd(i, n=20):
    m = ma(i, n); return (sum((x - m) ** 2 for x in C[i - n + 1:i + 1]) / n) ** 0.5
MA = [ma(i) for i in range(N)]
def env(k):
    return [None if m is None else m * (1 + k / 100) for m in MA], [None if m is None else m * (1 - k / 100) for m in MA]
def count(k, lo=19, hi=N):
    up, dn = env(k)
    a = sum(1 for i in range(lo, hi) if C[i] > up[i]); b = sum(1 for i in range(lo, hi) if C[i] < dn[i])
    return a, b
if __name__ == '__main__':
    print('C sample', C[0], C[40], C[65], C[80], C[100], C[120], 'max', max(C), C.index(max(C)), 'min after 65', min(C[65:]), C.index(min(C[65:])))
    for k in (2.5, 6, 10):
        print('k', k, 'all', count(k), 'calm19-40', count(k, 19, 41), 'rally41-65', count(k, 41, 66), 'chop66-100', count(k, 66, 101), 'fall', count(k, 101, 121))
    for d in (30, 60, 80, 90, 110):
        m = MA[d]; s = sd(d)
        print(d, C[d], round(m), 'env6', round(m * 1.06), round(m * 0.94), 'bb', round(m + 2 * s), round(m - 2 * s), 'bbw%', round(4 * s / m * 100, 1), 'disp', round(C[d] / m * 100, 1))
    print('win 41..60 sum', sum(C[41:61]), 'ma60', MA[60])
    up, dn = env(6)
    outs = [i for i in range(19, N) if C[i] > up[i] or C[i] < dn[i]]
    print('outs6', outs)
