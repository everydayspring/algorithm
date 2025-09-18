import sys

t = int(sys.stdin.readline().strip())
if t == 1:
    a, b = map(int, sys.stdin.readline().split())
    s = a + b
    chars = []
    for _ in range(13):
        chars.append(chr(97 + (s % 26)))
        s //= 26
    print("".join(reversed(chars)))
else:
    s = sys.stdin.readline().strip()
    v = 0
    for c in s:
        v = v * 26 + (ord(c) - 97)
    print(v)
