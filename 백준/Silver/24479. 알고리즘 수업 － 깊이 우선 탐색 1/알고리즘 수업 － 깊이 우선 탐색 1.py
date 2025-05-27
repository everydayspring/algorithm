import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(x):
    global cnt
    visited[x] = cnt
    for i in graph[x]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])
