import sys
sys.setrecursionlimit(1 << 25)

data=list(map(int,sys.stdin.buffer.read().split()))
n=data[0]
a=data[1:]
tmp=[0]*n

def sort_count(l,r):
    if r-l<=1:
        return 0
    m=(l+r)//2
    cnt=sort_count(l,m)+sort_count(m,r)
    i=l;j=m;k=l
    while i<m and j<r:
        if a[i]<=a[j]:
            tmp[k]=a[i]; i+=1
        else:
            tmp[k]=a[j]; j+=1
            cnt+=m-i
        k+=1
    while i<m:
        tmp[k]=a[i]; i+=1; k+=1
    while j<r:
        tmp[k]=a[j]; j+=1; k+=1
    a[l:r]=tmp[l:r]
    return cnt

print(sort_count(0,n))
