import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
a = set(map(int, data[1:n+1]))
m = int(data[n+1])
queries = map(int, data[n+2:])

for x in queries:
    print(1 if x in a else 0)
