import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())

dist = [float('inf')] * (n+1)
prev = [0] * (n+1)
dist[start] = 0
hq = []
heapq.heappush(hq, (0, start))

while hq:
    cost, now = heapq.heappop(hq)
    if dist[now] < cost:
        continue
    for to, w in graph[now]:
        if dist[to] > cost + w:
            dist[to] = cost + w
            prev[to] = now
            heapq.heappush(hq, (dist[to], to))

path = []
temp = end
while temp:
    path.append(temp)
    temp = prev[temp]
path.reverse()

print(dist[end])
print(len(path))
print(*path)
