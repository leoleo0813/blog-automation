"""VWAP 예시용 가정 장중 데이터(실제 종목 아님). 30분마다 (시각, 가격, 거래량)."""
BARS = [('09:00', 10000, 50000), ('09:30', 10200, 20000), ('10:00', 10300, 10000),
        ('10:30', 10100, 15000), ('11:00', 9900, 80000), ('11:30', 10000, 25000)]
def table():
    pv = v = 0; rows = []
    for i, (t, p, q) in enumerate(BARS, 1):
        pv += p * q; v += q
        simple = sum(b[1] for b in BARS[:i]) / i
        rows.append((t, p, q, p * q, pv, v, pv / v, simple))
    return rows
if __name__ == '__main__':
    for r in table():
        print(r[0], r[1], r[2], r[3], r[4], r[5], round(r[6], 1), round(r[7], 1))
