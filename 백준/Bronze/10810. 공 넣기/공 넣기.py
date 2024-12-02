N, M = map(int, input().split())

baskets = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())

    for idx in range(i, j + 1):
        baskets[idx] = k

print(*baskets[1:])
