import sys
sys.setrecursionlimit(10000)

n = int(input())

memo = [0] * (n + 1)

def fib_count(n):
    if n == 1 or n == 2:
        return 1
    if memo[n]:
        return memo[n]
    memo[n] = fib_count(n - 1) + fib_count(n - 2)
    return memo[n]

def dp_count(n):
    return n - 2

print(fib_count(n), dp_count(n))
