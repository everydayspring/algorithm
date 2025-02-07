N = int(input())
bags = 0

while N >= 0:
    if N % 5 == 0:
        bags += N // 5
        print(bags)
        break
    N -= 3
    bags += 1
else:
    print(-1)
