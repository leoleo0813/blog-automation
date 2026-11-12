"""이격도 예시용 가정 종가(실제 종목 아님). 1~40일 옆걸음(약 10,000원), 41~70일 강한 상승, 71~85일 급락, 86~100일 다시 옆걸음."""
C = []
for d in range(101):
    if d <= 40:
        c = 10000 + (40 if d % 2 else -40) + (d % 5) * 5
    elif d <= 70:
        c = 10000 + 60 * (d - 40) + ((d % 3) - 1) * 40
    elif d <= 85:
        c = 11800 - 110 * (d - 70) + (25 if d % 2 else -25)
    else:
        c = 10150 + 5 * (d - 85) + (35 if d % 2 else -35)
    C.append(round(c))
N = len(C)
def ma(n, i):
    return sum(C[i - n + 1:i + 1]) / n if i >= n - 1 else None
MA20 = [ma(20, i) for i in range(N)]
DISP = [None if m is None else C[i] / m * 100 for i, m in enumerate(MA20)]
if __name__ == '__main__':
    for d in (20, 40, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100):
        print(d, C[d], round(MA20[d]), round(DISP[d], 1), 'ma5', round(ma(5, d)), round(C[d]/ma(5,d)*100,1), 'ma60', ma(60,d) and round(ma(60, d)), ma(60,d) and round(C[d]/ma(60,d)*100,1))
    above = [i for i in range(N) if DISP[i] and DISP[i] >= 105]
    below = [i for i in range(N) if DISP[i] and DISP[i] <= 95]
    print('>=105', above[:1], above[-1:], len(above), ' <=95', below[:1], below[-1:], len(below))
    print('max', round(max(x for x in DISP if x), 1), DISP.index(max(x for x in DISP if x)), 'min', round(min(x for x in DISP if x), 1), DISP.index(min(x for x in DISP if x)))
    print('C at 70', C[70], 'peak', max(C), C.index(max(C)))
    print('win 41..60 closes', C[41:61], sum(C[41:61]))
