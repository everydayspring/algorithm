t = int(input())
ns = [int(input()) for _ in range(t)]

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in ns:
    print(dp[n])
