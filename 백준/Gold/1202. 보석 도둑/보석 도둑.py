import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort()
bags.sort()

total = 0
heap = []
j = 0

for bag in bags:
    while j < n and jewels[j][0] <= bag:
        heapq.heappush(heap, -jewels[j][1])
        j += 1
    if heap:
        total -= heapq.heappop(heap)

print(total)
