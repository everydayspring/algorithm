import sys
import heapq

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    edges = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        heapq.heappush(edges, (z, x, y))
        total += z

    parent = [i for i in range(m)]

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root != v_root:
            parent[v_root] = u_root
            return True
        return False

    mst_cost = 0
    while edges:
        cost, u, v = heapq.heappop(edges)
        if union(u, v):
            mst_cost += cost

    print(total - mst_cost)
