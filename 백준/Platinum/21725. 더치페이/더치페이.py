import sys
sys.setrecursionlimit(1 << 25)
input=sys.stdin.readline

n,m=map(int,input().split())
parent=list(range(n+1))
size=[1]*(n+1)
rank=[0]*(n+1)
tag=[0]*(n+1)
delta=[0]*(n+1)
pers=[0]*(n+1)

def find(x):
    if parent[x]==x:
        return x,0
    r, off = find(parent[x])
    delta[x]+=off
    parent[x]=r
    return r, delta[x]

def unite(x,y):
    rx, ox = find(x)
    ry, oy = find(y)
    if rx==ry:
        return
    if rank[rx]<rank[ry]:
        rx,ry=ry,rx
    parent[ry]=rx
    delta[ry]=tag[ry]-tag[rx]
    if rank[rx]==rank[ry]:
        rank[rx]+=1
    size[rx]+=size[ry]

for _ in range(m):
    t,*rest=map(int,input().split())
    if t==1:
        x,y=rest
        unite(x,y)
    else:
        x,c=rest
        r,_=find(x)
        s=c//size[r]
        tag[r]-=s
        pers[x]+=c

root,_=find(1)
for i in range(1,n+1):
    find(i)
balances=[0]*(n+1)
for i in range(1,n+1):
    balances[i]=pers[i]+delta[i]+tag[parent[i]]

pos=[]
neg=[]
for i in range(1,n+1):
    b=balances[i]
    if b>0:
        pos.append([i,b])
    elif b<0:
        neg.append([i,-b])

if sum(balances[1:])!=0:
    print(-1)
else:
    res=[]
    ip=0; ineg=0
    while ip<len(pos) and ineg<len(neg):
        pi,pv=pos[ip]
        ni,nv=neg[ineg]
        x=min(pv,nv)
        res.append((ni,pi,x))
        pv-=x; nv-=x
        if pv==0:
            ip+=1
        else:
            pos[ip][1]=pv
        if nv==0:
            ineg+=1
        else:
            neg[ineg][1]=nv
    print(len(res))
    for a,b,c in res:
        print(a,b,c)
