import sys

N, M = map(int, sys.stdin.readline().split())
S = set(sys.stdin.readline().strip() for _ in range(N))
queries = (sys.stdin.readline().strip() for _ in range(M))

count = sum(1 for q in queries if q in S)
print(count)
