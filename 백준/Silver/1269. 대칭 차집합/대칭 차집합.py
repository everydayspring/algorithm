import sys

N, M = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

symmetric_diff = A ^ B

sys.stdout.write(str(len(symmetric_diff)) + "\n")
