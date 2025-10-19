import sys

def egcd(a,b):
    x0,y0,x1,y1=1,0,0,1
    while b:
        q=a//b
        a,b=b,a-b*q
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1
    return a,x0,y0

def solve():
    input=sys.stdin.readline
    t=int(input().strip())
    LIM=10**9
    out=[]
    for _ in range(t):
        K,C=map(int,input().split())
        g,inv,_=egcd(C,K)
        if g!=1:
            out.append("IMPOSSIBLE")
            continue
        y=inv%K
        if y==0:
            y=K
        x=(C*y-1)//K
        if x<=0:
            y+=K
        if y>LIM:
            out.append("IMPOSSIBLE")
        else:
            out.append(str(y))
    print("\n".join(out))

if __name__=="__main__":
    solve()
