import sys

for a in range(1, 10):
    print("? A", a, flush=True)
    if int(sys.stdin.readline()) == 1:
        A = a
        break

for b in range(1, 10):
    print("? B", b, flush=True)
    if int(sys.stdin.readline()) == 1:
        B = b
        break

print("!", A + B, flush=True)
