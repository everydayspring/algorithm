import sys
import collections

input = sys.stdin.readline

v = int(input())
graph = collections.defaultdict(list)
for _ in range(v):
    data = list(map(int, input().split()))
    for i in range(1, len(data)-1, 2):
        graph[data[0]].append((data[i], data[i+1]))

def bfs(start):
    visited = [-1] * (v+1)
    visited[start] = 0
    queue = collections.deque([start])
    while queue:
        node = queue.popleft()
        for next_node, cost in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + cost
                queue.append(next_node)
    farthest = max(visited)
    farthest_node = visited.index(farthest)
    return farthest_node, farthest

node, _ = bfs(1)
_, diameter = bfs(node)
print(diameter)
