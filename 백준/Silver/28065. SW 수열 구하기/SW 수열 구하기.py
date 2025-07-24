n = int(input())
a, b = 1, n
ans = []
for i in range(n):
    if i % 2 == 0:
        ans.append(b)
        b -= 1
    else:
        ans.append(a)
        a += 1
print(*ans)
