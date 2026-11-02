# 같은 폴더의 ichimoku-cloud-calculation-data.py를 ichimoku_cloud_calculation_data.py 이름으로 복사해 import해서 실행
from ichimoku_cloud_calculation_data import C,H,L,N,tenkan,kijun,spanA,spanB
import statistics as st
def sma(xs,n): return [None if i<n-1 else sum(xs[i-n+1:i+1])/n for i in range(len(xs))]
def ema(xs,n):
    a=2/(n+1); out=[None]*len(xs); out[n-1]=sum(xs[:n])/n
    for i in range(n,len(xs)): out[i]=out[i-1]+a*(xs[i]-out[i-1])
    return out
s20=sma(C,20); s5=sma(C,5)
sd=[None if i<19 else st.pstdev(C[i-19:i+1]) for i in range(N)]
up=[None if s is None else m+2*s for m,s in zip(s20,sd)]; dn=[None if s is None else m-2*s for m,s in zip(s20,sd)]
# RSI 14 (Wilder)
ch=[0]+[C[i]-C[i-1] for i in range(1,N)]
rsi=[None]*N
g=sum(max(c,0) for c in ch[1:15])/14; l=sum(max(-c,0) for c in ch[1:15])/14
rsi[14]=100 - 100/(1+g/l) if l else 100
for i in range(15,N):
    g=(g*13+max(ch[i],0))/14; l=(l*13+max(-ch[i],0))/14
    rsi[i]=100-100/(1+g/l) if l else 100
e12,e26=ema(C,12),ema(C,26); macd=[None if a is None or b is None else a-b for a,b in zip(e12,e26)]
st0=next(i for i,v in enumerate(macd) if v is not None); sig=[None]*st0+ema(macd[st0:],9)
if __name__=='__main__':
    for i in range(55,N):
        flag=''
        if rsi[i]>70: flag+=' RSI>70'
        if rsi[i]<30: flag+=' RSI<30'
        if up[i] and C[i]>up[i]: flag+=' >상단'
        if dn[i] and C[i]<dn[i]: flag+=' <하단'
        if flag: print(i+1,C[i],round(rsi[i],1),round(up[i]),round(dn[i]),flag)
    bw=[(u-d)/m*100 for u,d,m in zip(up[19:],dn[19:],s20[19:])]
    print('bandwidth min/max', round(min(bw),2), bw.index(min(bw))+20, round(max(bw),2), bw.index(max(bw))+20)
