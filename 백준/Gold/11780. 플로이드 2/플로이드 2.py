import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF]*n for _ in range(n)]
route = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a-1][b-1] > c:
        dist[a-1][b-1] = c
        route[a-1][b-1] = [a-1, b-1]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                route[i][j] = route[i][k][:-1] + route[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0)
        else:
            path = route[i][j]
            print(len(path), end=' ')
            for p in path:
                print(p+1, end=' ')
            print()
