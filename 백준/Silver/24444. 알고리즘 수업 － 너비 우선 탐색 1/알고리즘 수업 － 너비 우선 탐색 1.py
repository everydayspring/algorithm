import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

visited = [0] * (n + 1)
order = 1
queue = deque([r])
visited[r] = order

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if not visited[v]:
            order += 1
            visited[v] = order
            queue.append(v)

for i in range(1, n + 1):
    print(visited[i])
