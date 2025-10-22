N = list(map(int, input()))
length = len(N)
number = 0

for i in range(length):
    number = number * 2 + N[i]

number *= 17
digits = []

while True:
    if number < 2:
        digits.append(number)
        break

    digits.append(number % 2)
    number //= 2


for digit in digits[::-1]:
    print(digit, end='')