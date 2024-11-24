cnt = int(input())
str = ""

for i in range(cnt):
    num1, num2 = map(int, input().split())
    str += f"Case #{i + 1}: {num1} + {num2} = {num1 + num2}\n"

print(str)