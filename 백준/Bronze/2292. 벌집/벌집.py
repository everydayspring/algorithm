N = int(input())
layer, count = 1, 1

while N > layer:
    layer += 6 * count
    count += 1

print(count)
