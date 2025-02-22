import sys

N, M = map(int, sys.stdin.readline().split())

not_heard = set(sys.stdin.readline().strip() for _ in range(N))
not_seen = set(sys.stdin.readline().strip() for _ in range(M))

not_heard_seen = sorted(not_heard & not_seen)

sys.stdout.write(f"{len(not_heard_seen)}\n" + "\n".join(not_heard_seen) + "\n")
