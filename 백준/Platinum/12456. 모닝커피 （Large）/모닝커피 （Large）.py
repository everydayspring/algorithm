import sys
from bisect import bisect_left
from collections import defaultdict

input=sys.stdin.readline
T=int(input().strip())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    items=[]
    for _ in range(N):
        c,t,s=map(int,input().split())
        if c==0: 
            continue
        t=min(t,K)
        if t<=0: 
            continue
        items.append((c,t,s))
    if not items:
        print(f"Case #{tc}: 0")
        continue
    deadlines=sorted({t for _,t,_ in items})
    m=len(deadlines)
    idx_map={d:i for i,d in enumerate(deadlines)}
    by_si=defaultdict(lambda: defaultdict(int))
    for c,t,s in items:
        k=idx_map[t]
        by_si[s][k]+=c
    slack=[deadlines[i] for i in range(m)]
    ans=0
    for s in sorted(by_si.keys(), reverse=True):
        ks=sorted(by_si[s].keys())
        for k in ks:
            cnt=by_si[s][k]
            smin=min(slack[k:])
            x=cnt if cnt<=smin else smin
            if x>0:
                ans+=x*s
                for j in range(k,m):
                    slack[j]-=x
    print(f"Case #{tc}: {ans}")
