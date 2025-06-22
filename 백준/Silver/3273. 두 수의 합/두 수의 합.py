n = int(input())
arr = list(map(int, input().split()))
x = int(input())

visited = [False] * 2000001
count = 0

for num in arr:
    if x - num > 0 and visited[x - num]:
        count += 1
    visited[num] = True

print(count)
