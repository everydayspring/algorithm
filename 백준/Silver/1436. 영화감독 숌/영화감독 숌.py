N = int(input())
count, num = 0, 666

while True:
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1
