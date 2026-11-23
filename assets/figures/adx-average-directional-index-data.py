"""ADX 예시용 가정 일봉 데이터(실제 종목 아님). (날, 고가, 저가, 종가). 기간은 설명용으로 5일."""
N = 5
BARS = [('1일', 10100, 9900, 10000), ('2일', 10250, 10000, 10200), ('3일', 10400, 10150, 10350),
        ('4일', 10500, 10300, 10450), ('5일', 10450, 10250, 10300), ('6일', 10650, 10350, 10600),
        ('7일', 10800, 10550, 10750), ('8일', 10850, 10650, 10700), ('9일', 10750, 10500, 10550),
        ('10일', 10700, 10450, 10500), ('11일', 10600, 10350, 10400)]
def calc(bars=BARS, n=N):
    rows = []
    for i in range(1, len(bars)):
        _, h, l, _ = bars[i]; _, ph, pl, pc = bars[i-1]
        up, dn = h - ph, pl - l
        pdm = up if (up > dn and up > 0) else 0
        mdm = dn if (dn > up and dn > 0) else 0
        tr = max(h - l, abs(h - pc), abs(l - pc))
        rows.append([bars[i][0], tr, pdm, mdm])
    # Wilder 합 평활
    sm = []  # (day, TRn, +DMn, -DMn)
    t, p, m = (sum(r[k] for r in rows[:n]) for k in (1, 2, 3))
    sm.append((rows[n-1][0], t, p, m))
    for r in rows[n:]:
        t = t - t/n + r[1]; p = p - p/n + r[2]; m = m - m/n + r[3]
        sm.append((r[0], t, p, m))
    out = []
    for d, t, p, m in sm:
        pdi, mdi = 100*p/t, 100*m/t
        dx = 100*abs(pdi-mdi)/(pdi+mdi)
        out.append([d, t, p, m, pdi, mdi, dx])
    return rows, out
if __name__ == '__main__':
    rows, out = calc()
    for r in rows: print('raw', *r)
    for o in out: print('sm', o[0], *[round(x, 2) for x in o[1:]])
    dxs = [o[6] for o in out]
    adx = sum(dxs[:N])/N if len(dxs) >= N else None
    print('first ADX (avg first %d DX):' % N, adx)
    if len(dxs) > N:
        a = adx
        for d in dxs[N:]:
            a = (a*(N-1)+d)/N; print('next ADX', round(a, 2))
