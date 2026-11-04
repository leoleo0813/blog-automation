from hub_data import C,H,L,N,rsi
def sma(xs,n):
    out=[None]*len(xs)
    for i in range(len(xs)):
        w=xs[i-n+1:i+1] if i>=n-1 else []
        if len(w)==n and None not in w: out[i]=sum(w)/n
    return out
fastK=[None if i<13 else (C[i]-min(L[i-13:i+1]))/(max(H[i-13:i+1])-min(L[i-13:i+1]))*100 for i in range(N)]
slowK=sma(fastK,3); slowD=sma(slowK,3)
if __name__=='__main__':
    def runs(arr,cond):
        out=[];s=None
        for i in range(N):
            c=arr[i] is not None and cond(arr[i])
            if c and s is None: s=i
            if not c and s is not None: out.append((s+1,i)); s=None
        if s is not None: out.append((s+1,N))
        return out
    print('slowK<20',runs(slowK,lambda v:v<20)); print('slowK>80',runs(slowK,lambda v:v>80))
    print('rsi<30',runs(rsi,lambda v:v<30)); print('rsi>70',runs(rsi,lambda v:v>70))
    cr=[]
    for i in range(1,N):
        a,b,a0,b0=slowK[i],slowD[i],slowK[i-1],slowD[i-1]
        if None in (a,b,a0,b0): continue
        if (a0-b0)*(a-b)<0: cr.append((i+1,'UP' if a>b else 'DN'))
    print('crosses',len(cr)); print(cr)
    for seg,(x,y) in (('decl',(15,80)),('rise',(81,110)),('side',(111,145))):
        print(seg, sum(1 for d,_ in cr if x<=d<=y))
    i=87; print('d88', C[i], 'HH14',max(H[i-13:i+1]),'LL14',min(L[i-13:i+1]),'fastK',round(fastK[i],1),'fk86,87',round(fastK[i-2],1),round(fastK[i-1],1),'slowK',round(slowK[i],1),'slowD',round(slowD[i],1),'sk86,87',round(slowK[i-2],1),round(slowK[i-1],1),'rsi',round(rsi[i],1))
