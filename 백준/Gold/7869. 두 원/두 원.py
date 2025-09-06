import sys, math

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.read().split())
dx, dy = x2 - x1, y2 - y1
d = math.hypot(dx, dy)

if d >= r1 + r2:
    area = 0.0
elif d <= abs(r1 - r2) or d == 0.0:
    area = math.pi * min(r1, r2) ** 2
else:
    a1 = (d*d + r1*r1 - r2*r2) / (2*d*r1)
    a2 = (d*d + r2*r2 - r1*r1) / (2*d*r2)
    a1 = max(-1.0, min(1.0, a1))
    a2 = max(-1.0, min(1.0, a2))
    th1 = math.acos(a1)
    th2 = math.acos(a2)
    area = r1*r1*th1 + r2*r2*th2 - 0.5*math.sqrt(max(0.0, (-d+r1+r2)*(d+r1-r2)*(d-r1+r2)*(d+r1+r2)))

print(f"{area:.3f}")
