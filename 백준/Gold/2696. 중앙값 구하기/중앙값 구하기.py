import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    m = int(input())
    nums = []
    while len(nums) < m:
        nums += list(map(int, input().split()))

    result = []
    max_heap = []
    min_heap = []

    for i in range(m):
        num = nums[i]
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if min_heap and -max_heap[0] > min_heap[0]:
            max_val = -heapq.heappop(max_heap)
            min_val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, max_val)

        if i % 2 == 0:
            result.append(-max_heap[0])

    print(len(result))
    for i in range(0, len(result), 10):
        print(*result[i:i+10])
