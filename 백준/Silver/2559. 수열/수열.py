n, k = map(int, input().split())
arr = list(map(int, input().split()))
current_sum = sum(arr[:k])
max_sum = current_sum
for i in range(k, n):
    current_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, current_sum)
print(max_sum)
