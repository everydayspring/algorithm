num1, num2, num3 = map(int, input().split())

print((num1 + num2) % num3)
print((num1 % num3 + num2 % num3) % num3)
print((num1 * num2) % num3)
print((num1 % num3 * num2 % num3) % num3)