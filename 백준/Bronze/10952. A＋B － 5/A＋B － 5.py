A, B = map(int, input().split())

result = ""

while A != 0 and B != 0:
    result += f"{A + B}\n"
    A, B = map(int, input().split())
    
print(result)