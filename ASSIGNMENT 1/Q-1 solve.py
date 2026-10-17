number = input().split()
num1 = []
num2 = []

for i in number:
    num1.append(int(i))

for i in num1:
    if i % 4 == 0 and i % 8 != 0:
        num2.append(i)

print(num2)