n = int(input())
count = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            count += 1
            print(count, end=' ')
    else:
        for j in range(n):
            count += 2
            print(count, end=' ')

    print()