import math
def series():
    p=[]
    for i in range(38): p.append(10800-30*i + (30 if i%3==0 else -20 if i%3==1 else 0))
    base=p[-1]
    for i in range(1,21): p.append(base+70*i + (25 if i%2 else -25))
    top=p[-1]
    sw=[0,120,40,-80,-140,-40,90,150,30,-110,-160,-30,110,140,0,-120,-150,10,130,100]
    for v in sw: p.append(top-150+v)
    return [round(x/10)*10 for x in p]
def ema(xs,n):
    a=2/(n+1); out=[None]*len(xs); out[n-1]=sum(xs[:n])/n
    for i in range(n,len(xs)): out[i]=out[i-1]+a*(xs[i]-out[i-1])
    return out
def sma(xs,n): return [None if i<n-1 else sum(xs[i-n+1:i+1])/n for i in range(len(xs))]
P=series(); e12=ema(P,12); e26=ema(P,26)
macd=[None if (a is None or b is None) else a-b for a,b in zip(e12,e26)]
start=next(i for i,v in enumerate(macd) if v is not None)
sig_part=ema(macd[start:],9); sig=[None]*start+sig_part
hist=[None if (m is None or s is None) else m-s for m,s in zip(macd,sig)]
s5=sma(P,5); s20=sma(P,20)
if __name__=='__main__':
    for i,x in enumerate(P):
        f=lambda v: '' if v is None else f'{v:9.1f}'
        print(i+1,x,f(e12[i]),f(e26[i]),f(macd[i]),f(sig[i]),f(hist[i]),f(s5[i]),f(s20[i]))
    def crosses(a,b,name):
        for i in range(1,len(a)):
            if None in (a[i],b[i],a[i-1],b[i-1]): continue
            if a[i-1]<=b[i-1] and a[i]>b[i]: print(name,'UP day',i+1)
            if a[i-1]>=b[i-1] and a[i]<b[i]: print(name,'DOWN day',i+1)
    crosses(s5,s20,'SMA5/20'); crosses(macd,[0]*len(P),'MACD0'); crosses(macd,sig,'MACD/SIG'); crosses(e12,e26,'EMA12/26')
