a = input()
b = input()

num1 = ''
num2 = ''

for i in range(len(a)):
    if a[i].isdigit() == True:
        num1 += a[i]

for i in range(len(b)):
    if b[i].isdigit() == True:
        num2 += b[i]

print(int(num1) + int(num2))