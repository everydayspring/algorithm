import sys

N = int(sys.stdin.readline().strip())
members = [sys.stdin.readline().split() for _ in range(N)]

members = [(int(age), name) for age, name in members]
members.sort(key=lambda x: x[0])

sys.stdout.write("\n".join(f"{age} {name}" for age, name in members) + "\n")
