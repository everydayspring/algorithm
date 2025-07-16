import sys
import math
input = sys.stdin.readline

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        parent[v_root] = u_root
        return True
    return False

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
parent = list(range(n))

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

edges = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        edges.append((dist, i, j))

edges.sort()
result = 0

for cost, a, b in edges:
    if union(a, b):
        result += cost

print(f"{result:.2f}")
