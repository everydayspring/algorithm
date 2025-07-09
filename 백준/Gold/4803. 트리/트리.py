import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

case_num = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    cycle = [False] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            cycle[x] = True
        else:
            parent[y] = x
            if cycle[y] or cycle[x]:
                cycle[x] = cycle[y] = True

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    tree_count = 0
    for i in range(1, n + 1):
        if parent[i] == i and not cycle[i]:
            tree_count += 1

    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")
    case_num += 1
