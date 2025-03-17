from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
balloons = list(map(int, data[1].split()))
queue = deque(enumerate(balloons, start=1))
result = []

while queue:
    index, move = queue.popleft()
    result.append(str(index))

    if queue:
        if move > 0:
            queue.rotate(-(move - 1))
        else:
            queue.rotate(-move)

sys.stdout.write(" ".join(result) + "\n")
