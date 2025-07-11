import sys
sys.setrecursionlimit(1000000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]
    return size[x_root]

t = int(sys.stdin.readline())
for _ in range(t):
    f = int(sys.stdin.readline())
    parent = dict()
    size = dict()
    for _ in range(f):
        a, b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        print(union(parent, size, a, b))
