import sys
input = sys.stdin.read

n, m, *arr = map(int, input().split())
prefix = [0] * (n + 1)
count = [0] * m
answer = 0

for i in range(1, n + 1):
    prefix[i] = (prefix[i - 1] + arr[i - 1]) % m
    count[prefix[i]] += 1

answer += count[0]

for c in count:
    answer += c * (c - 1) // 2

print(answer)
