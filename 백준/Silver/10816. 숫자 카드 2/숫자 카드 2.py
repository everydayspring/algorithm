import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().split()))

card_counts = Counter(cards)

sys.stdout.write(" ".join(str(card_counts[q]) if q in card_counts else "0" for q in queries) + "\n")
