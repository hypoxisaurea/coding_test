binary = list(map(int, list(input())))
length = len(binary)
number = 0

for i in range(length):
    number = number * 2 + binary[i]

print(number)