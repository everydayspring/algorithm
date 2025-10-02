import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n = next(it)
pos = []
neg = []
for _ in range(n):
    a = next(it); b = next(it)
    if b - a >= 0:
        pos.append((a, b))
    else:
        neg.append((a, b))

pos.sort(key=lambda x: x[0])
neg.sort(key=lambda x: x[1], reverse=True)

ans = 0
cum = 0
for a, b in pos + neg:
    if a > cum:
        ans = max(ans, a - cum)
    cum += b - a

print(ans)
