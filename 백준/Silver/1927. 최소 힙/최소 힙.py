import sys
import heapq

input = sys.stdin.read
data = list(map(int, input().split()))
n = data[0]
commands = data[1:]

heap = []
result = []

for x in commands:
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)

print('\n'.join(map(str, result)))
