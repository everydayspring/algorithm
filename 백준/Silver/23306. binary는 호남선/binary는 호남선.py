import sys

def ask(k):
    print(f"? {k}")
    sys.stdout.flush()
    return int(sys.stdin.readline().strip())

n = int(sys.stdin.readline().strip())
b1 = ask(1)
bN = ask(n)
a = 1 if bN > b1 else 0 if bN == b1 else -1
print(f"! {a}")
sys.stdout.flush()
