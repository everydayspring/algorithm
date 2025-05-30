import sys
sys.setrecursionlimit(10**6)
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

def dfs(x):
    global order
    visited[x] = order
    for y in graph[x]:
        if not visited[y]:
            order += 1
            dfs(y)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])
