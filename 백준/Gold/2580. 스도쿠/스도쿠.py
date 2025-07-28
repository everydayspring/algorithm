import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        n = board[i][j]
        if n == 0:
            zeros.append((i, j))
        else:
            rows[i].add(n)
            cols[j].add(n)
            boxes[(i // 3) * 3 + (j // 3)].add(n)

def solve(idx):
    if idx == len(zeros):
        print('\n'.join(' '.join(map(str, row)) for row in board))
        sys.exit(0)
    x, y = zeros[idx]
    box_idx = (x // 3) * 3 + (y // 3)
    for num in range(1, 10):
        if num not in rows[x] and num not in cols[y] and num not in boxes[box_idx]:
            board[x][y] = num
            rows[x].add(num)
            cols[y].add(num)
            boxes[box_idx].add(num)
            solve(idx + 1)
            board[x][y] = 0
            rows[x].remove(num)
            cols[y].remove(num)
            boxes[box_idx].remove(num)

solve(0)
