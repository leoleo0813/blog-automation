"""ATR 예시용 가정 고가·저가·종가(실제 종목 아님). 1~40일 잔잔, 41~80일 크게 출렁임(55일 갭 하락), 81~100일 다시 잔잔."""
H, L, C = [], [], []
c = 10000
for d in range(101):
    if d == 0:
        c = 10000; h, l = 10050, 9950
    elif d <= 40:                                  # 잔잔한 상승: 하루 폭 약 100원
        c = 10000 + 15 * d + (20 if d % 2 else -20)
        h, l = c + 50 + (d % 3) * 10, c - 50 - (d % 2) * 10
    elif d <= 80:                                  # 출렁임: 하루 폭 300~400원
        if d == 55:                                # 갭 하락: 전날 종가보다 고가가 낮음
            h, l, c = 10200, 10000, 10100
        else:
            base = 10600 - 10 * (d - 40)
            c = base + (180 if d % 2 else -180)
            h, l = c + 150 + (d % 3) * 30, c - 150 - (d % 2) * 40
    else:                                          # 다시 잔잔
        c = 10200 + 8 * (d - 80) + (15 if d % 2 else -15)
        h, l = c + 45 + (d % 3) * 10, c - 45 - (d % 2) * 10
    H.append(round(h)); L.append(round(l)); C.append(round(c))
N = len(C)
TR = [H[0] - L[0]] + [max(H[i] - L[i], abs(H[i] - C[i - 1]), abs(L[i] - C[i - 1])) for i in range(1, N)]
ATR = [None] * N
ATR[14] = sum(TR[1:15]) / 14
for i in range(15, N):
    ATR[i] = (ATR[i - 1] * 13 + TR[i]) / 14
if __name__ == '__main__':
    print('N', N)
    print('day1-3', [(H[i], L[i], C[i], TR[i]) for i in range(0, 4)])
    print('TR1..14', TR[1:15], 'ATR14', round(ATR[14], 1))
    print('day15', H[15], L[15], C[14], TR[15], round(ATR[15], 1))
    print('d54-56', [(i, H[i], L[i], C[i], TR[i]) for i in (54, 55, 56)])
    for d in (40, 54, 55, 60, 70, 80, 90, 100):
        print(d, C[d], round(ATR[d]), round(ATR[d] / C[d] * 100, 2), '%')
    print('max ATR', round(max(a for a in ATR if a)), ATR.index(max(a for a in ATR if a)))
