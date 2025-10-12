import sys

it = iter(sys.stdin.buffer.read().split())
n = int(next(it)); m = int(next(it)); k = int(next(it))

BIT = [0]*(n+1)
arr = [0]*(n+1)

def add(i, v):
    while i <= n:
        BIT[i] += v
        i += i & -i

def psum(i):
    s = 0
    while i > 0:
        s += BIT[i]
        i -= i & -i
    return s

for i in range(1, n+1):
    x = int(next(it))
    arr[i] = x
    add(i, x)

out_lines = []
for _ in range(m+k):
    a = int(next(it)); b = int(next(it)); c = int(next(it))
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        add(b, diff)
    else:
        if b > c:
            b, c = c, b
        out_lines.append(str(psum(c) - psum(b-1)))

sys.stdout.write("\n".join(out_lines))
