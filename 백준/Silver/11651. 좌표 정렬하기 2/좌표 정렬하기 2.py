import sys

N = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

points.sort(key=lambda p: (p[1], p[0]))

sys.stdout.write("\n".join(f"{x} {y}" for x, y in points) + "\n")
