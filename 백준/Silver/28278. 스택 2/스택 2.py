import sys

N = int(sys.stdin.readline().strip())
stack = []
output = []

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        output.append(str(stack.pop() if stack else -1))
    elif command[0] == '3':
        output.append(str(len(stack)))
    elif command[0] == '4':
        output.append(str(1 if not stack else 0))
    elif command[0] == '5':
        output.append(str(stack[-1] if stack else -1))

sys.stdout.write("\n".join(output) + "\n")
