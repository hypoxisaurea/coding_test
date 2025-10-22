a, b = map(int, input().split())
n = list(map(int, input()))
length = len(n)

number = 0
for i in range(length):
    number = number * a + n[i]

digits = []
while True:
    if number < b:
        digits.append(number)
        break
    
    digits.append(number % b)
    number //= b

for digit in digits[::-1]:
    print(digit, end='')