import sys

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    v = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

o1 = ccw(a, b, c)
o2 = ccw(a, b, d)
o3 = ccw(c, d, a)
o4 = ccw(c, d, b)

print(1 if o1 * o2 <= 0 and o3 * o4 <= 0 else 0)
