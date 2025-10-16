n = int(input())
count = 65

for i in range(1, n + 1):
    for j in range(i):
        if chr(count) > 'Z':
            count = 65

        print(chr(count), end='')
        count += 1

    print()