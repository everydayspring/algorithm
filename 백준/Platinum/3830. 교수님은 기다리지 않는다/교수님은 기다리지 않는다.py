import sys
sys.setrecursionlimit(1 << 25)
input=sys.stdin.readline

out=[]
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    parent=list(range(N+1))
    rank=[0]*(N+1)
    diff=[0]*(N+1)  # weight[x] - weight[root(x)]

    def find(x):
        if parent[x]!=x:
            r=find(parent[x])
            diff[x]+=diff[parent[x]]
            parent[x]=r
        return parent[x]

    def union(a,b,w):  # b - a = w
        ra=find(a); rb=find(b)
        if ra==rb:
            return
        da=diff[a]; db=diff[b]
        if rank[ra]<rank[rb]:
            ra,rb=rb,ra
            da,db=db,da
            w=-w
        parent[rb]=ra
        diff[rb]=w+da-db
        if rank[ra]==rank[rb]:
            rank[ra]+=1

    for _ in range(M):
        s=input().split()
        if s[0]=='!':
            a=int(s[1]); b=int(s[2]); w=int(s[3])
            union(a,b,w)
        else:
            a=int(s[1]); b=int(s[2])
            ra=find(a); rb=find(b)
            if ra!=rb:
                out.append("UNKNOWN")
            else:
                out.append(str(diff[b]-diff[a]))
print("\n".join(out))
