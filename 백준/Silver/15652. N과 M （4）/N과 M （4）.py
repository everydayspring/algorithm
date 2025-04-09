n, m = map(int, input().split())
result = []

def backtrack(start, path):
    if len(path) == m:
        print(*path)
        return
    for i in range(start, n + 1):
        backtrack(i, path + [i])

backtrack(1, [])
