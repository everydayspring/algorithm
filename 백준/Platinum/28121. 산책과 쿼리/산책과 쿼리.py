import sys

input=sys.stdin.readline

n,q=map(int,input().split())
parent=list(range(n+1))
rank=[0]*(n+1)
par=[0]*(n+1)
siz=[1]*(n+1)
good=[False]*(n+1)
ans=0

def find(x):
    if parent[x]!=x:
        r, px = find(parent[x])
        par[x]^=px
        parent[x]=r
    return parent[x], par[x]

def union(x,y,d):
    global ans
    rx, px = find(x)
    ry, py = find(y)
    if rx==ry:
        if (px^py)!=d and not good[rx]:
            good[rx]=True
            ans+=siz[rx]
        return
    if rank[rx]<rank[ry]:
        rx, ry = ry, rx
        px, py = py, px
        x, y = y, x
    if good[rx]:
        ans-=siz[rx]
    if good[ry]:
        ans-=siz[ry]
    parent[ry]=rx
    par[ry]=px^py^d
    if rank[rx]==rank[ry]:
        rank[rx]+=1
    siz[rx]+=siz[ry]
    good[rx]=good[rx] or good[ry]
    if good[rx]:
        ans+=siz[rx]

out=[]
for _ in range(q):
    a,b=map(int,input().split())
    union(a,b,1)
    out.append(str(ans))
print("\n".join(out))
