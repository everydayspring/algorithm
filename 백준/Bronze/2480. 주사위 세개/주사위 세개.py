numbers = input().split()

if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
    print(10000 + (int(numbers[0]) * 1000)) 
elif numbers[0] == numbers[1] or numbers[0] == numbers[2]:
    print(1000 + (int(numbers[0]) * 100)) 
elif numbers[1] == numbers[2]:
    print(1000 + (int(numbers[1]) * 100)) 
else:
    print(int(max(numbers)) * 100)