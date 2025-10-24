import math

n = int(input())
x = 0

while True:
    if n == pow(2, x):
        break

    x += 1

print(x)