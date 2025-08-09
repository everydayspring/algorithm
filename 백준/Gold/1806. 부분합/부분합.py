import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

left = 0
cur = 0
ans = n + 1

for right in range(n):
    cur += a[right]
    while cur >= s:
        ans = min(ans, right - left + 1)
        cur -= a[left]
        left += 1

print(0 if ans == n + 1 else ans)
