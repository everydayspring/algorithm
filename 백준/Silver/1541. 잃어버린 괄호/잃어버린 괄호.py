expression = input().split('-')
result = sum(map(int, expression[0].split('+')))
for part in expression[1:]:
    result -= sum(map(int, part.split('+')))
print(result)
