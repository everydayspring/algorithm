S = input()

result = [S.find(chr(c)) for c in range(ord('a'), ord('z') + 1)]

print(*result)