from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

best_sum = 0
for combo in combinations(cards, 3):
    current_sum = sum(combo)
    if best_sum < current_sum <= M:
        best_sum = current_sum

print(best_sum)
