from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(x):
    queue = deque([x])
    visited_bfs[x] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in graph[cur]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

dfs(v)
print()
bfs(v)
