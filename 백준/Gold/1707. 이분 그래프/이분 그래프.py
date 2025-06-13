import sys
from collections import deque

input = sys.stdin.readline
K = int(input())

def is_bipartite(V, graph):
    color = [0] * (V + 1)
    for start in range(1, V + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print("YES" if is_bipartite(V, graph) else "NO")
