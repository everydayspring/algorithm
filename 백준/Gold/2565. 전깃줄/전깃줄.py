n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
