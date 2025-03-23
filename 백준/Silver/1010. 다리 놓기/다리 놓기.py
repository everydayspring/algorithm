def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combination(M, N))
