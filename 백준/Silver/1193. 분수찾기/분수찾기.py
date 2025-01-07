X = int(input())
line, total = 1, 0

while total < X:
    total += line
    line += 1

line -= 1
offset = X - (total - line)

if line % 2 == 0:
    numerator = offset
    denominator = line - offset + 1
else:
    numerator = line - offset + 1
    denominator = offset

print(f"{numerator}/{denominator}")
