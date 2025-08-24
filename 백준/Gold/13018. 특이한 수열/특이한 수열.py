import sys
n,k=map(int,sys.stdin.readline().split())
if n==1:
    if k==0: print(1)
    else: print("Impossible")
    exit(0)
if k>n-1:
    print("Impossible")
    exit(0)
if k==0:
    print(*([i+1 for i in range(1,n)]+[1]))
    exit(0)
a=list(range(1,n+1))
d=(n-1)-k
i=1
if d&1:
    a[0],a[1]=a[1],a[0]
    d-=1
    i=2
while d>0 and i+1<n:
    a[i],a[i+1]=a[i+1],a[i]
    d-=2
    i+=2
print(*a)
