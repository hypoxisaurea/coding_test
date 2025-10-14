n = int(input())
count = 0

for i in range(1, 10):
    count += 1

    if n // i <= 1:
        break
        
    n //= i

print(count)