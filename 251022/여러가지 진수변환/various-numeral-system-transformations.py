N, B = map(int, input().split())
digits = []

while True:
    if N < 2:
        digits.append(N)
        break

    digits.append(N % B)
    N //= B

if digits[-1] == 0:
    digits.pop(-1)

for digit in digits[::-1]:
    print(digit, end='')