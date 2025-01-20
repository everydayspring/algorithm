x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

x4 = x_coords[0] if x_coords.count(x_coords[0]) == 1 else x_coords[1] if x_coords.count(x_coords[1]) == 1 else x_coords[2]
y4 = y_coords[0] if y_coords.count(y_coords[0]) == 1 else y_coords[1] if y_coords.count(y_coords[1]) == 1 else y_coords[2]

print(x4, y4)
