import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
ps=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    b=input().strip()
    row=ps[i]
    up=ps[i-1]
    for j in range(1,M+1):
        cell=1 if b[j-1]=='B' else 0
        m=cell^((i+j)&1)
        row[j]=row[j-1]+up[j]-up[j-1]+m

KK=K*K
ans=10**9
for i in range(K,N+1):
    row=ps[i]; up=ps[i-K]
    for j in range(K,M+1):
        w=row[j]-up[j]-row[j-K]+up[j-K]
        if w>KK-w: w=KK-w
        if w<ans: ans=w
print(ans)
