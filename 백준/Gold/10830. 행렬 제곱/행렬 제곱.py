def matmul(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

def power(a, b):
    if b == 1:
        return [[x % 1000 for x in row] for row in a]
    half = power(a, b // 2)
    if b % 2 == 0:
        return matmul(half, half)
    else:
        return matmul(matmul(half, half), a)

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = power(a, b)
for row in result:
    print(*row)
