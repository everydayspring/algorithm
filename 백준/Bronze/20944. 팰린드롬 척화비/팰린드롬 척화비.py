n = int(input())
half = n // 2
prefix = 'a' * half
if n % 2 == 0:
    print(prefix + prefix)
else:
    print(prefix + 'a' + prefix)
