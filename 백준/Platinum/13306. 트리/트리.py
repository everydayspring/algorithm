import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
N = next(it); Q = next(it)
par = [0]*(N+1)
for i in range(2, N+1):
    par[i] = next(it)
ops = []
removed = [False]*(N+1)
for _ in range(N-1+Q):
    x = next(it)
    if x == 0:
        b = next(it)
        ops.append((0, b))
        removed[b] = True
    else:
        c = next(it); d = next(it)
        ops.append((1, c, d))

parent = list(range(N+1))
rank = [0]*(N+1)
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
def union(a,b):
    a = find(a); b = find(b)
    if a == b: return
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1

for i in range(2, N+1):
    if not removed[i]:
        union(i, par[i])

ans = []
for op in reversed(ops):
    if op[0] == 0:
        b = op[1]
        union(b, par[b])
    else:
        _, c, d = op
        ans.append("YES" if find(c) == find(d) else "NO")

sys.stdout.write("\n".join(reversed(ans)))
