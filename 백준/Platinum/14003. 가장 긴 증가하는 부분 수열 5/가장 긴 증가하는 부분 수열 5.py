import sys
import bisect
input = sys.stdin.read

data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))

dp = []
track = []
for num in a:
    if not dp or dp[-1] < num:
        dp.append(num)
        track.append((len(dp) - 1, num))
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num
        track.append((idx, num))

length = len(dp)
result = []
for i in range(len(track) - 1, -1, -1):
    if track[i][0] == length - 1:
        result.append(track[i][1])
        length -= 1
result.reverse()

print(len(result))
print(*result)
