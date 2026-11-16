"""도지캔들 예시용 가정 캔들(실제 종목 아님). (이름, 시가, 고가, 저가, 종가)"""
CANDLES = [
    ('A', 10000, 10200, 9800, 10010),   # 십자형
    ('B', 10000, 10010, 9600, 10000),   # 잠자리형
    ('C', 10000, 10400, 9990, 9995),    # 비석형
    ('D', 10000, 10500, 9500, 10020),   # 긴 다리
    ('E', 10000, 10150, 9850, 10025),   # 경계(기준 따라 갈림)
    ('F', 10000, 10300, 9950, 10250),   # 일반 양봉
    ('G', 10000, 10020, 9990, 10010),   # 몸통 10원인데 하루 폭이 작은 날
]
def stats(o, h, l, c):
    rng = h - l; body = abs(c - o)
    return dict(range=rng, body=body, ratio=body / rng * 100, upper=h - max(o, c), lower=min(o, c) - l)
if __name__ == '__main__':
    for n, o, h, l, c in CANDLES:
        s = stats(o, h, l, c)
        print(n, s['range'], s['body'], round(s['ratio'], 1), s['upper'], s['lower'], round(s['upper'] / s['range'] * 100, 1), round(s['lower'] / s['range'] * 100, 1),
              '5%:', s['ratio'] <= 5, '10%:', s['ratio'] <= 10)
