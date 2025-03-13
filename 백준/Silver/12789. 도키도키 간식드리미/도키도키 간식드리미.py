import sys

n = int(sys.stdin.readline().strip())
queue = list(map(int, sys.stdin.readline().split()))

stack = []
current = 1

for num in queue:
    while stack and stack[-1] == current:
        stack.pop()
        current += 1
    if num == current:
        current += 1
    else:
        stack.append(num)

while stack and stack[-1] == current:
    stack.pop()
    current += 1

print("Nice" if not stack else "Sad")
