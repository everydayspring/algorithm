import sys
input = sys.stdin.readline

def count_paper(x, y, size):
    first = board[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != first:
                same = False
                break
        if not same:
            break
    if same:
        counts[first + 1] += 1
        return
    new_size = size // 3
    for dx in range(3):
        for dy in range(3):
            count_paper(x + dx * new_size, y + dy * new_size, new_size)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
counts = [0, 0, 0]

count_paper(0, 0, N)

print(counts[0])
print(counts[1])
print(counts[2])
