import sys

def read_int():
    while True:
        s = sys.stdin.readline()
        if not s:
            sys.exit(0)
        s = s.strip()
        if s:
            return int(s)

def ask(arr, idx, cache, N):
    if idx < 1 or idx > N:
        return None
    if idx in cache:
        return cache[idx]
    print(f"? {arr} {idx}", flush=True)
    val = read_int()
    cache[idx] = val
    return val

N = read_int()
cacheA, cacheB = {}, {}

l1, r1 = 1, N
l2, r2 = 1, N
k = N

while True:
    if l1 > r1:
        ans = ask("B", l2 + k - 1, cacheB, N)
        print(f"! {ans}", flush=True)
        sys.exit(0)
    if l2 > r2:
        ans = ask("A", l1 + k - 1, cacheA, N)
        print(f"! {ans}", flush=True)
        sys.exit(0)
    if k == 1:
        a1 = ask("A", l1, cacheA, N)
        b1 = ask("B", l2, cacheB, N)
        print(f"! {a1 if a1 <= b1 else b1}", flush=True)
        sys.exit(0)

    n1 = r1 - l1 + 1
    n2 = r2 - l2 + 1
    i = k // 2
    if i > n1:
        i = n1
    j = k - i
    if j > n2:
        j = n2
        i = k - j

    ai = ask("A", l1 + i - 1, cacheA, N)
    bj = ask("B", l2 + j - 1, cacheB, N)

    if ai <= bj:
        l1 += i
        k -= i
    else:
        l2 += j
        k -= j
