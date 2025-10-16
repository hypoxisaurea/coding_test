n = int(input())
count = 0

for _ in range(n):
    for _ in range(n):
        if count < 10:
            count += 2
        if count >= 10:
            count = 2

        print(count, end=' ')

    print()