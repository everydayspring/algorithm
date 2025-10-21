import sys

def egcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=egcd(b,a%b)
    return g,y1,x1-(a//b)*y1

N,A=map(int,sys.stdin.readline().split())
add_inv=(N-A)%N
g,x,_=egcd(A,N)
mul_inv=-1
if g==1:
    mul_inv=x%N
print(add_inv,mul_inv)
