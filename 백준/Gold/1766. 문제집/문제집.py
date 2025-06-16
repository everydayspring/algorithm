import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*result)
