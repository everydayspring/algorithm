import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,d = map(int,input().split())
    g[u].append((v,d))
    g[v].append((u,d))

subsz = [0]*(n+1)
dist_sum = [0]*(n+1)

def dfs1(u,p):
    subsz[u] = 1
    for v,w in g[u]:
        if v==p: continue
        dfs1(v,u)
        subsz[u]+=subsz[v]
        dist_sum[u]+=dist_sum[v]+subsz[v]*w

def dfs2(u,p):
    for v,w in g[u]:
        if v==p: continue
        dist_sum[v] = dist_sum[u] + (n-2*subsz[v])*w
        dfs2(v,u)

dfs1(1,-1)
dfs2(1,-1)

for i in range(1,n+1):
    print(dist_sum[i])
