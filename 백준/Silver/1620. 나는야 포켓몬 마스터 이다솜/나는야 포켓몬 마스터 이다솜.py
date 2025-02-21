import sys

N, M = map(int, sys.stdin.readline().split())

poke_dict = {}
poke_list = []

for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    poke_dict[name] = i
    poke_list.append(name)

results = []
for _ in range(M):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        results.append(poke_list[int(query) - 1])
    else:
        results.append(str(poke_dict[query]))

sys.stdout.write("\n".join(results) + "\n")
