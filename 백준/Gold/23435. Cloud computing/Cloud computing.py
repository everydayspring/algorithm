import sys

def ask(i, j):
    print(f"? {i} {j}", flush=True)
    s = sys.stdin.readline().strip()
    return s == "<"

N = int(sys.stdin.readline().strip())
beaten = [[] for _ in range(N)]
cur = list(range(N))
while len(cur) > 1:
    nxt = []
    i = 0
    while i + 1 < len(cur):
        a, b = cur[i], cur[i+1]
        if ask(a, b):
            nxt.append(a)
            beaten[a].append(b)
        else:
            nxt.append(b)
            beaten[b].append(a)
        i += 2
    if i < len(cur):
        nxt.append(cur[i])
    cur = nxt

mn = cur[0]
cands = beaten[mn]
if not cands:
    print(f"! {mn}", flush=True)
    sys.exit(0)

# tournament among candidates to find the smallest => second smallest overall
cur = cands[:]
while len(cur) > 1:
    nxt = []
    i = 0
    while i + 1 < len(cur):
        a, b = cur[i], cur[i+1]
        nxt.append(a if ask(a, b) else b)
        i += 2
    if i < len(cur):
        nxt.append(cur[i])
    cur = nxt

print(f"! {cur[0]}", flush=True)
