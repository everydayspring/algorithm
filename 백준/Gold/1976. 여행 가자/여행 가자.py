n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))
result = "YES"
for i in range(m-1):
    if find(plan[i]) != find(plan[i+1]):
        result = "NO"
        break
print(result)
