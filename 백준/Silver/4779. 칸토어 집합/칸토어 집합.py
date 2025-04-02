import sys

def cantor(s, e):
    if e - s < 3:
        return
    third = (e - s) // 3
    for i in range(s + third, s + 2 * third):
        line[i] = ' '
    cantor(s, s + third)
    cantor(s + 2 * third, e)

for line_input in sys.stdin:
    n = int(line_input)
    length = 3 ** n
    line = ['-'] * length
    cantor(0, length)
    print(''.join(line))
