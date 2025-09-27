import sys, heapq

it = map(int, sys.stdin.buffer.read().split())
t = next(it)
out_lines = []
for _ in range(t):
    k = next(it)
    h = [next(it) for _ in range(k)]
    heapq.heapify(h)
    cost = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        s = a + b
        cost += s
        heapq.heappush(h, s)
    out_lines.append(str(cost))
sys.stdout.write("\n".join(out_lines))
