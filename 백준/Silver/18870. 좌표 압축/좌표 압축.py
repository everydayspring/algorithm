import sys

N = int(sys.stdin.readline().strip())
coords = list(map(int, sys.stdin.readline().split()))

sorted_unique = sorted(set(coords))
index_map = {value: idx for idx, value in enumerate(sorted_unique)}

sys.stdout.write(" ".join(str(index_map[x]) for x in coords) + "\n")
