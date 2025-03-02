import sys
import math

n = int(sys.stdin.readline())
trees = [int(sys.stdin.readline()) for _ in range(n)]

intervals = [trees[i] - trees[i - 1] for i in range(1, n)]
gcd = math.gcd(*intervals)

new_trees = sum((interval // gcd - 1) for interval in intervals)
print(new_trees)
