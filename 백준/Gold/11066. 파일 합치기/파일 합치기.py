import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    k=int(input())
    arr=[]
    while len(arr)<k:
        arr+=list(map(int,input().split()))
    s=[0]*(k+1)
    for i in range(1,k+1):
        s[i]=s[i-1]+arr[i-1]
    dp=[[0]*(k+1) for _ in range(k+1)]
    opt=[[0]*(k+1) for _ in range(k+1)]
    for i in range(1,k+1):
        opt[i][i]=i
    for length in range(2,k+1):
        for i in range(1,k-length+2):
            j=i+length-1
            dp[i][j]=10**18
            start=opt[i][j-1]
            end=opt[i+1][j] if i+1<=j else j
            if start< i: start=i
            if end> j-1: end=j-1
            for m in range(start,end+1):
                v=dp[i][m]+dp[m+1][j]
                if v<dp[i][j]:
                    dp[i][j]=v
                    opt[i][j]=m
            dp[i][j]+=s[j]-s[i-1]
    print(dp[1][k])
