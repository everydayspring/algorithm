n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n - 1
min_sum = float('inf')
ans = (0, 0)

while left < right:
    total = arr[left] + arr[right]
    if abs(total) < min_sum:
        min_sum = abs(total)
        ans = (arr[left], arr[right])
    if total < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
