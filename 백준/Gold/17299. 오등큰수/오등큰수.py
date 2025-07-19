import sys
from collections import Counter

input = sys.stdin.read
n, *arr = map(int, input().split())

count = Counter(arr)
stack = []
result = [-1] * n

for i in range(n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
