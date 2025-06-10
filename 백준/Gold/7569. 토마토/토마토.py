from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append((z, y, x))

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[z][y][x] + 1
            queue.append((nz, ny, nx))

res = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0:
                print(-1)
                exit(0)
            res = max(res, box[z][y][x])

print(res - 1)
