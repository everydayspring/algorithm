import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
balls = list(map(int, input().split()))

possible = [set() for _ in range(n + 1)]
possible[0].add(0)

for i in range(1, n + 1):
    w = weights[i - 1]
    possible[i] = possible[i - 1].copy()
    for p in possible[i - 1]:
        possible[i].add(p + w)
        possible[i].add(abs(p - w))

result = []
for ball in balls:
    result.append('Y' if ball in possible[n] else 'N')

print(' '.join(result))
