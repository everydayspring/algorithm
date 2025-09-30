import sys
from functools import cmp_to_key

input=sys.stdin.readline
n=int(input().strip())
jobs=[]
for i in range(1,n+1):
    t,s=map(int,input().split())
    jobs.append((t,s,i))

def cmp(a,b):
    t1,s1,i1=a
    t2,s2,i2=b
    v=t1*s2 - t2*s1
    if v!=0:
        return -1 if v<0 else 1
    return -1 if i1<i2 else (1 if i1>i2 else 0)

jobs.sort(key=cmp_to_key(cmp))
print(" ".join(str(x[2]) for x in jobs))
