a, b, c = map(int, input().split())
sides = sorted([a, b, c])

if sides[0] + sides[1] > sides[2]:
    print(sum(sides))
else:
    print(2 * (sides[0] + sides[1]) - 1)
