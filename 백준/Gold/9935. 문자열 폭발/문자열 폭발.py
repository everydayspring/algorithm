import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
stack = []
l = len(bomb)

for c in s:
    stack.append(c)
    if ''.join(stack[-l:]) == bomb:
        del stack[-l:]

print(''.join(stack) if stack else "FRULA")
