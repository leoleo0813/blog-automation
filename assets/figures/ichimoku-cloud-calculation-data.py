"""일목균형표 예시용 가정 가격(고가·저가·종가)과 다섯 선 계산. 실제 종목 아님."""
C=[]
for i in range(80): C.append(11600-22*i + (40 if i%4==0 else -30 if i%4==2 else 0))
b=C[-1]
for i in range(1,31): C.append(b+60*i + (35 if i%2 else -35))
t=C[-1]
sw=[0,-150,-260,-180,-60,-220,-340,-250,-120,-280,-380,-300,-160,-310,-420,-330,-200,-360,-460,-380,-250,-400,-500,-420,-300,-450,-540,-470,-350,-480,-560,-500,-380,-520,-600]
for v in sw: C.append(t+v)
C=[round(x/10)*10 for x in C]
N=len(C)
H=[c+(90 if i%3==0 else 60 if i%3==1 else 120) for i,c in enumerate(C)]
L=[c-(80 if i%3==2 else 110 if i%3==0 else 70) for i,c in enumerate(C)]
def mid(n,i): 
    if i<n-1: return None
    return (max(H[i-n+1:i+1])+min(L[i-n+1:i+1]))/2
tenkan=[mid(9,i) for i in range(N)]
kijun=[mid(26,i) for i in range(N)]
spanA_raw=[None if (a is None or b is None) else (a+b)/2 for a,b in zip(tenkan,kijun)]
spanB_raw=[mid(52,i) for i in range(N)]
# 그려지는 위치: 선행스팬은 26일 앞(오늘 계산값이 26일 뒤 칸에 찍힘)
spanA=[None]*26+spanA_raw; spanB=[None]*26+spanB_raw   # 길이 N+26
chikou=[C[i+26] if i+26<N else None for i in range(N)]
if __name__=='__main__':
    def cloud(i):
        a,b=spanA[i],spanB[i]
        return None if a is None or b is None else (min(a,b),max(a,b))
    for i in range(N):
        cl=cloud(i); pos=''
        if cl: pos='위' if C[i]>cl[1] else '아래' if C[i]<cl[0] else '안'
        f=lambda v:'' if v is None else f'{v:8.0f}'
        print(i+1,C[i],H[i],L[i],f(tenkan[i]),f(kijun[i]),f(spanA[i]),f(spanB[i]),pos)
    for i in range(1,N):
        if None in (tenkan[i],kijun[i],tenkan[i-1],kijun[i-1]): continue
        if tenkan[i-1]<=kijun[i-1] and tenkan[i]>kijun[i]: print('호전(전환>기준) day',i+1)
        if tenkan[i-1]>=kijun[i-1] and tenkan[i]<kijun[i]: print('역전 day',i+1)
