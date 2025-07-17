import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def label_island():
    visited = [[False]*m for _ in range(n)]
    idx = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                idx += 1
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                graph[i][j] = idx
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]==1:
                            visited[nx][ny] = True
                            graph[nx][ny] = idx
                            q.append((nx, ny))
    return idx - 1

def find_bridges(island_count):
    bridges = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 1:
                for d in range(4):
                    length = 0
                    nx, ny = x + dx[d], y + dy[d]
                    while 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == graph[x][y]:
                            break
                        if graph[nx][ny] == 0:
                            length += 1
                        else:
                            if length >= 2:
                                bridges.append((length, graph[x][y], graph[nx][ny]))
                            break
                        nx += dx[d]
                        ny += dy[d]
    return bridges

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

island_count = label_island()
edges = find_bridges(island_count)
edges.sort()
parent = [i for i in range(island_count+2)]

result = 0
cnt = 0
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        cnt += 1

print(result if cnt == island_count - 1 else -1)
