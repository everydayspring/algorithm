import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 100001
dist = [-1] * MAX
dist[n] = 0
dq = deque([n])

while dq:
    x = dq.popleft()
    if x == k:
        print(dist[x])
        break
    for nx in (x * 2, x - 1, x + 1):
        if 0 <= nx < MAX and dist[nx] == -1:
            if nx == x * 2:
                dist[nx] = dist[x]
                dq.appendleft(nx)
            else:
                dist[nx] = dist[x] + 1
                dq.append(nx)
