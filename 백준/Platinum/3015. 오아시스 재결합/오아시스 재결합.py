import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0

for _ in range(n):
    height = int(input())
    count = 1

    while stack and stack[-1][0] <= height:
        h, c = stack.pop()
        result += c
        if h == height:
            count += c

    if stack:
        result += 1

    stack.append((height, count))

print(result)
