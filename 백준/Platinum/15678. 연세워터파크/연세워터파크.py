import sys
input=sys.stdin.readline
N,D=map(int,input().split())
K=list(map(int,input().split()))
from collections import deque
dq=deque()
ans=-10**30
for i,x in enumerate(K):
    while dq and dq[0][0]<i-D: dq.popleft()
    best = max(0, dq[0][1]) if dq else 0
    cur = x + best
    ans = max(ans, cur)
    while dq and dq[-1][1] <= cur: dq.pop()
    dq.append((i, cur))
print(ans)
