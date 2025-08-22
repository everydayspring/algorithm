import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, n, graph):
    dist = [INF]*(n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d+w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    gh_dist = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a == g and b == h) or (a == h and b == g):
            gh_dist = d
    candidates = [int(input()) for _ in range(t)]
    dist_s = dijkstra(s, n, graph)
    dist_g = dijkstra(g, n, graph)
    dist_h = dijkstra(h, n, graph)
    ans = []
    for x in candidates:
        path1 = dist_s[g] + gh_dist + dist_h[x]
        path2 = dist_s[h] + gh_dist + dist_g[x]
        if dist_s[x] == path1 or dist_s[x] == path2:
            ans.append(x)
    ans.sort()
    print(*ans)
