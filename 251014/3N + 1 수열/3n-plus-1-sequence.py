n = int(input())
count = 0

while True:
    if n == 1:
        break
    
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

    count += 1


print(count)