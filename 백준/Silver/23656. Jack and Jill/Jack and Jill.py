import sys

L, R = 1, 10**9
step = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    try:
        x = int(line)
    except:
        break
    step += 1
    if x < L:
        print(">", flush=True)
    elif x > R:
        print("<", flush=True)
    else:
        if L == R:
            if step >= 30:
                print("=", flush=True)
                sys.exit(0)
            else:
                if x == L:
                    print("<", flush=True)
                    R = x - 1
                else:
                    print(">", flush=True)
                    L = x + 1
        else:
            left_size = x - L
            right_size = R - x
            if step >= 30 and (L == x and left_size == 0 and right_size == 0):
                print("=", flush=True)
                sys.exit(0)
            if right_size >= left_size:
                print(">", flush=True)
                L = x + 1
            else:
                print("<", flush=True)
                R = x - 1
