import sys

input=sys.stdin.buffer.readline
INF=10**18

n,t,m=map(int,input().split())
s,e=map(int,input().split())

prev=[INF]*n
prev[s]=0

for _ in range(t):
    nxt=prev[:]
    for _ in range(m):
        u,v,w=map(int,input().split())
        pu=prev[u]
        pv=prev[v]
        if pu+w<nxt[v]:
            nxt[v]=pu+w
        if pv+w<nxt[u]:
            nxt[u]=pv+w
    prev=nxt

ans=prev[e]
print(ans if ans<INF else -1)
