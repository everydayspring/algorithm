import sys
MOD=1000000003
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
if k>n//2:
    print(0)
    sys.exit(0)
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,min(i,(k))+1):
        if i==1 and j==1:
            dp[i][j]=1
        else:
            dp[i][j]=(dp[i-1][j]+dp[i-2][j-1])%MOD
a=dp[n-1][k] if n-1>=0 else 0
b=dp[n-3][k-1] if n-3>=0 and k-1>=0 else 0
print((a+b)%MOD)
