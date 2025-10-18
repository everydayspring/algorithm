import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n = next(it)

MAXV = 2_000_000
bit = [0] * (MAXV + 2)

def add(i, v):
    while i <= MAXV:
        bit[i] += v
        i += i & -i

def kth(k):
    idx = 0
    step = 1 << 21
    while step:
        nxt = idx + step
        if nxt <= MAXV and bit[nxt] < k:
            k -= bit[nxt]
            idx = nxt
        step >>= 1
    return idx + 1

out = []
for _ in range(n):
    t = next(it); x = next(it)
    if t == 1:
        add(x, 1)
    else:
        v = kth(x)
        out.append(str(v))
        add(v, -1)

sys.stdout.write("\n".join(out))
