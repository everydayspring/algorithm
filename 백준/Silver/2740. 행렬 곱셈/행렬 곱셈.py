n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m2, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m2)]

result = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            result[i][j] += a[i][t] * b[t][j]

for row in result:
    print(*row)
