import sys
input = sys.stdin.readline

def compress(x, y, size):
    first = board[x][y]
    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != first:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        return first
    half = size // 2
    return "(" + \
           compress(x, y, half) + \
           compress(x, y + half, half) + \
           compress(x + half, y, half) + \
           compress(x + half, y + half, half) + \
           ")"

N = int(input())
board = [list(input().strip()) for _ in range(N)]
print(compress(0, 0, N))
