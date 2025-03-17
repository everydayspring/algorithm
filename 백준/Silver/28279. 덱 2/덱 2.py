import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
deque_ = deque()
output = []

for i in range(1, n + 1):
    command = data[i].split()
    
    if command[0] == '1':
        deque_.appendleft(int(command[1]))
    elif command[0] == '2':
        deque_.append(int(command[1]))
    elif command[0] == '3':
        output.append(str(deque_.popleft()) if deque_ else "-1")
    elif command[0] == '4':
        output.append(str(deque_.pop()) if deque_ else "-1")
    elif command[0] == '5':
        output.append(str(len(deque_)))
    elif command[0] == '6':
        output.append("1" if not deque_ else "0")
    elif command[0] == '7':
        output.append(str(deque_[0]) if deque_ else "-1")
    elif command[0] == '8':
        output.append(str(deque_[-1]) if deque_ else "-1")

sys.stdout.write("\n".join(output) + "\n")
