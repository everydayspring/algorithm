import sys

N = int(sys.stdin.readline().strip())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().split()))

sys.stdout.write(" ".join("1" if q in cards else "0" for q in queries) + "\n")
