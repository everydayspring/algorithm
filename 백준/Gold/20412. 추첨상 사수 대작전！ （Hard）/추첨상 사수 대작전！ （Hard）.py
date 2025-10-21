import sys

m, s, x1, x2 = map(int, sys.stdin.read().split())

if x1 == s and x2 == x1:
    a = 0
    c = x1 % m
else:
    denom = (x1 - s) % m
    inv = pow(denom, m - 2, m)
    a = ((x2 - x1) % m) * inv % m
    c = (x1 - a * s) % m

print(a, c)
