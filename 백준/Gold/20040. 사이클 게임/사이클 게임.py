import sys
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root == b_root:
        return False
    parent[b_root] = a_root
    return True

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    if not union(parent, a, b):
        print(i)
        exit()
print(0)
