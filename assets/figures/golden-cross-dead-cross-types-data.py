from hub_data import C,N,sma,ema
s5,s20,s60=sma(C,5),sma(C,20),sma(C,60)
e12,e26=ema(C,12),ema(C,26)
def crosses(a,b):
    out=[]
    for i in range(1,N):
        if None in (a[i],b[i],a[i-1],b[i-1]): continue
        if a[i-1]<=b[i-1] and a[i]>b[i]: out.append((i+1,'G'))
        if a[i-1]>=b[i-1] and a[i]<b[i]: out.append((i+1,'D'))
    return out
PAIRS={'5·20일':(s5,s20),'20·60일':(s20,s60),'12·26일 EMA(MACD 0선)':(e12,e26)}
if __name__=='__main__':
    for k,(a,b) in PAIRS.items():
        cr=crosses(a,b); print(k,cr)
        for d,t in cr:
            after=[C[j] for j in range(d-1,min(d-1+20,N))]
            print('  ',d,t,C[d-1],'20일 뒤' ,C[min(d-1+20,N-1)], '최대',max(after),'최소',min(after))
    print('s60 starts', next(i for i,v in enumerate(s60) if v is not None)+1)
