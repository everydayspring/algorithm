import sys
from collections import deque

data = list(map(int, sys.stdin.buffer.read().split()))
N, K = data[0], data[1]
E = data[2:2+N]
total = sum(E)

dq = deque()
dq.append((0, 0))
dp_i = 0

for i in range(1, N + 2):
    while dq and dq[0][0] < i - (K + 1):
        dq.popleft()
    min_prev = dq[0][1]
    cost = E[i - 1] if i <= N else 0
    dp_i = min_prev + cost
    while dq and dq[-1][1] >= dp_i:
        dq.pop()
    dq.append((i, dp_i))

print(total - dp_i)
