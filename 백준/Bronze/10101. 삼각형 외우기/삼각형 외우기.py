angles = [int(input()) for _ in range(3)]

if sum(angles) != 180:
    print("Error")
elif angles[0] == angles[1] == angles[2] == 60:
    print("Equilateral")
elif len(set(angles)) == 2:
    print("Isosceles")
else:
    print("Scalene")
