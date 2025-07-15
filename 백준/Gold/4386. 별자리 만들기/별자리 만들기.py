import sys
import math
input = sys.stdin.read

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

data = input().split()
n = int(data[0])
stars = []
index = 1

for _ in range(n):
    x, y = float(data[index]), float(data[index+1])
    stars.append((x, y))
    index += 2

edges = []
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        edges.append((dist, i, j))

edges.sort()
parent = [i for i in range(n)]
result = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(f"{result:.2f}")
