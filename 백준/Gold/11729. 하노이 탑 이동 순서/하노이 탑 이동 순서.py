def hanoi(n, start, end, temp, moves):
    if n == 1:
        moves.append((start, end))
    else:
        hanoi(n - 1, start, temp, end, moves)
        moves.append((start, end))
        hanoi(n - 1, temp, end, start, moves)

n = int(input())
moves = []
hanoi(n, 1, 3, 2, moves)
print(len(moves))
for a, b in moves:
    print(a, b)
