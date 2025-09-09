import sys
sys.setrecursionlimit(1_000_000)

input=sys.stdin.readline
n=int(input())
w=[list(map(int,input().split())) for _ in range(n)]
nexts=[[j for j in range(n) if w[i][j]>0] for i in range(n)]
FULL=(1<<n)-1

from functools import lru_cache

@lru_cache(None)
def dp(u, mask):
    if mask==FULL:
        return w[u][0] if w[u][0]>0 else 10**15
    res=10**15
    nm=mask
    for v in nexts[u]:
        if nm>>v&1==0:
            cost=w[u][v]+dp(v, nm|1<<v)
            if cost<res:
                res=cost
    return res

print(dp(0,1))
