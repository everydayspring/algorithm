n = int(input())
count = 0
users = set()

for _ in range(n):
    line = input()
    if line == "ENTER":
        users.clear()
    else:
        if line not in users:
            users.add(line)
            count += 1

print(count)
