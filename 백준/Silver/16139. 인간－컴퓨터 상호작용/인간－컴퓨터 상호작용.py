import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

S = input().strip()
q = int(input())
pos = [[] for _ in range(26)]
for i, ch in enumerate(S):
    pos[ord(ch) - 97].append(i)

out = []
for _ in range(q):
    a, l, r = input().split()
    l = int(l); r = int(r)
    arr = pos[ord(a) - 97]
    out.append(str(bisect_right(arr, r) - bisect_left(arr, l)))
print('\n'.join(out))
