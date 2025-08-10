import sys
n=int(sys.stdin.readline())
if n<2:
    print(0)
    sys.exit(0)
sieve=bytearray(b'\x01')*(n+1)
sieve[0:2]=b'\x00\x00'
m=int(n**0.5)
for i in range(2,m+1):
    if sieve[i]:
        sieve[i*i:n+1:i]=b'\x00'*(((n-i*i)//i)+1)
primes=[i for i in range(2,n+1) if sieve[i]]
l=r=s=cnt=0
while True:
    if s>=n:
        if s==n: cnt+=1
        s-=primes[l]; l+=1
    else:
        if r==len(primes): break
        s+=primes[r]; r+=1
print(cnt)
