n = int(input())
count = 10

for _ in range(n):
    for _ in range(n):
        count -= 1

        if count == 0:
            count = 9

        print(count, end='')
    print()