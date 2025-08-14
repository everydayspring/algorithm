import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dp=[[0,0] for _ in range(n+1)]
visited=[0]*(n+1)

def dfs(x):
    visited[x]=1
    dp[x][0]=0
    dp[x][1]=1
    for nx in g[x]:
        if not visited[nx]:
            dfs(nx)
            dp[x][0]+=dp[nx][1]
            dp[x][1]+=min(dp[nx][0],dp[nx][1])

dfs(1)
print(min(dp[1][0],dp[1][1]))
