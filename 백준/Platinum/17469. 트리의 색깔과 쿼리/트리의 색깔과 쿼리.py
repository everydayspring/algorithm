import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
N = next(it); Q = next(it)
par = [0]*(N+1)
for i in range(2, N+1):
    par[i] = next(it)
color = [0]*(N+1)
for i in range(1, N+1):
    color[i] = next(it)
ops = []
for _ in range(N+Q-1):
    x = next(it); a = next(it)
    ops.append((x, a))

parent = list(range(N+1))
size = [1]*(N+1)
mp = [None]*(N+1)
for i in range(1, N+1):
    d = {color[i]: 1}
    mp[i] = d

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    ra = find(a); rb = find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    mra = mp[ra]; mrb = mp[rb]
    if len(mra) < len(mrb):
        mra, mrb = mrb, mra
        mp[ra] = mra
    for k, v in mrb.items():
        mra[k] = mra.get(k, 0) + v
    mp[rb] = {}

ans = []
for x, a in reversed(ops):
    if x == 2:
        ans.append(str(len(mp[find(a)])))
    else:
        union(a, par[a])

sys.stdout.write("\n".join(reversed(ans)))
