import sys

it = iter(map(int, sys.stdin.buffer.read().split()))
n = next(it); m = next(it)

size = 1
while size < n:
    size <<= 1

INF = 10**18
minseg = [INF] * (2 * size)
maxseg = [-INF] * (2 * size)

for i in range(n):
    x = next(it)
    idx = size + i
    minseg[idx] = x
    maxseg[idx] = x

for i in range(size - 1, 0, -1):
    minseg[i] = min(minseg[i << 1], minseg[i << 1 | 1])
    maxseg[i] = max(maxseg[i << 1], maxseg[i << 1 | 1])

out = []
for _ in range(m):
    a = next(it); b = next(it)
    if a > b:
        a, b = b, a
    l = a - 1 + size
    r = b - 1 + size
    mn = INF
    mx = -INF
    while l <= r:
        if l & 1:
            if minseg[l] < mn: mn = minseg[l]
            if maxseg[l] > mx: mx = maxseg[l]
            l += 1
        if not (r & 1):
            if minseg[r] < mn: mn = minseg[r]
            if maxseg[r] > mx: mx = maxseg[r]
            r -= 1
        l >>= 1; r >>= 1
    out.append(f"{mn} {mx}")

sys.stdout.write("\n".join(out))
