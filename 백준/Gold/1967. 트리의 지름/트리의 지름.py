import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [False] * (n+1)
max_dist = 0
max_node = 0

def dfs(node, dist):
    global max_dist, max_node
    visited[node] = True
    if dist > max_dist:
        max_dist = dist
        max_node = node
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            dfs(next_node, dist + weight)

dfs(1, 0)
visited = [False] * (n+1)
max_dist = 0
dfs(max_node, 0)
print(max_dist)
