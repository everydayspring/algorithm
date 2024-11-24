import sys

input = sys.stdin.readline
T = int(input())

results = []

for _ in range(T):
    A, B = map(int, input().split())
    results.append(A + B)

sys.stdout.write('\n'.join(map(str, results)) + '\n')
