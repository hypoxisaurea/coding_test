n = int(input())

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(f"{n - i + 1} * {j} = {(n - i + 1) * j}", end='')

        if j != i:
            print(' / ', end='')

    print()