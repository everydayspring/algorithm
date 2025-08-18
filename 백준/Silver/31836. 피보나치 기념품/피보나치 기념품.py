import sys
input=sys.stdin.readline

N=int(input())
fib=[0]*(N+1)
if N>=1: fib[1]=1
if N>=2: fib[2]=1
for i in range(3,N+1):
    fib[i]=fib[i-1]+fib[i-2]

S=sum(fib[1:])
ban=set()
if S%2==1:
    ban.add(1)
    S-=fib[1]

T=S//2
A=[]
for i in range(N,0,-1):
    if i in ban: continue
    if fib[i]<=T:
        A.append(i)
        T-=fib[i]
    if T==0: break

Aset=set(A)
B=[i for i in range(1,N+1) if i not in ban and i not in Aset]
A.sort()

print(len(A))
print(*A)
print(len(B))
print(*B)
