import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = float('inf')
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
