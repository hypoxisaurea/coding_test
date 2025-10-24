n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print((i * n) + j + 1, end=' ')
        else:
            print((i * n) + n - j, end=' ')

    print()