N, M = map(int, input().split())
board = [input() for _ in range(N)]

def repaint_count(x, y, first_color):
    count = 0
    for i in range(8):
        for j in range(8):
            expected_color = 'W' if (i + j) % 2 == 0 else 'B'
            if first_color == 'B':
                expected_color = 'B' if (i + j) % 2 == 0 else 'W'
            if board[x + i][y + j] != expected_color:
                count += 1
    return count

min_repaint = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        min_repaint = min(min_repaint, repaint_count(i, j, 'W'), repaint_count(i, j, 'B'))

print(min_repaint)
