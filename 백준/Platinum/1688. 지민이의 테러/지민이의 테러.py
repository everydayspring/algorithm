import sys

def on_segment(ax, ay, bx, by, px, py):
    return (ax - px) * (by - py) == (ay - py) * (bx - px) and min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by)

def point_in_polygon(poly, px, py):
    cnt = 0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if on_segment(x1, y1, x2, y2, px, py):
            return True
        if y1 == y2:
            continue
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if y1 <= py < y2:
            lhs = (x2 - x1) * (py - y1)
            rhs = (px - x1) * (y2 - y1)
            if lhs > rhs:
                cnt ^= 1
    return cnt == 1

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    poly = [(int(next(it)), int(next(it))) for _ in range(N)]
    queries = [(int(next(it)), int(next(it))) for _ in range(3)]
    out = []
    for x, y in queries:
        out.append('1' if point_in_polygon(poly, x, y) else '0')
    print('\n'.join(out))

if __name__ == "__main__":
    main()
