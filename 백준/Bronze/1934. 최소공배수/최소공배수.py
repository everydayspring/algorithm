import sys
import math

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))
