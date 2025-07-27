n = int(input())
ans = 0
col = [False] * n
diag1 = [False] * (2 * n)
diag2 = [False] * (2 * n)

def dfs(r):
    global ans
    if r == n:
        ans += 1
        return
    for c in range(n):
        if not col[c] and not diag1[r + c] and not diag2[r - c + n]:
            col[c] = diag1[r + c] = diag2[r - c + n] = True
            dfs(r + 1)
            col[c] = diag1[r + c] = diag2[r - c + n] = False

dfs(0)
print(ans)
