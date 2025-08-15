import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
w=[0]+list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dp=[[0,0] for _ in range(n+1)]
vis=[0]*(n+1)

def dfs(x):
    vis[x]=1
    dp[x][1]=w[x]
    for nx in g[x]:
        if not vis[nx]:
            dfs(nx)
            dp[x][0]+=max(dp[nx][0],dp[nx][1])
            dp[x][1]+=dp[nx][0]
dfs(1)

res=[]
def trace(x,pre,inc):
    if inc:
        res.append(x)
        for nx in g[x]:
            if nx!=pre:
                trace(nx,x,0)
    else:
        for nx in g[x]:
            if nx!=pre:
                if dp[nx][1]>dp[nx][0]:
                    trace(nx,x,1)
                else:
                    trace(nx,x,0)

if dp[1][0]<dp[1][1]:
    trace(1,-1,1)
else:
    trace(1,-1,0)

print(max(dp[1]))
print(*sorted(res))
