import sys
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and farm[ny][nx] == 1:
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    count = 0
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    print(count)
