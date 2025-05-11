n = int(input())
k = int(input())

def count(mid):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    return cnt

left, right = 1, k
while left <= right:
    mid = (left + right) // 2
    if count(mid) < k:
        left = mid + 1
    else:
        right = mid - 1

print(left)
