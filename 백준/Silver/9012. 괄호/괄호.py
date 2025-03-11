import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    ps = sys.stdin.readline().strip()
    stack = []
    is_vps = True

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
