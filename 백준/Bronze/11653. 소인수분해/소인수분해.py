N = int(input())

factor = 2
while N > 1:
    while N % factor == 0:
        print(factor)
        N //= factor
    factor += 1
