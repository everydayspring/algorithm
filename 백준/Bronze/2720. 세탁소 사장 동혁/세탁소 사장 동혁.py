T = int(input())
coin_values = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    result = []
    for coin in coin_values:
        result.append(C // coin)
        C %= coin
    print(*result)
