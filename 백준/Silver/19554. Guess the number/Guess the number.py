import sys

def read_int():
    while True:
        s = sys.stdin.readline()
        if not s:
            sys.exit(0)
        s = s.strip()
        if s:
            try:
                return int(s)
            except:
                continue

N = read_int()
l, r = 1, N
while l <= r:
    m = (l + r) // 2
    print(f"? {m}", flush=True)
    resp = read_int()
    if resp == 0:
        print(f"= {m}", flush=True)
        sys.exit(0)
    elif resp == -1:
        l = m + 1
    else:
        r = m - 1
