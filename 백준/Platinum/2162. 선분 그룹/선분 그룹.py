import sys
input=sys.stdin.readline

def ccw(ax,ay,bx,by,cx,cy):
    v=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax)
    if v>0: return 1
    if v<0: return -1
    return 0

def intersect(a,b,c,d):
    a1=ccw(*a,*b,*c)
    a2=ccw(*a,*b,*d)
    b1=ccw(*c,*d,*a)
    b2=ccw(*c,*d,*b)
    if a1==0 and a2==0:
        if b<a: a,b=b,a
        if d<c: c,d=d,c
        return not (b<c or d<a)
    return a1*a2<=0 and b1*b2<=0

n=int(input().strip())
pts=[tuple(map(int,input().split())) for _ in range(n)]
a=[(x1,y1) for x1,y1,_,_ in pts]
b=[(x2,y2) for _,_,x2,y2 in pts]

p=list(range(n))
sz=[1]*n
def find(x):
    while p[x]!=x:
        p[x]=p[p[x]]
        x=p[x]
    return x
def union(x,y):
    x=find(x); y=find(y)
    if x==y: return
    if sz[x]<sz[y]: x,y=y,x
    p[y]=x
    sz[x]+=sz[y]

for i in range(n):
    ai=a[i]; bi=b[i]
    for j in range(i+1,n):
        if intersect(ai,bi,a[j],b[j]):
            union(i,j)

roots=set(find(i) for i in range(n))
mx=max(sz[find(i)] for i in range(n))
print(len(roots))
print(mx)
