lines = [input() for _ in range(5)]

max_length = max(len(line) for line in lines)

result = []
for i in range(max_length):
    for line in lines:
        if i < len(line):
            result.append(line[i])

print("".join(result))
