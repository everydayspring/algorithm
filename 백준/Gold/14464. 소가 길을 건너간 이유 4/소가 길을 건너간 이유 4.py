import sys, heapq

it = map(int, sys.stdin.buffer.read().split())
C = next(it); N = next(it)
T = [next(it) for _ in range(C)]
cows = [(next(it), next(it)) for _ in range(N)]
T.sort()
cows.sort()
h = []
ans = 0
j = 0
for t in T:
    while j < N and cows[j][0] <= t:
        heapq.heappush(h, cows[j][1])
        j += 1
    while h and h[0] < t:
        heapq.heappop(h)
    if h:
        heapq.heappop(h)
        ans += 1
print(ans)
