import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

def ccw(a, b, c):
    v = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return 1 if v > 0 else (-1 if v < 0 else 0)

ab = ccw(p1, p2, p3) * ccw(p1, p2, p4)
cd = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if ab == 0 and cd == 0:
    if p1 > p2:
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3
    print(1 if not (p2 < p3 or p4 < p1) else 0)
else:
    print(1 if ab <= 0 and cd <= 0 else 0)
