import sys, math
from itertools import permutations

a = list(map(int, sys.stdin.read().split()))
angles = [i * math.pi / 4 for i in range(8)]
dirs = [(math.cos(t), math.sin(t)) for t in angles]
eps = 1e-12

def is_convex(vals):
    pts = [(vals[i] * dirs[i][0], vals[i] * dirs[i][1]) for i in range(8)]
    signs_pos = signs_neg = False
    for i in range(8):
        A = pts[i]
        B = pts[(i + 1) % 8]
        C = pts[(i + 2) % 8]
        x1, y1 = B[0] - A[0], B[1] - A[1]
        x2, y2 = C[0] - B[0], C[1] - B[1]
        z = x1 * y2 - y1 * x2
        if z > eps:
            signs_pos = True
        elif z < -eps:
            signs_neg = True
        if signs_pos and signs_neg:
            return False
    return True

cnt = 0
for p in permutations(a):
    if is_convex(p):
        cnt += 1

print(cnt)
