import sys

N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

numbers.sort()

sys.stdout.write("\n".join(map(str, numbers)) + "\n")
