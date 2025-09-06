import math
x,y,D,T=map(int,input().split())
r=math.hypot(x,y)
ans=r
if r==0:
    ans=0.0
else:
    if r<D:
        ans=min(ans,T+(D-r),2*T)
    else:
        k=int(r//D)
        ans=min(ans,k*T+(r-k*D),(k+1)*T)
print("{:.10f}".format(ans))
