import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
G = next(it)
P = next(it)

parent = list(range(G + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

ans = 0
for _ in range(P):
    g = next(it)
    r = find(g)
    if r == 0:
        break
    parent[r] = find(r - 1)
    ans += 1

print(ans)
