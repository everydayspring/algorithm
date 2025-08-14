import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
pop=[0]+list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dp=[[0,0] for _ in range(n+1)]
v=[0]*(n+1)

def dfs(x):
    v[x]=1
    dp[x][1]=pop[x]
    for nx in g[x]:
        if not v[nx]:
            dfs(nx)
            dp[x][0]+=max(dp[nx][0],dp[nx][1])
            dp[x][1]+=dp[nx][0]

dfs(1)
print(max(dp[1][0],dp[1][1]))
