N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for i in range(len(numbers)):    
    if numbers[i] < X:
        print(numbers[i], end = ' ')