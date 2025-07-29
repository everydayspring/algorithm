import sys
from itertools import combinations

input = sys.stdin.read
data = input().split()

n = int(data[0])
s = []
idx = 1
for i in range(n):
    s.append(list(map(int, data[idx:idx+n])))
    idx += n

players = list(range(n))
min_diff = float('inf')

for team in combinations(players, n // 2):
    start_team = set(team)
    link_team = set(players) - start_team

    start_sum = 0
    link_sum = 0

    for i in start_team:
        for j in start_team:
            if i != j:
                start_sum += s[i][j]

    for i in link_team:
        for j in link_team:
            if i != j:
                link_sum += s[i][j]

    min_diff = min(min_diff, abs(start_sum - link_sum))
    if min_diff == 0:
        break

print(min_diff)
