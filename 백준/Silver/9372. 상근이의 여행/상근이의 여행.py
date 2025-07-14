import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    res = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2 + 2 * m
        res.append(str(n - 1))
    print('\n'.join(res))

main()
