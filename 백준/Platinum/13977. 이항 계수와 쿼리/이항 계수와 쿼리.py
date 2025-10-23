import sys

MOD = 1000000007
MAX = 4000000

fac = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD

inv = [1] * (MAX + 1)
inv[MAX] = pow(fac[MAX], MOD - 2, MOD)
for i in range(MAX, 0, -1):
    inv[i - 1] = inv[i] * i % MOD

input = sys.stdin.readline
m = int(input().strip())
res = []
for _ in range(m):
    n, k = map(int, input().split())
    res.append(str(fac[n] * inv[k] % MOD * inv[n - k] % MOD))
print("\n".join(res))
