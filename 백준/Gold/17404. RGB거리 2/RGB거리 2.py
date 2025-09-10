import sys

input=sys.stdin.readline
n=int(input())
cost=[tuple(map(int,input().split())) for _ in range(n)]
INF=10**9
ans=INF

for s in range(3):
    dp=[[INF]*3 for _ in range(n)]
    dp[0][s]=cost[0][s]
    for i in range(1,n):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+cost[i][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+cost[i][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+cost[i][2]
    for c in range(3):
        if c!=s:
            ans=min(ans,dp[-1][c])

print(ans)
