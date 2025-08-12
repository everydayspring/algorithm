from bisect import bisect_right

def dfs(arr, idx, end, total, res, limit):
    if total > limit:
        return
    if idx == end:
        res.append(total)
        return
    dfs(arr, idx + 1, end, total, res, limit)
    dfs(arr, idx + 1, end, total + arr[idx], res, limit)

n, c = map(int, input().split())
items = list(map(int, input().split()))

mid = n // 2
left, right = [], []
dfs(items, 0, mid, 0, left, c)
dfs(items, mid, n, 0, right, c)

left.sort()
right.sort()

ans = 0
for v in left:
    ans += bisect_right(right, c - v)

print(ans)
