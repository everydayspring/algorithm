import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
order = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort(reverse=True)

queue = deque([r])
visited[r] = order
order += 1

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = order
            order += 1
            queue.append(v)

for i in range(1, n + 1):
    print(visited[i])
