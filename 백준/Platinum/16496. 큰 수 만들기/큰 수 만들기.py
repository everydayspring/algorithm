import sys
from functools import cmp_to_key

input=sys.stdin.readline
n=int(input().strip())
arr=input().split()
def cmp(x,y):
    if x+y>y+x: return -1
    if x+y<y+x: return 1
    return 0
arr.sort(key=cmp_to_key(cmp))
if arr[0]=="0":
    print("0")
else:
    print("".join(arr))
