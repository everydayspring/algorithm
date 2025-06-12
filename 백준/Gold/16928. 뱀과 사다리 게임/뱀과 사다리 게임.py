from collections import deque

n, m = map(int, input().split())
board = [i for i in range(101)]
visited = [False] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

q = deque()
q.append((1, 0))
visited[1] = True

while q:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        break
    for i in range(1, 7):
        nxt = now + i
        if nxt <= 100 and not visited[nxt]:
            visited[nxt] = True
            q.append((board[nxt], cnt + 1))
