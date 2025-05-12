import sys
import bisect

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = []

for num in a:
    idx = bisect.bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))
