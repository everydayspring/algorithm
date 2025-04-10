n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)

def dfs(i, result, add, sub, mul, div):
    global max_result, min_result
    if i == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if add:
        dfs(i + 1, result + nums[i], add - 1, sub, mul, div)
    if sub:
        dfs(i + 1, result - nums[i], add, sub - 1, mul, div)
    if mul:
        dfs(i + 1, result * nums[i], add, sub, mul - 1, div)
    if div:
        if result < 0:
            dfs(i + 1, -(-result // nums[i]), add, sub, mul, div - 1)
        else:
            dfs(i + 1, result // nums[i], add, sub, mul, div - 1)

dfs(1, nums[0], add, sub, mul, div)
print(max_result)
print(min_result)
