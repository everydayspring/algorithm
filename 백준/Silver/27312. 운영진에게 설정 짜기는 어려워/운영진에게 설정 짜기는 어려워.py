import sys

def read_int():
    s = sys.stdin.readline()
    if not s:
        sys.exit(0)
    s = s.strip()
    if not s:
        return read_int()
    return int(s)

M, N, Q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
p = [1]*N

for k in range(1, M+1):
    print(f"? {k} {k}", flush=True)
    x = read_int()
    ak = a[k-1]
    y = x % ak + 1
    if y == x:
        y = 1 if x != 1 else 2
    p[k-1] = y

print("! " + " ".join(map(str, p)), flush=True)
sys.exit(0)
