import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

q = deque()
for i in range(n):
    if a[i] == 0:
        q.append(b[i])

for x in c:
    q.appendleft(x)
    print(q.pop(), end=' ')
