import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid for tree in trees if tree > mid)
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
