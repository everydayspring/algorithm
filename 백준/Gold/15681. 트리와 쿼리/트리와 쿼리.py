import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    subtree[node] = 1
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            subtree[node] += subtree[child]

dfs(r)

for _ in range(q):
    u = int(input())
    print(subtree[u])
