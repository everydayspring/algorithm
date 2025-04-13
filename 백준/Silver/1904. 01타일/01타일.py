n = int(input())
MOD = 15746

a, b = 1, 2
for _ in range(3, n + 1):
    a, b = b, (a + b) % MOD

print(a if n == 1 else b)
