import sys

it = iter(sys.stdin.buffer.read().split())
n = int(next(it)); m = int(next(it)); k = int(next(it))
MOD = 1_000_000_007

bit_prod = [1] * (n + 1)
bit_zero = [0] * (n + 1)
arr = [0] * (n + 1)

def mul_update(i, v):
    while i <= n:
        bit_prod[i] = (bit_prod[i] * v) % MOD
        i += i & -i

def mul_prefix(i):
    res = 1
    while i > 0:
        res = (res * bit_prod[i]) % MOD
        i -= i & -i
    return res

def zero_add(i, d):
    while i <= n:
        bit_zero[i] += d
        i += i & -i

def zero_prefix(i):
    s = 0
    while i > 0:
        s += bit_zero[i]
        i -= i & -i
    return s

for i in range(1, n + 1):
    x = int(next(it))
    arr[i] = x
    if x == 0:
        zero_add(i, 1)
    else:
        mul_update(i, x % MOD)

out = []
for _ in range(m + k):
    a = int(next(it)); b = int(next(it)); c = int(next(it))
    if a == 1:
        old = arr[b]
        new = c
        if old == 0 and new == 0:
            pass
        elif old == 0 and new != 0:
            zero_add(b, -1)
            mul_update(b, new % MOD)
        elif old != 0 and new == 0:
            zero_add(b, 1)
            inv_old = pow(old % MOD, MOD - 2, MOD)
            mul_update(b, inv_old)
        else:
            inv_old = pow(old % MOD, MOD - 2, MOD)
            mul_update(b, (new % MOD) * inv_old % MOD)
        arr[b] = new
    else:
        l, r = (b, c) if b <= c else (c, b)
        if zero_prefix(r) - zero_prefix(l - 1) > 0:
            out.append("0")
        else:
            pr = mul_prefix(r)
            pl = mul_prefix(l - 1)
            ans = pr * pow(pl, MOD - 2, MOD) % MOD
            out.append(str(ans))

sys.stdout.write("\n".join(out))
