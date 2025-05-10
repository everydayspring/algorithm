import sys

n, c = map(int, sys.stdin.readline().split())
houses = sorted(int(sys.stdin.readline()) for _ in range(n))

def can_place(distance):
    count = 1
    last = houses[0]
    for i in range(1, n):
        if houses[i] - last >= distance:
            count += 1
            last = houses[i]
    return count >= c

low, high = 1, houses[-1] - houses[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    if can_place(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
