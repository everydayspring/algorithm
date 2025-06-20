import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
INF = float('inf')
dist = [INF] * (N + 1)
dist[1] = 0

for i in range(N - 1):
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

for u, v, w in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        print(-1)
        exit()

for i in range(2, N + 1):
    print(dist[i] if dist[i] != INF else -1)
