import sys

N = int(sys.stdin.readline().strip())
words = set(sys.stdin.read().split())

sorted_words = sorted(words, key=lambda x: (len(x), x))

sys.stdout.write("\n".join(sorted_words) + "\n")
