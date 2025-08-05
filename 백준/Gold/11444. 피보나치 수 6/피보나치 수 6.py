MOD = 1000000007

def matmul(a, b):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]]

def power(mat, n):
    if n == 1:
        return mat
    half = power(mat, n // 2)
    result = matmul(half, half)
    if n % 2 == 1:
        result = matmul(result, mat)
    return result

n = int(input())
base = [[1, 1], [1, 0]]
if n == 0:
    print(0)
else:
    print(power(base, n)[0][1])
