import sys

def add(tree, n, i, v):
    while i <= n:
        tree[i] += v
        i += i & -i

def kth(tree, n, k):
    idx = 0
    bit = 1 << (n.bit_length())
    while bit:
        nxt = idx + bit
        if nxt <= n and tree[nxt] < k:
            k -= tree[nxt]
            idx = nxt
        bit >>= 1
    return idx + 1

data = sys.stdin.read().strip().split()
N = int(data[0]); K = int(data[1])
tree = [0]*(N+1)
for i in range(1, N+1):
    add(tree, N, i, 1)

cur = 0
res = []
for i in range(N, 0, -1):
    cur = (cur + K - 1) % i
    idx = kth(tree, N, cur + 1)
    res.append(str(idx))
    add(tree, N, idx, -1)

sys.stdout.write("<" + ", ".join(res) + ">")
