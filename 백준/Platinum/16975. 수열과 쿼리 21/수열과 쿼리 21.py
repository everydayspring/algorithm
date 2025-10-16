import sys

data=list(map(int,sys.stdin.buffer.read().split()))
it=iter(data)
n=next(it)
a=[0]+[next(it) for _ in range(n)]
m=next(it)

size=n+2
bit=[0]*(size+1)

def add(i,v):
    while i<=size:
        bit[i]+=v
        i+=i&-i
def ps(i):
    s=0
    while i>0:
        s+=bit[i]
        i-=i&-i
    return s

prev=0
for i in range(1,n+1):
    add(i,a[i]-prev)
    prev=a[i]

out=[]
for _ in range(m):
    t=next(it)
    if t==1:
        i=next(it);j=next(it);k=next(it)
        add(i,k)
        add(j+1,-k)
    else:
        x=next(it)
        out.append(str(ps(x)))
print("\n".join(out))
