import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(n)]
filtered = [w for w in words if len(w) >= m]
counted = Counter(filtered)

sorted_words = sorted(counted.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)
