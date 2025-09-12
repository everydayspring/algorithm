import sys
from collections import deque

input=sys.stdin.readline
N=int(input())
M=int(input())
adj=[[] for _ in range(N+1)]
ind=[0]*(N+1)
for _ in range(M):
    X,Y,K=map(int,input().split())
    adj[Y].append((X,K))
    ind[X]+=1

need=[[0]*(N+1) for _ in range(N+1)]
q=deque()
for i in range(1,N+1):
    if ind[i]==0:
        need[i][i]=1
        q.append(i)

while q:
    cur=q.popleft()
    for nxt,k in adj[cur]:
        for i in range(1,N+1):
            if need[cur][i]:
                need[nxt][i]+=need[cur][i]*k
        ind[nxt]-=1
        if ind[nxt]==0:
            q.append(nxt)

for i in range(1,N+1):
    if need[N][i]:
        print(i,need[N][i])
