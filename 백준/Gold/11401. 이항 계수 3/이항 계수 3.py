import sys
input = sys.stdin.readline
MOD = 1000000007

def power(a, b):
    result = 1
    while b > 0:
        if b % 2:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return result

n, k = map(int, input().split())
fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD

if k == 0 or k == n:
    print(1)
else:
    print(fact[n] * power(fact[k] * fact[n - k] % MOD, MOD - 2) % MOD)
