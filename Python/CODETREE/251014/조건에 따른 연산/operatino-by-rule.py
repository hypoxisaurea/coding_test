n = int(input())
count = 0

while True:
    if n >= 1000:
        break

    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = n * 2 + 2

    count += 1

print(count)