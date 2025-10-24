import math

a, b = input().split()

a = ord(a)
b = ord(b)

if a > b:
    minus = a - b
else:
    minus = b - a

print(a+b, minus)