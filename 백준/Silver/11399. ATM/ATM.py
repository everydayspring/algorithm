n = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
acc = 0
for t in times:
    acc += t
    total += acc
print(total)
