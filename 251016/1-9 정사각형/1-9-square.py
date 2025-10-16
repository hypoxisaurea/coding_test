n = int(input())
count = 0

for _ in range(n):
    for _ in range(n):
        count += 1

        if count == 10:
            count = 1

        print(count, end='')
        
    print()